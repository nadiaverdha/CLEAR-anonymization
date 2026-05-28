# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-05-28T09:09:47.996090

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-05-26_v1/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 678 |
| Validation documents | 171 |
| Test documents | 476 |
| Train sentences | 2189 |
| Validation sentences | 563 |
| Test sentences | 21234 |
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
| Accuracy (exact match) | 97.7% |
| True Positives | 292 |
| False Positives | 315 |
| False Negatives | 407 |
| Total Gold Entities | 699 |
| Micro Precision | 48.1% |
| Micro Recall | 41.8% |
| Micro F1 | 44.7% |
| Macro F1 | 44.7% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Administrative Court` | 1.7% | 100.0% | 0.9% | 6 | 6 | 0 |
| `Vienna Magistrate` | 2.0% | 100.0% | 1.0% | 7 | 7 | 0 |
| `Constitutional Court` | 2.3% | 100.0% | 1.1% | 8 | 8 | 0 |
| `Labor Court Vienna` | 9.3% | 100.0% | 4.9% | 34 | 34 | 0 |
| `Court with Location` | 5.0% | 100.0% | 2.6% | 18 | 18 | 0 |
| `Pensionsversicherungsanstalt` | 0.3% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Verwaltungsgerichtshof Genitive` | 1.4% | 100.0% | 0.7% | 5 | 5 | 0 |
| `Magistrate City Pattern` | 2.0% | 100.0% | 1.0% | 7 | 7 | 0 |
| `Federal Ministry of Justice` | 1.1% | 100.0% | 0.6% | 4 | 4 | 0 |
| `District Court Pattern` | 31.6% | 81.1% | 19.6% | 169 | 137 | 32 |
| `Regional Court Pattern` | 15.9% | 67.0% | 9.0% | 94 | 63 | 31 |
| `Bank and Other Org` | 3.9% | 66.7% | 2.0% | 21 | 14 | 7 |
| `Hyphenated Company Names` | 0.3% | 50.0% | 0.1% | 2 | 1 | 1 |
| `Generic GmbH Entity` | 5.0% | 14.5% | 3.0% | 145 | 21 | 124 |
| `Company Name Without Suffix` | 4.5% | 8.6% | 3.0% | 244 | 21 | 223 |
| `Federal Tax Court` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Tax Authority Austria` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Ministry of Finance` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Administrative Court Acronym` | 0.0% | 0.0% | 0.0% | 7 | 0 | 7 |
| `Federal Tax Court Acronym BFG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `UFS Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `University Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Social Ministry` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `AMS Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Local Tax Office` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
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
| `Tax Office Acronym FAÖ` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Constitutional Court Acronym` | 0.0% | 0.0% | 0.0% | 12 | 0 | 12 |
| `Gözcü Getränke` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bank Full Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FAÖ Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Tax Office Full Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bankhaus Denzel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Cervenka&Neunübel Telekom AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `PSD Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SVS/SVB` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Psychiatrie Otto Wagner Spital` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schweizerischen Unfallversicherungsanstalt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `ÖGK` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesamtes für Soziales und Behindertenwesen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `PSD Wien Full` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SUVA` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wiener Städtische` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Allianz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `AMS Österreich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Location` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesfinanzgericht Genitive` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Verwaltungsgericht Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FH Kärnten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Karl-Franzens-Universität Graz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BMI` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Ernst & Young` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Sozialversicherungsanstalt der Bauern` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
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
| `Law Firm GmbH/OG` | 0.0% | 0.0% | 0.0% | 10 | 0 | 10 |
| `Frontex Full Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Swiss Invalid Insurance` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Swiss Accident Insurance Full` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Kantonsspitals St. Gallen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Steueramt Kanton` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Higher Technical School` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Real Estate Office` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Austrian Society for European Politics` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BM für Finanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Retailers List` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
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
| `Limited Suffix` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Law Firm KG` | 0.0% | 0.0% | 0.0% | 10 | 0 | 10 |
| `Gesellschaft mbH Pattern` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `Labor Court Vienna`

**F1:** 0.093 | **Precision:** 1.000 | **Recall:** 0.049  

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
| 1.000 | 0.049 | 0.093 | 34 | 34 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 34 | 0 | 554 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10ObS150_17g`) (sent_id: `deanon_TRAIN/10ObS150_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Ing. Christian Stangl-Brachnik, MA BA und Mag. Claudia Gründel (beide aus dem Kreis der Arbeitgeber) als weitere Richter in der Sozialrechtssache der klagenden Partei OStR Esra Jakubait, vertreten durch Dr. Thomas Stampfer und Dr. Christoph Orgler, Rechtsanwälte in Graz, gegen die beklagte Partei Sozialversicherungsanstalt der Bauern, 1031 Wien, Ghegastraße 1, vertreten durch Dr. Michael Stögerer, Rechtsanwalt in Wien, wegen Ausgleichszulage, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2017, GZ 7 Rs 37/17s-11, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. April 2017, GZ 43 Cgs 113/17p-7, teils bestätigt und teils abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `OStR Esra Jakubait` (person)

**Example 1** (doc_id: `deanon_TRAIN/10ObS21_10a`) (sent_id: `deanon_TRAIN/10ObS21_10a_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Schinko als Vorsitzenden, die Hofräte Dr. Fellinger und Dr. Hoch sowie die fachkundigen Laienrichter Mag. Irene Kienzl (aus dem Kreis der Arbeitgeber) und Eva-Maria Florianschütz (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Gertrud Johanna Ostrovska, gegen die beklagte Partei Steiermärkische Gebietskrankenkasse, 8011 Graz, Josef-Pongratz-Platz 1, vertreten durch Das Haus des Rechts Rechtsanwälte Destaller-Mader in Graz, wegen Kostenübernahme, infolge Rekurses der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 19. November 2009, GZ 8 Rs 73/09f-10, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 1. September 2009, GZ 29 Cgs 90/09s-6, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Ostrovska` (person)

**Example 2** (doc_id: `deanon_TRAIN/10ObS21_10a`) (sent_id: `deanon_TRAIN/10ObS21_10a_133`)


Auch dieser Umstand spricht dafür, dass auch die Ablehnung der Kostenübernahme für ein verordnetes Heilmittel durch eine Feststellungsklage beim Arbeits- und Sozialgericht bekämpft werden kann.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Example 3** (doc_id: `deanon_TRAIN/10ObS49_15a`) (sent_id: `deanon_TRAIN/10ObS49_15a_4`)


Brigitte Augustin (aus dem Kreis der Arbeitgeber) und Peter Schönhofer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Samantha Neunteufl, Deutschland, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Vorarlberger Gebietskrankenkasse, Jahngasse 4, 6850 Dornbirn, vertreten durch Hoffmann & Brandstätter Rechtsanwälte KG in Innsbruck, wegen Kinderbetreuungsgeld, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 12. Februar 2015, GZ 11 Rs 4/15k-10, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 28. Oktober 2014, GZ 20 Cgs 71/14k-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Samantha Neunteufl` (person)

**Example 4** (doc_id: `deanon_TRAIN/10ObS92_17b`) (sent_id: `deanon_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Dr.in Gerlinde Saltzmann, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Dr.in Gerlinde Saltzmann` (person)
- `Pensionsversicherungsanstalt` (organisation)

**Example 5** (doc_id: `deanon_TRAIN/8Nc31_13w`) (sent_id: `deanon_TRAIN/8Nc31_13w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn als weitere Richter in der beim Landesgericht Salzburg als Arbeits- und Sozialgericht anhängigen Rechtssache der klagenden Partei Buth Analyse GmbH, Anabel Traudtmann, vertreten durch Dr. Ernst Kohlbacher, Rechtsanwalt in Salzburg, gegen die beklagte Partei Christine Schwemmer, vertreten durch Plankel Mayrhofer & Partner, Rechtsanwälte in Dornbirn, wegen 213,52 EUR sA, über den Delegierungsantrag der beklagten Partei den Beschluss gefasst:  Spruch Der Antrag der beklagten Partei, die Rechtssache an das Arbeits- und Sozialgericht Wien zu delegieren, wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |
| `Arbeits- und Sozialgericht Wien` | `Arbeits- und Sozialgericht Wien` |

**Missed by this rule (FN):**

- `Landesgericht Salzburg` (organisation)
- `Buth Analyse GmbH` (organisation)
- `Anabel Traudtmann` (person)
- `Christine Schwemmer` (person)

**Example 6** (doc_id: `deanon_TRAIN/8Nc31_13w`) (sent_id: `deanon_TRAIN/8Nc31_13w_4`)


Text Begründung: Mit der am 14. 12. 2012 beim Landesgericht Salzburg als Arbeits- und Sozialgericht eingebrachten Mahnklage begehrte die Klägerin, eine Finanzvermittlungsgesellschaft mit Sitz in Salzburg, von dem im Bundesland Burgenland wohnhaften Beklagten die Rückzahlung von Provisionen aus einem Agentenvertrag.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Landesgericht Salzburg` (organisation)

**Example 7** (doc_id: `deanon_TRAIN/8Nc31_13w`) (sent_id: `deanon_TRAIN/8Nc31_13w_6`)


Gleichzeitig beantragte er die Delegierung der Rechtssache an das Arbeits- und Sozialgericht Wien.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht Wien` | `Arbeits- und Sozialgericht Wien` |

**Example 8** (doc_id: `deanon_TRAIN/8ObA10_21k`) (sent_id: `deanon_TRAIN/8ObA10_21k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Wessely-Kristöfel als weitere Richter sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner (aus dem Kreis der Arbeitgeber) und Wolfgang Jelinek (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Thebuss + Großekemper Bildung AG, Univ.-Prof.in Anna Helffer, vertreten durch Dr. Raimund Gehart, Rechtsanwalt in Wien, gegen die beklagte Partei Paulina Strnadl, vertreten durch Dr. Franz Josef Hofer Rechtsanwalt GmbH in Friesach, wegen 5.625,88 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 10. Dezember 2020, GZ 6 Ra 69/20v-19, mit dem das Urteil des Landesgerichts Klagenfurt als Arbeits- und Sozialgericht vom 15. Mai 2020, GZ 35 Cga 90/19x-11, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Thebuss + Großekemper Bildung AG` (organisation)
- `Univ.-Prof.in Anna Helffer` (person)
- `Paulina Strnadl` (person)
- `Franz Josef Hofer Rechtsanwalt GmbH` (organisation)

**Example 9** (doc_id: `deanon_TRAIN/8ObA1_13z`) (sent_id: `deanon_TRAIN/8ObA1_13z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner sowie die fachkundigen Laienrichter Dr. Christoph Kainz und Horst Nurschinger als weitere Richter in der Arbeitsrechtssache der klagenden Partei Heinz Hennerich, vertreten durch Dr. Gerhard Hiebler, Dr. Gerd Grebenjak, Rechtsanwälte in Leoben, wider die beklagte Partei Verein DDr. Holger Müllegger, vertreten durch Dr. Dieter Neger, Rechtsanwalt in Graz, wegen Entlassungsanfechtung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Oktober 2012, GZ 6 Ra 67/12p-12, mit dem über Berufung der klagenden Partei das Urteil des Landesgerichts Leoben als Arbeits- und Sozialgericht vom 2. Juli 2012, GZ 20 Cga 23/11v-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Hennerich` (person)
- `DDr. Holger Müllegger` (person)

**Example 10** (doc_id: `deanon_TRAIN/8ObS8_22t`) (sent_id: `deanon_TRAIN/8ObS8_22t_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Stefula als weitere Richter (Senat gemäß § 11a Abs 3 Z 2 ASGG) in der Sozialrechtssache der klagenden Partei Holger Sykorski, vertreten durch Dr. Herbert Marschitz und andere Rechtsanwälte in Kufstein, gegen die beklagte Partei IEF-Service GmbH, 6020 Innsbruck, Meraner Straße 1, vertreten durch die Finanzprokuratur in Wien, wegen 34.726 EUR sA (Insolvenzentgelt), über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 18. Oktober 2022, GZ 25 Rs 56/22d-34, mit dem das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 9. Juni 2022, GZ 44 Cgs 43/21m-27, samt dem ihm vorangegangenen Verfahren für nichtig erklärt und die Klage zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Holger Sykorski` (person)

**Example 11** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Dehn und den Hofrat des Obersten Gerichtshofs Dr. Hargassner als weitere Richter in der Arbeitsrechtssache der klagenden Partei WestSicherheit GmbH, OMedR Paulina von Tietzen, vertreten durch Dr. Ernst Kohlbacher, Rechtsanwalt in Salzburg, gegen die beklagte Partei Amber Landscheid, vertreten durch Dr. Karl-Heinz Plankel, Dr. Herwig Mayrhofer ua, Rechtsanwälte in Dornbirn, wegen 15.600 EUR sA, über den Delegierungsantrag der beklagten Partei den Beschluss gefasst:  Spruch Der Antrag der beklagten Partei, anstelle des Landesgerichts Salzburg als Arbeits- und Sozialgericht das Arbeits- und Sozialgericht Wien zur Verhandlung und Entscheidung der Rechtssache des Landesgerichts Salzburg als Arbeits- und Sozialgericht AZ 15 Cga 88/15d zu bestimmen, wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |
| `Arbeits- und Sozialgericht Wien` | `Arbeits- und Sozialgericht Wien` |
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `WestSicherheit GmbH` (organisation)
- `OMedR Paulina von Tietzen` (person)
- `Amber Landscheid` (person)

**Example 12** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_4`)


Text Begründung: Mit ihrer am 22. 12. 2015 beim Landesgericht Salzburg als Arbeits- und Sozialgericht eingebrachten Klage begehrt die in Kagraner Anger 19, 4943 Nonsbach, Österreich (Sbg) ansässige Klägerin vom in Wien wohnhaften Beklagten die Zahlung einer Vertragsstrafe wegen mehrfacher Verstöße gegen das in seinem Agentenvertrag vereinbarte Wettbewerbsverbot.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Landesgericht Salzburg` (organisation)
- `Kagraner Anger 19, 4943 Nonsbach, Österreich` (address)

**Example 13** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_8`)


Es werde die Delegierung der Rechtssache an das Arbeits- und Sozialgericht Wien beantragt, weil der Beklagte dort seinen Lebensmittelpunkt habe und der Großteil der im Verfahren beantragten Zeugen aus dem Bereich Wien und Wien-Umgebung komme.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht Wien` | `Arbeits- und Sozialgericht Wien` |

**Example 14** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_14`)


Das Landesgericht Salzburg als Arbeits- und Sozialgericht sei auch mit den Rechtsangelegenheiten und regelmäßig gleichlautenden Vertragsgrundlagen und Provisions-abrechnungen der Klägerin seit Jahren vertraut.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Landesgericht Salzburg` (organisation)

**Example 15** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_15`)


Auch das Landesgericht Salzburg als Arbeits- und Sozialgericht gab im Ergebnis nach Abwägung von Für und Wider eine negative Stellungnahme ab.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Landesgericht Salzburg` (organisation)

**Example 16** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_18`)


Am 15. 2. 2016 übermittelte das Landesgericht Salzburg als Arbeits- und Sozialgericht im Nachhang eine von der Klägerin am 8.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Landesgericht Salzburg` (organisation)

**Example 17** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_35`)


Zu bedenken ist auch, dass das Landesgericht Salzburg als Arbeits- und Sozialgericht bereits eine Tagsatzung abgehalten und das Prozessprogramm festgelegt hat und mit der Problematik auch aus einem anderen Verfahren vertraut ist, während sich ein Wiener Gericht neu in die Sache einzuarbeiten hätte.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Landesgericht Salzburg` (organisation)

**Example 18** (doc_id: `deanon_TRAIN/9Ob59_20x`) (sent_id: `deanon_TRAIN/9Ob59_20x_17`)


Weiters begehrt der Kläger die Feststellung der Haftung des Beklagten für die ihm künftig aus der unrichtigen Gutachtenserstellung durch den Beklagten im Verfahren vor dem Arbeits- und Sozialgericht Wien zur AZ 25 Cgs 77/16w entstehenden Schaden.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht Wien` | `Arbeits- und Sozialgericht Wien` |

**Example 19** (doc_id: `deanon_TRAIN/9ObA118_18w`) (sent_id: `deanon_TRAIN/9ObA118_18w_4`)


Gabriele Svirak in der Arbeitsrechtssache der klagenden Partei Evelyn Lichtwer, vertreten durch Dr. Gerhard Hiebler, Dr. Gerd Grebenjak, Rechtsanwälte in Leoben, gegen die beklagte Partei Inn Wiltri Systeme GmbH, DDr. Johann Gerkens, vertreten durch Dr. Helmut Fetz, Dr. Birgit Fetz ua, Rechtsanwälte in Leoben, wegen 500 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. August 2018, GZ 7 Ra 23/18h-12, mit dem der Berufung der klagenden Partei gegen das Urteil des Landesgerichts Leoben als Arbeits- und Sozialgericht vom 14. Dezember 2017, GZ 23 Cga 75/17x-7, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision der klagenden Partei wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Evelyn Lichtwer` (person)
- `Inn Wiltri Systeme GmbH` (organisation)
- `DDr. Johann Gerkens` (person)

**Example 20** (doc_id: `deanon_TRAIN/9ObA118_19x`) (sent_id: `deanon_TRAIN/9ObA118_19x_5`)


Text Begründung: Mit Beschluss vom 15. Mai 2019, 9 ObA 41/19y, wies der Oberste Gerichtshof die außerordentliche Revision des Klägers in der beim Landesgericht Linz als Arbeits- und Sozialgericht anhängigen Arbeitsrechtssache gegen die beklagte Partei als seine frühere Arbeitgeberin mangels Vorliegens einer Rechtsfrage von erheblicher Bedeutung im Sinne des § 502 Abs 1 ZPO zurück.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Landesgericht Linz` (organisation)

**Example 21** (doc_id: `deanon_TRAIN/9ObA120_12f`) (sent_id: `deanon_TRAIN/9ObA120_12f_4`)


Dr. Helwig Aubauer und Mag. Regina Bauer-Albrecht als weitere Richter in der Arbeitsrechtssache der klagenden Partei Heidelinde Hobl, vertreten durch Dr. Dieter Gallistl, Rechtsanwalt in Linz, wider die beklagte Partei Elvira Vacha, vertreten durch Dr. Andreas Grassl, Rechtsanwalt in Wien, wegen Feststellung (Streitwert 174,77 EUR), über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. Juni 2012, GZ 12 Ra 48/12h-15, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts Wels als Arbeits- und Sozialgericht vom 31. Jänner 2012, GZ 16 Cga 154/11i-11, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Hobl` (person)
- `Elvira Vacha` (person)

**Example 22** (doc_id: `deanon_TRAIN/9ObA151_09k`) (sent_id: `deanon_TRAIN/9ObA151_09k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten des Obersten Gerichtshofs Dr. Rohrer als Vorsitzenden und die Hofräte des Obersten Gerichtshofs Dr. Hradil und Dr. Hopf sowie die fachkundigen Laienrichter KR Mag. Paul Kunsky und Franz Boindl als weitere Richter in der Arbeitsrechtssache der klagenden Partei PhD Ottfried Leonhardi, vertreten durch Dr. Charlotte Lindenberger, Rechtsanwältin in Steyr, gegen die beklagte Partei Baltromei Wind GmbH, Petra Ditrich, vertreten durch Dr. Otto Hauck, Rechtsanwalt in Kirchdorf, wegen 1.028,19 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 16. Oktober 2009, GZ 11 Ra 88/09d-10, womit das Urteil des Landesgerichts Steyr als Arbeits- und Sozialgericht vom 2. Juli 2009, GZ 24 Cga 9/09p-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch Der Revision wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `PhD Ottfried Leonhardi` (person)
- `Baltromei Wind GmbH` (organisation)
- `Petra Ditrich` (person)

**Example 23** (doc_id: `deanon_TRAIN/9ObA41_16v`) (sent_id: `deanon_TRAIN/9ObA41_16v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätinnen des Obersten Gerichtshofs Hon.-Prof. Dr. Dehn und Mag. Korn sowie die fachkundigen Laienrichter Dr. Johannes Pflug und Mag. Robert Brunner als weitere Richter in der Arbeitsrechtssache der klagenden Partei Mag. Joseph Mehl, vertreten durch Dr. Stephan Rainer und Dr. Andreas Ruetz, Rechtsanwälte in Innsbruck, gegen die beklagte Partei Heiko Ayna, vertreten durch Korn Rechtsanwälte OG in Wien, wegen 40.647,29 EUR brutto sA über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. Jänner 2016, GZ 15 Ra 16/16i-31, mit dem der Berufung der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 11. November 2015, GZ 43 Cga 118/14b-26, nicht Folge gegeben wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Mag. Joseph Mehl` (person)
- `Heiko Ayna` (person)

**Example 24** (doc_id: `deanon_TRAIN/9ObA43_12g`) (sent_id: `deanon_TRAIN/9ObA43_12g_4`)


Werner Keyzers, 4. Jaromir Heinrichson, alle vertreten durch die Advokaturbüro Jelenik & Partner AG, Landstraße 60, FL-9490 Vaduz (Zustellungsbevollmächtigter gemäß § 6 EIRAG: Mag. Norbert Wanker, Wasenweg 23, 6800 Feldkirch), gegen die beklagte Partei Wichtmann u. Staneck Energie GmbH, Dimitri Brunemann, vertreten durch Dr. Andreas Grundei, Rechtsanwalt in Wien, wegen Feststellung (Streitwert 10.000 EUR), über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 21. Februar 2012, GZ 15 Ra 13/12t-16, womit das Urteil des Landesgerichts Feldkirch als Arbeits- und Sozialgericht vom 4. Oktober 2011, GZ 35 Cga 85/11p-10, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Parteien wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Werner Keyzers` (person)
- `Jaromir Heinrichson` (person)
- `Partner AG` (organisation)
- `Wichtmann u. Staneck Energie GmbH` (organisation)
- `Dimitri Brunemann` (person)

**Example 25** (doc_id: `deanon_TRAIN/9ObA44_11b`) (sent_id: `deanon_TRAIN/9ObA44_11b_5`)


Dr. Wolfgang List, Rechtsanwalt in Wien, wider die beklagte Partei und Gegnerin der gefährdeten Partei Valerian Urbahn, vertreten durch Dr. J. Pfurtscheller, Dr. Orgler, Mag. Huber, Rechtsanwälte in Innsbruck, wegen Feststellung des Fortbestands eines Arbeitsverhältnisses, in eventu Anfechtung einer Kündigung nach § 105 ArbVG (Streitwert jeweils 31.000 EUR), in eventu 18.957 EUR sA, hier Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der klagenden und gefährdeten Partei gegen den Beschluss des Oberlandesgerichts Innsbruck als Rekursgericht in Arbeits- und Sozialrechtssachen vom 24. Februar 2011, GZ 15 Ra 11/11x-15, mit dem infolge Rekurses der klagenden und gefährdeten Partei der Beschluss des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 9. Dezember 2010, GZ 43 Cga 126/10y-8, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Valerian Urbahn` (person)

**Example 26** (doc_id: `deanon_TRAIN/9ObA4_13y`) (sent_id: `deanon_TRAIN/9ObA4_13y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Werner Rodlauer und Mag. Robert Brunner als weitere Richter in der Arbeitsrechtssache der klagenden Partei Maria Maritz, vertreten durch Dr. Susanne Kuen, Rechtsanwältin in Wien, gegen die beklagte Partei PHG Möbel Dienstleistungen GmbH, Zeno Speckl, vertreten durch Fellner Wratzfeld & Partner Rechtsanwälte GmbH in Wien, wegen 125.731,44 EUR sA, über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 30. Oktober 2012, GZ 11 Ra 82/12a-74, mit dem das Urteil des Landesgerichts Steyr als Arbeits- und Sozialgericht vom 31. Juli 2012, GZ 9 Cga 245/08g-70, aufgehoben und die Rechtssache an das Erstgericht zurückverwiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Maria Maritz` (person)
- `PHG Möbel Dienstleistungen GmbH` (organisation)
- `Zeno Speckl` (person)

**Example 27** (doc_id: `deanon_TRAIN/9ObA78_21t`) (sent_id: `deanon_TRAIN/9ObA78_21t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsrekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau und den Hofrat des Obersten Gerichtshofs Dr. Hargassner als weitere Richter in der Arbeitsrechtssache der klagenden Partei Ing. DI (FH) Griselda Eicholz, nunmehr vertreten durch Mag. Dr. Helmut Blum, Rechtsanwalt in Linz, gegen die beklagte Partei HochLuftfahrt GmbH, Saphira Thiehle, wegen Leistung, über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht in Arbeits- und Sozialrechtssachen vom 13. Mai 2019, GZ 11 Ra 33/19f-23, mit dem der Rekurs des Klägers gegen den Beschluss des Landesgerichts Linz als Arbeits- und Sozialgericht vom 8. April 2019, GZ 7 Cga 25/19k-9, zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Griselda Eicholz` (person)
- `HochLuftfahrt GmbH` (organisation)
- `Saphira Thiehle` (person)

**Example 28** (doc_id: `deanon_TRAIN/9ObA78_21t`) (sent_id: `deanon_TRAIN/9ObA78_21t_7`)


2. 2019 brachte der Kläger beim Landesgericht Linz als Arbeits- und Sozialgericht eine Klage gegen die Beklagte ein.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Landesgericht Linz` (organisation)

**Example 29** (doc_id: `deanon_TRAIN/9ObA82_20d`) (sent_id: `deanon_TRAIN/9ObA82_20d_3`)


Kopf Der Oberste Gerichtshof hat als Revisions- und Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau und den Hofrat des Obersten Gerichtshofs Dr. Hargassner sowie die fachkundigen Laienrichter Mag. Dr. Bernhard Gruber (aus dem Kreis der Arbeitgeber) und Angela Taschek (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Marktgemeinde Andrea Wiggering, vertreten durch Ehrenhöfer & Häusler Rechtsanwälte GmbH in Wiener Neustadt, gegen die beklagte Partei Cassandra Noldens, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, wegen 28.428,01 EUR sA, über den Rekurs und die außerordentliche Revision der klagenden Partei gegen den Beschluss (I.) und das Urteil (II.) des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 22. Juli 2020, GZ 9 Ra 111/19p-25, mit dem das Urteil des Landesgerichts Wiener Neustadt als Arbeits- und Sozialgericht vom 17. September 2019, GZ 9 Cga 126/18g-21, aus Anlass der Berufung der beklagten Partei hinsichtlich der Rückforderung einer Zahlung als nichtig aufgehoben und die Klage zurückgewiesen wurde und über Berufung der beklagen Partei hinsichtlich des Anspruchs nach dem OrgHG abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird teilweise Folge gegeben und der angefochtene Beschluss des Berufungsgerichts ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Andrea Wiggering` (person)
- `Cassandra Noldens` (person)

</details>

---

## `Court with Location`

**F1:** 0.050 | **Precision:** 1.000 | **Recall:** 0.026  

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
| 1.000 | 0.026 | 0.050 | 18 | 18 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 18 | 0 | 593 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob23_18g`) (sent_id: `deanon_TRAIN/10Ob23_18g_100`)


Die nach den Vorgaben des Verfassungsgerichtshofs gebotene steuerliche Entlastung des Geldunterhaltspflichtigen basiert auf dem Modell der getrennten Haushaltsführung (vgl RIS-Justiz RS0117015), in dem ein Elternteil seine Unterhaltspflicht durch Betreuungsleistungen und der andere durch Geldleistungen (allenfalls kombiniert mit anzurechnenden Naturalleistungen) erfüllt.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |

**Example 1** (doc_id: `deanon_TRAIN/3Ob26_23d`) (sent_id: `deanon_TRAIN/3Ob26_23d_48`)


Die Klägerin führt dagegen ins Treffen, dass die beschlussmäßige Umwidmung eines Grundstücks nach der Rechtsprechung des Verfassungsgerichtshofs erst dann erfolgen könne, wenn die Gemeinde bereits Eigentümerin des betroffenen Grundstücks sei; nur wenn es sich beim Grundstück um eine Privatstraße gehandelt hätte, die über Antrag des Eigentümers umgewidmet werden sollte, wäre eine Beschlussfassung nach § 27 Abs 2 Sbg LStG 1966 durch die Gemeinde vor Eigentumserwerb möglich gewesen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |

**Example 2** (doc_id: `deanon_TRAIN/3Ob26_23d`) (sent_id: `deanon_TRAIN/3Ob26_23d_51`)


Der von der Klägerin in diesem Zusammenhang zitierten Entscheidung des Verfassungsgerichtshofs vom 27. September 2003, V 108/01, lag nämlich der Sachverhalt zugrunde, dass der dort streitgegenständliche (Verbindungs-)Weg im Zeitpunkt der (vor der Enteignung des Grundstücks erfolgten) Widmung als Gemeindestraße schon seit Jahren als Privatstraße diente.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |

**Example 3** (doc_id: `deanon_TRAIN/3Ob26_23d`) (sent_id: `deanon_TRAIN/3Ob26_23d_52`)


Vor diesem Hintergrund sprach der Verfassungsgerichtshof aus, dass durch die Öffentlicherklärung einesin der Natur schon bestehendenWeges durch Verordnung mangels Eigentumserwerbs in gesetzwidriger Weise Gemeingebrauch begründet werde.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 4** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_67`)


In den vonRohregger(aaO) zitierten Entscheidungen bejahen auch der Verfassungsgerichtshof (B 1050/09) und der Verwaltungsgerichtshof (AW 2012/01/0032) die Bedeutung des § 10 RAO und der Vorgängerbestimmung des § 10 RL-BA 2015 für das öffentliche Interesse an dem Verbot der Doppelvertretung, weil es dem Schutz der durch einen Rechtsanwalt vertretenen Parteien diene, seine Einhaltung für das zwischen Rechtsanwalt und Klient bestehende Treueverhältnis für wesentlich erachtet werde und für das allgemeine Bild der Anwaltschaft in der Öffentlichkeit von Bedeutung sei.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 5** (doc_id: `deanon_TRAIN/5Ob31_16v`) (sent_id: `deanon_TRAIN/5Ob31_16v_15`)


Weiters wolle die Rechtssache gemäß Art 89 B-VG dem Verfassungsgerichtshof sowie gemäß Art 267 AEUV dem Europäischen Gerichtshof zur Prüfung vorgelegt werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 6** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_14`)


Der gesatzte Kollektivvertrag des Roten Kreuzes sei unanwendbar, da der Verwaltungsgerichtshof mit Erkenntnis vom 4. 9. 2013, 2011/08/0230 dem Österreichischen Roten Kreuz die Kollektivvertragsfähigkeit „de facto“ aberkannt habe, sodass die Verordnung des Bundeseinigungsamtes „rechtswidrig und ungültig“ sei.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 7** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_28`)


3. Der Verwaltungsgerichtshof hat mit seinem Erkenntnis vom 4. 9. 2013, 2011/08/0230 = DRdA 2014/27 (Felten) = ZAS 2014/13 (Tomandl) dem Österreichischen Roten Kreuz die Kollektivvertragsfähigkeit gemäß § 5 Abs 3 ArbVG nicht aberkannt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 8** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_29`)


Der Verwaltungsgerichtshof behob allein einen Bescheid, mit dem ein Antrag auf eine solche Aberkennung abgewiesen wurde, wegen Rechtswidrigkeit seines Inhalts (worauf auch der von der Beklagten angerufene Verfassungsgerichtshof in Punkt 2.4.5.3 seines Erkenntnisses ausdrücklich hinwies).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 9** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_30`)


Weil in der Folge abermals ein abweisender Bescheid erging, der sodann in Rechtskraft erwuchs (siehe erneut in Punkt 2.4.5.3 des VfGH-Erkenntnisses), ist es letzten Endes auch unrichtig, dass der Verwaltungsgerichtshof dem Roten Kreuz „de facto“ die Kollektivvertragsfähigkeit aberkannt hätte.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 10** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_31`)


Von dieser Sachlage ausgehend wies der von der Beklagten in diesem Verfahren mittels eines Parteiantrags auf Normenkontrolle angerufene Verfassungsgerichtshof den Antrag, die in BGBl II 2013/120 kundgemachte Verordnung des Bundeseinigungsamtes zur Gänze als verfassungswidrig aufzuheben, mit der Begründung ab, die Bedenken der Beklagten beruhten auf der nicht zutreffenden Prämisse, das Österreichische Rote Kreuz habe seine Kollektivvertragsfähigkeit durch das Erkenntnis des Verwaltungsgerichtshofs 2011/08/0230 „de facto“ verloren (Punkt 2.5 des Erkenntnisses).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 11** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_33`)


4. Die Frage, ob auch ohne Aufhebung der Verordnung BGBl II 2013/120 durch den Verfassungsgerichtshof allein dadurch, dass dem Österreichischen Roten Kreuz die Kollektivvertragsfähigkeit vom Bundeseinigungsamt mittels Bescheids aberkannt wird, die Satzung des Kollektivvertrags ihre Geltung verliert (vgl insbFriedrich, ASoK 2013, 460 f), stellt sich nicht, weil kein solcher Bescheid vorliegt.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 12** (doc_id: `deanon_TRAIN/8ObA72_19z`) (sent_id: `deanon_TRAIN/8ObA72_19z_12`)


2. Dabei konnte sich der Oberste Gerichtshof auf einschlägige Judikatur sowohl des Verfassungsgerichtshofs als auch des EuGH stützen: 2.1 Der Verfassungsgerichtshof hat in seinem Erkenntnis G 450/2015 ua Parteianträge von ÖBB-Bediensteten (unter anderem auch des Klägers) abgewiesen, die § 53a und § 56 Abs 18 bis 24 BundesbahnG je idF BGBl I Nr 64/2015 als verfassungswidrig aufzuheben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 13** (doc_id: `deanon_TRAIN/9ObA27_15h`) (sent_id: `deanon_TRAIN/9ObA27_15h_7`)


Ihr Antrag auf Gesetzesprüfung hinsichtlich der inzwischen aufgelösten Berufungskommission und eine Eventualbeschwerde seien beim Verfassungsgerichtshof anhängig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

</details>

---

## `Constitutional Court`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.011  

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
| 1.000 | 0.011 | 0.023 | 8 | 8 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 0 | 393 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/3Ob26_23d`) (sent_id: `deanon_TRAIN/3Ob26_23d_52`)


Vor diesem Hintergrund sprach der Verfassungsgerichtshof aus, dass durch die Öffentlicherklärung einesin der Natur schon bestehendenWeges durch Verordnung mangels Eigentumserwerbs in gesetzwidriger Weise Gemeingebrauch begründet werde.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 1** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_67`)


In den vonRohregger(aaO) zitierten Entscheidungen bejahen auch der Verfassungsgerichtshof (B 1050/09) und der Verwaltungsgerichtshof (AW 2012/01/0032) die Bedeutung des § 10 RAO und der Vorgängerbestimmung des § 10 RL-BA 2015 für das öffentliche Interesse an dem Verbot der Doppelvertretung, weil es dem Schutz der durch einen Rechtsanwalt vertretenen Parteien diene, seine Einhaltung für das zwischen Rechtsanwalt und Klient bestehende Treueverhältnis für wesentlich erachtet werde und für das allgemeine Bild der Anwaltschaft in der Öffentlichkeit von Bedeutung sei.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 2** (doc_id: `deanon_TRAIN/5Ob31_16v`) (sent_id: `deanon_TRAIN/5Ob31_16v_15`)


Weiters wolle die Rechtssache gemäß Art 89 B-VG dem Verfassungsgerichtshof sowie gemäß Art 267 AEUV dem Europäischen Gerichtshof zur Prüfung vorgelegt werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 3** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_29`)


Der Verwaltungsgerichtshof behob allein einen Bescheid, mit dem ein Antrag auf eine solche Aberkennung abgewiesen wurde, wegen Rechtswidrigkeit seines Inhalts (worauf auch der von der Beklagten angerufene Verfassungsgerichtshof in Punkt 2.4.5.3 seines Erkenntnisses ausdrücklich hinwies).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 4** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_31`)


Von dieser Sachlage ausgehend wies der von der Beklagten in diesem Verfahren mittels eines Parteiantrags auf Normenkontrolle angerufene Verfassungsgerichtshof den Antrag, die in BGBl II 2013/120 kundgemachte Verordnung des Bundeseinigungsamtes zur Gänze als verfassungswidrig aufzuheben, mit der Begründung ab, die Bedenken der Beklagten beruhten auf der nicht zutreffenden Prämisse, das Österreichische Rote Kreuz habe seine Kollektivvertragsfähigkeit durch das Erkenntnis des Verwaltungsgerichtshofs 2011/08/0230 „de facto“ verloren (Punkt 2.5 des Erkenntnisses).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofs` (organisation)

**Example 5** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_33`)


4. Die Frage, ob auch ohne Aufhebung der Verordnung BGBl II 2013/120 durch den Verfassungsgerichtshof allein dadurch, dass dem Österreichischen Roten Kreuz die Kollektivvertragsfähigkeit vom Bundeseinigungsamt mittels Bescheids aberkannt wird, die Satzung des Kollektivvertrags ihre Geltung verliert (vgl insbFriedrich, ASoK 2013, 460 f), stellt sich nicht, weil kein solcher Bescheid vorliegt.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 6** (doc_id: `deanon_TRAIN/8ObA72_19z`) (sent_id: `deanon_TRAIN/8ObA72_19z_12`)


2. Dabei konnte sich der Oberste Gerichtshof auf einschlägige Judikatur sowohl des Verfassungsgerichtshofs als auch des EuGH stützen: 2.1 Der Verfassungsgerichtshof hat in seinem Erkenntnis G 450/2015 ua Parteianträge von ÖBB-Bediensteten (unter anderem auch des Klägers) abgewiesen, die § 53a und § 56 Abs 18 bis 24 BundesbahnG je idF BGBl I Nr 64/2015 als verfassungswidrig aufzuheben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verfassungsgerichtshofs` (organisation)

**Example 7** (doc_id: `deanon_TRAIN/9ObA27_15h`) (sent_id: `deanon_TRAIN/9ObA27_15h_7`)


Ihr Antrag auf Gesetzesprüfung hinsichtlich der inzwischen aufgelösten Berufungskommission und eine Eventualbeschwerde seien beim Verfassungsgerichtshof anhängig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

</details>

---

## `Vienna Magistrate`

**F1:** 0.020 | **Precision:** 1.000 | **Recall:** 0.010  

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
| 1.000 | 0.010 | 0.020 | 7 | 7 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 0 | 615 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob11_11g`) (sent_id: `deanon_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Mag. Elmar Janaschek, geboren am 8. Mai 1999, und der minderjährigen VetR Charlotte Eissenmann, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Mag. Elmar Janaschek` (person)
- `VetR Charlotte Eissenmann` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob15_12x`) (sent_id: `deanon_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Egon Luckow, geboren am 1. August 2011, und des mj Priv.-Doz. Samuel Prestle, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Egon Luckow` (person)
- `Priv.-Doz. Samuel Prestle` (person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob25_25m`) (sent_id: `deanon_TRAIN/10Ob25_25m_4`)


Claire Al-Hakim, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Rechtsvertretung Bezirk 21, 1210 Wien, Franz-Jonas-Platz 12), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 22. November 2024, GZ 45 R 496/24k-26, mit dem der Beschluss des Bezirksgerichts Floridsdorf vom 2. August 2024, GZ 16 Pu 19/24a-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Claire Al-Hakim` (person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob3_23y`) (sent_id: `deanon_TRAIN/10Ob3_23y_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Ziegelbauer als Vorsitzenden sowie die Hofrätin Dr. Faber und die Hofräte Mag. Schober, Dr. Thunhart und Dr. Annerl als weitere Richter in der Pflegschaftssache der minderjährigen Juri Bents, geboren 18. Januar 2006, vertreten durch das Land Wien als Träger der Kinder- und Jugendhilfe (Magistrat der Stadt Wien, Rechtsvertretung Bezirke 1, 4 bis 9, 1060 Wien, Amerlingstraße 11), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch die Präsidentin des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 31. Oktober 2022, GZ 43 R 323/22a-17, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 9. Juni 2022, GZ 4 Pu 58/22a-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Juri Bents` (person)
- `18. Januar` (date)

**Example 4** (doc_id: `deanon_TRAIN/10Ob42_15x`) (sent_id: `deanon_TRAIN/10Ob42_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Pflegschaftssache 1. der mj Siegbert Führholzer, MBA, geboren am 30. August 1983 und 2. des mj Gerhard Luttermann, geboren am 11. März 1953, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung Bezirk 22, 1220 Wien, Hirschstettner Straße 19-21/Stiege N), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 10. Dezember 2014, GZ 42 R 343/13x, 42 R 344/13v und 42 R 345/13s-106, womit den Rekursen der Minderjährigen gegen den Beschluss des Bezirksgerichts Donaustadt vom 14. März 2013, GZ 3 Pu 61/12x-40, teilweise Folge gegeben wurde (Pkt 1 des Spruchs), dem Rekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen die Beschlüsse des Bezirksgerichts Donaustadt (jeweils) vom 6. Juni 2013, GZ 3 Pu 61/12x-49 und 3 Pu 61/12x-50, Folge gegeben (Pkt 2a des Spruchs), und aus Anlass des Rekurses die Anträge der Minderjährigen auf Gewährung von Unterhaltsvorschüssen zur Gänze abgewiesen wurden (Pkt 2b des Spruchs), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Siegbert Führholzer, MBA` (person)
- `30. August 1983` (date)
- `Gerhard Luttermann` (person)
- `11. März 1953` (date)

**Example 5** (doc_id: `deanon_TRAIN/3Ob66_11v`) (sent_id: `deanon_TRAIN/3Ob66_11v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Pflegschaftssache der mj Liudmila Sidler, vertreten durch den Jugendwohlfahrtsträger Land Wien, dieser vertreten durch den Magistrat der Stadt Wien, Amt für Jugend und Familie, Wien 2, Karmelitergasse 9, Mutter Liudmila Schlensok, vertreten durch den Sachwalter Dr. Herbert Eisserer, Rechtsanwalt in Wien, Vater Dmitry Schimczik vertreten durch Mag. Wolfgang Maier, Rechtsanwalt in Wien, wegen Übertragung der Obsorge, über den außerordentlichen Revisionsrekurs der Mutter gegen den Beschluss des Landesgerichts St. Pölten als Rekursgericht vom 16. Februar 2011, GZ 23 R 10/11k-171, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Lilienfeld vom 10. November 2010, GZ 1 P 121/09f-S-162, abgeändert wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Sidler` (person)
- `Schlensok` (person)
- `Schimczik` (person)

**Example 6** (doc_id: `deanon_TRAIN/7Ob119_18b`) (sent_id: `deanon_TRAIN/7Ob119_18b_4`)


Matzka als weitere Richter in der Pflegschaftssache der Minderjährigen Silke Wieging, geboren am 20. März 2010, 12. September 1996, vertreten durch das Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung Bezirke 12, 13, 23, 1230 Wien, Rößlergasse 15, Mutter Fiona Wenzlick, Vater Viola Peiniger, vertreten durch Dr. Tassilo Wallentin LL.M, Rechtsanwalt in Wien, wegen Unterhalt, infolge Revisionsrekurses des Vaters gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 8. Mai 2018, GZ 44 R 104/18x-180, womit der Rekurs des Vaters gegen den Beschluss des Bezirksgerichts Meidling vom 25. Jänner 2018, GZ 1 Pu 73/10b-173, teilweise zurückgewiesen und ihm im Übrigen nicht Folge gegeben wurde, den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Silke Wieging` (person)
- `20. März` (date)
- `12. September 1996` (date)
- `Fiona Wenzlick` (person)
- `Viola Peiniger` (person)

</details>

---

## `Magistrate City Pattern`

**F1:** 0.020 | **Precision:** 1.000 | **Recall:** 0.010  

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
| 1.000 | 0.010 | 0.020 | 7 | 7 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 0 | 615 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob11_11g`) (sent_id: `deanon_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Mag. Elmar Janaschek, geboren am 8. Mai 1999, und der minderjährigen VetR Charlotte Eissenmann, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Mag. Elmar Janaschek` (person)
- `VetR Charlotte Eissenmann` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob15_12x`) (sent_id: `deanon_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Egon Luckow, geboren am 1. August 2011, und des mj Priv.-Doz. Samuel Prestle, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Egon Luckow` (person)
- `Priv.-Doz. Samuel Prestle` (person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob25_25m`) (sent_id: `deanon_TRAIN/10Ob25_25m_4`)


Claire Al-Hakim, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Rechtsvertretung Bezirk 21, 1210 Wien, Franz-Jonas-Platz 12), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 22. November 2024, GZ 45 R 496/24k-26, mit dem der Beschluss des Bezirksgerichts Floridsdorf vom 2. August 2024, GZ 16 Pu 19/24a-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Claire Al-Hakim` (person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob3_23y`) (sent_id: `deanon_TRAIN/10Ob3_23y_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Ziegelbauer als Vorsitzenden sowie die Hofrätin Dr. Faber und die Hofräte Mag. Schober, Dr. Thunhart und Dr. Annerl als weitere Richter in der Pflegschaftssache der minderjährigen Juri Bents, geboren 18. Januar 2006, vertreten durch das Land Wien als Träger der Kinder- und Jugendhilfe (Magistrat der Stadt Wien, Rechtsvertretung Bezirke 1, 4 bis 9, 1060 Wien, Amerlingstraße 11), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch die Präsidentin des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 31. Oktober 2022, GZ 43 R 323/22a-17, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 9. Juni 2022, GZ 4 Pu 58/22a-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Juri Bents` (person)
- `18. Januar` (date)

**Example 4** (doc_id: `deanon_TRAIN/10Ob42_15x`) (sent_id: `deanon_TRAIN/10Ob42_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Pflegschaftssache 1. der mj Siegbert Führholzer, MBA, geboren am 30. August 1983 und 2. des mj Gerhard Luttermann, geboren am 11. März 1953, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung Bezirk 22, 1220 Wien, Hirschstettner Straße 19-21/Stiege N), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 10. Dezember 2014, GZ 42 R 343/13x, 42 R 344/13v und 42 R 345/13s-106, womit den Rekursen der Minderjährigen gegen den Beschluss des Bezirksgerichts Donaustadt vom 14. März 2013, GZ 3 Pu 61/12x-40, teilweise Folge gegeben wurde (Pkt 1 des Spruchs), dem Rekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen die Beschlüsse des Bezirksgerichts Donaustadt (jeweils) vom 6. Juni 2013, GZ 3 Pu 61/12x-49 und 3 Pu 61/12x-50, Folge gegeben (Pkt 2a des Spruchs), und aus Anlass des Rekurses die Anträge der Minderjährigen auf Gewährung von Unterhaltsvorschüssen zur Gänze abgewiesen wurden (Pkt 2b des Spruchs), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Siegbert Führholzer, MBA` (person)
- `30. August 1983` (date)
- `Gerhard Luttermann` (person)
- `11. März 1953` (date)

**Example 5** (doc_id: `deanon_TRAIN/3Ob66_11v`) (sent_id: `deanon_TRAIN/3Ob66_11v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Pflegschaftssache der mj Liudmila Sidler, vertreten durch den Jugendwohlfahrtsträger Land Wien, dieser vertreten durch den Magistrat der Stadt Wien, Amt für Jugend und Familie, Wien 2, Karmelitergasse 9, Mutter Liudmila Schlensok, vertreten durch den Sachwalter Dr. Herbert Eisserer, Rechtsanwalt in Wien, Vater Dmitry Schimczik vertreten durch Mag. Wolfgang Maier, Rechtsanwalt in Wien, wegen Übertragung der Obsorge, über den außerordentlichen Revisionsrekurs der Mutter gegen den Beschluss des Landesgerichts St. Pölten als Rekursgericht vom 16. Februar 2011, GZ 23 R 10/11k-171, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Lilienfeld vom 10. November 2010, GZ 1 P 121/09f-S-162, abgeändert wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Sidler` (person)
- `Schlensok` (person)
- `Schimczik` (person)

**Example 6** (doc_id: `deanon_TRAIN/7Ob119_18b`) (sent_id: `deanon_TRAIN/7Ob119_18b_4`)


Matzka als weitere Richter in der Pflegschaftssache der Minderjährigen Silke Wieging, geboren am 20. März 2010, 12. September 1996, vertreten durch das Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung Bezirke 12, 13, 23, 1230 Wien, Rößlergasse 15, Mutter Fiona Wenzlick, Vater Viola Peiniger, vertreten durch Dr. Tassilo Wallentin LL.M, Rechtsanwalt in Wien, wegen Unterhalt, infolge Revisionsrekurses des Vaters gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 8. Mai 2018, GZ 44 R 104/18x-180, womit der Rekurs des Vaters gegen den Beschluss des Bezirksgerichts Meidling vom 25. Jänner 2018, GZ 1 Pu 73/10b-173, teilweise zurückgewiesen und ihm im Übrigen nicht Folge gegeben wurde, den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Silke Wieging` (person)
- `20. März` (date)
- `12. September 1996` (date)
- `Fiona Wenzlick` (person)
- `Viola Peiniger` (person)

</details>

---

## `Administrative Court`

**F1:** 0.017 | **Precision:** 1.000 | **Recall:** 0.009  

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
| 1.000 | 0.009 | 0.017 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 281 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_67`)


In den vonRohregger(aaO) zitierten Entscheidungen bejahen auch der Verfassungsgerichtshof (B 1050/09) und der Verwaltungsgerichtshof (AW 2012/01/0032) die Bedeutung des § 10 RAO und der Vorgängerbestimmung des § 10 RL-BA 2015 für das öffentliche Interesse an dem Verbot der Doppelvertretung, weil es dem Schutz der durch einen Rechtsanwalt vertretenen Parteien diene, seine Einhaltung für das zwischen Rechtsanwalt und Klient bestehende Treueverhältnis für wesentlich erachtet werde und für das allgemeine Bild der Anwaltschaft in der Öffentlichkeit von Bedeutung sei.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `Verfassungsgerichtshof` (organisation)

**Example 1** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_14`)


Der gesatzte Kollektivvertrag des Roten Kreuzes sei unanwendbar, da der Verwaltungsgerichtshof mit Erkenntnis vom 4. 9. 2013, 2011/08/0230 dem Österreichischen Roten Kreuz die Kollektivvertragsfähigkeit „de facto“ aberkannt habe, sodass die Verordnung des Bundeseinigungsamtes „rechtswidrig und ungültig“ sei.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 2** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_28`)


3. Der Verwaltungsgerichtshof hat mit seinem Erkenntnis vom 4. 9. 2013, 2011/08/0230 = DRdA 2014/27 (Felten) = ZAS 2014/13 (Tomandl) dem Österreichischen Roten Kreuz die Kollektivvertragsfähigkeit gemäß § 5 Abs 3 ArbVG nicht aberkannt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 3** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_29`)


Der Verwaltungsgerichtshof behob allein einen Bescheid, mit dem ein Antrag auf eine solche Aberkennung abgewiesen wurde, wegen Rechtswidrigkeit seines Inhalts (worauf auch der von der Beklagten angerufene Verfassungsgerichtshof in Punkt 2.4.5.3 seines Erkenntnisses ausdrücklich hinwies).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `Verfassungsgerichtshof` (organisation)

**Example 4** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_30`)


Weil in der Folge abermals ein abweisender Bescheid erging, der sodann in Rechtskraft erwuchs (siehe erneut in Punkt 2.4.5.3 des VfGH-Erkenntnisses), ist es letzten Endes auch unrichtig, dass der Verwaltungsgerichtshof dem Roten Kreuz „de facto“ die Kollektivvertragsfähigkeit aberkannt hätte.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 5** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_31`)


Von dieser Sachlage ausgehend wies der von der Beklagten in diesem Verfahren mittels eines Parteiantrags auf Normenkontrolle angerufene Verfassungsgerichtshof den Antrag, die in BGBl II 2013/120 kundgemachte Verordnung des Bundeseinigungsamtes zur Gänze als verfassungswidrig aufzuheben, mit der Begründung ab, die Bedenken der Beklagten beruhten auf der nicht zutreffenden Prämisse, das Österreichische Rote Kreuz habe seine Kollektivvertragsfähigkeit durch das Erkenntnis des Verwaltungsgerichtshofs 2011/08/0230 „de facto“ verloren (Punkt 2.5 des Erkenntnisses).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Missed by this rule (FN):**

- `Verfassungsgerichtshof` (organisation)

</details>

---

## `District Court Pattern`

**F1:** 0.316 | **Precision:** 0.811 | **Recall:** 0.196  

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
| 0.811 | 0.196 | 0.316 | 169 | 137 | 32 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 137 | 32 | 562 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_4`)


Text Begründung: Die Klägerin begehrt mit der am 4. 8. 2017 beim Bezirksgericht Steyr eingebrachten Klage von dem in der Schweiz ansässigen Beklagten 4.660 EUR sA.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Steyr` | `Bezirksgericht Steyr` |

**Example 1** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_11`)


2018 erklärte sich dasBezirksgericht Steyrfür örtlich unzuständig und überwies (antragsgemäß) die Rechtssache an das nicht offenbar unzuständige Bezirksgericht Salzburg.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Example 2** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_22`)


Da das Bezirksgericht Salzburg die internationale Zuständigkeit Österreichs zur Erledigung der Klage rechtskräftig verneint hat, kann eine Ordination nicht mehr erfolgreich auf § 28 Abs 1 Z 1 JN gestützt werden.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Example 3** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Schramm als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Ivan Dimitroff, geboren am 19. Mai 1960, AZ 7 P 203/15g des Bezirksgerichts Mödling, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Mödling zurückgestellt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Missed by this rule (FN):**

- `Ivan Dimitroff` (person)
- `19. Mai 1960` (date)
- `Bezirksgerichts Mödling` (organisation)

**Example 4** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_4`)


Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |
| `Bezirksgericht Judenburg` | `Bezirksgericht Judenburg` |

**Missed by this rule (FN):**

- `Bezirksgerichts Judenburg` (organisation)

**Example 5** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_5`)


Das Bezirksgericht Mödling legte den Akt zur Entscheidung gemäß § 111 Abs 2 JN dem Obersten Gerichtshof vor (ON 8), ohne den Übertragungsbeschluss an die Parteien zuzustellen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Example 6** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_9`)


Nach Aufforderung im Sinn des § 252 Abs 3 ZPO benannte die Klägerin fristgerecht das Bezirksgericht Graz-Ost als das für die Durchführung des ordentlichen Verfahrens zuständige Gericht.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz` | `Bezirksgericht Graz` |

**Example 7** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_11`)


[3] Vor dem Bezirksgericht Graz-Ost beantragte sie die Vorlage der Rechtssache an den Obersten Gerichtshof zur Ordination nach § 28 Abs 1 Z 3 JN sowie die Unterbrechung des Verfahrens bis zur Entscheidung des Obersten Gerichtshofs (ON 18).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz` | `Bezirksgericht Graz` |

**Example 8** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_16`)


[5] Das Bezirksgericht Graz-Ost unterbrach das Verfahren bis zur Entscheidung des Obersten Gerichtshofs, „ein örtlich zuständiges Gericht gemäß § 98 Abs 1 Z 3 JN für die Geltendmachung der Forderungen der klagenden Partei gegenüber der Beklagten aus der gegenständlichen Geschäftsbeziehung zu bestimmen“, und sprach aus, dass das Verfahren nur über Antrag der Parteien fortgesetzt werde.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz` | `Bezirksgericht Graz` |

**Example 9** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_19`)


Das Bezirksgericht Graz-Ost legte den Akt dem Obersten Gerichtshof zur Entscheidung nach § 28 Abs 1 Z 3 JN vor.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz` | `Bezirksgericht Graz` |

**Example 10** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_30`)


Die Rechtssache wurde an das von der Klägerin namhafte gemachte Bezirksgericht Graz-Ost überwiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz` | `Bezirksgericht Graz` |

**Example 11** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_33`)


[12] 2.3 Solange das Bezirksgericht Graz-Ost seine sich aus § 252 Abs 3 ZPO ergebende Zuständigkeit nicht rechtskräftig verneint hat, ist der Oberste Gerichtshof nicht zur Bestimmung eines örtlich zuständigen Gerichts nach § 28 Abs 1 Z 3 JN berufen (RS0046450;

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz` | `Bezirksgericht Graz` |

**Example 12** (doc_id: `deanon_TRAIN/10Nc22_25d`) (sent_id: `deanon_TRAIN/10Nc22_25d_5`)


Der nach eigenen Angaben keinen „festen Wohnsitz“ habende Kläger erhob vor dem Bezirksgericht Neusiedl am See eine Klage auf Feststellung, dass der Beklagte nicht berechtigt sei, Daten in eine Datenanwendung einzufügen „bzw“ dass der Beklagte für die Entfernung solcher Daten aus der Anwendung „zuständig“ sei.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neusiedl` | `Bezirksgericht Neusiedl` |

**Example 13** (doc_id: `deanon_TRAIN/10Nc22_25d`) (sent_id: `deanon_TRAIN/10Nc22_25d_6`)


[2] Das Bezirksgericht Neusiedl am See und der Beklagte äußerten sich dahingehend, dass sie die Delegierung für nicht zweckmäßig erachteten.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neusiedl` | `Bezirksgericht Neusiedl` |

**Example 14** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und die Hofräte Dr. Fellinger und Dr. Schramm als weitere Richter in der Pflegschaftssache der Minderjährigen Delia Truepschuch, geboren am 1. Februar 2026, und Aloisa Eckmaier, geboren am 28. Februar 1976, AZ 2 PS 117/09t des Bezirksgerichts Feldkirchen, infolge Vorlage zur Genehmigung der Übertragung gemäß § 111 JN an das Bezirksgericht Neunkirchen, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Übertragung der Zuständigkeit zur Besorgung dieser Pflegschaftssache an das Bezirksgericht Neunkirchen wird genehmigt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Missed by this rule (FN):**

- `Delia Truepschuch` (person)
- `1. Februar 2026` (date)
- `Aloisa Eckmaier` (person)
- `28. Februar 1976` (date)

**Example 15** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_4`)


Begründung:  Rechtliche Beurteilung Das bisher zuständige Bezirksgericht Feldkirchen übertrug mit seinem - den Verfahrensbeteiligten zugestellten und nicht bekämpften - Beschluss vom 7. 10.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Feldkirchen` | `Bezirksgericht Feldkirchen` |

**Example 16** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_5`)


2009 die Zuständigkeit zur Führung der Pflegschaftssache an das Bezirksgericht Neunkirchen, weil die beiden Minderjährigen und ihre obsorgeberechtigte Mutter, in deren Haushalt sich die Kinder nach dem pflegschaftsgerichtlich genehmigten Scheidungsvergleich hauptsächlich aufhalten sollen, sich nunmehr ständig im Sprengel dieses Gerichts aufhielten.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Example 17** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_6`)


Das Bezirksgericht Neunkirchen verweigerte die Übernahme der Zuständigkeit, weil das übertragende Gericht den Antrag vom 24.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Example 18** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_7`)


8. 2009 schon zu bearbeiten begonnen habe, ihm die verfahrensbeteiligten Personen bekannt, dem Bezirksgericht Neunkirchen aber gänzlich unbekannt seien.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Example 19** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen ÖkR Priv.-Doz. Sven Egerth, geboren 3. Mai 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz` | `Bezirksgericht Graz` |

**Missed by this rule (FN):**

- `ÖkR Priv.-Doz. Sven Egerth` (person)
- `3. Mai` (date)

**Example 20** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_5`)


9. 2023 übertrug das Bezirksgericht Graz-West die Zuständigkeit zur Führung der Pflegschaftssache dem Bezirksgericht Braunau am Inn, das die Übernahme jedoch ablehnte.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz` | `Bezirksgericht Graz` |
| `Bezirksgericht Braunau` | `Bezirksgericht Braunau` |

**Example 21** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_6`)


[2] Das Bezirksgericht Graz-West legte den Akt daraufhin dem Obersten Gerichtshof zur Entscheidung gemäß § 111 Abs 2 JN vor, ohne den Übertragungsbeschluss den Parteien zuzustellen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz` | `Bezirksgericht Graz` |

**Example 22** (doc_id: `deanon_TRAIN/10Nc2_10s`) (sent_id: `deanon_TRAIN/10Nc2_10s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Pflegschaftssache des mj Andreas Wolfgang Spinner, geboren am 8. Juli 2004, und der mj Herta Vanessa Schlichtcroll, geboren am 4. April 2007, wegen Übertragung der Zuständigkeit nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Die mit Beschluss des Bezirksgerichts Salzburg vom 9. 9. 2009, AZ 42 PS 56/09a, verfügte Übertragung der Zuständigkeit zur Führung der Pflegschaftssache an das Bezirksgericht Mödling wird genehmigt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Missed by this rule (FN):**

- `Spinner` (person)
- `Schlichtcroll` (person)

**Example 23** (doc_id: `deanon_TRAIN/10Nc2_10s`) (sent_id: `deanon_TRAIN/10Nc2_10s_4`)


Begründung:  Rechtliche Beurteilung Die Zuständigkeit in der früher beim Bezirksgericht Steyr und beim Bezirksgericht Mattighofen anhängig gewesenen Pflegschaftssache wurde mit Beschluss des Bezirksgerichts Salzburg vom 26.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Steyr` | `Bezirksgericht Steyr` |
| `Bezirksgericht Mattighofen` | `Bezirksgericht Mattighofen` |

**Example 24** (doc_id: `deanon_TRAIN/10Nc2_10s`) (sent_id: `deanon_TRAIN/10Nc2_10s_7`)


2. 2009 beim Bezirksgericht Salzburg den Antrag, ihm die (einstweilige) Obsorge über die beiden Minderjährigen zu übertragen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Example 25** (doc_id: `deanon_TRAIN/10Nc2_10s`) (sent_id: `deanon_TRAIN/10Nc2_10s_12`)


2009 übertrug das Bezirksgericht Salzburg die Zuständigkeit zur Führung der Pflegschaftssache gemäß § 111 JN dem Bezirksgericht Mödling, weil die beiden Minderjährigen ihren Aufenthalt nunmehr im Sprengel dieses Gerichts hätten.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Example 26** (doc_id: `deanon_TRAIN/10Nc2_10s`) (sent_id: `deanon_TRAIN/10Nc2_10s_13`)


Auch die Mutter beantragte die Übertragung der Zuständigkeit an das Bezirksgericht Mödling, weil sie mit den Kindern nunmehr ihren Wohnsitz im Sprengel dieses Gerichts habe und sie dort auch vom Jugendwohlfahrtsträger betreut werde.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Example 27** (doc_id: `deanon_TRAIN/10Nc2_10s`) (sent_id: `deanon_TRAIN/10Nc2_10s_14`)


Das Bezirksgericht Mödling lehnte die Übernahme der Pflegschaftssache unter Hinweis auf die noch offenen Obsorgeanträge der Eltern ab.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Example 28** (doc_id: `deanon_TRAIN/10Nc2_10s`) (sent_id: `deanon_TRAIN/10Nc2_10s_18`)


Die Übertragung der Führung der Pflegschaftssache an das Bezirksgericht Mödling ist gerechtfertigt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Example 29** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei C. Dersudheim Digital GmbH, Taxlbergstraße 247, 8151 Rohrbach, Österreich, vertreten durch Dr. Carl Benkhofer, Rechtsanwalt in Wien, gegen die beklagte Partei Ingolf Grimpe, vertreten durch Greiml & Horwath Rechtsanwaltspartnerschaft in Graz, wegen 5.232 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 14 C 1302/11a des Bezirksgerichts Graz-West in nichtöffentlicher Sitzung, den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Graz-West das Bezirksgericht Fünfhaus bestimmt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Fünfhaus` | `Bezirksgericht Fünfhaus` |

**Missed by this rule (FN):**

- `Dersudheim Digital GmbH` (organisation)
- `Taxlbergstraße 247, 8151 Rohrbach, Österreich` (address)
- `Ingolf Grimpe` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_6`)


12. 2006 zur Einführung eines Europäischen Mahnverfahrens (EuMahnVO) vor dem Bezirksgericht für Handelssachen Wien die Zahlung von Forderungen aus in den Jahren 2018 und 2019 geschlossenen Werkverträgen.

**False Positives:**

- `Bezirksgericht für` — partial — pred is substring of gold: `Bezirksgericht für Handelssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht für Handelssachen Wien`(organisation)

**Example 1** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_7`)


[2] Das Bezirksgericht für Handelssachen Wien erließ – nach Verbesserung des Antrags – den Europäischen Zahlungsbefehl, gegen den die Beklagte fristgerecht Einspruch erhob.

**False Positives:**

- `Bezirksgericht für` — partial — pred is substring of gold: `Bezirksgericht für Handelssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht für Handelssachen Wien`(organisation)

**Example 2** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_10`)


Das Bezirksgericht für Handelssachen Wien überwies die Rechtssache an dieses Gericht.

**False Positives:**

- `Bezirksgericht für` — partial — pred is substring of gold: `Bezirksgericht für Handelssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht für Handelssachen Wien`(organisation)

**Example 3** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_22`)


[8] 1.1 Für das Verfahren nach der Europäischen Mahnverfahrensverordnung ist in Österreich nach § 252 Abs 2 ZPO ausschließlich das Bezirksgericht für Handelssachen Wien zuständig.

**False Positives:**

- `Bezirksgericht für` — partial — pred is substring of gold: `Bezirksgericht für Handelssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht für Handelssachen Wien`(organisation)

**Example 4** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_8`)


Das bisher zuständige Bezirksgericht werde daher die Interessen der Minderjährigen besser wahren können, zumal unmittelbare pflegschaftsbehördliche Maßnahmen nicht zu setzen seien.

**False Positives:**

- `Bezirksgericht werde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/10Ob21_15h`) (sent_id: `deanon_TRAIN/10Ob21_15h_17`)


Mit Urteil des Bezirksgerichts Bezirksgericht St. Pölten vom 21. 5. 2013 wurde die Klägerin zur Zahlung von 6.183,92 EUR sA an Sanierungskosten sowie zur Zahlung der Prozesskosten an den Betreiber eines Hoch- und Niederseilparks verurteilt.

**False Positives:**

- `Bezirksgericht St` — partial — pred is substring of gold: `Bezirksgericht St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht St. Pölten`(organisation)

**Example 6** (doc_id: `deanon_TRAIN/10Ob21_15h`) (sent_id: `deanon_TRAIN/10Ob21_15h_28`)


Weiters habe sie der Klägerin Zinsen und Prozesskosten, zu deren Zahlung sie im Verfahren vor dem Bezirksgericht Bezirksgericht Meidling verurteilt worden war, sowie die Kosten deren eigener Vertretung in diesem Verfahren zu ersetzen.

**False Positives:**

- `Bezirksgericht Bezirksgericht` — positional overlap with gold: `Bezirksgericht Meidling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Meidling`(organisation)

**Example 7** (doc_id: `deanon_TRAIN/10ObS150_17g`) (sent_id: `deanon_TRAIN/10ObS150_17g_10`)


Für ihn ist ein Sachwalter bestellt, der seit 2011 alle Angelegenheiten (§ 268 Abs 3 Z 3 ABGB) zu besorgen hat (siehe den Beschluss des Bezirksgericht Bezirksgericht Mattersburg vom 15.

**False Positives:**

- `Bezirksgericht Bezirksgericht` — positional overlap with gold: `Bezirksgericht Mattersburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Mattersburg`(organisation)

**Example 8** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__17`)


Indem das Bezirksgericht über die Jusepeitis&Niemöller Bildung GmbH eine (das Höchstmaß von somit 55 Tagessätzen übersteigende) Verbandsgeldbuße von 70 Tagessätzen verhängte, verletzte es § 4 Abs 3 VbVG).

**False Positives:**

- `Bezirksgericht über` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jusepeitis&Niemöller Bildung GmbH`(organisation)

**Example 9** (doc_id: `deanon_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_TRAIN/13Os7_20h_13Os8_20f__11`)


Im Protokoll über die Hauptverhandlung vor dem Bezirksgericht Innere Stadt Wien ist als Tag der Hauptverhandlung „23. 11. 2018“ angeführt (ON 18 S 1).

**False Positives:**

- `Bezirksgericht Innere` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 10** (doc_id: `deanon_TRAIN/13Os99_19m`) (sent_id: `deanon_TRAIN/13Os99_19m_12`)


Ein anderes Verständnis legt – entgegen der vom Berufungsgericht mit Verweis auf eine Literaturstelle (Hinterhofer/Oshidari, System des österreichischen Strafverfahrens Rz 10.89) vertretenen Ansicht – auch die historische Interpretation nicht nahe: Die im Verfahren vor dem Bezirksgericht schon in der Stammfassung der StPO vorgesehene Rechtsmittellegitimation des Privatbeteiligten (zum Nachteil des Angeklagten) wurde von der Rechtsprechung und überwiegend im Schrifttum zur früheren Rechtslage (mit Blick auf § 366 Abs 2 letzter Satz StPO idF vor BGBl 1978/169) dahin ausgelegt, dass dieser Berufung (nur) dann habe ergreifen können, wenn das Erstgericht eine Entschädigung (zumindest teilweise) zugesprochen hatte, nicht jedoch bei vollständiger Verweisung auf den Zivilrechtsweg.

**False Positives:**

- `Bezirksgericht schon` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_TRAIN/18ONc1_21y`) (sent_id: `deanon_TRAIN/18ONc1_21y_16`)


[5] Aufgrund des Verweises auf § 37 Abs 2 bis 5 JN ist für einen solchen Antrag das Bezirksgericht zuständig, in dessen Sprengel die Amtshandlung vorgenommen werden soll (HausmaningerinFasching/Konecny3§ 602 ZPO Rz 30).

**False Positives:**

- `Bezirksgericht zuständig` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_TRAIN/1Ob55_13i`) (sent_id: `deanon_TRAIN/1Ob55_13i_6`)


Mit der am 20. 8. 2012 beim Bezirksgericht Bezirksgericht Hallein eingebrachten Klage begehrte der Minderjährige von einem in Deutschland wohnhaften minderjährigen Beklagten Schadenersatz von 3.850 EUR sA und die Feststellung seiner Haftung für sämtliche aus dessen Steinwurf resultierenden Spät- und Dauerfolgen.

**False Positives:**

- `Bezirksgericht Bezirksgericht` — positional overlap with gold: `Bezirksgericht Hallein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Hallein`(organisation)

**Example 13** (doc_id: `deanon_TRAIN/1Ob55_13i`) (sent_id: `deanon_TRAIN/1Ob55_13i_69`)


8. 2012 beim gemäß Art 5 Nr 3 EuGVVO zuständigen Bezirksgericht Bezirksgericht Weiz (Gericht des Ortes, an dem das schädigende Ereignis eingetreten ist) im Elektronischen Rechtsverkehr eingebracht.

**False Positives:**

- `Bezirksgericht Bezirksgericht` — positional overlap with gold: `Bezirksgericht Weiz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Weiz`(organisation)

**Example 14** (doc_id: `deanon_TRAIN/2Nc17_17y`) (sent_id: `deanon_TRAIN/2Nc17_17y_4`)


Text Begründung: Die klagende Partei begehrt in ihrer beim Bezirksgericht Innere Stadt Wien am allgemeinen Gerichtsstand der beklagten Partei eingebrachten Klage Schadenersatz nach einem Verkehrsunfall auf der B 178 im Ortsgebiet von Going am Wilden Kaiser.

**False Positives:**

- `Bezirksgericht Innere` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 15** (doc_id: `deanon_TRAIN/2Nc17_17y`) (sent_id: `deanon_TRAIN/2Nc17_17y_11`)


Das Bezirksgericht Innere Stadt Wien hält die Delegierung für zweckmäßig.

**False Positives:**

- `Bezirksgericht Innere` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 16** (doc_id: `deanon_TRAIN/3Nc11_13t`) (sent_id: `deanon_TRAIN/3Nc11_13t_10`)


Für eine Unterlassungsexekution ist gemäß § 18 Z 4 zweiter Fall EO jenes Bezirksgericht zuständig, in dessen Sprengel die erste Exekutionshandlung, nämlich die Zustellung der Exekutionsbewilligung, zu bewirken ist.

**False Positives:**

- `Bezirksgericht zuständig` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_5`)


Für die Bewilligung und die Vollziehung der beabsichtigten Exekution gegen die Zweitbeklagte auf Urteilsveröffentlichung wird das Bezirksgericht Innere Stadt Wien als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Bezirksgericht Innere` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 18** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_8`)


Mit dem gegenständlichen Ordinationsantrag beantragen die Klägerinnen, der Oberste Gerichtshof möge das Bezirksgericht Innere Stadt Wien oder ein anderes Bezirksgericht als örtlich zuständiges Gericht für die Durchsetzung des Veröffentlichungsanspruchs gemäß § 354 EO gegen die Zweitbeklagte bestimmen.

**False Positives:**

- `Bezirksgericht Innere` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`
- `Bezirksgericht als` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 19** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_19`)


Dem Ordinationsantrag ist somit stattzugeben und zweckmäßigerweise das Bezirksgericht Innere Stadt Wien als zuständiges Gericht zu bestimmen.

**False Positives:**

- `Bezirksgericht Innere` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)

</details>

---

## `Regional Court Pattern`

**F1:** 0.159 | **Precision:** 0.670 | **Recall:** 0.090  

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
| 0.670 | 0.090 | 0.159 | 94 | 63 | 31 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 63 | 31 | 566 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc9_15b`) (sent_id: `deanon_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Mur Kraftalheim Holding GmbH, Gerald Zacharie, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Nexstein Textil GmbH, Dipl.-Ing. Lynn Forkarth, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |

**Missed by this rule (FN):**

- `Mur Kraftalheim Holding GmbH` (organisation)
- `Gerald Zacharie` (person)
- `Nexstein Textil GmbH` (organisation)
- `Dipl.-Ing. Lynn Forkarth` (person)

**Example 1** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_4`)


In Stattgebung der Nichtigkeitsbeschwerde wird das angefochtene Urteil aufgehoben, eine neue Hauptverhandlung angeordnet und die Sache an das Landesgericht Salzburg verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Example 2** (doc_id: `deanon_TRAIN/12Os107_11v`) (sent_id: `deanon_TRAIN/12Os107_11v_4`)


In Stattgebung sowie aus Anlass der Nichtigkeitsbeschwerde wird das angefochtene Urteil, das im Übrigen unberührt bleibt, in den Renata Himmeldirk betreffenden Schuldsprüchen B./I./ und II./ und demzufolge auch im Strafausspruch aufgehoben, eine neue Hauptverhandlung angeordnet und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an das Landesgericht Korneuburg verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Missed by this rule (FN):**

- `Himmeldirk` (person)

**Example 3** (doc_id: `deanon_TRAIN/12Os138_19i`) (sent_id: `deanon_TRAIN/12Os138_19i_6`)


Der dagegen gerichteten Beschwerde hatte das Landesgericht Innsbruck als Vollzugsgericht vom 13. Juni 2019, AZ 28 Bl 68/19p, nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgericht Innsbruck` | `Landesgericht Innsbruck` |

**Example 4** (doc_id: `deanon_TRAIN/12Os44_17p`) (sent_id: `deanon_TRAIN/12Os44_17p_4`)


Gründe:  Rechtliche Beurteilung Nach dem Norbert Naegelkraemer durch das Landesgericht Krems an der Donau am 4. Dezember 2015, GZ 16 Hv 32/15g-23, mehrerer Vergehen der gefährlichen Drohung nach § 107 Abs 1 StGB schuldig erkannt und zu einer teilbedingten Freiheitsstrafe verurteilt worden war, ordnete der Einzelrichter des genannten Landesgerichts nach Rechtskraft des Urteils die Zustellung der Aufforderung zum Strafantritt an den Verurteilten an.

| Predicted | Gold |
|---|---|
| `Landesgericht Krems` | `Landesgericht Krems` |

**Missed by this rule (FN):**

- `Naegelkraemer` (person)

**Example 5** (doc_id: `deanon_TRAIN/12Os71_19m_12Os72_19h_`) (sent_id: `deanon_TRAIN/12Os71_19m_12Os72_19h__5`)


Der dagegen gerichteten Beschwerde hatte das Landesgericht Innsbruck als Vollzugsgericht vom 17. Mai 2018, AZ 22 Bl 38/18f, 22 Bl 43/18s, nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgericht Innsbruck` | `Landesgericht Innsbruck` |

**Example 6** (doc_id: `deanon_TRAIN/13Os103_19z`) (sent_id: `deanon_TRAIN/13Os103_19z_12`)


Bei der Glaubwürdigkeitsbeurteilung ließ das Erstgericht weder die Divergenzen in den Angaben der Asli Dawids (vgl US 14) noch ihre Verurteilung durch das Landesgericht Feldkirch unberücksichtigt (vgl US 16).

| Predicted | Gold |
|---|---|
| `Landesgericht Feldkirch` | `Landesgericht Feldkirch` |

**Missed by this rule (FN):**

- `Dawids` (person)

**Example 7** (doc_id: `deanon_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_TRAIN/13Os110_19d_13Os111_19a__5`)


Das Urteil des Landesgerichts Eisenstadt vom 6. Juni 2017 (ON 155) wird aufgehoben, eine neue Hauptverhandlung angeordnet und die Sache an das Landesgericht Eisenstadt verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Eisenstadt` | `Landesgericht Eisenstadt` |

**Example 8** (doc_id: `deanon_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_TRAIN/13Os113_17t_13Os114_17i__6`)


Das Urteil des Landesgerichts Salzburg als Schöffengericht vom 28. Oktober 2015, GZ 41 Hv 49/15k-33, das im Übrigen unberührt bleibt, wird im Nikola Mikolajtschik betreffenden Strafausspruch aufgehoben und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an das Landesgericht Salzburg verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Missed by this rule (FN):**

- `Mikolajtschik` (person)

**Example 9** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__8`)


Mit zugleich gefasstem Beschluss sprach das Landesgericht Innsbruck gemäß § 265 StPO - ebenfalls unter Bestimmung einer dreijährigen Probezeit - die bedingte Entlassung aus dem im Urteilszeitpunkt noch nicht (durch Anrechnung der Vorhaft) verbüßten (unbedingten) Strafteil von einem Monat, zwanzig Tagen und einer Stunde aus (ON 48, nicht journalisierte Kopie des genannten Urteils).

| Predicted | Gold |
|---|---|
| `Landesgericht Innsbruck` | `Landesgericht Innsbruck` |

**Example 10** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__11`)


Unter einem fasste das Landesgericht Innsbruck den Beschluss, vom Widerruf der mit Urteil dieses Gerichts vom 6. März 2009, GZ 23 Hv 189/07m-104, gewährten bedingten Strafnachsicht abzusehen, die mit dem gemeinsam mit diesem Urteil ergangenen Beschluss gewährte bedingte Entlassung jedoch zu widerrufen (ON 49 S 3).

| Predicted | Gold |
|---|---|
| `Landesgericht Innsbruck` | `Landesgericht Innsbruck` |

**Example 11** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__13`)


Mit - unbekämpft in Rechtskraft erwachsenem - Beschluss vom 3. Februar 2012 (ON 54) rechnete das Landesgericht Innsbruck „gem § 400 StPO“ die in der Zeit vom 13. Dezember 2011, 17:00 Uhr, bis zum 23. Jänner 2012, 17:00 Uhr, im Verfahren AZ 27 HR 323/11h (= 20 Hv 43/12b) des Landesgerichts Feldkirch erlittene Verwahrungs- und Untersuchungshaft auf die mit Urteil vom 10. Jänner 2012 (ON 49) verhängte Freiheitsstrafe an (1) und sprach aus, dass der nach dieser Anrechnung aus dem genannten Urteil und dem gleichzeitig mit diesem gefassten Widerrufsbeschluss verbleibende Strafrest von einem Monat und zehn Tagen unter Bestimmung einer Probezeit von drei Jahren „bedingt nachgesehen“ werde (2).

| Predicted | Gold |
|---|---|
| `Landesgericht Innsbruck` | `Landesgericht Innsbruck` |

**Example 12** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__21`)


Da das Landesgericht Innsbruck hinsichtlich der mit - sogleich in Rechtskraft erwachsenem (ON 49 S 4) - Urteil vom 10. Jänner 2012 ausgesprochenen (ON 49 S 2) und der mit dem unter einem gefassten Widerrufsbeschluss aktualisierten (ON 49 S 3; siehe dazu aber (3) des Erkenntnisses) Freiheitsstrafe keine Strafvollzugsanordnung erließ, verletzte es somit § 397 erster Satz StPO iVm § 3 Abs 1 StVG.

| Predicted | Gold |
|---|---|
| `Landesgericht Innsbruck` | `Landesgericht Innsbruck` |

**Example 13** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__26`)


Ein Nachteil entstand der Verurteilten dadurch auch in Bezug auf die einen Monat übersteigende Untersuchungshaftzeit nicht, weil das Landesgericht Feldkirch zu AZ 20 Hv 43/12b - unter Missachtung des § 38 Abs 1 StGB - die vom Punkt 1 des Beschlusses des Landesgerichts Innsbruck vom 3. Februar 2012 (ON 54) umfasste Haftzeit (erneut zur Gänze) auf die im bezeichneten Verfahren verhängte (unbedingte) Freiheitsstrafe anrechnete.

| Predicted | Gold |
|---|---|
| `Landesgericht Feldkirch` | `Landesgericht Feldkirch` |

**Example 14** (doc_id: `deanon_TRAIN/15Os43_13g`) (sent_id: `deanon_TRAIN/15Os43_13g_5`)


Das Urteil, das im Übrigen unberührt bleibt, wird in Punkt A./2./ des Schuldspruchs sowie im Strafausspruch aufgehoben und es wird die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an das Landesgericht Korneuburg verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 15** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Herbes&Vißers Heizung GmbH, Waldemar Lokämper, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Traun-Luftfahrt GmbH, VetR DDr. Walter Stuehrmann, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

| Predicted | Gold |
|---|---|
| `Landesgericht Feldkirch` | `Landesgericht Feldkirch` |

**Missed by this rule (FN):**

- `Landesgericht Wiener Neustadt` (organisation)
- `Herbes&Vißers Heizung GmbH` (organisation)
- `Waldemar Lokämper` (person)
- `Traun-Luftfahrt GmbH` (organisation)
- `VetR DDr. Walter Stuehrmann` (person)

**Example 16** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_7`)


Die Klägerin begehrte die Delegierung des Verfahrens gemäß § 31 JN an das Landesgericht Feldkirch.

| Predicted | Gold |
|---|---|
| `Landesgericht Feldkirch` | `Landesgericht Feldkirch` |

**Example 17** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_23`)


Im vorliegenden Fall haben sowohl die Klägerin als auch das vorlegende Gericht zutreffend auf jene Umstände hingewiesen, die insgesamt eine Delegierung an das Landesgericht Feldkirch zweckmäßig erscheinen lassen (vgl dazu RIS-Justiz RS0046540), kann doch vor diesem Gericht unter Wahrung des Unmittelbarkeitsgrundsatzes das gesamte Beweisverfahren in einem Zug durchgeführt werden, was typischerweise nicht nur zu einer Erleichterung der Gerichtstätigkeit, sondern auch zu einer Verbilligung und Verkürzung des Verfahrens führt.

| Predicted | Gold |
|---|---|
| `Landesgericht Feldkirch` | `Landesgericht Feldkirch` |

**Example 18** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_6`)


Nach Zurück- bzw Abweisung seiner Begehren in erster Instanz lehnte er wiederholt Richter des Landesgerichts Leoben und des Oberlandesgerichts Graz erfolglos ab (vgl Landesgericht Leoben 2 Nc 24/11d, 2 Nc 25/11a, 2 Nc 28/11t;

| Predicted | Gold |
|---|---|
| `Landesgericht Leoben` | `Landesgericht Leoben` |

**Example 19** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_9`)


Am 26. Februar 2013 lehnte er den Vorsitzenden des Ablehnungssenats beim Landesgericht Leoben als befangen und nach Zurückweisung dieses Antrags (2 Nc 3/13v) die Entscheidungsträger dieses Beschlusses als befangen ab.

| Predicted | Gold |
|---|---|
| `Landesgericht Leoben` | `Landesgericht Leoben` |

**Example 20** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_11`)


Diese Ablehnung wies der Ablehnungssenat beim Landesgericht Leoben (ohne Beteiligung des abgelehnten Richters) mit Beschluss vom 4. Dezember 2013, 2 Nc 31/13m, zurück.

| Predicted | Gold |
|---|---|
| `Landesgericht Leoben` | `Landesgericht Leoben` |

**Example 21** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_6`)


Text Gründe: Mit dem angefochtenen Erkenntnis wurde Dr. Nadja Köpers, Rechtsanwalt in Laahen 3, 3240 Pölla, Österreich, wegen des Verstoßes gegen die Bestimmungen des § 9 (Abs 1) RAO und des § 2 RL-BA der Disziplinarvergehen der Verletzung von Berufspflichten und der Beeinträchtigung von Ehre oder (richtig:) Ansehen des Standes nach § 1 Abs 1 erster und zweiter Fall DSt schuldig erkannt, weil er als Rechtsvertreter der Ehegatten Roman und Elfriede Jakubus in Anträgen auf Aufschiebung der Zwangsversteigerungen für seine Mandanten vom 5. September 2013 in näher bezeichneten Verfahren des Bezirksgerichts Innsbruck und des Bezirksgerichts Amstetten sowie in einer näher genannten Feststellungsklage an das Landesgericht Linz vom 7. Oktober 2013 und in einer Impugnationsklage an das Bezirksgericht Amstetten vom 10. Oktober 2013 jeweils vorgebracht hatte, seine Mandanten hätten sämtliche Verpflichtungen aus einer mit der Bachseewald Heizung AG abgeschlossenen Vereinbarung vom 11. Dezember 2012, insbesondere jene zur unwiderruflichen Antragstellung auf Aufhebung der Höfeeigenschaft einer näher bezeichnenden Liegenschaft in Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich, eingehalten, obwohl ihm zum Zeitpunkt der Antragstellung und Klagseinbringung bekannt war, dass der Antrag auf Aufhebung der Höfeeigenschaft vom 13. Dezember 2012 bereits am 14. Juni 2013 von Roman Janis, durch ihn vertreten, entgegen der zuvor genannten Vereinbarung vom 11. Dezember 2012 wieder zurückgezogen worden war.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |

**Missed by this rule (FN):**

- `Dr. Nadja Köpers` (person)
- `Laahen 3, 3240 Pölla, Österreich` (address)
- `Jakubus` (person)
- `Bezirksgericht Amstetten` (organisation)
- `Bachseewald Heizung AG` (organisation)
- `Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich` (address)
- `Roman Janis` (person)

**Example 22** (doc_id: `deanon_TRAIN/2Ob63_11w`) (sent_id: `deanon_TRAIN/2Ob63_11w_109`)


Nr 18/2008 habe ein anderer Senat des Oberlandesgerichts Linz bzw das Landesgericht Salzburg die dort geregelten Pflegeaufwandsätze zuerkannt.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Example 23** (doc_id: `deanon_TRAIN/3Ob192_11y`) (sent_id: `deanon_TRAIN/3Ob192_11y_11`)


Seine am 4. Februar 2009 eingebrachte Oppositionsklage, deren Begehren darauf abzielt, dass der Anspruch der Beklagten aus dem Unterhaltsvergleich „sowie auf Unterhalt insgesamt“ erloschen ist, stützt derKlägerzusammengefasst auf eine Unterhaltsverwirkung iSd § 94 Abs 2 Satz 2 ABGB: Die Beklagte habe in dem gegen den Kläger geführten Strafverfahren vor dem Landesgericht Salzburg (31 Hv 139/07k), bezogen auf einen Vorfall am 3. Jänner 2006, unrichtig ausgesagt.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Example 24** (doc_id: `deanon_TRAIN/3Ob192_11y`) (sent_id: `deanon_TRAIN/3Ob192_11y_21`)


Unter anderem aufgrund dieses Vorfalls wurde der Kläger im Strafverfahren vor dem Landesgericht Salzburg wegen des Vergehens des Imstichlassens eines Verletzten nach § 94 StGB angeklagt.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Example 25** (doc_id: `deanon_TRAIN/3Ob203_11s`) (sent_id: `deanon_TRAIN/3Ob203_11s_14`)


Mit Beschluss des Landesgerichts Salzburg vom 18. Mai 2011, AZ 22 R 192/11f, 22 R 193/11b, wies das Landesgericht Salzburg die Berufung der Antragsteller mit der Begründung zurück, sie seien im Verfahren mehrfach und umfassend darüber belehrt worden, dass die von ihnen angestrebte Umbestellung der Verfahrenshelfer mangels Vorliegens der gesetzlichen Voraussetzungen nicht stattfinden könne.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Example 26** (doc_id: `deanon_TRAIN/3Ob248_10g`) (sent_id: `deanon_TRAIN/3Ob248_10g_6`)


Mit rechtskräftigem Urteil vom 10. Mai 2007, AZ 19 Cg 136/06a, hat das Landesgericht Leoben infolge erfolgreicher Irrtumsanfechtung (im Hinblick auf die fehlende Vorschadensfreiheit des Fahrzeugs) die nunmehrige Oppositionsklägerin schuldig erkannt, an Philippa Carau Zug um Zug gegen Rückgabe des Pkw einen Betrag von 71.320 EUR sA zu bezahlen.

| Predicted | Gold |
|---|---|
| `Landesgericht Leoben` | `Landesgericht Leoben` |

**Missed by this rule (FN):**

- `Philippa Carau` (person)

**Example 27** (doc_id: `deanon_TRAIN/3Ob32_17b`) (sent_id: `deanon_TRAIN/3Ob32_17b_6`)


Text Begründung: Am 4. Oktober 2010 erließ das Landesgericht Mailand (Tribunale Ordinario di Milano) über Antrag der Betreibenden, einer Gesellschaft mit Sitz in Italien, den elektronischen Mahnbescheid (decreto ingiunitivo telematico) zur Zahl 34300/2010, mit dem der Verpflichteten, einer GmbH mit Sitz in Wien, die in Geschäftsverbindung mit der Betreibenden stand, die Zahlung von 522.094,53 EUR sA an die Betreibende innerhalb von 50 Tagen nach Bekanntmachung des Mahnbescheids aufgetragen wurde.

| Predicted | Gold |
|---|---|
| `Landesgericht Mailand` | `Landesgericht Mailand` |

**Example 28** (doc_id: `deanon_TRAIN/3Ob32_17b`) (sent_id: `deanon_TRAIN/3Ob32_17b_7`)


Dieser enthielt den Hinweis, dass die Verpflichtete Anspruch darauf habe, vor dem Landesgericht Mailand innerhalb von 50 Tagen nach der Bekanntmachung Einspruch zu erheben, widrigenfalls der Mahnbescheid für endgültig und vollstreckbar erklärt werde.

| Predicted | Gold |
|---|---|
| `Landesgericht Mailand` | `Landesgericht Mailand` |

**Example 29** (doc_id: `deanon_TRAIN/4Nc3_12x`) (sent_id: `deanon_TRAIN/4Nc3_12x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel und Dr. Jensik als weitere Richter in der beim Landesgericht Innsbruck zu AZ 59 Cg 92/11x anhängigen Rechtssache der klagenden Partei Rudigkeit Finanzen GmbH, Ing. Sascha Rohkrämer, vertreten durch Mag. Heinz Heher, Rechtsanwalt in Wien, gegen die beklagte Partei Suddorftra Manufaktur GmbH, Ludmilla Nottelmann, vertreten durch Dr. Adrian Hollaender, Rechtsanwalt in Innsbruck, wegen Unterlassung, Urteilsveröffentlichung und 67.606 EUR sA, über die Delegierungsanträge der beklagten Partei gemäß § 31 Abs 2 JN, folgenden Beschluss gefasst:  Spruch Die Anträge der beklagten Partei, die Rechtssache an das „Landesgericht Wien“ bzw Handelsgericht Wien zu delegieren, werden abgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Innsbruck` | `Landesgericht Innsbruck` |
| `Landesgericht Wien` | `Landesgericht Wien` |

**Missed by this rule (FN):**

- `Rudigkeit Finanzen GmbH` (organisation)
- `Ing. Sascha Rohkrämer` (person)
- `Suddorftra Manufaktur GmbH` (organisation)
- `Ludmilla Nottelmann` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/12Os34_19w`) (sent_id: `deanon_TRAIN/12Os34_19w_4`)


Text Gründe: Im Ermittlungsverfahren gegen Viktor Mittermair und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und 3 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 703 St 3/11t (nunmehr AZ 713 St 24/18i) der Staatsanwaltschaft Wien, stellte der Beschuldigte Dr. Stefan Tolmin mit Schriftsatz vom 29. November 2017 – soweit im Folgenden von Relevanz – den Antrag auf Einstellung des Ermittlungsverfahrens „gemäß § 108 StPO“ (ON 558), welchen das Landesgericht für Strafsachen Wien mit Beschluss vom 22. Juni 2018, AZ 352 HR 214/11x, abwies (ON 644).

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Viktor Mittermair`(person)
- `Tolmin`(person)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 1** (doc_id: `deanon_TRAIN/13Os22_12b_13Ns16_12z_`) (sent_id: `deanon_TRAIN/13Os22_12b_13Ns16_12z__5`)


Text Gründe: Das Landesgericht für Strafsachen Wien verhängte mit Beschluss vom 9. Dezember 2011 über Mag. Türkan Laurin Bickmann die Untersuchungshaft aus den Gründen der Tatbegehungsgefahr nach § 173 Abs 2 Z 3 lit b und lit d StPO (ON 12).

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Wien`(organisation)
- `Laurin Bickmann`(person)

**Example 2** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__6`)


Dem Landesgericht für Strafsachen Graz wird ein Vorgehen gemäß §§ 14 und 15 dieser Verordnung aufgetragen.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Strafsachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Graz`(organisation)

**Example 3** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__23`)


Seither besteht das Landesgericht als Schöffengericht aus nur einem (Berufs-)Richter und zwei Schöffen (§ 32 Abs 1 dritter Satz StPO).

**False Positives:**

- `Landesgericht als` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__28`)


8. Das Landesgericht für Strafsachen Graz hätte demnach die Staatsanwaltschaft und den Angeklagten von der dauernden Verhinderung des Vorsitzenden des Schöffengerichts in Kenntnis setzen und vor Betrauung eines anderen Richters mit der Urteilsausfertigung nach ihrem Einverständnis fragen müssen.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Strafsachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Graz`(organisation)

**Example 5** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__30`)


Mit Blick auf § 292 letzter Satz StPO sah sich der Oberste Gerichtshof veranlasst, dem Landesgericht für Strafsachen Graz aufzutragen, gemäß §§ 14 und 15 der Kaiserlichen Verordnung vorzugehen.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Strafsachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Graz`(organisation)

**Example 6** (doc_id: `deanon_TRAIN/13Os34_19b`) (sent_id: `deanon_TRAIN/13Os34_19b_5`)


Dieser Beschluss wird aufgehoben und es wird dem Landesgericht für Strafsachen Graz aufgetragen, im Verfahren AZ 16 Hv 32/15a über den Widerruf zu entscheiden.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Strafsachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Graz`(organisation)

**Example 7** (doc_id: `deanon_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_TRAIN/13Os7_20h_13Os8_20f__5`)


In Stattgebung des Antrags der Generalprokuratur wird im außerordentlichen Weg die Wiederaufnahme des Berufungsverfahrens verfügt, der Beschluss des Landesgerichts für Strafsachen Wien vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), aufgehoben und die Sache zur neuerlichen Entscheidung über die Berufung des Angeklagten gegen das Urteil des Bezirksgerichts Innere Stadt Wien vom 27. November 2018 (ON 19 der U-Akten) an das Landesgericht für Strafsachen Wien verwiesen.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Wien`(organisation)

**Example 8** (doc_id: `deanon_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_TRAIN/13Os7_20h_13Os8_20f__10`)


Die am 22. Februar 2019 – innerhalb der Frist des § 467 Abs 1 StPO (vgl Zustellnachweis an ON 19) – ausgeführte Berufung des Robert Unterbusch (ON 21) wies das Landesgericht für Strafsachen Wien als Berufungsgericht mit Beschluss vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23), gemäß § 470 Z 1 StPO als unzulässig zurück, weil die am 27. November 2018 zur Post gegebene Rechtsmittelanmeldung gegen das am 23. November 2018 verkündete Urteil verspätet gewesen sei.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unterbusch`(person)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 9** (doc_id: `deanon_TRAIN/13Os99_19m`) (sent_id: `deanon_TRAIN/13Os99_19m_7`)


Die gegen diesen Ausspruch gerichtete Berufung des Privatbeteiligten (ON 23) wies das Oberlandesgericht Graz mit dem nunmehr angefochtenen Beschluss im Wesentlichen mit der Begründung zurück, auch im Verfahren vor dem Landesgericht als Einzelrichter stehe dem Privatbeteiligten die Berufung nur bei vollständiger Verweisung mit seinen Ansprüchen auf den Zivilrechtsweg (trotz Verurteilung) offen, während die Höhe des Zuspruchs nicht bekämpfbar sei (vgl zum kollegialgerichtlichen Verfahren § 283 Abs 4 iVm § 366 Abs 3 StPO).

**False Positives:**

- `Landesgericht als` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_TRAIN/13Os99_19m`) (sent_id: `deanon_TRAIN/13Os99_19m_11`)


Diese Regelung findet zufolge § 489 Abs 1 StPO auch im Verfahren vor dem Landesgericht als Einzelrichter Anwendung.

**False Positives:**

- `Landesgericht als` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_TRAIN/14Os132_10h`) (sent_id: `deanon_TRAIN/14Os132_10h_4`)


Text Gründe: Gegen Tomsilav Alexejenko ist beim Landesgericht für Strafsachen Wien ein - im Stadium der Hauptverhandlung befindliches - Verfahren wegen der Verbrechen des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und nach § 28a Abs 1 fünfter Fall, Abs 4 Z 3 SMG anhängig, in dem sich der Angeklagte seit 5. April 2010 in Untersuchungshaft befindet (ON 20).

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alexejenko`(person)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 12** (doc_id: `deanon_TRAIN/14Os63_12i`) (sent_id: `deanon_TRAIN/14Os63_12i_8`)


Mit Erkenntnis des Obersten Gerichtshofs vom 30. August 2011, AZ 14 Os 48/11g (ON 74 der Hv-Akten), wurde das Urteil, das im Übrigen unberührt blieb, in teilweiser Stattgebung der dagegen erhobenen Nichtigkeitsbeschwerde des Angeklagten im Schuldspruch I und demzufolge auch im Strafausspruch aufgehoben, im Umfang der Aufhebung eine neue Hauptverhandlung angeordnet und die Sache an das Landesgericht St. Pölten verwiesen.

**False Positives:**

- `Landesgericht St` — partial — pred is substring of gold: `Landesgericht St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht St. Pölten`(organisation)

**Example 13** (doc_id: `deanon_TRAIN/15Os110_17s`) (sent_id: `deanon_TRAIN/15Os110_17s_10`)


Aus Anlass eines vom Angeklagten am 17. Februar 2017 eingebrachten Antrags auf Aufhebung der Untersuchungshaft (ON 95) setzte das Landesgericht für Strafsachen Graz mit Beschluss vom 23. Februar 2017 die am 7. September 2016 verhängte (ON 11) – und danach wiederholt prolongierte (ON 32, 71) – Untersuchungshaft aus den Haftgründen der Flucht- und der Tatbegehungsgefahr nach § 173 Abs 2 Z 1 und Z 3 lit a StPO fort (ON 100).

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Strafsachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Graz`(organisation)

**Example 14** (doc_id: `deanon_TRAIN/15Os43_13g`) (sent_id: `deanon_TRAIN/15Os43_13g_12`)


Rechtliche Beurteilung Das Urteil des Landesgerichts Korneuburg vom 13. Juni 2012, GZ 505 Hv 5/11x-69, steht - wie die Generalprokuratur in ihrer Nichtigkeitsbeschwerde zur Wahrung des Gesetzes zutreffend ausführt - in seinem Punkt A./2./ mit dem Gesetz nicht im Einklang: Gemäß der auch für das Verfahren vor dem Landesgericht als Einzelrichter geltenden (§ 488 Abs 1 StPO) Bestimmung des § 270 Abs 4 StPO hat eine - unter den in dieser Vorschrift genannten, hier vorliegenden Voraussetzungen zulässigerweise - gekürzte Urteilsaus- fertigung die in § 270 Abs 2 StPO angeführten Angaben mit Ausnahme der Entscheidungsgründe, also auch die in § 260 StPO (§ 270 Abs 4 Z 1 StPO) genannten Punkte zu enthalten.

**False Positives:**

- `Landesgericht als` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Herbes&Vißers Heizung GmbH, Waldemar Lokämper, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Traun-Luftfahrt GmbH, VetR DDr. Walter Stuehrmann, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

**False Positives:**

- `Landesgericht Wiener` — partial — pred is substring of gold: `Landesgericht Wiener Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Wiener Neustadt`(organisation)
- `Herbes&Vißers Heizung GmbH`(organisation)
- `Waldemar Lokämper`(person)
- `Traun-Luftfahrt GmbH`(organisation)
- `VetR DDr. Walter Stuehrmann`(person)
- `Landesgericht Feldkirch`(organisation)

**Example 16** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_5`)


Text Begründung: Der Kläger macht in einem Verfahren vor dem Landesgericht Leoben Amtshaftungsansprüche gegen die Republik Österreich, sonstige Schadenersatzansprüche gegen eine Journalistin und die Inhaberin eines Printmediums sowie Feststellungsansprüche gegen alle beklagten Parteien geltend.

**False Positives:**

- `Landesgericht Leoben` — partial — pred is substring of gold: `Landesgericht Leoben Amtshaftungsansprüche`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Leoben Amtshaftungsansprüche`(organisation)

**Example 17** (doc_id: `deanon_TRAIN/1Ob78_22k`) (sent_id: `deanon_TRAIN/1Ob78_22k_8`)


Das Landesgericht für Zivilrechtssachen Wien gab der gegen das Ersturteil gerichteten Berufung des Beklagten mit dem (dessen Verfahrenshelfer am 17.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 18** (doc_id: `deanon_TRAIN/1Ob78_22k`) (sent_id: `deanon_TRAIN/1Ob78_22k_11`)


diese Entscheidung wurde vom Landesgericht für Zivilrechtssachen Wien später bestätigt.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 19** (doc_id: `deanon_TRAIN/3Ob1_20y`) (sent_id: `deanon_TRAIN/3Ob1_20y_9`)


Der von den Klägern aufgrund dieses Urteils beim Bezirksgericht Melk eingebrachte, in erster Instanz erfolgreiche Antrag auf Bewilligung der Exekution gemäß § 350 EO zur Durchsetzung der Einverleibung der Dienstbarkeit wurde vom Landesgericht St. Pölten als Rekursgericht mit Beschluss vom 1. Februar 2018 mit der Begründung abgewiesen, dass sich die dem Titel angeschlossenen Pläne (Beilage ./B1 und ON 71) nicht ohne weiteres in Übereinstimmung bringen ließen, weshalb der Verlauf des Servitutswegs dem Titel nicht eindeutig entnommen werden könne.

**False Positives:**

- `Landesgericht St` — partial — pred is substring of gold: `Landesgericht St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Melk`(organisation)
- `Landesgericht St. Pölten`(organisation)

**Example 20** (doc_id: `deanon_TRAIN/4Fsc1_10z`) (sent_id: `deanon_TRAIN/4Fsc1_10z_5`)


Diesen Ablehnungsantrag hat das Landesgericht für Zivilrechtssachen Wien am 19.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 21** (doc_id: `deanon_TRAIN/4Fsc1_10z`) (sent_id: `deanon_TRAIN/4Fsc1_10z_11`)


9. 2009 hat das Landesgericht für Zivilrechtssachen Wien am 12.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 22** (doc_id: `deanon_TRAIN/5Nc20_14g`) (sent_id: `deanon_TRAIN/5Nc20_14g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und die Hofrätin Dr. Lovrek sowie den Hofrat Dr. Höllwerth als weitere Richter in der Rechtssache der klagenden Partei Dr. Sean Schoenenborn, gegen die beklagte Partei Dr. Hagen Kanat, vertreten durch Eisenberger & Herzog Rechtsanwalts GmbH in Graz, wegen 234.164,98 EUR sA, über den Delegierungsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, gemäß § 31 JN anstelle des Landesgerichts für Zivilrechtssachen Graz das Landesgericht Wiener Neustadt, in eventu das Landesgericht Leoben, zur Verhandlung und Entscheidung dieser Rechtssache zu bestimmen, wird abgewiesen.

**False Positives:**

- `Landesgericht Wiener` — partial — pred is substring of gold: `Landesgericht Wiener Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Sean Schoenenborn`(person)
- `Dr. Hagen Kanat`(person)
- `Herzog Rechtsanwalts GmbH`(organisation)
- `Landesgericht Wiener Neustadt`(organisation)
- `Landesgericht Leoben`(organisation)

**Example 23** (doc_id: `deanon_TRAIN/5Nc20_14g`) (sent_id: `deanon_TRAIN/5Nc20_14g_6`)


Der Kläger beantragte die Delegation der Rechtsache an das Landesgericht Wiener Neustadt, in eventu das Landesgericht Leoben.

**False Positives:**

- `Landesgericht Wiener` — partial — pred is substring of gold: `Landesgericht Wiener Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Wiener Neustadt`(organisation)
- `Landesgericht Leoben`(organisation)

**Example 24** (doc_id: `deanon_TRAIN/5Nc20_14g`) (sent_id: `deanon_TRAIN/5Nc20_14g_8`)


Das Landesgericht für Zivilrechtssachen Graz erachtete eine Delegierung nicht als zweckmäßig.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_TRAIN/6Ob16_20a`) (sent_id: `deanon_TRAIN/6Ob16_20a_5`)


Text Begründung: Mit der beim Landesgericht für Zivilrechtssachen Wien eingebrachten Klage begehrt die Klägerin von der in Wien wohnhaften Beklagten die Zahlung von 422.136,06 EUR sA und erhebt diverse Eventualbegehren.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 26** (doc_id: `deanon_TRAIN/6Ob240_20t`) (sent_id: `deanon_TRAIN/6Ob240_20t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie durch die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Firmenbuchsache der zu FN FN912691n beim Landesgericht Landesgericht Klagenfurt eingetragenen Holtschmidt Versicherung GmbH mit Sitz in der politischen Gemeinde LG Wels, über den Revisionsrekurs der Lohneis Pflege gesellschaft mbH, Auf der Werzer Leitn 27, 9560 Klausen, Österreich, vertreten durch Dr. Robert Mogy, Rechtsanwalt in Klagenfurt, gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. Oktober 2020, GZ 4 R 153/20g-8, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen (§ 71 Abs 3 AußStrG iVm § 15 Abs 2 FBG).

**False Positives:**

- `Landesgericht Landesgericht` — positional overlap with gold: `Landesgericht Klagenfurt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FN912691n`(business_register_number)
- `Landesgericht Klagenfurt`(organisation)
- `Holtschmidt Versicherung GmbH`(organisation)
- `LG Wels`(organisation)
- `Lohneis Pflege gesellschaft mbH`(organisation)
- `Auf der Werzer Leitn 27, 9560 Klausen, Österreich`(address)

**Example 27** (doc_id: `deanon_TRAIN/6Ob82_15z`) (sent_id: `deanon_TRAIN/6Ob82_15z_12`)


Das Landesgericht für Zivilrechtssachen Wien wies mit Beschluss vom 22. 4. 2014 (40 R 94/14s) den Rekurs (32 Nc 121/13d-20) und mit Beschluss vom 14.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 28** (doc_id: `deanon_TRAIN/6Ob82_15z`) (sent_id: `deanon_TRAIN/6Ob82_15z_14`)


Mit Beschluss vom 11. 9. 2014, 33 Nc 34/14z-6, wies das Landesgericht für Zvilrechtssachen Wien den auf § 20 Abs 1 Z 5 JN gestützten Ablehnungsantrag des Beklagten gegen eine Richterin, die an der Fassung des Beschlusses vom 14.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_TRAIN/6Ob82_15z`) (sent_id: `deanon_TRAIN/6Ob82_15z_17`)


Das Oberlandesgericht Wien als Rekursgericht stellte mit Beschluss vom 22. 10. 2014, 13 R 170/14m-10, dem Landesgericht für Zivilrechtssachen Wien den Rekurs mit dem Auftrag zurück, das Verbesserungsverfahren zur Beseitigung des Formgebrechens der fehlenden Unterschrift eines Rechtsanwalts einzuleiten.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

</details>

---

## `Bank and Other Org`

**F1:** 0.039 | **Precision:** 0.667 | **Recall:** 0.020  

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
| 0.667 | 0.020 | 0.039 | 21 | 14 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 14 | 7 | 600 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob23_14a`) (sent_id: `deanon_TRAIN/10Ob23_14a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Aurelia von der Lei, geboren am 10. September 1997, in Pflege und Erziehung der Mutter Univ.-Prof.in Marceline Siladji, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Gmunden, 4810 Gmunden, Esplanade 10), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Linz, gegen den Beschluss des Landesgerichts Wels als Rekursgericht vom 15. Jänner 2014, GZ 21 R 298/13t-38, womit der Beschluss des Bezirksgerichts Gmunden vom 18. Oktober 2013, GZ 1 Pu 223/09k-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bezirkshauptmannschaft Gmunden` | `Bezirkshauptmannschaft Gmunden` |

**Missed by this rule (FN):**

- `Aurelia von der Lei` (person)
- `Univ.-Prof.in Marceline Siladji` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob2_14p`) (sent_id: `deanon_TRAIN/10Ob2_14p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Calvin Mützlaff, geboren am Volker Scheffski, Jaden Jurkutaitis, geboren am 8. Dezember 1982 und PhD Karim Trieber, geboren am 11. Januar 1975, in Pflege und Erziehung der Mutter StR Lara Jungnikl, vertreten durch das Land Vorarlberg als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Feldkirch, Schlossgraben 1, 6800 Feldkirch), wegen Gewährung von Unterhaltsvorschuss, über den Revisionsrekurs des Vaters RgR Dipl.-Ing. Quirin Bagemühl, vertreten durch Mag. Hans-Christian Obernberger, Rechtsanwalt in Feldkirch, gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 12. Juli 2011, GZ 3 R 198/11g, 3 R 199/11d, 3 R 200/11a-18, womit die Beschlüsse des Bezirksgerichts Feldkirch vom 18. Mai 2011, GZ 12 Pu 141/11f-4 bis 6, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirkshauptmannschaft Feldkirch` | `Bezirkshauptmannschaft Feldkirch` |

**Missed by this rule (FN):**

- `Calvin Mützlaff` (person)
- `Volker Scheffski` (person)
- `Jaden Jurkutaitis` (person)
- `8. Dezember 1982` (date)
- `PhD Karim Trieber` (person)
- `11. Januar 1975` (date)
- `StR Lara Jungnikl` (person)
- `RgR Dipl.-Ing. Quirin Bagemühl` (person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob30_14f`) (sent_id: `deanon_TRAIN/10Ob30_14f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch und Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der minderjährigen Thobias Altroggen, geboren am 16. März 2008, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Wien-Umgebung, Fachgebiet Jugendwohlfahrt), 3400 Klosterneuburg, Leopoldstraße 21, über das als „Berufung“ bezeichnete Rechtsmittel des Vaters Ignaz Dippert, gegen den Beschluss des Landesgerichts Korneuburg als Rekursgericht vom 25. März 2013, GZ 23 R 30/13v-53, womit der Beschluss des Bezirksgerichts Schwechat vom 27. August 2012, GZ 8 Pu 190/11i-39, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.

| Predicted | Gold |
|---|---|
| `Bezirkshauptmannschaft Wien` | `Bezirkshauptmannschaft Wien` |

**Missed by this rule (FN):**

- `Thobias Altroggen` (person)
- `16. März 2008` (date)
- `Ignaz Dippert` (person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob30_19p`) (sent_id: `deanon_TRAIN/10Ob30_19p_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der minderjährigen Franziska Dreikluft, geboren 3. November 2009, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Melk, 3390 Melk, Abt Karl-Straße 25a) wegen Unterhaltsvorschüssen, über den Revisionsrekurs des Kindes gegen den Beschluss des Landesgerichts St. Pölten als Rekursgericht vom 23. Jänner 2019, GZ 23 R 6/19h-52, mit dem der Beschluss des Bezirksgerichts Melk vom 21. November 2018, GZ 22 Pu 194/16m-42, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bezirkshauptmannschaft Melk` | `Bezirkshauptmannschaft Melk` |

**Missed by this rule (FN):**

- `Franziska Dreikluft` (person)
- `3. November` (date)

**Example 4** (doc_id: `deanon_TRAIN/3Ob26_23d`) (sent_id: `deanon_TRAIN/3Ob26_23d_52`)


Vor diesem Hintergrund sprach der Verfassungsgerichtshof aus, dass durch die Öffentlicherklärung einesin der Natur schon bestehendenWeges durch Verordnung mangels Eigentumserwerbs in gesetzwidriger Weise Gemeingebrauch begründet werde.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 5** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_67`)


In den vonRohregger(aaO) zitierten Entscheidungen bejahen auch der Verfassungsgerichtshof (B 1050/09) und der Verwaltungsgerichtshof (AW 2012/01/0032) die Bedeutung des § 10 RAO und der Vorgängerbestimmung des § 10 RL-BA 2015 für das öffentliche Interesse an dem Verbot der Doppelvertretung, weil es dem Schutz der durch einen Rechtsanwalt vertretenen Parteien diene, seine Einhaltung für das zwischen Rechtsanwalt und Klient bestehende Treueverhältnis für wesentlich erachtet werde und für das allgemeine Bild der Anwaltschaft in der Öffentlichkeit von Bedeutung sei.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 6** (doc_id: `deanon_TRAIN/5Ob31_16v`) (sent_id: `deanon_TRAIN/5Ob31_16v_15`)


Weiters wolle die Rechtssache gemäß Art 89 B-VG dem Verfassungsgerichtshof sowie gemäß Art 267 AEUV dem Europäischen Gerichtshof zur Prüfung vorgelegt werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 7** (doc_id: `deanon_TRAIN/8Ob141_19x`) (sent_id: `deanon_TRAIN/8Ob141_19x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn, den Hofrat Dr. Stefula und die Hofrätin Mag. Wessely-Kristöfel als weitere Richter in der Pflegschaftssache der Antragstellerin mj RgR Linn Neiheiser, geboren am 10. Februar 2008, in Unterhaltsangelegenheiten vertreten durch die Bezirkshauptmannschaft Bregenz, 6901 Bregenz, Bahnhofstraße 41, wegen Unterhalt, über den Revisionsrekurs der Antragstellerin gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 7. August 2019, GZ 2 R 170/19v-33, mit dem der Beschluss des Bezirksgerichts Bregenz vom 4. Juni 2019, GZ 9 Pu 315/19d-28, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bezirkshauptmannschaft Bregenz` | `Bezirkshauptmannschaft Bregenz` |

**Missed by this rule (FN):**

- `RgR Linn Neiheiser` (person)
- `10. Februar` (date)

**Example 8** (doc_id: `deanon_TRAIN/8Ob141_19x`) (sent_id: `deanon_TRAIN/8Ob141_19x_8`)


Die bis zur Rechtskraft dieses Beschlusses fällig gewordenen Beträge sind abzüglich bereits geleisteter Zahlungen binnen 14 Tagen, die hinkünftig fällig werdenden bis zum Ersten eines jeden Monats im Voraus zu Handen des jeweiligen gesetzlichen Vertreters, das ist derzeit die Bezirkshauptmannschaft Bregenz, zu leisten.

| Predicted | Gold |
|---|---|
| `Bezirkshauptmannschaft Bregenz` | `Bezirkshauptmannschaft Bregenz` |

**Example 9** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_29`)


Der Verwaltungsgerichtshof behob allein einen Bescheid, mit dem ein Antrag auf eine solche Aberkennung abgewiesen wurde, wegen Rechtswidrigkeit seines Inhalts (worauf auch der von der Beklagten angerufene Verfassungsgerichtshof in Punkt 2.4.5.3 seines Erkenntnisses ausdrücklich hinwies).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 10** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_31`)


Von dieser Sachlage ausgehend wies der von der Beklagten in diesem Verfahren mittels eines Parteiantrags auf Normenkontrolle angerufene Verfassungsgerichtshof den Antrag, die in BGBl II 2013/120 kundgemachte Verordnung des Bundeseinigungsamtes zur Gänze als verfassungswidrig aufzuheben, mit der Begründung ab, die Bedenken der Beklagten beruhten auf der nicht zutreffenden Prämisse, das Österreichische Rote Kreuz habe seine Kollektivvertragsfähigkeit durch das Erkenntnis des Verwaltungsgerichtshofs 2011/08/0230 „de facto“ verloren (Punkt 2.5 des Erkenntnisses).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofs` (organisation)

**Example 11** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_33`)


4. Die Frage, ob auch ohne Aufhebung der Verordnung BGBl II 2013/120 durch den Verfassungsgerichtshof allein dadurch, dass dem Österreichischen Roten Kreuz die Kollektivvertragsfähigkeit vom Bundeseinigungsamt mittels Bescheids aberkannt wird, die Satzung des Kollektivvertrags ihre Geltung verliert (vgl insbFriedrich, ASoK 2013, 460 f), stellt sich nicht, weil kein solcher Bescheid vorliegt.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 12** (doc_id: `deanon_TRAIN/8ObA72_19z`) (sent_id: `deanon_TRAIN/8ObA72_19z_12`)


2. Dabei konnte sich der Oberste Gerichtshof auf einschlägige Judikatur sowohl des Verfassungsgerichtshofs als auch des EuGH stützen: 2.1 Der Verfassungsgerichtshof hat in seinem Erkenntnis G 450/2015 ua Parteianträge von ÖBB-Bediensteten (unter anderem auch des Klägers) abgewiesen, die § 53a und § 56 Abs 18 bis 24 BundesbahnG je idF BGBl I Nr 64/2015 als verfassungswidrig aufzuheben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verfassungsgerichtshofs` (organisation)

**Example 13** (doc_id: `deanon_TRAIN/9ObA27_15h`) (sent_id: `deanon_TRAIN/9ObA27_15h_7`)


Ihr Antrag auf Gesetzesprüfung hinsichtlich der inzwischen aufgelösten Berufungskommission und eine Eventualbeschwerde seien beim Verfassungsgerichtshof anhängig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/14Os63_17x`) (sent_id: `deanon_TRAIN/14Os63_17x_8`)


1/b durch die zu Punkt a beschriebene Handlung fremde Urkunden, über die sie nicht alleine verfügen durfte, nämlich die in der Plastikhülle befindliche E-Card und ein Jahresticket der ÖBB des Peter Bohnert, mit dem Vorsatz unterdrückt zu verhindern, dass diese Urkunden im Rechtsverkehr zum Beweis eines Rechtes gebraucht werden.

**False Positives:**

- `ÖBB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bohnert`(person)

**Example 1** (doc_id: `deanon_TRAIN/6Ob169_12i`) (sent_id: `deanon_TRAIN/6Ob169_12i_42`)


Wenn das Erstgericht - dem Sachverständigengutachten folgend - zu der Einschätzung gelangte, dass in Anbetracht des Umstands, dass Art und Ausmaß der konkret festgestellten Kontaminierung und ihre Ursache (Lkw-Unfall) bekannt waren, in der Praxis keine sogenannte Vollanalyse durchzuführen gewesen wäre, so ist darin keine vom Obersten Gerichtshof im Interesse der Rechtssicherheit aufzugreifende Fehlbeurteilung zu erblicken, zumal auch die zuständige Bezirkshauptmannschaft in Anbetracht der bekannten Ursache der Kontaminierung nur eine Untersuchung der entsprechenden Kohlenwasserstoffwerte für erforderlich hielt.

**False Positives:**

- `Bezirkshauptmannschaft in` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/7Ob45_24d`) (sent_id: `deanon_TRAIN/7Ob45_24d_41`)


6. 2016 von einer Bezirkshauptmannschaft die Aufforderung gemäß § 103 Abs 2 KFG, binnen 14 Tagen nach Zustellung dieses Schreibens als Zulassungsbesitzer eines Kraftfahrzeugs dessen Lenker bekanntzugeben.

**False Positives:**

- `Bezirkshauptmannschaft die` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/7Ob45_24d`) (sent_id: `deanon_TRAIN/7Ob45_24d_51`)


[7] Mit Schreiben vom 19. 9. 2017 übermittelte der Klagevertreter der Beklagten das Straferkenntnis der Bezirkshauptmannschaft und ersuchte um Deckung für die Erhebung einer Beschwerde und sein Einschreiten in zweiter Instanz.

**False Positives:**

- `Bezirkshauptmannschaft und` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/7Ob45_24d`) (sent_id: `deanon_TRAIN/7Ob45_24d_54`)


[8] Am 19. 9. 2017 gab der Klagevertreter der Bezirkshauptmannschaft in der gegenständlichen Verwaltungsstrafsache die erteilte Vollmacht bekannt und beantragte die Übermittlung einer Aktenkopie.

**False Positives:**

- `Bezirkshauptmannschaft in` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/7Ob45_24d`) (sent_id: `deanon_TRAIN/7Ob45_24d_56`)


9. 2017 eine Beschwerde an das zuständige Landesverwaltungsgericht ein, in der er das Straferkenntnis der Bezirkshauptmannschaft sowohl dem Grunde als auch der Höhe nach anfocht.

**False Positives:**

- `Bezirkshauptmannschaft sowohl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/8ObA72_19z`) (sent_id: `deanon_TRAIN/8ObA72_19z_12`)


2. Dabei konnte sich der Oberste Gerichtshof auf einschlägige Judikatur sowohl des Verfassungsgerichtshofs als auch des EuGH stützen: 2.1 Der Verfassungsgerichtshof hat in seinem Erkenntnis G 450/2015 ua Parteianträge von ÖBB-Bediensteten (unter anderem auch des Klägers) abgewiesen, die § 53a und § 56 Abs 18 bis 24 BundesbahnG je idF BGBl I Nr 64/2015 als verfassungswidrig aufzuheben.

**False Positives:**

- `ÖBB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verfassungsgerichtshofs`(organisation)
- `Verfassungsgerichtshof`(organisation)

</details>

---

## `Generic GmbH Entity`

**F1:** 0.050 | **Precision:** 0.145 | **Recall:** 0.030  

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
| 0.145 | 0.030 | 0.050 | 145 | 21 | 124 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 21 | 124 | 676 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_6`)


Die Aktiengesellschaft habe damit geworben, mit den eingezahlten Beträgen Edelmetalle zu marktüblichen Preisen zu erwerben, zu lagern und zu verwalten und habe dem Beklagten in dessen Funktion als Rechtsanwalt und öffentlicher Notar den Auftrag erteilt, jährliche Prüfberichte über den vollständigen Bestand zu erstellen.

| Predicted | Gold |
|---|---|
| `Die Aktiengesellschaft` | `Die Aktiengesellschaft` |

**Example 1** (doc_id: `deanon_TRAIN/10Ob23_15b`) (sent_id: `deanon_TRAIN/10Ob23_15b_4`)


Steintra Solar GmbH, Kospachstraße 35, 3162 Rainfeld, Österreich, vertreten durch Dr. Paul Vavrovsky und Mag. Christian Schrott, Rechtsanwälte in Salzburg, 2. Umwelt Dorfwald ges.m.b.H., Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich, vertreten durch Dr. Katharina Sedlazeck-Gschaider, Rechtsanwältin in Salzburg, wegen 11.921,56 EUR sA und Feststellung (Streitwert 5.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 27. Jänner 2015, GZ 11 R 14/14d-34, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Steintra Solar GmbH` | `Steintra Solar GmbH` |

**Missed by this rule (FN):**

- `Kospachstraße 35, 3162 Rainfeld, Österreich` (address)
- `Umwelt Dorfwald ges.m.b.H.` (organisation)
- `Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich` (address)

**Example 2** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_5`)


Maschinenbau Heimfurtcon GmbH, Fretzschner Medien, 2.

| Predicted | Gold |
|---|---|
| `Maschinenbau Heimfurtcon GmbH` | `Maschinenbau Heimfurtcon GmbH` |

**Missed by this rule (FN):**

- `Fretzschner Medien` (organisation)

**Example 3** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_6`)


OberTratraSoftware Dienstleistungen AG, Prägrader Weg 43, 8616 Gasen, Österreich, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung (5.000 EUR) und 11.561,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2019, GZ 2 R 140/19z-30, mit dem das Urteil des Landesgerichts Wels vom 22. Juli 2019, GZ 26 Cg 66/18m-26, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

| Predicted | Gold |
|---|---|
| `OberTratraSoftware Dienstleistungen AG` | `OberTratraSoftware Dienstleistungen AG` |

**Missed by this rule (FN):**

- `Prägrader Weg 43, 8616 Gasen, Österreich` (address)

**Example 4** (doc_id: `deanon_TRAIN/2Ob159_18y`) (sent_id: `deanon_TRAIN/2Ob159_18y_11`)


Er selbst war ua als Fenstermonteur in der GmbH tätig.

| Predicted | Gold |
|---|---|
| `Er selbst war ua als Fenstermonteur in der GmbH` | `Er selbst war ua als Fenstermonteur in der GmbH` |

**Example 5** (doc_id: `deanon_TRAIN/2Ob63_11w`) (sent_id: `deanon_TRAIN/2Ob63_11w_4`)


Holz Seewald AG, Kaiserbrunnengasse 6, 5122 Lindach, Österreich, beide vertreten durch Dr. Leopold Hirsch, Rechtsanwalt in Salzburg, wegen 38.967,48 EUR sA und Feststellung (Streitinteresse 20.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 10. Februar 2011, GZ 4 R 206/10g-29, womit das Urteil des Landesgerichts Salzburg vom 17. August 2010, GZ 7 Cg 49/09f-25, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Holz Seewald AG` | `Holz Seewald AG` |

**Missed by this rule (FN):**

- `Kaiserbrunnengasse 6, 5122 Lindach, Österreich` (address)

**Example 6** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_62`)


Dabei wiesen die anwesenden Mitarbeiter der GmbH darauf hin, dass dieses Unternehmen Ansprechpartner für Serviceleistungen ist.

| Predicted | Gold |
|---|---|
| `Dabei wiesen die anwesenden Mitarbeiter der GmbH` | `Dabei wiesen die anwesenden Mitarbeiter der GmbH` |

**Example 7** (doc_id: `deanon_TRAIN/2Ob99_18z`) (sent_id: `deanon_TRAIN/2Ob99_18z_4`)


Oßmer KI GmbH, Dr.H.Pirchegger-Weg 23, 4154 Lengau, Österreich, vertreten durch Mag. Martina Hackl, Rechtsanwältin in Mödling, und 3. Pistor Pflege GmbH, Maierlweg 58, 4776 Kobledt, Österreich, vertreten durch Dr. Klaus Rainer, Rechtsanwalt in Graz, wegen 308.539,34 EUR sA und Feststellung (Streitwert 10.000 EUR), über die außerordentliche Revision der klagenden Partei (Revisionsinteresse 92.942,15 EUR) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. März 2018, GZ 1 R 140/17s-101, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oßmer KI GmbH` | `Oßmer KI GmbH` |

**Missed by this rule (FN):**

- `Dr.H.Pirchegger-Weg 23, 4154 Lengau, Österreich` (address)
- `Pistor Pflege GmbH` (organisation)
- `Maierlweg 58, 4776 Kobledt, Österreich` (address)

**Example 8** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_6`)


JQV Finanzen Gruppe GmbH, Innovationsplatz 79, 9751 Nigglai, Österreich, beide vertreten durch Ruggenthaler Rechtsanwalts KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 62.000 EUR) über den außerordentlichen Revisionsrekurs der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Wien vom 20. September 2010, GZ 30 R 29/10w-9, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `JQV Finanzen Gruppe GmbH` | `JQV Finanzen Gruppe GmbH` |

**Missed by this rule (FN):**

- `Innovationsplatz 79, 9751 Nigglai, Österreich` (address)

**Example 9** (doc_id: `deanon_TRAIN/4Ob98_20w`) (sent_id: `deanon_TRAIN/4Ob98_20w_5`)


Malkmuß Marine GmbH, Fettinger-Gasse 7, 4615 Niederprisching, Österreich, vertreten durch MMag.

| Predicted | Gold |
|---|---|
| `Malkmuß Marine GmbH` | `Malkmuß Marine GmbH` |

**Missed by this rule (FN):**

- `Fettinger-Gasse 7, 4615 Niederprisching, Österreich` (address)

**Example 10** (doc_id: `deanon_TRAIN/4Ob98_20w`) (sent_id: `deanon_TRAIN/4Ob98_20w_7`)


Roedel Textil GmbH, Hasledt 4, 9634 Bodenmühl, Österreich, vertreten durch Mag. Wolfgang Weilguni, Rechtsanwalt in Wien, wegen 1.028.146,05 EUR sA und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der Klägerin gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 21. April 2020, GZ 5 R 158/19w-116, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Roedel Textil GmbH` | `Roedel Textil GmbH` |

**Missed by this rule (FN):**

- `Hasledt 4, 9634 Bodenmühl, Österreich` (address)

**Example 11** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_80`)


Wird eine GmbH durch einen Dritten geschädigt, ist der dem Gesellschafter dadurch entstehende Nachteil in seinem Vermögen ein nicht ersatzfähiger mittelbarer Schaden.

| Predicted | Gold |
|---|---|
| `Wird eine GmbH` | `Wird eine GmbH` |

**Example 12** (doc_id: `deanon_TRAIN/6Ob118_16w`) (sent_id: `deanon_TRAIN/6Ob118_16w_4`)


SeeAlheimsudMedien Institut GmbH in Liquidation, LNMT Cloud, 2. WEA Robotik GmbH, Selpritscher Weg 52, 4951 Polling im Innkreis, Österreich, Deutschland, beide vertreten durch Wess Kispert Rechtsanwalts GmbH in Wien, wegen 103.578,16 EUR sA und Feststellung, über die Rekurse der beklagten Partei und der Nebenintervenienten gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 13. April 2016, GZ 14 R 173/16m-39, womit das Urteil des Landesgerichts Eisenstadt vom 31. August 2015, GZ 3 Cg 166/13y-34, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Den Rekursen wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `SeeAlheimsudMedien Institut GmbH` | `SeeAlheimsudMedien Institut GmbH` |

**Missed by this rule (FN):**

- `LNMT Cloud` (organisation)
- `WEA Robotik GmbH` (organisation)
- `Selpritscher Weg 52, 4951 Polling im Innkreis, Österreich` (address)

**Example 13** (doc_id: `deanon_TRAIN/6Ob16_20a`) (sent_id: `deanon_TRAIN/6Ob16_20a_52`)


Aus der Unternehmereigenschaft der GmbH kraft Rechtsform (§ 2 UGB) könne nicht geschlossen werden, dass die GmbH auch ein Unternehmen betreibe.

| Predicted | Gold |
|---|---|
| `Aus der Unternehmereigenschaft der GmbH` | `Aus der Unternehmereigenschaft der GmbH` |

**Example 14** (doc_id: `deanon_TRAIN/6Ob174_20m`) (sent_id: `deanon_TRAIN/6Ob174_20m_5`)


Holzfuß Garten GmbH, Kindlehen 4, 4211 Kottingersdorf, Österreich, vertreten durch Dr. Hans-Peter Neher, Rechtsanwalt in Bad Ischl, wegen Räumung, Unterlassung und Duldung, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Wels als Berufungsgericht vom 5. Juni 2020, GZ 22 R 109/20s-25, mit dem das Urteil des Bezirksgerichts Bad Ischl vom 29. Jänner 2020, GZ 12 C 27/19y-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Holzfuß Garten GmbH` | `Holzfuß Garten GmbH` |

**Missed by this rule (FN):**

- `Kindlehen 4, 4211 Kottingersdorf, Österreich` (address)

**Example 15** (doc_id: `deanon_TRAIN/6Ob18_20w`) (sent_id: `deanon_TRAIN/6Ob18_20w_6`)


Die GmbH war Eigentümerin einer Liegenschaft, der Beklagte ist Eigentümer der Nachbarliegenschaft.

| Predicted | Gold |
|---|---|
| `Die GmbH` | `Die GmbH` |

**Example 16** (doc_id: `deanon_TRAIN/6Ob18_20w`) (sent_id: `deanon_TRAIN/6Ob18_20w_12`)


Die GmbH wurde 2018 gemäß § 40 FBG wegen Vermögenslosigkeit im Firmenbuch gelöscht.

| Predicted | Gold |
|---|---|
| `Die GmbH` | `Die GmbH` |

**Example 17** (doc_id: `deanon_TRAIN/6Ob207_18m`) (sent_id: `deanon_TRAIN/6Ob207_18m_4`)


Balnuweit Technik GmbH, sowie 2. Ost Werkmon GmbH, alle Am Waidfeld 8, 5211 Gstöckat, Österreich, alle vertreten durch Dr. Peter Zöchbauer, Rechtsanwalt in Wien, wegen (zuletzt) Widerrufs, Veröffentlichung und Zahlung von 9.000 EUR, über die Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 30. Mai 2018, GZ 5 R 39/18v-27, womit über Berufung der beklagten Parteien das Urteil des Handelsgerichts Wien vom 24. Jänner 2018, GZ 39 Cg 26/17t-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Balnuweit Technik GmbH` | `Balnuweit Technik GmbH` |

**Missed by this rule (FN):**

- `Ost Werkmon GmbH` (organisation)
- `Am Waidfeld 8, 5211 Gstöckat, Österreich` (address)

**Example 18** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_31`)


Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG wäre hinsichtlich § 14 Abs 3 FBG sachlich nicht gerechtfertigt.

| Predicted | Gold |
|---|---|
| `Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG` | `Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob18_13i`) (sent_id: `deanon_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Monsud-Textil GmbH, VetR Herbert Dedert, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Textil GmbH` — partial — pred is substring of gold: `Monsud-Textil GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Monsud-Textil GmbH`(organisation)
- `VetR Herbert Dedert`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob29_25z`) (sent_id: `deanon_TRAIN/10Ob29_25z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hargassner als Vorsitzenden, den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier sowie die Hofrätin Dr. Wallner-Friedl in der Rechtssache der klagenden Partei Enns Werkdonver Holding GmbH, Mag.a DDr.in Lynn Rothwein, vertreten durch die Wallner Jorthan Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Prausewetter Umwelt AG, Valerius Gensmantel, vertreten durch die Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 25.380 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 13. Jänner 2025, GZ 12 R 40/24z-55, mit dem der Berufung der klagenden Partei nicht, hingegen jener der beklagten Partei gegen das Urteil des Landesgerichts Salzburg vom 25. Oktober 2024, GZ 14 Cg 35/22t-49, Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Friedl in der Rechtssache der klagenden Partei Enns Werkdonver Holding GmbH` — partial — gold is substring of pred: `Enns Werkdonver Holding GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Enns Werkdonver Holding GmbH`(organisation)
- `Mag.a DDr.in Lynn Rothwein`(person)
- `Prausewetter Umwelt AG`(organisation)
- `Valerius Gensmantel`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt, aus denen Erträge erzielt werden sollen.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — partial — gold is substring of pred: `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`(organisation)

**Example 3** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_7`)


Der Fonds wurde von einer in Deutschland ansässigen AG aufgelegt.

**False Positives:**

- `Der Fonds wurde von einer in Deutschland ansässigen AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_34`)


10. 2019 zu einem völlig gleichgelagerten Fall zu der vom Berufungsgericht angesprochenen Rechtsfrage Stellung genommen hat (beklagte Partei ist hier wie dort die Derber GmbH in Liqu).

**False Positives:**

- `beklagte Partei ist hier wie dort die Derber GmbH` — partial — gold is substring of pred: `Derber GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Derber GmbH`(organisation)

**Example 5** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Daniel Wiegand, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei West-Medien Manufaktur GmbH in Liqu, Kanzelweg 32, 4850 Oberthalheim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Medien Manufaktur GmbH` — partial — pred is substring of gold: `West-Medien Manufaktur GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DI Daniel Wiegand`(person)
- `West-Medien Manufaktur GmbH`(organisation)
- `Kanzelweg 32, 4850 Oberthalheim, Österreich`(address)
- `Eckert Rechtsanwalts GmbH`(organisation)

**Example 6** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_5`)


Text Begründung: Der Kläger erwarb als Verbraucher im Juni 2003 über Vermittlung eines selbständigen Vermögensberaters Kommanditanteile an der Bestelmeyer+Keßelheim Software GmbH & Co KG im Nominale von 17.000 EUR zuzüglich 850 EUR Agio.

**False Positives:**

- `Keßelheim Software GmbH & Co KG` — positional overlap with gold: `Bestelmeyer+Keßelheim Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bestelmeyer+Keßelheim Software GmbH`(organisation)

**Example 7** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — partial — gold is substring of pred: `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`(organisation)

**Example 8** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_7`)


Der Fonds wurde von einer in Deutschland ansässigen Aktiengesellschaft aufgelegt.

**False Positives:**

- `Der Fonds wurde von einer in Deutschland ansässigen Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_6`)


Text Gründe: Mit dem angefochtenen Urteil wurden Bernhard Beinicke und Norbert Wentzlick von der wider sie erhobenen Anklage, sie hätten am 7. Februar 2009 in Churer Straße 54, 9064 St. Michael ob der Gurk, Österreich /Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der DKZ Solar GesmbH & Co KG, Susanne Schueßler, durch die Vorgabe, die HochForschung GmbH sei eine zahlungsfähige Leasingnehmerin, somit durch Täuschung über Tatsachen, zum Abschluss eines Leasingvertrags über ein Rennfahrzeug für die Dauer von 24 Monaten zu einem monatlichen Entgelt von 10.698,10 Euro, somit zu einer Handlung verleitet, welche die Stadt-Sanitär Services GesmbH & Co KG in einem 50.000 Euro übersteigenden Betrag von insgesamt 235.358,20 Euro am Vermögen schädigte, gemäß § 259 Z 3 StPO (verfehlt auch von der rechtlichen Kategorie; vglLendl, WK-StPO § 259 Rz 1) freigesprochen.

**False Positives:**

- `Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der DKZ Solar GesmbH & Co KG` — partial — gold is substring of pred: `DKZ Solar GesmbH`
- `Sanitär Services GesmbH & Co KG` — positional overlap with gold: `Stadt-Sanitär Services GesmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bernhard Beinicke`(person)
- `Norbert Wentzlick`(person)
- `Churer Straße 54, 9064 St. Michael ob der Gurk, Österreich`(address)
- `DKZ Solar GesmbH`(organisation)
- `Susanne Schueßler`(person)
- `HochForschung GmbH`(organisation)
- `Stadt-Sanitär Services GesmbH`(organisation)

**Example 10** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_8`)


Nach den wesentlichen Feststellungen (US 3 bis 6) befand sich die See-Maschinenbau GmbH in der zweiten Jahreshälfte 2008 in erheblichen Zahlungsschwierigkeiten.

**False Positives:**

- `Maschinenbau GmbH` — partial — pred is substring of gold: `See-Maschinenbau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `See-Maschinenbau GmbH`(organisation)

**Example 11** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_11`)


„Nachdem“ es für die Wilken E‑Commerce GmbH notwendig geworden war, für die Aufnahme des Rennbetriebs 35.000 Euro in das Fahrzeug zu investieren, konnte aufgrund dessen schlechten Zustands kein Rennen erfolgreich beendet werden.

**False Positives:**

- `Commerce GmbH` — partial — pred is substring of gold: `Wilken E‑Commerce GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wilken E‑Commerce GmbH`(organisation)

**Example 12** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_23`)


Auch diesen Aspekt nimmt die Staatsanwaltschaft in der Rechtsrüge (Z 9 lit a) ausreichend in den Blick, indem sie auf - in Richtung der Erfüllung auch der objektiven Tatbestandsmerkmale der §§ 146, 147 Abs 3 StGB weisende - Beweisergebnisse zum vorliegenden Vertragsab-schluss trotz mangelnder finanzieller Ausstattung und Absicherung der Inn Dorfdersee GmbH hinweist.

**False Positives:**

- `schluss trotz mangelnder finanzieller Ausstattung und Absicherung der Inn Dorfdersee GmbH` — partial — gold is substring of pred: `Inn Dorfdersee GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Dorfdersee GmbH`(organisation)

**Example 13** (doc_id: `deanon_TRAIN/12Os107_11v`) (sent_id: `deanon_TRAIN/12Os107_11v_8`)


B./II./ am 13. November 2009 in Poysdorf als Zeugin in einem Ermittlungsverfahren nach der Strafprozessordnung vor der Kriminalpolizei bei ihrer förmlichen Vernehmung zur Sache falsch ausgesagt, indem sie wahrheitswidrig behauptete, die an sie bezahlten 22.800 Euro seien das Entgelt für LKW-Vermietungen an die Ost Lextal GmbH gewesen, wobei sie tatsächlich das Geld ausbezahlt bekam, ohne dafür an die genannte Gesellschaft eine Gegenleistung erbracht zu haben.

**False Positives:**

- `Vermietungen an die Ost Lextal GmbH` — partial — gold is substring of pred: `Ost Lextal GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ost Lextal GmbH`(organisation)

**Example 14** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__9`)


Text Gründe: Mit unbekämpft in Rechtskraft erwachsenen Urteilen des Bezirksgerichts Spittal an der Drau vom 22. Juni 2017, GZ 5 U 5/17f-26, wurden (I) Andreas Feiereisen des Vergehens der fahrlässigen Tötung nach § 80 Abs 1 StGB schuldig erkannt und hiefür zu einer Geldstrafe verurteilt sowie (II) die Werksynstein-Wind GmbH gemäß § 3 Abs 1 Z 2, Abs 2 VbVG für die vom Schuldspruch (I) erfasste Straftat ihres Entscheidungsträgers verantwortlich erklärt und über diese Gesellschaft eine Verbandsgeldbuße von 70 Tagessätzen zu je 50 Euro verhängt, die unter Bestimmung einer Probezeit von drei Jahren bedingt nachgesehen wurde.

**False Positives:**

- `Wind GmbH` — partial — pred is substring of gold: `Werksynstein-Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Feiereisen`(person)
- `Werksynstein-Wind GmbH`(organisation)

**Example 15** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__17`)


Indem das Bezirksgericht über die Jusepeitis&Niemöller Bildung GmbH eine (das Höchstmaß von somit 55 Tagessätzen übersteigende) Verbandsgeldbuße von 70 Tagessätzen verhängte, verletzte es § 4 Abs 3 VbVG).

**False Positives:**

- `Niemöller Bildung GmbH` — partial — pred is substring of gold: `Jusepeitis&Niemöller Bildung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jusepeitis&Niemöller Bildung GmbH`(organisation)

**Example 16** (doc_id: `deanon_TRAIN/15Os133_11i_15Os134_11m_`) (sent_id: `deanon_TRAIN/15Os133_11i_15Os134_11m__4`)


In der Medienrechtssache des Antragstellers Siegfried Kaierleber gegen die Antragsgegnerin MYPQ Versicherung Dienstleistungen GmbH wegen §§ 6 Abs 1, 8a Abs 6 MedienG, AZ 91 Hv 72/05g des Landesgerichts für Strafsachen Wien, verletzen die Beschlüsse dieses Gerichts vom 28. April 2009, GZ 91 Hv 72/05g-75, und des Oberlandesgerichts Wien als Beschwerdegericht vom 6. Juli 2009, AZ 18 Bs 218/09d, § 39 Abs 1 und § 56 Abs 1 (Art VI b Abs 1 in der Fassung BGBl I 2005/49) MedienG.

**False Positives:**

- `In der Medienrechtssache des Antragstellers Siegfried Kaierleber gegen die Antragsgegnerin MYPQ Versicherung Dienstleistungen GmbH` — partial — gold is substring of pred: `Kaierleber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kaierleber`(person)
- `MYPQ Versicherung Dienstleistungen GmbH`(organisation)

**Example 17** (doc_id: `deanon_TRAIN/17Ob10_20z`) (sent_id: `deanon_TRAIN/17Ob10_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätinnen Mag. Malesich und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Levi Adelwart, vertreten durch Stephan Briem Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Dr. Penelope Piephans als Treuhänder der Insolvenzgläubiger der Valkraftfen-Analyse Aktiengesellschaft, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH in Linz, wegen Feststellung (Streitwert 18.335,66 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. März 2020, GZ 1 R 31/20i-13, womit das Urteil des Landesgerichts Linz vom 9. Dezember 2019, GZ 4 Cg 73/18z-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Analyse Aktiengesellschaft` — partial — pred is substring of gold: `Valkraftfen-Analyse Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Levi Adelwart`(person)
- `Dr. Penelope Piephans`(person)
- `Valkraftfen-Analyse Aktiengesellschaft`(organisation)

**Example 18** (doc_id: `deanon_TRAIN/18ONc1_21y`) (sent_id: `deanon_TRAIN/18ONc1_21y_3`)


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

**Example 19** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Herbes&Vißers Heizung GmbH, Waldemar Lokämper, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Traun-Luftfahrt GmbH, VetR DDr. Walter Stuehrmann, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

**False Positives:**

- `Vißers Heizung GmbH` — partial — pred is substring of gold: `Herbes&Vißers Heizung GmbH`
- `Luftfahrt GmbH` — partial — pred is substring of gold: `Traun-Luftfahrt GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Wiener Neustadt`(organisation)
- `Herbes&Vißers Heizung GmbH`(organisation)
- `Waldemar Lokämper`(person)
- `Traun-Luftfahrt GmbH`(organisation)
- `VetR DDr. Walter Stuehrmann`(person)
- `Landesgericht Feldkirch`(organisation)

**Example 20** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_4`)


Republik Österreich, vertreten durch die Finanzprokuratur in Wien, 2. Dr. Ralph Kreidenweiß, und 3. Donau-Automotive GmbH, Ebersreith 11, 8761 Götzendorf, Österreich, beide vertreten durch Dr. Hubert Simon, Rechtsanwalt in Wien, wegen Leistung und Feststellung, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. April 2014, GZ 7 R 21/14h-7, mit dem der Beschluss des Landesgerichts Leoben vom 30. Jänner 2014, GZ 2 Nc 2/14y-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Automotive GmbH` — partial — pred is substring of gold: `Donau-Automotive GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Ralph Kreidenweiß`(person)
- `Donau-Automotive GmbH`(organisation)
- `Ebersreith 11, 8761 Götzendorf, Österreich`(address)

**Example 21** (doc_id: `deanon_TRAIN/1Ob140_14s`) (sent_id: `deanon_TRAIN/1Ob140_14s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer und Mag. Dr. Wurdinger sowie die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft, Meidlinger Hauptstraße 19, 5233 Erlach, Österreich, vertreten durch die Walch & Zehetbauer Rechtsanwälte OG, Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 344.011,19 EUR und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Juni 2014, GZ 4 R 202/13g-54, mit dem das Teilzwischenurteil des Landesgerichts Feldkirch vom 2. August 2013, GZ 8 Cg 143/11y-46, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

**False Positives:**

- `Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft` — partial — gold is substring of pred: `Tracondon Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tracondon Aktiengesellschaft`(organisation)
- `Meidlinger Hauptstraße 19, 5233 Erlach, Österreich`(address)

**Example 22** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Dr. Wurdinger als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Steger, Mag. Wessely-Kristöfel, Dr. Parzmayr und Dr. Pfurtscheller als weitere Richterinnen und Richter in der Rechtssache der klagenden Partei Bundeskammer für Arbeiter und Angestellte, Wien 4, Prinz-Eugen-Straße 20–22, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Alsynwald-Recycling AG, RgR Mag. Dr. Evelyn Steinkröger, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH in Wien, wegen Unterlassung und Urteilsveröffentlichung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. Juli 2024, GZ 2 R 77/24v-15, mit dem das Urteil des Handelsgerichts Wien vom 28. Februar 2024, GZ 57 Cg 36/23d-8, bestätigt wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Recycling AG` — partial — pred is substring of gold: `Alsynwald-Recycling AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alsynwald-Recycling AG`(organisation)
- `RgR Mag. Dr. Evelyn Steinkröger`(person)

**Example 23** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_116`)


Die Nieder Norber AG wird den Kunden in der Mitteilung auf die Änderungen hinweisen und darauf aufmerksam machen, dass sein Stillschweigen nach Ablauf der zwei Monate ab Zugang der Mitteilung durch das Unterlassen eines Widerspruchs in Schriftform als Zustimmung zu den Änderungen gilt.

**False Positives:**

- `Die Nieder Norber AG` — partial — gold is substring of pred: `Nieder Norber AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Norber AG`(organisation)

**Example 24** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_117`)


Außerdem wird die Valwalduni-Handel AG eine Gegenüberstellung über die von der Änderung betroffenen Bestimmungen sowie die vollständige Fassung der neuen Bedingungen auf ihrer Internetseite veröffentlichen und die Gegenüberstellung dem Kunden auf sein Verlangen zur Verfügung stellen;

**False Positives:**

- `Handel AG` — partial — pred is substring of gold: `Valwalduni-Handel AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Valwalduni-Handel AG`(organisation)

**Example 25** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_118`)


auch darauf wird die Landwerlin&Plumke Versand AG in derMitteilung hinweisen.

**False Positives:**

- `Plumke Versand AG` — partial — pred is substring of gold: `Landwerlin&Plumke Versand AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landwerlin&Plumke Versand AG`(organisation)

**Example 26** (doc_id: `deanon_TRAIN/1Ob182_17x`) (sent_id: `deanon_TRAIN/1Ob182_17x_25`)


Nach dem von den Vorinstanzen zugrunde gelegten Sachverhalt beabsichtigt der Antragsgegner einer zur Unternehmensgruppe der Familie gehörenden GmbH, an der er nur mehr einen Geschäftsanteil von 1 % hält, der aber mit weitreichenden Sonderrechten ausgestattet ist, und die einen dringenden Finanzierungsbedarf in Höhe von 3 Mio EUR hat, ein Privatdarlehen in dieser Höhe zu gewähren, dass er wiederum durch Aufnahme eines entsprechenden Bankkredits finanzieren will, von dem bereits 1 Mio EUR an den Antragsgegner und von diesem an die GmbH geflossen sind.

**False Positives:**

- `Nach dem von den Vorinstanzen zugrunde gelegten Sachverhalt beabsichtigt der Antragsgegner einer zur Unternehmensgruppe der Familie gehörenden GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_TRAIN/1Ob221_17g`) (sent_id: `deanon_TRAIN/1Ob221_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und Hofrätinnen Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Boothe u. Sandmeier IT GmbH (früher OberTelekom GmbH), Ewaldgasse 28, 4084 Mitterberg, Österreich, vormals vertreten durch Dr. Wolfgang Poleschinski, Rechtsanwalt in Hartberg, gegen die beklagte Partei Yelec Dangelmeier, vertreten durch die Dr. Farhad Paya Rechtsanwalt GmbH, Klagenfurt am Wörthersee, wegen 7.583,60 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 24. August 2017, GZ 1 R 127/17x-69, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 28. März 2017, GZ 16 C 1333/14i-65, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

**False Positives:**

- `früher OberTelekom GmbH` — partial — gold is substring of pred: `OberTelekom GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Boothe u. Sandmeier IT GmbH`(organisation)
- `OberTelekom GmbH`(organisation)
- `Ewaldgasse 28, 4084 Mitterberg, Österreich`(address)
- `Yelec Dangelmeier`(person)
- `Farhad Paya Rechtsanwalt GmbH`(organisation)

**Example 28** (doc_id: `deanon_TRAIN/1Ob26_20k`) (sent_id: `deanon_TRAIN/1Ob26_20k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Synsynfurt-Finanzen GmbH, Tanja Thielike, vertreten durch die Draxler Rexeis Sozietät von Rechtsanwälten OG, Graz, gegen die beklagte Partei Roberta Reumschüssel, Bakk. phil., vertreten durch Mag. Dr. Alfred Wansch, Rechtsanwalt in Wien, wegen Räumung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtsachen Wien als Berufungsgericht vom 13. November 2019, GZ 39 R 228/19x-70, mit dem das Urteil des Bezirksgerichts Hernals vom 30. April 2019, GZ 4 C 277/16f-64, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Finanzen GmbH` — partial — pred is substring of gold: `Synsynfurt-Finanzen GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synsynfurt-Finanzen GmbH`(organisation)
- `Tanja Thielike`(person)
- `Roberta Reumschüssel, Bakk. phil.`(person)

**Example 29** (doc_id: `deanon_TRAIN/1Ob38_21a`) (sent_id: `deanon_TRAIN/1Ob38_21a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei HR Janet Henken, vertreten durch die Greiml & Horwath Rechtsanwaltspartnerschaft, Graz, gegen die beklagte Partei Elvira Nossal, vertreten durch die Neger/Ulm Rechtsanwälte GmbH, Graz, wegen 6.720 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 3. Juni 2020, GZ 6 R 115/20f-20, mit dem das Urteil des Bezirksgerichts Deutschlandsberg vom 20. März 2020, GZ 11 C 55/19t-16, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Ulm Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `HR Janet Henken`(person)
- `Elvira Nossal`(person)

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `Company Name Without Suffix`

**F1:** 0.045 | **Precision:** 0.086 | **Recall:** 0.030  

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
| 0.086 | 0.030 | 0.045 | 244 | 21 | 223 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 21 | 223 | 676 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_6`)


Die Aktiengesellschaft habe damit geworben, mit den eingezahlten Beträgen Edelmetalle zu marktüblichen Preisen zu erwerben, zu lagern und zu verwalten und habe dem Beklagten in dessen Funktion als Rechtsanwalt und öffentlicher Notar den Auftrag erteilt, jährliche Prüfberichte über den vollständigen Bestand zu erstellen.

| Predicted | Gold |
|---|---|
| `Die Aktiengesellschaft` | `Die Aktiengesellschaft` |

**Example 1** (doc_id: `deanon_TRAIN/10Ob23_15b`) (sent_id: `deanon_TRAIN/10Ob23_15b_4`)


Steintra Solar GmbH, Kospachstraße 35, 3162 Rainfeld, Österreich, vertreten durch Dr. Paul Vavrovsky und Mag. Christian Schrott, Rechtsanwälte in Salzburg, 2. Umwelt Dorfwald ges.m.b.H., Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich, vertreten durch Dr. Katharina Sedlazeck-Gschaider, Rechtsanwältin in Salzburg, wegen 11.921,56 EUR sA und Feststellung (Streitwert 5.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 27. Jänner 2015, GZ 11 R 14/14d-34, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Steintra Solar GmbH` | `Steintra Solar GmbH` |

**Missed by this rule (FN):**

- `Kospachstraße 35, 3162 Rainfeld, Österreich` (address)
- `Umwelt Dorfwald ges.m.b.H.` (organisation)
- `Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich` (address)

**Example 2** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_5`)


Maschinenbau Heimfurtcon GmbH, Fretzschner Medien, 2.

| Predicted | Gold |
|---|---|
| `Maschinenbau Heimfurtcon GmbH` | `Maschinenbau Heimfurtcon GmbH` |

**Missed by this rule (FN):**

- `Fretzschner Medien` (organisation)

**Example 3** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_6`)


OberTratraSoftware Dienstleistungen AG, Prägrader Weg 43, 8616 Gasen, Österreich, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung (5.000 EUR) und 11.561,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2019, GZ 2 R 140/19z-30, mit dem das Urteil des Landesgerichts Wels vom 22. Juli 2019, GZ 26 Cg 66/18m-26, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

| Predicted | Gold |
|---|---|
| `OberTratraSoftware Dienstleistungen AG` | `OberTratraSoftware Dienstleistungen AG` |

**Missed by this rule (FN):**

- `Prägrader Weg 43, 8616 Gasen, Österreich` (address)

**Example 4** (doc_id: `deanon_TRAIN/2Ob159_18y`) (sent_id: `deanon_TRAIN/2Ob159_18y_11`)


Er selbst war ua als Fenstermonteur in der GmbH tätig.

| Predicted | Gold |
|---|---|
| `Er selbst war ua als Fenstermonteur in der GmbH` | `Er selbst war ua als Fenstermonteur in der GmbH` |

**Example 5** (doc_id: `deanon_TRAIN/2Ob63_11w`) (sent_id: `deanon_TRAIN/2Ob63_11w_4`)


Holz Seewald AG, Kaiserbrunnengasse 6, 5122 Lindach, Österreich, beide vertreten durch Dr. Leopold Hirsch, Rechtsanwalt in Salzburg, wegen 38.967,48 EUR sA und Feststellung (Streitinteresse 20.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 10. Februar 2011, GZ 4 R 206/10g-29, womit das Urteil des Landesgerichts Salzburg vom 17. August 2010, GZ 7 Cg 49/09f-25, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Holz Seewald AG` | `Holz Seewald AG` |

**Missed by this rule (FN):**

- `Kaiserbrunnengasse 6, 5122 Lindach, Österreich` (address)

**Example 6** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_62`)


Dabei wiesen die anwesenden Mitarbeiter der GmbH darauf hin, dass dieses Unternehmen Ansprechpartner für Serviceleistungen ist.

| Predicted | Gold |
|---|---|
| `Dabei wiesen die anwesenden Mitarbeiter der GmbH` | `Dabei wiesen die anwesenden Mitarbeiter der GmbH` |

**Example 7** (doc_id: `deanon_TRAIN/2Ob99_18z`) (sent_id: `deanon_TRAIN/2Ob99_18z_4`)


Oßmer KI GmbH, Dr.H.Pirchegger-Weg 23, 4154 Lengau, Österreich, vertreten durch Mag. Martina Hackl, Rechtsanwältin in Mödling, und 3. Pistor Pflege GmbH, Maierlweg 58, 4776 Kobledt, Österreich, vertreten durch Dr. Klaus Rainer, Rechtsanwalt in Graz, wegen 308.539,34 EUR sA und Feststellung (Streitwert 10.000 EUR), über die außerordentliche Revision der klagenden Partei (Revisionsinteresse 92.942,15 EUR) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. März 2018, GZ 1 R 140/17s-101, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oßmer KI GmbH` | `Oßmer KI GmbH` |

**Missed by this rule (FN):**

- `Dr.H.Pirchegger-Weg 23, 4154 Lengau, Österreich` (address)
- `Pistor Pflege GmbH` (organisation)
- `Maierlweg 58, 4776 Kobledt, Österreich` (address)

**Example 8** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_6`)


JQV Finanzen Gruppe GmbH, Innovationsplatz 79, 9751 Nigglai, Österreich, beide vertreten durch Ruggenthaler Rechtsanwalts KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 62.000 EUR) über den außerordentlichen Revisionsrekurs der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Wien vom 20. September 2010, GZ 30 R 29/10w-9, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `JQV Finanzen Gruppe GmbH` | `JQV Finanzen Gruppe GmbH` |

**Missed by this rule (FN):**

- `Innovationsplatz 79, 9751 Nigglai, Österreich` (address)

**Example 9** (doc_id: `deanon_TRAIN/4Ob98_20w`) (sent_id: `deanon_TRAIN/4Ob98_20w_5`)


Malkmuß Marine GmbH, Fettinger-Gasse 7, 4615 Niederprisching, Österreich, vertreten durch MMag.

| Predicted | Gold |
|---|---|
| `Malkmuß Marine GmbH` | `Malkmuß Marine GmbH` |

**Missed by this rule (FN):**

- `Fettinger-Gasse 7, 4615 Niederprisching, Österreich` (address)

**Example 10** (doc_id: `deanon_TRAIN/4Ob98_20w`) (sent_id: `deanon_TRAIN/4Ob98_20w_7`)


Roedel Textil GmbH, Hasledt 4, 9634 Bodenmühl, Österreich, vertreten durch Mag. Wolfgang Weilguni, Rechtsanwalt in Wien, wegen 1.028.146,05 EUR sA und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der Klägerin gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 21. April 2020, GZ 5 R 158/19w-116, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Roedel Textil GmbH` | `Roedel Textil GmbH` |

**Missed by this rule (FN):**

- `Hasledt 4, 9634 Bodenmühl, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_5`)


Die klagende Gesellschaft mit Sitz in Slowenien begehrt von der beklagten Gesellschaft mit Sitz in Deutschland im Europäischen Mahnverfahren nach der Verordnung (EG) 1896/2006 des Europäischen Parlaments und des Rates vom 12.

**False Positives:**

- `Die klagende Gesellschaft mit Sitz in Slowenien begehrt von der beklagten Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/10Ob13_20i`) (sent_id: `deanon_TRAIN/10Ob13_20i_10`)


Diese planten die Gründung einer Gesellschaft mit beschränkter Haftung, die die Liegenschaft erwerben und nach Parzellierung gewinnbringend weiterverkaufen sollte.

**False Positives:**

- `Diese planten die Gründung einer Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/10Ob15_16b`) (sent_id: `deanon_TRAIN/10Ob15_16b_35`)


Ohne konkrete Anhaltspunkte sind solche Schritte vom Gericht nicht zu unternehmen (10 Ob 67/11t;NeumayrinSchwimann/Kodek, ABGB4§ 11 UVG Rz 10 ff).

**False Positives:**

- `Ohne konkrete Anhaltspunkte sind solche Schritte vom Gericht nicht zu unternehmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10Ob18_13i`) (sent_id: `deanon_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Monsud-Textil GmbH, VetR Herbert Dedert, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Textil GmbH` — partial — pred is substring of gold: `Monsud-Textil GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Monsud-Textil GmbH`(organisation)
- `VetR Herbert Dedert`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob29_25z`) (sent_id: `deanon_TRAIN/10Ob29_25z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hargassner als Vorsitzenden, den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier sowie die Hofrätin Dr. Wallner-Friedl in der Rechtssache der klagenden Partei Enns Werkdonver Holding GmbH, Mag.a DDr.in Lynn Rothwein, vertreten durch die Wallner Jorthan Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Prausewetter Umwelt AG, Valerius Gensmantel, vertreten durch die Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 25.380 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 13. Jänner 2025, GZ 12 R 40/24z-55, mit dem der Berufung der klagenden Partei nicht, hingegen jener der beklagten Partei gegen das Urteil des Landesgerichts Salzburg vom 25. Oktober 2024, GZ 14 Cg 35/22t-49, Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Friedl in der Rechtssache der klagenden Partei Enns Werkdonver Holding GmbH` — partial — gold is substring of pred: `Enns Werkdonver Holding GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Enns Werkdonver Holding GmbH`(organisation)
- `Mag.a DDr.in Lynn Rothwein`(person)
- `Prausewetter Umwelt AG`(organisation)
- `Valerius Gensmantel`(person)

**Example 5** (doc_id: `deanon_TRAIN/10Ob42_15x`) (sent_id: `deanon_TRAIN/10Ob42_15x_17`)


Im Anwendungsbereich der EuZVO sei weder eine Zustellung per Post ohne Zustellnachweis, noch eine an die Postaufgabe anknüpfende Zustellfiktion des § 98 ZPO zulässig, sodass die Zustellung des Unterhaltsfestsetzungsbeschlusses, der dagegen erhobenen Rekurse, des Unterhaltsvorschussgewährungsbeschlusses und des dagegen erhobenen Rechtsmittels jeweils mangelhaft sei.

**False Positives:**

- `Im Anwendungsbereich der EuZVO sei weder eine Zustellung per Post` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt, aus denen Erträge erzielt werden sollen.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — partial — gold is substring of pred: `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`(organisation)

**Example 7** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_7`)


Der Fonds wurde von einer in Deutschland ansässigen AG aufgelegt.

**False Positives:**

- `Der Fonds wurde von einer in Deutschland ansässigen AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_34`)


10. 2019 zu einem völlig gleichgelagerten Fall zu der vom Berufungsgericht angesprochenen Rechtsfrage Stellung genommen hat (beklagte Partei ist hier wie dort die Derber GmbH in Liqu).

**False Positives:**

- `beklagte Partei ist hier wie dort die Derber GmbH` — partial — gold is substring of pred: `Derber GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Derber GmbH`(organisation)

**Example 9** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Daniel Wiegand, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei West-Medien Manufaktur GmbH in Liqu, Kanzelweg 32, 4850 Oberthalheim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Medien Manufaktur GmbH` — partial — pred is substring of gold: `West-Medien Manufaktur GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DI Daniel Wiegand`(person)
- `West-Medien Manufaktur GmbH`(organisation)
- `Kanzelweg 32, 4850 Oberthalheim, Österreich`(address)
- `Eckert Rechtsanwalts GmbH`(organisation)

**Example 10** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_5`)


Text Begründung: Der Kläger erwarb als Verbraucher im Juni 2003 über Vermittlung eines selbständigen Vermögensberaters Kommanditanteile an der Bestelmeyer+Keßelheim Software GmbH & Co KG im Nominale von 17.000 EUR zuzüglich 850 EUR Agio.

**False Positives:**

- `Keßelheim Software GmbH & Co KG` — positional overlap with gold: `Bestelmeyer+Keßelheim Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bestelmeyer+Keßelheim Software GmbH`(organisation)

**Example 11** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — partial — gold is substring of pred: `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`(organisation)

**Example 12** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_7`)


Der Fonds wurde von einer in Deutschland ansässigen Aktiengesellschaft aufgelegt.

**False Positives:**

- `Der Fonds wurde von einer in Deutschland ansässigen Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_6`)


Text Gründe: Mit dem angefochtenen Urteil wurden Bernhard Beinicke und Norbert Wentzlick von der wider sie erhobenen Anklage, sie hätten am 7. Februar 2009 in Churer Straße 54, 9064 St. Michael ob der Gurk, Österreich /Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der DKZ Solar GesmbH & Co KG, Susanne Schueßler, durch die Vorgabe, die HochForschung GmbH sei eine zahlungsfähige Leasingnehmerin, somit durch Täuschung über Tatsachen, zum Abschluss eines Leasingvertrags über ein Rennfahrzeug für die Dauer von 24 Monaten zu einem monatlichen Entgelt von 10.698,10 Euro, somit zu einer Handlung verleitet, welche die Stadt-Sanitär Services GesmbH & Co KG in einem 50.000 Euro übersteigenden Betrag von insgesamt 235.358,20 Euro am Vermögen schädigte, gemäß § 259 Z 3 StPO (verfehlt auch von der rechtlichen Kategorie; vglLendl, WK-StPO § 259 Rz 1) freigesprochen.

**False Positives:**

- `Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der DKZ Solar GesmbH & Co KG` — partial — gold is substring of pred: `DKZ Solar GesmbH`
- `Sanitär Services GesmbH & Co KG` — positional overlap with gold: `Stadt-Sanitär Services GesmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bernhard Beinicke`(person)
- `Norbert Wentzlick`(person)
- `Churer Straße 54, 9064 St. Michael ob der Gurk, Österreich`(address)
- `DKZ Solar GesmbH`(organisation)
- `Susanne Schueßler`(person)
- `HochForschung GmbH`(organisation)
- `Stadt-Sanitär Services GesmbH`(organisation)

**Example 14** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_8`)


Nach den wesentlichen Feststellungen (US 3 bis 6) befand sich die See-Maschinenbau GmbH in der zweiten Jahreshälfte 2008 in erheblichen Zahlungsschwierigkeiten.

**False Positives:**

- `Maschinenbau GmbH` — partial — pred is substring of gold: `See-Maschinenbau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `See-Maschinenbau GmbH`(organisation)

**Example 15** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_11`)


„Nachdem“ es für die Wilken E‑Commerce GmbH notwendig geworden war, für die Aufnahme des Rennbetriebs 35.000 Euro in das Fahrzeug zu investieren, konnte aufgrund dessen schlechten Zustands kein Rennen erfolgreich beendet werden.

**False Positives:**

- `Commerce GmbH` — partial — pred is substring of gold: `Wilken E‑Commerce GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wilken E‑Commerce GmbH`(organisation)

**Example 16** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_23`)


Auch diesen Aspekt nimmt die Staatsanwaltschaft in der Rechtsrüge (Z 9 lit a) ausreichend in den Blick, indem sie auf - in Richtung der Erfüllung auch der objektiven Tatbestandsmerkmale der §§ 146, 147 Abs 3 StGB weisende - Beweisergebnisse zum vorliegenden Vertragsab-schluss trotz mangelnder finanzieller Ausstattung und Absicherung der Inn Dorfdersee GmbH hinweist.

**False Positives:**

- `schluss trotz mangelnder finanzieller Ausstattung und Absicherung der Inn Dorfdersee GmbH` — partial — gold is substring of pred: `Inn Dorfdersee GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Dorfdersee GmbH`(organisation)

**Example 17** (doc_id: `deanon_TRAIN/12Os107_11v`) (sent_id: `deanon_TRAIN/12Os107_11v_8`)


B./II./ am 13. November 2009 in Poysdorf als Zeugin in einem Ermittlungsverfahren nach der Strafprozessordnung vor der Kriminalpolizei bei ihrer förmlichen Vernehmung zur Sache falsch ausgesagt, indem sie wahrheitswidrig behauptete, die an sie bezahlten 22.800 Euro seien das Entgelt für LKW-Vermietungen an die Ost Lextal GmbH gewesen, wobei sie tatsächlich das Geld ausbezahlt bekam, ohne dafür an die genannte Gesellschaft eine Gegenleistung erbracht zu haben.

**False Positives:**

- `Vermietungen an die Ost Lextal GmbH` — partial — gold is substring of pred: `Ost Lextal GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ost Lextal GmbH`(organisation)

**Example 18** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__9`)


Text Gründe: Mit unbekämpft in Rechtskraft erwachsenen Urteilen des Bezirksgerichts Spittal an der Drau vom 22. Juni 2017, GZ 5 U 5/17f-26, wurden (I) Andreas Feiereisen des Vergehens der fahrlässigen Tötung nach § 80 Abs 1 StGB schuldig erkannt und hiefür zu einer Geldstrafe verurteilt sowie (II) die Werksynstein-Wind GmbH gemäß § 3 Abs 1 Z 2, Abs 2 VbVG für die vom Schuldspruch (I) erfasste Straftat ihres Entscheidungsträgers verantwortlich erklärt und über diese Gesellschaft eine Verbandsgeldbuße von 70 Tagessätzen zu je 50 Euro verhängt, die unter Bestimmung einer Probezeit von drei Jahren bedingt nachgesehen wurde.

**False Positives:**

- `Wind GmbH` — partial — pred is substring of gold: `Werksynstein-Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Feiereisen`(person)
- `Werksynstein-Wind GmbH`(organisation)

**Example 19** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__17`)


Indem das Bezirksgericht über die Jusepeitis&Niemöller Bildung GmbH eine (das Höchstmaß von somit 55 Tagessätzen übersteigende) Verbandsgeldbuße von 70 Tagessätzen verhängte, verletzte es § 4 Abs 3 VbVG).

**False Positives:**

- `Niemöller Bildung GmbH` — partial — pred is substring of gold: `Jusepeitis&Niemöller Bildung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jusepeitis&Niemöller Bildung GmbH`(organisation)

**Example 20** (doc_id: `deanon_TRAIN/15Os133_11i_15Os134_11m_`) (sent_id: `deanon_TRAIN/15Os133_11i_15Os134_11m__4`)


In der Medienrechtssache des Antragstellers Siegfried Kaierleber gegen die Antragsgegnerin MYPQ Versicherung Dienstleistungen GmbH wegen §§ 6 Abs 1, 8a Abs 6 MedienG, AZ 91 Hv 72/05g des Landesgerichts für Strafsachen Wien, verletzen die Beschlüsse dieses Gerichts vom 28. April 2009, GZ 91 Hv 72/05g-75, und des Oberlandesgerichts Wien als Beschwerdegericht vom 6. Juli 2009, AZ 18 Bs 218/09d, § 39 Abs 1 und § 56 Abs 1 (Art VI b Abs 1 in der Fassung BGBl I 2005/49) MedienG.

**False Positives:**

- `In der Medienrechtssache des Antragstellers Siegfried Kaierleber gegen die Antragsgegnerin MYPQ Versicherung Dienstleistungen GmbH` — partial — gold is substring of pred: `Kaierleber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kaierleber`(person)
- `MYPQ Versicherung Dienstleistungen GmbH`(organisation)

**Example 21** (doc_id: `deanon_TRAIN/17Ob10_20z`) (sent_id: `deanon_TRAIN/17Ob10_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätinnen Mag. Malesich und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Levi Adelwart, vertreten durch Stephan Briem Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Dr. Penelope Piephans als Treuhänder der Insolvenzgläubiger der Valkraftfen-Analyse Aktiengesellschaft, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH in Linz, wegen Feststellung (Streitwert 18.335,66 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. März 2020, GZ 1 R 31/20i-13, womit das Urteil des Landesgerichts Linz vom 9. Dezember 2019, GZ 4 Cg 73/18z-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Analyse Aktiengesellschaft` — partial — pred is substring of gold: `Valkraftfen-Analyse Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Levi Adelwart`(person)
- `Dr. Penelope Piephans`(person)
- `Valkraftfen-Analyse Aktiengesellschaft`(organisation)

**Example 22** (doc_id: `deanon_TRAIN/18ONc1_21y`) (sent_id: `deanon_TRAIN/18ONc1_21y_3`)


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

**Example 23** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Herbes&Vißers Heizung GmbH, Waldemar Lokämper, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Traun-Luftfahrt GmbH, VetR DDr. Walter Stuehrmann, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

**False Positives:**

- `Vißers Heizung GmbH` — partial — pred is substring of gold: `Herbes&Vißers Heizung GmbH`
- `Luftfahrt GmbH` — partial — pred is substring of gold: `Traun-Luftfahrt GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Wiener Neustadt`(organisation)
- `Herbes&Vißers Heizung GmbH`(organisation)
- `Waldemar Lokämper`(person)
- `Traun-Luftfahrt GmbH`(organisation)
- `VetR DDr. Walter Stuehrmann`(person)
- `Landesgericht Feldkirch`(organisation)

**Example 24** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_4`)


Republik Österreich, vertreten durch die Finanzprokuratur in Wien, 2. Dr. Ralph Kreidenweiß, und 3. Donau-Automotive GmbH, Ebersreith 11, 8761 Götzendorf, Österreich, beide vertreten durch Dr. Hubert Simon, Rechtsanwalt in Wien, wegen Leistung und Feststellung, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. April 2014, GZ 7 R 21/14h-7, mit dem der Beschluss des Landesgerichts Leoben vom 30. Jänner 2014, GZ 2 Nc 2/14y-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Automotive GmbH` — partial — pred is substring of gold: `Donau-Automotive GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Ralph Kreidenweiß`(person)
- `Donau-Automotive GmbH`(organisation)
- `Ebersreith 11, 8761 Götzendorf, Österreich`(address)

**Example 25** (doc_id: `deanon_TRAIN/1Ob140_14s`) (sent_id: `deanon_TRAIN/1Ob140_14s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer und Mag. Dr. Wurdinger sowie die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft, Meidlinger Hauptstraße 19, 5233 Erlach, Österreich, vertreten durch die Walch & Zehetbauer Rechtsanwälte OG, Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 344.011,19 EUR und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Juni 2014, GZ 4 R 202/13g-54, mit dem das Teilzwischenurteil des Landesgerichts Feldkirch vom 2. August 2013, GZ 8 Cg 143/11y-46, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

**False Positives:**

- `Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft` — partial — gold is substring of pred: `Tracondon Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tracondon Aktiengesellschaft`(organisation)
- `Meidlinger Hauptstraße 19, 5233 Erlach, Österreich`(address)

**Example 26** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Dr. Wurdinger als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Steger, Mag. Wessely-Kristöfel, Dr. Parzmayr und Dr. Pfurtscheller als weitere Richterinnen und Richter in der Rechtssache der klagenden Partei Bundeskammer für Arbeiter und Angestellte, Wien 4, Prinz-Eugen-Straße 20–22, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Alsynwald-Recycling AG, RgR Mag. Dr. Evelyn Steinkröger, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH in Wien, wegen Unterlassung und Urteilsveröffentlichung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. Juli 2024, GZ 2 R 77/24v-15, mit dem das Urteil des Handelsgerichts Wien vom 28. Februar 2024, GZ 57 Cg 36/23d-8, bestätigt wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Recycling AG` — partial — pred is substring of gold: `Alsynwald-Recycling AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alsynwald-Recycling AG`(organisation)
- `RgR Mag. Dr. Evelyn Steinkröger`(person)

**Example 27** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_105`)


Die Beklagte müsse weder ihre interne Kalkulation offenlegen noch sämtliche Dienstleistungen, die mit der Bearbeitungsgebühr abgegolten würden, einzeln anführen.

**False Positives:**

- `Die Beklagte müsse weder ihre interne Kalkulation offenlegen noch sämtliche Dienstleistungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_116`)


Die Nieder Norber AG wird den Kunden in der Mitteilung auf die Änderungen hinweisen und darauf aufmerksam machen, dass sein Stillschweigen nach Ablauf der zwei Monate ab Zugang der Mitteilung durch das Unterlassen eines Widerspruchs in Schriftform als Zustimmung zu den Änderungen gilt.

**False Positives:**

- `Die Nieder Norber AG` — partial — gold is substring of pred: `Nieder Norber AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Norber AG`(organisation)

**Example 29** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_117`)


Außerdem wird die Valwalduni-Handel AG eine Gegenüberstellung über die von der Änderung betroffenen Bestimmungen sowie die vollständige Fassung der neuen Bedingungen auf ihrer Internetseite veröffentlichen und die Gegenüberstellung dem Kunden auf sein Verlangen zur Verfügung stellen;

**False Positives:**

- `Handel AG` — partial — pred is substring of gold: `Valwalduni-Handel AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Valwalduni-Handel AG`(organisation)

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
| 0.000 | 0.000 | 0.000 | 12 | 0 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 12 | 567 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/12Os138_19i`) (sent_id: `deanon_TRAIN/12Os138_19i_10`)


GP 19 ff; vgl VfGH B 181/2014;

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/12Os71_19m_12Os72_19h_`) (sent_id: `deanon_TRAIN/12Os71_19m_12Os72_19h__9`)


GP 19 ff; vgl VfGH B 181/2014;

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/13Os137_17x`) (sent_id: `deanon_TRAIN/13Os137_17x_15`)


Sie wären somit nicht dem Gericht, sondern der Verwaltungsbehörde zuzurechnen und daher – als Akte unmittelbarer verwaltungsbehördlicher Befehls- und Zwangsgewalt – (nicht mit Grundrechtsbeschwerde an den Obersten Gerichtshof, sondern) gemäß Art 130 Abs 1 Z 2 B-VG mit Beschwerde an das zuständige Verwaltungsgericht zu bekämpfen (vgl VfGH 13.

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/17Os2_18z`) (sent_id: `deanon_TRAIN/17Os2_18z_19`)


Davon abgesehen sind Amtsgeschäfte (etwa tatsächliche Verrichtungen) der Hoheitsverwaltung zuzurechnen, wenn sie einen spezifischen Zusammenhang mit Hoheitsakten aufweisen (RIS-Justiz RS0130809;Raschauer, Allgemeines Verwaltungsrecht5Rz 684 ff;Grabenwarter/Holoubek, Verfassungsrecht – Allgemeines Verwaltungsrecht3Rz 736 ff; zur ständigen Rechtsprechung des VfGH grundlegend VfSlg 3.262).

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_91`)


2.4Diese Beurteilung steht mit der Entscheidung des VfGH zu V 52/91 (zu § 53 Abs 3 BO 1986) im Einklang.

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_112`)


Der VfGH hat sich in der Entscheidung zu V 52/91 mit der Rechtmäßigkeit des inhaltsgleichen § 53 Abs 3 BO 1986 im Lichte der Freiheit der Erwerbsausübung bereits befasst und (unter anderem) den auf die Aufhebung dieser Bestimmung gerichteten Individualantrag abgewiesen.

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_113`)


Dazu hat der VfGH ausgeführt, dass es aufgrund der vom Gesetzgeber angeordneten Differenzierung zwischen Taxis und Mietwagen sachlich gerechtfertigt ist, dass die BO 1986 auch in Ansehung des Ortes der Aufnahme von Fahrgästen für Mietwagen eine andere Regelung vorsieht als jene, die für Taxis gilt.

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_114`)


Zudem hat der VfGH ausgesprochen, dass das Gebot des § 53 Abs 3 BO 1986 zur Zielerreichung geeignet ist und keine unadäquate Einschränkung der Erwerbsausübungsfreiheit begründet.

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_115`)


Die Schranken der Freiheit der Erwerbsausübung werden durch die in Rede stehende Anordnung für Mietwagenunternehmer somit nicht überschritten (vgl allgemein auch VfGH G 347/2016 und V 44/2013).

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_120`)


Wie bereits ausgeführt, sind die Verstöße der Mietwagenunternehmer, die von der Beklagten ermöglicht und gefördert werden, nach dem Wortlaut der Norm und der vorliegenden Rechtsprechung vor allem des VfGH eindeutig.

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_144`)


Wenngleich es dem Gesetzgeber im Allgemeinen zusteht, Gesetze auch rückwirkend in Kraft zu setzen, kann im Einzelfall eine Rückwirkung als gegen den Gleichheitsgrundsatz (Art 2 StGG, Art 7 B-VG) verstoßend verfassungswidrig sein, wenn dadurch gegen den Vertrauensgrundsatz verstoßen und/oder die Rechtsstellung der von der Rückwirkung Betroffenen maßgeblich verschlechtert wird (vgl VfGH G 228/89;

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_30`)


Weil in der Folge abermals ein abweisender Bescheid erging, der sodann in Rechtskraft erwuchs (siehe erneut in Punkt 2.4.5.3 des VfGH-Erkenntnisses), ist es letzten Endes auch unrichtig, dass der Verwaltungsgerichtshof dem Roten Kreuz „de facto“ die Kollektivvertragsfähigkeit aberkannt hätte.

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

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
| 0.000 | 0.000 | 0.000 | 10 | 0 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 10 | 504 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/1Ob139_18z`) (sent_id: `deanon_TRAIN/1Ob139_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Angelina Töpker Inc., Ronja Straßgschwandtner, vertreten durch Mag. Ralph Kilches, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Lilia Anderßon, als Insolvenzverwalter im Insolvenzverfahren über das Vermögen der Vanek und Eloy Analyse GmbH, Kanischaberg 21, 4742 Kornrödt, Österreich, vertreten durch die Haslinger/Nagele & Partner Rechtsanwälte GmbH, Linz, wegen Feststellung einer Insolvenzforderung (Streitwert 447.352,05 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 28. Juni 2018, GZ 1 R 83/18h-8, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Nagele & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Haslinger/Nagele & Partner Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Angelina Töpker`(person)
- `Ronja Straßgschwandtner`(person)
- `Mag. Lilia Anderßon`(person)
- `Vanek und Eloy Analyse GmbH`(organisation)
- `Kanischaberg 21, 4742 Kornrödt, Österreich`(address)
- `Haslinger/Nagele & Partner Rechtsanwälte GmbH`(organisation)

**Example 1** (doc_id: `deanon_TRAIN/1Ob38_21a`) (sent_id: `deanon_TRAIN/1Ob38_21a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei HR Janet Henken, vertreten durch die Greiml & Horwath Rechtsanwaltspartnerschaft, Graz, gegen die beklagte Partei Elvira Nossal, vertreten durch die Neger/Ulm Rechtsanwälte GmbH, Graz, wegen 6.720 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 3. Juni 2020, GZ 6 R 115/20f-20, mit dem das Urteil des Bezirksgerichts Deutschlandsberg vom 20. März 2020, GZ 11 C 55/19t-16, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Ulm Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `HR Janet Henken`(person)
- `Elvira Nossal`(person)

**Example 2** (doc_id: `deanon_TRAIN/3Ob114_14g`) (sent_id: `deanon_TRAIN/3Ob114_14g_58`)


8.Die Vorinstanzen legten nicht die Bilanzen einer Rechtsanwälte GmbH als Bemessungsgrundlage zugrunde, sondern die Gewinnanteile des Beklagten an dieser Rechtsanwälte GmbH; zu einer allfälligen Minderung dieses Einkommens des Beklagten wurde eine Negativfeststellung getroffen, die zu seinen Lasten geht.

**False Positives:**

- `Die Vorinstanzen legten nicht die Bilanzen einer Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/3Ob44_20x`) (sent_id: `deanon_TRAIN/3Ob44_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie die Hofräte Priv.-Doz. Dr. Rassi und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Andreas Clösges, vertreten durch die Eger/Gründl Rechtsanwälte OG in Graz, gegen die beklagte Partei Chemie Valtri GmbH, Niels Niefeldt, vertreten durch Mag. Manuel Fähnrich, Rechtsanwalt in Graz, wegen 34.000 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 31. Jänner 2020, GZ 2 R 168/19x-28, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Gründl Rechtsanwälte OG` — partial — pred is substring of gold: `Eger/Gründl Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Andreas Clösges`(person)
- `Eger/Gründl Rechtsanwälte OG`(organisation)
- `Chemie Valtri GmbH`(organisation)
- `Niels Niefeldt`(person)

**Example 4** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_4`)


Logdercon-Digital, Dänemark, 2. Fengart GmbH, Oberer Weinweg 87, 9020 Klagenfurt, Österreich, beide vertreten durch Graf & Pitkowitz Rechtsanwälte GmbH in Wien, gegen die Beklagten 1. LGR Medien GmbH, OVX Finanzen, 2. Analyse Kelunizor AG, Fahnberg 42, 4100 Großamberg, Österreich, Deutschland, beide vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Gesamtstreitwert 69.500 EUR), über den Ordinationsantrag der Klägerinnen den Beschluss gefasst:  Spruch Dem Ordinationsantrag wird stattgegeben.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Logdercon-Digital`(organisation)
- `Fengart GmbH`(organisation)
- `Oberer Weinweg 87, 9020 Klagenfurt, Österreich`(address)
- `LGR Medien GmbH`(organisation)
- `OVX Finanzen`(organisation)
- `Analyse Kelunizor AG`(organisation)
- `Fahnberg 42, 4100 Großamberg, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)

**Example 5** (doc_id: `deanon_TRAIN/6Ob145_21y`) (sent_id: `deanon_TRAIN/6Ob145_21y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden, den Hofrat Dr. Nowotny, die Hofrätinnen Dr. Hofer-Zeni-Rennhofer und Dr. Faber und den Hofrat Mag. Pertmayr als weitere Richter in der Rechtssache der gefährdeten Partei Dipl.-Ing. Kirstin Iseler, MA Bakk. rer. nat., vertreten durch DORDA Rechtsanwälte GmbH in Wien, wider die Gegnerin der gefährdeten Partei Wilfried Pawell, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, über den Rekurs der gefährdeten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 26. Mai 2021, GZ 47 R 99/21p-19, womit aus Anlass des Rekurses der Gegnerin der gefährdeten Partei die einstweilige Verfügung des Bezirksgerichts Favoriten vom 3. April 2021, GZ 56 C 107/21m-2, als nichtig aufgehoben wurde, den Beschluss gefasst:  Spruch Dem Rekurs wirdFolge gegeben.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. Kirstin Iseler, MA Bakk. rer. nat.`(person)
- `Wilfried Pawell`(person)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)

**Example 6** (doc_id: `deanon_TRAIN/8ObA18_17f`) (sent_id: `deanon_TRAIN/8ObA18_17f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Brenn als weitere Richter sowie die fachkundigen Laienrichter Mag. Dr. Bernhard Gruber und Harald Kohlruss in der Arbeitsrechtssache der klagenden Partei Cassandra Hennel, vertreten durch Freimüller/Obereder/Pilz Rechtsanwält_innen GmbH in Wien, gegen die beklagte Partei SeeTextil AG, Othmar Dempewolf, vertreten durch DLA Piper Weiss-Tessbach Rechtsanwälte GmbH in Wien, wegen Feststellung (Streitwert 282,56 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. November 2016, GZ 7 Ra 90/16f-19, mit dem das Urteil des Arbeits- und Sozialgerichts Wien vom 20. Juli 2016, GZ 33 Cga 50/16p-15, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Tessbach Rechtsanwälte GmbH` — partial — pred is substring of gold: `DLA Piper Weiss-Tessbach Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Cassandra Hennel`(person)
- `SeeTextil AG`(organisation)
- `Othmar Dempewolf`(person)
- `DLA Piper Weiss-Tessbach Rechtsanwälte GmbH`(organisation)
- `Arbeits- und Sozialgerichts`(organisation)

**Example 7** (doc_id: `deanon_TRAIN/8ObA47_20z`) (sent_id: `deanon_TRAIN/8ObA47_20z_4`)


Sabine Duminger (aus dem Kreis der Arbeitgeber) und Robert Hauser (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Ilse Rzeznitzek, vertreten durch Lughofer, Moser & Partner, Rechtsanwälte in Traun, gegen die beklagte Partei Stadt Linz, Alva Kaulfuß, Bakk. iur., vertreten durch Wildmoser/Koch & Partner Rechtsanwälte GmbH in Linz, wegen Feststellung des aufrechten Dienstverhältnisses, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 9. März 2020, GZ 11 Ra 11/20x-18, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Koch & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Wildmoser/Koch & Partner Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ilse Rzeznitzek`(person)
- `Alva Kaulfuß, Bakk. iur.`(person)
- `Wildmoser/Koch & Partner Rechtsanwälte GmbH`(organisation)

**Example 8** (doc_id: `deanon_TRAIN/8ObA71_14w`) (sent_id: `deanon_TRAIN/8ObA71_14w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden und durch die Hofrätin Dr. Tarmann-Prentner, den Hofrat Mag. Ziegelbauer, sowie die fachkundigen Laienrichter Mag. Andreas Mörk und Mag. Matthias Schachner als weitere Richter in der Arbeitsrechtssache der klagenden Partei Karl Höroldt, vertreten durch Forcher-Mayr & Kantner Rechtsanwälte Partnerschaft in Innsbruck, gegen die beklagte Partei Rhein-Lebensmittel Manufaktur AG, David Gideon, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Feststellung (Streitwert: 21.800 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 30. September 2014, GZ 15 Ra 92/14p-40, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Karl Höroldt`(person)
- `Rhein-Lebensmittel Manufaktur AG`(organisation)
- `David Gideon`(person)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)

**Example 9** (doc_id: `deanon_TRAIN/8ObA72_19z`) (sent_id: `deanon_TRAIN/8ObA72_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Wessely-Kristöfel als weitere Richter sowie die fachkundigen Laienrichter Johannes Püller (aus dem Kreis der Arbeitgeber) und Mag. Michael Puhm (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Hermine Thom, vertreten durch Dr. Markus Orgler, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Mur Brucktridon AG, Dipl.-Ing. Griselda Lamberty, Bakk. rer. nat., vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 4.200,83 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 17. Oktober 2019, GZ 13 Ra 41/15z-30, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hermine Thom`(person)
- `Mur Brucktridon AG`(organisation)
- `Dipl.-Ing. Griselda Lamberty, Bakk. rer. nat.`(person)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)

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
| `organisation` | 0 | 10 | 597 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt, aus denen Erträge erzielt werden sollen.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — partial — gold is substring of pred: `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`(organisation)

**Example 1** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_5`)


Text Begründung: Der Kläger erwarb als Verbraucher im Juni 2003 über Vermittlung eines selbständigen Vermögensberaters Kommanditanteile an der Bestelmeyer+Keßelheim Software GmbH & Co KG im Nominale von 17.000 EUR zuzüglich 850 EUR Agio.

**False Positives:**

- `Keßelheim Software GmbH & Co KG` — positional overlap with gold: `Bestelmeyer+Keßelheim Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bestelmeyer+Keßelheim Software GmbH`(organisation)

**Example 2** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — partial — gold is substring of pred: `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`(organisation)

**Example 3** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_6`)


Text Gründe: Mit dem angefochtenen Urteil wurden Bernhard Beinicke und Norbert Wentzlick von der wider sie erhobenen Anklage, sie hätten am 7. Februar 2009 in Churer Straße 54, 9064 St. Michael ob der Gurk, Österreich /Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der DKZ Solar GesmbH & Co KG, Susanne Schueßler, durch die Vorgabe, die HochForschung GmbH sei eine zahlungsfähige Leasingnehmerin, somit durch Täuschung über Tatsachen, zum Abschluss eines Leasingvertrags über ein Rennfahrzeug für die Dauer von 24 Monaten zu einem monatlichen Entgelt von 10.698,10 Euro, somit zu einer Handlung verleitet, welche die Stadt-Sanitär Services GesmbH & Co KG in einem 50.000 Euro übersteigenden Betrag von insgesamt 235.358,20 Euro am Vermögen schädigte, gemäß § 259 Z 3 StPO (verfehlt auch von der rechtlichen Kategorie; vglLendl, WK-StPO § 259 Rz 1) freigesprochen.

**False Positives:**

- `Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der DKZ Solar GesmbH & Co KG` — partial — gold is substring of pred: `DKZ Solar GesmbH`
- `Sanitär Services GesmbH & Co KG` — positional overlap with gold: `Stadt-Sanitär Services GesmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bernhard Beinicke`(person)
- `Norbert Wentzlick`(person)
- `Churer Straße 54, 9064 St. Michael ob der Gurk, Österreich`(address)
- `DKZ Solar GesmbH`(organisation)
- `Susanne Schueßler`(person)
- `HochForschung GmbH`(organisation)
- `Stadt-Sanitär Services GesmbH`(organisation)

**Example 4** (doc_id: `deanon_TRAIN/2Ob99_18z`) (sent_id: `deanon_TRAIN/2Ob99_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden, den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé sowie die Hofräte Dr. Nowotny und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Stadt-Textil GmbH & Co KG, Kreuzlandstraße 52, 9462 Kalchberg, Österreich, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Kazlowski + Röttjer Automotive GmbH, Clarissa Lenschau, vertreten durch Keschmann Rechtsanwalts-GmbH in Wien, sowie die Nebenintervenientinnen 1. Ost-Chemie GmbH, M.-Klieber-Gasse 22, 3611 Himberg, Österreich, vertreten durch Dr. Dirk Just, Rechtsanwalt in Wien, 2.

**False Positives:**

- `Textil GmbH & Co KG` — positional overlap with gold: `Stadt-Textil GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stadt-Textil GmbH`(organisation)
- `Kreuzlandstraße 52, 9462 Kalchberg, Österreich`(address)
- `Kazlowski + Röttjer Automotive GmbH`(organisation)
- `Clarissa Lenschau`(person)
- `Ost-Chemie GmbH`(organisation)
- `M.-Klieber-Gasse 22, 3611 Himberg, Österreich`(address)

**Example 5** (doc_id: `deanon_TRAIN/3Ob114_14g`) (sent_id: `deanon_TRAIN/3Ob114_14g_4`)


KzlR Hartmut Raffenberg KG und 2.

**False Positives:**

- `KzlR Hartmut Raffenberg KG` — partial — gold is substring of pred: `KzlR Hartmut Raffenberg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KzlR Hartmut Raffenberg`(person)

**Example 6** (doc_id: `deanon_TRAIN/3Ob114_14g`) (sent_id: `deanon_TRAIN/3Ob114_14g_6`)


Begründung:  Rechtliche Beurteilung Die Erstklägerin (eine Rechtsanwalts KG), der Zweitkläger (deren Komplementär) und die Mutter des Zweitklägers (in Hinkunft: Pensionsberechtigte) führten als Kläger und Widerbeklagte ein Schiedsverfahren gegen den (hier) Beklagten (als ausgeschiedenen Komplementär) als Beklagten und Widerkläger, das mit einem Schiedsspruch vom 2. Mai 2011 endete.

**False Positives:**

- `eine Rechtsanwalts KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_5`)


Klingenbeil Versand GmbH & Co KG, 2.

**False Positives:**

- `Klingenbeil Versand GmbH & Co KG` — partial — gold is substring of pred: `Klingenbeil Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Klingenbeil Versand GmbH`(organisation)

**Example 8** (doc_id: `deanon_TRAIN/5Ob146_16f`) (sent_id: `deanon_TRAIN/5Ob146_16f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers Mag. Niels Mueter, vertreten durch Dr. Anke Reisch, Rechtsanwältin in Kitzbühel, gegen die Antragsgegnerin Talgart-Chemie GmbH & Co KG, Tiefe Gasse 5, 2061 Obritz, Österreich, vertreten durch Dr. Lisbeth Lass und Dr. Hans Christian Lass, Rechtsanwälte in Innsbruck, wegen § 52 Abs 1 Z 6 iVm § 20 Abs 3 WEG 2002, infolge des „außerordentlichen“ Revisionsrekurses des Antragstellers gegen den (richtig) Sachbeschluss des Landesgerichts Innsbruck vom 24. Mai 2016, GZ 4 R 128/16a-50, mit dem der Sachbeschluss des Bezirksgerichts Kitzbühel vom 14. März 2016, GZ 4 Msch 7/14x-36, abgeändert wurde, den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.

**False Positives:**

- `Chemie GmbH & Co KG` — positional overlap with gold: `Talgart-Chemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Niels Mueter`(person)
- `Talgart-Chemie GmbH`(organisation)
- `Tiefe Gasse 5, 2061 Obritz, Österreich`(address)

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
| 0.000 | 0.000 | 0.000 | 7 | 0 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 7 | 567 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/12Os138_19i`) (sent_id: `deanon_TRAIN/12Os138_19i_11`)


VwGH Ro 2014/03/0045).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/12Os71_19m_12Os72_19h_`) (sent_id: `deanon_TRAIN/12Os71_19m_12Os72_19h__10`)


VwGH Ro 2014/03/0045).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/3Ob164_20v`) (sent_id: `deanon_TRAIN/3Ob164_20v_130`)


Gegenteiliges ergibt sich auch nicht aus den im Rechtsmittel zitierten Entscheidungen des VwGH, in denen nur geklärt wurde, dass Rinde nicht als Abfall iSd § 2 Abs 1 AWG gilt.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_79`)


Eine „spontane“ Aufnahme von Fahrgästen ist untersagt (vgl auch VwGH 90/03/0118; 90/03/0041;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_81`)


Die Anordnung, dass die Bestellung (Anforderung eines Fahrzeugs: VwGH Ra 2014/03/0006) beim Gewerbetreibendeneinlangenmuss, verfolgt keinen Selbstzweck.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_95`)


3.Aus den angeführten Grundsätzen folgt, dass eine gleichzeitige Information des Mietwagenunternehmers und des Fahrers über die zu erbringende Beförderungsleistung den gesetzlichen Anforderungen nicht entspricht (vgl auch BGH I ZR 3/16 = GRUR 2017, 743 zur ähnlichen Rechtslage in Deutschland), sowie dass der Umfang der Beförderungsleistung (nach Anfangs- und Endpunkt) im Bestellzeitpunkt (vor der Information des Fahrers) bestimmt sein muss (vgl VwGH Ra 2014/03/0006).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/6Ob161_10k`) (sent_id: `deanon_TRAIN/6Ob161_10k_36`)


Die dem Enteigneten gebührende Entschädigung muss alle durch die Enteignung verursachten vermögensrechtlichen Nachteile erfassen, wobei bei ihrer Bemessung auch auf sämtliche bestehende wirtschaftliche Möglichkeiten bedacht zu nehmen ist (VwGH 28.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

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

</details>

---

<details>
<summary>📋 All Rules</summary>

## `District Court Pattern`

**F1:** 0.316 | **Precision:** 0.811 | **Recall:** 0.196  

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
| 0.811 | 0.196 | 0.316 | 169 | 137 | 32 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 137 | 32 | 562 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_4`)


Text Begründung: Die Klägerin begehrt mit der am 4. 8. 2017 beim Bezirksgericht Steyr eingebrachten Klage von dem in der Schweiz ansässigen Beklagten 4.660 EUR sA.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Steyr` | `Bezirksgericht Steyr` |

**Example 1** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_11`)


2018 erklärte sich dasBezirksgericht Steyrfür örtlich unzuständig und überwies (antragsgemäß) die Rechtssache an das nicht offenbar unzuständige Bezirksgericht Salzburg.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Example 2** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_22`)


Da das Bezirksgericht Salzburg die internationale Zuständigkeit Österreichs zur Erledigung der Klage rechtskräftig verneint hat, kann eine Ordination nicht mehr erfolgreich auf § 28 Abs 1 Z 1 JN gestützt werden.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Example 3** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Schramm als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Ivan Dimitroff, geboren am 19. Mai 1960, AZ 7 P 203/15g des Bezirksgerichts Mödling, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Mödling zurückgestellt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Missed by this rule (FN):**

- `Ivan Dimitroff` (person)
- `19. Mai 1960` (date)
- `Bezirksgerichts Mödling` (organisation)

**Example 4** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_4`)


Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |
| `Bezirksgericht Judenburg` | `Bezirksgericht Judenburg` |

**Missed by this rule (FN):**

- `Bezirksgerichts Judenburg` (organisation)

**Example 5** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_5`)


Das Bezirksgericht Mödling legte den Akt zur Entscheidung gemäß § 111 Abs 2 JN dem Obersten Gerichtshof vor (ON 8), ohne den Übertragungsbeschluss an die Parteien zuzustellen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Example 6** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_9`)


Nach Aufforderung im Sinn des § 252 Abs 3 ZPO benannte die Klägerin fristgerecht das Bezirksgericht Graz-Ost als das für die Durchführung des ordentlichen Verfahrens zuständige Gericht.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz` | `Bezirksgericht Graz` |

**Example 7** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_11`)


[3] Vor dem Bezirksgericht Graz-Ost beantragte sie die Vorlage der Rechtssache an den Obersten Gerichtshof zur Ordination nach § 28 Abs 1 Z 3 JN sowie die Unterbrechung des Verfahrens bis zur Entscheidung des Obersten Gerichtshofs (ON 18).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz` | `Bezirksgericht Graz` |

**Example 8** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_16`)


[5] Das Bezirksgericht Graz-Ost unterbrach das Verfahren bis zur Entscheidung des Obersten Gerichtshofs, „ein örtlich zuständiges Gericht gemäß § 98 Abs 1 Z 3 JN für die Geltendmachung der Forderungen der klagenden Partei gegenüber der Beklagten aus der gegenständlichen Geschäftsbeziehung zu bestimmen“, und sprach aus, dass das Verfahren nur über Antrag der Parteien fortgesetzt werde.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz` | `Bezirksgericht Graz` |

**Example 9** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_19`)


Das Bezirksgericht Graz-Ost legte den Akt dem Obersten Gerichtshof zur Entscheidung nach § 28 Abs 1 Z 3 JN vor.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz` | `Bezirksgericht Graz` |

**Example 10** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_30`)


Die Rechtssache wurde an das von der Klägerin namhafte gemachte Bezirksgericht Graz-Ost überwiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz` | `Bezirksgericht Graz` |

**Example 11** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_33`)


[12] 2.3 Solange das Bezirksgericht Graz-Ost seine sich aus § 252 Abs 3 ZPO ergebende Zuständigkeit nicht rechtskräftig verneint hat, ist der Oberste Gerichtshof nicht zur Bestimmung eines örtlich zuständigen Gerichts nach § 28 Abs 1 Z 3 JN berufen (RS0046450;

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz` | `Bezirksgericht Graz` |

**Example 12** (doc_id: `deanon_TRAIN/10Nc22_25d`) (sent_id: `deanon_TRAIN/10Nc22_25d_5`)


Der nach eigenen Angaben keinen „festen Wohnsitz“ habende Kläger erhob vor dem Bezirksgericht Neusiedl am See eine Klage auf Feststellung, dass der Beklagte nicht berechtigt sei, Daten in eine Datenanwendung einzufügen „bzw“ dass der Beklagte für die Entfernung solcher Daten aus der Anwendung „zuständig“ sei.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neusiedl` | `Bezirksgericht Neusiedl` |

**Example 13** (doc_id: `deanon_TRAIN/10Nc22_25d`) (sent_id: `deanon_TRAIN/10Nc22_25d_6`)


[2] Das Bezirksgericht Neusiedl am See und der Beklagte äußerten sich dahingehend, dass sie die Delegierung für nicht zweckmäßig erachteten.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neusiedl` | `Bezirksgericht Neusiedl` |

**Example 14** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und die Hofräte Dr. Fellinger und Dr. Schramm als weitere Richter in der Pflegschaftssache der Minderjährigen Delia Truepschuch, geboren am 1. Februar 2026, und Aloisa Eckmaier, geboren am 28. Februar 1976, AZ 2 PS 117/09t des Bezirksgerichts Feldkirchen, infolge Vorlage zur Genehmigung der Übertragung gemäß § 111 JN an das Bezirksgericht Neunkirchen, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Übertragung der Zuständigkeit zur Besorgung dieser Pflegschaftssache an das Bezirksgericht Neunkirchen wird genehmigt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Missed by this rule (FN):**

- `Delia Truepschuch` (person)
- `1. Februar 2026` (date)
- `Aloisa Eckmaier` (person)
- `28. Februar 1976` (date)

**Example 15** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_4`)


Begründung:  Rechtliche Beurteilung Das bisher zuständige Bezirksgericht Feldkirchen übertrug mit seinem - den Verfahrensbeteiligten zugestellten und nicht bekämpften - Beschluss vom 7. 10.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Feldkirchen` | `Bezirksgericht Feldkirchen` |

**Example 16** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_5`)


2009 die Zuständigkeit zur Führung der Pflegschaftssache an das Bezirksgericht Neunkirchen, weil die beiden Minderjährigen und ihre obsorgeberechtigte Mutter, in deren Haushalt sich die Kinder nach dem pflegschaftsgerichtlich genehmigten Scheidungsvergleich hauptsächlich aufhalten sollen, sich nunmehr ständig im Sprengel dieses Gerichts aufhielten.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Example 17** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_6`)


Das Bezirksgericht Neunkirchen verweigerte die Übernahme der Zuständigkeit, weil das übertragende Gericht den Antrag vom 24.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Example 18** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_7`)


8. 2009 schon zu bearbeiten begonnen habe, ihm die verfahrensbeteiligten Personen bekannt, dem Bezirksgericht Neunkirchen aber gänzlich unbekannt seien.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Example 19** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen ÖkR Priv.-Doz. Sven Egerth, geboren 3. Mai 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz` | `Bezirksgericht Graz` |

**Missed by this rule (FN):**

- `ÖkR Priv.-Doz. Sven Egerth` (person)
- `3. Mai` (date)

**Example 20** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_5`)


9. 2023 übertrug das Bezirksgericht Graz-West die Zuständigkeit zur Führung der Pflegschaftssache dem Bezirksgericht Braunau am Inn, das die Übernahme jedoch ablehnte.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz` | `Bezirksgericht Graz` |
| `Bezirksgericht Braunau` | `Bezirksgericht Braunau` |

**Example 21** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_6`)


[2] Das Bezirksgericht Graz-West legte den Akt daraufhin dem Obersten Gerichtshof zur Entscheidung gemäß § 111 Abs 2 JN vor, ohne den Übertragungsbeschluss den Parteien zuzustellen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz` | `Bezirksgericht Graz` |

**Example 22** (doc_id: `deanon_TRAIN/10Nc2_10s`) (sent_id: `deanon_TRAIN/10Nc2_10s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Pflegschaftssache des mj Andreas Wolfgang Spinner, geboren am 8. Juli 2004, und der mj Herta Vanessa Schlichtcroll, geboren am 4. April 2007, wegen Übertragung der Zuständigkeit nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Die mit Beschluss des Bezirksgerichts Salzburg vom 9. 9. 2009, AZ 42 PS 56/09a, verfügte Übertragung der Zuständigkeit zur Führung der Pflegschaftssache an das Bezirksgericht Mödling wird genehmigt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Missed by this rule (FN):**

- `Spinner` (person)
- `Schlichtcroll` (person)

**Example 23** (doc_id: `deanon_TRAIN/10Nc2_10s`) (sent_id: `deanon_TRAIN/10Nc2_10s_4`)


Begründung:  Rechtliche Beurteilung Die Zuständigkeit in der früher beim Bezirksgericht Steyr und beim Bezirksgericht Mattighofen anhängig gewesenen Pflegschaftssache wurde mit Beschluss des Bezirksgerichts Salzburg vom 26.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Steyr` | `Bezirksgericht Steyr` |
| `Bezirksgericht Mattighofen` | `Bezirksgericht Mattighofen` |

**Example 24** (doc_id: `deanon_TRAIN/10Nc2_10s`) (sent_id: `deanon_TRAIN/10Nc2_10s_7`)


2. 2009 beim Bezirksgericht Salzburg den Antrag, ihm die (einstweilige) Obsorge über die beiden Minderjährigen zu übertragen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Example 25** (doc_id: `deanon_TRAIN/10Nc2_10s`) (sent_id: `deanon_TRAIN/10Nc2_10s_12`)


2009 übertrug das Bezirksgericht Salzburg die Zuständigkeit zur Führung der Pflegschaftssache gemäß § 111 JN dem Bezirksgericht Mödling, weil die beiden Minderjährigen ihren Aufenthalt nunmehr im Sprengel dieses Gerichts hätten.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Example 26** (doc_id: `deanon_TRAIN/10Nc2_10s`) (sent_id: `deanon_TRAIN/10Nc2_10s_13`)


Auch die Mutter beantragte die Übertragung der Zuständigkeit an das Bezirksgericht Mödling, weil sie mit den Kindern nunmehr ihren Wohnsitz im Sprengel dieses Gerichts habe und sie dort auch vom Jugendwohlfahrtsträger betreut werde.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Example 27** (doc_id: `deanon_TRAIN/10Nc2_10s`) (sent_id: `deanon_TRAIN/10Nc2_10s_14`)


Das Bezirksgericht Mödling lehnte die Übernahme der Pflegschaftssache unter Hinweis auf die noch offenen Obsorgeanträge der Eltern ab.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Example 28** (doc_id: `deanon_TRAIN/10Nc2_10s`) (sent_id: `deanon_TRAIN/10Nc2_10s_18`)


Die Übertragung der Führung der Pflegschaftssache an das Bezirksgericht Mödling ist gerechtfertigt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Example 29** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei C. Dersudheim Digital GmbH, Taxlbergstraße 247, 8151 Rohrbach, Österreich, vertreten durch Dr. Carl Benkhofer, Rechtsanwalt in Wien, gegen die beklagte Partei Ingolf Grimpe, vertreten durch Greiml & Horwath Rechtsanwaltspartnerschaft in Graz, wegen 5.232 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 14 C 1302/11a des Bezirksgerichts Graz-West in nichtöffentlicher Sitzung, den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Graz-West das Bezirksgericht Fünfhaus bestimmt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Fünfhaus` | `Bezirksgericht Fünfhaus` |

**Missed by this rule (FN):**

- `Dersudheim Digital GmbH` (organisation)
- `Taxlbergstraße 247, 8151 Rohrbach, Österreich` (address)
- `Ingolf Grimpe` (person)

**Example 30** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_9`)


Die klagende Partei beantragt die Delegierung des Verfahrens vom Bezirksgericht Graz-West an das Bezirksgericht Fünfhaus.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz` | `Bezirksgericht Graz` |
| `Bezirksgericht Fünfhaus` | `Bezirksgericht Fünfhaus` |

**Example 31** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_11`)


Das Bezirksgericht Graz-West spricht sich für die Delegierung aus.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz` | `Bezirksgericht Graz` |

**Example 32** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin mj Zarin Steevens, geboren 26. Mai 2017, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Vöcklabruck, 4840 Vöcklabruck, Sportplatzstraße 1–3), deren Mutter Dorothea Akkaya, und des Antragsgegners Mirko Hamidi, Russische Föderation, wegen Feststellung der Abstammung, aufgrund der vom Bezirksgericht Josefstadt verfügten Vorlage des Akts AZ 23 Fam 2/21y zur Entscheidung gemäß § 111 Abs 2 JN den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Villach zurückgestellt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Missed by this rule (FN):**

- `Zarin Steevens` (person)
- `26. Mai` (date)
- `Dorothea Akkaya` (person)
- `Mirko Hamidi` (person)

**Example 33** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_8`)


[2] Mit Beschluss vom 10. 8. 2020 übertrug das zunächst in dieser Rechtssache angerufene Bezirksgericht Vöcklabruck die Zuständigkeit gemäß § 111 Abs 1 JN an das Bezirksgericht Villach, weil sich die Minderjährige nunmehr in einem Containerdorf in Raumberg 325, 2301 Schönau an der Donau, Österreich aufhalte (ON 7).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Vöcklabruck` | `Bezirksgericht Vöcklabruck` |
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Missed by this rule (FN):**

- `Raumberg 325, 2301 Schönau an der Donau, Österreich` (address)

**Example 34** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_10`)


Das Bezirksgericht Villach übernahm die Zuständigkeit mit Beschluss vom 19. 8. 2020 (ON 8), schrieb eine Tagsatzung für den 28.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Example 35** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_14`)


Daraufhin beraumte das Bezirksgericht Villach die Tagsatzung ab, widerrief das Zustellersuchen (ON 20a) und übertrug mitBeschluss vom 10.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Example 36** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_16`)


2021die Zuständigkeit zur Besorgung dieser Rechtssache nach § 111 Abs 1 JN an das Bezirksgericht Josefstadt (ON 22).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Example 37** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_18`)


Das Bezirksgericht Josefstadt lehnte die Übernahme der Zuständigkeit unter Rückmittlung des Akts am 18.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Example 38** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_21`)


Das Bezirksgericht Villach retournierte den Akt daraufhin an das Bezirksgericht Josefstadt mit dem Hinweis, dass der Akt vom Bezirksgericht Josefstadt dem gemeinsam übergeordneten Gericht vorzulegen sei (ON 30).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Example 39** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_22`)


[7] Letztlich legte das Bezirksgericht Josefstadt die Akten dem Obersten Gerichtshof zur Entscheidung des Zuständigkeitsstreits vor.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Example 40** (doc_id: `deanon_TRAIN/10Nc3_21d`) (sent_id: `deanon_TRAIN/10Nc3_21d_23`)


[8] Die vom Bezirksgericht Villach veranlasste Vorlage der Akten an den Obersten Gerichtshof ist verfrüht:  Rechtliche Beurteilung [9] Übertragungsbeschlüsse nach § 111 JN sind durch die Parteien anfechtbar (RIS-Justiz RS0046981 [insb T5]).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Example 41** (doc_id: `deanon_TRAIN/10Nc6_22x`) (sent_id: `deanon_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei PhD Ignaz Nardelli, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Diethard Eisenlöffel, Bakk. phil., Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Missed by this rule (FN):**

- `PhD Ignaz Nardelli` (person)
- `Diethard Eisenlöffel, Bakk. phil.` (person)

**Example 42** (doc_id: `deanon_TRAIN/10Nc6_22x`) (sent_id: `deanon_TRAIN/10Nc6_22x_7`)


Das vom Kläger angerufene Bezirksgericht Schwechat sprach rechtskräftig seine (internationale) Unzuständigkeit aus.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 43** (doc_id: `deanon_TRAIN/10Nc6_22x`) (sent_id: `deanon_TRAIN/10Nc6_22x_38`)


Unter Berücksichtigung dieser Vorgaben hat eine Zuweisung an das Bezirksgericht Schwechat zu erfolgen, lag doch zum einen der Abflugort in dessen Sprengel und wurde zum anderen die Klage bereits bei diesem Gericht behandelt (6 Nc 31/20s mwN ua).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 44** (doc_id: `deanon_TRAIN/10Nc7_10a`) (sent_id: `deanon_TRAIN/10Nc7_10a_4`)


Anstelle des Bezirksgerichts Kitzbühel wird das Bezirksgericht Mödling als zur Führung des Verlassenschaftsverfahrens zuständiges Gericht bestimmt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Example 45** (doc_id: `deanon_TRAIN/10Nc7_10a`) (sent_id: `deanon_TRAIN/10Nc7_10a_10`)


Im Hinblick auf die angeführten Umstände erscheint die Übertragung der Zuständigkeit an das Bezirksgericht Mödling im Sinne des § 31 Abs 1 JN zweckmäßig und geeignet, eine Verkürzung und Verbilligung des Verfahrens zu bewirken.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Example 46** (doc_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__5`)


Das Abwesenheitsurteil vom 26. September 2018 sowie der unter einem gefasste Beschluss (ON 25) werden aufgehoben und die Sache zu neuer Verhandlung und Entscheidung an das Bezirksgericht Leopoldstadt verwiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Leopoldstadt` | `Bezirksgericht Leopoldstadt` |

**Example 47** (doc_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__11`)


Nach zwei negativen Versuchen der Vorführung zur Hauptverhandlung am 2. Mai 2018 (ON 10a, 11) und am 27. Juni 2018 (ON 17, 18) führte das Bezirksgericht Leopoldstadt die – wiederholte (§ 276a zweiter Satz StPO) – Hauptverhandlung am 26. September 2018 in Abwesenheit des Angeklagten durch (ON 24), weil auch zu diesem Termin ein Vorführungsversuch erfolglos geblieben war (ON 23).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Leopoldstadt` | `Bezirksgericht Leopoldstadt` |

**Example 48** (doc_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__13`)


Mit Abwesenheitsurteil vom 26. September 2018 (ON 25) sprach das Bezirksgericht Leopoldstadt Nenad Pentzold des Vergehens der Veruntreuung nach § 133 Abs 1 StGB schuldig und verurteilte ihn zu einer Freiheitsstrafe.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Leopoldstadt` | `Bezirksgericht Leopoldstadt` |

**Missed by this rule (FN):**

- `Pentzold` (person)

**Example 49** (doc_id: `deanon_TRAIN/12Os5_11v_12Os6_11s_12Os7_11p_12Os8_11k_`) (sent_id: `deanon_TRAIN/12Os5_11v_12Os6_11s_12Os7_11p_12Os8_11k__14`)


Am 3. Mai 2010 brachte die Staatsanwaltschaft Wiener Neustadt beim Bezirksgericht Baden erneut einen Strafantrag gegen Christian Kowalzyk wegen des Verdachts der (während der Probezeit begangenen) Vergehen des unbefugten Gebrauchs von Fahrzeugen nach § 136 Abs 1 StGB sowie der Urkundenunterdrückung nach § 229 Abs 1 StGB ein und beantragte zugleich die „Straffestsetzung zu AZ 12 U 86/07z des Bezirksgerichtes Baden“ (ON 3 im Akt AZ 12 U 105/10y).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Baden` | `Bezirksgericht Baden` |

**Missed by this rule (FN):**

- `Christian Kowalzyk` (person)

**Example 50** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__7`)


Das angefochtene Urteil, das im Übrigen unberührt bleibt, wird im Ausspruch über die Verbandsgeldbuße aufgehoben und die Sache in diesem Umfang wird zu neuer Verhandlung und Entscheidung an das Bezirksgericht Spittal an der Drau verwiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Spittal` | `Bezirksgericht Spittal` |

**Example 51** (doc_id: `deanon_TRAIN/18ONc1_21y`) (sent_id: `deanon_TRAIN/18ONc1_21y_6`)


[2] Mit ihrem am 7. Jänner 2021 „aus Vorsicht“ auch beim Obersten Gerichtshof eingebrachtenAntragbegehrt die anwaltlich nicht vertreteneSchiedsbeklagteals Antragstellerin, die Einvernahme von zehn Personen als Zeugen vor dem Bezirksgericht Liezen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Liezen` | `Bezirksgericht Liezen` |

**Example 52** (doc_id: `deanon_TRAIN/18ONc1_21y`) (sent_id: `deanon_TRAIN/18ONc1_21y_10`)


Gleichzeitig wurde der idente Antrag auch beim Bezirksgericht Liezen eingebracht.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Liezen` | `Bezirksgericht Liezen` |

**Example 53** (doc_id: `deanon_TRAIN/1Nc2_20i`) (sent_id: `deanon_TRAIN/1Nc2_20i_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie den Hofrat Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei KommR Franz Kubank, vertreten durch Dr. Michael Wukoschitz, Rechtsanwalt in Wien, gegen die beklagte Partei Laurin Aichhorn a.d., Timothy Schulmeister, Serbien, wegen 600 EUR sA, über den Ordinationsantrag nach § 28 JN den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Missed by this rule (FN):**

- `KommR Franz Kubank` (person)
- `Laurin Aichhorn` (person)
- `Timothy Schulmeister` (person)

**Example 54** (doc_id: `deanon_TRAIN/1Nc2_20i`) (sent_id: `deanon_TRAIN/1Nc2_20i_7`)


Sie beantragt beim Obersten Gerichtshof gemäß § 28 JN unter Anschluss der einzubringenden Klage die Ordination des Bezirksgerichts für Handelssachen Wien als örtlich zuständiges Gericht, auch wenn aufgrund des Abflugorts das Bezirksgericht Schwechat naheliegend erschiene, das aber in Fluggastsachen überlastet sei.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 55** (doc_id: `deanon_TRAIN/1Nc2_20i`) (sent_id: `deanon_TRAIN/1Nc2_20i_10`)


2. Der Oberste Gerichtshof hat bereits in anderen gleichgelagerten Fällen der Durchsetzung von Ansprüchen nach der EU-Fluggastrechte-VO gegen das auch hier beklagte Flugunternehmen mit Sitz in Hirschmühle 31, 8221 Hofing, Österreich (Serbien) die Ordination bewilligt und das Bezirksgericht Schwechat, in dessen Sprengel der Abflughafen liegt, als zuständiges Gericht bestimmt (6 Nc 1/19b = ZVR 2019/114, 259 [zustMayr];

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Missed by this rule (FN):**

- `Hirschmühle 31, 8221 Hofing, Österreich` (address)

**Example 56** (doc_id: `deanon_TRAIN/1Ob55_13i`) (sent_id: `deanon_TRAIN/1Ob55_13i_7`)


Nach dem Klagsvorbringen sei er am 19. 8. 2009 im Strandbad Bezirksgericht Silz beim Verlassen des Wassers von einem ca zwei Fäuste großen Stein ins Gesicht getroffen worden, der vom damals sechsjährigen Beklagten geworfen worden sei.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Silz` | `Bezirksgericht Silz` |

**Example 57** (doc_id: `deanon_TRAIN/1Ob55_13i`) (sent_id: `deanon_TRAIN/1Ob55_13i_18`)


Verwiesen werde auf einen Akt der Staatsanwaltschaft Bezirksgericht Wels, in welchem gegen den Schädiger Vorerhebungen geführt, jedoch mangels Deliktsfähigkeit eingestellt worden seien.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Wels` | `Bezirksgericht Wels` |

**Example 58** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_6`)


Text Gründe: Mit dem angefochtenen Erkenntnis wurde Dr. Nadja Köpers, Rechtsanwalt in Laahen 3, 3240 Pölla, Österreich, wegen des Verstoßes gegen die Bestimmungen des § 9 (Abs 1) RAO und des § 2 RL-BA der Disziplinarvergehen der Verletzung von Berufspflichten und der Beeinträchtigung von Ehre oder (richtig:) Ansehen des Standes nach § 1 Abs 1 erster und zweiter Fall DSt schuldig erkannt, weil er als Rechtsvertreter der Ehegatten Roman und Elfriede Jakubus in Anträgen auf Aufschiebung der Zwangsversteigerungen für seine Mandanten vom 5. September 2013 in näher bezeichneten Verfahren des Bezirksgerichts Innsbruck und des Bezirksgerichts Amstetten sowie in einer näher genannten Feststellungsklage an das Landesgericht Linz vom 7. Oktober 2013 und in einer Impugnationsklage an das Bezirksgericht Amstetten vom 10. Oktober 2013 jeweils vorgebracht hatte, seine Mandanten hätten sämtliche Verpflichtungen aus einer mit der Bachseewald Heizung AG abgeschlossenen Vereinbarung vom 11. Dezember 2012, insbesondere jene zur unwiderruflichen Antragstellung auf Aufhebung der Höfeeigenschaft einer näher bezeichnenden Liegenschaft in Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich, eingehalten, obwohl ihm zum Zeitpunkt der Antragstellung und Klagseinbringung bekannt war, dass der Antrag auf Aufhebung der Höfeeigenschaft vom 13. Dezember 2012 bereits am 14. Juni 2013 von Roman Janis, durch ihn vertreten, entgegen der zuvor genannten Vereinbarung vom 11. Dezember 2012 wieder zurückgezogen worden war.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Amstetten` | `Bezirksgericht Amstetten` |

**Missed by this rule (FN):**

- `Dr. Nadja Köpers` (person)
- `Laahen 3, 3240 Pölla, Österreich` (address)
- `Jakubus` (person)
- `Landesgericht Linz` (organisation)
- `Bachseewald Heizung AG` (organisation)
- `Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich` (address)
- `Roman Janis` (person)

**Example 59** (doc_id: `deanon_TRAIN/2Nc17_17y`) (sent_id: `deanon_TRAIN/2Nc17_17y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und durch die Hofräte Dr. Veith und Dr. Musger als weitere Richter in der Rechtssache der klagenden Partei Glanzbruckkraft-Recycling -Aktiengesellschaft, Steindläcker 26, 4183 Obertraberg, Österreich, vertreten durch THUM WEINREICH SCHWARZ CHYBA REITER Rechtsanwälte OG in St. Pölten, gegen die beklagte Partei Verband der Versicherungsunternehmen Österreichs, Schwarzenbergplatz 7, 1030 Wien, vertreten durch Mag. Georg E. Thalhammer, Rechtsanwalt in Wien, wegen 11.550 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Innere Stadt Wien das Bezirksgericht Kitzbühel bestimmt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Kitzbühel` | `Bezirksgericht Kitzbühel` |

**Missed by this rule (FN):**

- `Glanzbruckkraft-Recycling` (organisation)
- `Steindläcker 26, 4183 Obertraberg, Österreich` (address)

**Example 60** (doc_id: `deanon_TRAIN/2Nc17_17y`) (sent_id: `deanon_TRAIN/2Nc17_17y_7`)


Nachdem die beklagte Partei das Klagebegehren dem Grunde und der Höhe nach bestritten hatte, beantragte die klagende Partei die Delegierung der Rechtssache an das Bezirksgericht Kitzbühel, in dessen Sprengel sich der Unfall ereignet habe.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Kitzbühel` | `Bezirksgericht Kitzbühel` |

**Example 61** (doc_id: `deanon_TRAIN/2Nc24_12w`) (sent_id: `deanon_TRAIN/2Nc24_12w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith und Dr. E. Solé als weitere Richter in der Rechtssache der klagenden Partei Thaddäus Gerzabek, LLM, vertreten durch Dr. Hanspeter Egger, Rechtsanwalt in Wien, gegen die beklagte Partei Pietruszak Recycling -AG, Rainer Chochola, vertreten durch Dr. Norbert Bergmüller, Rechtsanwalt in Schladming, wegen 1.505,25 EUR sA, über den Delegierungsantrag der beklagten Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Hietzing das Bezirksgericht Irdning bestimmt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Irdning` | `Bezirksgericht Irdning` |

**Missed by this rule (FN):**

- `Thaddäus Gerzabek, LLM` (person)
- `Pietruszak Recycling` (organisation)
- `Rainer Chochola` (person)

**Example 62** (doc_id: `deanon_TRAIN/2Nc24_12w`) (sent_id: `deanon_TRAIN/2Nc24_12w_4`)


Text Begründung: Der Kläger begehrt in seiner beim Bezirksgericht Hietzing am allgemeinen Gerichtsstand der beklagten Partei eingebrachten Klage Schadenersatz nach einem Verkehrsunfall auf der Salzkammergutstraße in Unterburg.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Hietzing` | `Bezirksgericht Hietzing` |

**Example 63** (doc_id: `deanon_TRAIN/2Nc24_12w`) (sent_id: `deanon_TRAIN/2Nc24_12w_5`)


Die beklagte Partei beantragt die Delegierung der Rechtssache an das Bezirksgericht Irdning, in dessen Sprengel sich der Unfall ereignet habe.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Irdning` | `Bezirksgericht Irdning` |

**Example 64** (doc_id: `deanon_TRAIN/2Nc24_12w`) (sent_id: `deanon_TRAIN/2Nc24_12w_8`)


Das Bezirksgericht Hietzing erachtete eine Delegierung für zweckmäßig.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Hietzing` | `Bezirksgericht Hietzing` |

**Example 65** (doc_id: `deanon_TRAIN/3Nc11_13t`) (sent_id: `deanon_TRAIN/3Nc11_13t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie die Hofräte Univ.-Prof Dr. Neumayr und Dr. Jensik als weitere Richter in der Ordinationssache der Antragstellerin Waldzorval Technologien GmbH, Dr.-Kühne-Gasse 29, 9560 Albern, Österreich, vertreten durch Dr. Clemens Thiele, Rechtsanwalt in Salzburg, gegen die Antragsgegnerin Pflege Allemkraft GmbH, Schirmerstraße 61, 8967 Oberhausberg, Österreich, wegen Exekutionsführung nach § 355 EO, infolge Antrags gemäß § 28 JN den Beschluss gefasst:  Spruch Für die Bewilligung und die Vollziehung der beabsichtigten Unterlassungsexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Missed by this rule (FN):**

- `Waldzorval Technologien GmbH` (organisation)
- `Dr.-Kühne-Gasse 29, 9560 Albern, Österreich` (address)
- `Pflege Allemkraft GmbH` (organisation)
- `Schirmerstraße 61, 8967 Oberhausberg, Österreich` (address)

**Example 66** (doc_id: `deanon_TRAIN/3Nc2_19b`) (sent_id: `deanon_TRAIN/3Nc2_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Roch und Dr. Rassi als weitere Richter in der Pflegschaftssache der minderjährigen Cornelius Eggerling, Mutter: Laura Schrader, LLB, Vater: Werner Pelargus, infolge Vorlage zur Entscheidung nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Oberwart zurückgestellt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Oberwart` | `Bezirksgericht Oberwart` |

**Missed by this rule (FN):**

- `Cornelius Eggerling` (person)
- `Laura Schrader, LLB` (person)
- `Werner Pelargus` (person)

**Example 67** (doc_id: `deanon_TRAIN/3Nc2_19b`) (sent_id: `deanon_TRAIN/3Nc2_19b_4`)


Text Begründung: Das Bezirksgericht Oberwart übertrug mit Beschluss vom 19. Dezember 2018 die Pflegschaftssache gemäß § 111 JN an das Bezirksgericht Fürstenfeld, weil sich das Kind nunmehr ständig in dessen Sprengel aufhalte.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Oberwart` | `Bezirksgericht Oberwart` |
| `Bezirksgericht Fürstenfeld` | `Bezirksgericht Fürstenfeld` |

**Example 68** (doc_id: `deanon_TRAIN/3Nc2_19b`) (sent_id: `deanon_TRAIN/3Nc2_19b_5`)


Das Bezirksgericht Fürstenfeld lehnte die Übernahme der Zuständigkeit am 2. Jänner 2019 ab und sandte den Akt an das Bezirksgericht Oberwart zurück.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Fürstenfeld` | `Bezirksgericht Fürstenfeld` |
| `Bezirksgericht Oberwart` | `Bezirksgericht Oberwart` |

**Example 69** (doc_id: `deanon_TRAIN/3Ob1_20y`) (sent_id: `deanon_TRAIN/3Ob1_20y_9`)


Der von den Klägern aufgrund dieses Urteils beim Bezirksgericht Melk eingebrachte, in erster Instanz erfolgreiche Antrag auf Bewilligung der Exekution gemäß § 350 EO zur Durchsetzung der Einverleibung der Dienstbarkeit wurde vom Landesgericht St. Pölten als Rekursgericht mit Beschluss vom 1. Februar 2018 mit der Begründung abgewiesen, dass sich die dem Titel angeschlossenen Pläne (Beilage ./B1 und ON 71) nicht ohne weiteres in Übereinstimmung bringen ließen, weshalb der Verlauf des Servitutswegs dem Titel nicht eindeutig entnommen werden könne.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Melk` | `Bezirksgericht Melk` |

**Missed by this rule (FN):**

- `Landesgericht St. Pölten` (organisation)

**Example 70** (doc_id: `deanon_TRAIN/3Ob203_11s`) (sent_id: `deanon_TRAIN/3Ob203_11s_9`)


Am selben Tag langte eine von den Antragstellern selbst verfasste Berufung per Fax beim Bezirksgericht Saalfelden ein.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Saalfelden` | `Bezirksgericht Saalfelden` |

**Example 71** (doc_id: `deanon_TRAIN/4Nc18_11a`) (sent_id: `deanon_TRAIN/4Nc18_11a_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel und Dr. Jensik als weitere Richter in der Rechtssache der klagenden Partei HochCloud GmbH, Piedro Temur, vertreten durch Dr. Christian Fuchshuber LL.M., Rechtsanwalt in Innsbruck, gegen die beklagte Partei SUI Pharma Consulting GmbH, Nancy Herz, vertreten durch Dr. Gerhard Strobich, Rechtsanwalt in Trofaiach, wegen 5.873,18 EUR sA, über den Delegierungsantrag der beklagten Partei den Beschluss gefasst:  Spruch Der Antrag, zur Verhandlung und Entscheidung in dieser Rechtssache anstelle des Bezirksgerichts Innsbruck das Bezirksgericht Leoben zu bestimmen, wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Leoben` | `Bezirksgericht Leoben` |

**Missed by this rule (FN):**

- `HochCloud GmbH` (organisation)
- `Piedro Temur` (person)
- `SUI Pharma Consulting GmbH` (organisation)
- `Nancy Herz` (person)

**Example 72** (doc_id: `deanon_TRAIN/4Nc18_11a`) (sent_id: `deanon_TRAIN/4Nc18_11a_4`)


Text Begründung: Die Klägerin mit Sitz in Innsbruck begehrt mit ihrer beim Bezirksgericht Innsbruck eingebrachten Klage 5.873,18 EUR sA für der Beklagten vereinbarungsgemäß erbrachte Reisedienstleistungen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innsbruck` | `Bezirksgericht Innsbruck` |

**Example 73** (doc_id: `deanon_TRAIN/4Nc18_11a`) (sent_id: `deanon_TRAIN/4Nc18_11a_8`)


Die Beklagte beantragte die Delegierung der Rechtssache an das Bezirksgericht Leoben.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Leoben` | `Bezirksgericht Leoben` |

**Example 74** (doc_id: `deanon_TRAIN/4Nc18_11a`) (sent_id: `deanon_TRAIN/4Nc18_11a_14`)


Das Bezirksgericht Innsbruck sprach sich gleichermaßen gegen die beantragte Delegierung aus, verwies auf die Möglichkeit der Zeugenvernehmung mittels Videokonferenz nach § 277 ZPO und (deswegen) auf den fehlenden Vorteil für die Parteien, der mit einer allfälligen Delegierung verbunden wäre.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innsbruck` | `Bezirksgericht Innsbruck` |

**Example 75** (doc_id: `deanon_TRAIN/5Nc13_13a`) (sent_id: `deanon_TRAIN/5Nc13_13a_14`)


Mit dem vorliegendenOrdinationsantragbegehren die Kläger, für die Rechtssache das Bezirksgericht Imst als örtlich zuständiges Gericht zu bestimmen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Imst` | `Bezirksgericht Imst` |

**Example 76** (doc_id: `deanon_TRAIN/5Nc13_13a`) (sent_id: `deanon_TRAIN/5Nc13_13a_15`)


Sie gestehen zu, dass das angerufene Bezirksgericht Imst nicht zufolge § 83 Abs 1 JN zuständig sei, weil der Bestandgegenstand nicht im Sprengel dieses Bezirksgerichts, sondern im Fürstentum Liechtenstein liege.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Imst` | `Bezirksgericht Imst` |

**Example 77** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_4`)


Kirsten Falterer, MA, vertreten durch Mag. Daniel Schöpf, Mag. Christian Maurer, Mag. Daniel Maurer, Rechtsanwälte in Salzburg, gegen die beklagte Partei Mona Gronmayer, BSc, vertreten durch die Steiner Anderwald Rechtsanwälte OG in Spittal an der Drau, wegen 28.017,16 EUR sA, über Vorlage des Akts AZ 3 C 361/20p des Bezirksgerichts Spittal an der Drau zur Entscheidung eines negativen Kompetenzkonflikts, den Beschluss gefasst:  Spruch Zur Fortführung dieser Rechtssache ist das Bezirksgericht Spittal an der Drau zuständig.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Spittal` | `Bezirksgericht Spittal` |

**Missed by this rule (FN):**

- `Kirsten Falterer, MA` (person)
- `Mona Gronmayer, BSc` (person)

**Example 78** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_6`)


Text Begründung: Mit der beim Bezirksgericht Salzburg eingebrachten Mahnklage begehrte der Kläger von der Beklagten die Zahlung von 28.017,16 EUR sA.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Example 79** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_9`)


In ihrem Einspruch gegen den vom Bezirksgericht Salzburg erlassenen Zahlungsbefehl erhob die Beklagte die Einrede der sachlichen und örtlichen Unzuständigkeit mit der Begründung, die Rechnungen stünden in einem tatsächlichen und rechtlichen Zusammenhang und seien daher zusammenzurechnen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_6`)


12. 2006 zur Einführung eines Europäischen Mahnverfahrens (EuMahnVO) vor dem Bezirksgericht für Handelssachen Wien die Zahlung von Forderungen aus in den Jahren 2018 und 2019 geschlossenen Werkverträgen.

**False Positives:**

- `Bezirksgericht für` — partial — pred is substring of gold: `Bezirksgericht für Handelssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht für Handelssachen Wien`(organisation)

**Example 1** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_7`)


[2] Das Bezirksgericht für Handelssachen Wien erließ – nach Verbesserung des Antrags – den Europäischen Zahlungsbefehl, gegen den die Beklagte fristgerecht Einspruch erhob.

**False Positives:**

- `Bezirksgericht für` — partial — pred is substring of gold: `Bezirksgericht für Handelssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht für Handelssachen Wien`(organisation)

**Example 2** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_10`)


Das Bezirksgericht für Handelssachen Wien überwies die Rechtssache an dieses Gericht.

**False Positives:**

- `Bezirksgericht für` — partial — pred is substring of gold: `Bezirksgericht für Handelssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht für Handelssachen Wien`(organisation)

**Example 3** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_22`)


[8] 1.1 Für das Verfahren nach der Europäischen Mahnverfahrensverordnung ist in Österreich nach § 252 Abs 2 ZPO ausschließlich das Bezirksgericht für Handelssachen Wien zuständig.

**False Positives:**

- `Bezirksgericht für` — partial — pred is substring of gold: `Bezirksgericht für Handelssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht für Handelssachen Wien`(organisation)

**Example 4** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_8`)


Das bisher zuständige Bezirksgericht werde daher die Interessen der Minderjährigen besser wahren können, zumal unmittelbare pflegschaftsbehördliche Maßnahmen nicht zu setzen seien.

**False Positives:**

- `Bezirksgericht werde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/10Ob21_15h`) (sent_id: `deanon_TRAIN/10Ob21_15h_17`)


Mit Urteil des Bezirksgerichts Bezirksgericht St. Pölten vom 21. 5. 2013 wurde die Klägerin zur Zahlung von 6.183,92 EUR sA an Sanierungskosten sowie zur Zahlung der Prozesskosten an den Betreiber eines Hoch- und Niederseilparks verurteilt.

**False Positives:**

- `Bezirksgericht St` — partial — pred is substring of gold: `Bezirksgericht St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht St. Pölten`(organisation)

**Example 6** (doc_id: `deanon_TRAIN/10Ob21_15h`) (sent_id: `deanon_TRAIN/10Ob21_15h_28`)


Weiters habe sie der Klägerin Zinsen und Prozesskosten, zu deren Zahlung sie im Verfahren vor dem Bezirksgericht Bezirksgericht Meidling verurteilt worden war, sowie die Kosten deren eigener Vertretung in diesem Verfahren zu ersetzen.

**False Positives:**

- `Bezirksgericht Bezirksgericht` — positional overlap with gold: `Bezirksgericht Meidling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Meidling`(organisation)

**Example 7** (doc_id: `deanon_TRAIN/10ObS150_17g`) (sent_id: `deanon_TRAIN/10ObS150_17g_10`)


Für ihn ist ein Sachwalter bestellt, der seit 2011 alle Angelegenheiten (§ 268 Abs 3 Z 3 ABGB) zu besorgen hat (siehe den Beschluss des Bezirksgericht Bezirksgericht Mattersburg vom 15.

**False Positives:**

- `Bezirksgericht Bezirksgericht` — positional overlap with gold: `Bezirksgericht Mattersburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Mattersburg`(organisation)

**Example 8** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__17`)


Indem das Bezirksgericht über die Jusepeitis&Niemöller Bildung GmbH eine (das Höchstmaß von somit 55 Tagessätzen übersteigende) Verbandsgeldbuße von 70 Tagessätzen verhängte, verletzte es § 4 Abs 3 VbVG).

**False Positives:**

- `Bezirksgericht über` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jusepeitis&Niemöller Bildung GmbH`(organisation)

**Example 9** (doc_id: `deanon_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_TRAIN/13Os7_20h_13Os8_20f__11`)


Im Protokoll über die Hauptverhandlung vor dem Bezirksgericht Innere Stadt Wien ist als Tag der Hauptverhandlung „23. 11. 2018“ angeführt (ON 18 S 1).

**False Positives:**

- `Bezirksgericht Innere` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 10** (doc_id: `deanon_TRAIN/13Os99_19m`) (sent_id: `deanon_TRAIN/13Os99_19m_12`)


Ein anderes Verständnis legt – entgegen der vom Berufungsgericht mit Verweis auf eine Literaturstelle (Hinterhofer/Oshidari, System des österreichischen Strafverfahrens Rz 10.89) vertretenen Ansicht – auch die historische Interpretation nicht nahe: Die im Verfahren vor dem Bezirksgericht schon in der Stammfassung der StPO vorgesehene Rechtsmittellegitimation des Privatbeteiligten (zum Nachteil des Angeklagten) wurde von der Rechtsprechung und überwiegend im Schrifttum zur früheren Rechtslage (mit Blick auf § 366 Abs 2 letzter Satz StPO idF vor BGBl 1978/169) dahin ausgelegt, dass dieser Berufung (nur) dann habe ergreifen können, wenn das Erstgericht eine Entschädigung (zumindest teilweise) zugesprochen hatte, nicht jedoch bei vollständiger Verweisung auf den Zivilrechtsweg.

**False Positives:**

- `Bezirksgericht schon` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_TRAIN/18ONc1_21y`) (sent_id: `deanon_TRAIN/18ONc1_21y_16`)


[5] Aufgrund des Verweises auf § 37 Abs 2 bis 5 JN ist für einen solchen Antrag das Bezirksgericht zuständig, in dessen Sprengel die Amtshandlung vorgenommen werden soll (HausmaningerinFasching/Konecny3§ 602 ZPO Rz 30).

**False Positives:**

- `Bezirksgericht zuständig` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_TRAIN/1Ob55_13i`) (sent_id: `deanon_TRAIN/1Ob55_13i_6`)


Mit der am 20. 8. 2012 beim Bezirksgericht Bezirksgericht Hallein eingebrachten Klage begehrte der Minderjährige von einem in Deutschland wohnhaften minderjährigen Beklagten Schadenersatz von 3.850 EUR sA und die Feststellung seiner Haftung für sämtliche aus dessen Steinwurf resultierenden Spät- und Dauerfolgen.

**False Positives:**

- `Bezirksgericht Bezirksgericht` — positional overlap with gold: `Bezirksgericht Hallein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Hallein`(organisation)

**Example 13** (doc_id: `deanon_TRAIN/1Ob55_13i`) (sent_id: `deanon_TRAIN/1Ob55_13i_69`)


8. 2012 beim gemäß Art 5 Nr 3 EuGVVO zuständigen Bezirksgericht Bezirksgericht Weiz (Gericht des Ortes, an dem das schädigende Ereignis eingetreten ist) im Elektronischen Rechtsverkehr eingebracht.

**False Positives:**

- `Bezirksgericht Bezirksgericht` — positional overlap with gold: `Bezirksgericht Weiz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Weiz`(organisation)

**Example 14** (doc_id: `deanon_TRAIN/2Nc17_17y`) (sent_id: `deanon_TRAIN/2Nc17_17y_4`)


Text Begründung: Die klagende Partei begehrt in ihrer beim Bezirksgericht Innere Stadt Wien am allgemeinen Gerichtsstand der beklagten Partei eingebrachten Klage Schadenersatz nach einem Verkehrsunfall auf der B 178 im Ortsgebiet von Going am Wilden Kaiser.

**False Positives:**

- `Bezirksgericht Innere` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 15** (doc_id: `deanon_TRAIN/2Nc17_17y`) (sent_id: `deanon_TRAIN/2Nc17_17y_11`)


Das Bezirksgericht Innere Stadt Wien hält die Delegierung für zweckmäßig.

**False Positives:**

- `Bezirksgericht Innere` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 16** (doc_id: `deanon_TRAIN/3Nc11_13t`) (sent_id: `deanon_TRAIN/3Nc11_13t_10`)


Für eine Unterlassungsexekution ist gemäß § 18 Z 4 zweiter Fall EO jenes Bezirksgericht zuständig, in dessen Sprengel die erste Exekutionshandlung, nämlich die Zustellung der Exekutionsbewilligung, zu bewirken ist.

**False Positives:**

- `Bezirksgericht zuständig` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_5`)


Für die Bewilligung und die Vollziehung der beabsichtigten Exekution gegen die Zweitbeklagte auf Urteilsveröffentlichung wird das Bezirksgericht Innere Stadt Wien als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Bezirksgericht Innere` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 18** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_8`)


Mit dem gegenständlichen Ordinationsantrag beantragen die Klägerinnen, der Oberste Gerichtshof möge das Bezirksgericht Innere Stadt Wien oder ein anderes Bezirksgericht als örtlich zuständiges Gericht für die Durchsetzung des Veröffentlichungsanspruchs gemäß § 354 EO gegen die Zweitbeklagte bestimmen.

**False Positives:**

- `Bezirksgericht Innere` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`
- `Bezirksgericht als` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 19** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_19`)


Dem Ordinationsantrag ist somit stattzugeben und zweckmäßigerweise das Bezirksgericht Innere Stadt Wien als zuständiges Gericht zu bestimmen.

**False Positives:**

- `Bezirksgericht Innere` — partial — pred is substring of gold: `Bezirksgericht Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere Stadt Wien`(organisation)

</details>

---

## `Regional Court Pattern`

**F1:** 0.159 | **Precision:** 0.670 | **Recall:** 0.090  

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
| 0.670 | 0.090 | 0.159 | 94 | 63 | 31 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 63 | 31 | 566 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc9_15b`) (sent_id: `deanon_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Mur Kraftalheim Holding GmbH, Gerald Zacharie, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Nexstein Textil GmbH, Dipl.-Ing. Lynn Forkarth, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |

**Missed by this rule (FN):**

- `Mur Kraftalheim Holding GmbH` (organisation)
- `Gerald Zacharie` (person)
- `Nexstein Textil GmbH` (organisation)
- `Dipl.-Ing. Lynn Forkarth` (person)

**Example 1** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_4`)


In Stattgebung der Nichtigkeitsbeschwerde wird das angefochtene Urteil aufgehoben, eine neue Hauptverhandlung angeordnet und die Sache an das Landesgericht Salzburg verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Example 2** (doc_id: `deanon_TRAIN/12Os107_11v`) (sent_id: `deanon_TRAIN/12Os107_11v_4`)


In Stattgebung sowie aus Anlass der Nichtigkeitsbeschwerde wird das angefochtene Urteil, das im Übrigen unberührt bleibt, in den Renata Himmeldirk betreffenden Schuldsprüchen B./I./ und II./ und demzufolge auch im Strafausspruch aufgehoben, eine neue Hauptverhandlung angeordnet und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an das Landesgericht Korneuburg verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Missed by this rule (FN):**

- `Himmeldirk` (person)

**Example 3** (doc_id: `deanon_TRAIN/12Os138_19i`) (sent_id: `deanon_TRAIN/12Os138_19i_6`)


Der dagegen gerichteten Beschwerde hatte das Landesgericht Innsbruck als Vollzugsgericht vom 13. Juni 2019, AZ 28 Bl 68/19p, nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgericht Innsbruck` | `Landesgericht Innsbruck` |

**Example 4** (doc_id: `deanon_TRAIN/12Os44_17p`) (sent_id: `deanon_TRAIN/12Os44_17p_4`)


Gründe:  Rechtliche Beurteilung Nach dem Norbert Naegelkraemer durch das Landesgericht Krems an der Donau am 4. Dezember 2015, GZ 16 Hv 32/15g-23, mehrerer Vergehen der gefährlichen Drohung nach § 107 Abs 1 StGB schuldig erkannt und zu einer teilbedingten Freiheitsstrafe verurteilt worden war, ordnete der Einzelrichter des genannten Landesgerichts nach Rechtskraft des Urteils die Zustellung der Aufforderung zum Strafantritt an den Verurteilten an.

| Predicted | Gold |
|---|---|
| `Landesgericht Krems` | `Landesgericht Krems` |

**Missed by this rule (FN):**

- `Naegelkraemer` (person)

**Example 5** (doc_id: `deanon_TRAIN/12Os71_19m_12Os72_19h_`) (sent_id: `deanon_TRAIN/12Os71_19m_12Os72_19h__5`)


Der dagegen gerichteten Beschwerde hatte das Landesgericht Innsbruck als Vollzugsgericht vom 17. Mai 2018, AZ 22 Bl 38/18f, 22 Bl 43/18s, nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgericht Innsbruck` | `Landesgericht Innsbruck` |

**Example 6** (doc_id: `deanon_TRAIN/13Os103_19z`) (sent_id: `deanon_TRAIN/13Os103_19z_12`)


Bei der Glaubwürdigkeitsbeurteilung ließ das Erstgericht weder die Divergenzen in den Angaben der Asli Dawids (vgl US 14) noch ihre Verurteilung durch das Landesgericht Feldkirch unberücksichtigt (vgl US 16).

| Predicted | Gold |
|---|---|
| `Landesgericht Feldkirch` | `Landesgericht Feldkirch` |

**Missed by this rule (FN):**

- `Dawids` (person)

**Example 7** (doc_id: `deanon_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_TRAIN/13Os110_19d_13Os111_19a__5`)


Das Urteil des Landesgerichts Eisenstadt vom 6. Juni 2017 (ON 155) wird aufgehoben, eine neue Hauptverhandlung angeordnet und die Sache an das Landesgericht Eisenstadt verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Eisenstadt` | `Landesgericht Eisenstadt` |

**Example 8** (doc_id: `deanon_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_TRAIN/13Os113_17t_13Os114_17i__6`)


Das Urteil des Landesgerichts Salzburg als Schöffengericht vom 28. Oktober 2015, GZ 41 Hv 49/15k-33, das im Übrigen unberührt bleibt, wird im Nikola Mikolajtschik betreffenden Strafausspruch aufgehoben und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an das Landesgericht Salzburg verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Missed by this rule (FN):**

- `Mikolajtschik` (person)

**Example 9** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__8`)


Mit zugleich gefasstem Beschluss sprach das Landesgericht Innsbruck gemäß § 265 StPO - ebenfalls unter Bestimmung einer dreijährigen Probezeit - die bedingte Entlassung aus dem im Urteilszeitpunkt noch nicht (durch Anrechnung der Vorhaft) verbüßten (unbedingten) Strafteil von einem Monat, zwanzig Tagen und einer Stunde aus (ON 48, nicht journalisierte Kopie des genannten Urteils).

| Predicted | Gold |
|---|---|
| `Landesgericht Innsbruck` | `Landesgericht Innsbruck` |

**Example 10** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__11`)


Unter einem fasste das Landesgericht Innsbruck den Beschluss, vom Widerruf der mit Urteil dieses Gerichts vom 6. März 2009, GZ 23 Hv 189/07m-104, gewährten bedingten Strafnachsicht abzusehen, die mit dem gemeinsam mit diesem Urteil ergangenen Beschluss gewährte bedingte Entlassung jedoch zu widerrufen (ON 49 S 3).

| Predicted | Gold |
|---|---|
| `Landesgericht Innsbruck` | `Landesgericht Innsbruck` |

**Example 11** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__13`)


Mit - unbekämpft in Rechtskraft erwachsenem - Beschluss vom 3. Februar 2012 (ON 54) rechnete das Landesgericht Innsbruck „gem § 400 StPO“ die in der Zeit vom 13. Dezember 2011, 17:00 Uhr, bis zum 23. Jänner 2012, 17:00 Uhr, im Verfahren AZ 27 HR 323/11h (= 20 Hv 43/12b) des Landesgerichts Feldkirch erlittene Verwahrungs- und Untersuchungshaft auf die mit Urteil vom 10. Jänner 2012 (ON 49) verhängte Freiheitsstrafe an (1) und sprach aus, dass der nach dieser Anrechnung aus dem genannten Urteil und dem gleichzeitig mit diesem gefassten Widerrufsbeschluss verbleibende Strafrest von einem Monat und zehn Tagen unter Bestimmung einer Probezeit von drei Jahren „bedingt nachgesehen“ werde (2).

| Predicted | Gold |
|---|---|
| `Landesgericht Innsbruck` | `Landesgericht Innsbruck` |

**Example 12** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__21`)


Da das Landesgericht Innsbruck hinsichtlich der mit - sogleich in Rechtskraft erwachsenem (ON 49 S 4) - Urteil vom 10. Jänner 2012 ausgesprochenen (ON 49 S 2) und der mit dem unter einem gefassten Widerrufsbeschluss aktualisierten (ON 49 S 3; siehe dazu aber (3) des Erkenntnisses) Freiheitsstrafe keine Strafvollzugsanordnung erließ, verletzte es somit § 397 erster Satz StPO iVm § 3 Abs 1 StVG.

| Predicted | Gold |
|---|---|
| `Landesgericht Innsbruck` | `Landesgericht Innsbruck` |

**Example 13** (doc_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t_`) (sent_id: `deanon_TRAIN/13Os123_12f_13Os124_12b_13Os136_12t__26`)


Ein Nachteil entstand der Verurteilten dadurch auch in Bezug auf die einen Monat übersteigende Untersuchungshaftzeit nicht, weil das Landesgericht Feldkirch zu AZ 20 Hv 43/12b - unter Missachtung des § 38 Abs 1 StGB - die vom Punkt 1 des Beschlusses des Landesgerichts Innsbruck vom 3. Februar 2012 (ON 54) umfasste Haftzeit (erneut zur Gänze) auf die im bezeichneten Verfahren verhängte (unbedingte) Freiheitsstrafe anrechnete.

| Predicted | Gold |
|---|---|
| `Landesgericht Feldkirch` | `Landesgericht Feldkirch` |

**Example 14** (doc_id: `deanon_TRAIN/15Os43_13g`) (sent_id: `deanon_TRAIN/15Os43_13g_5`)


Das Urteil, das im Übrigen unberührt bleibt, wird in Punkt A./2./ des Schuldspruchs sowie im Strafausspruch aufgehoben und es wird die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an das Landesgericht Korneuburg verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 15** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Herbes&Vißers Heizung GmbH, Waldemar Lokämper, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Traun-Luftfahrt GmbH, VetR DDr. Walter Stuehrmann, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

| Predicted | Gold |
|---|---|
| `Landesgericht Feldkirch` | `Landesgericht Feldkirch` |

**Missed by this rule (FN):**

- `Landesgericht Wiener Neustadt` (organisation)
- `Herbes&Vißers Heizung GmbH` (organisation)
- `Waldemar Lokämper` (person)
- `Traun-Luftfahrt GmbH` (organisation)
- `VetR DDr. Walter Stuehrmann` (person)

**Example 16** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_7`)


Die Klägerin begehrte die Delegierung des Verfahrens gemäß § 31 JN an das Landesgericht Feldkirch.

| Predicted | Gold |
|---|---|
| `Landesgericht Feldkirch` | `Landesgericht Feldkirch` |

**Example 17** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_23`)


Im vorliegenden Fall haben sowohl die Klägerin als auch das vorlegende Gericht zutreffend auf jene Umstände hingewiesen, die insgesamt eine Delegierung an das Landesgericht Feldkirch zweckmäßig erscheinen lassen (vgl dazu RIS-Justiz RS0046540), kann doch vor diesem Gericht unter Wahrung des Unmittelbarkeitsgrundsatzes das gesamte Beweisverfahren in einem Zug durchgeführt werden, was typischerweise nicht nur zu einer Erleichterung der Gerichtstätigkeit, sondern auch zu einer Verbilligung und Verkürzung des Verfahrens führt.

| Predicted | Gold |
|---|---|
| `Landesgericht Feldkirch` | `Landesgericht Feldkirch` |

**Example 18** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_6`)


Nach Zurück- bzw Abweisung seiner Begehren in erster Instanz lehnte er wiederholt Richter des Landesgerichts Leoben und des Oberlandesgerichts Graz erfolglos ab (vgl Landesgericht Leoben 2 Nc 24/11d, 2 Nc 25/11a, 2 Nc 28/11t;

| Predicted | Gold |
|---|---|
| `Landesgericht Leoben` | `Landesgericht Leoben` |

**Example 19** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_9`)


Am 26. Februar 2013 lehnte er den Vorsitzenden des Ablehnungssenats beim Landesgericht Leoben als befangen und nach Zurückweisung dieses Antrags (2 Nc 3/13v) die Entscheidungsträger dieses Beschlusses als befangen ab.

| Predicted | Gold |
|---|---|
| `Landesgericht Leoben` | `Landesgericht Leoben` |

**Example 20** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_11`)


Diese Ablehnung wies der Ablehnungssenat beim Landesgericht Leoben (ohne Beteiligung des abgelehnten Richters) mit Beschluss vom 4. Dezember 2013, 2 Nc 31/13m, zurück.

| Predicted | Gold |
|---|---|
| `Landesgericht Leoben` | `Landesgericht Leoben` |

**Example 21** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_6`)


Text Gründe: Mit dem angefochtenen Erkenntnis wurde Dr. Nadja Köpers, Rechtsanwalt in Laahen 3, 3240 Pölla, Österreich, wegen des Verstoßes gegen die Bestimmungen des § 9 (Abs 1) RAO und des § 2 RL-BA der Disziplinarvergehen der Verletzung von Berufspflichten und der Beeinträchtigung von Ehre oder (richtig:) Ansehen des Standes nach § 1 Abs 1 erster und zweiter Fall DSt schuldig erkannt, weil er als Rechtsvertreter der Ehegatten Roman und Elfriede Jakubus in Anträgen auf Aufschiebung der Zwangsversteigerungen für seine Mandanten vom 5. September 2013 in näher bezeichneten Verfahren des Bezirksgerichts Innsbruck und des Bezirksgerichts Amstetten sowie in einer näher genannten Feststellungsklage an das Landesgericht Linz vom 7. Oktober 2013 und in einer Impugnationsklage an das Bezirksgericht Amstetten vom 10. Oktober 2013 jeweils vorgebracht hatte, seine Mandanten hätten sämtliche Verpflichtungen aus einer mit der Bachseewald Heizung AG abgeschlossenen Vereinbarung vom 11. Dezember 2012, insbesondere jene zur unwiderruflichen Antragstellung auf Aufhebung der Höfeeigenschaft einer näher bezeichnenden Liegenschaft in Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich, eingehalten, obwohl ihm zum Zeitpunkt der Antragstellung und Klagseinbringung bekannt war, dass der Antrag auf Aufhebung der Höfeeigenschaft vom 13. Dezember 2012 bereits am 14. Juni 2013 von Roman Janis, durch ihn vertreten, entgegen der zuvor genannten Vereinbarung vom 11. Dezember 2012 wieder zurückgezogen worden war.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |

**Missed by this rule (FN):**

- `Dr. Nadja Köpers` (person)
- `Laahen 3, 3240 Pölla, Österreich` (address)
- `Jakubus` (person)
- `Bezirksgericht Amstetten` (organisation)
- `Bachseewald Heizung AG` (organisation)
- `Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich` (address)
- `Roman Janis` (person)

**Example 22** (doc_id: `deanon_TRAIN/2Ob63_11w`) (sent_id: `deanon_TRAIN/2Ob63_11w_109`)


Nr 18/2008 habe ein anderer Senat des Oberlandesgerichts Linz bzw das Landesgericht Salzburg die dort geregelten Pflegeaufwandsätze zuerkannt.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Example 23** (doc_id: `deanon_TRAIN/3Ob192_11y`) (sent_id: `deanon_TRAIN/3Ob192_11y_11`)


Seine am 4. Februar 2009 eingebrachte Oppositionsklage, deren Begehren darauf abzielt, dass der Anspruch der Beklagten aus dem Unterhaltsvergleich „sowie auf Unterhalt insgesamt“ erloschen ist, stützt derKlägerzusammengefasst auf eine Unterhaltsverwirkung iSd § 94 Abs 2 Satz 2 ABGB: Die Beklagte habe in dem gegen den Kläger geführten Strafverfahren vor dem Landesgericht Salzburg (31 Hv 139/07k), bezogen auf einen Vorfall am 3. Jänner 2006, unrichtig ausgesagt.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Example 24** (doc_id: `deanon_TRAIN/3Ob192_11y`) (sent_id: `deanon_TRAIN/3Ob192_11y_21`)


Unter anderem aufgrund dieses Vorfalls wurde der Kläger im Strafverfahren vor dem Landesgericht Salzburg wegen des Vergehens des Imstichlassens eines Verletzten nach § 94 StGB angeklagt.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Example 25** (doc_id: `deanon_TRAIN/3Ob203_11s`) (sent_id: `deanon_TRAIN/3Ob203_11s_14`)


Mit Beschluss des Landesgerichts Salzburg vom 18. Mai 2011, AZ 22 R 192/11f, 22 R 193/11b, wies das Landesgericht Salzburg die Berufung der Antragsteller mit der Begründung zurück, sie seien im Verfahren mehrfach und umfassend darüber belehrt worden, dass die von ihnen angestrebte Umbestellung der Verfahrenshelfer mangels Vorliegens der gesetzlichen Voraussetzungen nicht stattfinden könne.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Example 26** (doc_id: `deanon_TRAIN/3Ob248_10g`) (sent_id: `deanon_TRAIN/3Ob248_10g_6`)


Mit rechtskräftigem Urteil vom 10. Mai 2007, AZ 19 Cg 136/06a, hat das Landesgericht Leoben infolge erfolgreicher Irrtumsanfechtung (im Hinblick auf die fehlende Vorschadensfreiheit des Fahrzeugs) die nunmehrige Oppositionsklägerin schuldig erkannt, an Philippa Carau Zug um Zug gegen Rückgabe des Pkw einen Betrag von 71.320 EUR sA zu bezahlen.

| Predicted | Gold |
|---|---|
| `Landesgericht Leoben` | `Landesgericht Leoben` |

**Missed by this rule (FN):**

- `Philippa Carau` (person)

**Example 27** (doc_id: `deanon_TRAIN/3Ob32_17b`) (sent_id: `deanon_TRAIN/3Ob32_17b_6`)


Text Begründung: Am 4. Oktober 2010 erließ das Landesgericht Mailand (Tribunale Ordinario di Milano) über Antrag der Betreibenden, einer Gesellschaft mit Sitz in Italien, den elektronischen Mahnbescheid (decreto ingiunitivo telematico) zur Zahl 34300/2010, mit dem der Verpflichteten, einer GmbH mit Sitz in Wien, die in Geschäftsverbindung mit der Betreibenden stand, die Zahlung von 522.094,53 EUR sA an die Betreibende innerhalb von 50 Tagen nach Bekanntmachung des Mahnbescheids aufgetragen wurde.

| Predicted | Gold |
|---|---|
| `Landesgericht Mailand` | `Landesgericht Mailand` |

**Example 28** (doc_id: `deanon_TRAIN/3Ob32_17b`) (sent_id: `deanon_TRAIN/3Ob32_17b_7`)


Dieser enthielt den Hinweis, dass die Verpflichtete Anspruch darauf habe, vor dem Landesgericht Mailand innerhalb von 50 Tagen nach der Bekanntmachung Einspruch zu erheben, widrigenfalls der Mahnbescheid für endgültig und vollstreckbar erklärt werde.

| Predicted | Gold |
|---|---|
| `Landesgericht Mailand` | `Landesgericht Mailand` |

**Example 29** (doc_id: `deanon_TRAIN/4Nc3_12x`) (sent_id: `deanon_TRAIN/4Nc3_12x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel und Dr. Jensik als weitere Richter in der beim Landesgericht Innsbruck zu AZ 59 Cg 92/11x anhängigen Rechtssache der klagenden Partei Rudigkeit Finanzen GmbH, Ing. Sascha Rohkrämer, vertreten durch Mag. Heinz Heher, Rechtsanwalt in Wien, gegen die beklagte Partei Suddorftra Manufaktur GmbH, Ludmilla Nottelmann, vertreten durch Dr. Adrian Hollaender, Rechtsanwalt in Innsbruck, wegen Unterlassung, Urteilsveröffentlichung und 67.606 EUR sA, über die Delegierungsanträge der beklagten Partei gemäß § 31 Abs 2 JN, folgenden Beschluss gefasst:  Spruch Die Anträge der beklagten Partei, die Rechtssache an das „Landesgericht Wien“ bzw Handelsgericht Wien zu delegieren, werden abgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Innsbruck` | `Landesgericht Innsbruck` |
| `Landesgericht Wien` | `Landesgericht Wien` |

**Missed by this rule (FN):**

- `Rudigkeit Finanzen GmbH` (organisation)
- `Ing. Sascha Rohkrämer` (person)
- `Suddorftra Manufaktur GmbH` (organisation)
- `Ludmilla Nottelmann` (person)

**Example 30** (doc_id: `deanon_TRAIN/4Nc3_12x`) (sent_id: `deanon_TRAIN/4Nc3_12x_6`)


Die Klägerin brachte beim Landesgericht Innsbruck eine Unterlassungs- und Zahlungsklage ein.

| Predicted | Gold |
|---|---|
| `Landesgericht Innsbruck` | `Landesgericht Innsbruck` |

**Example 31** (doc_id: `deanon_TRAIN/4Nc3_12x`) (sent_id: `deanon_TRAIN/4Nc3_12x_11`)


Nach Einbringen der Klagebeantwortung beantragte sie die Delegierung an das „Landesgericht Wien“.

| Predicted | Gold |
|---|---|
| `Landesgericht Wien` | `Landesgericht Wien` |

**Example 32** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_10`)


Die Streitteile hätten außerdem keine Gerichtsstandvereinbarung getroffen, weshalb das Landesgericht Klagenfurt zuständig sei.

| Predicted | Gold |
|---|---|
| `Landesgericht Klagenfurt` | `Landesgericht Klagenfurt` |

**Example 33** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_11`)


Der Kläger räumte daraufhin ein, dass die Forderungen gemäß § 55 JN zusammenzurechnen seien, und stellte für den Fall, dass sich das Bezirksgericht Salzburg für unzuständig erklärt, den Antrag, die Klage an das nicht offenbar unzuständige Landesgericht Salzburg zu überweisen.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Missed by this rule (FN):**

- `Bezirksgericht Salzburg` (organisation)

**Example 34** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_12`)


Für den Fall der Unzuständigkeit dieses Landesgerichts beantragte er die Überweisung an das Landesgericht Klagenfurt, allenfalls an das Bezirksgericht Spittal an der Drau.

| Predicted | Gold |
|---|---|
| `Landesgericht Klagenfurt` | `Landesgericht Klagenfurt` |

**Missed by this rule (FN):**

- `Bezirksgericht Spittal` (organisation)

**Example 35** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_13`)


Das Bezirksgericht Salzburg sprach mit rechtskräftigem Beschluss vom 6. Dezember 2019 seine sachliche Unzuständigkeit aus und überwies die Rechtssache an das nicht offenbar unzuständige Landesgericht Salzburg.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Missed by this rule (FN):**

- `Bezirksgericht Salzburg` (organisation)

**Example 36** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_14`)


Das Landesgericht Salzburg erklärte sich mit dem in der Verhandlung am 15. Jänner 2020 verkündeten Beschluss für örtlich unzuständig und überwies die Rechtssache an das nicht offenbar unzuständige Landesgericht Klagenfurt.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |
| `Landesgericht Klagenfurt` | `Landesgericht Klagenfurt` |

**Example 37** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_16`)


Mit rechtskräftigem Beschluss vom 23. Jänner 2020 wies das Landesgericht Klagenfurt die Klage wegen sachlicher Unzuständigkeit zurück, weil ein Vorbringen in der Klage, wonach die Ansprüche zusammenzurechnen seien, nicht erstattet worden sei.

| Predicted | Gold |
|---|---|
| `Landesgericht Klagenfurt` | `Landesgericht Klagenfurt` |

**Example 38** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_17`)


Über Antrag des Klägers hob das Landesgericht Klagenfurt die Zurückweisung der Klage mit rechtskräftigem Beschluss vom 14. Februar 2020 auf und überwies die Rechtssache dem Bezirksgericht Spittal an der Drau.

| Predicted | Gold |
|---|---|
| `Landesgericht Klagenfurt` | `Landesgericht Klagenfurt` |

**Missed by this rule (FN):**

- `Bezirksgericht Spittal` (organisation)

**Example 39** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_19`)


Das Landesgericht Klagenfurt sei an den Unzuständigkeitsbeschluss des Bezirksgerichts Salzburg betreffend die sachliche Unzuständigkeit der Bezirksgerichte gebunden und habe daher seine sachliche Unzuständigkeit, mit der Begründung ein Bezirksgericht sei zuständig, nicht mehr aussprechen können.

| Predicted | Gold |
|---|---|
| `Landesgericht Klagenfurt` | `Landesgericht Klagenfurt` |

**Example 40** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_24`)


Zwar haben hier das Bezirksgericht Salzburg, das Landesgericht Salzburg, das Landesgericht Klagenfurt und das Bezirksgericht Spittal an der Drau jeweils seine Zuständigkeit verneint.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |
| `Landesgericht Klagenfurt` | `Landesgericht Klagenfurt` |

**Missed by this rule (FN):**

- `Bezirksgericht Salzburg` (organisation)
- `Bezirksgericht Spittal` (organisation)

**Example 41** (doc_id: `deanon_TRAIN/5Nc15_20f`) (sent_id: `deanon_TRAIN/5Nc15_20f_25`)


Allerdings besteht ein Streit über die Zuständigkeit iSd § 47 Abs 1 JN nur zwischen dem Landesgericht Klagenfurt und dem Bezirksgericht Spittal an der Drau.

| Predicted | Gold |
|---|---|
| `Landesgericht Klagenfurt` | `Landesgericht Klagenfurt` |

**Missed by this rule (FN):**

- `Bezirksgericht Spittal` (organisation)

**Example 42** (doc_id: `deanon_TRAIN/5Nc20_14g`) (sent_id: `deanon_TRAIN/5Nc20_14g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und die Hofrätin Dr. Lovrek sowie den Hofrat Dr. Höllwerth als weitere Richter in der Rechtssache der klagenden Partei Dr. Sean Schoenenborn, gegen die beklagte Partei Dr. Hagen Kanat, vertreten durch Eisenberger & Herzog Rechtsanwalts GmbH in Graz, wegen 234.164,98 EUR sA, über den Delegierungsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, gemäß § 31 JN anstelle des Landesgerichts für Zivilrechtssachen Graz das Landesgericht Wiener Neustadt, in eventu das Landesgericht Leoben, zur Verhandlung und Entscheidung dieser Rechtssache zu bestimmen, wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Leoben` | `Landesgericht Leoben` |

**Missed by this rule (FN):**

- `Dr. Sean Schoenenborn` (person)
- `Dr. Hagen Kanat` (person)
- `Herzog Rechtsanwalts GmbH` (organisation)
- `Landesgericht Wiener Neustadt` (organisation)

**Example 43** (doc_id: `deanon_TRAIN/5Nc20_14g`) (sent_id: `deanon_TRAIN/5Nc20_14g_6`)


Der Kläger beantragte die Delegation der Rechtsache an das Landesgericht Wiener Neustadt, in eventu das Landesgericht Leoben.

| Predicted | Gold |
|---|---|
| `Landesgericht Leoben` | `Landesgericht Leoben` |

**Missed by this rule (FN):**

- `Landesgericht Wiener Neustadt` (organisation)

**Example 44** (doc_id: `deanon_TRAIN/6Ob182_20p`) (sent_id: `deanon_TRAIN/6Ob182_20p_40`)


Dieser Auffassung hat sich zwischenzeitig bereits zweitinstanzliche Rechtsprechung ausdrücklich (vgl etwa LG Salzburg EFSlg 156.701 [2018], 159.791, 159.792 [2019];

| Predicted | Gold |
|---|---|
| `LG Salzburg` | `LG Salzburg` |

**Example 45** (doc_id: `deanon_TRAIN/6Ob182_20p`) (sent_id: `deanon_TRAIN/6Ob182_20p_41`)


LG Linz EFSlg 156.702 [2018], 159.793 [2019]) und die Entscheidung 9 Ob 57/17y offensichtlich angeschlossen.

| Predicted | Gold |
|---|---|
| `LG Linz` | `LG Linz` |

**Example 46** (doc_id: `deanon_TRAIN/6Ob240_20t`) (sent_id: `deanon_TRAIN/6Ob240_20t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie durch die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Firmenbuchsache der zu FN FN912691n beim Landesgericht Landesgericht Klagenfurt eingetragenen Holtschmidt Versicherung GmbH mit Sitz in der politischen Gemeinde LG Wels, über den Revisionsrekurs der Lohneis Pflege gesellschaft mbH, Auf der Werzer Leitn 27, 9560 Klausen, Österreich, vertreten durch Dr. Robert Mogy, Rechtsanwalt in Klagenfurt, gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. Oktober 2020, GZ 4 R 153/20g-8, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen (§ 71 Abs 3 AußStrG iVm § 15 Abs 2 FBG).

| Predicted | Gold |
|---|---|
| `LG Wels` | `LG Wels` |

**Missed by this rule (FN):**

- `FN912691n` (business_register_number)
- `Landesgericht Klagenfurt` (organisation)
- `Holtschmidt Versicherung GmbH` (organisation)
- `Lohneis Pflege gesellschaft mbH` (organisation)
- `Auf der Werzer Leitn 27, 9560 Klausen, Österreich` (address)

**Example 47** (doc_id: `deanon_TRAIN/7Ob244_10y`) (sent_id: `deanon_TRAIN/7Ob244_10y_9`)


Dagegen erhob der Ablehnungswerber Rekurs an das Landesgericht Leoben, mit dem er die Ablehnung von Richtern der Rechtsmittelsenate in Zivilrechtssachen verband.

| Predicted | Gold |
|---|---|
| `Landesgericht Leoben` | `Landesgericht Leoben` |

**Example 48** (doc_id: `deanon_TRAIN/7Ob244_10y`) (sent_id: `deanon_TRAIN/7Ob244_10y_10`)


Gegen die im Ablehnungsverfahren vor dem Landesgericht Leoben ergangene Entscheidung (GZ 2 Nc 20/10i-3) erhob er Rekurs an das Oberlandesgericht Graz, den er mit einer Ablehnung „sämtlicher Richter des Oberlandesgerichts im Zivilrechtsberufungssenat mit Ausnahme von Dr. Florentine Fromeyer “ verband.

| Predicted | Gold |
|---|---|
| `Landesgericht Leoben` | `Landesgericht Leoben` |

**Missed by this rule (FN):**

- `Dr. Florentine Fromeyer` (person)

**Example 49** (doc_id: `deanon_TRAIN/8Nc31_13w`) (sent_id: `deanon_TRAIN/8Nc31_13w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn als weitere Richter in der beim Landesgericht Salzburg als Arbeits- und Sozialgericht anhängigen Rechtssache der klagenden Partei Buth Analyse GmbH, Anabel Traudtmann, vertreten durch Dr. Ernst Kohlbacher, Rechtsanwalt in Salzburg, gegen die beklagte Partei Christine Schwemmer, vertreten durch Plankel Mayrhofer & Partner, Rechtsanwälte in Dornbirn, wegen 213,52 EUR sA, über den Delegierungsantrag der beklagten Partei den Beschluss gefasst:  Spruch Der Antrag der beklagten Partei, die Rechtssache an das Arbeits- und Sozialgericht Wien zu delegieren, wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Missed by this rule (FN):**

- `Arbeits- und Sozialgericht` (organisation)
- `Buth Analyse GmbH` (organisation)
- `Anabel Traudtmann` (person)
- `Christine Schwemmer` (person)
- `Arbeits- und Sozialgericht Wien` (organisation)

**Example 50** (doc_id: `deanon_TRAIN/8Nc31_13w`) (sent_id: `deanon_TRAIN/8Nc31_13w_4`)


Text Begründung: Mit der am 14. 12. 2012 beim Landesgericht Salzburg als Arbeits- und Sozialgericht eingebrachten Mahnklage begehrte die Klägerin, eine Finanzvermittlungsgesellschaft mit Sitz in Salzburg, von dem im Bundesland Burgenland wohnhaften Beklagten die Rückzahlung von Provisionen aus einem Agentenvertrag.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Missed by this rule (FN):**

- `Arbeits- und Sozialgericht` (organisation)

**Example 51** (doc_id: `deanon_TRAIN/8Ob29_19a`) (sent_id: `deanon_TRAIN/8Ob29_19a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner, die Hofräte Dr. Hargassner und Dr. Stefula und die Hofrätin Mag. Wessely-Kristöfel als weitere Richter in der Erlagssache des Erlegers Landesgericht Innsbruck, vertreten durch die Finanzprokuratur, 1010 Wien, Singerstraße 17–19, gegen die Erlagsgegner 1.

| Predicted | Gold |
|---|---|
| `Landesgericht Innsbruck` | `Landesgericht Innsbruck` |

**Example 52** (doc_id: `deanon_TRAIN/8ObS8_22t`) (sent_id: `deanon_TRAIN/8ObS8_22t_7`)


Das Landesgericht Innsbruck eröffnete mit Beschluss vom 24.

| Predicted | Gold |
|---|---|
| `Landesgericht Innsbruck` | `Landesgericht Innsbruck` |

**Example 53** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_4`)


Text Begründung: Mit ihrer am 22. 12. 2015 beim Landesgericht Salzburg als Arbeits- und Sozialgericht eingebrachten Klage begehrt die in Kagraner Anger 19, 4943 Nonsbach, Österreich (Sbg) ansässige Klägerin vom in Wien wohnhaften Beklagten die Zahlung einer Vertragsstrafe wegen mehrfacher Verstöße gegen das in seinem Agentenvertrag vereinbarte Wettbewerbsverbot.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Missed by this rule (FN):**

- `Arbeits- und Sozialgericht` (organisation)
- `Kagraner Anger 19, 4943 Nonsbach, Österreich` (address)

**Example 54** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_14`)


Das Landesgericht Salzburg als Arbeits- und Sozialgericht sei auch mit den Rechtsangelegenheiten und regelmäßig gleichlautenden Vertragsgrundlagen und Provisions-abrechnungen der Klägerin seit Jahren vertraut.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Missed by this rule (FN):**

- `Arbeits- und Sozialgericht` (organisation)

**Example 55** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_15`)


Auch das Landesgericht Salzburg als Arbeits- und Sozialgericht gab im Ergebnis nach Abwägung von Für und Wider eine negative Stellungnahme ab.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Missed by this rule (FN):**

- `Arbeits- und Sozialgericht` (organisation)

**Example 56** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_18`)


Am 15. 2. 2016 übermittelte das Landesgericht Salzburg als Arbeits- und Sozialgericht im Nachhang eine von der Klägerin am 8.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Missed by this rule (FN):**

- `Arbeits- und Sozialgericht` (organisation)

**Example 57** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_35`)


Zu bedenken ist auch, dass das Landesgericht Salzburg als Arbeits- und Sozialgericht bereits eine Tagsatzung abgehalten und das Prozessprogramm festgelegt hat und mit der Problematik auch aus einem anderen Verfahren vertraut ist, während sich ein Wiener Gericht neu in die Sache einzuarbeiten hätte.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Missed by this rule (FN):**

- `Arbeits- und Sozialgericht` (organisation)

**Example 58** (doc_id: `deanon_TRAIN/9ObA118_19x`) (sent_id: `deanon_TRAIN/9ObA118_19x_5`)


Text Begründung: Mit Beschluss vom 15. Mai 2019, 9 ObA 41/19y, wies der Oberste Gerichtshof die außerordentliche Revision des Klägers in der beim Landesgericht Linz als Arbeits- und Sozialgericht anhängigen Arbeitsrechtssache gegen die beklagte Partei als seine frühere Arbeitgeberin mangels Vorliegens einer Rechtsfrage von erheblicher Bedeutung im Sinne des § 502 Abs 1 ZPO zurück.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |

**Missed by this rule (FN):**

- `Arbeits- und Sozialgericht` (organisation)

**Example 59** (doc_id: `deanon_TRAIN/9ObA78_21t`) (sent_id: `deanon_TRAIN/9ObA78_21t_7`)


2. 2019 brachte der Kläger beim Landesgericht Linz als Arbeits- und Sozialgericht eine Klage gegen die Beklagte ein.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |

**Missed by this rule (FN):**

- `Arbeits- und Sozialgericht` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/12Os34_19w`) (sent_id: `deanon_TRAIN/12Os34_19w_4`)


Text Gründe: Im Ermittlungsverfahren gegen Viktor Mittermair und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und 3 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 703 St 3/11t (nunmehr AZ 713 St 24/18i) der Staatsanwaltschaft Wien, stellte der Beschuldigte Dr. Stefan Tolmin mit Schriftsatz vom 29. November 2017 – soweit im Folgenden von Relevanz – den Antrag auf Einstellung des Ermittlungsverfahrens „gemäß § 108 StPO“ (ON 558), welchen das Landesgericht für Strafsachen Wien mit Beschluss vom 22. Juni 2018, AZ 352 HR 214/11x, abwies (ON 644).

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Viktor Mittermair`(person)
- `Tolmin`(person)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 1** (doc_id: `deanon_TRAIN/13Os22_12b_13Ns16_12z_`) (sent_id: `deanon_TRAIN/13Os22_12b_13Ns16_12z__5`)


Text Gründe: Das Landesgericht für Strafsachen Wien verhängte mit Beschluss vom 9. Dezember 2011 über Mag. Türkan Laurin Bickmann die Untersuchungshaft aus den Gründen der Tatbegehungsgefahr nach § 173 Abs 2 Z 3 lit b und lit d StPO (ON 12).

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Wien`(organisation)
- `Laurin Bickmann`(person)

**Example 2** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__6`)


Dem Landesgericht für Strafsachen Graz wird ein Vorgehen gemäß §§ 14 und 15 dieser Verordnung aufgetragen.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Strafsachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Graz`(organisation)

**Example 3** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__23`)


Seither besteht das Landesgericht als Schöffengericht aus nur einem (Berufs-)Richter und zwei Schöffen (§ 32 Abs 1 dritter Satz StPO).

**False Positives:**

- `Landesgericht als` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__28`)


8. Das Landesgericht für Strafsachen Graz hätte demnach die Staatsanwaltschaft und den Angeklagten von der dauernden Verhinderung des Vorsitzenden des Schöffengerichts in Kenntnis setzen und vor Betrauung eines anderen Richters mit der Urteilsausfertigung nach ihrem Einverständnis fragen müssen.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Strafsachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Graz`(organisation)

**Example 5** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__30`)


Mit Blick auf § 292 letzter Satz StPO sah sich der Oberste Gerichtshof veranlasst, dem Landesgericht für Strafsachen Graz aufzutragen, gemäß §§ 14 und 15 der Kaiserlichen Verordnung vorzugehen.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Strafsachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Graz`(organisation)

**Example 6** (doc_id: `deanon_TRAIN/13Os34_19b`) (sent_id: `deanon_TRAIN/13Os34_19b_5`)


Dieser Beschluss wird aufgehoben und es wird dem Landesgericht für Strafsachen Graz aufgetragen, im Verfahren AZ 16 Hv 32/15a über den Widerruf zu entscheiden.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Strafsachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Graz`(organisation)

**Example 7** (doc_id: `deanon_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_TRAIN/13Os7_20h_13Os8_20f__5`)


In Stattgebung des Antrags der Generalprokuratur wird im außerordentlichen Weg die Wiederaufnahme des Berufungsverfahrens verfügt, der Beschluss des Landesgerichts für Strafsachen Wien vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), aufgehoben und die Sache zur neuerlichen Entscheidung über die Berufung des Angeklagten gegen das Urteil des Bezirksgerichts Innere Stadt Wien vom 27. November 2018 (ON 19 der U-Akten) an das Landesgericht für Strafsachen Wien verwiesen.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Wien`(organisation)

**Example 8** (doc_id: `deanon_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_TRAIN/13Os7_20h_13Os8_20f__10`)


Die am 22. Februar 2019 – innerhalb der Frist des § 467 Abs 1 StPO (vgl Zustellnachweis an ON 19) – ausgeführte Berufung des Robert Unterbusch (ON 21) wies das Landesgericht für Strafsachen Wien als Berufungsgericht mit Beschluss vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23), gemäß § 470 Z 1 StPO als unzulässig zurück, weil die am 27. November 2018 zur Post gegebene Rechtsmittelanmeldung gegen das am 23. November 2018 verkündete Urteil verspätet gewesen sei.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unterbusch`(person)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 9** (doc_id: `deanon_TRAIN/13Os99_19m`) (sent_id: `deanon_TRAIN/13Os99_19m_7`)


Die gegen diesen Ausspruch gerichtete Berufung des Privatbeteiligten (ON 23) wies das Oberlandesgericht Graz mit dem nunmehr angefochtenen Beschluss im Wesentlichen mit der Begründung zurück, auch im Verfahren vor dem Landesgericht als Einzelrichter stehe dem Privatbeteiligten die Berufung nur bei vollständiger Verweisung mit seinen Ansprüchen auf den Zivilrechtsweg (trotz Verurteilung) offen, während die Höhe des Zuspruchs nicht bekämpfbar sei (vgl zum kollegialgerichtlichen Verfahren § 283 Abs 4 iVm § 366 Abs 3 StPO).

**False Positives:**

- `Landesgericht als` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_TRAIN/13Os99_19m`) (sent_id: `deanon_TRAIN/13Os99_19m_11`)


Diese Regelung findet zufolge § 489 Abs 1 StPO auch im Verfahren vor dem Landesgericht als Einzelrichter Anwendung.

**False Positives:**

- `Landesgericht als` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_TRAIN/14Os132_10h`) (sent_id: `deanon_TRAIN/14Os132_10h_4`)


Text Gründe: Gegen Tomsilav Alexejenko ist beim Landesgericht für Strafsachen Wien ein - im Stadium der Hauptverhandlung befindliches - Verfahren wegen der Verbrechen des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und nach § 28a Abs 1 fünfter Fall, Abs 4 Z 3 SMG anhängig, in dem sich der Angeklagte seit 5. April 2010 in Untersuchungshaft befindet (ON 20).

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alexejenko`(person)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 12** (doc_id: `deanon_TRAIN/14Os63_12i`) (sent_id: `deanon_TRAIN/14Os63_12i_8`)


Mit Erkenntnis des Obersten Gerichtshofs vom 30. August 2011, AZ 14 Os 48/11g (ON 74 der Hv-Akten), wurde das Urteil, das im Übrigen unberührt blieb, in teilweiser Stattgebung der dagegen erhobenen Nichtigkeitsbeschwerde des Angeklagten im Schuldspruch I und demzufolge auch im Strafausspruch aufgehoben, im Umfang der Aufhebung eine neue Hauptverhandlung angeordnet und die Sache an das Landesgericht St. Pölten verwiesen.

**False Positives:**

- `Landesgericht St` — partial — pred is substring of gold: `Landesgericht St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht St. Pölten`(organisation)

**Example 13** (doc_id: `deanon_TRAIN/15Os110_17s`) (sent_id: `deanon_TRAIN/15Os110_17s_10`)


Aus Anlass eines vom Angeklagten am 17. Februar 2017 eingebrachten Antrags auf Aufhebung der Untersuchungshaft (ON 95) setzte das Landesgericht für Strafsachen Graz mit Beschluss vom 23. Februar 2017 die am 7. September 2016 verhängte (ON 11) – und danach wiederholt prolongierte (ON 32, 71) – Untersuchungshaft aus den Haftgründen der Flucht- und der Tatbegehungsgefahr nach § 173 Abs 2 Z 1 und Z 3 lit a StPO fort (ON 100).

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Strafsachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Graz`(organisation)

**Example 14** (doc_id: `deanon_TRAIN/15Os43_13g`) (sent_id: `deanon_TRAIN/15Os43_13g_12`)


Rechtliche Beurteilung Das Urteil des Landesgerichts Korneuburg vom 13. Juni 2012, GZ 505 Hv 5/11x-69, steht - wie die Generalprokuratur in ihrer Nichtigkeitsbeschwerde zur Wahrung des Gesetzes zutreffend ausführt - in seinem Punkt A./2./ mit dem Gesetz nicht im Einklang: Gemäß der auch für das Verfahren vor dem Landesgericht als Einzelrichter geltenden (§ 488 Abs 1 StPO) Bestimmung des § 270 Abs 4 StPO hat eine - unter den in dieser Vorschrift genannten, hier vorliegenden Voraussetzungen zulässigerweise - gekürzte Urteilsaus- fertigung die in § 270 Abs 2 StPO angeführten Angaben mit Ausnahme der Entscheidungsgründe, also auch die in § 260 StPO (§ 270 Abs 4 Z 1 StPO) genannten Punkte zu enthalten.

**False Positives:**

- `Landesgericht als` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Herbes&Vißers Heizung GmbH, Waldemar Lokämper, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Traun-Luftfahrt GmbH, VetR DDr. Walter Stuehrmann, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

**False Positives:**

- `Landesgericht Wiener` — partial — pred is substring of gold: `Landesgericht Wiener Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Wiener Neustadt`(organisation)
- `Herbes&Vißers Heizung GmbH`(organisation)
- `Waldemar Lokämper`(person)
- `Traun-Luftfahrt GmbH`(organisation)
- `VetR DDr. Walter Stuehrmann`(person)
- `Landesgericht Feldkirch`(organisation)

**Example 16** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_5`)


Text Begründung: Der Kläger macht in einem Verfahren vor dem Landesgericht Leoben Amtshaftungsansprüche gegen die Republik Österreich, sonstige Schadenersatzansprüche gegen eine Journalistin und die Inhaberin eines Printmediums sowie Feststellungsansprüche gegen alle beklagten Parteien geltend.

**False Positives:**

- `Landesgericht Leoben` — partial — pred is substring of gold: `Landesgericht Leoben Amtshaftungsansprüche`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Leoben Amtshaftungsansprüche`(organisation)

**Example 17** (doc_id: `deanon_TRAIN/1Ob78_22k`) (sent_id: `deanon_TRAIN/1Ob78_22k_8`)


Das Landesgericht für Zivilrechtssachen Wien gab der gegen das Ersturteil gerichteten Berufung des Beklagten mit dem (dessen Verfahrenshelfer am 17.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 18** (doc_id: `deanon_TRAIN/1Ob78_22k`) (sent_id: `deanon_TRAIN/1Ob78_22k_11`)


diese Entscheidung wurde vom Landesgericht für Zivilrechtssachen Wien später bestätigt.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 19** (doc_id: `deanon_TRAIN/3Ob1_20y`) (sent_id: `deanon_TRAIN/3Ob1_20y_9`)


Der von den Klägern aufgrund dieses Urteils beim Bezirksgericht Melk eingebrachte, in erster Instanz erfolgreiche Antrag auf Bewilligung der Exekution gemäß § 350 EO zur Durchsetzung der Einverleibung der Dienstbarkeit wurde vom Landesgericht St. Pölten als Rekursgericht mit Beschluss vom 1. Februar 2018 mit der Begründung abgewiesen, dass sich die dem Titel angeschlossenen Pläne (Beilage ./B1 und ON 71) nicht ohne weiteres in Übereinstimmung bringen ließen, weshalb der Verlauf des Servitutswegs dem Titel nicht eindeutig entnommen werden könne.

**False Positives:**

- `Landesgericht St` — partial — pred is substring of gold: `Landesgericht St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Melk`(organisation)
- `Landesgericht St. Pölten`(organisation)

**Example 20** (doc_id: `deanon_TRAIN/4Fsc1_10z`) (sent_id: `deanon_TRAIN/4Fsc1_10z_5`)


Diesen Ablehnungsantrag hat das Landesgericht für Zivilrechtssachen Wien am 19.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 21** (doc_id: `deanon_TRAIN/4Fsc1_10z`) (sent_id: `deanon_TRAIN/4Fsc1_10z_11`)


9. 2009 hat das Landesgericht für Zivilrechtssachen Wien am 12.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 22** (doc_id: `deanon_TRAIN/5Nc20_14g`) (sent_id: `deanon_TRAIN/5Nc20_14g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und die Hofrätin Dr. Lovrek sowie den Hofrat Dr. Höllwerth als weitere Richter in der Rechtssache der klagenden Partei Dr. Sean Schoenenborn, gegen die beklagte Partei Dr. Hagen Kanat, vertreten durch Eisenberger & Herzog Rechtsanwalts GmbH in Graz, wegen 234.164,98 EUR sA, über den Delegierungsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, gemäß § 31 JN anstelle des Landesgerichts für Zivilrechtssachen Graz das Landesgericht Wiener Neustadt, in eventu das Landesgericht Leoben, zur Verhandlung und Entscheidung dieser Rechtssache zu bestimmen, wird abgewiesen.

**False Positives:**

- `Landesgericht Wiener` — partial — pred is substring of gold: `Landesgericht Wiener Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Sean Schoenenborn`(person)
- `Dr. Hagen Kanat`(person)
- `Herzog Rechtsanwalts GmbH`(organisation)
- `Landesgericht Wiener Neustadt`(organisation)
- `Landesgericht Leoben`(organisation)

**Example 23** (doc_id: `deanon_TRAIN/5Nc20_14g`) (sent_id: `deanon_TRAIN/5Nc20_14g_6`)


Der Kläger beantragte die Delegation der Rechtsache an das Landesgericht Wiener Neustadt, in eventu das Landesgericht Leoben.

**False Positives:**

- `Landesgericht Wiener` — partial — pred is substring of gold: `Landesgericht Wiener Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Wiener Neustadt`(organisation)
- `Landesgericht Leoben`(organisation)

**Example 24** (doc_id: `deanon_TRAIN/5Nc20_14g`) (sent_id: `deanon_TRAIN/5Nc20_14g_8`)


Das Landesgericht für Zivilrechtssachen Graz erachtete eine Delegierung nicht als zweckmäßig.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_TRAIN/6Ob16_20a`) (sent_id: `deanon_TRAIN/6Ob16_20a_5`)


Text Begründung: Mit der beim Landesgericht für Zivilrechtssachen Wien eingebrachten Klage begehrt die Klägerin von der in Wien wohnhaften Beklagten die Zahlung von 422.136,06 EUR sA und erhebt diverse Eventualbegehren.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 26** (doc_id: `deanon_TRAIN/6Ob240_20t`) (sent_id: `deanon_TRAIN/6Ob240_20t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie durch die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Firmenbuchsache der zu FN FN912691n beim Landesgericht Landesgericht Klagenfurt eingetragenen Holtschmidt Versicherung GmbH mit Sitz in der politischen Gemeinde LG Wels, über den Revisionsrekurs der Lohneis Pflege gesellschaft mbH, Auf der Werzer Leitn 27, 9560 Klausen, Österreich, vertreten durch Dr. Robert Mogy, Rechtsanwalt in Klagenfurt, gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. Oktober 2020, GZ 4 R 153/20g-8, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen (§ 71 Abs 3 AußStrG iVm § 15 Abs 2 FBG).

**False Positives:**

- `Landesgericht Landesgericht` — positional overlap with gold: `Landesgericht Klagenfurt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FN912691n`(business_register_number)
- `Landesgericht Klagenfurt`(organisation)
- `Holtschmidt Versicherung GmbH`(organisation)
- `LG Wels`(organisation)
- `Lohneis Pflege gesellschaft mbH`(organisation)
- `Auf der Werzer Leitn 27, 9560 Klausen, Österreich`(address)

**Example 27** (doc_id: `deanon_TRAIN/6Ob82_15z`) (sent_id: `deanon_TRAIN/6Ob82_15z_12`)


Das Landesgericht für Zivilrechtssachen Wien wies mit Beschluss vom 22. 4. 2014 (40 R 94/14s) den Rekurs (32 Nc 121/13d-20) und mit Beschluss vom 14.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 28** (doc_id: `deanon_TRAIN/6Ob82_15z`) (sent_id: `deanon_TRAIN/6Ob82_15z_14`)


Mit Beschluss vom 11. 9. 2014, 33 Nc 34/14z-6, wies das Landesgericht für Zvilrechtssachen Wien den auf § 20 Abs 1 Z 5 JN gestützten Ablehnungsantrag des Beklagten gegen eine Richterin, die an der Fassung des Beschlusses vom 14.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_TRAIN/6Ob82_15z`) (sent_id: `deanon_TRAIN/6Ob82_15z_17`)


Das Oberlandesgericht Wien als Rekursgericht stellte mit Beschluss vom 22. 10. 2014, 13 R 170/14m-10, dem Landesgericht für Zivilrechtssachen Wien den Rekurs mit dem Auftrag zurück, das Verbesserungsverfahren zur Beseitigung des Formgebrechens der fehlenden Unterschrift eines Rechtsanwalts einzuleiten.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 30** (doc_id: `deanon_TRAIN/6Ob82_15z`) (sent_id: `deanon_TRAIN/6Ob82_15z_18`)


Das Landesgericht für Zivilrechtssachen Wien trug dem Beklagten mit Beschluss vom 12.

**False Positives:**

- `Landesgericht für` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

</details>

---

## `Labor Court Vienna`

**F1:** 0.093 | **Precision:** 1.000 | **Recall:** 0.049  

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
| 1.000 | 0.049 | 0.093 | 34 | 34 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 34 | 0 | 554 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10ObS150_17g`) (sent_id: `deanon_TRAIN/10ObS150_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Ing. Christian Stangl-Brachnik, MA BA und Mag. Claudia Gründel (beide aus dem Kreis der Arbeitgeber) als weitere Richter in der Sozialrechtssache der klagenden Partei OStR Esra Jakubait, vertreten durch Dr. Thomas Stampfer und Dr. Christoph Orgler, Rechtsanwälte in Graz, gegen die beklagte Partei Sozialversicherungsanstalt der Bauern, 1031 Wien, Ghegastraße 1, vertreten durch Dr. Michael Stögerer, Rechtsanwalt in Wien, wegen Ausgleichszulage, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2017, GZ 7 Rs 37/17s-11, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. April 2017, GZ 43 Cgs 113/17p-7, teils bestätigt und teils abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `OStR Esra Jakubait` (person)

**Example 1** (doc_id: `deanon_TRAIN/10ObS21_10a`) (sent_id: `deanon_TRAIN/10ObS21_10a_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Schinko als Vorsitzenden, die Hofräte Dr. Fellinger und Dr. Hoch sowie die fachkundigen Laienrichter Mag. Irene Kienzl (aus dem Kreis der Arbeitgeber) und Eva-Maria Florianschütz (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Gertrud Johanna Ostrovska, gegen die beklagte Partei Steiermärkische Gebietskrankenkasse, 8011 Graz, Josef-Pongratz-Platz 1, vertreten durch Das Haus des Rechts Rechtsanwälte Destaller-Mader in Graz, wegen Kostenübernahme, infolge Rekurses der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 19. November 2009, GZ 8 Rs 73/09f-10, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 1. September 2009, GZ 29 Cgs 90/09s-6, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Ostrovska` (person)

**Example 2** (doc_id: `deanon_TRAIN/10ObS21_10a`) (sent_id: `deanon_TRAIN/10ObS21_10a_133`)


Auch dieser Umstand spricht dafür, dass auch die Ablehnung der Kostenübernahme für ein verordnetes Heilmittel durch eine Feststellungsklage beim Arbeits- und Sozialgericht bekämpft werden kann.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Example 3** (doc_id: `deanon_TRAIN/10ObS49_15a`) (sent_id: `deanon_TRAIN/10ObS49_15a_4`)


Brigitte Augustin (aus dem Kreis der Arbeitgeber) und Peter Schönhofer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Samantha Neunteufl, Deutschland, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Vorarlberger Gebietskrankenkasse, Jahngasse 4, 6850 Dornbirn, vertreten durch Hoffmann & Brandstätter Rechtsanwälte KG in Innsbruck, wegen Kinderbetreuungsgeld, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 12. Februar 2015, GZ 11 Rs 4/15k-10, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 28. Oktober 2014, GZ 20 Cgs 71/14k-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Samantha Neunteufl` (person)

**Example 4** (doc_id: `deanon_TRAIN/10ObS92_17b`) (sent_id: `deanon_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Dr.in Gerlinde Saltzmann, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Dr.in Gerlinde Saltzmann` (person)
- `Pensionsversicherungsanstalt` (organisation)

**Example 5** (doc_id: `deanon_TRAIN/8Nc31_13w`) (sent_id: `deanon_TRAIN/8Nc31_13w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn als weitere Richter in der beim Landesgericht Salzburg als Arbeits- und Sozialgericht anhängigen Rechtssache der klagenden Partei Buth Analyse GmbH, Anabel Traudtmann, vertreten durch Dr. Ernst Kohlbacher, Rechtsanwalt in Salzburg, gegen die beklagte Partei Christine Schwemmer, vertreten durch Plankel Mayrhofer & Partner, Rechtsanwälte in Dornbirn, wegen 213,52 EUR sA, über den Delegierungsantrag der beklagten Partei den Beschluss gefasst:  Spruch Der Antrag der beklagten Partei, die Rechtssache an das Arbeits- und Sozialgericht Wien zu delegieren, wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |
| `Arbeits- und Sozialgericht Wien` | `Arbeits- und Sozialgericht Wien` |

**Missed by this rule (FN):**

- `Landesgericht Salzburg` (organisation)
- `Buth Analyse GmbH` (organisation)
- `Anabel Traudtmann` (person)
- `Christine Schwemmer` (person)

**Example 6** (doc_id: `deanon_TRAIN/8Nc31_13w`) (sent_id: `deanon_TRAIN/8Nc31_13w_4`)


Text Begründung: Mit der am 14. 12. 2012 beim Landesgericht Salzburg als Arbeits- und Sozialgericht eingebrachten Mahnklage begehrte die Klägerin, eine Finanzvermittlungsgesellschaft mit Sitz in Salzburg, von dem im Bundesland Burgenland wohnhaften Beklagten die Rückzahlung von Provisionen aus einem Agentenvertrag.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Landesgericht Salzburg` (organisation)

**Example 7** (doc_id: `deanon_TRAIN/8Nc31_13w`) (sent_id: `deanon_TRAIN/8Nc31_13w_6`)


Gleichzeitig beantragte er die Delegierung der Rechtssache an das Arbeits- und Sozialgericht Wien.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht Wien` | `Arbeits- und Sozialgericht Wien` |

**Example 8** (doc_id: `deanon_TRAIN/8ObA10_21k`) (sent_id: `deanon_TRAIN/8ObA10_21k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Wessely-Kristöfel als weitere Richter sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner (aus dem Kreis der Arbeitgeber) und Wolfgang Jelinek (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Thebuss + Großekemper Bildung AG, Univ.-Prof.in Anna Helffer, vertreten durch Dr. Raimund Gehart, Rechtsanwalt in Wien, gegen die beklagte Partei Paulina Strnadl, vertreten durch Dr. Franz Josef Hofer Rechtsanwalt GmbH in Friesach, wegen 5.625,88 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 10. Dezember 2020, GZ 6 Ra 69/20v-19, mit dem das Urteil des Landesgerichts Klagenfurt als Arbeits- und Sozialgericht vom 15. Mai 2020, GZ 35 Cga 90/19x-11, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Thebuss + Großekemper Bildung AG` (organisation)
- `Univ.-Prof.in Anna Helffer` (person)
- `Paulina Strnadl` (person)
- `Franz Josef Hofer Rechtsanwalt GmbH` (organisation)

**Example 9** (doc_id: `deanon_TRAIN/8ObA1_13z`) (sent_id: `deanon_TRAIN/8ObA1_13z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner sowie die fachkundigen Laienrichter Dr. Christoph Kainz und Horst Nurschinger als weitere Richter in der Arbeitsrechtssache der klagenden Partei Heinz Hennerich, vertreten durch Dr. Gerhard Hiebler, Dr. Gerd Grebenjak, Rechtsanwälte in Leoben, wider die beklagte Partei Verein DDr. Holger Müllegger, vertreten durch Dr. Dieter Neger, Rechtsanwalt in Graz, wegen Entlassungsanfechtung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Oktober 2012, GZ 6 Ra 67/12p-12, mit dem über Berufung der klagenden Partei das Urteil des Landesgerichts Leoben als Arbeits- und Sozialgericht vom 2. Juli 2012, GZ 20 Cga 23/11v-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Hennerich` (person)
- `DDr. Holger Müllegger` (person)

**Example 10** (doc_id: `deanon_TRAIN/8ObS8_22t`) (sent_id: `deanon_TRAIN/8ObS8_22t_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Stefula als weitere Richter (Senat gemäß § 11a Abs 3 Z 2 ASGG) in der Sozialrechtssache der klagenden Partei Holger Sykorski, vertreten durch Dr. Herbert Marschitz und andere Rechtsanwälte in Kufstein, gegen die beklagte Partei IEF-Service GmbH, 6020 Innsbruck, Meraner Straße 1, vertreten durch die Finanzprokuratur in Wien, wegen 34.726 EUR sA (Insolvenzentgelt), über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 18. Oktober 2022, GZ 25 Rs 56/22d-34, mit dem das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 9. Juni 2022, GZ 44 Cgs 43/21m-27, samt dem ihm vorangegangenen Verfahren für nichtig erklärt und die Klage zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Holger Sykorski` (person)

**Example 11** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Dehn und den Hofrat des Obersten Gerichtshofs Dr. Hargassner als weitere Richter in der Arbeitsrechtssache der klagenden Partei WestSicherheit GmbH, OMedR Paulina von Tietzen, vertreten durch Dr. Ernst Kohlbacher, Rechtsanwalt in Salzburg, gegen die beklagte Partei Amber Landscheid, vertreten durch Dr. Karl-Heinz Plankel, Dr. Herwig Mayrhofer ua, Rechtsanwälte in Dornbirn, wegen 15.600 EUR sA, über den Delegierungsantrag der beklagten Partei den Beschluss gefasst:  Spruch Der Antrag der beklagten Partei, anstelle des Landesgerichts Salzburg als Arbeits- und Sozialgericht das Arbeits- und Sozialgericht Wien zur Verhandlung und Entscheidung der Rechtssache des Landesgerichts Salzburg als Arbeits- und Sozialgericht AZ 15 Cga 88/15d zu bestimmen, wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |
| `Arbeits- und Sozialgericht Wien` | `Arbeits- und Sozialgericht Wien` |
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `WestSicherheit GmbH` (organisation)
- `OMedR Paulina von Tietzen` (person)
- `Amber Landscheid` (person)

**Example 12** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_4`)


Text Begründung: Mit ihrer am 22. 12. 2015 beim Landesgericht Salzburg als Arbeits- und Sozialgericht eingebrachten Klage begehrt die in Kagraner Anger 19, 4943 Nonsbach, Österreich (Sbg) ansässige Klägerin vom in Wien wohnhaften Beklagten die Zahlung einer Vertragsstrafe wegen mehrfacher Verstöße gegen das in seinem Agentenvertrag vereinbarte Wettbewerbsverbot.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Landesgericht Salzburg` (organisation)
- `Kagraner Anger 19, 4943 Nonsbach, Österreich` (address)

**Example 13** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_8`)


Es werde die Delegierung der Rechtssache an das Arbeits- und Sozialgericht Wien beantragt, weil der Beklagte dort seinen Lebensmittelpunkt habe und der Großteil der im Verfahren beantragten Zeugen aus dem Bereich Wien und Wien-Umgebung komme.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht Wien` | `Arbeits- und Sozialgericht Wien` |

**Example 14** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_14`)


Das Landesgericht Salzburg als Arbeits- und Sozialgericht sei auch mit den Rechtsangelegenheiten und regelmäßig gleichlautenden Vertragsgrundlagen und Provisions-abrechnungen der Klägerin seit Jahren vertraut.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Landesgericht Salzburg` (organisation)

**Example 15** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_15`)


Auch das Landesgericht Salzburg als Arbeits- und Sozialgericht gab im Ergebnis nach Abwägung von Für und Wider eine negative Stellungnahme ab.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Landesgericht Salzburg` (organisation)

**Example 16** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_18`)


Am 15. 2. 2016 übermittelte das Landesgericht Salzburg als Arbeits- und Sozialgericht im Nachhang eine von der Klägerin am 8.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Landesgericht Salzburg` (organisation)

**Example 17** (doc_id: `deanon_TRAIN/9Nc5_16h`) (sent_id: `deanon_TRAIN/9Nc5_16h_35`)


Zu bedenken ist auch, dass das Landesgericht Salzburg als Arbeits- und Sozialgericht bereits eine Tagsatzung abgehalten und das Prozessprogramm festgelegt hat und mit der Problematik auch aus einem anderen Verfahren vertraut ist, während sich ein Wiener Gericht neu in die Sache einzuarbeiten hätte.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Landesgericht Salzburg` (organisation)

**Example 18** (doc_id: `deanon_TRAIN/9Ob59_20x`) (sent_id: `deanon_TRAIN/9Ob59_20x_17`)


Weiters begehrt der Kläger die Feststellung der Haftung des Beklagten für die ihm künftig aus der unrichtigen Gutachtenserstellung durch den Beklagten im Verfahren vor dem Arbeits- und Sozialgericht Wien zur AZ 25 Cgs 77/16w entstehenden Schaden.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht Wien` | `Arbeits- und Sozialgericht Wien` |

**Example 19** (doc_id: `deanon_TRAIN/9ObA118_18w`) (sent_id: `deanon_TRAIN/9ObA118_18w_4`)


Gabriele Svirak in der Arbeitsrechtssache der klagenden Partei Evelyn Lichtwer, vertreten durch Dr. Gerhard Hiebler, Dr. Gerd Grebenjak, Rechtsanwälte in Leoben, gegen die beklagte Partei Inn Wiltri Systeme GmbH, DDr. Johann Gerkens, vertreten durch Dr. Helmut Fetz, Dr. Birgit Fetz ua, Rechtsanwälte in Leoben, wegen 500 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. August 2018, GZ 7 Ra 23/18h-12, mit dem der Berufung der klagenden Partei gegen das Urteil des Landesgerichts Leoben als Arbeits- und Sozialgericht vom 14. Dezember 2017, GZ 23 Cga 75/17x-7, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision der klagenden Partei wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Evelyn Lichtwer` (person)
- `Inn Wiltri Systeme GmbH` (organisation)
- `DDr. Johann Gerkens` (person)

**Example 20** (doc_id: `deanon_TRAIN/9ObA118_19x`) (sent_id: `deanon_TRAIN/9ObA118_19x_5`)


Text Begründung: Mit Beschluss vom 15. Mai 2019, 9 ObA 41/19y, wies der Oberste Gerichtshof die außerordentliche Revision des Klägers in der beim Landesgericht Linz als Arbeits- und Sozialgericht anhängigen Arbeitsrechtssache gegen die beklagte Partei als seine frühere Arbeitgeberin mangels Vorliegens einer Rechtsfrage von erheblicher Bedeutung im Sinne des § 502 Abs 1 ZPO zurück.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Landesgericht Linz` (organisation)

**Example 21** (doc_id: `deanon_TRAIN/9ObA120_12f`) (sent_id: `deanon_TRAIN/9ObA120_12f_4`)


Dr. Helwig Aubauer und Mag. Regina Bauer-Albrecht als weitere Richter in der Arbeitsrechtssache der klagenden Partei Heidelinde Hobl, vertreten durch Dr. Dieter Gallistl, Rechtsanwalt in Linz, wider die beklagte Partei Elvira Vacha, vertreten durch Dr. Andreas Grassl, Rechtsanwalt in Wien, wegen Feststellung (Streitwert 174,77 EUR), über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. Juni 2012, GZ 12 Ra 48/12h-15, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts Wels als Arbeits- und Sozialgericht vom 31. Jänner 2012, GZ 16 Cga 154/11i-11, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Hobl` (person)
- `Elvira Vacha` (person)

**Example 22** (doc_id: `deanon_TRAIN/9ObA151_09k`) (sent_id: `deanon_TRAIN/9ObA151_09k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten des Obersten Gerichtshofs Dr. Rohrer als Vorsitzenden und die Hofräte des Obersten Gerichtshofs Dr. Hradil und Dr. Hopf sowie die fachkundigen Laienrichter KR Mag. Paul Kunsky und Franz Boindl als weitere Richter in der Arbeitsrechtssache der klagenden Partei PhD Ottfried Leonhardi, vertreten durch Dr. Charlotte Lindenberger, Rechtsanwältin in Steyr, gegen die beklagte Partei Baltromei Wind GmbH, Petra Ditrich, vertreten durch Dr. Otto Hauck, Rechtsanwalt in Kirchdorf, wegen 1.028,19 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 16. Oktober 2009, GZ 11 Ra 88/09d-10, womit das Urteil des Landesgerichts Steyr als Arbeits- und Sozialgericht vom 2. Juli 2009, GZ 24 Cga 9/09p-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch Der Revision wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `PhD Ottfried Leonhardi` (person)
- `Baltromei Wind GmbH` (organisation)
- `Petra Ditrich` (person)

**Example 23** (doc_id: `deanon_TRAIN/9ObA41_16v`) (sent_id: `deanon_TRAIN/9ObA41_16v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätinnen des Obersten Gerichtshofs Hon.-Prof. Dr. Dehn und Mag. Korn sowie die fachkundigen Laienrichter Dr. Johannes Pflug und Mag. Robert Brunner als weitere Richter in der Arbeitsrechtssache der klagenden Partei Mag. Joseph Mehl, vertreten durch Dr. Stephan Rainer und Dr. Andreas Ruetz, Rechtsanwälte in Innsbruck, gegen die beklagte Partei Heiko Ayna, vertreten durch Korn Rechtsanwälte OG in Wien, wegen 40.647,29 EUR brutto sA über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. Jänner 2016, GZ 15 Ra 16/16i-31, mit dem der Berufung der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 11. November 2015, GZ 43 Cga 118/14b-26, nicht Folge gegeben wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Mag. Joseph Mehl` (person)
- `Heiko Ayna` (person)

**Example 24** (doc_id: `deanon_TRAIN/9ObA43_12g`) (sent_id: `deanon_TRAIN/9ObA43_12g_4`)


Werner Keyzers, 4. Jaromir Heinrichson, alle vertreten durch die Advokaturbüro Jelenik & Partner AG, Landstraße 60, FL-9490 Vaduz (Zustellungsbevollmächtigter gemäß § 6 EIRAG: Mag. Norbert Wanker, Wasenweg 23, 6800 Feldkirch), gegen die beklagte Partei Wichtmann u. Staneck Energie GmbH, Dimitri Brunemann, vertreten durch Dr. Andreas Grundei, Rechtsanwalt in Wien, wegen Feststellung (Streitwert 10.000 EUR), über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 21. Februar 2012, GZ 15 Ra 13/12t-16, womit das Urteil des Landesgerichts Feldkirch als Arbeits- und Sozialgericht vom 4. Oktober 2011, GZ 35 Cga 85/11p-10, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Parteien wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Werner Keyzers` (person)
- `Jaromir Heinrichson` (person)
- `Partner AG` (organisation)
- `Wichtmann u. Staneck Energie GmbH` (organisation)
- `Dimitri Brunemann` (person)

**Example 25** (doc_id: `deanon_TRAIN/9ObA44_11b`) (sent_id: `deanon_TRAIN/9ObA44_11b_5`)


Dr. Wolfgang List, Rechtsanwalt in Wien, wider die beklagte Partei und Gegnerin der gefährdeten Partei Valerian Urbahn, vertreten durch Dr. J. Pfurtscheller, Dr. Orgler, Mag. Huber, Rechtsanwälte in Innsbruck, wegen Feststellung des Fortbestands eines Arbeitsverhältnisses, in eventu Anfechtung einer Kündigung nach § 105 ArbVG (Streitwert jeweils 31.000 EUR), in eventu 18.957 EUR sA, hier Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der klagenden und gefährdeten Partei gegen den Beschluss des Oberlandesgerichts Innsbruck als Rekursgericht in Arbeits- und Sozialrechtssachen vom 24. Februar 2011, GZ 15 Ra 11/11x-15, mit dem infolge Rekurses der klagenden und gefährdeten Partei der Beschluss des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 9. Dezember 2010, GZ 43 Cga 126/10y-8, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Valerian Urbahn` (person)

**Example 26** (doc_id: `deanon_TRAIN/9ObA4_13y`) (sent_id: `deanon_TRAIN/9ObA4_13y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Werner Rodlauer und Mag. Robert Brunner als weitere Richter in der Arbeitsrechtssache der klagenden Partei Maria Maritz, vertreten durch Dr. Susanne Kuen, Rechtsanwältin in Wien, gegen die beklagte Partei PHG Möbel Dienstleistungen GmbH, Zeno Speckl, vertreten durch Fellner Wratzfeld & Partner Rechtsanwälte GmbH in Wien, wegen 125.731,44 EUR sA, über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 30. Oktober 2012, GZ 11 Ra 82/12a-74, mit dem das Urteil des Landesgerichts Steyr als Arbeits- und Sozialgericht vom 31. Juli 2012, GZ 9 Cga 245/08g-70, aufgehoben und die Rechtssache an das Erstgericht zurückverwiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Maria Maritz` (person)
- `PHG Möbel Dienstleistungen GmbH` (organisation)
- `Zeno Speckl` (person)

**Example 27** (doc_id: `deanon_TRAIN/9ObA78_21t`) (sent_id: `deanon_TRAIN/9ObA78_21t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsrekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau und den Hofrat des Obersten Gerichtshofs Dr. Hargassner als weitere Richter in der Arbeitsrechtssache der klagenden Partei Ing. DI (FH) Griselda Eicholz, nunmehr vertreten durch Mag. Dr. Helmut Blum, Rechtsanwalt in Linz, gegen die beklagte Partei HochLuftfahrt GmbH, Saphira Thiehle, wegen Leistung, über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht in Arbeits- und Sozialrechtssachen vom 13. Mai 2019, GZ 11 Ra 33/19f-23, mit dem der Rekurs des Klägers gegen den Beschluss des Landesgerichts Linz als Arbeits- und Sozialgericht vom 8. April 2019, GZ 7 Cga 25/19k-9, zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Griselda Eicholz` (person)
- `HochLuftfahrt GmbH` (organisation)
- `Saphira Thiehle` (person)

**Example 28** (doc_id: `deanon_TRAIN/9ObA78_21t`) (sent_id: `deanon_TRAIN/9ObA78_21t_7`)


2. 2019 brachte der Kläger beim Landesgericht Linz als Arbeits- und Sozialgericht eine Klage gegen die Beklagte ein.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Landesgericht Linz` (organisation)

**Example 29** (doc_id: `deanon_TRAIN/9ObA82_20d`) (sent_id: `deanon_TRAIN/9ObA82_20d_3`)


Kopf Der Oberste Gerichtshof hat als Revisions- und Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau und den Hofrat des Obersten Gerichtshofs Dr. Hargassner sowie die fachkundigen Laienrichter Mag. Dr. Bernhard Gruber (aus dem Kreis der Arbeitgeber) und Angela Taschek (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Marktgemeinde Andrea Wiggering, vertreten durch Ehrenhöfer & Häusler Rechtsanwälte GmbH in Wiener Neustadt, gegen die beklagte Partei Cassandra Noldens, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, wegen 28.428,01 EUR sA, über den Rekurs und die außerordentliche Revision der klagenden Partei gegen den Beschluss (I.) und das Urteil (II.) des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 22. Juli 2020, GZ 9 Ra 111/19p-25, mit dem das Urteil des Landesgerichts Wiener Neustadt als Arbeits- und Sozialgericht vom 17. September 2019, GZ 9 Cga 126/18g-21, aus Anlass der Berufung der beklagten Partei hinsichtlich der Rückforderung einer Zahlung als nichtig aufgehoben und die Klage zurückgewiesen wurde und über Berufung der beklagen Partei hinsichtlich des Anspruchs nach dem OrgHG abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird teilweise Folge gegeben und der angefochtene Beschluss des Berufungsgerichts ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `Andrea Wiggering` (person)
- `Cassandra Noldens` (person)

**Example 30** (doc_id: `deanon_TRAIN/9ObA96_13b`) (sent_id: `deanon_TRAIN/9ObA96_13b_4`)


Brigitte Augustin und Mag. Andreas Hach als weitere Richter in der Arbeitsrechtssache der klagenden Partei DI Anita Crämer, vertreten durch Dr. Gerhard Hiebler und Dr. Gerd Grebenjak, Rechtsanwälte in Leoben, gegen die beklagte Partei, GQG E‑Commerce Gesellschaft mbH, Franz-Cäsar-Weg 5, 4115 Gumpesberg, Österreich, vertreten durch Siemer-Siegel-Füreder & Partner, Rechtsanwälte in Wien, wegen Feststellung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 18. April 2013, GZ 6 Ra 18/13h-10, mit dem der Berufung der beklagten Partei gegen das Urteil des Landesgerichts Leoben als Arbeits- und Sozialgericht vom 7. November 2012, GZ 23 Cga 115/12x-6, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht` | `Arbeits- und Sozialgericht` |

**Missed by this rule (FN):**

- `DI Anita Crämer` (person)
- `GQG E‑Commerce Gesellschaft mbH` (organisation)
- `Franz-Cäsar-Weg 5, 4115 Gumpesberg, Österreich` (address)

</details>

---

## `Court with Location`

**F1:** 0.050 | **Precision:** 1.000 | **Recall:** 0.026  

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
| 1.000 | 0.026 | 0.050 | 18 | 18 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 18 | 0 | 593 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob23_18g`) (sent_id: `deanon_TRAIN/10Ob23_18g_100`)


Die nach den Vorgaben des Verfassungsgerichtshofs gebotene steuerliche Entlastung des Geldunterhaltspflichtigen basiert auf dem Modell der getrennten Haushaltsführung (vgl RIS-Justiz RS0117015), in dem ein Elternteil seine Unterhaltspflicht durch Betreuungsleistungen und der andere durch Geldleistungen (allenfalls kombiniert mit anzurechnenden Naturalleistungen) erfüllt.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |

**Example 1** (doc_id: `deanon_TRAIN/3Ob26_23d`) (sent_id: `deanon_TRAIN/3Ob26_23d_48`)


Die Klägerin führt dagegen ins Treffen, dass die beschlussmäßige Umwidmung eines Grundstücks nach der Rechtsprechung des Verfassungsgerichtshofs erst dann erfolgen könne, wenn die Gemeinde bereits Eigentümerin des betroffenen Grundstücks sei; nur wenn es sich beim Grundstück um eine Privatstraße gehandelt hätte, die über Antrag des Eigentümers umgewidmet werden sollte, wäre eine Beschlussfassung nach § 27 Abs 2 Sbg LStG 1966 durch die Gemeinde vor Eigentumserwerb möglich gewesen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |

**Example 2** (doc_id: `deanon_TRAIN/3Ob26_23d`) (sent_id: `deanon_TRAIN/3Ob26_23d_51`)


Der von der Klägerin in diesem Zusammenhang zitierten Entscheidung des Verfassungsgerichtshofs vom 27. September 2003, V 108/01, lag nämlich der Sachverhalt zugrunde, dass der dort streitgegenständliche (Verbindungs-)Weg im Zeitpunkt der (vor der Enteignung des Grundstücks erfolgten) Widmung als Gemeindestraße schon seit Jahren als Privatstraße diente.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |

**Example 3** (doc_id: `deanon_TRAIN/3Ob26_23d`) (sent_id: `deanon_TRAIN/3Ob26_23d_52`)


Vor diesem Hintergrund sprach der Verfassungsgerichtshof aus, dass durch die Öffentlicherklärung einesin der Natur schon bestehendenWeges durch Verordnung mangels Eigentumserwerbs in gesetzwidriger Weise Gemeingebrauch begründet werde.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 4** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_67`)


In den vonRohregger(aaO) zitierten Entscheidungen bejahen auch der Verfassungsgerichtshof (B 1050/09) und der Verwaltungsgerichtshof (AW 2012/01/0032) die Bedeutung des § 10 RAO und der Vorgängerbestimmung des § 10 RL-BA 2015 für das öffentliche Interesse an dem Verbot der Doppelvertretung, weil es dem Schutz der durch einen Rechtsanwalt vertretenen Parteien diene, seine Einhaltung für das zwischen Rechtsanwalt und Klient bestehende Treueverhältnis für wesentlich erachtet werde und für das allgemeine Bild der Anwaltschaft in der Öffentlichkeit von Bedeutung sei.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 5** (doc_id: `deanon_TRAIN/5Ob31_16v`) (sent_id: `deanon_TRAIN/5Ob31_16v_15`)


Weiters wolle die Rechtssache gemäß Art 89 B-VG dem Verfassungsgerichtshof sowie gemäß Art 267 AEUV dem Europäischen Gerichtshof zur Prüfung vorgelegt werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 6** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_14`)


Der gesatzte Kollektivvertrag des Roten Kreuzes sei unanwendbar, da der Verwaltungsgerichtshof mit Erkenntnis vom 4. 9. 2013, 2011/08/0230 dem Österreichischen Roten Kreuz die Kollektivvertragsfähigkeit „de facto“ aberkannt habe, sodass die Verordnung des Bundeseinigungsamtes „rechtswidrig und ungültig“ sei.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 7** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_28`)


3. Der Verwaltungsgerichtshof hat mit seinem Erkenntnis vom 4. 9. 2013, 2011/08/0230 = DRdA 2014/27 (Felten) = ZAS 2014/13 (Tomandl) dem Österreichischen Roten Kreuz die Kollektivvertragsfähigkeit gemäß § 5 Abs 3 ArbVG nicht aberkannt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 8** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_29`)


Der Verwaltungsgerichtshof behob allein einen Bescheid, mit dem ein Antrag auf eine solche Aberkennung abgewiesen wurde, wegen Rechtswidrigkeit seines Inhalts (worauf auch der von der Beklagten angerufene Verfassungsgerichtshof in Punkt 2.4.5.3 seines Erkenntnisses ausdrücklich hinwies).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 9** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_30`)


Weil in der Folge abermals ein abweisender Bescheid erging, der sodann in Rechtskraft erwuchs (siehe erneut in Punkt 2.4.5.3 des VfGH-Erkenntnisses), ist es letzten Endes auch unrichtig, dass der Verwaltungsgerichtshof dem Roten Kreuz „de facto“ die Kollektivvertragsfähigkeit aberkannt hätte.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 10** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_31`)


Von dieser Sachlage ausgehend wies der von der Beklagten in diesem Verfahren mittels eines Parteiantrags auf Normenkontrolle angerufene Verfassungsgerichtshof den Antrag, die in BGBl II 2013/120 kundgemachte Verordnung des Bundeseinigungsamtes zur Gänze als verfassungswidrig aufzuheben, mit der Begründung ab, die Bedenken der Beklagten beruhten auf der nicht zutreffenden Prämisse, das Österreichische Rote Kreuz habe seine Kollektivvertragsfähigkeit durch das Erkenntnis des Verwaltungsgerichtshofs 2011/08/0230 „de facto“ verloren (Punkt 2.5 des Erkenntnisses).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Example 11** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_33`)


4. Die Frage, ob auch ohne Aufhebung der Verordnung BGBl II 2013/120 durch den Verfassungsgerichtshof allein dadurch, dass dem Österreichischen Roten Kreuz die Kollektivvertragsfähigkeit vom Bundeseinigungsamt mittels Bescheids aberkannt wird, die Satzung des Kollektivvertrags ihre Geltung verliert (vgl insbFriedrich, ASoK 2013, 460 f), stellt sich nicht, weil kein solcher Bescheid vorliegt.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 12** (doc_id: `deanon_TRAIN/8ObA72_19z`) (sent_id: `deanon_TRAIN/8ObA72_19z_12`)


2. Dabei konnte sich der Oberste Gerichtshof auf einschlägige Judikatur sowohl des Verfassungsgerichtshofs als auch des EuGH stützen: 2.1 Der Verfassungsgerichtshof hat in seinem Erkenntnis G 450/2015 ua Parteianträge von ÖBB-Bediensteten (unter anderem auch des Klägers) abgewiesen, die § 53a und § 56 Abs 18 bis 24 BundesbahnG je idF BGBl I Nr 64/2015 als verfassungswidrig aufzuheben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 13** (doc_id: `deanon_TRAIN/9ObA27_15h`) (sent_id: `deanon_TRAIN/9ObA27_15h_7`)


Ihr Antrag auf Gesetzesprüfung hinsichtlich der inzwischen aufgelösten Berufungskommission und eine Eventualbeschwerde seien beim Verfassungsgerichtshof anhängig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

</details>

---

## `Generic GmbH Entity`

**F1:** 0.050 | **Precision:** 0.145 | **Recall:** 0.030  

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
| 0.145 | 0.030 | 0.050 | 145 | 21 | 124 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 21 | 124 | 676 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_6`)


Die Aktiengesellschaft habe damit geworben, mit den eingezahlten Beträgen Edelmetalle zu marktüblichen Preisen zu erwerben, zu lagern und zu verwalten und habe dem Beklagten in dessen Funktion als Rechtsanwalt und öffentlicher Notar den Auftrag erteilt, jährliche Prüfberichte über den vollständigen Bestand zu erstellen.

| Predicted | Gold |
|---|---|
| `Die Aktiengesellschaft` | `Die Aktiengesellschaft` |

**Example 1** (doc_id: `deanon_TRAIN/10Ob23_15b`) (sent_id: `deanon_TRAIN/10Ob23_15b_4`)


Steintra Solar GmbH, Kospachstraße 35, 3162 Rainfeld, Österreich, vertreten durch Dr. Paul Vavrovsky und Mag. Christian Schrott, Rechtsanwälte in Salzburg, 2. Umwelt Dorfwald ges.m.b.H., Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich, vertreten durch Dr. Katharina Sedlazeck-Gschaider, Rechtsanwältin in Salzburg, wegen 11.921,56 EUR sA und Feststellung (Streitwert 5.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 27. Jänner 2015, GZ 11 R 14/14d-34, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Steintra Solar GmbH` | `Steintra Solar GmbH` |

**Missed by this rule (FN):**

- `Kospachstraße 35, 3162 Rainfeld, Österreich` (address)
- `Umwelt Dorfwald ges.m.b.H.` (organisation)
- `Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich` (address)

**Example 2** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_5`)


Maschinenbau Heimfurtcon GmbH, Fretzschner Medien, 2.

| Predicted | Gold |
|---|---|
| `Maschinenbau Heimfurtcon GmbH` | `Maschinenbau Heimfurtcon GmbH` |

**Missed by this rule (FN):**

- `Fretzschner Medien` (organisation)

**Example 3** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_6`)


OberTratraSoftware Dienstleistungen AG, Prägrader Weg 43, 8616 Gasen, Österreich, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung (5.000 EUR) und 11.561,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2019, GZ 2 R 140/19z-30, mit dem das Urteil des Landesgerichts Wels vom 22. Juli 2019, GZ 26 Cg 66/18m-26, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

| Predicted | Gold |
|---|---|
| `OberTratraSoftware Dienstleistungen AG` | `OberTratraSoftware Dienstleistungen AG` |

**Missed by this rule (FN):**

- `Prägrader Weg 43, 8616 Gasen, Österreich` (address)

**Example 4** (doc_id: `deanon_TRAIN/2Ob159_18y`) (sent_id: `deanon_TRAIN/2Ob159_18y_11`)


Er selbst war ua als Fenstermonteur in der GmbH tätig.

| Predicted | Gold |
|---|---|
| `Er selbst war ua als Fenstermonteur in der GmbH` | `Er selbst war ua als Fenstermonteur in der GmbH` |

**Example 5** (doc_id: `deanon_TRAIN/2Ob63_11w`) (sent_id: `deanon_TRAIN/2Ob63_11w_4`)


Holz Seewald AG, Kaiserbrunnengasse 6, 5122 Lindach, Österreich, beide vertreten durch Dr. Leopold Hirsch, Rechtsanwalt in Salzburg, wegen 38.967,48 EUR sA und Feststellung (Streitinteresse 20.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 10. Februar 2011, GZ 4 R 206/10g-29, womit das Urteil des Landesgerichts Salzburg vom 17. August 2010, GZ 7 Cg 49/09f-25, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Holz Seewald AG` | `Holz Seewald AG` |

**Missed by this rule (FN):**

- `Kaiserbrunnengasse 6, 5122 Lindach, Österreich` (address)

**Example 6** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_62`)


Dabei wiesen die anwesenden Mitarbeiter der GmbH darauf hin, dass dieses Unternehmen Ansprechpartner für Serviceleistungen ist.

| Predicted | Gold |
|---|---|
| `Dabei wiesen die anwesenden Mitarbeiter der GmbH` | `Dabei wiesen die anwesenden Mitarbeiter der GmbH` |

**Example 7** (doc_id: `deanon_TRAIN/2Ob99_18z`) (sent_id: `deanon_TRAIN/2Ob99_18z_4`)


Oßmer KI GmbH, Dr.H.Pirchegger-Weg 23, 4154 Lengau, Österreich, vertreten durch Mag. Martina Hackl, Rechtsanwältin in Mödling, und 3. Pistor Pflege GmbH, Maierlweg 58, 4776 Kobledt, Österreich, vertreten durch Dr. Klaus Rainer, Rechtsanwalt in Graz, wegen 308.539,34 EUR sA und Feststellung (Streitwert 10.000 EUR), über die außerordentliche Revision der klagenden Partei (Revisionsinteresse 92.942,15 EUR) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. März 2018, GZ 1 R 140/17s-101, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oßmer KI GmbH` | `Oßmer KI GmbH` |

**Missed by this rule (FN):**

- `Dr.H.Pirchegger-Weg 23, 4154 Lengau, Österreich` (address)
- `Pistor Pflege GmbH` (organisation)
- `Maierlweg 58, 4776 Kobledt, Österreich` (address)

**Example 8** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_6`)


JQV Finanzen Gruppe GmbH, Innovationsplatz 79, 9751 Nigglai, Österreich, beide vertreten durch Ruggenthaler Rechtsanwalts KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 62.000 EUR) über den außerordentlichen Revisionsrekurs der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Wien vom 20. September 2010, GZ 30 R 29/10w-9, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `JQV Finanzen Gruppe GmbH` | `JQV Finanzen Gruppe GmbH` |

**Missed by this rule (FN):**

- `Innovationsplatz 79, 9751 Nigglai, Österreich` (address)

**Example 9** (doc_id: `deanon_TRAIN/4Ob98_20w`) (sent_id: `deanon_TRAIN/4Ob98_20w_5`)


Malkmuß Marine GmbH, Fettinger-Gasse 7, 4615 Niederprisching, Österreich, vertreten durch MMag.

| Predicted | Gold |
|---|---|
| `Malkmuß Marine GmbH` | `Malkmuß Marine GmbH` |

**Missed by this rule (FN):**

- `Fettinger-Gasse 7, 4615 Niederprisching, Österreich` (address)

**Example 10** (doc_id: `deanon_TRAIN/4Ob98_20w`) (sent_id: `deanon_TRAIN/4Ob98_20w_7`)


Roedel Textil GmbH, Hasledt 4, 9634 Bodenmühl, Österreich, vertreten durch Mag. Wolfgang Weilguni, Rechtsanwalt in Wien, wegen 1.028.146,05 EUR sA und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der Klägerin gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 21. April 2020, GZ 5 R 158/19w-116, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Roedel Textil GmbH` | `Roedel Textil GmbH` |

**Missed by this rule (FN):**

- `Hasledt 4, 9634 Bodenmühl, Österreich` (address)

**Example 11** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_80`)


Wird eine GmbH durch einen Dritten geschädigt, ist der dem Gesellschafter dadurch entstehende Nachteil in seinem Vermögen ein nicht ersatzfähiger mittelbarer Schaden.

| Predicted | Gold |
|---|---|
| `Wird eine GmbH` | `Wird eine GmbH` |

**Example 12** (doc_id: `deanon_TRAIN/6Ob118_16w`) (sent_id: `deanon_TRAIN/6Ob118_16w_4`)


SeeAlheimsudMedien Institut GmbH in Liquidation, LNMT Cloud, 2. WEA Robotik GmbH, Selpritscher Weg 52, 4951 Polling im Innkreis, Österreich, Deutschland, beide vertreten durch Wess Kispert Rechtsanwalts GmbH in Wien, wegen 103.578,16 EUR sA und Feststellung, über die Rekurse der beklagten Partei und der Nebenintervenienten gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 13. April 2016, GZ 14 R 173/16m-39, womit das Urteil des Landesgerichts Eisenstadt vom 31. August 2015, GZ 3 Cg 166/13y-34, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Den Rekursen wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `SeeAlheimsudMedien Institut GmbH` | `SeeAlheimsudMedien Institut GmbH` |

**Missed by this rule (FN):**

- `LNMT Cloud` (organisation)
- `WEA Robotik GmbH` (organisation)
- `Selpritscher Weg 52, 4951 Polling im Innkreis, Österreich` (address)

**Example 13** (doc_id: `deanon_TRAIN/6Ob16_20a`) (sent_id: `deanon_TRAIN/6Ob16_20a_52`)


Aus der Unternehmereigenschaft der GmbH kraft Rechtsform (§ 2 UGB) könne nicht geschlossen werden, dass die GmbH auch ein Unternehmen betreibe.

| Predicted | Gold |
|---|---|
| `Aus der Unternehmereigenschaft der GmbH` | `Aus der Unternehmereigenschaft der GmbH` |

**Example 14** (doc_id: `deanon_TRAIN/6Ob174_20m`) (sent_id: `deanon_TRAIN/6Ob174_20m_5`)


Holzfuß Garten GmbH, Kindlehen 4, 4211 Kottingersdorf, Österreich, vertreten durch Dr. Hans-Peter Neher, Rechtsanwalt in Bad Ischl, wegen Räumung, Unterlassung und Duldung, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Wels als Berufungsgericht vom 5. Juni 2020, GZ 22 R 109/20s-25, mit dem das Urteil des Bezirksgerichts Bad Ischl vom 29. Jänner 2020, GZ 12 C 27/19y-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Holzfuß Garten GmbH` | `Holzfuß Garten GmbH` |

**Missed by this rule (FN):**

- `Kindlehen 4, 4211 Kottingersdorf, Österreich` (address)

**Example 15** (doc_id: `deanon_TRAIN/6Ob18_20w`) (sent_id: `deanon_TRAIN/6Ob18_20w_6`)


Die GmbH war Eigentümerin einer Liegenschaft, der Beklagte ist Eigentümer der Nachbarliegenschaft.

| Predicted | Gold |
|---|---|
| `Die GmbH` | `Die GmbH` |

**Example 16** (doc_id: `deanon_TRAIN/6Ob18_20w`) (sent_id: `deanon_TRAIN/6Ob18_20w_12`)


Die GmbH wurde 2018 gemäß § 40 FBG wegen Vermögenslosigkeit im Firmenbuch gelöscht.

| Predicted | Gold |
|---|---|
| `Die GmbH` | `Die GmbH` |

**Example 17** (doc_id: `deanon_TRAIN/6Ob207_18m`) (sent_id: `deanon_TRAIN/6Ob207_18m_4`)


Balnuweit Technik GmbH, sowie 2. Ost Werkmon GmbH, alle Am Waidfeld 8, 5211 Gstöckat, Österreich, alle vertreten durch Dr. Peter Zöchbauer, Rechtsanwalt in Wien, wegen (zuletzt) Widerrufs, Veröffentlichung und Zahlung von 9.000 EUR, über die Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 30. Mai 2018, GZ 5 R 39/18v-27, womit über Berufung der beklagten Parteien das Urteil des Handelsgerichts Wien vom 24. Jänner 2018, GZ 39 Cg 26/17t-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Balnuweit Technik GmbH` | `Balnuweit Technik GmbH` |

**Missed by this rule (FN):**

- `Ost Werkmon GmbH` (organisation)
- `Am Waidfeld 8, 5211 Gstöckat, Österreich` (address)

**Example 18** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_31`)


Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG wäre hinsichtlich § 14 Abs 3 FBG sachlich nicht gerechtfertigt.

| Predicted | Gold |
|---|---|
| `Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG` | `Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob18_13i`) (sent_id: `deanon_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Monsud-Textil GmbH, VetR Herbert Dedert, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Textil GmbH` — partial — pred is substring of gold: `Monsud-Textil GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Monsud-Textil GmbH`(organisation)
- `VetR Herbert Dedert`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob29_25z`) (sent_id: `deanon_TRAIN/10Ob29_25z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hargassner als Vorsitzenden, den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier sowie die Hofrätin Dr. Wallner-Friedl in der Rechtssache der klagenden Partei Enns Werkdonver Holding GmbH, Mag.a DDr.in Lynn Rothwein, vertreten durch die Wallner Jorthan Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Prausewetter Umwelt AG, Valerius Gensmantel, vertreten durch die Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 25.380 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 13. Jänner 2025, GZ 12 R 40/24z-55, mit dem der Berufung der klagenden Partei nicht, hingegen jener der beklagten Partei gegen das Urteil des Landesgerichts Salzburg vom 25. Oktober 2024, GZ 14 Cg 35/22t-49, Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Friedl in der Rechtssache der klagenden Partei Enns Werkdonver Holding GmbH` — partial — gold is substring of pred: `Enns Werkdonver Holding GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Enns Werkdonver Holding GmbH`(organisation)
- `Mag.a DDr.in Lynn Rothwein`(person)
- `Prausewetter Umwelt AG`(organisation)
- `Valerius Gensmantel`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt, aus denen Erträge erzielt werden sollen.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — partial — gold is substring of pred: `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`(organisation)

**Example 3** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_7`)


Der Fonds wurde von einer in Deutschland ansässigen AG aufgelegt.

**False Positives:**

- `Der Fonds wurde von einer in Deutschland ansässigen AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_34`)


10. 2019 zu einem völlig gleichgelagerten Fall zu der vom Berufungsgericht angesprochenen Rechtsfrage Stellung genommen hat (beklagte Partei ist hier wie dort die Derber GmbH in Liqu).

**False Positives:**

- `beklagte Partei ist hier wie dort die Derber GmbH` — partial — gold is substring of pred: `Derber GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Derber GmbH`(organisation)

**Example 5** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Daniel Wiegand, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei West-Medien Manufaktur GmbH in Liqu, Kanzelweg 32, 4850 Oberthalheim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Medien Manufaktur GmbH` — partial — pred is substring of gold: `West-Medien Manufaktur GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DI Daniel Wiegand`(person)
- `West-Medien Manufaktur GmbH`(organisation)
- `Kanzelweg 32, 4850 Oberthalheim, Österreich`(address)
- `Eckert Rechtsanwalts GmbH`(organisation)

**Example 6** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_5`)


Text Begründung: Der Kläger erwarb als Verbraucher im Juni 2003 über Vermittlung eines selbständigen Vermögensberaters Kommanditanteile an der Bestelmeyer+Keßelheim Software GmbH & Co KG im Nominale von 17.000 EUR zuzüglich 850 EUR Agio.

**False Positives:**

- `Keßelheim Software GmbH & Co KG` — positional overlap with gold: `Bestelmeyer+Keßelheim Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bestelmeyer+Keßelheim Software GmbH`(organisation)

**Example 7** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — partial — gold is substring of pred: `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`(organisation)

**Example 8** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_7`)


Der Fonds wurde von einer in Deutschland ansässigen Aktiengesellschaft aufgelegt.

**False Positives:**

- `Der Fonds wurde von einer in Deutschland ansässigen Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_6`)


Text Gründe: Mit dem angefochtenen Urteil wurden Bernhard Beinicke und Norbert Wentzlick von der wider sie erhobenen Anklage, sie hätten am 7. Februar 2009 in Churer Straße 54, 9064 St. Michael ob der Gurk, Österreich /Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der DKZ Solar GesmbH & Co KG, Susanne Schueßler, durch die Vorgabe, die HochForschung GmbH sei eine zahlungsfähige Leasingnehmerin, somit durch Täuschung über Tatsachen, zum Abschluss eines Leasingvertrags über ein Rennfahrzeug für die Dauer von 24 Monaten zu einem monatlichen Entgelt von 10.698,10 Euro, somit zu einer Handlung verleitet, welche die Stadt-Sanitär Services GesmbH & Co KG in einem 50.000 Euro übersteigenden Betrag von insgesamt 235.358,20 Euro am Vermögen schädigte, gemäß § 259 Z 3 StPO (verfehlt auch von der rechtlichen Kategorie; vglLendl, WK-StPO § 259 Rz 1) freigesprochen.

**False Positives:**

- `Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der DKZ Solar GesmbH & Co KG` — partial — gold is substring of pred: `DKZ Solar GesmbH`
- `Sanitär Services GesmbH & Co KG` — positional overlap with gold: `Stadt-Sanitär Services GesmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bernhard Beinicke`(person)
- `Norbert Wentzlick`(person)
- `Churer Straße 54, 9064 St. Michael ob der Gurk, Österreich`(address)
- `DKZ Solar GesmbH`(organisation)
- `Susanne Schueßler`(person)
- `HochForschung GmbH`(organisation)
- `Stadt-Sanitär Services GesmbH`(organisation)

**Example 10** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_8`)


Nach den wesentlichen Feststellungen (US 3 bis 6) befand sich die See-Maschinenbau GmbH in der zweiten Jahreshälfte 2008 in erheblichen Zahlungsschwierigkeiten.

**False Positives:**

- `Maschinenbau GmbH` — partial — pred is substring of gold: `See-Maschinenbau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `See-Maschinenbau GmbH`(organisation)

**Example 11** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_11`)


„Nachdem“ es für die Wilken E‑Commerce GmbH notwendig geworden war, für die Aufnahme des Rennbetriebs 35.000 Euro in das Fahrzeug zu investieren, konnte aufgrund dessen schlechten Zustands kein Rennen erfolgreich beendet werden.

**False Positives:**

- `Commerce GmbH` — partial — pred is substring of gold: `Wilken E‑Commerce GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wilken E‑Commerce GmbH`(organisation)

**Example 12** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_23`)


Auch diesen Aspekt nimmt die Staatsanwaltschaft in der Rechtsrüge (Z 9 lit a) ausreichend in den Blick, indem sie auf - in Richtung der Erfüllung auch der objektiven Tatbestandsmerkmale der §§ 146, 147 Abs 3 StGB weisende - Beweisergebnisse zum vorliegenden Vertragsab-schluss trotz mangelnder finanzieller Ausstattung und Absicherung der Inn Dorfdersee GmbH hinweist.

**False Positives:**

- `schluss trotz mangelnder finanzieller Ausstattung und Absicherung der Inn Dorfdersee GmbH` — partial — gold is substring of pred: `Inn Dorfdersee GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Dorfdersee GmbH`(organisation)

**Example 13** (doc_id: `deanon_TRAIN/12Os107_11v`) (sent_id: `deanon_TRAIN/12Os107_11v_8`)


B./II./ am 13. November 2009 in Poysdorf als Zeugin in einem Ermittlungsverfahren nach der Strafprozessordnung vor der Kriminalpolizei bei ihrer förmlichen Vernehmung zur Sache falsch ausgesagt, indem sie wahrheitswidrig behauptete, die an sie bezahlten 22.800 Euro seien das Entgelt für LKW-Vermietungen an die Ost Lextal GmbH gewesen, wobei sie tatsächlich das Geld ausbezahlt bekam, ohne dafür an die genannte Gesellschaft eine Gegenleistung erbracht zu haben.

**False Positives:**

- `Vermietungen an die Ost Lextal GmbH` — partial — gold is substring of pred: `Ost Lextal GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ost Lextal GmbH`(organisation)

**Example 14** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__9`)


Text Gründe: Mit unbekämpft in Rechtskraft erwachsenen Urteilen des Bezirksgerichts Spittal an der Drau vom 22. Juni 2017, GZ 5 U 5/17f-26, wurden (I) Andreas Feiereisen des Vergehens der fahrlässigen Tötung nach § 80 Abs 1 StGB schuldig erkannt und hiefür zu einer Geldstrafe verurteilt sowie (II) die Werksynstein-Wind GmbH gemäß § 3 Abs 1 Z 2, Abs 2 VbVG für die vom Schuldspruch (I) erfasste Straftat ihres Entscheidungsträgers verantwortlich erklärt und über diese Gesellschaft eine Verbandsgeldbuße von 70 Tagessätzen zu je 50 Euro verhängt, die unter Bestimmung einer Probezeit von drei Jahren bedingt nachgesehen wurde.

**False Positives:**

- `Wind GmbH` — partial — pred is substring of gold: `Werksynstein-Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Feiereisen`(person)
- `Werksynstein-Wind GmbH`(organisation)

**Example 15** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__17`)


Indem das Bezirksgericht über die Jusepeitis&Niemöller Bildung GmbH eine (das Höchstmaß von somit 55 Tagessätzen übersteigende) Verbandsgeldbuße von 70 Tagessätzen verhängte, verletzte es § 4 Abs 3 VbVG).

**False Positives:**

- `Niemöller Bildung GmbH` — partial — pred is substring of gold: `Jusepeitis&Niemöller Bildung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jusepeitis&Niemöller Bildung GmbH`(organisation)

**Example 16** (doc_id: `deanon_TRAIN/15Os133_11i_15Os134_11m_`) (sent_id: `deanon_TRAIN/15Os133_11i_15Os134_11m__4`)


In der Medienrechtssache des Antragstellers Siegfried Kaierleber gegen die Antragsgegnerin MYPQ Versicherung Dienstleistungen GmbH wegen §§ 6 Abs 1, 8a Abs 6 MedienG, AZ 91 Hv 72/05g des Landesgerichts für Strafsachen Wien, verletzen die Beschlüsse dieses Gerichts vom 28. April 2009, GZ 91 Hv 72/05g-75, und des Oberlandesgerichts Wien als Beschwerdegericht vom 6. Juli 2009, AZ 18 Bs 218/09d, § 39 Abs 1 und § 56 Abs 1 (Art VI b Abs 1 in der Fassung BGBl I 2005/49) MedienG.

**False Positives:**

- `In der Medienrechtssache des Antragstellers Siegfried Kaierleber gegen die Antragsgegnerin MYPQ Versicherung Dienstleistungen GmbH` — partial — gold is substring of pred: `Kaierleber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kaierleber`(person)
- `MYPQ Versicherung Dienstleistungen GmbH`(organisation)

**Example 17** (doc_id: `deanon_TRAIN/17Ob10_20z`) (sent_id: `deanon_TRAIN/17Ob10_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätinnen Mag. Malesich und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Levi Adelwart, vertreten durch Stephan Briem Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Dr. Penelope Piephans als Treuhänder der Insolvenzgläubiger der Valkraftfen-Analyse Aktiengesellschaft, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH in Linz, wegen Feststellung (Streitwert 18.335,66 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. März 2020, GZ 1 R 31/20i-13, womit das Urteil des Landesgerichts Linz vom 9. Dezember 2019, GZ 4 Cg 73/18z-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Analyse Aktiengesellschaft` — partial — pred is substring of gold: `Valkraftfen-Analyse Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Levi Adelwart`(person)
- `Dr. Penelope Piephans`(person)
- `Valkraftfen-Analyse Aktiengesellschaft`(organisation)

**Example 18** (doc_id: `deanon_TRAIN/18ONc1_21y`) (sent_id: `deanon_TRAIN/18ONc1_21y_3`)


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

**Example 19** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Herbes&Vißers Heizung GmbH, Waldemar Lokämper, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Traun-Luftfahrt GmbH, VetR DDr. Walter Stuehrmann, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

**False Positives:**

- `Vißers Heizung GmbH` — partial — pred is substring of gold: `Herbes&Vißers Heizung GmbH`
- `Luftfahrt GmbH` — partial — pred is substring of gold: `Traun-Luftfahrt GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Wiener Neustadt`(organisation)
- `Herbes&Vißers Heizung GmbH`(organisation)
- `Waldemar Lokämper`(person)
- `Traun-Luftfahrt GmbH`(organisation)
- `VetR DDr. Walter Stuehrmann`(person)
- `Landesgericht Feldkirch`(organisation)

**Example 20** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_4`)


Republik Österreich, vertreten durch die Finanzprokuratur in Wien, 2. Dr. Ralph Kreidenweiß, und 3. Donau-Automotive GmbH, Ebersreith 11, 8761 Götzendorf, Österreich, beide vertreten durch Dr. Hubert Simon, Rechtsanwalt in Wien, wegen Leistung und Feststellung, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. April 2014, GZ 7 R 21/14h-7, mit dem der Beschluss des Landesgerichts Leoben vom 30. Jänner 2014, GZ 2 Nc 2/14y-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Automotive GmbH` — partial — pred is substring of gold: `Donau-Automotive GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Ralph Kreidenweiß`(person)
- `Donau-Automotive GmbH`(organisation)
- `Ebersreith 11, 8761 Götzendorf, Österreich`(address)

**Example 21** (doc_id: `deanon_TRAIN/1Ob140_14s`) (sent_id: `deanon_TRAIN/1Ob140_14s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer und Mag. Dr. Wurdinger sowie die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft, Meidlinger Hauptstraße 19, 5233 Erlach, Österreich, vertreten durch die Walch & Zehetbauer Rechtsanwälte OG, Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 344.011,19 EUR und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Juni 2014, GZ 4 R 202/13g-54, mit dem das Teilzwischenurteil des Landesgerichts Feldkirch vom 2. August 2013, GZ 8 Cg 143/11y-46, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

**False Positives:**

- `Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft` — partial — gold is substring of pred: `Tracondon Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tracondon Aktiengesellschaft`(organisation)
- `Meidlinger Hauptstraße 19, 5233 Erlach, Österreich`(address)

**Example 22** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Dr. Wurdinger als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Steger, Mag. Wessely-Kristöfel, Dr. Parzmayr und Dr. Pfurtscheller als weitere Richterinnen und Richter in der Rechtssache der klagenden Partei Bundeskammer für Arbeiter und Angestellte, Wien 4, Prinz-Eugen-Straße 20–22, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Alsynwald-Recycling AG, RgR Mag. Dr. Evelyn Steinkröger, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH in Wien, wegen Unterlassung und Urteilsveröffentlichung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. Juli 2024, GZ 2 R 77/24v-15, mit dem das Urteil des Handelsgerichts Wien vom 28. Februar 2024, GZ 57 Cg 36/23d-8, bestätigt wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Recycling AG` — partial — pred is substring of gold: `Alsynwald-Recycling AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alsynwald-Recycling AG`(organisation)
- `RgR Mag. Dr. Evelyn Steinkröger`(person)

**Example 23** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_116`)


Die Nieder Norber AG wird den Kunden in der Mitteilung auf die Änderungen hinweisen und darauf aufmerksam machen, dass sein Stillschweigen nach Ablauf der zwei Monate ab Zugang der Mitteilung durch das Unterlassen eines Widerspruchs in Schriftform als Zustimmung zu den Änderungen gilt.

**False Positives:**

- `Die Nieder Norber AG` — partial — gold is substring of pred: `Nieder Norber AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Norber AG`(organisation)

**Example 24** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_117`)


Außerdem wird die Valwalduni-Handel AG eine Gegenüberstellung über die von der Änderung betroffenen Bestimmungen sowie die vollständige Fassung der neuen Bedingungen auf ihrer Internetseite veröffentlichen und die Gegenüberstellung dem Kunden auf sein Verlangen zur Verfügung stellen;

**False Positives:**

- `Handel AG` — partial — pred is substring of gold: `Valwalduni-Handel AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Valwalduni-Handel AG`(organisation)

**Example 25** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_118`)


auch darauf wird die Landwerlin&Plumke Versand AG in derMitteilung hinweisen.

**False Positives:**

- `Plumke Versand AG` — partial — pred is substring of gold: `Landwerlin&Plumke Versand AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landwerlin&Plumke Versand AG`(organisation)

**Example 26** (doc_id: `deanon_TRAIN/1Ob182_17x`) (sent_id: `deanon_TRAIN/1Ob182_17x_25`)


Nach dem von den Vorinstanzen zugrunde gelegten Sachverhalt beabsichtigt der Antragsgegner einer zur Unternehmensgruppe der Familie gehörenden GmbH, an der er nur mehr einen Geschäftsanteil von 1 % hält, der aber mit weitreichenden Sonderrechten ausgestattet ist, und die einen dringenden Finanzierungsbedarf in Höhe von 3 Mio EUR hat, ein Privatdarlehen in dieser Höhe zu gewähren, dass er wiederum durch Aufnahme eines entsprechenden Bankkredits finanzieren will, von dem bereits 1 Mio EUR an den Antragsgegner und von diesem an die GmbH geflossen sind.

**False Positives:**

- `Nach dem von den Vorinstanzen zugrunde gelegten Sachverhalt beabsichtigt der Antragsgegner einer zur Unternehmensgruppe der Familie gehörenden GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_TRAIN/1Ob221_17g`) (sent_id: `deanon_TRAIN/1Ob221_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und Hofrätinnen Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Boothe u. Sandmeier IT GmbH (früher OberTelekom GmbH), Ewaldgasse 28, 4084 Mitterberg, Österreich, vormals vertreten durch Dr. Wolfgang Poleschinski, Rechtsanwalt in Hartberg, gegen die beklagte Partei Yelec Dangelmeier, vertreten durch die Dr. Farhad Paya Rechtsanwalt GmbH, Klagenfurt am Wörthersee, wegen 7.583,60 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 24. August 2017, GZ 1 R 127/17x-69, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 28. März 2017, GZ 16 C 1333/14i-65, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

**False Positives:**

- `früher OberTelekom GmbH` — partial — gold is substring of pred: `OberTelekom GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Boothe u. Sandmeier IT GmbH`(organisation)
- `OberTelekom GmbH`(organisation)
- `Ewaldgasse 28, 4084 Mitterberg, Österreich`(address)
- `Yelec Dangelmeier`(person)
- `Farhad Paya Rechtsanwalt GmbH`(organisation)

**Example 28** (doc_id: `deanon_TRAIN/1Ob26_20k`) (sent_id: `deanon_TRAIN/1Ob26_20k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Synsynfurt-Finanzen GmbH, Tanja Thielike, vertreten durch die Draxler Rexeis Sozietät von Rechtsanwälten OG, Graz, gegen die beklagte Partei Roberta Reumschüssel, Bakk. phil., vertreten durch Mag. Dr. Alfred Wansch, Rechtsanwalt in Wien, wegen Räumung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtsachen Wien als Berufungsgericht vom 13. November 2019, GZ 39 R 228/19x-70, mit dem das Urteil des Bezirksgerichts Hernals vom 30. April 2019, GZ 4 C 277/16f-64, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Finanzen GmbH` — partial — pred is substring of gold: `Synsynfurt-Finanzen GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synsynfurt-Finanzen GmbH`(organisation)
- `Tanja Thielike`(person)
- `Roberta Reumschüssel, Bakk. phil.`(person)

**Example 29** (doc_id: `deanon_TRAIN/1Ob38_21a`) (sent_id: `deanon_TRAIN/1Ob38_21a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei HR Janet Henken, vertreten durch die Greiml & Horwath Rechtsanwaltspartnerschaft, Graz, gegen die beklagte Partei Elvira Nossal, vertreten durch die Neger/Ulm Rechtsanwälte GmbH, Graz, wegen 6.720 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 3. Juni 2020, GZ 6 R 115/20f-20, mit dem das Urteil des Bezirksgerichts Deutschlandsberg vom 20. März 2020, GZ 11 C 55/19t-16, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Ulm Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `HR Janet Henken`(person)
- `Elvira Nossal`(person)

**Example 30** (doc_id: `deanon_TRAIN/1Ob9_22p`) (sent_id: `deanon_TRAIN/1Ob9_22p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. HR Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Parteien 1. Mag. Tosca Xyländer und 2. Mag. Heinrich Vlachojannis, vertreten durch die Koch Jilek Rechtsanwälte Partnerschaft, Bruck an der Mur, gegen die beklagte Partei Grüttemann E‑Commerce Aktiengesellschaft, Friedhof Döbling 165, 8401 Abtissendorf, Österreich, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH, Wien, wegen 40.358,88 EUR sA, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. November 2021, GZ 5 R 163/21h-43, mit dem das Urteil des Handelsgerichts Wien vom 31. August 2021, GZ 55 Cg 60/20i-36, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Commerce Aktiengesellschaft` — partial — pred is substring of gold: `Grüttemann E‑Commerce Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Tosca Xyländer`(person)
- `Mag. Heinrich Vlachojannis`(person)
- `Grüttemann E‑Commerce Aktiengesellschaft`(organisation)
- `Friedhof Döbling 165, 8401 Abtissendorf, Österreich`(address)

**Example 31** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_11`)


Denn die Beweisthemen (Geschäftsgrundlage der eingangs genannten Vereinbarung vom 11. Dezember 2012 mit der Süd-Immobilien AG; von derselben intendierte Verwertung der Liegenschaften in Draskovichgasse 12, 8240 Friedberg, Österreich durch Zwangsversteigerung ungeachtet eines allfälligen Abverkaufs von Liegenschaften in Steghof 15, 4891 Höhenwarth, Österreich ; Auftrag der Mandanten des Disziplinarbeschuldigten zur Zurückziehung des Antrags auf Aufhebung der Höfeeigenschaft;

**False Positives:**

- `Immobilien AG` — partial — pred is substring of gold: `Süd-Immobilien AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Süd-Immobilien AG`(organisation)
- `Draskovichgasse 12, 8240 Friedberg, Österreich`(address)
- `Steghof 15, 4891 Höhenwarth, Österreich`(address)

**Example 32** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_12`)


Unkenntnis des Disziplinarbeschuldigten von den Gründen der Daten Unizorstein AG für die beantragte Fortsetzung der Zwangsversteigerungsverfahren;

**False Positives:**

- `Unkenntnis des Disziplinarbeschuldigten von den Gründen der Daten Unizorstein AG` — partial — gold is substring of pred: `Daten Unizorstein AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Daten Unizorstein AG`(organisation)

**Example 33** (doc_id: `deanon_TRAIN/2Ob159_18y`) (sent_id: `deanon_TRAIN/2Ob159_18y_10`)


Der Kläger war Alleingesellschafter und -geschäftsführer einer GmbH, die sich mit Fenstermontage beschäftigte.

**False Positives:**

- `geschäftsführer einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_19`)


Die beklagte Partei brachte das Gerät nach der Rücknahme zur KI Lexglanzber GmbH, deren Geschäftsführer der Cousin des Geschäftsführers der beklagten Partei ist.

**False Positives:**

- `Die beklagte Partei brachte das Gerät nach der Rücknahme zur KI Lexglanzber GmbH` — partial — gold is substring of pred: `KI Lexglanzber GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KI Lexglanzber GmbH`(organisation)

**Example 35** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_25`)


Im Herbst 2012 habe sich ein Aufkleber der Ostvallem-Robotik GmbH vom Luftentfeuchter gelöst und ein Typenschild mit dem Baujahr 1986 freigelegt.

**False Positives:**

- `Robotik GmbH` — partial — pred is substring of gold: `Ostvallem-Robotik GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ostvallem-Robotik GmbH`(organisation)

**Example 36** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_61`)


Die beklagte Partei führte gemeinsam mit der LHS Lebensmittel Consulting GmbH eine Einschulungsveranstaltung für Heutrocknungsgeräte durch, an der auch der Kläger teilnahm.

**False Positives:**

- `Die beklagte Partei führte gemeinsam mit der LHS Lebensmittel Consulting GmbH` — partial — gold is substring of pred: `LHS Lebensmittel Consulting GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `LHS Lebensmittel Consulting GmbH`(organisation)

**Example 37** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_64`)


Der Kläger hat sich nie an die GmbH gewandt, um ein Service durchführen zu lassen.

**False Positives:**

- `Der Kläger hat sich nie an die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_78`)


Die Bachtri GmbH hat vor der Auslieferung des neu zusammengesetzten Geräts eine Druckprobe durchgeführt.

**False Positives:**

- `Die Bachtri GmbH` — partial — gold is substring of pred: `Bachtri GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bachtri GmbH`(organisation)

**Example 39** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_80`)


Die Maerklin und Steckelmann Software GmbH befüllte den neu zusammengesetzten Luftentfeuchter Anfang 2011 mit dem Kältemittel R22, dessen Verwendung seit 1. 1.

**False Positives:**

- `Die Maerklin und Steckelmann Software GmbH` — partial — gold is substring of pred: `Maerklin und Steckelmann Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maerklin und Steckelmann Software GmbH`(organisation)

**Example 40** (doc_id: `deanon_TRAIN/2Ob99_18z`) (sent_id: `deanon_TRAIN/2Ob99_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden, den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé sowie die Hofräte Dr. Nowotny und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Stadt-Textil GmbH & Co KG, Kreuzlandstraße 52, 9462 Kalchberg, Österreich, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Kazlowski + Röttjer Automotive GmbH, Clarissa Lenschau, vertreten durch Keschmann Rechtsanwalts-GmbH in Wien, sowie die Nebenintervenientinnen 1. Ost-Chemie GmbH, M.-Klieber-Gasse 22, 3611 Himberg, Österreich, vertreten durch Dr. Dirk Just, Rechtsanwalt in Wien, 2.

**False Positives:**

- `Textil GmbH & Co KG` — positional overlap with gold: `Stadt-Textil GmbH`
- `Chemie GmbH` — partial — pred is substring of gold: `Ost-Chemie GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stadt-Textil GmbH`(organisation)
- `Kreuzlandstraße 52, 9462 Kalchberg, Österreich`(address)
- `Kazlowski + Röttjer Automotive GmbH`(organisation)
- `Clarissa Lenschau`(person)
- `Ost-Chemie GmbH`(organisation)
- `M.-Klieber-Gasse 22, 3611 Himberg, Österreich`(address)

**Example 41** (doc_id: `deanon_TRAIN/3Nc19_22g`) (sent_id: `deanon_TRAIN/3Nc19_22g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek sowie den Hofrat Dr. Stefula als weitere Richter in der Ordinationssache der Antragstellerin Stadt-Robotik GmbH, Hum 65, 9241 Kantnig, Österreich, vertreten durch Specht & Partner Rechtsanwalt GmbH in Wien, gegen die Antragsgegnerin Ing. Verona Obersteiner, Russische Föderation, wegen § 355 EO, über den Ordinationsantrag der Antragstellerin, den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Robotik GmbH` — partial — pred is substring of gold: `Stadt-Robotik GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stadt-Robotik GmbH`(organisation)
- `Hum 65, 9241 Kantnig, Österreich`(address)
- `Partner Rechtsanwalt GmbH`(organisation)
- `Ing. Verona Obersteiner`(person)

**Example 42** (doc_id: `deanon_TRAIN/3Ob114_14g`) (sent_id: `deanon_TRAIN/3Ob114_14g_4`)


KzlR Hartmut Raffenberg KG und 2.

**False Positives:**

- `KzlR Hartmut Raffenberg KG` — partial — gold is substring of pred: `KzlR Hartmut Raffenberg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KzlR Hartmut Raffenberg`(person)

**Example 43** (doc_id: `deanon_TRAIN/3Ob114_14g`) (sent_id: `deanon_TRAIN/3Ob114_14g_6`)


Begründung:  Rechtliche Beurteilung Die Erstklägerin (eine Rechtsanwalts KG), der Zweitkläger (deren Komplementär) und die Mutter des Zweitklägers (in Hinkunft: Pensionsberechtigte) führten als Kläger und Widerbeklagte ein Schiedsverfahren gegen den (hier) Beklagten (als ausgeschiedenen Komplementär) als Beklagten und Widerkläger, das mit einem Schiedsspruch vom 2. Mai 2011 endete.

**False Positives:**

- `eine Rechtsanwalts KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_TRAIN/3Ob114_14g`) (sent_id: `deanon_TRAIN/3Ob114_14g_58`)


8.Die Vorinstanzen legten nicht die Bilanzen einer Rechtsanwälte GmbH als Bemessungsgrundlage zugrunde, sondern die Gewinnanteile des Beklagten an dieser Rechtsanwälte GmbH; zu einer allfälligen Minderung dieses Einkommens des Beklagten wurde eine Negativfeststellung getroffen, die zu seinen Lasten geht.

**False Positives:**

- `Die Vorinstanzen legten nicht die Bilanzen einer Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_TRAIN/3Ob248_10g`) (sent_id: `deanon_TRAIN/3Ob248_10g_5`)


Text Begründung: Der nunmehrige Oppositionsbeklagte Ronja Crux hatte im Jahr 2005 bei der nunmehrigen Oppositionsklägerin, der Synkraftal-Chemie GmbH, einen gebrauchten Pkw Porsche Carrera 4 gekauft.

**False Positives:**

- `Chemie GmbH` — partial — pred is substring of gold: `Synkraftal-Chemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ronja Crux`(person)
- `Synkraftal-Chemie GmbH`(organisation)

**Example 46** (doc_id: `deanon_TRAIN/3Ob44_20x`) (sent_id: `deanon_TRAIN/3Ob44_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie die Hofräte Priv.-Doz. Dr. Rassi und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Andreas Clösges, vertreten durch die Eger/Gründl Rechtsanwälte OG in Graz, gegen die beklagte Partei Chemie Valtri GmbH, Niels Niefeldt, vertreten durch Mag. Manuel Fähnrich, Rechtsanwalt in Graz, wegen 34.000 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 31. Jänner 2020, GZ 2 R 168/19x-28, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Gründl Rechtsanwälte OG` — partial — pred is substring of gold: `Eger/Gründl Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Andreas Clösges`(person)
- `Eger/Gründl Rechtsanwälte OG`(organisation)
- `Chemie Valtri GmbH`(organisation)
- `Niels Niefeldt`(person)

**Example 47** (doc_id: `deanon_TRAIN/4Fsc1_10z`) (sent_id: `deanon_TRAIN/4Fsc1_10z_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel und Dr. Jensik als weitere Richter in der Rechtssache der klagenden Partei Lexglanzfen-Garten AG, Pia Özbek, vertreten durch Dr. Hartmut Mayer, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Esra Waitkat, vertreten durch Mag. Gerhard Pilz, Rechtsanwalt, als Verfahrenshelfer, wegen 3.330,19 EUR sA (AZ 35 R 24/09b des Landesgerichts für Zivilrechtssachen Wien), zum Fristsetzungsantrag der beklagten Partei vom 28. Oktober 2009 an den Obersten Gerichtshof im Ablehnungsverfahren den Beschluss gefasst:  Spruch Der Fristsetzungsantrag wird zurückgewiesen.

**False Positives:**

- `Garten AG` — partial — pred is substring of gold: `Lexglanzfen-Garten AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lexglanzfen-Garten AG`(organisation)
- `Pia Özbek`(person)
- `Mag. Esra Waitkat`(person)

**Example 48** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_4`)


Logdercon-Digital, Dänemark, 2. Fengart GmbH, Oberer Weinweg 87, 9020 Klagenfurt, Österreich, beide vertreten durch Graf & Pitkowitz Rechtsanwälte GmbH in Wien, gegen die Beklagten 1. LGR Medien GmbH, OVX Finanzen, 2. Analyse Kelunizor AG, Fahnberg 42, 4100 Großamberg, Österreich, Deutschland, beide vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Gesamtstreitwert 69.500 EUR), über den Ordinationsantrag der Klägerinnen den Beschluss gefasst:  Spruch Dem Ordinationsantrag wird stattgegeben.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Logdercon-Digital`(organisation)
- `Fengart GmbH`(organisation)
- `Oberer Weinweg 87, 9020 Klagenfurt, Österreich`(address)
- `LGR Medien GmbH`(organisation)
- `OVX Finanzen`(organisation)
- `Analyse Kelunizor AG`(organisation)
- `Fahnberg 42, 4100 Großamberg, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)

**Example 49** (doc_id: `deanon_TRAIN/4Ob136_11w`) (sent_id: `deanon_TRAIN/4Ob136_11w_5`)


Lee Tinnemeyer, 2. Mag. Romana Weisbrodt, beide vertreten durch Mag. Ulrich Salburg, Rechtsanwalt in Wien, gegen die beklagte Partei Nexbach-Marine AG, StR Hon.-Prof.in Linda Tarak, vertreten durch Kunz Schima Wallentin Rechtsanwälte OEG in Wien, wegen 60.626,11 EUR sA, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. November 2011, GZ 1 R 242/10f-21, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Marine AG` — partial — pred is substring of gold: `Nexbach-Marine AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lee Tinnemeyer`(person)
- `Mag. Romana Weisbrodt`(person)
- `Nexbach-Marine AG`(organisation)
- `StR Hon.-Prof.in Linda Tarak`(person)

**Example 50** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei XDC Druck GmbH, Scarlett Augustus, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Wien, gegen die beklagte Partei UBER B.V., Larissa Ebele, Niederlande, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Unterlassung, Veröffentlichung und Feststellung (Streitwert im Sicherungsverfahren 70.000 EUR), über den Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 4. Juli 2018, GZ 3 R 32/18z-14, mit dem der Beschluss des Handelsgerichts Wien vom 24. April 2018, GZ 58 Cg 10/18f-6, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei XDC Druck GmbH` — partial — gold is substring of pred: `XDC Druck GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `XDC Druck GmbH`(organisation)
- `Scarlett Augustus`(person)
- `Larissa Ebele`(person)

**Example 51** (doc_id: `deanon_TRAIN/4Ob18_20f`) (sent_id: `deanon_TRAIN/4Ob18_20f_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Jörg Drathschmidt, vertreten durch Dr. Winfried Sattlegger und andere Rechtsanwälte in Linz, gegen die beklagte Partei Wien Dorfsud GmbH, Gerlinde Balcerzak, vertreten durch Dr. Helmut Trenkwalder, Rechtsanwalt in Linz, und die Nebenintervenientin auf Seiten der beklagten Partei Waldfen-Versand GmbH, Eva Boztas, vertreten durch Schneider & Schneider Rechtsanwalts GmbH in Wien, wegen 35.628,94 EUR sA Zug um Zug gegen Herausgabe eines Fahrzeugs, über den Rekurs der Nebenintervenientin gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht vom 7. November 2019, GZ 6 R 114/19f-41, mit dem das Urteil des Landesgerichts Linz vom 3. Juli 2019, GZ 36 Cg 4/17m-36, im klagsstattgebenden Teil (Spruchpunkt 1.) aufgehoben wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Versand GmbH` — partial — pred is substring of gold: `Waldfen-Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jörg Drathschmidt`(person)
- `Wien Dorfsud GmbH`(organisation)
- `Gerlinde Balcerzak`(person)
- `Waldfen-Versand GmbH`(organisation)
- `Eva Boztas`(person)
- `Schneider Rechtsanwalts GmbH`(organisation)

**Example 52** (doc_id: `deanon_TRAIN/4Ob194_22s`) (sent_id: `deanon_TRAIN/4Ob194_22s_4`)


Matzka und Dr. Annerl sowie die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Dueckers Wind GmbH, Corvin Cetinbag, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, gegen die beklagten Parteien 1. Wendy Goetzen (Verein), 2. Birkfeld+Münzenrieder Daten GmbH, beide Stegg 92, 3925 Neumelon, Österreich, vertreten durch Dr. Brigitte Birnbaum, Dr. Rainer Toperczer, Rechtsanwälte in Wien, wegen Unterlassung, Herausgabe, Feststellung und Urteilsveröffentlichung (Gesamtstreitwert 75.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Juli 2022, GZ 2 R 47/22d-41, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Münzenrieder Daten GmbH` — partial — pred is substring of gold: `Birkfeld+Münzenrieder Daten GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dueckers Wind GmbH`(organisation)
- `Corvin Cetinbag`(person)
- `Wendy Goetzen`(person)
- `Birkfeld+Münzenrieder Daten GmbH`(organisation)
- `Stegg 92, 3925 Neumelon, Österreich`(address)

**Example 53** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Kraftheimglanz-Versand GmbH, OStR Dipl.

**False Positives:**

- `Versand GmbH` — partial — pred is substring of gold: `Kraftheimglanz-Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kraftheimglanz-Versand GmbH`(organisation)

**Example 54** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_5`)


Klingenbeil Versand GmbH & Co KG, 2.

**False Positives:**

- `Klingenbeil Versand GmbH & Co KG` — partial — gold is substring of pred: `Klingenbeil Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Klingenbeil Versand GmbH`(organisation)

**Example 55** (doc_id: `deanon_TRAIN/4Ob224_23d`) (sent_id: `deanon_TRAIN/4Ob224_23d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, den Hofrat Mag. Dr. Wurdinger und die Hofrätin Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Verlexglanz-Marine GmbH, Andreas Häntsch, Deutschland, vertreten durch die Saxinger Chalupsky & Partner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Emma Bergner kammer, Cathleen Hofschulte, vertreten durch Dr. Friedrich Schulz, Rechtsanwalt in Wien, wegen Unterlassung, Widerruf und Veröffentlichung desselben (Gesamtstreitwert 46.200 EUR), aus Anlass der außerordentlichen Revisionen der klagenden und der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 23. Oktober 2023, GZ 4 R 99/23t-32, mit dem das Urteil des Handelsgerichts Wien vom 27. April 2023, GZ 57 Cg 34/21g-24, bestätigt wurde, den Beschluss gefasst:  Spruch Die gemeinsame Anzeige beider Parteien vom 27. August 2024 über das vereinbarte Ruhen des Verfahrens wird zur Kenntnis genommen.

**False Positives:**

- `Marine GmbH` — partial — pred is substring of gold: `Verlexglanz-Marine GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Verlexglanz-Marine GmbH`(organisation)
- `Andreas Häntsch`(person)
- `Emma Bergner`(person)
- `Cathleen Hofschulte`(person)

**Example 56** (doc_id: `deanon_TRAIN/4Ob69_14x`) (sent_id: `deanon_TRAIN/4Ob69_14x_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Univ.-Prof. Dr. Anita Christöphler, vertreten durch Riesemann Rechtsanwalts GmbH in Graz, gegen die beklagte Partei Husein E‑Commerce GmbH, Dolores Linse, Deutschland, vertreten durch Dr. Peter Schlösser, Rechtsanwalt in Graz, wegen Unterlassung, Beseitigung, Urteilsveröffentlichung, Rechnungslegung und Zahlung (Streitwert im Sicherungsverfahren 50.000 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz vom 5. März 2014, GZ 5 R 20/14x-21, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Commerce GmbH` — partial — pred is substring of gold: `Husein E‑Commerce GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Anita Christöphler`(person)
- `Husein E‑Commerce GmbH`(organisation)
- `Dolores Linse`(person)

**Example 57** (doc_id: `deanon_TRAIN/4Ob9_20g`) (sent_id: `deanon_TRAIN/4Ob9_20g_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Ing. KzlR MedR Brunhild Syndikus, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1) Böhnstedt+Bittlmeier Verlag GmbH, Wien Traalmon Betriebe, und 2) TraunBau AG, Schneeballenweg 6, 4232 Penzendorf, Österreich, beide vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 11.091,23 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 6. November 2019, GZ 2 R 158/19x-27, mit dem das Urteil des Landesgerichts Linz vom 29. August 2019, GZ 36 Cg 14/18h-22, bestätigt wurde, den Beschluss gefasst:  Spruch I. Das Revisionsverfahren zu 4 Ob 9/20g wird bis zur Vorabentscheidung des Gerichtshofs der Europäischen Union über das Vorabentscheidungsersuchen des Obersten Gerichtshofs vom 17.

**False Positives:**

- `Bittlmeier Verlag GmbH` — partial — pred is substring of gold: `Böhnstedt+Bittlmeier Verlag GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. KzlR MedR Brunhild Syndikus`(person)
- `Böhnstedt+Bittlmeier Verlag GmbH`(organisation)
- `Wien Traalmon Betriebe`(organisation)
- `TraunBau AG`(organisation)
- `Schneeballenweg 6, 4232 Penzendorf, Österreich`(address)

**Example 58** (doc_id: `deanon_TRAIN/5Ob146_16f`) (sent_id: `deanon_TRAIN/5Ob146_16f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers Mag. Niels Mueter, vertreten durch Dr. Anke Reisch, Rechtsanwältin in Kitzbühel, gegen die Antragsgegnerin Talgart-Chemie GmbH & Co KG, Tiefe Gasse 5, 2061 Obritz, Österreich, vertreten durch Dr. Lisbeth Lass und Dr. Hans Christian Lass, Rechtsanwälte in Innsbruck, wegen § 52 Abs 1 Z 6 iVm § 20 Abs 3 WEG 2002, infolge des „außerordentlichen“ Revisionsrekurses des Antragstellers gegen den (richtig) Sachbeschluss des Landesgerichts Innsbruck vom 24. Mai 2016, GZ 4 R 128/16a-50, mit dem der Sachbeschluss des Bezirksgerichts Kitzbühel vom 14. März 2016, GZ 4 Msch 7/14x-36, abgeändert wurde, den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.

**False Positives:**

- `Chemie GmbH & Co KG` — positional overlap with gold: `Talgart-Chemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Niels Mueter`(person)
- `Talgart-Chemie GmbH`(organisation)
- `Tiefe Gasse 5, 2061 Obritz, Österreich`(address)

**Example 59** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_6`)


Die Klägerin ist (Minderheits-)Gesellschafterin einer GmbH.

**False Positives:**

- `Gesellschafterin einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_7`)


Sie begehrte die beklagte Rechtsanwaltsgesellschaft zu verpflichten, die Rechtsberatung und/oder Rechtsvertretung dieser GmbH in bestimmt bezeichneten Angelegenheiten zu unterlassen.

**False Positives:**

- `oder Rechtsvertretung dieser GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_8`)


Die Klägerin begehrte weiters die Feststellung der Haftung der Beklagten für alle Schäden und Nachteile der Klägerin aus oder in Zusammenhang mit der Rechtsberatung und/oder Rechtsvertretung dieser GmbH durch die Beklagte aus und in Zusammenhang mit diesen Angelegenheiten.

**False Positives:**

- `oder Rechtsvertretung dieser GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_31`)


Das mit der dritten im Klagebegehren genannten Angelegenheit angestrebte per se-Verbot der Vertretung der GmbH gegenüber Dritten könne außerdem mit einem Interessenkonflikt zwischen der Gesellschaft und dem Mehrheitsgesellschafter keinesfalls begründet werden.

**False Positives:**

- `Verbot der Vertretung der GmbH` — partial — pred is substring of gold: `Das mit der dritten im Klagebegehren genannten Angelegenheit angestrebte per se-Verbot der Vertretung der GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Das mit der dritten im Klagebegehren genannten Angelegenheit angestrebte per se-Verbot der Vertretung der GmbH`(organisation)

**Example 63** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_78`)


Das von der Klägerin gewünschte Auslegungsergebnis gerät zudem mit dem für die GmbH in § 61 Abs 1 und 2 GmbHG normierten Trennungsprinzip in Konflikt, das eine strikte Trennung zwischen Gesellschaft und Gesellschaftern und damit auch zwischen Gesellschaftsvermögen und Privatvermögen der Gesellschafter anordnet (1 Ob 81/18w).

**False Positives:**

- `Das von der Klägerin gewünschte Auslegungsergebnis gerät zudem mit dem für die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_TRAIN/5Ob206_24s`) (sent_id: `deanon_TRAIN/5Ob206_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Painsi, Dr. Weixelbraun-Mohr, Dr. Steger und Dr. Pfurtscheller als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers OMedR Louisa Dutzke, vertreten durch Mag. Wolfgang Doppelhofer LL.M. LL.M., Rechtsanwalt in Wien, gegen die Antragsgegnerin Alsud-Pflege GmbH, Kirchenwaldweg 10, 3104 St. Pölten, Österreich, vertreten durch Weishaupt Horak Georgiev Rechtsanwälte GmbH & Co KG in Wien, wegen Feststellung der Ausstattungskategorie nach § 15a MRG, über den Revisionsrekurs der Antragsgegnerin gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 26. August 2024, GZ 39 R 144/24a-22, mit dem der Sachbeschluss des Bezirksgerichts Hietzing vom 29. Mai 2024, GZ 9 MSch 18/23k-18, aufgehoben wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Pflege GmbH` — partial — pred is substring of gold: `Alsud-Pflege GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OMedR Louisa Dutzke`(person)
- `Alsud-Pflege GmbH`(organisation)
- `Kirchenwaldweg 10, 3104 St. Pölten, Österreich`(address)

**Example 65** (doc_id: `deanon_TRAIN/5Ob219_11h`) (sent_id: `deanon_TRAIN/5Ob219_11h_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden sowie die Hofrätinnen Dr. Hurch und Dr. Lovrek und die Hofräte Dr. Höllwerth und Mag. Wurzer als weitere Richter in der Rechtssache der klagenden Partei Ian James Möllenhoff, vertreten durch Dr. Michael Brandauer, Rechtsanwalt in Feldkirch, gegen die beklagte Partei Dorfbruckwil-Möbel GmbH, KzlR Dr. Erhard Goppelt, MSc, vertreten durch Dr. Gernot Hofstätter, Rechtsanwalt in Innsbruck, wegen 147.000 EUR sA und Feststellung (Streitwert 5.000 EUR), über den außerordentlichen Revisionsrekurs des Klägers gegen den Beschluss des Oberlandesgerichts Innsbruck als Rekursgericht vom 12. September 2011, GZ 4 R 166/11k-15, womit der Rekurs des Klägers gegen den Beschluss des Landesgerichts Innsbruck vom 20. Juni 2011, GZ 10 Cg 212/10g-8, zurückgewiesen wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Möbel GmbH` — partial — pred is substring of gold: `Dorfbruckwil-Möbel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Möllenhoff`(person)
- `Dorfbruckwil-Möbel GmbH`(organisation)
- `KzlR Dr. Erhard Goppelt, MSc`(person)

**Example 66** (doc_id: `deanon_TRAIN/5Ob31_16v`) (sent_id: `deanon_TRAIN/5Ob31_16v_4`)


Herta Riecken OG, Silvana Scheugenpflug, 2. DI Annemarie Autor, 3. Mag. Pawel Schemeitat, 4. MMag.

**False Positives:**

- `Herta Riecken OG` — partial — gold is substring of pred: `Herta Riecken`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Herta Riecken`(person)
- `Silvana Scheugenpflug`(person)
- `DI Annemarie Autor`(person)
- `Mag. Pawel Schemeitat`(person)

**Example 67** (doc_id: `deanon_TRAIN/5Ob48_22b`) (sent_id: `deanon_TRAIN/5Ob48_22b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer, Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Univ.-Prof. Dr. Ernestine Füssl, vertreten durch Dr. Klaus Plätzer, Rechtsanwalt in Salzburg, gegen die beklagte Partei Gümüs+Klaess Heizung GmbH, Edeltraud Ceschelski, vertreten durch Dr. Johannes Hebenstreit, Rechtsanwalt in Salzburg, wegen 6.971,22 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 16. Dezember 2021, GZ 53 R 200/21z-20, mit dem das Urteil des Bezirksgerichts Salzburg vom 16. August 2021, GZ 23 C 54/21d-12, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Klaess Heizung GmbH` — partial — pred is substring of gold: `Gümüs+Klaess Heizung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Ernestine Füssl`(person)
- `Gümüs+Klaess Heizung GmbH`(organisation)
- `Edeltraud Ceschelski`(person)

**Example 68** (doc_id: `deanon_TRAIN/5Ob84_16p`) (sent_id: `deanon_TRAIN/5Ob84_16p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der Rechtssache der klagenden Partei Dimitri Ringlstetter, vertreten durch Dr. Friedrich Gatscha, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. Heimaluni-Event GmbH, Vorderstraß 39, 3920 Harruck, Österreich, vertreten durch Mag. Gerhard Walzl, Rechtsanwalt in Wien, 2. IJWQ Digital Services GmbH, Dr.-Stephan-Krause-Gasse 73, 3244 Baulanden, Österreich, vertreten durch Mag. Alain Danner, Rechtsanwalt in Wien, 3. Dr. Amalia Brodke, vertreten durch Mag. Gerhard Walzl, Rechtsanwalt in Wien, wegen 1. Übertragung der Zusage auf Einräumung von Wohnungseigentum (30.000 EUR), 2. Einverleibung von Miteigentum (50.000 EUR), 3. Zahlung (122.785,01 EUR sA), 4. Feststellung (15.000 EUR), über die außerordentliche Revision der klagenden Partei (Revisionsinteresse 95.000 EUR) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. März 2016, GZ 34 R 152/15w-50, den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Event GmbH` — partial — pred is substring of gold: `Heimaluni-Event GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dimitri Ringlstetter`(person)
- `Heimaluni-Event GmbH`(organisation)
- `Vorderstraß 39, 3920 Harruck, Österreich`(address)
- `IJWQ Digital Services GmbH`(organisation)
- `Dr.-Stephan-Krause-Gasse 73, 3244 Baulanden, Österreich`(address)
- `Dr. Amalia Brodke`(person)

**Example 69** (doc_id: `deanon_TRAIN/6Ob123_19k`) (sent_id: `deanon_TRAIN/6Ob123_19k_10`)


Jedes dieser Unternehmen ist derzeit an das Fernwärmenetz der Fernwärme Wien GmbH angeschlossen.

**False Positives:**

- `Jedes dieser Unternehmen ist derzeit an das Fernwärmenetz der Fernwärme Wien GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_TRAIN/6Ob145_21y`) (sent_id: `deanon_TRAIN/6Ob145_21y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden, den Hofrat Dr. Nowotny, die Hofrätinnen Dr. Hofer-Zeni-Rennhofer und Dr. Faber und den Hofrat Mag. Pertmayr als weitere Richter in der Rechtssache der gefährdeten Partei Dipl.-Ing. Kirstin Iseler, MA Bakk. rer. nat., vertreten durch DORDA Rechtsanwälte GmbH in Wien, wider die Gegnerin der gefährdeten Partei Wilfried Pawell, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, über den Rekurs der gefährdeten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 26. Mai 2021, GZ 47 R 99/21p-19, womit aus Anlass des Rekurses der Gegnerin der gefährdeten Partei die einstweilige Verfügung des Bezirksgerichts Favoriten vom 3. April 2021, GZ 56 C 107/21m-2, als nichtig aufgehoben wurde, den Beschluss gefasst:  Spruch Dem Rekurs wirdFolge gegeben.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. Kirstin Iseler, MA Bakk. rer. nat.`(person)
- `Wilfried Pawell`(person)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)

**Example 71** (doc_id: `deanon_TRAIN/6Ob16_20a`) (sent_id: `deanon_TRAIN/6Ob16_20a_58`)


Überdies spreche die Bestimmung von der „Veräußerung eines Unternehmens“ und nicht von der „Veräußerung von Geschäftsanteilen an GmbH oder Aktien“.

**False Positives:**

- `Veräußerung von Geschäftsanteilen an GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_TRAIN/6Ob18_20w`) (sent_id: `deanon_TRAIN/6Ob18_20w_7`)


Der Beklagte ließ auf seine Kosten auf der Liegenschaft der GmbH eine Tiefgarage mit 15 Stellplätzen errichten.

**False Positives:**

- `Der Beklagte ließ auf seine Kosten auf der Liegenschaft der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_TRAIN/6Ob18_20w`) (sent_id: `deanon_TRAIN/6Ob18_20w_9`)


Im Zuge dieser Veräußerung vereinbarte der Beklagte mit der durch den Käufer als Geschäftsführer vertretenen GmbH, dass diese auf ihrer Liegenschaft dem Beklagten und seinen Rechtsnachfolgern im Eigentum der Nachbarliegenschaft unentgeltlich die Dienstbarkeiten der Benützung der unterirdischen Tiefgaragenplätze sowie des Gehens und Fahrens (zu den Stellplätzen) einräume.

**False Positives:**

- `Im Zuge dieser Veräußerung vereinbarte der Beklagte mit der durch den Käufer als Geschäftsführer vertretenen GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_TRAIN/6Ob18_20w`) (sent_id: `deanon_TRAIN/6Ob18_20w_10`)


Diese Dienstbarkeiten wurden im C-Blatt der Liegenschaft der GmbH verbüchert.

**False Positives:**

- `Blatt der Liegenschaft der GmbH` — partial — pred is substring of gold: `Diese Dienstbarkeiten wurden im C-Blatt der Liegenschaft der GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Diese Dienstbarkeiten wurden im C-Blatt der Liegenschaft der GmbH`(organisation)

**Example 75** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_15`)


[4] Zu FN FN110230q ist im Firmenbuch des Handelsgerichts Wien die Seetra-Recycling GmbH (in der Folge „Bauvereinigung“) mit einem Stammkapital von 6.033.342,30 EUR eingetragen.

**False Positives:**

- `Recycling GmbH` — partial — pred is substring of gold: `Seetra-Recycling GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FN110230q`(business_register_number)
- `Seetra-Recycling GmbH`(organisation)

**Example 76** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_29`)


diese sei eine gemeinnützige Bauvereinigung in der Rechtsform einer GmbH.

**False Positives:**

- `diese sei eine gemeinnützige Bauvereinigung in der Rechtsform einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_33`)


Diese Gesetzeslücke sei durch eine analoge Anwendung des § 14 Abs 3 FBG auf gemeinnützige Bauvereinigungen in sämtlichen möglichen Rechtsformen (also auch in der Rechtsform einer GmbH oder AG) anzuwenden.

**False Positives:**

- `also auch in der Rechtsform einer GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_66`)


Die Bestimmung sei daher analog auch auf gemeinnützige Bauvereinigungen in der Rechtsform der GmbH oder AG anzuwenden.

**False Positives:**

- `Die Bestimmung sei daher analog auch auf gemeinnützige Bauvereinigungen in der Rechtsform der GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_86`)


Auch bei Bauvereinigungen in der Rechtsform der Gesellschaft mit beschränkter Haftung oder der Aktiengesellschaft hat die Prüfung diesen Vorschriften zu entsprechen.

**False Positives:**

- `Auch bei Bauvereinigungen in der Rechtsform der Gesellschaft mit beschränkter Haftung oder der Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_107`)


Wenn nun kraft ausdrücklicher gesetzlicher Vorschrift gemeinnützige Bauvereinigungen auch in den Rechtsformen einer GmbH oder AG erlaubt sind (§ 1 Abs 1 WGG) und gleichzeitig auch für diese die Pflicht statuiert wird, einem Revisionsverband anzugehören (§ 5 Abs 1 WGG), so ist auch für eine in der Rechtsform einer GmbH oder AG bestehende Bauvereinigung der Revisionsverband als „zuständig“ im Sinn von § 14 Abs 3 FBG und demgemäß insoweit als Amtspartei anzusehen.

**False Positives:**

- `Wenn nun kraft ausdrücklicher gesetzlicher Vorschrift gemeinnützige Bauvereinigungen auch in den Rechtsformen einer GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Company Name Without Suffix`

**F1:** 0.045 | **Precision:** 0.086 | **Recall:** 0.030  

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
| 0.086 | 0.030 | 0.045 | 244 | 21 | 223 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 21 | 223 | 676 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_6`)


Die Aktiengesellschaft habe damit geworben, mit den eingezahlten Beträgen Edelmetalle zu marktüblichen Preisen zu erwerben, zu lagern und zu verwalten und habe dem Beklagten in dessen Funktion als Rechtsanwalt und öffentlicher Notar den Auftrag erteilt, jährliche Prüfberichte über den vollständigen Bestand zu erstellen.

| Predicted | Gold |
|---|---|
| `Die Aktiengesellschaft` | `Die Aktiengesellschaft` |

**Example 1** (doc_id: `deanon_TRAIN/10Ob23_15b`) (sent_id: `deanon_TRAIN/10Ob23_15b_4`)


Steintra Solar GmbH, Kospachstraße 35, 3162 Rainfeld, Österreich, vertreten durch Dr. Paul Vavrovsky und Mag. Christian Schrott, Rechtsanwälte in Salzburg, 2. Umwelt Dorfwald ges.m.b.H., Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich, vertreten durch Dr. Katharina Sedlazeck-Gschaider, Rechtsanwältin in Salzburg, wegen 11.921,56 EUR sA und Feststellung (Streitwert 5.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 27. Jänner 2015, GZ 11 R 14/14d-34, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Steintra Solar GmbH` | `Steintra Solar GmbH` |

**Missed by this rule (FN):**

- `Kospachstraße 35, 3162 Rainfeld, Österreich` (address)
- `Umwelt Dorfwald ges.m.b.H.` (organisation)
- `Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich` (address)

**Example 2** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_5`)


Maschinenbau Heimfurtcon GmbH, Fretzschner Medien, 2.

| Predicted | Gold |
|---|---|
| `Maschinenbau Heimfurtcon GmbH` | `Maschinenbau Heimfurtcon GmbH` |

**Missed by this rule (FN):**

- `Fretzschner Medien` (organisation)

**Example 3** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_6`)


OberTratraSoftware Dienstleistungen AG, Prägrader Weg 43, 8616 Gasen, Österreich, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung (5.000 EUR) und 11.561,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2019, GZ 2 R 140/19z-30, mit dem das Urteil des Landesgerichts Wels vom 22. Juli 2019, GZ 26 Cg 66/18m-26, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

| Predicted | Gold |
|---|---|
| `OberTratraSoftware Dienstleistungen AG` | `OberTratraSoftware Dienstleistungen AG` |

**Missed by this rule (FN):**

- `Prägrader Weg 43, 8616 Gasen, Österreich` (address)

**Example 4** (doc_id: `deanon_TRAIN/2Ob159_18y`) (sent_id: `deanon_TRAIN/2Ob159_18y_11`)


Er selbst war ua als Fenstermonteur in der GmbH tätig.

| Predicted | Gold |
|---|---|
| `Er selbst war ua als Fenstermonteur in der GmbH` | `Er selbst war ua als Fenstermonteur in der GmbH` |

**Example 5** (doc_id: `deanon_TRAIN/2Ob63_11w`) (sent_id: `deanon_TRAIN/2Ob63_11w_4`)


Holz Seewald AG, Kaiserbrunnengasse 6, 5122 Lindach, Österreich, beide vertreten durch Dr. Leopold Hirsch, Rechtsanwalt in Salzburg, wegen 38.967,48 EUR sA und Feststellung (Streitinteresse 20.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 10. Februar 2011, GZ 4 R 206/10g-29, womit das Urteil des Landesgerichts Salzburg vom 17. August 2010, GZ 7 Cg 49/09f-25, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Holz Seewald AG` | `Holz Seewald AG` |

**Missed by this rule (FN):**

- `Kaiserbrunnengasse 6, 5122 Lindach, Österreich` (address)

**Example 6** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_62`)


Dabei wiesen die anwesenden Mitarbeiter der GmbH darauf hin, dass dieses Unternehmen Ansprechpartner für Serviceleistungen ist.

| Predicted | Gold |
|---|---|
| `Dabei wiesen die anwesenden Mitarbeiter der GmbH` | `Dabei wiesen die anwesenden Mitarbeiter der GmbH` |

**Example 7** (doc_id: `deanon_TRAIN/2Ob99_18z`) (sent_id: `deanon_TRAIN/2Ob99_18z_4`)


Oßmer KI GmbH, Dr.H.Pirchegger-Weg 23, 4154 Lengau, Österreich, vertreten durch Mag. Martina Hackl, Rechtsanwältin in Mödling, und 3. Pistor Pflege GmbH, Maierlweg 58, 4776 Kobledt, Österreich, vertreten durch Dr. Klaus Rainer, Rechtsanwalt in Graz, wegen 308.539,34 EUR sA und Feststellung (Streitwert 10.000 EUR), über die außerordentliche Revision der klagenden Partei (Revisionsinteresse 92.942,15 EUR) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. März 2018, GZ 1 R 140/17s-101, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oßmer KI GmbH` | `Oßmer KI GmbH` |

**Missed by this rule (FN):**

- `Dr.H.Pirchegger-Weg 23, 4154 Lengau, Österreich` (address)
- `Pistor Pflege GmbH` (organisation)
- `Maierlweg 58, 4776 Kobledt, Österreich` (address)

**Example 8** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_6`)


JQV Finanzen Gruppe GmbH, Innovationsplatz 79, 9751 Nigglai, Österreich, beide vertreten durch Ruggenthaler Rechtsanwalts KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 62.000 EUR) über den außerordentlichen Revisionsrekurs der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Wien vom 20. September 2010, GZ 30 R 29/10w-9, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `JQV Finanzen Gruppe GmbH` | `JQV Finanzen Gruppe GmbH` |

**Missed by this rule (FN):**

- `Innovationsplatz 79, 9751 Nigglai, Österreich` (address)

**Example 9** (doc_id: `deanon_TRAIN/4Ob98_20w`) (sent_id: `deanon_TRAIN/4Ob98_20w_5`)


Malkmuß Marine GmbH, Fettinger-Gasse 7, 4615 Niederprisching, Österreich, vertreten durch MMag.

| Predicted | Gold |
|---|---|
| `Malkmuß Marine GmbH` | `Malkmuß Marine GmbH` |

**Missed by this rule (FN):**

- `Fettinger-Gasse 7, 4615 Niederprisching, Österreich` (address)

**Example 10** (doc_id: `deanon_TRAIN/4Ob98_20w`) (sent_id: `deanon_TRAIN/4Ob98_20w_7`)


Roedel Textil GmbH, Hasledt 4, 9634 Bodenmühl, Österreich, vertreten durch Mag. Wolfgang Weilguni, Rechtsanwalt in Wien, wegen 1.028.146,05 EUR sA und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der Klägerin gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 21. April 2020, GZ 5 R 158/19w-116, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Roedel Textil GmbH` | `Roedel Textil GmbH` |

**Missed by this rule (FN):**

- `Hasledt 4, 9634 Bodenmühl, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_5`)


Die klagende Gesellschaft mit Sitz in Slowenien begehrt von der beklagten Gesellschaft mit Sitz in Deutschland im Europäischen Mahnverfahren nach der Verordnung (EG) 1896/2006 des Europäischen Parlaments und des Rates vom 12.

**False Positives:**

- `Die klagende Gesellschaft mit Sitz in Slowenien begehrt von der beklagten Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/10Ob13_20i`) (sent_id: `deanon_TRAIN/10Ob13_20i_10`)


Diese planten die Gründung einer Gesellschaft mit beschränkter Haftung, die die Liegenschaft erwerben und nach Parzellierung gewinnbringend weiterverkaufen sollte.

**False Positives:**

- `Diese planten die Gründung einer Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/10Ob15_16b`) (sent_id: `deanon_TRAIN/10Ob15_16b_35`)


Ohne konkrete Anhaltspunkte sind solche Schritte vom Gericht nicht zu unternehmen (10 Ob 67/11t;NeumayrinSchwimann/Kodek, ABGB4§ 11 UVG Rz 10 ff).

**False Positives:**

- `Ohne konkrete Anhaltspunkte sind solche Schritte vom Gericht nicht zu unternehmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10Ob18_13i`) (sent_id: `deanon_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Monsud-Textil GmbH, VetR Herbert Dedert, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Textil GmbH` — partial — pred is substring of gold: `Monsud-Textil GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Monsud-Textil GmbH`(organisation)
- `VetR Herbert Dedert`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob29_25z`) (sent_id: `deanon_TRAIN/10Ob29_25z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hargassner als Vorsitzenden, den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier sowie die Hofrätin Dr. Wallner-Friedl in der Rechtssache der klagenden Partei Enns Werkdonver Holding GmbH, Mag.a DDr.in Lynn Rothwein, vertreten durch die Wallner Jorthan Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Prausewetter Umwelt AG, Valerius Gensmantel, vertreten durch die Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 25.380 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 13. Jänner 2025, GZ 12 R 40/24z-55, mit dem der Berufung der klagenden Partei nicht, hingegen jener der beklagten Partei gegen das Urteil des Landesgerichts Salzburg vom 25. Oktober 2024, GZ 14 Cg 35/22t-49, Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Friedl in der Rechtssache der klagenden Partei Enns Werkdonver Holding GmbH` — partial — gold is substring of pred: `Enns Werkdonver Holding GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Enns Werkdonver Holding GmbH`(organisation)
- `Mag.a DDr.in Lynn Rothwein`(person)
- `Prausewetter Umwelt AG`(organisation)
- `Valerius Gensmantel`(person)

**Example 5** (doc_id: `deanon_TRAIN/10Ob42_15x`) (sent_id: `deanon_TRAIN/10Ob42_15x_17`)


Im Anwendungsbereich der EuZVO sei weder eine Zustellung per Post ohne Zustellnachweis, noch eine an die Postaufgabe anknüpfende Zustellfiktion des § 98 ZPO zulässig, sodass die Zustellung des Unterhaltsfestsetzungsbeschlusses, der dagegen erhobenen Rekurse, des Unterhaltsvorschussgewährungsbeschlusses und des dagegen erhobenen Rechtsmittels jeweils mangelhaft sei.

**False Positives:**

- `Im Anwendungsbereich der EuZVO sei weder eine Zustellung per Post` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt, aus denen Erträge erzielt werden sollen.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — partial — gold is substring of pred: `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`(organisation)

**Example 7** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_7`)


Der Fonds wurde von einer in Deutschland ansässigen AG aufgelegt.

**False Positives:**

- `Der Fonds wurde von einer in Deutschland ansässigen AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_34`)


10. 2019 zu einem völlig gleichgelagerten Fall zu der vom Berufungsgericht angesprochenen Rechtsfrage Stellung genommen hat (beklagte Partei ist hier wie dort die Derber GmbH in Liqu).

**False Positives:**

- `beklagte Partei ist hier wie dort die Derber GmbH` — partial — gold is substring of pred: `Derber GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Derber GmbH`(organisation)

**Example 9** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Daniel Wiegand, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei West-Medien Manufaktur GmbH in Liqu, Kanzelweg 32, 4850 Oberthalheim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Medien Manufaktur GmbH` — partial — pred is substring of gold: `West-Medien Manufaktur GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DI Daniel Wiegand`(person)
- `West-Medien Manufaktur GmbH`(organisation)
- `Kanzelweg 32, 4850 Oberthalheim, Österreich`(address)
- `Eckert Rechtsanwalts GmbH`(organisation)

**Example 10** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_5`)


Text Begründung: Der Kläger erwarb als Verbraucher im Juni 2003 über Vermittlung eines selbständigen Vermögensberaters Kommanditanteile an der Bestelmeyer+Keßelheim Software GmbH & Co KG im Nominale von 17.000 EUR zuzüglich 850 EUR Agio.

**False Positives:**

- `Keßelheim Software GmbH & Co KG` — positional overlap with gold: `Bestelmeyer+Keßelheim Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bestelmeyer+Keßelheim Software GmbH`(organisation)

**Example 11** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — partial — gold is substring of pred: `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`(organisation)

**Example 12** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_7`)


Der Fonds wurde von einer in Deutschland ansässigen Aktiengesellschaft aufgelegt.

**False Positives:**

- `Der Fonds wurde von einer in Deutschland ansässigen Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_6`)


Text Gründe: Mit dem angefochtenen Urteil wurden Bernhard Beinicke und Norbert Wentzlick von der wider sie erhobenen Anklage, sie hätten am 7. Februar 2009 in Churer Straße 54, 9064 St. Michael ob der Gurk, Österreich /Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der DKZ Solar GesmbH & Co KG, Susanne Schueßler, durch die Vorgabe, die HochForschung GmbH sei eine zahlungsfähige Leasingnehmerin, somit durch Täuschung über Tatsachen, zum Abschluss eines Leasingvertrags über ein Rennfahrzeug für die Dauer von 24 Monaten zu einem monatlichen Entgelt von 10.698,10 Euro, somit zu einer Handlung verleitet, welche die Stadt-Sanitär Services GesmbH & Co KG in einem 50.000 Euro übersteigenden Betrag von insgesamt 235.358,20 Euro am Vermögen schädigte, gemäß § 259 Z 3 StPO (verfehlt auch von der rechtlichen Kategorie; vglLendl, WK-StPO § 259 Rz 1) freigesprochen.

**False Positives:**

- `Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der DKZ Solar GesmbH & Co KG` — partial — gold is substring of pred: `DKZ Solar GesmbH`
- `Sanitär Services GesmbH & Co KG` — positional overlap with gold: `Stadt-Sanitär Services GesmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bernhard Beinicke`(person)
- `Norbert Wentzlick`(person)
- `Churer Straße 54, 9064 St. Michael ob der Gurk, Österreich`(address)
- `DKZ Solar GesmbH`(organisation)
- `Susanne Schueßler`(person)
- `HochForschung GmbH`(organisation)
- `Stadt-Sanitär Services GesmbH`(organisation)

**Example 14** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_8`)


Nach den wesentlichen Feststellungen (US 3 bis 6) befand sich die See-Maschinenbau GmbH in der zweiten Jahreshälfte 2008 in erheblichen Zahlungsschwierigkeiten.

**False Positives:**

- `Maschinenbau GmbH` — partial — pred is substring of gold: `See-Maschinenbau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `See-Maschinenbau GmbH`(organisation)

**Example 15** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_11`)


„Nachdem“ es für die Wilken E‑Commerce GmbH notwendig geworden war, für die Aufnahme des Rennbetriebs 35.000 Euro in das Fahrzeug zu investieren, konnte aufgrund dessen schlechten Zustands kein Rennen erfolgreich beendet werden.

**False Positives:**

- `Commerce GmbH` — partial — pred is substring of gold: `Wilken E‑Commerce GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wilken E‑Commerce GmbH`(organisation)

**Example 16** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_23`)


Auch diesen Aspekt nimmt die Staatsanwaltschaft in der Rechtsrüge (Z 9 lit a) ausreichend in den Blick, indem sie auf - in Richtung der Erfüllung auch der objektiven Tatbestandsmerkmale der §§ 146, 147 Abs 3 StGB weisende - Beweisergebnisse zum vorliegenden Vertragsab-schluss trotz mangelnder finanzieller Ausstattung und Absicherung der Inn Dorfdersee GmbH hinweist.

**False Positives:**

- `schluss trotz mangelnder finanzieller Ausstattung und Absicherung der Inn Dorfdersee GmbH` — partial — gold is substring of pred: `Inn Dorfdersee GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Dorfdersee GmbH`(organisation)

**Example 17** (doc_id: `deanon_TRAIN/12Os107_11v`) (sent_id: `deanon_TRAIN/12Os107_11v_8`)


B./II./ am 13. November 2009 in Poysdorf als Zeugin in einem Ermittlungsverfahren nach der Strafprozessordnung vor der Kriminalpolizei bei ihrer förmlichen Vernehmung zur Sache falsch ausgesagt, indem sie wahrheitswidrig behauptete, die an sie bezahlten 22.800 Euro seien das Entgelt für LKW-Vermietungen an die Ost Lextal GmbH gewesen, wobei sie tatsächlich das Geld ausbezahlt bekam, ohne dafür an die genannte Gesellschaft eine Gegenleistung erbracht zu haben.

**False Positives:**

- `Vermietungen an die Ost Lextal GmbH` — partial — gold is substring of pred: `Ost Lextal GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ost Lextal GmbH`(organisation)

**Example 18** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__9`)


Text Gründe: Mit unbekämpft in Rechtskraft erwachsenen Urteilen des Bezirksgerichts Spittal an der Drau vom 22. Juni 2017, GZ 5 U 5/17f-26, wurden (I) Andreas Feiereisen des Vergehens der fahrlässigen Tötung nach § 80 Abs 1 StGB schuldig erkannt und hiefür zu einer Geldstrafe verurteilt sowie (II) die Werksynstein-Wind GmbH gemäß § 3 Abs 1 Z 2, Abs 2 VbVG für die vom Schuldspruch (I) erfasste Straftat ihres Entscheidungsträgers verantwortlich erklärt und über diese Gesellschaft eine Verbandsgeldbuße von 70 Tagessätzen zu je 50 Euro verhängt, die unter Bestimmung einer Probezeit von drei Jahren bedingt nachgesehen wurde.

**False Positives:**

- `Wind GmbH` — partial — pred is substring of gold: `Werksynstein-Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Feiereisen`(person)
- `Werksynstein-Wind GmbH`(organisation)

**Example 19** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__17`)


Indem das Bezirksgericht über die Jusepeitis&Niemöller Bildung GmbH eine (das Höchstmaß von somit 55 Tagessätzen übersteigende) Verbandsgeldbuße von 70 Tagessätzen verhängte, verletzte es § 4 Abs 3 VbVG).

**False Positives:**

- `Niemöller Bildung GmbH` — partial — pred is substring of gold: `Jusepeitis&Niemöller Bildung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jusepeitis&Niemöller Bildung GmbH`(organisation)

**Example 20** (doc_id: `deanon_TRAIN/15Os133_11i_15Os134_11m_`) (sent_id: `deanon_TRAIN/15Os133_11i_15Os134_11m__4`)


In der Medienrechtssache des Antragstellers Siegfried Kaierleber gegen die Antragsgegnerin MYPQ Versicherung Dienstleistungen GmbH wegen §§ 6 Abs 1, 8a Abs 6 MedienG, AZ 91 Hv 72/05g des Landesgerichts für Strafsachen Wien, verletzen die Beschlüsse dieses Gerichts vom 28. April 2009, GZ 91 Hv 72/05g-75, und des Oberlandesgerichts Wien als Beschwerdegericht vom 6. Juli 2009, AZ 18 Bs 218/09d, § 39 Abs 1 und § 56 Abs 1 (Art VI b Abs 1 in der Fassung BGBl I 2005/49) MedienG.

**False Positives:**

- `In der Medienrechtssache des Antragstellers Siegfried Kaierleber gegen die Antragsgegnerin MYPQ Versicherung Dienstleistungen GmbH` — partial — gold is substring of pred: `Kaierleber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kaierleber`(person)
- `MYPQ Versicherung Dienstleistungen GmbH`(organisation)

**Example 21** (doc_id: `deanon_TRAIN/17Ob10_20z`) (sent_id: `deanon_TRAIN/17Ob10_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätinnen Mag. Malesich und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Levi Adelwart, vertreten durch Stephan Briem Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Dr. Penelope Piephans als Treuhänder der Insolvenzgläubiger der Valkraftfen-Analyse Aktiengesellschaft, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH in Linz, wegen Feststellung (Streitwert 18.335,66 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. März 2020, GZ 1 R 31/20i-13, womit das Urteil des Landesgerichts Linz vom 9. Dezember 2019, GZ 4 Cg 73/18z-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Analyse Aktiengesellschaft` — partial — pred is substring of gold: `Valkraftfen-Analyse Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Levi Adelwart`(person)
- `Dr. Penelope Piephans`(person)
- `Valkraftfen-Analyse Aktiengesellschaft`(organisation)

**Example 22** (doc_id: `deanon_TRAIN/18ONc1_21y`) (sent_id: `deanon_TRAIN/18ONc1_21y_3`)


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

**Example 23** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Herbes&Vißers Heizung GmbH, Waldemar Lokämper, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Traun-Luftfahrt GmbH, VetR DDr. Walter Stuehrmann, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

**False Positives:**

- `Vißers Heizung GmbH` — partial — pred is substring of gold: `Herbes&Vißers Heizung GmbH`
- `Luftfahrt GmbH` — partial — pred is substring of gold: `Traun-Luftfahrt GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Wiener Neustadt`(organisation)
- `Herbes&Vißers Heizung GmbH`(organisation)
- `Waldemar Lokämper`(person)
- `Traun-Luftfahrt GmbH`(organisation)
- `VetR DDr. Walter Stuehrmann`(person)
- `Landesgericht Feldkirch`(organisation)

**Example 24** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_4`)


Republik Österreich, vertreten durch die Finanzprokuratur in Wien, 2. Dr. Ralph Kreidenweiß, und 3. Donau-Automotive GmbH, Ebersreith 11, 8761 Götzendorf, Österreich, beide vertreten durch Dr. Hubert Simon, Rechtsanwalt in Wien, wegen Leistung und Feststellung, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. April 2014, GZ 7 R 21/14h-7, mit dem der Beschluss des Landesgerichts Leoben vom 30. Jänner 2014, GZ 2 Nc 2/14y-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Automotive GmbH` — partial — pred is substring of gold: `Donau-Automotive GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Ralph Kreidenweiß`(person)
- `Donau-Automotive GmbH`(organisation)
- `Ebersreith 11, 8761 Götzendorf, Österreich`(address)

**Example 25** (doc_id: `deanon_TRAIN/1Ob140_14s`) (sent_id: `deanon_TRAIN/1Ob140_14s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer und Mag. Dr. Wurdinger sowie die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft, Meidlinger Hauptstraße 19, 5233 Erlach, Österreich, vertreten durch die Walch & Zehetbauer Rechtsanwälte OG, Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 344.011,19 EUR und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Juni 2014, GZ 4 R 202/13g-54, mit dem das Teilzwischenurteil des Landesgerichts Feldkirch vom 2. August 2013, GZ 8 Cg 143/11y-46, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

**False Positives:**

- `Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft` — partial — gold is substring of pred: `Tracondon Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tracondon Aktiengesellschaft`(organisation)
- `Meidlinger Hauptstraße 19, 5233 Erlach, Österreich`(address)

**Example 26** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Dr. Wurdinger als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Steger, Mag. Wessely-Kristöfel, Dr. Parzmayr und Dr. Pfurtscheller als weitere Richterinnen und Richter in der Rechtssache der klagenden Partei Bundeskammer für Arbeiter und Angestellte, Wien 4, Prinz-Eugen-Straße 20–22, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Alsynwald-Recycling AG, RgR Mag. Dr. Evelyn Steinkröger, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH in Wien, wegen Unterlassung und Urteilsveröffentlichung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. Juli 2024, GZ 2 R 77/24v-15, mit dem das Urteil des Handelsgerichts Wien vom 28. Februar 2024, GZ 57 Cg 36/23d-8, bestätigt wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Recycling AG` — partial — pred is substring of gold: `Alsynwald-Recycling AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alsynwald-Recycling AG`(organisation)
- `RgR Mag. Dr. Evelyn Steinkröger`(person)

**Example 27** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_105`)


Die Beklagte müsse weder ihre interne Kalkulation offenlegen noch sämtliche Dienstleistungen, die mit der Bearbeitungsgebühr abgegolten würden, einzeln anführen.

**False Positives:**

- `Die Beklagte müsse weder ihre interne Kalkulation offenlegen noch sämtliche Dienstleistungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_116`)


Die Nieder Norber AG wird den Kunden in der Mitteilung auf die Änderungen hinweisen und darauf aufmerksam machen, dass sein Stillschweigen nach Ablauf der zwei Monate ab Zugang der Mitteilung durch das Unterlassen eines Widerspruchs in Schriftform als Zustimmung zu den Änderungen gilt.

**False Positives:**

- `Die Nieder Norber AG` — partial — gold is substring of pred: `Nieder Norber AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Norber AG`(organisation)

**Example 29** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_117`)


Außerdem wird die Valwalduni-Handel AG eine Gegenüberstellung über die von der Änderung betroffenen Bestimmungen sowie die vollständige Fassung der neuen Bedingungen auf ihrer Internetseite veröffentlichen und die Gegenüberstellung dem Kunden auf sein Verlangen zur Verfügung stellen;

**False Positives:**

- `Handel AG` — partial — pred is substring of gold: `Valwalduni-Handel AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Valwalduni-Handel AG`(organisation)

**Example 30** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_118`)


auch darauf wird die Landwerlin&Plumke Versand AG in derMitteilung hinweisen.

**False Positives:**

- `Plumke Versand AG` — partial — pred is substring of gold: `Landwerlin&Plumke Versand AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landwerlin&Plumke Versand AG`(organisation)

**Example 31** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_168`)


Dabei handelt es sich jedenfalls um wesentliche Pflichten der Parteien und insbesondere von der Bank geschuldete Leistungen.

**False Positives:**

- `Dabei handelt es sich jedenfalls um wesentliche Pflichten der Parteien und insbesondere von der Bank` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_TRAIN/1Ob182_17x`) (sent_id: `deanon_TRAIN/1Ob182_17x_25`)


Nach dem von den Vorinstanzen zugrunde gelegten Sachverhalt beabsichtigt der Antragsgegner einer zur Unternehmensgruppe der Familie gehörenden GmbH, an der er nur mehr einen Geschäftsanteil von 1 % hält, der aber mit weitreichenden Sonderrechten ausgestattet ist, und die einen dringenden Finanzierungsbedarf in Höhe von 3 Mio EUR hat, ein Privatdarlehen in dieser Höhe zu gewähren, dass er wiederum durch Aufnahme eines entsprechenden Bankkredits finanzieren will, von dem bereits 1 Mio EUR an den Antragsgegner und von diesem an die GmbH geflossen sind.

**False Positives:**

- `Nach dem von den Vorinstanzen zugrunde gelegten Sachverhalt beabsichtigt der Antragsgegner einer zur Unternehmensgruppe der Familie gehörenden GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_TRAIN/1Ob221_17g`) (sent_id: `deanon_TRAIN/1Ob221_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und Hofrätinnen Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Boothe u. Sandmeier IT GmbH (früher OberTelekom GmbH), Ewaldgasse 28, 4084 Mitterberg, Österreich, vormals vertreten durch Dr. Wolfgang Poleschinski, Rechtsanwalt in Hartberg, gegen die beklagte Partei Yelec Dangelmeier, vertreten durch die Dr. Farhad Paya Rechtsanwalt GmbH, Klagenfurt am Wörthersee, wegen 7.583,60 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 24. August 2017, GZ 1 R 127/17x-69, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 28. März 2017, GZ 16 C 1333/14i-65, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

**False Positives:**

- `früher OberTelekom GmbH` — partial — gold is substring of pred: `OberTelekom GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Boothe u. Sandmeier IT GmbH`(organisation)
- `OberTelekom GmbH`(organisation)
- `Ewaldgasse 28, 4084 Mitterberg, Österreich`(address)
- `Yelec Dangelmeier`(person)
- `Farhad Paya Rechtsanwalt GmbH`(organisation)

**Example 34** (doc_id: `deanon_TRAIN/1Ob22_24b`) (sent_id: `deanon_TRAIN/1Ob22_24b_10`)


Nach Verstaatlichung der Bank erzielt er daraus kein Einkommen mehr.

**False Positives:**

- `Nach Verstaatlichung der Bank` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_TRAIN/1Ob26_20k`) (sent_id: `deanon_TRAIN/1Ob26_20k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Synsynfurt-Finanzen GmbH, Tanja Thielike, vertreten durch die Draxler Rexeis Sozietät von Rechtsanwälten OG, Graz, gegen die beklagte Partei Roberta Reumschüssel, Bakk. phil., vertreten durch Mag. Dr. Alfred Wansch, Rechtsanwalt in Wien, wegen Räumung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtsachen Wien als Berufungsgericht vom 13. November 2019, GZ 39 R 228/19x-70, mit dem das Urteil des Bezirksgerichts Hernals vom 30. April 2019, GZ 4 C 277/16f-64, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Finanzen GmbH` — partial — pred is substring of gold: `Synsynfurt-Finanzen GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synsynfurt-Finanzen GmbH`(organisation)
- `Tanja Thielike`(person)
- `Roberta Reumschüssel, Bakk. phil.`(person)

**Example 36** (doc_id: `deanon_TRAIN/1Ob38_21a`) (sent_id: `deanon_TRAIN/1Ob38_21a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei HR Janet Henken, vertreten durch die Greiml & Horwath Rechtsanwaltspartnerschaft, Graz, gegen die beklagte Partei Elvira Nossal, vertreten durch die Neger/Ulm Rechtsanwälte GmbH, Graz, wegen 6.720 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 3. Juni 2020, GZ 6 R 115/20f-20, mit dem das Urteil des Bezirksgerichts Deutschlandsberg vom 20. März 2020, GZ 11 C 55/19t-16, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Ulm Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `HR Janet Henken`(person)
- `Elvira Nossal`(person)

**Example 37** (doc_id: `deanon_TRAIN/1Ob57_16p`) (sent_id: `deanon_TRAIN/1Ob57_16p_16`)


Die Antragstellerin maturierte (erst) mit Nachprüfung im März 2009 und bereitete sich nach einem dreimonatigen Überbrückungsstudium auf das letztlich (nach einer erfolglos versuchten Aufnahmeprüfung an der Universität für Musik und darstellende Kunst Wien im September 2009) im Februar 2010 am Vienna Konservatorium begonnene Harfestudium durch den Besuch einer Musikschule neben einer Vollzeitbeschäftigung vor.

**False Positives:**

- `nach einer erfolglos versuchten Aufnahmeprüfung an der Universität` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_TRAIN/1Ob9_22p`) (sent_id: `deanon_TRAIN/1Ob9_22p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. HR Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Parteien 1. Mag. Tosca Xyländer und 2. Mag. Heinrich Vlachojannis, vertreten durch die Koch Jilek Rechtsanwälte Partnerschaft, Bruck an der Mur, gegen die beklagte Partei Grüttemann E‑Commerce Aktiengesellschaft, Friedhof Döbling 165, 8401 Abtissendorf, Österreich, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH, Wien, wegen 40.358,88 EUR sA, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. November 2021, GZ 5 R 163/21h-43, mit dem das Urteil des Handelsgerichts Wien vom 31. August 2021, GZ 55 Cg 60/20i-36, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Commerce Aktiengesellschaft` — partial — pred is substring of gold: `Grüttemann E‑Commerce Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Tosca Xyländer`(person)
- `Mag. Heinrich Vlachojannis`(person)
- `Grüttemann E‑Commerce Aktiengesellschaft`(organisation)
- `Friedhof Döbling 165, 8401 Abtissendorf, Österreich`(address)

**Example 39** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_11`)


Denn die Beweisthemen (Geschäftsgrundlage der eingangs genannten Vereinbarung vom 11. Dezember 2012 mit der Süd-Immobilien AG; von derselben intendierte Verwertung der Liegenschaften in Draskovichgasse 12, 8240 Friedberg, Österreich durch Zwangsversteigerung ungeachtet eines allfälligen Abverkaufs von Liegenschaften in Steghof 15, 4891 Höhenwarth, Österreich ; Auftrag der Mandanten des Disziplinarbeschuldigten zur Zurückziehung des Antrags auf Aufhebung der Höfeeigenschaft;

**False Positives:**

- `Immobilien AG` — partial — pred is substring of gold: `Süd-Immobilien AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Süd-Immobilien AG`(organisation)
- `Draskovichgasse 12, 8240 Friedberg, Österreich`(address)
- `Steghof 15, 4891 Höhenwarth, Österreich`(address)

**Example 40** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_12`)


Unkenntnis des Disziplinarbeschuldigten von den Gründen der Daten Unizorstein AG für die beantragte Fortsetzung der Zwangsversteigerungsverfahren;

**False Positives:**

- `Unkenntnis des Disziplinarbeschuldigten von den Gründen der Daten Unizorstein AG` — partial — gold is substring of pred: `Daten Unizorstein AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Daten Unizorstein AG`(organisation)

**Example 41** (doc_id: `deanon_TRAIN/2Ob159_18y`) (sent_id: `deanon_TRAIN/2Ob159_18y_10`)


Der Kläger war Alleingesellschafter und -geschäftsführer einer GmbH, die sich mit Fenstermontage beschäftigte.

**False Positives:**

- `geschäftsführer einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_TRAIN/2Ob159_18y`) (sent_id: `deanon_TRAIN/2Ob159_18y_28`)


Die Berücksichtigung von Chancen und Risken für ein nicht mehr auf dem Markt befindliches Unternehmen wäre in den Bereich der reinen Spekulation einzuordnen.

**False Positives:**

- `Die Berücksichtigung von Chancen und Risken für ein nicht mehr auf dem Markt befindliches Unternehmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_TRAIN/2Ob226_19b`) (sent_id: `deanon_TRAIN/2Ob226_19b_8`)


Nach dem Tod der Mutter begleitete die Klägerin den Vater zur Bank, wo sich ein Schließfach der Mutter befand.

**False Positives:**

- `Nach dem Tod der Mutter begleitete die Klägerin den Vater zur Bank` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_19`)


Die beklagte Partei brachte das Gerät nach der Rücknahme zur KI Lexglanzber GmbH, deren Geschäftsführer der Cousin des Geschäftsführers der beklagten Partei ist.

**False Positives:**

- `Die beklagte Partei brachte das Gerät nach der Rücknahme zur KI Lexglanzber GmbH` — partial — gold is substring of pred: `KI Lexglanzber GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KI Lexglanzber GmbH`(organisation)

**Example 45** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_25`)


Im Herbst 2012 habe sich ein Aufkleber der Ostvallem-Robotik GmbH vom Luftentfeuchter gelöst und ein Typenschild mit dem Baujahr 1986 freigelegt.

**False Positives:**

- `Robotik GmbH` — partial — pred is substring of gold: `Ostvallem-Robotik GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ostvallem-Robotik GmbH`(organisation)

**Example 46** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_29`)


Der beklagten Partei sei schließlich bei der Planung der Dacheinhausung ein Fehler unterlaufen.

**False Positives:**

- `Der beklagten Partei sei schließlich bei der Planung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_61`)


Die beklagte Partei führte gemeinsam mit der LHS Lebensmittel Consulting GmbH eine Einschulungsveranstaltung für Heutrocknungsgeräte durch, an der auch der Kläger teilnahm.

**False Positives:**

- `Die beklagte Partei führte gemeinsam mit der LHS Lebensmittel Consulting GmbH` — partial — gold is substring of pred: `LHS Lebensmittel Consulting GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `LHS Lebensmittel Consulting GmbH`(organisation)

**Example 48** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_64`)


Der Kläger hat sich nie an die GmbH gewandt, um ein Service durchführen zu lassen.

**False Positives:**

- `Der Kläger hat sich nie an die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_78`)


Die Bachtri GmbH hat vor der Auslieferung des neu zusammengesetzten Geräts eine Druckprobe durchgeführt.

**False Positives:**

- `Die Bachtri GmbH` — partial — gold is substring of pred: `Bachtri GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bachtri GmbH`(organisation)

**Example 50** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_80`)


Die Maerklin und Steckelmann Software GmbH befüllte den neu zusammengesetzten Luftentfeuchter Anfang 2011 mit dem Kältemittel R22, dessen Verwendung seit 1. 1.

**False Positives:**

- `Die Maerklin und Steckelmann Software GmbH` — partial — gold is substring of pred: `Maerklin und Steckelmann Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maerklin und Steckelmann Software GmbH`(organisation)

**Example 51** (doc_id: `deanon_TRAIN/2Ob99_18z`) (sent_id: `deanon_TRAIN/2Ob99_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden, den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé sowie die Hofräte Dr. Nowotny und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Stadt-Textil GmbH & Co KG, Kreuzlandstraße 52, 9462 Kalchberg, Österreich, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Kazlowski + Röttjer Automotive GmbH, Clarissa Lenschau, vertreten durch Keschmann Rechtsanwalts-GmbH in Wien, sowie die Nebenintervenientinnen 1. Ost-Chemie GmbH, M.-Klieber-Gasse 22, 3611 Himberg, Österreich, vertreten durch Dr. Dirk Just, Rechtsanwalt in Wien, 2.

**False Positives:**

- `Textil GmbH & Co KG` — positional overlap with gold: `Stadt-Textil GmbH`
- `Chemie GmbH` — partial — pred is substring of gold: `Ost-Chemie GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stadt-Textil GmbH`(organisation)
- `Kreuzlandstraße 52, 9462 Kalchberg, Österreich`(address)
- `Kazlowski + Röttjer Automotive GmbH`(organisation)
- `Clarissa Lenschau`(person)
- `Ost-Chemie GmbH`(organisation)
- `M.-Klieber-Gasse 22, 3611 Himberg, Österreich`(address)

**Example 52** (doc_id: `deanon_TRAIN/3Nc19_22g`) (sent_id: `deanon_TRAIN/3Nc19_22g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek sowie den Hofrat Dr. Stefula als weitere Richter in der Ordinationssache der Antragstellerin Stadt-Robotik GmbH, Hum 65, 9241 Kantnig, Österreich, vertreten durch Specht & Partner Rechtsanwalt GmbH in Wien, gegen die Antragsgegnerin Ing. Verona Obersteiner, Russische Föderation, wegen § 355 EO, über den Ordinationsantrag der Antragstellerin, den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Robotik GmbH` — partial — pred is substring of gold: `Stadt-Robotik GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stadt-Robotik GmbH`(organisation)
- `Hum 65, 9241 Kantnig, Österreich`(address)
- `Partner Rechtsanwalt GmbH`(organisation)
- `Ing. Verona Obersteiner`(person)

**Example 53** (doc_id: `deanon_TRAIN/3Ob105_13g`) (sent_id: `deanon_TRAIN/3Ob105_13g_13`)


Erst Anfang Juni habe sie den Betrieb einstellen müssen.

**False Positives:**

- `Erst Anfang Juni habe sie den Betrieb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_TRAIN/3Ob114_14g`) (sent_id: `deanon_TRAIN/3Ob114_14g_4`)


KzlR Hartmut Raffenberg KG und 2.

**False Positives:**

- `KzlR Hartmut Raffenberg KG` — partial — gold is substring of pred: `KzlR Hartmut Raffenberg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KzlR Hartmut Raffenberg`(person)

**Example 55** (doc_id: `deanon_TRAIN/3Ob114_14g`) (sent_id: `deanon_TRAIN/3Ob114_14g_6`)


Begründung:  Rechtliche Beurteilung Die Erstklägerin (eine Rechtsanwalts KG), der Zweitkläger (deren Komplementär) und die Mutter des Zweitklägers (in Hinkunft: Pensionsberechtigte) führten als Kläger und Widerbeklagte ein Schiedsverfahren gegen den (hier) Beklagten (als ausgeschiedenen Komplementär) als Beklagten und Widerkläger, das mit einem Schiedsspruch vom 2. Mai 2011 endete.

**False Positives:**

- `eine Rechtsanwalts KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_TRAIN/3Ob114_14g`) (sent_id: `deanon_TRAIN/3Ob114_14g_58`)


8.Die Vorinstanzen legten nicht die Bilanzen einer Rechtsanwälte GmbH als Bemessungsgrundlage zugrunde, sondern die Gewinnanteile des Beklagten an dieser Rechtsanwälte GmbH; zu einer allfälligen Minderung dieses Einkommens des Beklagten wurde eine Negativfeststellung getroffen, die zu seinen Lasten geht.

**False Positives:**

- `Die Vorinstanzen legten nicht die Bilanzen einer Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_TRAIN/3Ob164_20v`) (sent_id: `deanon_TRAIN/3Ob164_20v_59`)


Als Preise für die Abnahme elektrischer Energie aus Stromerzeugungsanlagen (Neuanlagen), die unter ausschließlicher Verwendung des Energieträgers feste Biomasse (zB Waldhackgut) betrieben werden, werden folgende Beträge festgesetzt: ... (2)

**False Positives:**

- `Als Preise für die Abnahme elektrischer Energie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_TRAIN/3Ob164_20v`) (sent_id: `deanon_TRAIN/3Ob164_20v_60`)


Als Preise für die Abnahme elektrischer Energie aus Stromerzeugungsanlagen (Neuanlagen), die unter ausschließlicher Verwendung des Energieträgers Abfälle mit hohem biogenen Anteil betrieben werden, werden folgende Beträge festgesetzt: 1.

**False Positives:**

- `Als Preise für die Abnahme elektrischer Energie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_TRAIN/3Ob164_20v`) (sent_id: `deanon_TRAIN/3Ob164_20v_105`)


Als Tarife für die Abnahme elektrischer Energie aus Stromerzeugungsanlagen, die unter ausschließlicher Verwendung von fester Biomasse, jedoch mit Ausnahme von Abfällen mit hohem biogenen Anteil, betrieben werden, werden folgende Beträge festgesetzt: [...]

**False Positives:**

- `Als Tarife für die Abnahme elektrischer Energie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_TRAIN/3Ob164_20v`) (sent_id: `deanon_TRAIN/3Ob164_20v_111`)


Hinsichtlich der Tarife für die Abnahme elektrischer Energie aus Hybrid- und Mischfeuerungsanlagen bei Zufeuerung in kalorischen Kraftwerken, die unter Einsatz der Energieträger Biomasse oder Abfälle mit hohem biogenen Anteil betrieben werden, gilt Folgendes: 1.

**False Positives:**

- `Hinsichtlich der Tarife für die Abnahme elektrischer Energie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_TRAIN/3Ob248_10g`) (sent_id: `deanon_TRAIN/3Ob248_10g_5`)


Text Begründung: Der nunmehrige Oppositionsbeklagte Ronja Crux hatte im Jahr 2005 bei der nunmehrigen Oppositionsklägerin, der Synkraftal-Chemie GmbH, einen gebrauchten Pkw Porsche Carrera 4 gekauft.

**False Positives:**

- `Chemie GmbH` — partial — pred is substring of gold: `Synkraftal-Chemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ronja Crux`(person)
- `Synkraftal-Chemie GmbH`(organisation)

**Example 62** (doc_id: `deanon_TRAIN/3Ob32_17b`) (sent_id: `deanon_TRAIN/3Ob32_17b_77`)


Dass sie sich dessen auch bewusst war, zeigt die mit Dr. Sibylle Duvenkrop bestehende Vereinbarung, auch an die Verpflichtete gerichtete RSb-Sendungen von der Post zu übernehmen und diese an die Verpflichtete weiterzuleiten.

**False Positives:**

- `Sendungen von der Post` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Sibylle Duvenkrop`(person)

**Example 63** (doc_id: `deanon_TRAIN/3Ob44_20x`) (sent_id: `deanon_TRAIN/3Ob44_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie die Hofräte Priv.-Doz. Dr. Rassi und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Andreas Clösges, vertreten durch die Eger/Gründl Rechtsanwälte OG in Graz, gegen die beklagte Partei Chemie Valtri GmbH, Niels Niefeldt, vertreten durch Mag. Manuel Fähnrich, Rechtsanwalt in Graz, wegen 34.000 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 31. Jänner 2020, GZ 2 R 168/19x-28, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Gründl Rechtsanwälte OG` — partial — pred is substring of gold: `Eger/Gründl Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Andreas Clösges`(person)
- `Eger/Gründl Rechtsanwälte OG`(organisation)
- `Chemie Valtri GmbH`(organisation)
- `Niels Niefeldt`(person)

**Example 64** (doc_id: `deanon_TRAIN/4Fsc1_10z`) (sent_id: `deanon_TRAIN/4Fsc1_10z_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel und Dr. Jensik als weitere Richter in der Rechtssache der klagenden Partei Lexglanzfen-Garten AG, Pia Özbek, vertreten durch Dr. Hartmut Mayer, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Esra Waitkat, vertreten durch Mag. Gerhard Pilz, Rechtsanwalt, als Verfahrenshelfer, wegen 3.330,19 EUR sA (AZ 35 R 24/09b des Landesgerichts für Zivilrechtssachen Wien), zum Fristsetzungsantrag der beklagten Partei vom 28. Oktober 2009 an den Obersten Gerichtshof im Ablehnungsverfahren den Beschluss gefasst:  Spruch Der Fristsetzungsantrag wird zurückgewiesen.

**False Positives:**

- `Garten AG` — partial — pred is substring of gold: `Lexglanzfen-Garten AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lexglanzfen-Garten AG`(organisation)
- `Pia Özbek`(person)
- `Mag. Esra Waitkat`(person)

**Example 65** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_4`)


Logdercon-Digital, Dänemark, 2. Fengart GmbH, Oberer Weinweg 87, 9020 Klagenfurt, Österreich, beide vertreten durch Graf & Pitkowitz Rechtsanwälte GmbH in Wien, gegen die Beklagten 1. LGR Medien GmbH, OVX Finanzen, 2. Analyse Kelunizor AG, Fahnberg 42, 4100 Großamberg, Österreich, Deutschland, beide vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Gesamtstreitwert 69.500 EUR), über den Ordinationsantrag der Klägerinnen den Beschluss gefasst:  Spruch Dem Ordinationsantrag wird stattgegeben.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Logdercon-Digital`(organisation)
- `Fengart GmbH`(organisation)
- `Oberer Weinweg 87, 9020 Klagenfurt, Österreich`(address)
- `LGR Medien GmbH`(organisation)
- `OVX Finanzen`(organisation)
- `Analyse Kelunizor AG`(organisation)
- `Fahnberg 42, 4100 Großamberg, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)

**Example 66** (doc_id: `deanon_TRAIN/4Ob136_11w`) (sent_id: `deanon_TRAIN/4Ob136_11w_5`)


Lee Tinnemeyer, 2. Mag. Romana Weisbrodt, beide vertreten durch Mag. Ulrich Salburg, Rechtsanwalt in Wien, gegen die beklagte Partei Nexbach-Marine AG, StR Hon.-Prof.in Linda Tarak, vertreten durch Kunz Schima Wallentin Rechtsanwälte OEG in Wien, wegen 60.626,11 EUR sA, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. November 2011, GZ 1 R 242/10f-21, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Marine AG` — partial — pred is substring of gold: `Nexbach-Marine AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lee Tinnemeyer`(person)
- `Mag. Romana Weisbrodt`(person)
- `Nexbach-Marine AG`(organisation)
- `StR Hon.-Prof.in Linda Tarak`(person)

**Example 67** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei XDC Druck GmbH, Scarlett Augustus, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Wien, gegen die beklagte Partei UBER B.V., Larissa Ebele, Niederlande, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Unterlassung, Veröffentlichung und Feststellung (Streitwert im Sicherungsverfahren 70.000 EUR), über den Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 4. Juli 2018, GZ 3 R 32/18z-14, mit dem der Beschluss des Handelsgerichts Wien vom 24. April 2018, GZ 58 Cg 10/18f-6, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei XDC Druck GmbH` — partial — gold is substring of pred: `XDC Druck GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `XDC Druck GmbH`(organisation)
- `Scarlett Augustus`(person)
- `Larissa Ebele`(person)

**Example 68** (doc_id: `deanon_TRAIN/4Ob18_20f`) (sent_id: `deanon_TRAIN/4Ob18_20f_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Jörg Drathschmidt, vertreten durch Dr. Winfried Sattlegger und andere Rechtsanwälte in Linz, gegen die beklagte Partei Wien Dorfsud GmbH, Gerlinde Balcerzak, vertreten durch Dr. Helmut Trenkwalder, Rechtsanwalt in Linz, und die Nebenintervenientin auf Seiten der beklagten Partei Waldfen-Versand GmbH, Eva Boztas, vertreten durch Schneider & Schneider Rechtsanwalts GmbH in Wien, wegen 35.628,94 EUR sA Zug um Zug gegen Herausgabe eines Fahrzeugs, über den Rekurs der Nebenintervenientin gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht vom 7. November 2019, GZ 6 R 114/19f-41, mit dem das Urteil des Landesgerichts Linz vom 3. Juli 2019, GZ 36 Cg 4/17m-36, im klagsstattgebenden Teil (Spruchpunkt 1.) aufgehoben wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Versand GmbH` — partial — pred is substring of gold: `Waldfen-Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jörg Drathschmidt`(person)
- `Wien Dorfsud GmbH`(organisation)
- `Gerlinde Balcerzak`(person)
- `Waldfen-Versand GmbH`(organisation)
- `Eva Boztas`(person)
- `Schneider Rechtsanwalts GmbH`(organisation)

**Example 69** (doc_id: `deanon_TRAIN/4Ob194_22s`) (sent_id: `deanon_TRAIN/4Ob194_22s_4`)


Matzka und Dr. Annerl sowie die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Dueckers Wind GmbH, Corvin Cetinbag, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, gegen die beklagten Parteien 1. Wendy Goetzen (Verein), 2. Birkfeld+Münzenrieder Daten GmbH, beide Stegg 92, 3925 Neumelon, Österreich, vertreten durch Dr. Brigitte Birnbaum, Dr. Rainer Toperczer, Rechtsanwälte in Wien, wegen Unterlassung, Herausgabe, Feststellung und Urteilsveröffentlichung (Gesamtstreitwert 75.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Juli 2022, GZ 2 R 47/22d-41, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Münzenrieder Daten GmbH` — partial — pred is substring of gold: `Birkfeld+Münzenrieder Daten GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dueckers Wind GmbH`(organisation)
- `Corvin Cetinbag`(person)
- `Wendy Goetzen`(person)
- `Birkfeld+Münzenrieder Daten GmbH`(organisation)
- `Stegg 92, 3925 Neumelon, Österreich`(address)

**Example 70** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Kraftheimglanz-Versand GmbH, OStR Dipl.

**False Positives:**

- `Versand GmbH` — partial — pred is substring of gold: `Kraftheimglanz-Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kraftheimglanz-Versand GmbH`(organisation)

**Example 71** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_5`)


Klingenbeil Versand GmbH & Co KG, 2.

**False Positives:**

- `Klingenbeil Versand GmbH & Co KG` — partial — gold is substring of pred: `Klingenbeil Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Klingenbeil Versand GmbH`(organisation)

**Example 72** (doc_id: `deanon_TRAIN/4Ob19_10p`) (sent_id: `deanon_TRAIN/4Ob19_10p_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Traun-Sanitär gesellschaft mbH,*****, vertreten durch Prof. Haslinger & Partner, Rechtsanwälte in Linz, gegen die beklagte Partei NWJ KI Dienstleistungen AG,*****, vertreten durch Rechtsanwälte Konrad & Schröttner OG in Graz, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 65.000 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 25. November 2009, GZ 6 R 169/09h-37, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Sanitär gesellschaft` — partial — pred is substring of gold: `Traun-Sanitär gesellschaft mbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Traun-Sanitär gesellschaft mbH`(organisation)
- `NWJ KI Dienstleistungen AG`(organisation)

**Example 73** (doc_id: `deanon_TRAIN/4Ob224_23d`) (sent_id: `deanon_TRAIN/4Ob224_23d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, den Hofrat Mag. Dr. Wurdinger und die Hofrätin Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Verlexglanz-Marine GmbH, Andreas Häntsch, Deutschland, vertreten durch die Saxinger Chalupsky & Partner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Emma Bergner kammer, Cathleen Hofschulte, vertreten durch Dr. Friedrich Schulz, Rechtsanwalt in Wien, wegen Unterlassung, Widerruf und Veröffentlichung desselben (Gesamtstreitwert 46.200 EUR), aus Anlass der außerordentlichen Revisionen der klagenden und der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 23. Oktober 2023, GZ 4 R 99/23t-32, mit dem das Urteil des Handelsgerichts Wien vom 27. April 2023, GZ 57 Cg 34/21g-24, bestätigt wurde, den Beschluss gefasst:  Spruch Die gemeinsame Anzeige beider Parteien vom 27. August 2024 über das vereinbarte Ruhen des Verfahrens wird zur Kenntnis genommen.

**False Positives:**

- `Marine GmbH` — partial — pred is substring of gold: `Verlexglanz-Marine GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Verlexglanz-Marine GmbH`(organisation)
- `Andreas Häntsch`(person)
- `Emma Bergner`(person)
- `Cathleen Hofschulte`(person)

**Example 74** (doc_id: `deanon_TRAIN/4Ob69_14x`) (sent_id: `deanon_TRAIN/4Ob69_14x_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Univ.-Prof. Dr. Anita Christöphler, vertreten durch Riesemann Rechtsanwalts GmbH in Graz, gegen die beklagte Partei Husein E‑Commerce GmbH, Dolores Linse, Deutschland, vertreten durch Dr. Peter Schlösser, Rechtsanwalt in Graz, wegen Unterlassung, Beseitigung, Urteilsveröffentlichung, Rechnungslegung und Zahlung (Streitwert im Sicherungsverfahren 50.000 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz vom 5. März 2014, GZ 5 R 20/14x-21, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Commerce GmbH` — partial — pred is substring of gold: `Husein E‑Commerce GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Anita Christöphler`(person)
- `Husein E‑Commerce GmbH`(organisation)
- `Dolores Linse`(person)

**Example 75** (doc_id: `deanon_TRAIN/4Ob69_14x`) (sent_id: `deanon_TRAIN/4Ob69_14x_7`)


der Kläger hatte daran aufgrund eines Werkvertrags mit dieser Gesellschaft führend mitgearbeitet.

**False Positives:**

- `der Kläger hatte daran aufgrund eines Werkvertrags mit dieser Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_TRAIN/4Ob69_14x`) (sent_id: `deanon_TRAIN/4Ob69_14x_23`)


Denn ansonsten hätte die Gesellschaft dieses Recht nach der Wertung des § 26 Satz 2 UrhG verloren.

**False Positives:**

- `Denn ansonsten hätte die Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_TRAIN/4Ob9_20g`) (sent_id: `deanon_TRAIN/4Ob9_20g_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Ing. KzlR MedR Brunhild Syndikus, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1) Böhnstedt+Bittlmeier Verlag GmbH, Wien Traalmon Betriebe, und 2) TraunBau AG, Schneeballenweg 6, 4232 Penzendorf, Österreich, beide vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 11.091,23 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 6. November 2019, GZ 2 R 158/19x-27, mit dem das Urteil des Landesgerichts Linz vom 29. August 2019, GZ 36 Cg 14/18h-22, bestätigt wurde, den Beschluss gefasst:  Spruch I. Das Revisionsverfahren zu 4 Ob 9/20g wird bis zur Vorabentscheidung des Gerichtshofs der Europäischen Union über das Vorabentscheidungsersuchen des Obersten Gerichtshofs vom 17.

**False Positives:**

- `Bittlmeier Verlag GmbH` — partial — pred is substring of gold: `Böhnstedt+Bittlmeier Verlag GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. KzlR MedR Brunhild Syndikus`(person)
- `Böhnstedt+Bittlmeier Verlag GmbH`(organisation)
- `Wien Traalmon Betriebe`(organisation)
- `TraunBau AG`(organisation)
- `Schneeballenweg 6, 4232 Penzendorf, Österreich`(address)

**Example 78** (doc_id: `deanon_TRAIN/5Ob106_20d`) (sent_id: `deanon_TRAIN/5Ob106_20d_28`)


Es führte Erhebungen durch Einholung einer Auskunft der Schule des mj KzlR OSR Josepha Dolecek, Einsicht in die im Rekursverfahren vorgelegten Urkunden und Einvernahme beider Eltern im Zug einer mündlichen Verhandlung durch und traf ergänzende Festellungen zur schulischen Situation des mj StR Jan Danesch und zur Wohnsituation bei den Eltern.

**False Positives:**

- `Es führte Erhebungen durch Einholung einer Auskunft der Schule` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `KzlR OSR Josepha Dolecek`(person)
- `StR Jan Danesch`(person)

**Example 79** (doc_id: `deanon_TRAIN/5Ob106_20d`) (sent_id: `deanon_TRAIN/5Ob106_20d_32`)


Malik Dittmeier sei in seiner neuen Schule „gut angekommen“ und erhalte eine Therapie, Ibrahim Follmar, Bakk. rer. nat. LLB besuche einen Kindergarten in der Nähe des Wohnorts der Mutter.

**False Positives:**

- `Malik Dittmeier sei in seiner neuen Schule` — partial — gold is substring of pred: `Malik Dittmeier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Malik Dittmeier`(person)
- `Ibrahim Follmar, Bakk. rer. nat. LLB`(person)

**Example 80** (doc_id: `deanon_TRAIN/5Ob106_20d`) (sent_id: `deanon_TRAIN/5Ob106_20d_75`)


Dass er in der Schule gesagt habe, er wolle nicht mehr leben, sei mit seiner Mutter abgesprochen gewesen, was ein großer Fehler gewesen sei.

**False Positives:**

- `Dass er in der Schule` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_TRAIN/5Ob146_16f`) (sent_id: `deanon_TRAIN/5Ob146_16f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers Mag. Niels Mueter, vertreten durch Dr. Anke Reisch, Rechtsanwältin in Kitzbühel, gegen die Antragsgegnerin Talgart-Chemie GmbH & Co KG, Tiefe Gasse 5, 2061 Obritz, Österreich, vertreten durch Dr. Lisbeth Lass und Dr. Hans Christian Lass, Rechtsanwälte in Innsbruck, wegen § 52 Abs 1 Z 6 iVm § 20 Abs 3 WEG 2002, infolge des „außerordentlichen“ Revisionsrekurses des Antragstellers gegen den (richtig) Sachbeschluss des Landesgerichts Innsbruck vom 24. Mai 2016, GZ 4 R 128/16a-50, mit dem der Sachbeschluss des Bezirksgerichts Kitzbühel vom 14. März 2016, GZ 4 Msch 7/14x-36, abgeändert wurde, den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.

**False Positives:**

- `Chemie GmbH & Co KG` — positional overlap with gold: `Talgart-Chemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Niels Mueter`(person)
- `Talgart-Chemie GmbH`(organisation)
- `Tiefe Gasse 5, 2061 Obritz, Österreich`(address)

**Example 82** (doc_id: `deanon_TRAIN/5Ob152_12g`) (sent_id: `deanon_TRAIN/5Ob152_12g_29`)


Der JWT sei von der Schule kontaktiert worden, was indiziert habe, dass auch dort die Situation als problematisch und dringlich eingestuft worden sei.

**False Positives:**

- `Der JWT sei von der Schule` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_TRAIN/5Ob152_12g`) (sent_id: `deanon_TRAIN/5Ob152_12g_37`)


Immerhin werde in diversen Medien alljährlich über Kurzschlusshandlungen von Schülern aus Anlass der Zeugnisverteilung berichtet.

**False Positives:**

- `Immerhin werde in diversen Medien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_TRAIN/5Ob152_12g`) (sent_id: `deanon_TRAIN/5Ob152_12g_89`)


7. 2010 hinterließ, wie lange dieses Kontaktgespräch dauerte, ob und gegebenenfalls mit welchem Ergebnis hinterfragt wurde, wo die Minderjährige im Fall ihres angekündigten Fortlaufens unterkommen wollte, und welche Erhebungsmaßnahmen die Mitarbeiter des JWT (zB Rückfrage in der Schule oder bei Mitschülern) vor dem Vorgehen nach § 215 Abs 1 Satz 2 ABGB setzten oder aus welchen Gründen solche unterblieben.

**False Positives:**

- `zB Rückfrage in der Schule` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_6`)


Die Klägerin ist (Minderheits-)Gesellschafterin einer GmbH.

**False Positives:**

- `Gesellschafterin einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_7`)


Sie begehrte die beklagte Rechtsanwaltsgesellschaft zu verpflichten, die Rechtsberatung und/oder Rechtsvertretung dieser GmbH in bestimmt bezeichneten Angelegenheiten zu unterlassen.

**False Positives:**

- `oder Rechtsvertretung dieser GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 87** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_8`)


Die Klägerin begehrte weiters die Feststellung der Haftung der Beklagten für alle Schäden und Nachteile der Klägerin aus oder in Zusammenhang mit der Rechtsberatung und/oder Rechtsvertretung dieser GmbH durch die Beklagte aus und in Zusammenhang mit diesen Angelegenheiten.

**False Positives:**

- `oder Rechtsvertretung dieser GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_23`)


Aber selbst wenn die Beklagte die Gesellschaft aufgrund eines aus der gleichzeitigen Vertretung der Mehrheitsgesellschafterin abgeleiteten Interessenkonflikts nicht vertreten dürfte, könnte die Klägerin als Minderheitsgesellschafterin daraus keine eigenen Unterlassungsansprüche ableiten.

**False Positives:**

- `Aber selbst wenn die Beklagte die Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Bank and Other Org`

**F1:** 0.039 | **Precision:** 0.667 | **Recall:** 0.020  

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
| 0.667 | 0.020 | 0.039 | 21 | 14 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 14 | 7 | 600 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob23_14a`) (sent_id: `deanon_TRAIN/10Ob23_14a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Aurelia von der Lei, geboren am 10. September 1997, in Pflege und Erziehung der Mutter Univ.-Prof.in Marceline Siladji, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Gmunden, 4810 Gmunden, Esplanade 10), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Linz, gegen den Beschluss des Landesgerichts Wels als Rekursgericht vom 15. Jänner 2014, GZ 21 R 298/13t-38, womit der Beschluss des Bezirksgerichts Gmunden vom 18. Oktober 2013, GZ 1 Pu 223/09k-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bezirkshauptmannschaft Gmunden` | `Bezirkshauptmannschaft Gmunden` |

**Missed by this rule (FN):**

- `Aurelia von der Lei` (person)
- `Univ.-Prof.in Marceline Siladji` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob2_14p`) (sent_id: `deanon_TRAIN/10Ob2_14p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Calvin Mützlaff, geboren am Volker Scheffski, Jaden Jurkutaitis, geboren am 8. Dezember 1982 und PhD Karim Trieber, geboren am 11. Januar 1975, in Pflege und Erziehung der Mutter StR Lara Jungnikl, vertreten durch das Land Vorarlberg als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Feldkirch, Schlossgraben 1, 6800 Feldkirch), wegen Gewährung von Unterhaltsvorschuss, über den Revisionsrekurs des Vaters RgR Dipl.-Ing. Quirin Bagemühl, vertreten durch Mag. Hans-Christian Obernberger, Rechtsanwalt in Feldkirch, gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 12. Juli 2011, GZ 3 R 198/11g, 3 R 199/11d, 3 R 200/11a-18, womit die Beschlüsse des Bezirksgerichts Feldkirch vom 18. Mai 2011, GZ 12 Pu 141/11f-4 bis 6, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirkshauptmannschaft Feldkirch` | `Bezirkshauptmannschaft Feldkirch` |

**Missed by this rule (FN):**

- `Calvin Mützlaff` (person)
- `Volker Scheffski` (person)
- `Jaden Jurkutaitis` (person)
- `8. Dezember 1982` (date)
- `PhD Karim Trieber` (person)
- `11. Januar 1975` (date)
- `StR Lara Jungnikl` (person)
- `RgR Dipl.-Ing. Quirin Bagemühl` (person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob30_14f`) (sent_id: `deanon_TRAIN/10Ob30_14f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch und Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der minderjährigen Thobias Altroggen, geboren am 16. März 2008, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Wien-Umgebung, Fachgebiet Jugendwohlfahrt), 3400 Klosterneuburg, Leopoldstraße 21, über das als „Berufung“ bezeichnete Rechtsmittel des Vaters Ignaz Dippert, gegen den Beschluss des Landesgerichts Korneuburg als Rekursgericht vom 25. März 2013, GZ 23 R 30/13v-53, womit der Beschluss des Bezirksgerichts Schwechat vom 27. August 2012, GZ 8 Pu 190/11i-39, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.

| Predicted | Gold |
|---|---|
| `Bezirkshauptmannschaft Wien` | `Bezirkshauptmannschaft Wien` |

**Missed by this rule (FN):**

- `Thobias Altroggen` (person)
- `16. März 2008` (date)
- `Ignaz Dippert` (person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob30_19p`) (sent_id: `deanon_TRAIN/10Ob30_19p_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der minderjährigen Franziska Dreikluft, geboren 3. November 2009, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Melk, 3390 Melk, Abt Karl-Straße 25a) wegen Unterhaltsvorschüssen, über den Revisionsrekurs des Kindes gegen den Beschluss des Landesgerichts St. Pölten als Rekursgericht vom 23. Jänner 2019, GZ 23 R 6/19h-52, mit dem der Beschluss des Bezirksgerichts Melk vom 21. November 2018, GZ 22 Pu 194/16m-42, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bezirkshauptmannschaft Melk` | `Bezirkshauptmannschaft Melk` |

**Missed by this rule (FN):**

- `Franziska Dreikluft` (person)
- `3. November` (date)

**Example 4** (doc_id: `deanon_TRAIN/3Ob26_23d`) (sent_id: `deanon_TRAIN/3Ob26_23d_52`)


Vor diesem Hintergrund sprach der Verfassungsgerichtshof aus, dass durch die Öffentlicherklärung einesin der Natur schon bestehendenWeges durch Verordnung mangels Eigentumserwerbs in gesetzwidriger Weise Gemeingebrauch begründet werde.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 5** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_67`)


In den vonRohregger(aaO) zitierten Entscheidungen bejahen auch der Verfassungsgerichtshof (B 1050/09) und der Verwaltungsgerichtshof (AW 2012/01/0032) die Bedeutung des § 10 RAO und der Vorgängerbestimmung des § 10 RL-BA 2015 für das öffentliche Interesse an dem Verbot der Doppelvertretung, weil es dem Schutz der durch einen Rechtsanwalt vertretenen Parteien diene, seine Einhaltung für das zwischen Rechtsanwalt und Klient bestehende Treueverhältnis für wesentlich erachtet werde und für das allgemeine Bild der Anwaltschaft in der Öffentlichkeit von Bedeutung sei.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 6** (doc_id: `deanon_TRAIN/5Ob31_16v`) (sent_id: `deanon_TRAIN/5Ob31_16v_15`)


Weiters wolle die Rechtssache gemäß Art 89 B-VG dem Verfassungsgerichtshof sowie gemäß Art 267 AEUV dem Europäischen Gerichtshof zur Prüfung vorgelegt werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 7** (doc_id: `deanon_TRAIN/8Ob141_19x`) (sent_id: `deanon_TRAIN/8Ob141_19x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn, den Hofrat Dr. Stefula und die Hofrätin Mag. Wessely-Kristöfel als weitere Richter in der Pflegschaftssache der Antragstellerin mj RgR Linn Neiheiser, geboren am 10. Februar 2008, in Unterhaltsangelegenheiten vertreten durch die Bezirkshauptmannschaft Bregenz, 6901 Bregenz, Bahnhofstraße 41, wegen Unterhalt, über den Revisionsrekurs der Antragstellerin gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 7. August 2019, GZ 2 R 170/19v-33, mit dem der Beschluss des Bezirksgerichts Bregenz vom 4. Juni 2019, GZ 9 Pu 315/19d-28, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bezirkshauptmannschaft Bregenz` | `Bezirkshauptmannschaft Bregenz` |

**Missed by this rule (FN):**

- `RgR Linn Neiheiser` (person)
- `10. Februar` (date)

**Example 8** (doc_id: `deanon_TRAIN/8Ob141_19x`) (sent_id: `deanon_TRAIN/8Ob141_19x_8`)


Die bis zur Rechtskraft dieses Beschlusses fällig gewordenen Beträge sind abzüglich bereits geleisteter Zahlungen binnen 14 Tagen, die hinkünftig fällig werdenden bis zum Ersten eines jeden Monats im Voraus zu Handen des jeweiligen gesetzlichen Vertreters, das ist derzeit die Bezirkshauptmannschaft Bregenz, zu leisten.

| Predicted | Gold |
|---|---|
| `Bezirkshauptmannschaft Bregenz` | `Bezirkshauptmannschaft Bregenz` |

**Example 9** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_29`)


Der Verwaltungsgerichtshof behob allein einen Bescheid, mit dem ein Antrag auf eine solche Aberkennung abgewiesen wurde, wegen Rechtswidrigkeit seines Inhalts (worauf auch der von der Beklagten angerufene Verfassungsgerichtshof in Punkt 2.4.5.3 seines Erkenntnisses ausdrücklich hinwies).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 10** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_31`)


Von dieser Sachlage ausgehend wies der von der Beklagten in diesem Verfahren mittels eines Parteiantrags auf Normenkontrolle angerufene Verfassungsgerichtshof den Antrag, die in BGBl II 2013/120 kundgemachte Verordnung des Bundeseinigungsamtes zur Gänze als verfassungswidrig aufzuheben, mit der Begründung ab, die Bedenken der Beklagten beruhten auf der nicht zutreffenden Prämisse, das Österreichische Rote Kreuz habe seine Kollektivvertragsfähigkeit durch das Erkenntnis des Verwaltungsgerichtshofs 2011/08/0230 „de facto“ verloren (Punkt 2.5 des Erkenntnisses).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofs` (organisation)

**Example 11** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_33`)


4. Die Frage, ob auch ohne Aufhebung der Verordnung BGBl II 2013/120 durch den Verfassungsgerichtshof allein dadurch, dass dem Österreichischen Roten Kreuz die Kollektivvertragsfähigkeit vom Bundeseinigungsamt mittels Bescheids aberkannt wird, die Satzung des Kollektivvertrags ihre Geltung verliert (vgl insbFriedrich, ASoK 2013, 460 f), stellt sich nicht, weil kein solcher Bescheid vorliegt.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 12** (doc_id: `deanon_TRAIN/8ObA72_19z`) (sent_id: `deanon_TRAIN/8ObA72_19z_12`)


2. Dabei konnte sich der Oberste Gerichtshof auf einschlägige Judikatur sowohl des Verfassungsgerichtshofs als auch des EuGH stützen: 2.1 Der Verfassungsgerichtshof hat in seinem Erkenntnis G 450/2015 ua Parteianträge von ÖBB-Bediensteten (unter anderem auch des Klägers) abgewiesen, die § 53a und § 56 Abs 18 bis 24 BundesbahnG je idF BGBl I Nr 64/2015 als verfassungswidrig aufzuheben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verfassungsgerichtshofs` (organisation)

**Example 13** (doc_id: `deanon_TRAIN/9ObA27_15h`) (sent_id: `deanon_TRAIN/9ObA27_15h_7`)


Ihr Antrag auf Gesetzesprüfung hinsichtlich der inzwischen aufgelösten Berufungskommission und eine Eventualbeschwerde seien beim Verfassungsgerichtshof anhängig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/14Os63_17x`) (sent_id: `deanon_TRAIN/14Os63_17x_8`)


1/b durch die zu Punkt a beschriebene Handlung fremde Urkunden, über die sie nicht alleine verfügen durfte, nämlich die in der Plastikhülle befindliche E-Card und ein Jahresticket der ÖBB des Peter Bohnert, mit dem Vorsatz unterdrückt zu verhindern, dass diese Urkunden im Rechtsverkehr zum Beweis eines Rechtes gebraucht werden.

**False Positives:**

- `ÖBB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bohnert`(person)

**Example 1** (doc_id: `deanon_TRAIN/6Ob169_12i`) (sent_id: `deanon_TRAIN/6Ob169_12i_42`)


Wenn das Erstgericht - dem Sachverständigengutachten folgend - zu der Einschätzung gelangte, dass in Anbetracht des Umstands, dass Art und Ausmaß der konkret festgestellten Kontaminierung und ihre Ursache (Lkw-Unfall) bekannt waren, in der Praxis keine sogenannte Vollanalyse durchzuführen gewesen wäre, so ist darin keine vom Obersten Gerichtshof im Interesse der Rechtssicherheit aufzugreifende Fehlbeurteilung zu erblicken, zumal auch die zuständige Bezirkshauptmannschaft in Anbetracht der bekannten Ursache der Kontaminierung nur eine Untersuchung der entsprechenden Kohlenwasserstoffwerte für erforderlich hielt.

**False Positives:**

- `Bezirkshauptmannschaft in` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/7Ob45_24d`) (sent_id: `deanon_TRAIN/7Ob45_24d_41`)


6. 2016 von einer Bezirkshauptmannschaft die Aufforderung gemäß § 103 Abs 2 KFG, binnen 14 Tagen nach Zustellung dieses Schreibens als Zulassungsbesitzer eines Kraftfahrzeugs dessen Lenker bekanntzugeben.

**False Positives:**

- `Bezirkshauptmannschaft die` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/7Ob45_24d`) (sent_id: `deanon_TRAIN/7Ob45_24d_51`)


[7] Mit Schreiben vom 19. 9. 2017 übermittelte der Klagevertreter der Beklagten das Straferkenntnis der Bezirkshauptmannschaft und ersuchte um Deckung für die Erhebung einer Beschwerde und sein Einschreiten in zweiter Instanz.

**False Positives:**

- `Bezirkshauptmannschaft und` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/7Ob45_24d`) (sent_id: `deanon_TRAIN/7Ob45_24d_54`)


[8] Am 19. 9. 2017 gab der Klagevertreter der Bezirkshauptmannschaft in der gegenständlichen Verwaltungsstrafsache die erteilte Vollmacht bekannt und beantragte die Übermittlung einer Aktenkopie.

**False Positives:**

- `Bezirkshauptmannschaft in` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/7Ob45_24d`) (sent_id: `deanon_TRAIN/7Ob45_24d_56`)


9. 2017 eine Beschwerde an das zuständige Landesverwaltungsgericht ein, in der er das Straferkenntnis der Bezirkshauptmannschaft sowohl dem Grunde als auch der Höhe nach anfocht.

**False Positives:**

- `Bezirkshauptmannschaft sowohl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/8ObA72_19z`) (sent_id: `deanon_TRAIN/8ObA72_19z_12`)


2. Dabei konnte sich der Oberste Gerichtshof auf einschlägige Judikatur sowohl des Verfassungsgerichtshofs als auch des EuGH stützen: 2.1 Der Verfassungsgerichtshof hat in seinem Erkenntnis G 450/2015 ua Parteianträge von ÖBB-Bediensteten (unter anderem auch des Klägers) abgewiesen, die § 53a und § 56 Abs 18 bis 24 BundesbahnG je idF BGBl I Nr 64/2015 als verfassungswidrig aufzuheben.

**False Positives:**

- `ÖBB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verfassungsgerichtshofs`(organisation)
- `Verfassungsgerichtshof`(organisation)

</details>

---

## `Constitutional Court`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.011  

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
| 1.000 | 0.011 | 0.023 | 8 | 8 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 0 | 393 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/3Ob26_23d`) (sent_id: `deanon_TRAIN/3Ob26_23d_52`)


Vor diesem Hintergrund sprach der Verfassungsgerichtshof aus, dass durch die Öffentlicherklärung einesin der Natur schon bestehendenWeges durch Verordnung mangels Eigentumserwerbs in gesetzwidriger Weise Gemeingebrauch begründet werde.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 1** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_67`)


In den vonRohregger(aaO) zitierten Entscheidungen bejahen auch der Verfassungsgerichtshof (B 1050/09) und der Verwaltungsgerichtshof (AW 2012/01/0032) die Bedeutung des § 10 RAO und der Vorgängerbestimmung des § 10 RL-BA 2015 für das öffentliche Interesse an dem Verbot der Doppelvertretung, weil es dem Schutz der durch einen Rechtsanwalt vertretenen Parteien diene, seine Einhaltung für das zwischen Rechtsanwalt und Klient bestehende Treueverhältnis für wesentlich erachtet werde und für das allgemeine Bild der Anwaltschaft in der Öffentlichkeit von Bedeutung sei.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 2** (doc_id: `deanon_TRAIN/5Ob31_16v`) (sent_id: `deanon_TRAIN/5Ob31_16v_15`)


Weiters wolle die Rechtssache gemäß Art 89 B-VG dem Verfassungsgerichtshof sowie gemäß Art 267 AEUV dem Europäischen Gerichtshof zur Prüfung vorgelegt werden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 3** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_29`)


Der Verwaltungsgerichtshof behob allein einen Bescheid, mit dem ein Antrag auf eine solche Aberkennung abgewiesen wurde, wegen Rechtswidrigkeit seines Inhalts (worauf auch der von der Beklagten angerufene Verfassungsgerichtshof in Punkt 2.4.5.3 seines Erkenntnisses ausdrücklich hinwies).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 4** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_31`)


Von dieser Sachlage ausgehend wies der von der Beklagten in diesem Verfahren mittels eines Parteiantrags auf Normenkontrolle angerufene Verfassungsgerichtshof den Antrag, die in BGBl II 2013/120 kundgemachte Verordnung des Bundeseinigungsamtes zur Gänze als verfassungswidrig aufzuheben, mit der Begründung ab, die Bedenken der Beklagten beruhten auf der nicht zutreffenden Prämisse, das Österreichische Rote Kreuz habe seine Kollektivvertragsfähigkeit durch das Erkenntnis des Verwaltungsgerichtshofs 2011/08/0230 „de facto“ verloren (Punkt 2.5 des Erkenntnisses).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofs` (organisation)

**Example 5** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_33`)


4. Die Frage, ob auch ohne Aufhebung der Verordnung BGBl II 2013/120 durch den Verfassungsgerichtshof allein dadurch, dass dem Österreichischen Roten Kreuz die Kollektivvertragsfähigkeit vom Bundeseinigungsamt mittels Bescheids aberkannt wird, die Satzung des Kollektivvertrags ihre Geltung verliert (vgl insbFriedrich, ASoK 2013, 460 f), stellt sich nicht, weil kein solcher Bescheid vorliegt.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 6** (doc_id: `deanon_TRAIN/8ObA72_19z`) (sent_id: `deanon_TRAIN/8ObA72_19z_12`)


2. Dabei konnte sich der Oberste Gerichtshof auf einschlägige Judikatur sowohl des Verfassungsgerichtshofs als auch des EuGH stützen: 2.1 Der Verfassungsgerichtshof hat in seinem Erkenntnis G 450/2015 ua Parteianträge von ÖBB-Bediensteten (unter anderem auch des Klägers) abgewiesen, die § 53a und § 56 Abs 18 bis 24 BundesbahnG je idF BGBl I Nr 64/2015 als verfassungswidrig aufzuheben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Verfassungsgerichtshofs` (organisation)

**Example 7** (doc_id: `deanon_TRAIN/9ObA27_15h`) (sent_id: `deanon_TRAIN/9ObA27_15h_7`)


Ihr Antrag auf Gesetzesprüfung hinsichtlich der inzwischen aufgelösten Berufungskommission und eine Eventualbeschwerde seien beim Verfassungsgerichtshof anhängig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

</details>

---

## `Vienna Magistrate`

**F1:** 0.020 | **Precision:** 1.000 | **Recall:** 0.010  

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
| 1.000 | 0.010 | 0.020 | 7 | 7 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 0 | 615 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob11_11g`) (sent_id: `deanon_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Mag. Elmar Janaschek, geboren am 8. Mai 1999, und der minderjährigen VetR Charlotte Eissenmann, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Mag. Elmar Janaschek` (person)
- `VetR Charlotte Eissenmann` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob15_12x`) (sent_id: `deanon_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Egon Luckow, geboren am 1. August 2011, und des mj Priv.-Doz. Samuel Prestle, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Egon Luckow` (person)
- `Priv.-Doz. Samuel Prestle` (person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob25_25m`) (sent_id: `deanon_TRAIN/10Ob25_25m_4`)


Claire Al-Hakim, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Rechtsvertretung Bezirk 21, 1210 Wien, Franz-Jonas-Platz 12), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 22. November 2024, GZ 45 R 496/24k-26, mit dem der Beschluss des Bezirksgerichts Floridsdorf vom 2. August 2024, GZ 16 Pu 19/24a-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Claire Al-Hakim` (person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob3_23y`) (sent_id: `deanon_TRAIN/10Ob3_23y_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Ziegelbauer als Vorsitzenden sowie die Hofrätin Dr. Faber und die Hofräte Mag. Schober, Dr. Thunhart und Dr. Annerl als weitere Richter in der Pflegschaftssache der minderjährigen Juri Bents, geboren 18. Januar 2006, vertreten durch das Land Wien als Träger der Kinder- und Jugendhilfe (Magistrat der Stadt Wien, Rechtsvertretung Bezirke 1, 4 bis 9, 1060 Wien, Amerlingstraße 11), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch die Präsidentin des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 31. Oktober 2022, GZ 43 R 323/22a-17, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 9. Juni 2022, GZ 4 Pu 58/22a-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Juri Bents` (person)
- `18. Januar` (date)

**Example 4** (doc_id: `deanon_TRAIN/10Ob42_15x`) (sent_id: `deanon_TRAIN/10Ob42_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Pflegschaftssache 1. der mj Siegbert Führholzer, MBA, geboren am 30. August 1983 und 2. des mj Gerhard Luttermann, geboren am 11. März 1953, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung Bezirk 22, 1220 Wien, Hirschstettner Straße 19-21/Stiege N), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 10. Dezember 2014, GZ 42 R 343/13x, 42 R 344/13v und 42 R 345/13s-106, womit den Rekursen der Minderjährigen gegen den Beschluss des Bezirksgerichts Donaustadt vom 14. März 2013, GZ 3 Pu 61/12x-40, teilweise Folge gegeben wurde (Pkt 1 des Spruchs), dem Rekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen die Beschlüsse des Bezirksgerichts Donaustadt (jeweils) vom 6. Juni 2013, GZ 3 Pu 61/12x-49 und 3 Pu 61/12x-50, Folge gegeben (Pkt 2a des Spruchs), und aus Anlass des Rekurses die Anträge der Minderjährigen auf Gewährung von Unterhaltsvorschüssen zur Gänze abgewiesen wurden (Pkt 2b des Spruchs), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Siegbert Führholzer, MBA` (person)
- `30. August 1983` (date)
- `Gerhard Luttermann` (person)
- `11. März 1953` (date)

**Example 5** (doc_id: `deanon_TRAIN/3Ob66_11v`) (sent_id: `deanon_TRAIN/3Ob66_11v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Pflegschaftssache der mj Liudmila Sidler, vertreten durch den Jugendwohlfahrtsträger Land Wien, dieser vertreten durch den Magistrat der Stadt Wien, Amt für Jugend und Familie, Wien 2, Karmelitergasse 9, Mutter Liudmila Schlensok, vertreten durch den Sachwalter Dr. Herbert Eisserer, Rechtsanwalt in Wien, Vater Dmitry Schimczik vertreten durch Mag. Wolfgang Maier, Rechtsanwalt in Wien, wegen Übertragung der Obsorge, über den außerordentlichen Revisionsrekurs der Mutter gegen den Beschluss des Landesgerichts St. Pölten als Rekursgericht vom 16. Februar 2011, GZ 23 R 10/11k-171, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Lilienfeld vom 10. November 2010, GZ 1 P 121/09f-S-162, abgeändert wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Sidler` (person)
- `Schlensok` (person)
- `Schimczik` (person)

**Example 6** (doc_id: `deanon_TRAIN/7Ob119_18b`) (sent_id: `deanon_TRAIN/7Ob119_18b_4`)


Matzka als weitere Richter in der Pflegschaftssache der Minderjährigen Silke Wieging, geboren am 20. März 2010, 12. September 1996, vertreten durch das Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung Bezirke 12, 13, 23, 1230 Wien, Rößlergasse 15, Mutter Fiona Wenzlick, Vater Viola Peiniger, vertreten durch Dr. Tassilo Wallentin LL.M, Rechtsanwalt in Wien, wegen Unterhalt, infolge Revisionsrekurses des Vaters gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 8. Mai 2018, GZ 44 R 104/18x-180, womit der Rekurs des Vaters gegen den Beschluss des Bezirksgerichts Meidling vom 25. Jänner 2018, GZ 1 Pu 73/10b-173, teilweise zurückgewiesen und ihm im Übrigen nicht Folge gegeben wurde, den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Silke Wieging` (person)
- `20. März` (date)
- `12. September 1996` (date)
- `Fiona Wenzlick` (person)
- `Viola Peiniger` (person)

</details>

---

## `Magistrate City Pattern`

**F1:** 0.020 | **Precision:** 1.000 | **Recall:** 0.010  

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
| 1.000 | 0.010 | 0.020 | 7 | 7 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 0 | 615 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob11_11g`) (sent_id: `deanon_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Mag. Elmar Janaschek, geboren am 8. Mai 1999, und der minderjährigen VetR Charlotte Eissenmann, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Mag. Elmar Janaschek` (person)
- `VetR Charlotte Eissenmann` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob15_12x`) (sent_id: `deanon_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Egon Luckow, geboren am 1. August 2011, und des mj Priv.-Doz. Samuel Prestle, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Egon Luckow` (person)
- `Priv.-Doz. Samuel Prestle` (person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob25_25m`) (sent_id: `deanon_TRAIN/10Ob25_25m_4`)


Claire Al-Hakim, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Rechtsvertretung Bezirk 21, 1210 Wien, Franz-Jonas-Platz 12), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 22. November 2024, GZ 45 R 496/24k-26, mit dem der Beschluss des Bezirksgerichts Floridsdorf vom 2. August 2024, GZ 16 Pu 19/24a-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Claire Al-Hakim` (person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob3_23y`) (sent_id: `deanon_TRAIN/10Ob3_23y_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Ziegelbauer als Vorsitzenden sowie die Hofrätin Dr. Faber und die Hofräte Mag. Schober, Dr. Thunhart und Dr. Annerl als weitere Richter in der Pflegschaftssache der minderjährigen Juri Bents, geboren 18. Januar 2006, vertreten durch das Land Wien als Träger der Kinder- und Jugendhilfe (Magistrat der Stadt Wien, Rechtsvertretung Bezirke 1, 4 bis 9, 1060 Wien, Amerlingstraße 11), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch die Präsidentin des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 31. Oktober 2022, GZ 43 R 323/22a-17, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 9. Juni 2022, GZ 4 Pu 58/22a-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Juri Bents` (person)
- `18. Januar` (date)

**Example 4** (doc_id: `deanon_TRAIN/10Ob42_15x`) (sent_id: `deanon_TRAIN/10Ob42_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Pflegschaftssache 1. der mj Siegbert Führholzer, MBA, geboren am 30. August 1983 und 2. des mj Gerhard Luttermann, geboren am 11. März 1953, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung Bezirk 22, 1220 Wien, Hirschstettner Straße 19-21/Stiege N), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 10. Dezember 2014, GZ 42 R 343/13x, 42 R 344/13v und 42 R 345/13s-106, womit den Rekursen der Minderjährigen gegen den Beschluss des Bezirksgerichts Donaustadt vom 14. März 2013, GZ 3 Pu 61/12x-40, teilweise Folge gegeben wurde (Pkt 1 des Spruchs), dem Rekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen die Beschlüsse des Bezirksgerichts Donaustadt (jeweils) vom 6. Juni 2013, GZ 3 Pu 61/12x-49 und 3 Pu 61/12x-50, Folge gegeben (Pkt 2a des Spruchs), und aus Anlass des Rekurses die Anträge der Minderjährigen auf Gewährung von Unterhaltsvorschüssen zur Gänze abgewiesen wurden (Pkt 2b des Spruchs), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Siegbert Führholzer, MBA` (person)
- `30. August 1983` (date)
- `Gerhard Luttermann` (person)
- `11. März 1953` (date)

**Example 5** (doc_id: `deanon_TRAIN/3Ob66_11v`) (sent_id: `deanon_TRAIN/3Ob66_11v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Pflegschaftssache der mj Liudmila Sidler, vertreten durch den Jugendwohlfahrtsträger Land Wien, dieser vertreten durch den Magistrat der Stadt Wien, Amt für Jugend und Familie, Wien 2, Karmelitergasse 9, Mutter Liudmila Schlensok, vertreten durch den Sachwalter Dr. Herbert Eisserer, Rechtsanwalt in Wien, Vater Dmitry Schimczik vertreten durch Mag. Wolfgang Maier, Rechtsanwalt in Wien, wegen Übertragung der Obsorge, über den außerordentlichen Revisionsrekurs der Mutter gegen den Beschluss des Landesgerichts St. Pölten als Rekursgericht vom 16. Februar 2011, GZ 23 R 10/11k-171, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Lilienfeld vom 10. November 2010, GZ 1 P 121/09f-S-162, abgeändert wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Sidler` (person)
- `Schlensok` (person)
- `Schimczik` (person)

**Example 6** (doc_id: `deanon_TRAIN/7Ob119_18b`) (sent_id: `deanon_TRAIN/7Ob119_18b_4`)


Matzka als weitere Richter in der Pflegschaftssache der Minderjährigen Silke Wieging, geboren am 20. März 2010, 12. September 1996, vertreten durch das Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung Bezirke 12, 13, 23, 1230 Wien, Rößlergasse 15, Mutter Fiona Wenzlick, Vater Viola Peiniger, vertreten durch Dr. Tassilo Wallentin LL.M, Rechtsanwalt in Wien, wegen Unterhalt, infolge Revisionsrekurses des Vaters gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 8. Mai 2018, GZ 44 R 104/18x-180, womit der Rekurs des Vaters gegen den Beschluss des Bezirksgerichts Meidling vom 25. Jänner 2018, GZ 1 Pu 73/10b-173, teilweise zurückgewiesen und ihm im Übrigen nicht Folge gegeben wurde, den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Silke Wieging` (person)
- `20. März` (date)
- `12. September 1996` (date)
- `Fiona Wenzlick` (person)
- `Viola Peiniger` (person)

</details>

---

## `Administrative Court`

**F1:** 0.017 | **Precision:** 1.000 | **Recall:** 0.009  

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
| 1.000 | 0.009 | 0.017 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 281 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_67`)


In den vonRohregger(aaO) zitierten Entscheidungen bejahen auch der Verfassungsgerichtshof (B 1050/09) und der Verwaltungsgerichtshof (AW 2012/01/0032) die Bedeutung des § 10 RAO und der Vorgängerbestimmung des § 10 RL-BA 2015 für das öffentliche Interesse an dem Verbot der Doppelvertretung, weil es dem Schutz der durch einen Rechtsanwalt vertretenen Parteien diene, seine Einhaltung für das zwischen Rechtsanwalt und Klient bestehende Treueverhältnis für wesentlich erachtet werde und für das allgemeine Bild der Anwaltschaft in der Öffentlichkeit von Bedeutung sei.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `Verfassungsgerichtshof` (organisation)

**Example 1** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_14`)


Der gesatzte Kollektivvertrag des Roten Kreuzes sei unanwendbar, da der Verwaltungsgerichtshof mit Erkenntnis vom 4. 9. 2013, 2011/08/0230 dem Österreichischen Roten Kreuz die Kollektivvertragsfähigkeit „de facto“ aberkannt habe, sodass die Verordnung des Bundeseinigungsamtes „rechtswidrig und ungültig“ sei.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 2** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_28`)


3. Der Verwaltungsgerichtshof hat mit seinem Erkenntnis vom 4. 9. 2013, 2011/08/0230 = DRdA 2014/27 (Felten) = ZAS 2014/13 (Tomandl) dem Österreichischen Roten Kreuz die Kollektivvertragsfähigkeit gemäß § 5 Abs 3 ArbVG nicht aberkannt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 3** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_29`)


Der Verwaltungsgerichtshof behob allein einen Bescheid, mit dem ein Antrag auf eine solche Aberkennung abgewiesen wurde, wegen Rechtswidrigkeit seines Inhalts (worauf auch der von der Beklagten angerufene Verfassungsgerichtshof in Punkt 2.4.5.3 seines Erkenntnisses ausdrücklich hinwies).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `Verfassungsgerichtshof` (organisation)

**Example 4** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_30`)


Weil in der Folge abermals ein abweisender Bescheid erging, der sodann in Rechtskraft erwuchs (siehe erneut in Punkt 2.4.5.3 des VfGH-Erkenntnisses), ist es letzten Endes auch unrichtig, dass der Verwaltungsgerichtshof dem Roten Kreuz „de facto“ die Kollektivvertragsfähigkeit aberkannt hätte.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 5** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_31`)


Von dieser Sachlage ausgehend wies der von der Beklagten in diesem Verfahren mittels eines Parteiantrags auf Normenkontrolle angerufene Verfassungsgerichtshof den Antrag, die in BGBl II 2013/120 kundgemachte Verordnung des Bundeseinigungsamtes zur Gänze als verfassungswidrig aufzuheben, mit der Begründung ab, die Bedenken der Beklagten beruhten auf der nicht zutreffenden Prämisse, das Österreichische Rote Kreuz habe seine Kollektivvertragsfähigkeit durch das Erkenntnis des Verwaltungsgerichtshofs 2011/08/0230 „de facto“ verloren (Punkt 2.5 des Erkenntnisses).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofs` | `Verwaltungsgerichtshofs` |

**Missed by this rule (FN):**

- `Verfassungsgerichtshof` (organisation)

</details>

---

## `Verwaltungsgerichtshof Genitive`

**F1:** 0.014 | **Precision:** 1.000 | **Recall:** 0.007  

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
| 1.000 | 0.007 | 0.014 | 5 | 5 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 0 | 282 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_67`)


In den vonRohregger(aaO) zitierten Entscheidungen bejahen auch der Verfassungsgerichtshof (B 1050/09) und der Verwaltungsgerichtshof (AW 2012/01/0032) die Bedeutung des § 10 RAO und der Vorgängerbestimmung des § 10 RL-BA 2015 für das öffentliche Interesse an dem Verbot der Doppelvertretung, weil es dem Schutz der durch einen Rechtsanwalt vertretenen Parteien diene, seine Einhaltung für das zwischen Rechtsanwalt und Klient bestehende Treueverhältnis für wesentlich erachtet werde und für das allgemeine Bild der Anwaltschaft in der Öffentlichkeit von Bedeutung sei.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `Verfassungsgerichtshof` (organisation)

**Example 1** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_14`)


Der gesatzte Kollektivvertrag des Roten Kreuzes sei unanwendbar, da der Verwaltungsgerichtshof mit Erkenntnis vom 4. 9. 2013, 2011/08/0230 dem Österreichischen Roten Kreuz die Kollektivvertragsfähigkeit „de facto“ aberkannt habe, sodass die Verordnung des Bundeseinigungsamtes „rechtswidrig und ungültig“ sei.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 2** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_28`)


3. Der Verwaltungsgerichtshof hat mit seinem Erkenntnis vom 4. 9. 2013, 2011/08/0230 = DRdA 2014/27 (Felten) = ZAS 2014/13 (Tomandl) dem Österreichischen Roten Kreuz die Kollektivvertragsfähigkeit gemäß § 5 Abs 3 ArbVG nicht aberkannt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 3** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_29`)


Der Verwaltungsgerichtshof behob allein einen Bescheid, mit dem ein Antrag auf eine solche Aberkennung abgewiesen wurde, wegen Rechtswidrigkeit seines Inhalts (worauf auch der von der Beklagten angerufene Verfassungsgerichtshof in Punkt 2.4.5.3 seines Erkenntnisses ausdrücklich hinwies).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `Verfassungsgerichtshof` (organisation)

**Example 4** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_30`)


Weil in der Folge abermals ein abweisender Bescheid erging, der sodann in Rechtskraft erwuchs (siehe erneut in Punkt 2.4.5.3 des VfGH-Erkenntnisses), ist es letzten Endes auch unrichtig, dass der Verwaltungsgerichtshof dem Roten Kreuz „de facto“ die Kollektivvertragsfähigkeit aberkannt hätte.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

</details>

---

## `Federal Ministry of Justice`

**F1:** 0.011 | **Precision:** 1.000 | **Recall:** 0.006  

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
| 1.000 | 0.006 | 0.011 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 528 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/15Os35_19i_15Os36_19m_`) (sent_id: `deanon_TRAIN/15Os35_19i_15Os36_19m__6`)


Eine Bewilligung der Auslieferung gemäß § 34 Abs 1 ARHG ist nach Auskunft des Bundesministeriums für Justiz bislang nicht erfolgt, mit einer solchen wird bis zur Entscheidung über einen allfälligen Erneuerungsantragzugewartetwerden.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Justiz` | `Bundesministeriums für Justiz` |

**Example 1** (doc_id: `deanon_TRAIN/2Ob179_15k`) (sent_id: `deanon_TRAIN/2Ob179_15k_22`)


Das fremde Recht habe aber durch die Mitwirkung der Parteien und die Rechtsauskunft des Bundesministeriums für Justiz nur begrenzt und nicht zu allen relevanten Rechtsfragen ermittelt werden können.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Justiz` | `Bundesministeriums für Justiz` |

**Example 2** (doc_id: `deanon_TRAIN/2Ob179_15k`) (sent_id: `deanon_TRAIN/2Ob179_15k_74`)


Es ist gemäß § 4 Abs 1 IPRG von Amts wegen zu ermitteln, wobei nach der demonstrativen Aufzählung in dieser Bestimmung zulässige Hilfsmittel dafür auch die Mitwirkung der Beteiligten, Auskünfte des Bundesministeriums für Justiz und Sachverständigengutachten sind.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Justiz` | `Bundesministeriums für Justiz` |

**Example 3** (doc_id: `deanon_TRAIN/2Ob179_15k`) (sent_id: `deanon_TRAIN/2Ob179_15k_93`)


Ob das Erstgericht im fortgesetzten Verfahren gemäß der Empfehlung des Bundesministeriums für Justiz doch noch ein Rechtsgutachten einholt oder sich die erforderlichen Kenntnisse auf anderem Weg zu verschaffen versucht, steht in seinem Ermessen und ist nicht entscheidend.

| Predicted | Gold |
|---|---|
| `Bundesministeriums für Justiz` | `Bundesministeriums für Justiz` |

</details>

---

## `Pensionsversicherungsanstalt`

**F1:** 0.003 | **Precision:** 1.000 | **Recall:** 0.001  

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
| 1.000 | 0.001 | 0.003 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 582 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10ObS92_17b`) (sent_id: `deanon_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Dr.in Gerlinde Saltzmann, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Missed by this rule (FN):**

- `Dr.in Gerlinde Saltzmann` (person)
- `Arbeits- und Sozialgericht` (organisation)

</details>

---

## `Hyphenated Company Names`

**F1:** 0.003 | **Precision:** 0.500 | **Recall:** 0.001  

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
| 0.500 | 0.001 | 0.003 | 2 | 1 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 1 | 501 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/8Ob100_19t`) (sent_id: `deanon_TRAIN/8Ob100_19t_4`)


Kraftzorstein-Telekom GmbH Karsten Öllinger, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, und 2. Univ.-Prof.in Rebecca Obermeyr GmbH Klöcklstraße 57, 9111 Berg ob Attendorf, Österreich, vertreten durch Lederer Hoff & Apfelbacher Rechtsanwälte GmbH in Wien, wegen 11.388,49 EUR sA und Feststellung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. Juni 2019, GZ 5 R 60/19h-33, mit dem das Urteil des Handelsgerichts Wien vom 12. März 2019, GZ 51 Cg 62/17z-28, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Kraftzorstein-Telekom GmbH` | `Kraftzorstein-Telekom GmbH` |

**Missed by this rule (FN):**

- `Karsten Öllinger` (person)
- `Eckert Rechtsanwalts GmbH` (organisation)
- `Univ.-Prof.in Rebecca Obermeyr` (person)
- `Klöcklstraße 57, 9111 Berg ob Attendorf, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/1Ob140_14s`) (sent_id: `deanon_TRAIN/1Ob140_14s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer und Mag. Dr. Wurdinger sowie die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft, Meidlinger Hauptstraße 19, 5233 Erlach, Österreich, vertreten durch die Walch & Zehetbauer Rechtsanwälte OG, Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 344.011,19 EUR und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Juni 2014, GZ 4 R 202/13g-54, mit dem das Teilzwischenurteil des Landesgerichts Feldkirch vom 2. August 2013, GZ 8 Cg 143/11y-46, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

**False Positives:**

- `Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft` — partial — gold is substring of pred: `Tracondon Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tracondon Aktiengesellschaft`(organisation)
- `Meidlinger Hauptstraße 19, 5233 Erlach, Österreich`(address)

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
| 0.000 | 0.000 | 0.000 | 7 | 0 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 7 | 567 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/12Os138_19i`) (sent_id: `deanon_TRAIN/12Os138_19i_11`)


VwGH Ro 2014/03/0045).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/12Os71_19m_12Os72_19h_`) (sent_id: `deanon_TRAIN/12Os71_19m_12Os72_19h__10`)


VwGH Ro 2014/03/0045).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/3Ob164_20v`) (sent_id: `deanon_TRAIN/3Ob164_20v_130`)


Gegenteiliges ergibt sich auch nicht aus den im Rechtsmittel zitierten Entscheidungen des VwGH, in denen nur geklärt wurde, dass Rinde nicht als Abfall iSd § 2 Abs 1 AWG gilt.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_79`)


Eine „spontane“ Aufnahme von Fahrgästen ist untersagt (vgl auch VwGH 90/03/0118; 90/03/0041;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_81`)


Die Anordnung, dass die Bestellung (Anforderung eines Fahrzeugs: VwGH Ra 2014/03/0006) beim Gewerbetreibendeneinlangenmuss, verfolgt keinen Selbstzweck.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_95`)


3.Aus den angeführten Grundsätzen folgt, dass eine gleichzeitige Information des Mietwagenunternehmers und des Fahrers über die zu erbringende Beförderungsleistung den gesetzlichen Anforderungen nicht entspricht (vgl auch BGH I ZR 3/16 = GRUR 2017, 743 zur ähnlichen Rechtslage in Deutschland), sowie dass der Umfang der Beförderungsleistung (nach Anfangs- und Endpunkt) im Bestellzeitpunkt (vor der Information des Fahrers) bestimmt sein muss (vgl VwGH Ra 2014/03/0006).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/6Ob161_10k`) (sent_id: `deanon_TRAIN/6Ob161_10k_36`)


Die dem Enteigneten gebührende Entschädigung muss alle durch die Enteignung verursachten vermögensrechtlichen Nachteile erfassen, wobei bei ihrer Bemessung auch auf sämtliche bestehende wirtschaftliche Möglichkeiten bedacht zu nehmen ist (VwGH 28.

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
| 0.000 | 0.000 | 0.000 | 12 | 0 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 12 | 567 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/12Os138_19i`) (sent_id: `deanon_TRAIN/12Os138_19i_10`)


GP 19 ff; vgl VfGH B 181/2014;

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/12Os71_19m_12Os72_19h_`) (sent_id: `deanon_TRAIN/12Os71_19m_12Os72_19h__9`)


GP 19 ff; vgl VfGH B 181/2014;

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/13Os137_17x`) (sent_id: `deanon_TRAIN/13Os137_17x_15`)


Sie wären somit nicht dem Gericht, sondern der Verwaltungsbehörde zuzurechnen und daher – als Akte unmittelbarer verwaltungsbehördlicher Befehls- und Zwangsgewalt – (nicht mit Grundrechtsbeschwerde an den Obersten Gerichtshof, sondern) gemäß Art 130 Abs 1 Z 2 B-VG mit Beschwerde an das zuständige Verwaltungsgericht zu bekämpfen (vgl VfGH 13.

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/17Os2_18z`) (sent_id: `deanon_TRAIN/17Os2_18z_19`)


Davon abgesehen sind Amtsgeschäfte (etwa tatsächliche Verrichtungen) der Hoheitsverwaltung zuzurechnen, wenn sie einen spezifischen Zusammenhang mit Hoheitsakten aufweisen (RIS-Justiz RS0130809;Raschauer, Allgemeines Verwaltungsrecht5Rz 684 ff;Grabenwarter/Holoubek, Verfassungsrecht – Allgemeines Verwaltungsrecht3Rz 736 ff; zur ständigen Rechtsprechung des VfGH grundlegend VfSlg 3.262).

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_91`)


2.4Diese Beurteilung steht mit der Entscheidung des VfGH zu V 52/91 (zu § 53 Abs 3 BO 1986) im Einklang.

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_112`)


Der VfGH hat sich in der Entscheidung zu V 52/91 mit der Rechtmäßigkeit des inhaltsgleichen § 53 Abs 3 BO 1986 im Lichte der Freiheit der Erwerbsausübung bereits befasst und (unter anderem) den auf die Aufhebung dieser Bestimmung gerichteten Individualantrag abgewiesen.

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_113`)


Dazu hat der VfGH ausgeführt, dass es aufgrund der vom Gesetzgeber angeordneten Differenzierung zwischen Taxis und Mietwagen sachlich gerechtfertigt ist, dass die BO 1986 auch in Ansehung des Ortes der Aufnahme von Fahrgästen für Mietwagen eine andere Regelung vorsieht als jene, die für Taxis gilt.

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_114`)


Zudem hat der VfGH ausgesprochen, dass das Gebot des § 53 Abs 3 BO 1986 zur Zielerreichung geeignet ist und keine unadäquate Einschränkung der Erwerbsausübungsfreiheit begründet.

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_115`)


Die Schranken der Freiheit der Erwerbsausübung werden durch die in Rede stehende Anordnung für Mietwagenunternehmer somit nicht überschritten (vgl allgemein auch VfGH G 347/2016 und V 44/2013).

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_120`)


Wie bereits ausgeführt, sind die Verstöße der Mietwagenunternehmer, die von der Beklagten ermöglicht und gefördert werden, nach dem Wortlaut der Norm und der vorliegenden Rechtsprechung vor allem des VfGH eindeutig.

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_144`)


Wenngleich es dem Gesetzgeber im Allgemeinen zusteht, Gesetze auch rückwirkend in Kraft zu setzen, kann im Einzelfall eine Rückwirkung als gegen den Gleichheitsgrundsatz (Art 2 StGG, Art 7 B-VG) verstoßend verfassungswidrig sein, wenn dadurch gegen den Vertrauensgrundsatz verstoßen und/oder die Rechtsstellung der von der Rückwirkung Betroffenen maßgeblich verschlechtert wird (vgl VfGH G 228/89;

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_TRAIN/8ObA2_18d`) (sent_id: `deanon_TRAIN/8ObA2_18d_30`)


Weil in der Folge abermals ein abweisender Bescheid erging, der sodann in Rechtskraft erwuchs (siehe erneut in Punkt 2.4.5.3 des VfGH-Erkenntnisses), ist es letzten Endes auch unrichtig, dass der Verwaltungsgerichtshof dem Roten Kreuz „de facto“ die Kollektivvertragsfähigkeit aberkannt hätte.

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

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
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 588 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10ObS150_17g`) (sent_id: `deanon_TRAIN/10ObS150_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Ing. Christian Stangl-Brachnik, MA BA und Mag. Claudia Gründel (beide aus dem Kreis der Arbeitgeber) als weitere Richter in der Sozialrechtssache der klagenden Partei OStR Esra Jakubait, vertreten durch Dr. Thomas Stampfer und Dr. Christoph Orgler, Rechtsanwälte in Graz, gegen die beklagte Partei Sozialversicherungsanstalt der Bauern, 1031 Wien, Ghegastraße 1, vertreten durch Dr. Michael Stögerer, Rechtsanwalt in Wien, wegen Ausgleichszulage, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2017, GZ 7 Rs 37/17s-11, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. April 2017, GZ 43 Cgs 113/17p-7, teils bestätigt und teils abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Sozialversicherungsanstalt der Bauern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OStR Esra Jakubait`(person)
- `Arbeits- und Sozialgericht`(organisation)

**Example 1** (doc_id: `deanon_TRAIN/10ObS150_17g`) (sent_id: `deanon_TRAIN/10ObS150_17g_8`)


Text Entscheidungsgründe: Der Kläger bezieht von der beklagten Sozialversicherungsanstalt der Bauern eine Erwerbsunfähigkeitspension samt Ausgleichszulage.

**False Positives:**

- `Sozialversicherungsanstalt der Bauern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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
| `organisation` | 0 | 4 | 504 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/1Ob139_18z`) (sent_id: `deanon_TRAIN/1Ob139_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Angelina Töpker Inc., Ronja Straßgschwandtner, vertreten durch Mag. Ralph Kilches, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Lilia Anderßon, als Insolvenzverwalter im Insolvenzverfahren über das Vermögen der Vanek und Eloy Analyse GmbH, Kanischaberg 21, 4742 Kornrödt, Österreich, vertreten durch die Haslinger/Nagele & Partner Rechtsanwälte GmbH, Linz, wegen Feststellung einer Insolvenzforderung (Streitwert 447.352,05 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 28. Juni 2018, GZ 1 R 83/18h-8, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Nagele & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Haslinger/Nagele & Partner Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Angelina Töpker`(person)
- `Ronja Straßgschwandtner`(person)
- `Mag. Lilia Anderßon`(person)
- `Vanek und Eloy Analyse GmbH`(organisation)
- `Kanischaberg 21, 4742 Kornrödt, Österreich`(address)
- `Haslinger/Nagele & Partner Rechtsanwälte GmbH`(organisation)

**Example 1** (doc_id: `deanon_TRAIN/1Ob38_21a`) (sent_id: `deanon_TRAIN/1Ob38_21a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei HR Janet Henken, vertreten durch die Greiml & Horwath Rechtsanwaltspartnerschaft, Graz, gegen die beklagte Partei Elvira Nossal, vertreten durch die Neger/Ulm Rechtsanwälte GmbH, Graz, wegen 6.720 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 3. Juni 2020, GZ 6 R 115/20f-20, mit dem das Urteil des Bezirksgerichts Deutschlandsberg vom 20. März 2020, GZ 11 C 55/19t-16, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Ulm Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `HR Janet Henken`(person)
- `Elvira Nossal`(person)

**Example 2** (doc_id: `deanon_TRAIN/8ObA18_17f`) (sent_id: `deanon_TRAIN/8ObA18_17f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Brenn als weitere Richter sowie die fachkundigen Laienrichter Mag. Dr. Bernhard Gruber und Harald Kohlruss in der Arbeitsrechtssache der klagenden Partei Cassandra Hennel, vertreten durch Freimüller/Obereder/Pilz Rechtsanwält_innen GmbH in Wien, gegen die beklagte Partei SeeTextil AG, Othmar Dempewolf, vertreten durch DLA Piper Weiss-Tessbach Rechtsanwälte GmbH in Wien, wegen Feststellung (Streitwert 282,56 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. November 2016, GZ 7 Ra 90/16f-19, mit dem das Urteil des Arbeits- und Sozialgerichts Wien vom 20. Juli 2016, GZ 33 Cga 50/16p-15, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Tessbach Rechtsanwälte GmbH` — partial — pred is substring of gold: `DLA Piper Weiss-Tessbach Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Cassandra Hennel`(person)
- `SeeTextil AG`(organisation)
- `Othmar Dempewolf`(person)
- `DLA Piper Weiss-Tessbach Rechtsanwälte GmbH`(organisation)
- `Arbeits- und Sozialgerichts`(organisation)

**Example 3** (doc_id: `deanon_TRAIN/8ObA47_20z`) (sent_id: `deanon_TRAIN/8ObA47_20z_4`)


Sabine Duminger (aus dem Kreis der Arbeitgeber) und Robert Hauser (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Ilse Rzeznitzek, vertreten durch Lughofer, Moser & Partner, Rechtsanwälte in Traun, gegen die beklagte Partei Stadt Linz, Alva Kaulfuß, Bakk. iur., vertreten durch Wildmoser/Koch & Partner Rechtsanwälte GmbH in Linz, wegen Feststellung des aufrechten Dienstverhältnisses, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 9. März 2020, GZ 11 Ra 11/20x-18, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Koch & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Wildmoser/Koch & Partner Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ilse Rzeznitzek`(person)
- `Alva Kaulfuß, Bakk. iur.`(person)
- `Wildmoser/Koch & Partner Rechtsanwälte GmbH`(organisation)

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
| 0.000 | 0.000 | 0.000 | 10 | 0 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 10 | 504 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/1Ob139_18z`) (sent_id: `deanon_TRAIN/1Ob139_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Angelina Töpker Inc., Ronja Straßgschwandtner, vertreten durch Mag. Ralph Kilches, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Lilia Anderßon, als Insolvenzverwalter im Insolvenzverfahren über das Vermögen der Vanek und Eloy Analyse GmbH, Kanischaberg 21, 4742 Kornrödt, Österreich, vertreten durch die Haslinger/Nagele & Partner Rechtsanwälte GmbH, Linz, wegen Feststellung einer Insolvenzforderung (Streitwert 447.352,05 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 28. Juni 2018, GZ 1 R 83/18h-8, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Nagele & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Haslinger/Nagele & Partner Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Angelina Töpker`(person)
- `Ronja Straßgschwandtner`(person)
- `Mag. Lilia Anderßon`(person)
- `Vanek und Eloy Analyse GmbH`(organisation)
- `Kanischaberg 21, 4742 Kornrödt, Österreich`(address)
- `Haslinger/Nagele & Partner Rechtsanwälte GmbH`(organisation)

**Example 1** (doc_id: `deanon_TRAIN/1Ob38_21a`) (sent_id: `deanon_TRAIN/1Ob38_21a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei HR Janet Henken, vertreten durch die Greiml & Horwath Rechtsanwaltspartnerschaft, Graz, gegen die beklagte Partei Elvira Nossal, vertreten durch die Neger/Ulm Rechtsanwälte GmbH, Graz, wegen 6.720 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 3. Juni 2020, GZ 6 R 115/20f-20, mit dem das Urteil des Bezirksgerichts Deutschlandsberg vom 20. März 2020, GZ 11 C 55/19t-16, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Ulm Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `HR Janet Henken`(person)
- `Elvira Nossal`(person)

**Example 2** (doc_id: `deanon_TRAIN/3Ob114_14g`) (sent_id: `deanon_TRAIN/3Ob114_14g_58`)


8.Die Vorinstanzen legten nicht die Bilanzen einer Rechtsanwälte GmbH als Bemessungsgrundlage zugrunde, sondern die Gewinnanteile des Beklagten an dieser Rechtsanwälte GmbH; zu einer allfälligen Minderung dieses Einkommens des Beklagten wurde eine Negativfeststellung getroffen, die zu seinen Lasten geht.

**False Positives:**

- `Die Vorinstanzen legten nicht die Bilanzen einer Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/3Ob44_20x`) (sent_id: `deanon_TRAIN/3Ob44_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie die Hofräte Priv.-Doz. Dr. Rassi und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Andreas Clösges, vertreten durch die Eger/Gründl Rechtsanwälte OG in Graz, gegen die beklagte Partei Chemie Valtri GmbH, Niels Niefeldt, vertreten durch Mag. Manuel Fähnrich, Rechtsanwalt in Graz, wegen 34.000 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 31. Jänner 2020, GZ 2 R 168/19x-28, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Gründl Rechtsanwälte OG` — partial — pred is substring of gold: `Eger/Gründl Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Andreas Clösges`(person)
- `Eger/Gründl Rechtsanwälte OG`(organisation)
- `Chemie Valtri GmbH`(organisation)
- `Niels Niefeldt`(person)

**Example 4** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_4`)


Logdercon-Digital, Dänemark, 2. Fengart GmbH, Oberer Weinweg 87, 9020 Klagenfurt, Österreich, beide vertreten durch Graf & Pitkowitz Rechtsanwälte GmbH in Wien, gegen die Beklagten 1. LGR Medien GmbH, OVX Finanzen, 2. Analyse Kelunizor AG, Fahnberg 42, 4100 Großamberg, Österreich, Deutschland, beide vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Gesamtstreitwert 69.500 EUR), über den Ordinationsantrag der Klägerinnen den Beschluss gefasst:  Spruch Dem Ordinationsantrag wird stattgegeben.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Logdercon-Digital`(organisation)
- `Fengart GmbH`(organisation)
- `Oberer Weinweg 87, 9020 Klagenfurt, Österreich`(address)
- `LGR Medien GmbH`(organisation)
- `OVX Finanzen`(organisation)
- `Analyse Kelunizor AG`(organisation)
- `Fahnberg 42, 4100 Großamberg, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)

**Example 5** (doc_id: `deanon_TRAIN/6Ob145_21y`) (sent_id: `deanon_TRAIN/6Ob145_21y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden, den Hofrat Dr. Nowotny, die Hofrätinnen Dr. Hofer-Zeni-Rennhofer und Dr. Faber und den Hofrat Mag. Pertmayr als weitere Richter in der Rechtssache der gefährdeten Partei Dipl.-Ing. Kirstin Iseler, MA Bakk. rer. nat., vertreten durch DORDA Rechtsanwälte GmbH in Wien, wider die Gegnerin der gefährdeten Partei Wilfried Pawell, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, über den Rekurs der gefährdeten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 26. Mai 2021, GZ 47 R 99/21p-19, womit aus Anlass des Rekurses der Gegnerin der gefährdeten Partei die einstweilige Verfügung des Bezirksgerichts Favoriten vom 3. April 2021, GZ 56 C 107/21m-2, als nichtig aufgehoben wurde, den Beschluss gefasst:  Spruch Dem Rekurs wirdFolge gegeben.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. Kirstin Iseler, MA Bakk. rer. nat.`(person)
- `Wilfried Pawell`(person)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)

**Example 6** (doc_id: `deanon_TRAIN/8ObA18_17f`) (sent_id: `deanon_TRAIN/8ObA18_17f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Brenn als weitere Richter sowie die fachkundigen Laienrichter Mag. Dr. Bernhard Gruber und Harald Kohlruss in der Arbeitsrechtssache der klagenden Partei Cassandra Hennel, vertreten durch Freimüller/Obereder/Pilz Rechtsanwält_innen GmbH in Wien, gegen die beklagte Partei SeeTextil AG, Othmar Dempewolf, vertreten durch DLA Piper Weiss-Tessbach Rechtsanwälte GmbH in Wien, wegen Feststellung (Streitwert 282,56 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. November 2016, GZ 7 Ra 90/16f-19, mit dem das Urteil des Arbeits- und Sozialgerichts Wien vom 20. Juli 2016, GZ 33 Cga 50/16p-15, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Tessbach Rechtsanwälte GmbH` — partial — pred is substring of gold: `DLA Piper Weiss-Tessbach Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Cassandra Hennel`(person)
- `SeeTextil AG`(organisation)
- `Othmar Dempewolf`(person)
- `DLA Piper Weiss-Tessbach Rechtsanwälte GmbH`(organisation)
- `Arbeits- und Sozialgerichts`(organisation)

**Example 7** (doc_id: `deanon_TRAIN/8ObA47_20z`) (sent_id: `deanon_TRAIN/8ObA47_20z_4`)


Sabine Duminger (aus dem Kreis der Arbeitgeber) und Robert Hauser (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Ilse Rzeznitzek, vertreten durch Lughofer, Moser & Partner, Rechtsanwälte in Traun, gegen die beklagte Partei Stadt Linz, Alva Kaulfuß, Bakk. iur., vertreten durch Wildmoser/Koch & Partner Rechtsanwälte GmbH in Linz, wegen Feststellung des aufrechten Dienstverhältnisses, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 9. März 2020, GZ 11 Ra 11/20x-18, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Koch & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Wildmoser/Koch & Partner Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ilse Rzeznitzek`(person)
- `Alva Kaulfuß, Bakk. iur.`(person)
- `Wildmoser/Koch & Partner Rechtsanwälte GmbH`(organisation)

**Example 8** (doc_id: `deanon_TRAIN/8ObA71_14w`) (sent_id: `deanon_TRAIN/8ObA71_14w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden und durch die Hofrätin Dr. Tarmann-Prentner, den Hofrat Mag. Ziegelbauer, sowie die fachkundigen Laienrichter Mag. Andreas Mörk und Mag. Matthias Schachner als weitere Richter in der Arbeitsrechtssache der klagenden Partei Karl Höroldt, vertreten durch Forcher-Mayr & Kantner Rechtsanwälte Partnerschaft in Innsbruck, gegen die beklagte Partei Rhein-Lebensmittel Manufaktur AG, David Gideon, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Feststellung (Streitwert: 21.800 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 30. September 2014, GZ 15 Ra 92/14p-40, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Karl Höroldt`(person)
- `Rhein-Lebensmittel Manufaktur AG`(organisation)
- `David Gideon`(person)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)

**Example 9** (doc_id: `deanon_TRAIN/8ObA72_19z`) (sent_id: `deanon_TRAIN/8ObA72_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Wessely-Kristöfel als weitere Richter sowie die fachkundigen Laienrichter Johannes Püller (aus dem Kreis der Arbeitgeber) und Mag. Michael Puhm (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Hermine Thom, vertreten durch Dr. Markus Orgler, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Mur Brucktridon AG, Dipl.-Ing. Griselda Lamberty, Bakk. rer. nat., vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 4.200,83 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 17. Oktober 2019, GZ 13 Ra 41/15z-30, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hermine Thom`(person)
- `Mur Brucktridon AG`(organisation)
- `Dipl.-Ing. Griselda Lamberty, Bakk. rer. nat.`(person)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

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
| `organisation` | 0 | 10 | 597 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt, aus denen Erträge erzielt werden sollen.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — partial — gold is substring of pred: `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`(organisation)

**Example 1** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_5`)


Text Begründung: Der Kläger erwarb als Verbraucher im Juni 2003 über Vermittlung eines selbständigen Vermögensberaters Kommanditanteile an der Bestelmeyer+Keßelheim Software GmbH & Co KG im Nominale von 17.000 EUR zuzüglich 850 EUR Agio.

**False Positives:**

- `Keßelheim Software GmbH & Co KG` — positional overlap with gold: `Bestelmeyer+Keßelheim Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bestelmeyer+Keßelheim Software GmbH`(organisation)

**Example 2** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — partial — gold is substring of pred: `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH`(organisation)

**Example 3** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_6`)


Text Gründe: Mit dem angefochtenen Urteil wurden Bernhard Beinicke und Norbert Wentzlick von der wider sie erhobenen Anklage, sie hätten am 7. Februar 2009 in Churer Straße 54, 9064 St. Michael ob der Gurk, Österreich /Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der DKZ Solar GesmbH & Co KG, Susanne Schueßler, durch die Vorgabe, die HochForschung GmbH sei eine zahlungsfähige Leasingnehmerin, somit durch Täuschung über Tatsachen, zum Abschluss eines Leasingvertrags über ein Rennfahrzeug für die Dauer von 24 Monaten zu einem monatlichen Entgelt von 10.698,10 Euro, somit zu einer Handlung verleitet, welche die Stadt-Sanitär Services GesmbH & Co KG in einem 50.000 Euro übersteigenden Betrag von insgesamt 235.358,20 Euro am Vermögen schädigte, gemäß § 259 Z 3 StPO (verfehlt auch von der rechtlichen Kategorie; vglLendl, WK-StPO § 259 Rz 1) freigesprochen.

**False Positives:**

- `Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der DKZ Solar GesmbH & Co KG` — partial — gold is substring of pred: `DKZ Solar GesmbH`
- `Sanitär Services GesmbH & Co KG` — positional overlap with gold: `Stadt-Sanitär Services GesmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bernhard Beinicke`(person)
- `Norbert Wentzlick`(person)
- `Churer Straße 54, 9064 St. Michael ob der Gurk, Österreich`(address)
- `DKZ Solar GesmbH`(organisation)
- `Susanne Schueßler`(person)
- `HochForschung GmbH`(organisation)
- `Stadt-Sanitär Services GesmbH`(organisation)

**Example 4** (doc_id: `deanon_TRAIN/2Ob99_18z`) (sent_id: `deanon_TRAIN/2Ob99_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden, den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé sowie die Hofräte Dr. Nowotny und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Stadt-Textil GmbH & Co KG, Kreuzlandstraße 52, 9462 Kalchberg, Österreich, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Kazlowski + Röttjer Automotive GmbH, Clarissa Lenschau, vertreten durch Keschmann Rechtsanwalts-GmbH in Wien, sowie die Nebenintervenientinnen 1. Ost-Chemie GmbH, M.-Klieber-Gasse 22, 3611 Himberg, Österreich, vertreten durch Dr. Dirk Just, Rechtsanwalt in Wien, 2.

**False Positives:**

- `Textil GmbH & Co KG` — positional overlap with gold: `Stadt-Textil GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stadt-Textil GmbH`(organisation)
- `Kreuzlandstraße 52, 9462 Kalchberg, Österreich`(address)
- `Kazlowski + Röttjer Automotive GmbH`(organisation)
- `Clarissa Lenschau`(person)
- `Ost-Chemie GmbH`(organisation)
- `M.-Klieber-Gasse 22, 3611 Himberg, Österreich`(address)

**Example 5** (doc_id: `deanon_TRAIN/3Ob114_14g`) (sent_id: `deanon_TRAIN/3Ob114_14g_4`)


KzlR Hartmut Raffenberg KG und 2.

**False Positives:**

- `KzlR Hartmut Raffenberg KG` — partial — gold is substring of pred: `KzlR Hartmut Raffenberg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KzlR Hartmut Raffenberg`(person)

**Example 6** (doc_id: `deanon_TRAIN/3Ob114_14g`) (sent_id: `deanon_TRAIN/3Ob114_14g_6`)


Begründung:  Rechtliche Beurteilung Die Erstklägerin (eine Rechtsanwalts KG), der Zweitkläger (deren Komplementär) und die Mutter des Zweitklägers (in Hinkunft: Pensionsberechtigte) führten als Kläger und Widerbeklagte ein Schiedsverfahren gegen den (hier) Beklagten (als ausgeschiedenen Komplementär) als Beklagten und Widerkläger, das mit einem Schiedsspruch vom 2. Mai 2011 endete.

**False Positives:**

- `eine Rechtsanwalts KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_5`)


Klingenbeil Versand GmbH & Co KG, 2.

**False Positives:**

- `Klingenbeil Versand GmbH & Co KG` — partial — gold is substring of pred: `Klingenbeil Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Klingenbeil Versand GmbH`(organisation)

**Example 8** (doc_id: `deanon_TRAIN/5Ob146_16f`) (sent_id: `deanon_TRAIN/5Ob146_16f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers Mag. Niels Mueter, vertreten durch Dr. Anke Reisch, Rechtsanwältin in Kitzbühel, gegen die Antragsgegnerin Talgart-Chemie GmbH & Co KG, Tiefe Gasse 5, 2061 Obritz, Österreich, vertreten durch Dr. Lisbeth Lass und Dr. Hans Christian Lass, Rechtsanwälte in Innsbruck, wegen § 52 Abs 1 Z 6 iVm § 20 Abs 3 WEG 2002, infolge des „außerordentlichen“ Revisionsrekurses des Antragstellers gegen den (richtig) Sachbeschluss des Landesgerichts Innsbruck vom 24. Mai 2016, GZ 4 R 128/16a-50, mit dem der Sachbeschluss des Bezirksgerichts Kitzbühel vom 14. März 2016, GZ 4 Msch 7/14x-36, abgeändert wurde, den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.

**False Positives:**

- `Chemie GmbH & Co KG` — positional overlap with gold: `Talgart-Chemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Niels Mueter`(person)
- `Talgart-Chemie GmbH`(organisation)
- `Tiefe Gasse 5, 2061 Obritz, Österreich`(address)

</details>

---

## `Gesellschaft mbH Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 355 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/4Ob19_10p`) (sent_id: `deanon_TRAIN/4Ob19_10p_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Traun-Sanitär gesellschaft mbH,*****, vertreten durch Prof. Haslinger & Partner, Rechtsanwälte in Linz, gegen die beklagte Partei NWJ KI Dienstleistungen AG,*****, vertreten durch Rechtsanwälte Konrad & Schröttner OG in Graz, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 65.000 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 25. November 2009, GZ 6 R 169/09h-37, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Sanitär gesellschaft mbH` — partial — pred is substring of gold: `Traun-Sanitär gesellschaft mbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Traun-Sanitär gesellschaft mbH`(organisation)
- `NWJ KI Dienstleistungen AG`(organisation)

**Example 1** (doc_id: `deanon_TRAIN/9ObA96_13b`) (sent_id: `deanon_TRAIN/9ObA96_13b_4`)


Brigitte Augustin und Mag. Andreas Hach als weitere Richter in der Arbeitsrechtssache der klagenden Partei DI Anita Crämer, vertreten durch Dr. Gerhard Hiebler und Dr. Gerd Grebenjak, Rechtsanwälte in Leoben, gegen die beklagte Partei, GQG E‑Commerce Gesellschaft mbH, Franz-Cäsar-Weg 5, 4115 Gumpesberg, Österreich, vertreten durch Siemer-Siegel-Füreder & Partner, Rechtsanwälte in Wien, wegen Feststellung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 18. April 2013, GZ 6 Ra 18/13h-10, mit dem der Berufung der beklagten Partei gegen das Urteil des Landesgerichts Leoben als Arbeits- und Sozialgericht vom 7. November 2012, GZ 23 Cga 115/12x-6, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Commerce Gesellschaft mbH` — partial — pred is substring of gold: `GQG E‑Commerce Gesellschaft mbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DI Anita Crämer`(person)
- `GQG E‑Commerce Gesellschaft mbH`(organisation)
- `Franz-Cäsar-Weg 5, 4115 Gumpesberg, Österreich`(address)
- `Arbeits- und Sozialgericht`(organisation)

</details>

---

</details>

---

