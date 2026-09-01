# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-08-30T11:15:59.792913

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-08-28_v14/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 500 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 400 |
| Validation documents | 100 |
| Test documents | 477 |
| Train sentences | 6773 |
| Validation sentences | 1648 |
| Test sentences | 22727 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 30 |
| Max samples in prompt | 150 |
| Refinement iterations | 6 |
| Seed | 42 |
| Agentic | True |
| Enable Critic | True |
| Enable Prune | False |
| Critic Interval | 10 |
| Audit Interval | 0 |
| Use GREX | True |
| Format | regex |
| Synthesis strategy | bulk |
| Sampling strategy | balanced |
| Batch size | 30 |
| Refine per batch | 1 |
| Manually annotated examples | 0 |
| First batch with manual data | None |

</details>

---

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 90.2% |
| True Positives | 544 |
| False Positives | 557 |
| False Negatives | 3470 |
| Total Gold Entities | 4014 |
| Micro Precision | 49.4% |
| Micro Recall | 13.6% |
| Micro F1 | 21.3% |
| Macro F1 | 21.3% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Wiener Gebietskrankenkasse` | 0.2% | 100.0% | 0.1% | 4 | 4 | 0 |
| `Magistrat der Stadt Wien Full` | 0.4% | 100.0% | 0.2% | 8 | 8 | 0 |
| `Bezirksgericht City` | 5.1% | 89.7% | 2.6% | 117 | 105 | 12 |
| `BFG and VwGH Acronyms` | 11.9% | 81.4% | 6.4% | 317 | 258 | 59 |
| `ÖBB Acronym` | 0.4% | 69.2% | 0.2% | 13 | 9 | 4 |
| `KG Company Names` | 0.5% | 36.7% | 0.3% | 30 | 11 | 19 |
| `GmbH Company Names` | 5.9% | 29.2% | 3.3% | 449 | 131 | 318 |
| `AG Company Names` | 0.9% | 20.5% | 0.4% | 88 | 18 | 70 |
| `German Federal Court of Finance Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `AMS Acronym` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Pensionsversicherungsanstalt` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `ÖGK Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Common Legal Acronyms` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Company with Fa. Prefix` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `University of Vienna` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Federal Ministry of Interior` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesamt für Soziales` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `OECD` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `EU Court` | 0.0% | 0.0% | 0.0% | 8 | 0 | 8 |
| `Landespolizeidirektion Generic` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Verwaltungsgericht City` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `FAÖ Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesamtes für Soziales` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `COFAG Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BHAG Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BM für Finanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `I AG Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wiener Gemeinderates` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesministeriums für Finanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesministers für Arbeit` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SK Telecom Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesfinanzgerichts Genitive` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Amt für Betrugsbekämpfung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt für Großbetriebe` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Landesgericht with City` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Alpen-KI GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Treuhand-Union Villach` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Court Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FB + KG Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Magistrat der Stadt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Frontex Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesministerium für Finanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wiener Linien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wiener Gemeindebezirk` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Rentenversicherung Bund` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Deutschen Rentenversicherung Bund` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `WGKK Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesministerium für Inneres` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mur Steinstein Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Stadt Wien Partial` | 0.0% | 0.0% | 0.0% | 24 | 0 | 24 |
| `Wirtschaftsuniversität Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `AGL Specific Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Verlag Derkel GmbH Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Verwiltal-Pharma GmbH Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Central Liaison Office` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Europäische Gerichtshof` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Steinchen und Pflügler Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Code Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Full Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Zollamt Entity` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Finanzamt Standalone` | 0.0% | 0.0% | 0.0% | 10 | 0 | 10 |
| `Finanzpolizei Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesfinanzgericht (BFG) Suffix` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BFG Acronym Standalone` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Fa. Company Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Landesgerichtes with City` | 0.0% | 0.0% | 0.0% | 24 | 0 | 24 |
| `Specific GmbH Company Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `EASO Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamts Österreich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesfinanzgericht Full Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `KG Company Names Refined` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `AG Company Names Refined` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Wiener Gebietskrankenkasse` 

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `fc09f5c8`  
**Description:**
Matches the specific organization 'Wiener Gebietskrankenkasse' which was missing from the rules.

**Content:**
```
\bWiener\s+Gebietskrankenkasse\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 3512 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, den Hofrat Dr. Fellinger und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter KR Hermann Furtner (aus dem Kreis der Arbeitgeber) und AR Angelika Neuhauser (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Birgit Jaros, vertreten durch Dr. Herbert Pochieser, Rechtsanwalt in Wien, gegen die beklagte Partei Wiener Gebietskrankenkasse, 1100 Wien, Wienerbergstraße 15-19, vertreten durch Dr. Heinz Edelmann, Rechtsanwalt in Wien, wegen Kostenerstattung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 11. September 2012, GZ 8 Rs 49/12b-28, womit das Urteil des Arbeits- und Sozialgerichts Wien vom 21. November 2011, GZ 17 Cgs 120/10a-24, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Wiener Gebietskrankenkasse` | `Wiener Gebietskrankenkasse` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Fichtenau` (person)
- `KR Hermann Furtner` (person)
- `AR Angelika Neuhauser` (person)
- `Birgit Jaros` (person)
- `Dr. Herbert Pochieser` (person)
- `Dr. Heinz Edelmann` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/3Ob99_10w`) (sent_id: `deanon_260716_TRAIN/3Ob99_10w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Senatspräsidenten Hon.-Prof. Dr. Sailer, den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und den Hofrat Dr. Jensik als weitere Richter in der Rechtssache der klagenden Partei Dr. Johannes Müller, Rechtsanwalt, Wien 3, Ditscheinergasse 2, als Masseverwalter im Konkurs der Wald-Event GmbH, gegen die beklagte Partei Wiener Gebietskrankenkasse, Wien 10, Wienerbergstraße 15-19, vertreten durch Preslmayr Rechtsanwälte OG in Wien, und der Nebenintervenienten auf der Seite der beklagten Partei 1.)

| Predicted | Gold |
|---|---|
| `Wiener Gebietskrankenkasse` | `Wiener Gebietskrankenkasse` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Prückner` (person)
- `Hon.-Prof. Dr. Sailer` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Lovrek` (person)
- `Dr. Jensik` (person)
- `Dr. Johannes Müller` (person)
- `Wald-Event GmbH` (organisation)
- `Preslmayr Rechtsanwälte OG` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/3Ob99_10w`) (sent_id: `deanon_260716_TRAIN/3Ob99_10w_22`)


7. den offenen Saldo bei der Wiener Gebietskrankenkasse im Ausmaß von EUR 86.000 (nach Ausdehnung des Zahlungsziels) zu bezahlen.

| Predicted | Gold |
|---|---|
| `Wiener Gebietskrankenkasse` | `Wiener Gebietskrankenkasse` |

**Example 3** (doc_id: `deanon_260716_TRAIN/3Ob99_10w`) (sent_id: `deanon_260716_TRAIN/3Ob99_10w_24`)


Die Folgen einer Nichtbezahlung des offenen Saldos bei der Wiener Gebietskrankenkasse sind Ihnen bekannt.

| Predicted | Gold |
|---|---|
| `Wiener Gebietskrankenkasse` | `Wiener Gebietskrankenkasse` |

</details>

---

## `Magistrat der Stadt Wien Full` 

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `82e5575a`  
**Description:**
Matches 'Magistrat der Stadt Wien' including optional department info like 'Magistratsabteilung 67', ensuring full capture and preventing partial 'Stadt Wien' matches.

**Content:**
```
\bMagistrat(?:es)?\s+der\s+Stadt\s+Wien(?:\s*,\s*Magistratsabteilung\s+\d+)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 8 | 8 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 0 | 3858 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Bartholomäus Junghahn, geboren am 8. Mai 1999, und der minderjährigen HR Sophie Elefteriadis, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Bartholomäus Junghahn` (person)
- `HR Sophie Elefteriadis` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Leander Lindlahr, geboren am 1. August 2011, und des mj Yussuf Prussog, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Leander Lindlahr` (person)
- `Yussuf Prussog` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der minderjährigen Annabelle Thurnher, geboren am 24. Juni 2001, vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung, Bezirk 10, 1100 Wien, Van der Nüll-Gasse 20), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 17. September 2009, GZ 44 R 454/09d-38, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Favoriten vom 16. Juni 2009, GZ 40 P 36/08f-U-26, teilweise abgeändert wurde, den B e s c h l u s s gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Annabelle Thurnher` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_17`)


5. 2009 auch dem „Magistrat der Stadt Wien MA 11, AJF-R Bezirk 10, Van der Nüll-Gasse 20, 1100 Wien“ als gesetzlichen Vertreter der Minderjährigen zugestellt und von einem Postbevollmächtigten des Jugendamts übernommen wurde.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 4** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_52`)


Nach dem im Akt befindlichen Rückschein wurde der Beschluss über die pflegschaftsgerichtliche Genehmigung des Scheidungsvergleichs richtigerweise dem „Magistrat der Stadt Wien MA 11, AJF-R Bezirk 10, Van der Nüll-Gasse 20, 1100 Wien“ als gesetzlichen Vertreter der Minderjährigen zugestellt und von einem Postbevollmächtigten dieser Dienststelle übernommen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 5** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Ziegelbauer als Vorsitzenden sowie die Hofrätin Dr. Faber und die Hofräte Mag. Schober, Dr. Thunhart und Dr. Annerl als weitere Richter in der Pflegschaftssache der minderjährigen Meinrad Bruhnsen, geboren 30. Januar 2006, vertreten durch das Land Wien als Träger der Kinder- und Jugendhilfe (Magistrat der Stadt Wien, Rechtsvertretung Bezirke 1, 4 bis 9, 1060 Wien, Amerlingstraße 11), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch die Präsidentin des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 31. Oktober 2022, GZ 43 R 323/22a-17, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 9. Juni 2022, GZ 4 Pu 58/22a-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Mag. Schober` (person)
- `Dr. Thunhart` (person)
- `Dr. Annerl` (person)
- `Meinrad Bruhnsen` (person)
- `30. Januar` (date)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Innere Stadt Wien` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Pflegschaftssache 1. der mj Emma Mittelstaedt, geboren am 21. Mai 2025 und 2. des mj Milena Roesche, geboren am 25. Juni 1957, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung Bezirk 22, 1220 Wien, Hirschstettner Straße 19-21/Stiege N), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 10. Dezember 2014, GZ 42 R 343/13x, 42 R 344/13v und 42 R 345/13s-106, womit den Rekursen der Minderjährigen gegen den Beschluss des Bezirksgerichts Donaustadt vom 14. März 2013, GZ 3 Pu 61/12x-40, teilweise Folge gegeben wurde (Pkt 1 des Spruchs), dem Rekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen die Beschlüsse des Bezirksgerichts Donaustadt (jeweils) vom 6. Juni 2013, GZ 3 Pu 61/12x-49 und 3 Pu 61/12x-50, Folge gegeben (Pkt 2a des Spruchs), und aus Anlass des Rekurses die Anträge der Minderjährigen auf Gewährung von Unterhaltsvorschüssen zur Gänze abgewiesen wurden (Pkt 2b des Spruchs), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Korn` (person)
- `Emma Mittelstaedt` (person)
- `21. Mai 2025` (date)
- `Milena Roesche` (person)
- `25. Juni 1957` (date)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/7Ob119_18b`) (sent_id: `deanon_260716_TRAIN/7Ob119_18b_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und durch die Hofrätinnen und Hofräte Dr. Höllwerth, Dr. E. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Pflegschaftssache der Minderjährigen Geraldine Moßmann, geboren am 7. November 2010, 26. Mai 2013, vertreten durch das Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung Bezirke 12, 13, 23, 1230 Wien, Rößlergasse 15, Mutter Pia Birkenkötter, Vater Lea Schameitat, vertreten durch Dr. Tassilo Wallentin LL.M, Rechtsanwalt in Wien, wegen Unterhalt, infolge Revisionsrekurses des Vaters gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 8. Mai 2018, GZ 44 R 104/18x-180, womit der Rekurs des Vaters gegen den Beschluss des Bezirksgerichts Meidling vom 25. Jänner 2018, GZ 1 Pu 73/10b-173, teilweise zurückgewiesen und ihm im Übrigen nicht Folge gegeben wurde, den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.  Text Begründung: Der Vater verpflichtete sich zunächst mit Vergleich des Bezirksgerichts Meidling vom 1. 10. 2010, GZ 1 C 9/10k-9, zu einer monatlichen Unterhaltsleistung von 180 EUR.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Dr. Höllwerth` (person)
- `Dr. E. Solé` (person)
- `Mag. Malesich` (person)
- `MMag. Matzka` (person)
- `Geraldine Moßmann` (person)
- `7. November` (date)
- `26. Mai 2013` (date)
- `Pia Birkenkötter` (person)
- `Lea Schameitat` (person)
- `Dr. Tassilo Wallentin` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Meidling` (organisation)
- `Bezirksgerichts Meidling` (organisation)

</details>

---

## `Bezirksgericht City` 🏆

**F1:** 0.051 | **Precision:** 0.897 | **Recall:** 0.026  

**Format:** `regex`  
**Rule ID:** `4766d729`  
**Description:**
Matches 'Bezirksgericht' followed by a city name or identifier (e.g., 'Bezirksgericht O', 'Bezirksgericht Wien').

**Content:**
```
\bBezirksgericht\s+[A-Z][a-zA-Zäöüß\-]+(?:\s+[A-Z][a-zA-Zäöüß\-]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.897 | 0.026 | 0.051 | 117 | 105 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 105 | 12 | 3908 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Jason Langeloh, vertreten durch die Mag. Martin Rützler, Rechtsanwalt in Dornbirn, gegen die beklagte Partei, Selma Einoeder, vertreten durch Mag. Alexander Gerngross und Mag. Klaus Köck, Rechtsanwälte in Premstätten bei Graz, wegen 6.795,66 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 223 C 1313/24w des Bezirksgerichts Graz-Ost den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an das Bezirksgericht Dornbirn wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Dornbirn` | `Bezirksgericht Dornbirn` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Mag. Schober` (person)
- `Dr. Vollmaier` (person)
- `Jason Langeloh` (person)
- `Mag. Martin Rützler` (person)
- `Selma Einoeder` (person)
- `Mag. Alexander Gerngross` (person)
- `Mag. Klaus Köck` (person)
- `Bezirksgerichts Graz-Ost` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_8`)


[3] Mit Antrag vom 21. 2. 2025 beantragte der Kläger – noch vor der vorbereitenden Tagsatzung – die Delegierung der Rechtssache an das Bezirksgericht Dornbirn, weil nicht nur er sowie das Unternehmen, in dessen Kfz-Werkstatt das Fahrzeug repariert worden sei, und dem er im Verfahren den Streit verkündet habe, sondern auch die von ihm in großer Zahl namhaft gemachten Zeugen ihren (Wohn-)Sitz in Vorarlberg hätten.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Dornbirn` | `Bezirksgericht Dornbirn` |

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_10`)


Die Weiterführung des Verfahrens vor dem Bezirksgericht Graz-Ost wäre daher mit einem erheblichen Mehraufwand verbunden bzw müsste allenfalls praktisch das gesamte Beweisverfahren im Wege der Videokonferenz durchgeführt werden.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz-Ost` | `Bezirksgericht Graz-Ost` |

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_4`)


Text Begründung: Die Klägerin begehrt mit der am 4. 8. 2017 beim Bezirksgericht Steyr eingebrachten Klage von dem in der Schweiz ansässigen Beklagten 4.660 EUR sA.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Steyr` | `Bezirksgericht Steyr` |

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_11`)


2018 erklärte sich dasBezirksgericht Steyrfür örtlich unzuständig und überwies (antragsgemäß) die Rechtssache an das nicht offenbar unzuständige Bezirksgericht Salzburg.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_22`)


Da das Bezirksgericht Salzburg die internationale Zuständigkeit Österreichs zur Erledigung der Klage rechtskräftig verneint hat, kann eine Ordination nicht mehr erfolgreich auf § 28 Abs 1 Z 1 JN gestützt werden.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Schramm als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Florens Drehkopf, LLB, geboren am 16. Dezember 1952, AZ 7 P 203/15g des Bezirksgerichts Mödling, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Mödling zurückgestellt.  Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |
| `Bezirksgericht Judenburg` | `Bezirksgericht Judenburg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schramm` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Florens Drehkopf, LLB` (person)
- `16. Dezember 1952` (date)
- `Bezirksgerichts Mödling` (organisation)
- `Bezirksgerichts Judenburg` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_4`)


Das Bezirksgericht Mödling legte den Akt zur Entscheidung gemäß § 111 Abs 2 JN dem Obersten Gerichtshof vor (ON 8), ohne den Übertragungsbeschluss an die Parteien zuzustellen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Missed by this rule (FN):**

- `Obersten Gerichtshof` (organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Marlene Friss, Russische Föderation, gegen die verpflichtete Partei WestTelekom GmbH, Rehwald 11, 4723 Fronberg, Österreich, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innere Stadt Wien` | `Bezirksgericht Innere Stadt Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Marlene Friss` (person)
- `WestTelekom GmbH` (organisation)
- `Rehwald 11, 4723 Fronberg, Österreich` (address)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_11`)


Der Antrag war daher dem Bezirksgericht Innere Stadt Wien, in dessen Sprengel die verpflichtete Partei nach dem Antragsvorbringen ihren Sitz hat, gemäß § 44 JN zu überweisen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innere Stadt Wien` | `Bezirksgericht Innere Stadt Wien` |

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und die Hofräte Dr. Fellinger und Dr. Schramm als weitere Richter in der Pflegschaftssache der Minderjährigen Gerhard Lohrmann, geboren am 10. August 1983, und Veit Künneken, geboren am 31. Mai 1967, AZ 2 PS 117/09t des Bezirksgerichts Feldkirchen, infolge Vorlage zur Genehmigung der Übertragung gemäß § 111 JN an das Bezirksgericht Neunkirchen, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Übertragung der Zuständigkeit zur Besorgung dieser Pflegschaftssache an das Bezirksgericht Neunkirchen wird genehmigt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Gerhard Lohrmann` (person)
- `10. August 1983` (date)
- `Veit Künneken` (person)
- `31. Mai 1967` (date)
- `Bezirksgerichts Feldkirchen` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_4`)


Begründung:  Rechtliche Beurteilung Das bisher zuständige Bezirksgericht Feldkirchen übertrug mit seinem - den Verfahrensbeteiligten zugestellten und nicht bekämpften - Beschluss vom 7. 10.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Feldkirchen` | `Bezirksgericht Feldkirchen` |

**Example 12** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_5`)


2009 die Zuständigkeit zur Führung der Pflegschaftssache an das Bezirksgericht Neunkirchen, weil die beiden Minderjährigen und ihre obsorgeberechtigte Mutter, in deren Haushalt sich die Kinder nach dem pflegschaftsgerichtlich genehmigten Scheidungsvergleich hauptsächlich aufhalten sollen, sich nunmehr ständig im Sprengel dieses Gerichts aufhielten.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Example 13** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_6`)


Das Bezirksgericht Neunkirchen verweigerte die Übernahme der Zuständigkeit, weil das übertragende Gericht den Antrag vom 24.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Example 14** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_7`)


8. 2009 schon zu bearbeiten begonnen habe, ihm die verfahrensbeteiligten Personen bekannt, dem Bezirksgericht Neunkirchen aber gänzlich unbekannt seien.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Neunkirchen` | `Bezirksgericht Neunkirchen` |

**Example 15** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen Selma Eichler, LLM, geboren 13. September 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt. Begründung:  Rechtliche Beurteilung [1] Mit Beschluss vom 12.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz-West` | `Bezirksgericht Graz-West` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Nowotny` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Selma Eichler, LLM` (person)
- `13. September` (date)
- `Bezirksgerichts Graz-West` (organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_4`)


9. 2023 übertrug das Bezirksgericht Graz-West die Zuständigkeit zur Führung der Pflegschaftssache dem Bezirksgericht Braunau am Inn, das die Übernahme jedoch ablehnte.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz-West` | `Bezirksgericht Graz-West` |

**Missed by this rule (FN):**

- `Bezirksgericht Braunau am Inn` (organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_5`)


[2] Das Bezirksgericht Graz-West legte den Akt daraufhin dem Obersten Gerichtshof zur Entscheidung gemäß § 111 Abs 2 JN vor, ohne den Übertragungsbeschluss den Parteien zuzustellen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz-West` | `Bezirksgericht Graz-West` |

**Missed by this rule (FN):**

- `Obersten Gerichtshof` (organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin mj Dietlind Schiewick, geboren 23. Oktober 2017, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Vöcklabruck, 4840 Vöcklabruck, Sportplatzstraße 1–3), deren Mutter Gisela Akcakaya, MSc, und des Antragsgegners Ernst Hartjens, Russische Föderation, wegen Feststellung der Abstammung, aufgrund der vom Bezirksgericht Josefstadt verfügten Vorlage des Akts AZ 23 Fam 2/21y zur Entscheidung gemäß § 111 Abs 2 JN den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Villach zurückgestellt.  Text Begründung: [1] Gegenstand des Verfahrens ist der Antrag auf Feststellung der Abstammung der zum Zeitpunkt der Antragstellung am 24.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Mag. Ziegelbauer` (person)
- `Dietlind Schiewick` (person)
- `23. Oktober` (date)
- `Bezirkshauptmannschaft Vöcklabruck` (organisation)
- `Gisela Akcakaya, MSc` (person)
- `Ernst Hartjens` (person)

**Example 19** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_7`)


[2] Mit Beschluss vom 10. 8. 2020 übertrug das zunächst in dieser Rechtssache angerufene Bezirksgericht Vöcklabruck die Zuständigkeit gemäß § 111 Abs 1 JN an das Bezirksgericht Villach, weil sich die Minderjährige nunmehr in einem Containerdorf in Kreutzerstraße 7, 4851 Haunolding, Österreich aufhalte (ON 7).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Vöcklabruck` | `Bezirksgericht Vöcklabruck` |
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Missed by this rule (FN):**

- `Kreutzerstraße 7, 4851 Haunolding, Österreich` (address)

**Example 20** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_9`)


Das Bezirksgericht Villach übernahm die Zuständigkeit mit Beschluss vom 19. 8. 2020 (ON 8), schrieb eine Tagsatzung für den 28.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Example 21** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_13`)


Daraufhin beraumte das Bezirksgericht Villach die Tagsatzung ab, widerrief das Zustellersuchen (ON 20a) und übertrug mitBeschluss vom 10.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Example 22** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_15`)


2021die Zuständigkeit zur Besorgung dieser Rechtssache nach § 111 Abs 1 JN an das Bezirksgericht Josefstadt (ON 22).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Example 23** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_17`)


Das Bezirksgericht Josefstadt lehnte die Übernahme der Zuständigkeit unter Rückmittlung des Akts am 18.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Example 24** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_20`)


Das Bezirksgericht Villach retournierte den Akt daraufhin an das Bezirksgericht Josefstadt mit dem Hinweis, dass der Akt vom Bezirksgericht Josefstadt dem gemeinsam übergeordneten Gericht vorzulegen sei (ON 30).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Example 25** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_21`)


[7] Letztlich legte das Bezirksgericht Josefstadt die Akten dem Obersten Gerichtshof zur Entscheidung des Zuständigkeitsstreits vor.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Missed by this rule (FN):**

- `Obersten Gerichtshof` (organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_22`)


[8] Die vom Bezirksgericht Villach veranlasste Vorlage der Akten an den Obersten Gerichtshof ist verfrüht:  Rechtliche Beurteilung [9] Übertragungsbeschlüsse nach § 111 JN sind durch die Parteien anfechtbar (RIS-Justiz RS0046981 [insb T5]).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Missed by this rule (FN):**

- `Obersten Gerichtshof` (organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie durch die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Hon.-Prof.in KzlR Iris Makowska, vertreten durch Skribe Rechtsanwaelte GmbH in Wien, gegen die beklagte Partei Dieter Apfelbacher Ltd, Am Fundbach 31w, 9170 Tratten, Österreich, wegen 400 EUR sA, über den Ordinationsantrag nach § 28 JN in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Hon.-Prof.in KzlR Iris Makowska` (person)
- `Skribe Rechtsanwaelte GmbH` (organisation)
- `Dieter Apfelbacher` (person)
- `Am Fundbach 31w, 9170 Tratten, Österreich` (address)

**Example 28** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_5`)


Das von der Klägerin mit ihrer Klage angerufene Bezirksgericht Schwechat hat die internationale und örtliche Zuständigkeit rechtskräftig verneint (RIS-Justiz RS0046450).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 29** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_11`)


Unter Berücksichtigung dieser Vorgaben erscheint eine Zuweisung der Sache an das Bezirksgericht Schwechat als zweckmäßig.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 30** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Paulina Nüsken, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Oliver Eylart, Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Paulina Nüsken` (person)
- `Skribe Rechtsanwälte GmbH` (organisation)
- `Oliver Eylart` (person)

**Example 31** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_7`)


Das vom Kläger angerufene Bezirksgericht Schwechat sprach rechtskräftig seine (internationale) Unzuständigkeit aus.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 32** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_38`)


Unter Berücksichtigung dieser Vorgaben hat eine Zuweisung an das Bezirksgericht Schwechat zu erfolgen, lag doch zum einen der Abflugort in dessen Sprengel und wurde zum anderen die Klage bereits bei diesem Gericht behandelt (6 Nc 31/20s mwN ua).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 33** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_4`)


Anstelle des Bezirksgerichts Kitzbühel wird das Bezirksgericht Mödling als zur Führung des Verlassenschaftsverfahrens zuständiges Gericht bestimmt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Missed by this rule (FN):**

- `Bezirksgerichts Kitzbühel` (organisation)

**Example 34** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_10`)


Im Hinblick auf die angeführten Umstände erscheint die Übertragung der Zuständigkeit an das Bezirksgericht Mödling im Sinne des § 31 Abs 1 JN zweckmäßig und geeignet, eine Verkürzung und Verbilligung des Verfahrens zu bewirken.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Example 35** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_4`)


Text Begründung: Beim Bezirksgericht Innere Stadt Wien ist zur AZ 2 P 88/07t ein Pflegschaftsverfahren betreffend die mj Kinder Basil Biewer anhängig.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innere Stadt Wien` | `Bezirksgericht Innere Stadt Wien` |

**Missed by this rule (FN):**

- `Basil Biewer` (person)

**Example 36** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_8`)


Am 20. 9. 2016 beantragte die Antragstellerin beim Bezirksgericht Josefstadt die Erhöhung der monatlichen Unterhaltszahlung auf 440 EUR ab 1. 9. 2016.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Example 37** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__5`)


Das Abwesenheitsurteil vom 26. September 2018 sowie der unter einem gefasste Beschluss (ON 25) werden aufgehoben und die Sache zu neuer Verhandlung und Entscheidung an das Bezirksgericht Leopoldstadt verwiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Leopoldstadt` | `Bezirksgericht Leopoldstadt` |

**Example 38** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__11`)


Nach zwei negativen Versuchen der Vorführung zur Hauptverhandlung am 2. Mai 2018 (ON 10a, 11) und am 27. Juni 2018 (ON 17, 18) führte das Bezirksgericht Leopoldstadt die – wiederholte (§ 276a zweiter Satz StPO) – Hauptverhandlung am 26. September 2018 in Abwesenheit des Angeklagten durch (ON 24), weil auch zu diesem Termin ein Vorführungsversuch erfolglos geblieben war (ON 23).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Leopoldstadt` | `Bezirksgericht Leopoldstadt` |

**Example 39** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__6`)


Das Urteil, das im Übrigen unberührt bleibt, wird in seinem Strafausspruch aufgehoben und dem Bezirksgericht Kufstein im Umfang der Aufhebung die neuerliche Verhandlung und Entscheidung aufgetragen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Kufstein` | `Bezirksgericht Kufstein` |

**Example 40** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__22`)


Durch die Verhängung einer (Zusatz-)Geldstrafe von 200 Tagessätzen in Missachtung des durch § 5 Z 5 JGG geänderten Strafrahmens bei ersichtlicher Nichtanwendung des § 37 Abs 1 StGB und demzufolge auch der bei Zusatzstrafen anzuwendenden Strafbemessungsvorschrift des § 31 Abs 1 zweiter Satz StGB hat das Bezirksgericht Kufstein das Gesetz in den genannten Bestimmungen zum Nachteil der Verurteilten verletzt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Kufstein` | `Bezirksgericht Kufstein` |

**Example 41** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__23`)


Der Oberste Gerichtshof sah sich daher gemäß § 292 letzter Satz StPO veranlasst, das Urteil im Strafausspruch aufzuheben und dem Bezirksgericht Kufstein in diesem Umfang die Verfahrenserneuerung aufzutragen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Kufstein` | `Bezirksgericht Kufstein` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)

**Example 42** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_3`)


Kopf Der Oberste Gerichtshof hat am 14. August 2014 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, die Hofräte des Obersten Gerichtshofs Dr. Lässig, Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Anscheringer als Schriftführer in der Strafsache gegen Natascha von Bohr wegen Vergehen des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 erster und zweiter Fall, Abs 2 SMG in dem zu AZ 18 U 198/14k des Bezirksgerichts Innere Stadt Wien und AZ 18 U 266/14m des Bezirksgerichts Linz zwischen diesen Gerichten geführten Zuständigkeitsstreit den Beschluss gefasst:  Spruch Das Hauptverfahren ist vom Bezirksgericht Linz zu führen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Linz` | `Bezirksgericht Linz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Dr. Nordmeyer` (person)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Mann` (person)
- `Mag. Anscheringer` (person)
- `Natascha von Bohr` (person)
- `Bezirksgerichts Innere Stadt Wien` (organisation)
- `Bezirksgerichts Linz` (organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_5`)


Das Bezirksgericht Linz überwies die Sache dem Bezirksgericht Innere Stadt Wien mit der Begründung örtlicher Unzuständigkeit (vgl ON 1 S 3: „erste Taten in Wien“).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Linz` | `Bezirksgericht Linz` |
| `Bezirksgericht Innere Stadt Wien` | `Bezirksgericht Innere Stadt Wien` |

**Example 44** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__10`)


Im Protokoll über die Hauptverhandlung vor dem Bezirksgericht Innere Stadt Wien ist als Tag der Hauptverhandlung „23. 11. 2018“ angeführt (ON 18 S 1).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innere Stadt Wien` | `Bezirksgericht Innere Stadt Wien` |

**Example 45** (doc_id: `deanon_260716_TRAIN/14Ns52_18k`) (sent_id: `deanon_260716_TRAIN/14Ns52_18k_4`)


2005 den Beschluss gefasst:  Spruch Für die Durchführung des Strafverfahrens ist das Bezirksgericht Linz zuständig.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Linz` | `Bezirksgericht Linz` |

**Example 46** (doc_id: `deanon_260716_TRAIN/14Ns52_18k`) (sent_id: `deanon_260716_TRAIN/14Ns52_18k_5`)


Gründe:  Rechtliche Beurteilung Mit beim Bezirksgericht Linz eingebrachtem Strafantrag vom 28. Juni 2018 (ON 12) legte die Staatsanwaltschaft Linz Daniel Berlage ein „ab ca Mitte Mai 2016 bis … 18. Jänner 2018“ (1) und am 18. Jänner 2018 „in Linz“ (2) gesetztes, als die Vergehen des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 erster und zweiter Fall, Abs 2 SMG beurteiltes Verhalten zur Last.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Linz` | `Bezirksgericht Linz` |

**Missed by this rule (FN):**

- `Daniel Berlage` (person)

**Example 47** (doc_id: `deanon_260716_TRAIN/14Ns52_18k`) (sent_id: `deanon_260716_TRAIN/14Ns52_18k_12`)


Das Bezirksgericht Linz überwies die Sache „gemäß § 37 Abs 2 StPO“ unter Hinweis auf eine im letztgenannten Verfahren durchgeführte Abfrage aus dem Zentralen Melderegister, aus der sich ergab, dass der Angeklagte von 20. März 2014 bis 5. Mai 2017, sohin zu Beginn des von der Anklage umfassten Tatzeitraums, im Bezirk Amstetten polizeilich gemeldet war (ON 14), wegen örtlicher Unzuständigkeit dem Bezirksgericht St. Pölten (ON 1 S 3 verso).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Linz` | `Bezirksgericht Linz` |

**Missed by this rule (FN):**

- `Bezirksgericht St. Pölten` (organisation)

**Example 48** (doc_id: `deanon_260716_TRAIN/14Ns52_18k`) (sent_id: `deanon_260716_TRAIN/14Ns52_18k_17`)


Die vom Bezirksgericht Linz vertretene Ansicht, die früheste vom Anklagevorwurf erfasste Tat sei an jenem Ort verübt worden, an dem der Angeklagte zur Zeit ihrer Begehung polizeilich gemeldet gewesen sei, findet im Gesetz keine Stütze;

| Predicted | Gold |
|---|---|
| `Bezirksgericht Linz` | `Bezirksgericht Linz` |

**Example 49** (doc_id: `deanon_260716_TRAIN/15Os107_16y`) (sent_id: `deanon_260716_TRAIN/15Os107_16y_7`)


Mit unangefochten in Rechtskraft erwachsenem Beschluss vom 7. Mai 2013 (ON 39) bestimmte das Bezirksgericht Steyr die vom Privatankläger zu ersetzenden „Kosten der Vertretung des Privatangeklagten“ – nämlich für eine Intervention beim Bezirksgericht Steyr, für die Teilnahme an der Hauptverhandlung und für den Kostenbestimmungsantrag unter gleichzeitiger Abweisung des Mehrbegehrens – (aufgrund eines Rechenfehlers statt mit 544,44 Euro) mit 342,08 Euro (1./) sowie vom Angeklagten für sein Erscheinen vor Gericht geltend gemachte (Fahrt-)Kosten (ON 32a S 2) mit 15,40 Euro (2./).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Steyr` | `Bezirksgericht Steyr` |
| `Bezirksgericht Steyr` | `Bezirksgericht Steyr` |

**Example 50** (doc_id: `deanon_260716_TRAIN/15Os107_16y`) (sent_id: `deanon_260716_TRAIN/15Os107_16y_8`)


Über Antrag des Verfahrenshilfeverteidigers berichtigte das Bezirksgericht Steyr mit Beschluss vom 4. November 2015 (ON 44) den „Rechnungsendbetrag“ zu 1./ (als offenkundigen Rechenfehler) auf 544,44 Euro.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Steyr` | `Bezirksgericht Steyr` |

**Example 51** (doc_id: `deanon_260716_TRAIN/15Os97_10v`) (sent_id: `deanon_260716_TRAIN/15Os97_10v_13`)


Rechtliche Beurteilung Wie die Generalprokuratur in ihrer zur Wahrung des Gesetzes erhobenen Nichtigkeitsbeschwerde zutreffend ausführt, verletzt der Vorgang, dass es das Bezirksgericht Innsbruck unterließ, von seinem gemeinsam mit dem Urteil vom 4. August 2009 (unter Absehen vom Widerruf der Andreas Gaisert im Verfahren AZ 23 BE29/06a des Landesgerichts Innsbruck gewährten bedingten Entlassung) gefassten Beschluss auf Verlängerung der Probezeit unverzüglich das Vollzugsgericht in Kenntnis zu setzen, § 494a Abs 7 StPO, wonach das erkennende Gericht all jene Gerichte unverzüglich zu verständigen hat, deren Vorentscheidungen von einer Entscheidung nach § 494a Abs 1 und 6 StPO betroffen sind.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innsbruck` | `Bezirksgericht Innsbruck` |

**Missed by this rule (FN):**

- `Andreas Gaisert` (person)
- `Landesgerichts Innsbruck` (organisation)

**Example 52** (doc_id: `deanon_260716_TRAIN/15Os97_10v`) (sent_id: `deanon_260716_TRAIN/15Os97_10v_16`)


Das Bezirksgericht Innsbruck hätte daher sogleich nach Fassung seines Probezeitverlängerungsbeschlusses - und nicht erst im Zuge der Endverfügung vom 31. März 2010 - das Vollzugsgericht davon in Kenntnis setzen müssen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innsbruck` | `Bezirksgericht Innsbruck` |

**Example 53** (doc_id: `deanon_260716_TRAIN/1Ob55_13i`) (sent_id: `deanon_260716_TRAIN/1Ob55_13i_6`)


Nach dem Klagsvorbringen sei er am 19. 8. 2009 im Strandbad Bezirksgericht Donaustadt beim Verlassen des Wassers von einem ca zwei Fäuste großen Stein ins Gesicht getroffen worden, der vom damals sechsjährigen Beklagten geworfen worden sei.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Donaustadt` | `Bezirksgericht Donaustadt` |

**Example 54** (doc_id: `deanon_260716_TRAIN/1Ob55_13i`) (sent_id: `deanon_260716_TRAIN/1Ob55_13i_17`)


Verwiesen werde auf einen Akt der Staatsanwaltschaft Bezirksgericht Voitsberg, in welchem gegen den Schädiger Vorerhebungen geführt, jedoch mangels Deliktsfähigkeit eingestellt worden seien.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Voitsberg` | `Bezirksgericht Voitsberg` |

**Example 55** (doc_id: `deanon_260716_TRAIN/23Os1_15t`) (sent_id: `deanon_260716_TRAIN/23Os1_15t_6`)


Text Gründe: Mit dem angefochtenen Erkenntnis wurde Dr. Xaver Springinsgut, Rechtsanwalt in St.Oswald - Rosennockstraße 31, 2051 Platt, Österreich, wegen des Verstoßes gegen die Bestimmungen des § 9 (Abs 1) RAO und des § 2 RL-BA der Disziplinarvergehen der Verletzung von Berufspflichten und der Beeinträchtigung von Ehre oder (richtig:) Ansehen des Standes nach § 1 Abs 1 erster und zweiter Fall DSt schuldig erkannt, weil er als Rechtsvertreter der Ehegatten Roman und Elfriede Jähnel in Anträgen auf Aufschiebung der Zwangsversteigerungen für seine Mandanten vom 5. September 2013 in näher bezeichneten Verfahren des Bezirksgerichts Innsbruck und des Bezirksgerichts Amstetten sowie in einer näher genannten Feststellungsklage an das Landesgericht Linz vom 7. Oktober 2013 und in einer Impugnationsklage an das Bezirksgericht Amstetten vom 10. Oktober 2013 jeweils vorgebracht hatte, seine Mandanten hätten sämtliche Verpflichtungen aus einer mit der Alpen Nexlex AG abgeschlossenen Vereinbarung vom 11. Dezember 2012, insbesondere jene zur unwiderruflichen Antragstellung auf Aufhebung der Höfeeigenschaft einer näher bezeichnenden Liegenschaft in Schulgartenweg 18, 9872 Grantsch, Österreich, eingehalten, obwohl ihm zum Zeitpunkt der Antragstellung und Klagseinbringung bekannt war, dass der Antrag auf Aufhebung der Höfeeigenschaft vom 13. Dezember 2012 bereits am 14. Juni 2013 von Roman Jiran, durch ihn vertreten, entgegen der zuvor genannten Vereinbarung vom 11. Dezember 2012 wieder zurückgezogen worden war.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Amstetten` | `Bezirksgericht Amstetten` |

**Missed by this rule (FN):**

- `Dr. Xaver Springinsgut` (person)
- `St.Oswald - Rosennockstraße 31, 2051 Platt, Österreich` (address)
- `Elfriede Jähnel` (person)
- `Bezirksgerichts Innsbruck` (organisation)
- `Bezirksgerichts Amstetten` (organisation)
- `Landesgericht Linz` (organisation)
- `Alpen Nexlex AG` (organisation)
- `Schulgartenweg 18, 9872 Grantsch, Österreich` (address)
- `Roman Jiran` (person)

**Example 56** (doc_id: `deanon_260716_TRAIN/3Nc11_13t`) (sent_id: `deanon_260716_TRAIN/3Nc11_13t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie die Hofräte Univ.-Prof Dr. Neumayr und Dr. Jensik als weitere Richter in der Ordinationssache der Antragstellerin Mikulska Textil GmbH, Kohleck 4, 6794 Partenen, Österreich, vertreten durch Dr. Clemens Thiele, Rechtsanwalt in Salzburg, gegen die Antragsgegnerin TraunWind GmbH, Ferdinand Schaller-Weg 1, 4131 Stieberberg, Österreich, wegen Exekutionsführung nach § 355 EO, infolge Antrags gemäß § 28 JN den Beschluss gefasst:  Spruch Für die Bewilligung und die Vollziehung der beabsichtigten Unterlassungsexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Prückner` (person)
- `Dr. Neumayr` (person)
- `Dr. Jensik` (person)
- `Mikulska Textil GmbH` (organisation)
- `Kohleck 4, 6794 Partenen, Österreich` (address)
- `Dr. Clemens Thiele` (person)
- `TraunWind GmbH` (organisation)
- `Ferdinand Schaller-Weg 1, 4131 Stieberberg, Österreich` (address)

**Example 57** (doc_id: `deanon_260716_TRAIN/3Nc32_19i`) (sent_id: `deanon_260716_TRAIN/3Nc32_19i_5`)


Das Bezirksgericht Telfs legte den Akt unmittelbar (dh ohne jede sonstige Erledigung) von Amts wegen dem Obersten Gerichtshof zwecks Entscheidung über eine Ordination nach § 28 JN vor.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Telfs` | `Bezirksgericht Telfs` |

**Missed by this rule (FN):**

- `Obersten Gerichtshof` (organisation)

**Example 58** (doc_id: `deanon_260716_TRAIN/3Nc32_19i`) (sent_id: `deanon_260716_TRAIN/3Nc32_19i_8`)


Da das angerufene Bezirksgericht Telfs bislang noch nicht negativ über seine Zuständigkeit entschieden hat, kommt eine Ordination nach § 28 JN nicht in Betracht.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Telfs` | `Bezirksgericht Telfs` |

**Example 59** (doc_id: `deanon_260716_TRAIN/3Nc39_24a`) (sent_id: `deanon_260716_TRAIN/3Nc39_24a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn und die Hofrätin Dr. Kodek als weitere Richter in der Ordinationssache der betreibenden Partei PhD Miklos Juergens, vertreten durch Dr. Florian Johann Ernst Knaipp, Rechtsanwalt in Wien, gegen die verpflichtete Partei Dumberger Technik Limited, Dr.-Franz-Reinprecht-Weg 33, 9913 Abfaltersbach, Österreich, wegen 47.126,91 EUR sA, über den Antrag auf Ordination nach § 28 JN, den Beschluss gefasst:  Spruch Für die Bewilligung und den Vollzug der von der betreibenden Partei beabsichtigten Rechteexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Höllwerth` (person)
- `Hon.-Prof. Dr. Brenn` (person)
- `Dr. Kodek` (person)
- `PhD Miklos Juergens` (person)
- `Dr. Florian Johann Ernst Knaipp` (person)
- `Dumberger Technik Limited` (organisation)
- `Dr.-Franz-Reinprecht-Weg 33, 9913 Abfaltersbach, Österreich` (address)

**Example 60** (doc_id: `deanon_260716_TRAIN/3Nc39_24a`) (sent_id: `deanon_260716_TRAIN/3Nc39_24a_29`)


Als örtlich zuständiges Exekutionsgericht für die beabsichtigte Rechteexekution ist das Bezirksgericht Salzburg zu bestimmen, weil die Rhein Kraftnor.at GmbH als Registrierungsstelle der von der beabsichtigten Exekutionsführung betroffenen Domain der Verpflichteten im Sprengel dieses Gerichts ihren Sitz hat.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Missed by this rule (FN):**

- `Rhein Kraftnor.at` (organisation)

**Example 61** (doc_id: `deanon_260716_TRAIN/4Nc18_11a`) (sent_id: `deanon_260716_TRAIN/4Nc18_11a_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel und Dr. Jensik als weitere Richter in der Rechtssache der klagenden Partei Kosfelder+Gerasimowitsch KI GmbH, Webergarten 4c, 2534 Maria Raisenmarkt, Österreich, vertreten durch Dr. Christian Fuchshuber LL.M., Rechtsanwalt in Innsbruck, gegen die beklagte Partei Gastronomie Seezor GmbH, Psaltersteig 61, 4624 Felling, Österreich, vertreten durch Dr. Gerhard Strobich, Rechtsanwalt in Trofaiach, wegen 5.873,18 EUR sA, über den Delegierungsantrag der beklagten Partei den Beschluss gefasst:  Spruch Der Antrag, zur Verhandlung und Entscheidung in dieser Rechtssache anstelle des Bezirksgerichts Innsbruck das Bezirksgericht Leoben zu bestimmen, wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Leoben` | `Bezirksgericht Leoben` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schenk` (person)
- `Dr. Vogel` (person)
- `Dr. Jensik` (person)
- `Kosfelder+Gerasimowitsch KI GmbH` (organisation)
- `Webergarten 4c, 2534 Maria Raisenmarkt, Österreich` (address)
- `Dr. Christian Fuchshuber LL.M.` (person)
- `Gastronomie Seezor GmbH` (organisation)
- `Psaltersteig 61, 4624 Felling, Österreich` (address)
- `Dr. Gerhard Strobich` (person)
- `Bezirksgerichts Innsbruck` (organisation)

**Example 62** (doc_id: `deanon_260716_TRAIN/4Nc18_11a`) (sent_id: `deanon_260716_TRAIN/4Nc18_11a_4`)


Text Begründung: Die Klägerin mit Sitz in Innsbruck begehrt mit ihrer beim Bezirksgericht Innsbruck eingebrachten Klage 5.873,18 EUR sA für der Beklagten vereinbarungsgemäß erbrachte Reisedienstleistungen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innsbruck` | `Bezirksgericht Innsbruck` |

**Example 63** (doc_id: `deanon_260716_TRAIN/4Nc18_11a`) (sent_id: `deanon_260716_TRAIN/4Nc18_11a_8`)


Die Beklagte beantragte die Delegierung der Rechtssache an das Bezirksgericht Leoben.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Leoben` | `Bezirksgericht Leoben` |

**Example 64** (doc_id: `deanon_260716_TRAIN/4Nc18_11a`) (sent_id: `deanon_260716_TRAIN/4Nc18_11a_14`)


Das Bezirksgericht Innsbruck sprach sich gleichermaßen gegen die beantragte Delegierung aus, verwies auf die Möglichkeit der Zeugenvernehmung mittels Videokonferenz nach § 277 ZPO und (deswegen) auf den fehlenden Vorteil für die Parteien, der mit einer allfälligen Delegierung verbunden wäre.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innsbruck` | `Bezirksgericht Innsbruck` |

**Example 65** (doc_id: `deanon_260716_TRAIN/4Nc4_17a`) (sent_id: `deanon_260716_TRAIN/4Nc4_17a_6`)


Für die Bewilligung und die Vollziehung der beabsichtigten Exekution gegen die Zweitbeklagte auf Urteilsveröffentlichung wird das Bezirksgericht Innere Stadt Wien als örtlich zuständiges Gericht bestimmt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innere Stadt Wien` | `Bezirksgericht Innere Stadt Wien` |

**Example 66** (doc_id: `deanon_260716_TRAIN/4Nc4_17a`) (sent_id: `deanon_260716_TRAIN/4Nc4_17a_9`)


Mit dem gegenständlichen Ordinationsantrag beantragen die Klägerinnen, der Oberste Gerichtshof möge das Bezirksgericht Innere Stadt Wien oder ein anderes Bezirksgericht als örtlich zuständiges Gericht für die Durchsetzung des Veröffentlichungsanspruchs gemäß § 354 EO gegen die Zweitbeklagte bestimmen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innere Stadt Wien` | `Bezirksgericht Innere Stadt Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)

**Example 67** (doc_id: `deanon_260716_TRAIN/4Nc4_17a`) (sent_id: `deanon_260716_TRAIN/4Nc4_17a_19`)


Die Ordinationsvoraussetzungen gemäß § 28 Abs 1 Z 2 JN sind daher erfüllt. Dem Ordinationsantrag ist somit stattzugeben und zweckmäßigerweise das Bezirksgericht Innere Stadt Wien als zuständiges Gericht zu bestimmen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innere Stadt Wien` | `Bezirksgericht Innere Stadt Wien` |

**Example 68** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofrätin Dr. Grohmann und den Hofrat Dr. Steger als weitere Richter in der Pflegschaftssache des mj Aron Margwarth, geboren am 29. März 1957, Vater Klaus Rufer, vertreten durch Prof. Dr. Georg Zanger, Rechtsanwalt in Wien, wegen Obsorge, über den Delegierungsantrag der Mutter Rafaela Erreth, vertreten durch Mag. Britta Schönhart-Loinig, Rechtsanwältin in Wien, den Beschluss gefasst:  Spruch Der Antrag auf Delegierung der Pflegschaftssache vom Bezirksgericht Gänserndorf an das Bezirksgericht Villach wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Gänserndorf` | `Bezirksgericht Gänserndorf` |
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Jensik` (person)
- `Dr. Grohmann` (person)
- `Dr. Steger` (person)
- `Aron Margwarth` (person)
- `29. März 1957` (date)
- `Klaus Rufer` (person)
- `Prof. Dr. Georg Zanger` (person)
- `Rafaela Erreth` (person)
- `Mag. Britta Schönhart-Loinig` (person)

**Example 69** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_12`)


Seit damals ist das Bezirksgericht Gänserndorf mit diesem mittlerweile hoch eskalierten Obsorgestreit regelmäßig und intensiv befasst, der Prozessstoff umfasst bereits zwei Aktenbände.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Gänserndorf` | `Bezirksgericht Gänserndorf` |

**Example 70** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_22`)


7. 2019 die Delegierung der Pflegschaftssache an das Bezirksgericht Villach nach § 31 Abs 1 JN.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Example 71** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_28`)


Da der Mittelpunkt der Lebensführung des Kindes nunmehr in Velden liege und offene Anträge nicht gegen eine Zuständigkeitsübertragung sprächen, sei das Bezirksgericht Villach besser in der Lage, die pflegschaftsgerichtlichen Agenden zu besorgen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Example 72** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_30`)


Der zukünftige gewöhnliche Aufenthalt des Minderjährigen hänge vom Ausgang des beim Bezirksgericht Gänserndorf anhängigen Verfahrens ab, das seit August 2018 intensiv mit den zugrunde liegenden Umständen befasst sei, bereits Sachverständigengutachten und Stellungnahmen des Jugendamts eingeholt und anlässlich von Tagsatzungen vergleichsweise Einigungen zum Kontaktrecht initiiert habe.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Gänserndorf` | `Bezirksgericht Gänserndorf` |

**Example 73** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_36`)


Die Handhabung des pflegschaftsgerichtlichen Schutzes des Kindes sei durch das Bezirksgericht Gänserndorf wirksamer gestaltbar als durch das Bezirksgericht Villach, das die Familie überhaupt noch nicht kenne.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Gänserndorf` | `Bezirksgericht Gänserndorf` |
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Example 74** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_39`)


Die Mutter habe nicht die Übertragung der Zuständigkeit nach § 111 JN, sondern die Delegierung der Außerstreitsache nach § 31 Abs 1 JN begehrt, die Entscheidung darüber komme – da es sich um eine Delegierung aus einem Oberlandesgerichtssprengel an den anderen handle – dem Obersten Gerichtshof zu. Das Bezirksgericht Gänserndorf legte die Akten daraufhin dem Obersten Gerichtshof zur Entscheidung über den Delegierungsantrag vor.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Gänserndorf` | `Bezirksgericht Gänserndorf` |

**Missed by this rule (FN):**

- `Obersten Gerichtshof` (organisation)
- `Obersten Gerichtshof` (organisation)

**Example 75** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_57`)


das delegierte Bezirksgericht Villach müsste sich in den mittlerweile bereits umfangreichen Pflegschaftsakt erst einarbeiten.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Example 76** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_58`)


Darüber hinaus hat das Bezirksgericht Gänserndorf bereits für 26.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Gänserndorf` | `Bezirksgericht Gänserndorf` |

**Example 77** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_61`)


Dass in diesem Verfahrensstadium die Delegierung der Pflegschaftssache an das Bezirksgericht Villach dem Kindeswohl besser entsprechen würde als die Weiterführung des Obsorge- und Kontaktrechtsverfahrens durch den bisher zuständigen Richter des Bezirksgerichts Gänserndorf, ist ebensowenig zu erkennen wie eine dadurch erzielbare Verfahrensbeschleunigung und Erleichterung des Gerichtszugangs für sämtliche Beteiligte.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Missed by this rule (FN):**

- `Bezirksgerichts Gänserndorf` (organisation)

**Example 78** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_62`)


Der Umstand, dass der Minderjährige derzeit im Sprengel des Bezirksgerichts Villach wohnt und für die Mutter seine Betreuung bei Terminen am Bezirksgericht Villach leichter zu organisieren wäre als beim Bezirksgericht Gänserndorf, reicht daher für eine Bejahung der Zweckmäßigkeit iSd § 31 Abs 1 JN nicht aus.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |
| `Bezirksgericht Gänserndorf` | `Bezirksgericht Gänserndorf` |

**Missed by this rule (FN):**

- `Bezirksgerichts Villach` (organisation)

**Example 79** (doc_id: `deanon_260716_TRAIN/6Ob199_10y`) (sent_id: `deanon_260716_TRAIN/6Ob199_10y_4`)


Im vorliegenden Verfahren geht es um die pflegschaftsbehördliche Genehmigung eines Vergleichs vor dem Bezirksgericht Meidling.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Meidling` | `Bezirksgericht Meidling` |

**Example 80** (doc_id: `deanon_260716_TRAIN/7Nc4_12s`) (sent_id: `deanon_260716_TRAIN/7Nc4_12s_4`)


Lieselotte Sedlmair, und 2. Yorick Bergbauer, wegen Erlassung einer einstweiligen Verfügung, infolge der Vorlage des Aktes 1 C 16/12t des Bezirksgerichts Wiener Neustadt zur Entscheidung über den negativen Kompetenzkonflikt mit dem Bezirksgericht Mürzzuschlag nach § 47 JN den Beschluss gefasst:  Spruch Zur Entscheidung über den Antrag auf Erlassung der einstweiligen Verfügung ist das Bezirksgericht Wiener Neustadt zuständig.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mürzzuschlag` | `Bezirksgericht Mürzzuschlag` |
| `Bezirksgericht Wiener Neustadt` | `Bezirksgericht Wiener Neustadt` |

**Missed by this rule (FN):**

- `Lieselotte Sedlmair` (person)
- `Yorick Bergbauer` (person)
- `Bezirksgerichts Wiener Neustadt` (organisation)

**Example 81** (doc_id: `deanon_260716_TRAIN/7Nc4_12s`) (sent_id: `deanon_260716_TRAIN/7Nc4_12s_6`)


Text Begründung: Der Antragsteller stellte mit am 2. 1. 2012 beim Bezirksgericht Mürzzuschlag eingelangtem Schriftsatz den Antrag, mit einstweiliger Verfügung gemäß §§ 382g, 381 Z 2 EO gegen die Antragsgegner diverse Verbote zu erlassen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mürzzuschlag` | `Bezirksgericht Mürzzuschlag` |

**Example 82** (doc_id: `deanon_260716_TRAIN/7Nc4_12s`) (sent_id: `deanon_260716_TRAIN/7Nc4_12s_7`)


Das Bezirksgericht Mürzzuschlag erklärte sich mit am selben Tag gefasstem Beschluss gemäß § 387 Abs 4 EO für unzuständig und überwies das Verfahren nach § 44 JN an das nicht offenbar unzuständige Bezirksgericht Wiener Neustadt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mürzzuschlag` | `Bezirksgericht Mürzzuschlag` |
| `Bezirksgericht Wiener Neustadt` | `Bezirksgericht Wiener Neustadt` |

**Example 83** (doc_id: `deanon_260716_TRAIN/7Nc4_12s`) (sent_id: `deanon_260716_TRAIN/7Nc4_12s_9`)


Das Bezirksgericht Wiener Neustadt stellte den Provisorialantrag zunächst den Antragsgegnern zur Äußerung zu. Es fasste nach einer Anfrage beim Zentralen Melderegister dann aber am 8.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Wiener Neustadt` | `Bezirksgericht Wiener Neustadt` |

**Example 84** (doc_id: `deanon_260716_TRAIN/7Nc4_12s`) (sent_id: `deanon_260716_TRAIN/7Nc4_12s_10`)


2. 2012 den Beschluss, die Rechtssache wiederum dem Bezirksgericht Mürzzuschlag (zurück-)zuüberweisen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mürzzuschlag` | `Bezirksgericht Mürzzuschlag` |

**Example 85** (doc_id: `deanon_260716_TRAIN/7Nc4_12s`) (sent_id: `deanon_260716_TRAIN/7Nc4_12s_12`)


Das Bezirksgericht Wiener Neustadt könne daher seine Unzuständigkeit aussprechen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Wiener Neustadt` | `Bezirksgericht Wiener Neustadt` |

**Example 86** (doc_id: `deanon_260716_TRAIN/7Nc4_12s`) (sent_id: `deanon_260716_TRAIN/7Nc4_12s_15`)


Das Bezirksgericht Wiener Neustadt legte den Akt dem Obersten Gerichtshof zur Entscheidung über den negativen Kompetenzkonflikt nach § 47 JN vor.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Wiener Neustadt` | `Bezirksgericht Wiener Neustadt` |

**Missed by this rule (FN):**

- `Obersten Gerichtshof` (organisation)

**Example 87** (doc_id: `deanon_260716_TRAIN/8Ob96_17a`) (sent_id: `deanon_260716_TRAIN/8Ob96_17a_16`)


Das Erstgericht schränkte das Verfahren auf die Fragen der örtlichen und sachlichen Zuständigkeit ein und stellte – soweit Gegenstand des Rechtsmittelverfahrens – fest, der Antrag sei im Verfahren außer Streitsachen zu erledigen und die Rechtssache werde an das nicht offenbar unzuständige Bezirksgericht Fünfhaus überwiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Fünfhaus` | `Bezirksgericht Fünfhaus` |

**Example 88** (doc_id: `deanon_260716_TRAIN/8Ob96_17a`) (sent_id: `deanon_260716_TRAIN/8Ob96_17a_43`)


3.3 Die vom Erstgericht ausgesprochene Überweisung an das Bezirksgericht Fünfhaus wird im Revisionsrekurs nicht inhaltlich bekämpft.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Fünfhaus` | `Bezirksgericht Fünfhaus` |

**Example 89** (doc_id: `deanon_260716_TRAIN/9Nc65_19m`) (sent_id: `deanon_260716_TRAIN/9Nc65_19m_4`)


Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 90** (doc_id: `deanon_260716_TRAIN/9Nc65_19m`) (sent_id: `deanon_260716_TRAIN/9Nc65_19m_27`)


Unter Berücksichtigung dieser Vorgaben hat eine Zuweisung der vorliegenden Rechtssache an das Bezirksgericht Schwechat zu erfolgen, weil der Abflugort im Sprengel dieses Gerichts gelegen war.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_4`)


9. 2023 übertrug das Bezirksgericht Graz-West die Zuständigkeit zur Führung der Pflegschaftssache dem Bezirksgericht Braunau am Inn, das die Übernahme jedoch ablehnte.

**False Positives:**

- `Bezirksgericht Braunau` — partial — pred is substring of gold: `Bezirksgericht Braunau am Inn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz-West`(organisation)
- `Bezirksgericht Braunau am Inn`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_26`)


Weiters habe sie der Klägerin Zinsen und Prozesskosten, zu deren Zahlung sie im Verfahren vor dem Bezirksgericht Bezirksgericht Hall (in Tirol) verurteilt worden war, sowie die Kosten deren eigener Vertretung in diesem Verfahren zu ersetzen.

**False Positives:**

- `Bezirksgericht Bezirksgericht Hall` — positional overlap with gold: `Bezirksgericht Hall (in Tirol)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Hall (in Tirol)`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_10`)


Für ihn ist ein Sachwalter bestellt, der seit 2011 alle Angelegenheiten (§ 268 Abs 3 Z 3 ABGB) zu besorgen hat (siehe den Beschluss des Bezirksgericht Bezirksgericht Freistadt vom 15.

**False Positives:**

- `Bezirksgericht Bezirksgericht Freistadt` — partial — gold is substring of pred: `Bezirksgericht Freistadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Freistadt`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__13`)


Mit Abwesenheitsurteil vom 26. September 2018 (ON 25) sprach das Bezirksgericht Leopoldstadt Nenad Panagiotakopoulou des Vergehens der Veruntreuung nach § 133 Abs 1 StGB schuldig und verurteilte ihn zu einer Freiheitsstrafe.

**False Positives:**

- `Bezirksgericht Leopoldstadt Nenad Panagiotakopoulou` — partial — gold is substring of pred: `Bezirksgericht Leopoldstadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Leopoldstadt`(organisation)
- `Nenad Panagiotakopoulou`(person)

**Example 4** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_9`)


In diesem Fall kommt das Verfahren (soweit hier von Interesse) gemäß § 37 Abs 2 zweiter Satz StPO jenem Gericht zu, in dessen Zuständigkeit die frühere Straftat fällt. Zutreffend weist das Bezirksgericht Innere Stadt darauf hin, dass nach der Aktenlage kein Anhaltspunkt für einen Tatort in Wien besteht.

**False Positives:**

- `Bezirksgericht Innere Stadt` — partial — gold is substring of pred: `Bezirksgericht Innere`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Innere`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/14Ns52_18k`) (sent_id: `deanon_260716_TRAIN/14Ns52_18k_12`)


Das Bezirksgericht Linz überwies die Sache „gemäß § 37 Abs 2 StPO“ unter Hinweis auf eine im letztgenannten Verfahren durchgeführte Abfrage aus dem Zentralen Melderegister, aus der sich ergab, dass der Angeklagte von 20. März 2014 bis 5. Mai 2017, sohin zu Beginn des von der Anklage umfassten Tatzeitraums, im Bezirk Amstetten polizeilich gemeldet war (ON 14), wegen örtlicher Unzuständigkeit dem Bezirksgericht St. Pölten (ON 1 S 3 verso).

**False Positives:**

- `Bezirksgericht St` — partial — pred is substring of gold: `Bezirksgericht St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Linz`(organisation)
- `Bezirksgericht St. Pölten`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/1Ob55_13i`) (sent_id: `deanon_260716_TRAIN/1Ob55_13i_5`)


Text Begründung: Die Obsorge für den Minderjährigen steht allein der Mutter zu. Mit der am 20. 8. 2012 beim Bezirksgericht Bezirksgericht Bregenz eingebrachten Klage begehrte der Minderjährige von einem in Deutschland wohnhaften minderjährigen Beklagten Schadenersatz von 3.850 EUR sA und die Feststellung seiner Haftung für sämtliche aus dessen Steinwurf resultierenden Spät- und Dauerfolgen.

**False Positives:**

- `Bezirksgericht Bezirksgericht Bregenz` — partial — gold is substring of pred: `Bezirksgericht Bregenz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Bregenz`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/1Ob55_13i`) (sent_id: `deanon_260716_TRAIN/1Ob55_13i_67`)


8. 2012 beim gemäß Art 5 Nr 3 EuGVVO zuständigen Bezirksgericht Bezirksgericht Baden (Gericht des Ortes, an dem das schädigende Ereignis eingetreten ist) im Elektronischen Rechtsverkehr eingebracht.

**False Positives:**

- `Bezirksgericht Bezirksgericht Baden` — partial — gold is substring of pred: `Bezirksgericht Baden`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Baden`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/2Ob162_23x`) (sent_id: `deanon_260716_TRAIN/2Ob162_23x_7`)


Text Begründung: [1] Beim Bezirksgericht St. Johann im Pongau ist zu AZ 455 A 78/22f das Verlassenschaftsverfahren nach dem 2022 verstorbenen Erblasser anhängig.

**False Positives:**

- `Bezirksgericht St` — partial — pred is substring of gold: `Bezirksgericht St. Johann im Pongau`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht St. Johann im Pongau`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/7Ob4_12g`) (sent_id: `deanon_260716_TRAIN/7Ob4_12g_5`)


Text Begründung: Über Einrede der örtlichen Unzuständigkeit erklärte sich das zunächst angerufene Bezirksgericht Hall in Tirol für unzuständig und überwies die Rechtssache aufgrund des (Eventual-)Antrags der Klägerin („für den Fall, dass das [Erst-]Gericht seine Unzuständigkeit ausspricht“) gemäß § 261 Abs 6 ZPO an das nicht offenbar unzuständige Bezirksgericht Wolfsberg, in dessen Sprengel sich der Sitz der Beklagten befindet.

**False Positives:**

- `Bezirksgericht Hall` — partial — pred is substring of gold: `Bezirksgericht Hall in Tirol`
- `Bezirksgericht Wolfsberg` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Hall in Tirol`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/7Ob4_12g`) (sent_id: `deanon_260716_TRAIN/7Ob4_12g_7`)


das Bezirksgericht Wolfsberg als allgemeiner Gerichtsstand der Beklagten, welche dessen - durch Parteienvereinbarung begründbare - Zuständigkeit ebenfalls heranziehe, sei hingegen „nicht offenbar unzuständig“.

**False Positives:**

- `Bezirksgericht Wolfsberg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `BFG and VwGH Acronyms` 🏆

**F1:** 0.119 | **Precision:** 0.814 | **Recall:** 0.064  

**Format:** `regex`  
**Rule ID:** `5ec1bb77`  
**Description:**
Matches full court names including '(BFG)' suffix as a single entity. Updated to capture 'Bundesfinanzgericht' followed by optional genitive endings and the '(BFG)' suffix as one unit, preventing split matches.

**Content:**
```
\b(?:Verwaltungsgerichtshof(?:es|s)?|Verfassungsgerichtshof(?:es|s)?|Landesgericht(?:es|s)\s+[A-Z][a-z]+|Landesgerichts\s+[A-Z])\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.814 | 0.064 | 0.119 | 317 | 258 | 59 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 258 | 59 | 3737 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der beim Landesgericht Linz zu AZ 3 Cg 46/21a anhängigen Rechtssache der klagenden Partei Hollengk Planung GmbH, Am Steindl 3, 9873 Döbriach, Österreich, vertreten durch Huber Berchtold Rechtsanwälte OG in Wien, gegen die beklagte Partei Wind Nexheimval GmbH, Wiesbergsiedlung 4, 8341 Pöllau, Österreich, vertreten durch ScherbaumSeebacher Rechtsanwälte GmbH in Graz, wegen 188.117,55 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN folgenden Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, zur Verhandlung und Entscheidung der Rechtssache anstelle des Landesgerichts Linz das Landesgericht Korneuburg zu bestimmen, wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Linz` | `Landesgerichts Linz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Landesgericht Linz` (organisation)
- `Hollengk Planung GmbH` (organisation)
- `Am Steindl 3, 9873 Döbriach, Österreich` (address)
- `Huber Berchtold Rechtsanwälte OG` (organisation)
- `Wind Nexheimval GmbH` (organisation)
- `Wiesbergsiedlung 4, 8341 Pöllau, Österreich` (address)
- `ScherbaumSeebacher Rechtsanwälte GmbH` (organisation)
- `Landesgericht Korneuburg` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_19`)


Sowohl die Beklagte als auch ihre Geschäftsführer sowie fünf namhaft gemachte Zeugen hätten ihren Arbeitsplatz bzw Wohnsitz im Sprengel des Landesgerichts Linz.

| Predicted | Gold |
|---|---|
| `Landesgerichts Linz` | `Landesgerichts Linz` |

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_30`)


Zwar ist das Bauvorhaben im Sprengel des Landesgerichts Korneuburg situiert.

| Predicted | Gold |
|---|---|
| `Landesgerichts Korneuburg` | `Landesgerichts Korneuburg` |

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_31`)


Mehrere von der Beklagten namhaft gemachte Zeugen sind aber im Sprengel des angerufenen Landesgerichts Linz bzw in Oberösterreich wohnhaft.

| Predicted | Gold |
|---|---|
| `Landesgerichts Linz` | `Landesgerichts Linz` |

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Steidlen+Ysner Daten GmbH, Kaminweg 34, 8200 Laßnitzthal, Österreich, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Verlag Waldlemder GmbH, Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

| Predicted | Gold |
|---|---|
| `Landesgerichts Linz` | `Landesgerichts Linz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Landesgericht Linz` (organisation)
- `Steidlen+Ysner Daten GmbH` (organisation)
- `Kaminweg 34, 8200 Laßnitzthal, Österreich` (address)
- `Dr. Roland Kassowitz` (person)
- `Verlag Waldlemder GmbH` (organisation)
- `Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich` (address)
- `Prof. Haslinger` (person)
- `Handelsgericht Wien` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Rechtssache der klagenden Partei Mur Dorftalnex Technologien -GmbH, Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich, vertreten durch Dr. Peter Lechner und Dr. Hermann Pfurtscheller, Rechtsanwälte in Innsbruck, und ihrer Nebenintervenientin Ober Dertri GmbH, Hintereggweg 93, 2070 Kleinhöflein, Österreich, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Rudolf Ketelhut GmbH, Fiebrichgasse 17, 5120 Seeleiten, Österreich, vertreten durch Rechtsanwaltskanzlei Dr. Bernhard Hämmerle GmbH in Innsbruck, und ihrer Nebenintervenientin Völkertz Energie GmbH, Brunnbachweg 19, 4653 Mayersdorf, Österreich, vertreten durch Dr. Franz Pechmann, Rechtsanwalt in Wien, wegen 696.238,34 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck vom 2. Oktober 2009, GZ 4 R 108/09b-167, mit dem das Urteil des Landesgerichts Innsbruck vom 23. Februar 2009, GZ 41 Cg 228/01z-152, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Mur Dorftalnex Technologien -GmbH` (organisation)
- `Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich` (address)
- `Dr. Peter Lechner` (person)
- `Dr. Hermann Pfurtscheller` (person)
- `Ober Dertri GmbH` (organisation)
- `Hintereggweg 93, 2070 Kleinhöflein, Österreich` (address)
- `Dr. Thomas Girardi` (person)
- `Rudolf Ketelhut` (person)
- `Fiebrichgasse 17, 5120 Seeleiten, Österreich` (address)
- `Dr. Bernhard Hämmerle GmbH` (organisation)
- `Völkertz Energie GmbH` (organisation)
- `Brunnbachweg 19, 4653 Mayersdorf, Österreich` (address)
- `Dr. Franz Pechmann` (person)
- `Oberlandesgerichts Innsbruck` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Schneidergruberweg 37, 5132 Reith, Österreich, vertreten durch Dr. Alois Schneider, Rechtsanwalt in Rattenberg, wider die beklagte Partei Dario von Ebers, vertreten durch Dr. Walter Hausberger, Dr. Katharina Moritz und Dr. Alfred Schmidt, Rechtsanwälte in Wörgl, wegen Entfernung und Unterlassung (Revisionsinteresse 10.000 EUR), infolge Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 3. November 2017, GZ 3 R 172/17s-22, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Rattenberg vom 17. Mai 2017, GZ 3 C 401/15k-18, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Stefula` (person)
- `Schneidergruberweg 37, 5132 Reith, Österreich` (address)
- `Dr. Alois Schneider` (person)
- `Dario von Ebers` (person)
- `Dr. Walter Hausberger` (person)
- `Dr. Katharina Moritz` (person)
- `Dr. Alfred Schmidt` (person)
- `Bezirksgerichts Rattenberg` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des minderjährigen Cedric Annamüller, geboren am 8. März 2007, 16. Mai 1964, vertreten durch das Land Kärnten als Kinder- und Jugendhilfeträger (Magistrat der Landeshauptstadt Klagenfurt, Abteilung für Jugend und Familie, Bahnhofstraße 35, 9010 Klagenfurt am Wörthersee), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Graz, gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 8. Jänner 2016, GZ 4 R 283/15g-16, womit der Beschluss des Bezirksgerichts Klagenfurt vom 17. November 2015, GZ 1 Pu 69/10x-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Klagenfurt` | `Landesgerichts Klagenfurt` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Ziegelbauer` (person)
- `Cedric Annamüller` (person)
- `8. März` (date)
- `16. Mai 1964` (date)
- `Oberlandesgerichts Graz` (organisation)
- `Bezirksgerichts Klagenfurt` (organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludmilla von Amelunxen, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, gegen die beklagte Partei Svetlana Leinhäuser, vertreten durch Dr. Thomas Brückl, Mag. Christian Breit, Rechtsanwälte in Ried im Innkreis, wegen 1.778,52 EUR und Unterlassung (Streitwert 2.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Wels als Berufungsgericht vom 25. Jänner 2023, GZ 21 R 2/23b-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Grieskirchen vom 27. Oktober 2022, GZ 3 C 642/20h-27, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts Wels` | `Landesgerichts Wels` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Mag. Schober` (person)
- `Dr. Annerl` (person)
- `Ludmilla von Amelunxen` (person)
- `Dr. Bernhard Birek` (person)
- `Svetlana Leinhäuser` (person)
- `Dr. Thomas Brückl` (person)
- `Mag. Christian Breit` (person)
- `Bezirksgerichts Grieskirchen` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_5`)


Anita Schetzel, vertreten durch die Summereder Pichler Wächter Rechtsanwälte GmbH in Leonding, wegen 12.750 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Wels als Berufungsgericht vom 13. Dezember 2023, GZ 21 R 277/23v-53, mit dem das Urteil des Bezirksgerichts Wels vom 23. August 2023, GZ 9 C 430/22s-47, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Die Revision wird in Ansehung der Klageforderungen von 2.700 EUR sA, 4.575 EUR sA und 450 EUR sA zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Wels` | `Landesgerichts Wels` |

**Missed by this rule (FN):**

- `Anita Schetzel` (person)
- `Bezirksgerichts Wels` (organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_93`)


Die nach den Vorgaben des Verfassungsgerichtshofs gebotene steuerliche Entlastung des Geldunterhaltspflichtigen basiert auf dem Modell der getrennten Haushaltsführung (vgl RIS-Justiz RS0117015), in dem ein Elternteil seine Unterhaltspflicht durch Betreuungsleistungen und der andere durch Geldleistungen (allenfalls kombiniert mit anzurechnenden Naturalleistungen) erfüllt. Bei getrennter Haushaltsführung hat die Familienbeihilfe die Funktion, Betreuungsleistungen abzugelten und die steuerliche Entlastung des Geldunterhaltspflichtigen zu bewirken (RIS-Justiz RS0117015 [T20]).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |

**Example 11** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_10`)


2008 erfolgte die Eintragung beim Firmenbuch des Landesgerichts Eisenstadt mit einer Niederlassung in Angyalföldstraße 52, 4193 Hayrl, Österreich.

| Predicted | Gold |
|---|---|
| `Landesgerichts Eisenstadt` | `Landesgerichts Eisenstadt` |

**Missed by this rule (FN):**

- `Angyalföldstraße 52, 4193 Hayrl, Österreich` (address)

**Example 12** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_5`)


Unter Alver GmbH, beide Granglitzweg 11, 3251 Kroißenberg, Österreich, beide vertreten durch Dr. Michael Schneditz-Bolfras und andere Rechtsanwälte in Gmunden, wegen Bucheinsicht (in eventu Rechnungslegung) und Zahlung (Streitwert: 70.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Teilurteil des Oberlandesgerichts Linz als Berufungsgericht vom 17. Februar 2014, GZ 3 R 13/14y-90, womit das Urteil des Landesgerichts Wels vom 27. November 2013 (in der mit Beschluss vom 12. Dezember 2013 berichtigten Fassung), GZ 2 Cg 78/10p-82 und -84, abgeändert wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts Wels` | `Landesgerichts Wels` |

**Missed by this rule (FN):**

- `Unter Alver GmbH` (organisation)
- `Granglitzweg 11, 3251 Kroißenberg, Österreich` (address)
- `Dr. Michael Schneditz-Bolfras` (person)
- `Oberlandesgerichts Linz` (organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Jaden Meyerjohann, geboren am 3. Juli 2020, Leroy Jungschmidt, geboren am 28. Mai 1965 und Clemens Theocharakis, geboren am 25. März 1999, in Pflege und Erziehung der Mutter Emanuela Janischefsky, vertreten durch das Land Vorarlberg als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Feldkirch, Schlossgraben 1, 6800 Feldkirch), wegen Gewährung von Unterhaltsvorschuss, über den Revisionsrekurs des Vaters Ashley Biesert, vertreten durch Mag. Hans-Christian Obernberger, Rechtsanwalt in Feldkirch, gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 12. Juli 2011, GZ 3 R 198/11g, 3 R 199/11d, 3 R 200/11a-18, womit die Beschlüsse des Bezirksgerichts Feldkirch vom 18. Mai 2011, GZ 12 Pu 141/11f-4 bis 6, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Jaden Meyerjohann` (person)
- `3. Juli 2020` (date)
- `Leroy Jungschmidt` (person)
- `28. Mai 1965` (date)
- `Clemens Theocharakis` (person)
- `25. März 1999` (date)
- `Emanuela Janischefsky` (person)
- `Bezirkshauptmannschaft Feldkirch` (organisation)
- `Ashley Biesert` (person)
- `Mag. Hans-Christian Obernberger` (person)
- `Bezirksgerichts Feldkirch` (organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch und Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der minderjährigen Karsten Alberter, geboren am 2. April 2010, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Wien-Umgebung, Fachgebiet Jugendwohlfahrt), 3400 Klosterneuburg, Leopoldstraße 21, über das als „Berufung“ bezeichnete Rechtsmittel des Vaters Helmut Dreilich, gegen den Beschluss des Landesgerichts Korneuburg als Rekursgericht vom 25. März 2013, GZ 23 R 30/13v-53, womit der Beschluss des Bezirksgerichts Schwechat vom 27. August 2012, GZ 8 Pu 190/11i-39, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.  Text Begründung: Verfahrensgegenstand ist die Festsetzung des gesetzlichen Unterhalts für die mj Lena Amini.

| Predicted | Gold |
|---|---|
| `Landesgerichts Korneuburg` | `Landesgerichts Korneuburg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Karsten Alberter` (person)
- `2. April 2010` (date)
- `Helmut Dreilich` (person)
- `Bezirksgerichts Schwechat` (organisation)
- `Lena Amini` (person)

**Example 15** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Karim Mielewczik, gegen die beklagte Partei Dr. Sandro Gädecken, vertreten durch Ing. Dr. Stefan Krall und Dr. Oliver Kühnl, Rechtsanwälte in Innsbruck, wegen 9.456 EUR sA (Revisionsinteresse 9.268,50 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 25. Februar 2025, GZ 21 R 434/24f-29, mit dem das Urteil des Bezirksgerichts Seekirchen am Wallersee vom 5. September 2024, GZ 2 C 1107/23d-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Hon.-Prof. PD Dr. Rassi` (person)
- `Dr. Annerl` (person)
- `Dr. Vollmaier` (person)
- `Dr. Wallner-Friedl` (person)
- `Karim Mielewczik` (person)
- `Dr. Sandro Gädecken` (person)
- `Ing. Dr. Stefan Krall` (person)
- `Dr. Oliver Kühnl` (person)
- `Bezirksgerichts Seekirchen` (organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/10Ob3_12g`) (sent_id: `deanon_260716_TRAIN/10Ob3_12g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Maja Pirkmayr, vertreten durch Dr. Georg Gorton und DDr. Birgit Gorton, Rechtsanwälte in Klagenfurt, gegen die beklagte Partei Ing. Emanuel Puff, vertreten durch Dr. Gottfried Kassin, Rechtsanwalt in St. Veit an der Glan, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 26. Mai 2011, GZ 2 R 83/11z-49, mit dem das Urteil des Bezirksgerichts St. Veit an der Glan vom 29. Oktober 2010, GZ 3 C 333/09h-34, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Klagenfurt` | `Landesgerichts Klagenfurt` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Maja Pirkmayr` (person)
- `Dr. Georg Gorton` (person)
- `DDr. Birgit Gorton` (person)
- `Ing. Emanuel Puff` (person)
- `Dr. Gottfried Kassin` (person)

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_5`)


Dr. Felix Cornils, Niederlande, beide vertreten durch Tramposch & Partner, Rechtsanwälte KG in Innsbruck, gegen die beklagte Partei Mag.a Constanze Rizzo, vertreten durch König Ermacora Klotz & Partner, Rechtsanwälte in Innsbruck, wegen je 15.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 1. Juli 2020, GZ 10 R 16/20h-49, mit dem das Urteil des Landesgerichts Innsbruck vom 6. Februar 2020, GZ 41 Cg 11/19i-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Dr. Felix Cornils` (person)
- `Tramposch & Partner, Rechtsanwälte KG` (organisation)
- `Mag.a Constanze Rizzo` (person)
- `Oberlandesgerichts Innsbruck` (organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob6_24s`) (sent_id: `deanon_260716_TRAIN/10Ob6_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Dr. Weber, Mag. Schober, Dr. Annerl und Dr. Vollmaier als weitere Richter in der Rechtssache des (ehemaligen) Klägers und Gegners der gefährdeten Parteien Agatha von der Heide, vertreten durch MMag. Dr. Sebastian Pribas, Rechtsanwalt in Dornbirn, als Verfahrenshelfer, dieser vertreten durch Mag. Benedikt Walch, Rechtsanwalt in Lech am Arlberg, gegen die (ehemals) Beklagte und erstgefährdete Partei Alva Sengül, sowie die zweitgefährdete Partei mj Selina Birkmeir, und die drittgefährdete Partei mj Harald Ladwig, LLM, alle wohnhaft in In der Klaus 72, 4785 Bach, Österreich, und vertreten durch Mag. German Bertsch, Rechtsanwalt in Feldkirch, wegen Ehescheidung sowie einstweiligem Ehegatten- und Kindesunterhalt, über den außerordentlichen Revisionsrekurs des Gegners der gefährdeten Parteien gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 22. September 2022, GZ 3 R 187/22f-323, womit der Beschluss des Bezirksgerichts Feldkirch vom 29. April 2022, GZ 2 C 23/17g-306, bestätigt wurde, den Beschluss gefasst:  Spruch In Ansehung der auf Zahlung von einstweiligem Ehegattenunterhalt gerichteten Begehren wird der außerordentliche Revisionsrekurs gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Dr. Weber` (person)
- `Mag. Schober` (person)
- `Dr. Annerl` (person)
- `Dr. Vollmaier` (person)
- `Agatha von der Heide` (person)
- `MMag. Dr. Sebastian Pribas` (person)
- `Mag. Benedikt Walch` (person)
- `Alva Sengül` (person)
- `Selina Birkmeir` (person)
- `Harald Ladwig, LLM` (person)
- `In der Klaus 72, 4785 Bach, Österreich` (address)
- `Mag. German Bertsch` (person)
- `Bezirksgerichts Feldkirch` (organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_91`)


Das Berufungsgericht sehe sich daher nicht zu einer Antragstellung an den Verfassungsgerichtshof veranlasst.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 20** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_147`)


2. Seine Anregung, ein Gesetzesprüfungsver-fahren beim Verfassungsgerichtshof bezüglich der „von der beklagten Partei ins Treffen geführten gesetzlichen Bestimmungen“ einzuleiten, begründet der Kläger mit einer Verletzung des Gleichheitssatzes.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 21** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_158`)


Mangelhaft soll das Berufungsverfahren deshalb geblieben sein, weil das Berufungsgericht keinen Antrag an den Verfassungsgerichtshof gestellt hat: Hat der Oberste Gerichtshof oder ein zur Entscheidung in zweiter Instanz zuständiges Gericht gegen die Anwendung eines (Bundes- oder Landes-)Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken, so ist nach Art 89 Abs 2 B-VG von Amts wegen der Antrag auf Aufhebung dieses Gesetzes beim Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_159`)


Nach einhelliger Rechtsprechung steht den Parteien eines Gerichtsverfahrens kein Recht auf Antragstellung hinsichtlich einer Befassung des Verfassungsgerichtshofs zu. Die Parteien können eine solche Antragstellung nur anregen (RIS-Justiz RS0056514;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |

**Example 23** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_162`)


Unterlässt ein Gericht die Anfechtung einer Norm beim Verfassungsgerichtshof, steht dagegen nach ständiger Rechtsprechung keiner Partei ein Rechtsmittel zu (RIS-Justiz RS0056514 [T10]).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 24** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Roland Soukup, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Dr. Gabriele Griehsel` (person)
- `Dr. Wolfgang Kozak` (person)
- `Roland Soukup` (person)
- `Mahringer Steinwender Bestebner Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Linz` (organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_3`)


Kopf Der Oberste Gerichtshof hat am 15. Jänner 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart der Richteramtsanwärterin Dr. Parapatits als Schriftführerin, in der Strafsache gegen Bernhard Buddäus und Norbert Wehrhahn wegen des Verbrechens des schweren Betrugs nach §§ 146, 147 Abs 3 StGB über die Nichtigkeitsbeschwerde und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 29. März 2012, GZ 31 Hv 51/10y-84, nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Angeklagten sowie des Verteidigers des Zweitangeklagten Mag. Rienmüller zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Zehetner` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Mag. Lendl` (person)
- `Mag. Michel` (person)
- `Dr. Oshidari` (person)
- `Dr. Parapatits` (person)
- `Bernhard Buddäus` (person)
- `Norbert Wehrhahn` (person)
- `Mag. Höpler` (person)
- `Mag. Rienmüller` (person)

**Example 26** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_3`)


Kopf Der Oberste Gerichtshof hat am 17. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Sommer als Schriftführer, in der Strafsache gegen Richard Lindt wegen des Vergehens der vorsätzlichen Beeinträchtigung der Umwelt nach § 180 Abs 2 Z 1, Z 2 StGB und einer weiteren strafbaren Handlung, AZ 40 Hv 147/10g des Landesgerichts Salzburg, über die Beschwerde des Genannten gegen den Beschluss dieses Gerichts vom 7. September 2011, ON 547, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Zehetner` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Mag. Lendl` (person)
- `Mag. Michel` (person)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Sommer` (person)
- `Richard Lindt` (person)

**Example 27** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_4`)


Gründe:  Rechtliche Beurteilung Mit dem angefochtenen Beschluss wurde die von Richard Lilienfein erhobene Nichtigkeitsbeschwerde gegen das Urteil des Landesgerichts Salzburg vom 17. Juni 2011, GZ 40 Hv 147/10g-538, als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Richard Lilienfein` (person)

**Example 28** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_8`)


Die von Richard Leissner gegen das ihn freisprechende Urteil des Einzelrichters des Landesgerichts Salzburg vom 17. Juni 2011 ausdrücklich an den Obersten Gerichtshof gerichtete Nichtigkeitsbeschwerde wurde vom Erstgericht zutreffend gemäß § 285a Z 1 StPO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Richard Leissner` (person)
- `Obersten Gerichtshof` (organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/11Os67_16m`) (sent_id: `deanon_260716_TRAIN/11Os67_16m_3`)


Kopf Der Oberste Gerichtshof hat am 13. September 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Rathgeb als Schriftführerin in der Strafsache gegen Daniel Kur wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 1 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 22. April 2016, GZ 22 Hv 14/16s-43, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Michel` (person)
- `Mag. Fürnkranz` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oberressl` (person)
- `Mag. Rathgeb` (person)
- `Daniel Kur` (person)

**Example 30** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_4`)


Augst 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Vizepräsidentin des Obersten Gerichtshofs Mag. Marek, die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Wieser als Schriftführerin in der Maßnahmenvollzugssache des Gerald Winand wegen bedingter Nachsicht einer mit Freiheitsentziehung verbundenen vorbeugenden Maßnahme (§ 21 Abs 1 StGB) über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien vom 16. Mai 2018, AZ 22 Bs 119/18p (AZ 606 Hv 1/17k des Landesgerichts Korneuburg), nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Korneuburg` | `Landesgerichts Korneuburg` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Marek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Fürnkranz` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oberressl` (person)
- `Mag. Wieser` (person)
- `Gerald Winand` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_5`)


Gründe:  Rechtliche Beurteilung Der gegen den Beschluss des Oberlandesgerichts Wien, mit dem eine Beschwerde des Gerald Wandscheer gegen den Beschluss des Landesgerichts Korneuburg vom 21. Februar 2018, GZ 606 Hv 1/17k-94, als verspätet zurückgewiesen worden war, gerichtete „Einspruch“ war ebenso zurückzuweisen, weil gegen derartige Entscheidungen eines Beschwerdegerichts kein weiterer Rechtszug vorgesehen ist (§ 89 Abs 6 StPO).

| Predicted | Gold |
|---|---|
| `Landesgerichts Korneuburg` | `Landesgerichts Korneuburg` |

**Missed by this rule (FN):**

- `Oberlandesgerichts Wien` (organisation)
- `Gerald Wandscheer` (person)

**Example 32** (doc_id: `deanon_260716_TRAIN/12Ns94_11m`) (sent_id: `deanon_260716_TRAIN/12Ns94_11m_3`)


Kopf Der Oberste Gerichtshof hat am 28. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in der Strafsache gegen Mag. Herwig Bernts wegen des Vergehens des Widerstands gegen die Staatsgewalt nach § 269 Abs 1 erster Fall StGB und anderer strafbarer Handlungen, AZ 20 Hv 38/11f des Landesgerichts Linz, über den Antrag des Angeklagten auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

| Predicted | Gold |
|---|---|
| `Landesgerichts Linz` | `Landesgerichts Linz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Herwig Bernts` (person)
- `OGH` (organisation)

**Example 33** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__9`)


Unter einem erging der Beschluss, gemäß § 494a Abs 1 Z 2 StPO vom Widerruf der zum AZ 36 Hv 118/05p des Landesgerichts Innsbruck und zum AZ 3 U 350/06d des Bezirksgerichts Kufstein jeweils gewährten bedingten Strafnachsicht abzusehen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Bezirksgerichts Kufstein` (organisation)

**Example 34** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_3`)


Kopf Der Oberste Gerichtshof hat am 12. September 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart der Richteramtsanwärterin Mag. Ruckendorfer als Schriftführerin in der Strafsache gegen Thomas Leutz wegen des Verbrechens des gewerbsmäßigen schweren Betrugs nach §§ 146, 147 Abs 1 Z 1, Abs 3, 148 zweiter Fall, 15 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 13. September 2018, GZ 35 Hv 46/18m-130, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Dr. Brenner` (person)
- `Dr. Setz-Hummel` (person)
- `Mag. Ruckendorfer` (person)
- `Thomas Leutz` (person)

**Example 35** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_4`)


In Stattgebung der Nichtigkeitsbeschwerde wird das angefochtene Urteil, das im Übrigen unberührt bleibt, im Ausspruch über den Verfall aufgehoben, soweit er sich auf einen 35.353,95 Euro übersteigenden Betrag bezieht, und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an den Einzelrichter des Landesgerichts Innsbruck verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Example 36** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_26`)


In Stattgebung der Nichtigkeitsbeschwerde des Angeklagten war daher das angefochtene Urteil wie im Spruch ersichtlich aufzuheben und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an den Einzelrichter des Landesgerichts Innsbruck (§ 445 Abs 2 StPO;

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Example 37** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_3`)


Kopf Der Oberste Gerichtshof hat am 5. März 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden, die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Brenner als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Kaltenbrunner als Schriftführerin in der Strafsache gegen Johannes Barkhof wegen des Vergehens der fortgesetzten Gewaltausübung nach § 107b Abs 1 und Abs 2 StGB und weiterer strafbarer Handlungen, AZ 51 Hv 32/13i des Landesgerichts Feldkirch, über die von der Generalprokuratur gegen den Beschluss des genannten Gerichts vom 4. Mai 2014, GZ 51 Hv 32/13i-35, und weitere Vorgänge erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Eisenmenger, und der Verteidigerin Mag. Reisinger zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Dr. Brenner` (person)
- `Mag. Kaltenbrunner` (person)
- `Johannes Barkhof` (person)
- `Dr. Eisenmenger` (person)
- `Mag. Reisinger` (person)

**Example 38** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_4`)


Im Verfahren AZ 51 Hv 32/13i des Landesgerichts Feldkirch, verletzt die Unterlassung der nachstehend angeführten Zustellungen an den gesetzlichen Vertreter des jugendlichen Beschuldigten Johannes Büffel das Gesetz, und zwar 1./ des Antrags der Staatsanwaltschaft vom 12. März 2014 auf Wiederaufnahme des Strafverfahrens (ON 29) zur Gegenäußerung binnen 14 Tagen in § 38 Abs 1 JGG iVm § 357 Abs 2 erster Satz StPO; 2./ des Beschlusses vom 4. Mai 2014 auf Wiederaufnahme des Strafverfahrens (ON 35) in § 38 Abs 3 erster Satz JGG iVm § 86 Abs 2 StPO iVm § 87 Abs 1 StPO.

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Johannes Büffel` (person)

**Example 39** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_6`)


Text Gründe: In der Jugendstrafsache AZ 51 Hv 32/13i des Landesgerichts Feldkirch legte die Staatsanwaltschaft Feldkirch mit Strafantrag vom 18. April 2013, AZ 9 St 82/13f, dem am 23. August 1996 geborenen Angeklagten Johannes Bednorz als Vergehen der fortgesetzten Gewaltausübung nach § 107b Abs 1 und Abs 2 StGB (I./) sowie der Nötigung nach den §§ 15 Abs 1, 105 Abs 1 StGB (II./, III./1./), der gefährlichen Drohung nach § 107 Abs 1 StGB (III./2./) und der Sachbeschädigung nach § 125 StGB (III./3./) qualifiziertes Verhalten zum Nachteil der Sabrina Hemmersdorfer zur Last (ON 3).

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Johannes Bednorz` (person)
- `Sabrina Hemmersdorfer` (person)

**Example 40** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_7`)


Mit gekürzt ausgefertigtem Urteil der Einzelrichterin in Jugendstrafsachen des Landesgerichts Feldkirch vom 5. Juni 2013 wurde der jugendliche Angeklagte mehrerer Vergehen schuldig erkannt, jedoch von der Anklage (I./), er habe in Heinrich-Prosl-Gasse 6, 2034 Großharras, Österreich im Zeitraum von März 2012 bis Ende Februar 2013 gegen Sabrina Höllerl eine längere Zeit hindurch fortgesetzt Gewalt ausgeübt, indem er sie mehr als zehnmal mit Fäusten gegen den Bauch und gegen das Gesicht geschlagen habe, wodurch diese teilweise Prellungen und Schürfwunden erlitten habe, mangels Schuldbeweises gemäß § 259 Z 3 StPO freigesprochen (ON 14).

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Heinrich-Prosl-Gasse 6, 2034 Großharras, Österreich` (address)
- `Sabrina Höllerl` (person)

**Example 41** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_8`)


Aus Anlass des ihre polizeilichen Angaben abschwächenden und zum oben angeführten Freispruch führenden Aussageverhaltens der Zeugin Sabrina Härtel in der Hauptverhandlung vom 5. Juni 2013 (ON 13 S 5 ff) erhob die Staatsanwaltschaft Feldkirch am 20. Juni 2013 zu AZ 9 St 131/13m in der Jugendstrafsache AZ 20 Hv 68/13f des Landesgerichts Feldkirch Strafantrag (ON 4 des zuletzt bezeichneten Aktes) gegen die Genannte wegen des Verdachts der am 8. März 2013 und am 15. März 2013 in Franz Schuster-Straße 8, 8212 Kleinpesendorf, Österreich im Ermittlungsverfahren gegen Johannes Breenkötter begangenen Vergehen der falschen Beweisaussage nach § 288 Abs 1 und Abs 4 StGB (I./) sowie der Verleumdung nach § 297 Abs 1 zweiter Fall StGB (II./).

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Sabrina Härtel` (person)
- `Franz Schuster-Straße 8, 8212 Kleinpesendorf, Österreich` (address)
- `Johannes Breenkötter` (person)

**Example 42** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_9`)


Nachdem die Angeklagte Sabrina Heckel in der Hauptverhandlung am 24. Juli 2013 angegeben hatte, als Zeugin nicht vor der Polizei, sondern in der Hauptverhandlung am 5. Juni 2013 gegen Johannes Butze falsch ausgesagt zu haben, gab die Staatsanwaltschaft noch in dieser Hauptverhandlung eine Alternativanklage zu Protokoll, der zufolge sie als Zeugin in der Hauptverhandlung am 5. Juni 2013 gegen Johannes Bulthaup vor dem Landesgericht Feldkirch die Vergehen der falschen Beweisaussage nach § 288 Abs 1 StGB (III./) und der Begünstigung nach § 299 Abs 1 StGB (IV./) begangen habe (ON 10 S 3 f des Aktes AZ 51 Hv 46/13y des Landesgerichts Feldkirch).

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Sabrina Heckel` (person)
- `Johannes Butze` (person)
- `Johannes Bulthaup` (person)
- `Landesgericht Feldkirch` (organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_10`)


Mit gekürzt ausgefertigtem Urteil des Landesgerichts Feldkirch vom 2. September 2013, GZ 20 Hv 68/13f-13, wurde Sabrina Harrazin im Sinne dieser Alternativanklage schuldig erkannt.

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Sabrina Harrazin` (person)

**Example 44** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_11`)


Hierauf beantragte die Staatsanwaltschaft Feldkirch in dem Johannes Bergknecht betreffenden Verfahren AZ 51 Hv 32/13i des Landesgerichts Feldkirch am 12. März 2014 gemäß § 355 StPO iVm § 352 Abs 1 Z 1 StPO die Wiederaufnahme des Strafverfahrens im Umfang des am 5. Juni 2013 ergangenen Freispruchs des Angeklagten Johannes Bertrang, weil dieser durch die falsche Beweisaussage der Zeugin Sabrina Holzschuher herbeigeführt worden sei (ON 29).

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Johannes Bergknecht` (person)
- `Johannes Bertrang` (person)
- `Sabrina Holzschuher` (person)

**Example 45** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_13`)


Mit Beschluss des Einzelrichters des Landesgerichts Feldkirch vom 4. Mai 2014, GZ 51 Hv 32/13i-35, wurde in Stattgebung des Antrags der Staatsanwaltschaft das Strafverfahren gegen Johannes Braentel wegen § 107b Abs 1 und Abs 2 StGB gemäß § 355 StPO im Umfang des rechtskräftigen Freispruchs wiederaufgenommen und das Urteil des Landesgerichts Feldkirch vom 5. Juni 2013 (ON 14) umfänglich des Freispruchs aufgehoben.

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Johannes Braentel` (person)

**Example 46** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_15`)


Die Staatsanwaltschaft Feldkirch erhob am 14. August 2014 zu AZ 9 St 82/13f hinsichtlich des dem seinerzeitigen Freispruch zu Grunde liegenden Vorwurfs Strafantrag gegen Johannes Brookhoff (ON 36 in dem das wiederaufgenommene Verfahren betreffenden Akt AZ 39 Hv 64/14h des Landesgerichts Feldkirch).

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Johannes Brookhoff` (person)

**Example 47** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_16`)


Anlässlich der Ausschreibung der Hauptverhandlung im wiederaufgenommenen Verfahren für den 24. September 2014 wurde dem Angeklagten ein Verfahrenshilfeverteidiger beigegeben (ON 38 im Akt AZ 39 Hv 64/14h des Landesgerichts Feldkirch).

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Example 48** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_18`)


Am 1. Oktober 2014 verfügte das Landesgericht Feldkirch die Zustellung der „ON 35“ (gemeint sichtlich: des Beschlusses auf Wiederaufnahme des Strafverfahrens ON 35 im Akt AZ 51 Hv 32/13i und ON 47 im Akt AZ 39 Hv 64/14h jeweils des Landesgerichts Feldkirch) an „die Erziehungsberechtigte des Johannes Bauckloh “, worauf der seinerzeitigen gesetzlichen Vertreterin (der Mutter) des nunmehr volljährigen Angeklagten der Beschluss am 3. Oktober 2014 eigenhändig zugestellt wurde (ON 42 S 3).

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Landesgericht Feldkirch` (organisation)
- `Johannes Bauckloh` (person)

**Example 49** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_19`)


Am 17. Oktober 2014 langte beim Landesgericht Feldkirch zu AZ 51 Hv 32/13i eine vom Verfahrenshilfeverteidiger im Verfahren AZ 39 Hv 64/14h dieses Landesgerichts verfasste Beschwerde des Angeklagten Johannes Bartlmäß (ON 42 im Akt AZ 51 Hv 32/13i des Landesgerichts Feldkirch) gegen den Beschluss des Landesgerichts Feldkirch vom 4. Mai 2014 auf Wiederaufnahme des Strafverfahrens ein.

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Landesgericht Feldkirch` (organisation)
- `Johannes Bartlmäß` (person)

**Example 50** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_20`)


Mit Beschluss des Oberlandesgerichts Innsbruck als Beschwerdegericht vom 25. November 2014, AZ 11 Bs 326/14z, 349/14g (ON 47 im Akt AZ 51 Hv 32/13i des Landesgerichts Feldkirch bzw ON 52 im Akt AZ 39 Hv 64/14h dieses Landesgerichts), wurde die Beschwerde als unzulässig (verspätet) zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Oberlandesgerichts Innsbruck` (organisation)

**Example 51** (doc_id: `deanon_260716_TRAIN/13Os105_19v`) (sent_id: `deanon_260716_TRAIN/13Os105_19v_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Lendl, Mag. Michel und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Roman Ueberlein und einen weiteren Angeklagten wegen des Verbrechens des schweren gewerbsmäßig durch Einbruch begangenen Diebstahls nach §§ 127, 128 Abs 1 Z 5, 129 Abs 2 Z 1 (iVm Abs 1 Z 1), 130 Abs 3 (iVm Abs 1 erster Fall) und 15 StGB sowie einer weiteren strafbaren Handlung, AZ 37 Hv 122/18b des Landesgerichts Innsbruck, über den Antrag des Verurteilten Roman Urbath auf Erneuerung des Strafverfahrens nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Mag. Lendl` (person)
- `Mag. Michel` (person)
- `Dr. Brenner` (person)
- `Dr. Ondreasova` (person)
- `Roman Ueberlein` (person)
- `Roman Urbath` (person)

**Example 52** (doc_id: `deanon_260716_TRAIN/13Os105_19v`) (sent_id: `deanon_260716_TRAIN/13Os105_19v_4`)


Text Gründe: Mit Urteil des Landesgerichts Innsbruck als Schöffengericht vom 19. November 2018, GZ 37 Hv 122/18b-17, wurde – soweit hier von Bedeutung – Roman Ungetühm mehrerer strafbarer Handlungen schuldig erkannt und zu einer Freiheitsstrafe verurteilt. Mit Beschluss vom 2. April 2019, GZ 11 Os 22/19y-4, wies der Oberste Gerichtshof die von Roman Ulucan dagegen aus Z 11 des § 281 Abs 1 StPO erhobene Nichtigkeitsbeschwerde gemäß § 285d Abs 1 StPO bei nichtöffentlicher Beratung sofort zurück.

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Roman Ungetühm` (person)
- `Oberste Gerichtshof` (organisation)
- `Roman Ulucan` (person)

**Example 53** (doc_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a__3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Zoltan Schoenwiese wegen des Verbrechens des gewerbsmäßig und als Mitglied einer kriminellen Vereinigung durch Einbruch begangenen schweren Diebstahls nach §§ 127, 128 Abs 2, 129 Abs 1 Z 1, 130 Abs 1 erster und zweiter Fall, Abs 2 erster und zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 25 Hv 30/17m des Landesgerichts Eisenstadt, über die von der Generalprokuratur gegen das Urteil dieses Gerichts vom 6. Juni 2017 (ON 155) und einen Vorgang erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, und der Verteidigerin Mag. Urak zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts Eisenstadt` | `Landesgerichts Eisenstadt` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Dr. Ondreasova` (person)
- `Zoltan Schoenwiese` (person)
- `Mag. Höpler` (person)
- `Mag. Urak` (person)

**Example 54** (doc_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a__4`)


In der Strafsache AZ 25 Hv 30/17m des Landesgerichts Eisenstadt verletzt die Unterlassung der Verlesung des Europäischen Haftbefehls vom 27. Juli 2015 (ON 44) und der Mitteilung des ungarischen Justizministeriums vom 26. November 2015 (ON 125) in der Hauptverhandlung (ON 154) § 252 Abs 2 StPO.

| Predicted | Gold |
|---|---|
| `Landesgerichts Eisenstadt` | `Landesgerichts Eisenstadt` |

**Example 55** (doc_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a__5`)


Das Urteil des Landesgerichts Eisenstadt vom 6. Juni 2017 (ON 155) wird aufgehoben, eine neue Hauptverhandlung angeordnet und die Sache an das Landesgericht Eisenstadt verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Eisenstadt` | `Landesgerichts Eisenstadt` |

**Missed by this rule (FN):**

- `Landesgericht Eisenstadt` (organisation)

**Example 56** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__3`)


Kopf Der Oberste Gerichtshof hat am 11. Oktober 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Nikola Manderscheidt wegen des Vergehens des schweren Betrugs nach §§ 12 dritter Fall, 146, 147 Abs 1 Z 1 StGB, AZ 41 Hv 49/15k des Landesgerichts Salzburg, über die von der Generalprokuratur gegen das Urteil des Landesgerichts Salzburg vom 28. Oktober 2015, GZ 41 Hv 49/15k-33, und den unter einem gefassten Beschluss auf Absehen vom Widerruf einer bedingten Strafnachsicht erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin MMag. Jenichl, des Verurteilten sowie seines Verteidigers Mag. Wolm zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Mag. Wetter` (person)
- `Nikola Manderscheidt` (person)
- `MMag. Jenichl` (person)
- `Mag. Wolm` (person)

**Example 57** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__4`)


Es verletzen (1) das Urteil des Landesgerichts Salzburg als Schöffengericht vom 28. Oktober 2015, GZ 41 Hv 49/15k-33, § 31 Abs 1 erster Satz StGB und (2) der unter einem verkündete Beschluss auf Absehen vom Widerruf der Nikola Mehlhose mit Urteil des Landesgerichts Salzburg vom 10. September 2014, GZ 47 Hv 86/14v-7, gewährten bedingten Strafnachsicht § 494a Abs 1 Z 2 StPO.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Nikola Mehlhose` (person)

**Example 58** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__5`)


Das Urteil des Landesgerichts Salzburg als Schöffengericht vom 28. Oktober 2015, GZ 41 Hv 49/15k-33, das im Übrigen unberührt bleibt, wird im Nikola Meine betreffenden Strafausspruch aufgehoben und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an das Landesgericht Salzburg verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Nikola Meine` (person)
- `Landesgericht Salzburg` (organisation)

**Example 59** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__6`)


Gründe:  Rechtliche Beurteilung Mit in Rechtskraft erwachsenem Urteil des Landesgerichts Salzburg vom 10. September 2014, GZ 47 Hv 86/14v-7, wurde Nikola Miscenko wegen des Vergehens des Betrugs nach § 146 StGB zu einer unter Bestimmung einer dreijährigen Probezeit bedingt nachgesehenen Freiheitsstrafe von vier Monaten verurteilt. Mit Urteil des Landesgerichts Salzburg vom 28. Oktober 2015, GZ 41 Hv 49/15k-33, das auch einen Schuldspruch eines anderen Angeklagten enthält, wurde der Genannte wegen eines am 27. Mai 2012 begangenen Vergehens schuldig erkannt und hierfür eine weitere Sanktion verhängt.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Nikola Miscenko` (person)

**Example 60** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__7`)


Unter einem fasste das Gericht neben anderen Aussprüchen auch den Beschluss, vom Widerruf der Nikola Mikeska mit Urteil des Landesgerichts Salzburg vom 10. September 2014, GZ 47 Hv 86/14v-7, gewährten bedingten Strafnachsicht abzusehen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Nikola Mikeska` (person)

**Example 61** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__10`)


Da das Urteil des Landesgerichts Salzburg als Schöffengericht vom 28. Oktober 2015 auf das Erkenntnis vom 10. September 2014 nicht Bedacht nimmt, verstößt es gegen die genannte Bestimmung.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Example 62** (doc_id: `deanon_260716_TRAIN/13Os126_17d`) (sent_id: `deanon_260716_TRAIN/13Os126_17d_3`)


Kopf Der Oberste Gerichtshof hat am 6. Dezember 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Schuber als Schriftführer in der Strafsache gegen Mehdi Rekemeyer wegen des Verbrechens des Raubes nach §§ 15, 142 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 19. Juli 2017, GZ 63 Hv 56/17d-44, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Anordnung von Bewährungshilfe nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Mag. Schuber` (person)
- `Mehdi Rekemeyer` (person)

**Example 63** (doc_id: `deanon_260716_TRAIN/13Os16_15z`) (sent_id: `deanon_260716_TRAIN/13Os16_15z_4`)


Gründe:  Rechtliche Beurteilung Mit dem angefochtenen Beschluss wies das Oberlandesgericht Linz die Beschwerde des Herbert Oehlschlager gegen den Beschluss des Landesgerichts Wels vom 19. November 2014, AZ 24 Bl 81/14h (ON 9 der Ermittlungsakten), mit dem der Antrag des Genannten auf Fortführung des Verfahrens zurückgewiesen worden war, gemäß § 196 Abs 1 erster Satz StPO zurück (ON 12 der Ermittlungsakten).

| Predicted | Gold |
|---|---|
| `Landesgerichts Wels` | `Landesgerichts Wels` |

**Missed by this rule (FN):**

- `Oberlandesgericht Linz` (organisation)
- `Herbert Oehlschlager` (person)

**Example 64** (doc_id: `deanon_260716_TRAIN/13Os74_17g`) (sent_id: `deanon_260716_TRAIN/13Os74_17g_3`)


Kopf Der Oberste Gerichtshof hat am 6. September 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Michael Wakup wegen des Verbrechens des sexuellen Missbrauchs einer wehrlosen oder psychisch beeinträchtigten Person nach §§ 15, 205 Abs 1 StGB sowie weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Linz als Schöffengericht vom 21. März 2017, GZ 22 Hv 1/17p-32, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Widerruf bedingter Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Linz` | `Landesgerichts Linz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Mag. Wetter` (person)
- `Michael Wakup` (person)

**Example 65** (doc_id: `deanon_260716_TRAIN/13Os78_12p`) (sent_id: `deanon_260716_TRAIN/13Os78_12p_3`)


Kopf Der Oberste Gerichtshof hat am 30. August 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Temper als Schriftführerin in der Strafsache gegen Michael Lengjel und andere Beschuldigte wegen des Vergehens des schweren Betrugs nach §§ 146, 147 Abs 2 StGB sowie weiterer strafbarer Handlungen, AZ 21 Bl 5/11k des Landesgerichts Innsbruck, über die Beschwerden der Anna Wynand und des DI Georg Lu Brian Waltemate gegen den Beschluss des Oberlandesgerichts Innsbruck vom 29. Mai 2012, AZ 6 Bs 220/12x, 221/12v, 222/12s, 223/12p und 224/12k, nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerden werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Marek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Dr. Oshidari` (person)
- `Mag. Temper` (person)
- `Michael Lengjel` (person)
- `Anna Wynand` (person)
- `Brian Waltemate` (person)
- `Oberlandesgerichts Innsbruck` (organisation)

**Example 66** (doc_id: `deanon_260716_TRAIN/13Os78_12p`) (sent_id: `deanon_260716_TRAIN/13Os78_12p_4`)


Gründe:  Rechtliche Beurteilung Mit dem angefochtenen Beschluss wies das Oberlandesgericht Innsbruck die Beschwerden der Anna Waniek und des DI Georg Lu Carla Hanel gegen mehrere Verfügungen des Vorsitzenden eines Drei-Richter-Senats des Landesgerichts Innsbruck als unzulässig zurück.

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Oberlandesgericht Innsbruck` (organisation)
- `Anna Waniek` (person)
- `Carla Hanel` (person)

**Example 67** (doc_id: `deanon_260716_TRAIN/13Os97_11f`) (sent_id: `deanon_260716_TRAIN/13Os97_11f_3`)


Kopf Der Oberste Gerichtshof hat am 25. August 2011 durch den Vizepräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Ratz als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in Gegenwart der Richteramtsanwärterin Mag. Einwagner als Schriftführerin in der Strafsache gegen Ernst Grießbaum wegen Verbrechen des sexuellen Missbrauchs einer wehrlosen oder psychisch beeinträchtigten Person nach §§ 205 Abs 1 und 15 StGB sowie einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 5. Jänner 2011, GZ 39 Hv 110/09g-63, nach Einsichtnahme durch die Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde und die Berufung wegen des Ausspruchs über die Schuld werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Ratz` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Marek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Mag. Einwagner` (person)
- `Ernst Grießbaum` (person)

**Example 68** (doc_id: `deanon_260716_TRAIN/13Os99_19m`) (sent_id: `deanon_260716_TRAIN/13Os99_19m_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Christoph Holthuijsen wegen des Verbrechens der schweren Körperverletzung nach § 84 Abs 4 StGB, AZ 18 Hv 37/19b des Landesgerichts Klagenfurt, über die von der Generalprokuratur gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 21. August 2019, AZ 10 Bs 221/19d, ergriffene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Verteidigerin Mag. Sternad und des Privatbeteiligtenvertreters Mag. Höllwerth zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts Klagenfurt` | `Landesgerichts Klagenfurt` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Dr. Ondreasova` (person)
- `Christoph Holthuijsen` (person)
- `Oberlandesgerichts Graz` (organisation)
- `Mag. Höpler` (person)
- `Mag. Sternad` (person)
- `Mag. Höllwerth` (person)

**Example 69** (doc_id: `deanon_260716_TRAIN/13Os99_19m`) (sent_id: `deanon_260716_TRAIN/13Os99_19m_5`)


Text Gründe: Mit Urteil des Landesgerichts Klagenfurt als Einzelrichter vom 13. Mai 2019 (ON 20) wurde Christoph Huertler des Verbrechens der schweren Körperverletzung nach § 84 Abs 4 StGB schuldig erkannt und zu einer Geldstrafe sowie dazu verurteilt, dem Privatbeteiligten Fabian Pfandler 500 Euro Schmerzengeld zu zahlen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Klagenfurt` | `Landesgerichts Klagenfurt` |

**Missed by this rule (FN):**

- `Christoph Huertler` (person)
- `Fabian Pfandler` (person)

**Example 70** (doc_id: `deanon_260716_TRAIN/14Os120_15a`) (sent_id: `deanon_260716_TRAIN/14Os120_15a_3`)


Kopf Der Oberste Gerichtshof hat am 15. Dezember 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Rechtspraktikantin Mag. Jukic als Schriftführerin im Verfahren zur Unterbringung des Rudolf Kuralay in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Betroffenen gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 16. September 2015, GZ 24 Hv 90/15x-32, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Philipp` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Hetlinger` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Mann` (person)
- `Mag. Jukic` (person)
- `Rudolf Kuralay` (person)

**Example 71** (doc_id: `deanon_260716_TRAIN/14Os19_16z`) (sent_id: `deanon_260716_TRAIN/14Os19_16z_3`)


Kopf Der Oberste Gerichtshof hat am 12. April 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Fritsche als Schriftführerin im Verfahren zur Unterbringung des Thomas Menge in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Betroffenen gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 12. Jänner 2016, GZ 38 Hv 130/15g-53, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Philipp` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Hetlinger` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Mann` (person)
- `Mag. Fritsche` (person)
- `Thomas Menge` (person)

**Example 72** (doc_id: `deanon_260716_TRAIN/15Os115_18b`) (sent_id: `deanon_260716_TRAIN/15Os115_18b_3`)


Kopf Der Oberste Gerichtshof hat am 26. September 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Ertl, LL.M., als Schriftführer in der Strafsache gegen Arijan Peschak wegen des Verbrechens des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Wels als Schöffengericht vom 14. Juni 2018, GZ 39 Hv 7/18a-76, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Wels` | `Landesgerichts Wels` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Lendl` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Fürnkranz` (person)
- `Dr. Mann` (person)
- `Mag. Ertl, LL.M.` (person)
- `Arijan Peschak` (person)

**Example 73** (doc_id: `deanon_260716_TRAIN/15Os43_13g`) (sent_id: `deanon_260716_TRAIN/15Os43_13g_3`)


Kopf Der Oberste Gerichtshof hat am 22. Mai 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Danek als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Dr. Michel-Kwapinski und Mag. Fürnkranz als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Müller als Schriftführerin in der Strafsache gegen Manfred Backus wegen des Vergehens der Vorbereitung von Suchtgifthandel nach § 28 Abs 1 zweiter Satz, Abs 2, Abs 4 SMG und anderer strafbarer Handlungen über die von der Generalprokuratur gegen das Urteil des Landesgerichts Korneuburg vom 13. Juni 2012, GZ 505 Hv 5/11x-69, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Staatsanwalt Mag. Mugler, des Verurteilten sowie seiner Verteidiger Mag. Machac und Mag. Kessler, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts Korneuburg` | `Landesgerichts Korneuburg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Danek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Lendl` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Fürnkranz` (person)
- `Mag. Müller` (person)
- `Manfred Backus` (person)
- `Mag. Mugler` (person)
- `Mag. Machac` (person)
- `Mag. Kessler` (person)

**Example 74** (doc_id: `deanon_260716_TRAIN/15Os43_13g`) (sent_id: `deanon_260716_TRAIN/15Os43_13g_4`)


Das in gekürzter Form ausgefertigte Urteil des Landesgerichts Korneuburg vom 13. Juni 2012, GZ 505 Hv 5/11x-69, verletzt in Punkt A./2./ des Schuldspruchs § 28 Abs 1 zweiter Satz SMG sowie § 270 Abs 4 Z 1 iVm Abs 2 Z 4 StPO.

| Predicted | Gold |
|---|---|
| `Landesgerichts Korneuburg` | `Landesgerichts Korneuburg` |

**Example 75** (doc_id: `deanon_260716_TRAIN/15Os43_13g`) (sent_id: `deanon_260716_TRAIN/15Os43_13g_6`)


Text Gründe: Mit in Rechtskraft erwachsenem, gekürzt ausgefertigtem Urteil des Einzelrichters des Landesgerichts Korneuburg vom 13. Juni 2012 (ON 69) wurde Manfred Bäumcker des Vergehens (richtig: der Vergehen;

| Predicted | Gold |
|---|---|
| `Landesgerichts Korneuburg` | `Landesgerichts Korneuburg` |

**Missed by this rule (FN):**

- `Manfred Bäumcker` (person)

**Example 76** (doc_id: `deanon_260716_TRAIN/15Os43_13g`) (sent_id: `deanon_260716_TRAIN/15Os43_13g_11`)


Rechtliche Beurteilung Das Urteil des Landesgerichts Korneuburg vom 13. Juni 2012, GZ 505 Hv 5/11x-69, steht - wie die Generalprokuratur in ihrer Nichtigkeitsbeschwerde zur Wahrung des Gesetzes zutreffend ausführt - in seinem Punkt A./2./ mit dem Gesetz nicht im Einklang: Gemäß der auch für das Verfahren vor dem Landesgericht als Einzelrichter geltenden (§ 488 Abs 1 StPO) Bestimmung des § 270 Abs 4 StPO hat eine - unter den in dieser Vorschrift genannten, hier vorliegenden Voraussetzungen zulässigerweise - gekürzte Urteilsaus- fertigung die in § 270 Abs 2 StPO angeführten Angaben mit Ausnahme der Entscheidungsgründe, also auch die in § 260 StPO (§ 270 Abs 4 Z 1 StPO) genannten Punkte zu enthalten.

| Predicted | Gold |
|---|---|
| `Landesgerichts Korneuburg` | `Landesgerichts Korneuburg` |

**Example 77** (doc_id: `deanon_260716_TRAIN/15Os50_15i`) (sent_id: `deanon_260716_TRAIN/15Os50_15i_3`)


Kopf Der Oberste Gerichtshof hat am 10. Juni 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann als weitere Richter in Gegenwart des Rechtspraktikanten Mag. Zechner als Schriftführer in der Strafsache gegen Manfred Mudder und einen weiteren Angeklagten wegen des Vergehens des Betrugs nach § 146 StGB und anderer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Linz als Schöffengericht vom 28. Jänner 2015, GZ 34 Hv 118/14b-50, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Linz` | `Landesgerichts Linz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Danek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Lendl` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Fürnkranz` (person)
- `Dr. Mann` (person)
- `Mag. Zechner` (person)
- `Manfred Mudder` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_10`)


Die Klägerin stützte die Zuständigkeit des von ihr angerufenen Landesgerichts Wr. Neustadt als Handelsgericht auf § 88 Abs 1 und 2 JN.

**False Positives:**

- `Landesgerichts Wr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_11`)


Für den Fall der örtlichen Unzuständigkeit des angerufenen Gerichts beantragte die Klägerin gemäß § 28 JN die Bestimmung des Landesgerichts Wr. Neustadt als Handelsgericht als für den gegenständlichen Rechtsstreit örtlich zuständiges Gericht.

**False Positives:**

- `Landesgerichts Wr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Ralph Prusseit, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Akbayrak Metall GmbH, Schroateck 57, 4710 Niederweng, Österreich, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Landesgerichts Krems` — partial — pred is substring of gold: `Landesgerichts Krems an der Donau`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Dr. Steger`(person)
- `Dr. Annerl`(person)
- `Dr. Wallner-Friedl`(person)
- `Ralph Prusseit`(person)
- `Mag. Franz Eckl`(person)
- `Akbayrak Metall GmbH`(organisation)
- `Schroateck 57, 4710 Niederweng, Österreich`(address)
- `Skribe Rechtsanwälte GmbH`(organisation)
- `Landesgerichts Krems an der Donau`(organisation)
- `Bezirksgerichts Zwettl`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_4`)


Enns-Umwelt Consulting Limited, Alpineweg 221, 5730 Jochbergthurn, Österreich, 2. Ing. Lara Markart, letztere vertreten durch Radel Stampf Supper Rechtsanwälte OG in Mattersburg, wegen 160.422,79 EUR sA, infolge Revision der klagenden Partei (Revisionsinteresse 107.422,79 EUR sA) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Jänner 2015, GZ 4 R 119/14w-32, womit das Urteil des Landesgerichts St. Pölten vom 25. April 2014, GZ 37 Cg 96/13f-28, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Landesgerichts St` — partial — pred is substring of gold: `Landesgerichts St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Enns-Umwelt`(organisation)
- `Alpineweg 221, 5730 Jochbergthurn, Österreich`(address)
- `Ing. Lara Markart`(person)
- `Radel Stampf Supper Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts St. Pölten`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Brigitte Martz, geboren am 16. November 1978, wegen Kontaktrechts des Vaters Dr. Gustav Thöning, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Madeleine Musialik, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

**False Positives:**

- `Landesgerichts Wiener` — partial — pred is substring of gold: `Landesgerichts Wiener Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Mag. Ziegelbauer`(person)
- `Brigitte Martz`(person)
- `16. November 1978`(date)
- `Dr. Gustav Thöning`(person)
- `Pieler & Pieler & Partner KG`(organisation)
- `Dr. Madeleine Musialik`(person)
- `Kosch & Partner Rechtsanwälte GmbH`(organisation)
- `Landesgerichts Wiener Neustadt`(organisation)
- `Bezirksgerichts Wiener Neustadt`(organisation)
- `Obersten Gerichtshofs`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/10Ob30_19p`) (sent_id: `deanon_260716_TRAIN/10Ob30_19p_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der minderjährigen Maja Dolleschell, geboren 14. August 2009, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Melk, 3390 Melk, Abt Karl-Straße 25a) wegen Unterhaltsvorschüssen, über den Revisionsrekurs des Kindes gegen den Beschluss des Landesgerichts St. Pölten als Rekursgericht vom 23. Jänner 2019, GZ 23 R 6/19h-52, mit dem der Beschluss des Bezirksgerichts Melk vom 21. November 2018, GZ 22 Pu 194/16m-42, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Landesgerichts St` — partial — pred is substring of gold: `Landesgerichts St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Maja Dolleschell`(person)
- `14. August`(date)
- `Bezirkshauptmannschaft Melk`(organisation)
- `Landesgerichts St. Pölten`(organisation)
- `Bezirksgerichts Melk`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Landesgerichts Wiener` — partial — pred is substring of gold: `Landesgerichts Wiener Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Mag. Korn`(person)
- `Langhansl+Antonewitz Chemie AG`(organisation)
- `Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich`(address)
- `Poinstingl & Partner Rechtsanwälte OG`(organisation)
- `Drau-Pharma GmbH`(organisation)
- `Strazzegasse 12, 8762 Oberzeiring, Österreich`(address)
- `Mag. Johannes Bügler`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Wiener Neustadt`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Ob43_19z`) (sent_id: `deanon_260716_TRAIN/10Ob43_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Othmar Mertl, vertreten durch Nitsch Pajor Zöllner Rechtsanwälte OG in Mödling, gegen die beklagte Partei Stadtgemeinde Malik Fridt, vertreten durch Krist Bubits Rechtsanwälte OG in Mödling, wegen 1.) 21.216,92 EUR sA und 2.) Feststellung (Streitwert: 2.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Februar 2019, GZ 12 R 96/18b-36, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Wiener Neustadt vom 31. August 2018, GZ 20 Cg 86/17h-31, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Landesgerichts Wiener` — partial — pred is substring of gold: `Landesgerichts Wiener Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Othmar Mertl`(person)
- `Nitsch Pajor Zöllner Rechtsanwälte OG`(organisation)
- `Malik Fridt`(person)
- `Krist Bubits Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Wiener Neustadt`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/11Os59_13f`) (sent_id: `deanon_260716_TRAIN/11Os59_13f_3`)


Kopf Der Oberste Gerichtshof hat am 28. Mai 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Kurzthaler als Schriftführer, in der Strafsache gegen Andreas Schiessl wegen des Verbrechens des schweren Raubes nach §§ 15, 142 Abs 1, 143 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Wiener Neustadt als Schöffengericht vom 28. Februar 2013, GZ 37 Hv 158/12k-13, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Landesgerichts Wiener` — partial — pred is substring of gold: `Landesgerichts Wiener Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Zehetner`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Mag. Lendl`(person)
- `Mag. Michel`(person)
- `Dr. Oshidari`(person)
- `Mag. Kurzthaler`(person)
- `Andreas Schiessl`(person)
- `Landesgerichts Wiener Neustadt`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_3`)


Kopf Der Oberste Gerichtshof hat am 16. März 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Brenner in der Strafvollzugssache des Oliver Pekarek, AZ 39 Ns 43/15i des Landesgerichts Krems an der Donau, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Landesgerichts Krems` — partial — pred is substring of gold: `Landesgerichts Krems an der Donau`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Schroll`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. T. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Brenner`(person)
- `Oliver Pekarek`(person)
- `Landesgerichts Krems an der Donau`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `OGH`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Thomas Michenfelder wegen des Verbrechens des schweren gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 2 und Z 5, 129 Abs 1 Z 1, Z 2 und Z 3, 130 Abs 2 zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 38 Hv 40/18z des Landesgerichts Krems an der Donau, über die von der Generalprokuratur gegen den Beschluss des Präsidenten des Oberlandesgerichts Wien vom 17. Oktober 2018, AZ 130 Ns 31/18w, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Mag. Gföller und der Verteidigerin Dr. Zeh-Gindl zu Recht erkannt:  Spruch

**False Positives:**

- `Landesgerichts Krems` — partial — pred is substring of gold: `Landesgerichts Krems an der Donau`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. T. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Oshidari`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Dr. Mann`(person)
- `Dr. Brenner`(person)
- `Mag. Rögner`(person)
- `Thomas Michenfelder`(person)
- `Landesgerichts Krems an der Donau`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Mag. Gföller`(person)
- `Dr. Zeh-Gindl`(person)

**Example 11** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_5`)


Dieser Beschluss wird aufgehoben und es wird in der Sache selbst erkannt, dass der Senatspräsident des Oberlandesgerichts Wien Dr. Krenn sowie die Richterinnen des Oberlandesgerichts Wien Mag. Edwards und Mag. Sanda von der Entscheidung über die Berufung des Angeklagten gegen das Urteil des Landesgerichts Krems an der Donau vom 8. August 2018, GZ 38 Hv 40/18z-100, nicht ausgeschlossen sind.

**False Positives:**

- `Landesgerichts Krems` — partial — pred is substring of gold: `Landesgerichts Krems an der Donau`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgerichts Wien`(organisation)
- `Dr. Krenn`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Mag. Edwards`(person)
- `Mag. Sanda`(person)
- `Landesgerichts Krems an der Donau`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_6`)


Text Gründe: Soweit für die Behandlung der Nichtigkeitsbeschwerde zur Wahrung des Gesetzes von Bedeutung wurde Thomas Maksym mit Urteil des Landesgerichts Krems an der Donau vom 13. März 2018 (ON 72) des Verbrechens des schweren gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 2 und Z 5, 129 Abs 1 Z 1, Z 2 und Z 3, 130 Abs 2 zweiter Fall und 15 StGB (I./) sowie der Vergehen der Urkundenunterdrückung nach § 229 Abs 1 StGB (II./) und des Betrugs nach § 146 StGB (III./) schuldig erkannt und zu einer Freiheitsstrafe verurteilt. Aus Anlass der (allein aufrechterhaltenen) Berufung des Angeklagten wegen des Ausspruchs über die Strafe (ON 86) hob der zuständige 21.

**False Positives:**

- `Landesgerichts Krems` — partial — pred is substring of gold: `Landesgerichts Krems an der Donau`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Thomas Maksym`(person)
- `Landesgerichts Krems an der Donau`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_10`)


Im zweiten Rechtsgang sprach die Einzelrichterin des Landesgerichts Krems an der Donau Thomas Muthardt mit Urteil vom 8. August 2018 (ON 100) neuerlich anklagekonform schuldig und verurteilte ihn zu einer Freiheitsstrafe.

**False Positives:**

- `Landesgerichts Krems` — partial — pred is substring of gold: `Landesgerichts Krems an der Donau`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Krems an der Donau`(organisation)
- `Thomas Muthardt`(person)

**Example 14** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_13`)


Dazu führte er aus, dass die genannten Richter das Urteil des Landesgerichts Krems an der Donau vom 13. März 2018 (ON 72) in amtswegiger Wahrnehmung des Nichtigkeitsgrundes des § 281 Abs 1 Z 9 lit a [der Sache nach Z 10] StPO „großteils aufgehoben“ und „dabei“ „die Tatfrage mit Hinweis auf die Strafbarkeit des angelasteten Verhaltens indizierende Verfahrensergebnisse mit voller Kognitionsbefugnis [beurteilt] und […] beweiswürdigend Stellung bezogen“ hätten.

**False Positives:**

- `Landesgerichts Krems` — partial — pred is substring of gold: `Landesgerichts Krems an der Donau`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Krems an der Donau`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_3`)


Kopf Der Oberste Gerichtshof hat am 8. April 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Holzweber als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll, Dr. Schwab, Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger in Gegenwart der Richteramtsanwärterin Mag. Bayer als Schriftführerin in der Strafsache gegen Dr. Ernst-Peter Nepomuk Lieschke wegen des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB über die Beschwerde des Verurteilten gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 19. Jänner 2010, AZ 20 Bs 461/09d (GZ 20 Hv 73/09p-19 des Landesgerichts St. Pölten), nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Landesgerichts St` — partial — pred is substring of gold: `Landesgerichts St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Holzweber`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Schroll`(person)
- `Dr. Schwab`(person)
- `Dr. T. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Hetlinger`(person)
- `Mag. Bayer`(person)
- `Dr. Ernst`(person)
- `Nepomuk Lieschke`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts St. Pölten`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_4`)


Text G r ü n d e : Mit Urteil des Einzelrichters des Landesgerichts St. Pölten vom 18. September 2009, GZ 20 Hv 73/09p-13, wurde Dr. Ernst-Peter Paula Langehanke des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB schuldig erkannt und zu einer für eine Probezeit von drei Jahren bedingt nachgesehenen Freiheitsstrafe von vier Wochen verurteilt. Der vom Angeklagten dagegen erhobenen Berufung wegen Nichtigkeit, Schuld und Strafe gab das Oberlandesgericht Wien mit der nunmehr angefochtenen Entscheidung keine Folge (ON 19).

**False Positives:**

- `Landesgerichts St` — partial — pred is substring of gold: `Landesgerichts St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts St. Pölten`(organisation)
- `Dr. Ernst`(person)
- `Paula Langehanke`(person)
- `Oberlandesgericht Wien`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/13Os155_15s`) (sent_id: `deanon_260716_TRAIN/13Os155_15s_3`)


Kopf Der Oberste Gerichtshof hat am 9. März 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtswärters Mag. Schönmann als Schriftführer in der Strafsache gegen Thomas Enulait wegen des Verbrechens des schweren sexuellen Missbrauchs von Unmündigen nach § 206 Abs 1 und 3 erster Fall StGB sowie weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts St. Pölten als Schöffengericht vom 1. September 2015, GZ 20 Hv 13/15y-53, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde und die Berufung wegen des Ausspruchs über die Schuld werden zurückgewiesen.

**False Positives:**

- `Landesgerichts St` — partial — pred is substring of gold: `Landesgerichts St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Lässig`(person)
- `Mag. Michel`(person)
- `Dr. Oberressl`(person)
- `Dr. Brenner`(person)
- `Mag. Schönmann`(person)
- `Thomas Enulait`(person)
- `Landesgerichts St. Pölten`(organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/14Os108_18s`) (sent_id: `deanon_260716_TRAIN/14Os108_18s_3`)


Kopf Der Oberste Gerichtshof hat am 13. November 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Kontrollorin Gsellmann als Schriftführerin in der Strafsache gegen Misha Riffart und andere Angeklagte wegen des Verbrechens des im Rahmen einer kriminellen Vereinigung gewerbsmäßig schweren und durch Einbruch begangenen Diebstahls nach §§ 127, 129 Abs 1 Z 2, Abs 2 Z 1, 130 Abs 2 und 3, jeweils iVm Abs 1 zweiter Fall, § 15 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Valeri Kunkelmann gegen das Urteil des Landesgerichts St. Pölten als Schöffengericht vom 28. Juni 2018, GZ 39 Hv 37/18x-157, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Landesgerichts St` — partial — pred is substring of gold: `Landesgerichts St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Danek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Hetlinger`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Dr. Oshidari`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Mann`(person)
- `Misha Riffart`(person)
- `Valeri Kunkelmann`(person)
- `Landesgerichts St. Pölten`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/14Os70_10s`) (sent_id: `deanon_260716_TRAIN/14Os70_10s_4`)


Gründe:  Rechtliche Beurteilung Mit dem angefochtenen Beschluss wies das Oberlandesgericht Wien die Beschwerde des Heinrich Knot gegen den Beschluss des Landesgerichts St. Pölten als Beschwerdegericht vom 11. Februar 2010, GZ 9 Bl 158/09y-7, unter Hinweis auf § 89 Abs 6 StPO zurück.

**False Positives:**

- `Landesgerichts St` — partial — pred is substring of gold: `Landesgerichts St. Pölten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgericht Wien`(organisation)
- `Heinrich Knot`(person)
- `Landesgerichts St. Pölten`(organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/15Os162_11d`) (sent_id: `deanon_260716_TRAIN/15Os162_11d_4`)


In der Strafvollzugssache der Radmila Muend, AZ 188 BE 302/10x des Landesgerichts für Strafsachen Wien (vormals AZ 44 BE 397/10a des Landesgerichts Wiener Neustadt), verletzt der ohne vorangehende Einsichtnahme in den Akt AZ 75 Hv 151/06h des Landesgerichts für Strafsachen Wien gefasste Beschluss des Landesgerichts Wiener Neustadt als Vollzugsgericht vom 24. August 2010, GZ 44 BE 397/10a- 5, über die bedingte Entlassung der Verurteilten § 152 Abs 2 erster Satz StVG.

**False Positives:**

- `Landesgerichts Wiener` — partial — pred is substring of gold: `Landesgerichts Wiener Neustadt`
- `Landesgerichts Wiener` — similar text (different position): `Landesgerichts Wiener Neustadt`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Radmila Muend`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Landesgerichts Wiener Neustadt`(organisation)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Landesgerichts Wiener Neustadt`(organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/15Os162_11d`) (sent_id: `deanon_260716_TRAIN/15Os162_11d_10`)


Mit Beschluss des Landesgerichts Wiener Neustadt als Vollzugsgericht vom 24. August 2010, GZ 44 BE 397/10a-5, wurde Radmila Maseizik am 5. November 2010 aus dem Vollzug der mit Urteil des Landesgerichts für Strafsachen Wien vom 12. August 2009, AZ 81 Hv 85/09a, verhängten unbedingten Freiheitsstrafe von 27 Monaten und der mit Urteil des Landesgerichts für Strafsachen Wien vom 8. November 2006, AZ 75 Hv 151/06h, ausgesprochenen zehnmonatigen Freiheitsstrafe nach Verbüßung eines Teils von 25 Monaten gemäß § 46 StGB bedingt entlassen.

**False Positives:**

- `Landesgerichts Wiener` — partial — pred is substring of gold: `Landesgerichts Wiener Neustadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Wiener Neustadt`(organisation)
- `Radmila Maseizik`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Landesgerichts für Strafsachen Wien`(organisation)

</details>

---

## `ÖBB Acronym` 🏆

**F1:** 0.004 | **Precision:** 0.692 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `86eca1f6`  
**Description:**
Matches the ÖBB (Österreichische Bundesbahnen) acronym as an organization.

**Content:**
```
\bÖBB\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.692 | 0.002 | 0.004 | 13 | 9 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 9 | 4 | 2516 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_62`)


… .“ b) Neue Rechtslage: § 53a des Bundesbahngesetzes, BGBl I 2011/129 lautet: „(1) Für jene Bediensteten und Ruhegenussempfänger, die bis zum 31. Dezember 2004 bei den Österreichischen Bundesbahnen (ÖBB), einem ihrer Rechtsvorgänger oder ab Rechtswirksamkeit der angeordneten Spaltungs- und Umwandlungsvorgänge bei der ÖBB-Holding AG, den im 3.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Missed by this rule (FN):**

- `ÖBB-Holding AG` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_80`)


Auch im ÖBB-Dienstrecht der 'Allgemeinen Vertragsbedingungen für Dienstverträge bei den Österreichischen Bundesbahnen' (AVB), die als Vertragsschablone für die ÖBB-Angestellten mit einem Eintritt vor dem 01.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |
| `ÖBB` | `ÖBB` |

**Example 2** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_83`)


Von dieser Regelung betroffen sind rund 27.000 ÖBB-Angestellte.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 3** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_86`)


Ohne eine Neuregelung werden die betroffenen ÖBB-Angestellten (auch wenn sie bereits im Ruhestand sind) die Neufestsetzung ihres Vorrückungsstichtages begehren und die Gehaltsdifferenz der letzten 3 Jahre (Verjährungsfrist) geltend machen.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 4** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_87`)


Daraus ergibt sich auch für die Zukunft eine finanzielle Belastung für die ÖBB, sowie eine höhere Belastung des Bundes aus den künftigen Ruhegenüssen.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 5** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_213`)


GP 1) wird dazu ausgeführt, dass ohne Neuregelung die betroffenen ÖBB-Angestellten die Neufestsetzung ihres Vorrückungsstichtags begehren und die Gehaltsdifferenz in den letzten drei Jahren (Verjährungsfrist) geltend machen werden.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 6** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_214`)


Daraus ergebe sich eine finanzielle Belastung für die ÖBB und für den Bund.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 7** (doc_id: `deanon_260716_TRAIN/8ObA72_19z`) (sent_id: `deanon_260716_TRAIN/8ObA72_19z_12`)


2. Dabei konnte sich der Oberste Gerichtshof auf einschlägige Judikatur sowohl des Verfassungsgerichtshofs als auch des EuGH stützen: 2.1 Der Verfassungsgerichtshof hat in seinem Erkenntnis G 450/2015 ua Parteianträge von ÖBB-Bediensteten (unter anderem auch des Klägers) abgewiesen, die § 53a und § 56 Abs 18 bis 24 BundesbahnG je idF BGBl I Nr 64/2015 als verfassungswidrig aufzuheben.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Verfassungsgerichtshofs` (organisation)
- `Verfassungsgerichtshof` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/1Ob169_15g`) (sent_id: `deanon_260716_TRAIN/1Ob169_15g_55`)


C-417/13,ÖBB-Personenverkehr, ECLI:EU:C:2015:38, Rn 66 f).

**False Positives:**

- `ÖBB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/2Ob99_24h`) (sent_id: `deanon_260716_TRAIN/2Ob99_24h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Grohmann als Vorsitzende und die Hofräte MMag. Sloboda, Dr. Thunhart und Dr. Kikinger sowie die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei ÖBB-Infrastruktur Aktiengesellschaft, Kathreinweg 48, 4572 Schalchgraben, Österreich, vertreten durch Dr. Martin Wandl und Dr. Wolfgang Krempl, Rechtsanwälte in St. Pölten, gegen die beklagten Parteien 1. Melina McNaughtan, 2. Ophelia Middelkamp, und 3. ÖkR HR Karlheinz Göttl, alle vertreten durch Dr. Peter Lindinger und Dr. Andreas Pramer, Rechtsanwälte in Linz, wegen 54.038,42 EUR sA, über die Revisionen sämtlicher Streitteile gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 13. März 2024, GZ 11 R 5/24w-61, womit infolge Berufung der beklagten Parteien das Urteil des Landesgerichts Linz vom 28. November 2023, GZ 5 Cg 82/22m-54, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revisionen werden zurückgewiesen.

**False Positives:**

- `ÖBB` — partial — pred is substring of gold: `ÖBB-Infrastruktur Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Grohmann`(person)
- `MMag. Sloboda`(person)
- `Dr. Thunhart`(person)
- `Dr. Kikinger`(person)
- `Mag. Fitz`(person)
- `ÖBB-Infrastruktur Aktiengesellschaft`(organisation)
- `Kathreinweg 48, 4572 Schalchgraben, Österreich`(address)
- `Dr. Martin Wandl`(person)
- `Dr. Wolfgang Krempl`(person)
- `Melina McNaughtan`(person)
- `Ophelia Middelkamp`(person)
- `ÖkR HR Karlheinz Göttl`(person)
- `Dr. Peter Lindinger`(person)
- `Dr. Andreas Pramer`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Linz`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden und die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn sowie die fachkundigen Laienrichter Mag. Dr. Monika Lanz und Wolfgang Cadilek als weitere Richter in der Arbeitsrechtssache der klagenden Partei Hon.-Prof. Dieter Kovacs, vertreten durch Pfurtscheller Orgler Huber, Rechtsanwälte in Innsbruck, gegen die beklagte Partei ÖBB-Personenverkehr AG, Monsbergergasse 12, 6210 Astenberg, Österreich, vertreten durch die CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 3.963,75 EUR brutto sA, aus Anlass der (außerordentlichen) Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. Februar 2013, GZ 13 Ra 1/13i-16, mit dem das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 16. Oktober 2012, GZ 42 Cga 87/12h-12, abgeändert wurde, den Beschluss gefasst:  Spruch A.Dem Gerichtshof der Europäischen Union werden folgende Fragen zur Vorabentscheidung vorgelegt: 1.Ist Art 21 der Grundrechtecharta in Verbindung mit Art 7 Abs 1, Art 16 und Art 17 der Richtlinie 2000/78/EG dahin auszulegen, dass a)ein Arbeitnehmer, für den vom Arbeitgeber aufgrund einer gesetzlich normierten altersdiskriminierenden Anrechnung von Vordienstzeiten zunächst ein unrichtiger Vorrückungsstichtag festgesetzt wurde, in jedem Fall Anspruch auf Zahlung der Gehaltsdifferenz unter Zugrundelegung des diskriminierungsfreien Vorrückungsstichtags hat, b)oder aber dahin, dass der Mitgliedstaat die Möglichkeit hat, durch eine diskriminierungsfreie Anrechnung der Vordienstzeiten die Altersdiskriminierung auch ohne finanziellen Ausgleich (durch Neufestsetzung des Vorrückungsstichtags bei gleichzeitiger Verlängerung des Vorrückungszeitraums) zu beseitigen, insbesondere wenn diese entgeltneutrale Lösung die Liquidität des Arbeitgebers aufrechterhalten sowie einen übermäßigen Neuberechnungsaufwand vermeiden soll?

**False Positives:**

- `ÖBB` — partial — pred is substring of gold: `ÖBB-Personenverkehr AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Spenling`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Brenn`(person)
- `Mag. Dr. Monika Lanz`(person)
- `Wolfgang Cadilek`(person)
- `Hon.-Prof. Dieter Kovacs`(person)
- `Pfurtscheller Orgler Huber, Rechtsanwälte`(organisation)
- `ÖBB-Personenverkehr AG`(organisation)
- `Monsbergergasse 12, 6210 Astenberg, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Innsbruck`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_62`)


… .“ b) Neue Rechtslage: § 53a des Bundesbahngesetzes, BGBl I 2011/129 lautet: „(1) Für jene Bediensteten und Ruhegenussempfänger, die bis zum 31. Dezember 2004 bei den Österreichischen Bundesbahnen (ÖBB), einem ihrer Rechtsvorgänger oder ab Rechtswirksamkeit der angeordneten Spaltungs- und Umwandlungsvorgänge bei der ÖBB-Holding AG, den im 3.

**False Positives:**

- `ÖBB` — similar text (different position): `ÖBB`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ÖBB`(organisation)
- `ÖBB-Holding AG`(organisation)

</details>

---

## `KG Company Names` 🏆

**F1:** 0.005 | **Precision:** 0.367 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `2482aec5`  
**Description:**
Matches company names ending in 'KG' or 'GmbH & Co KG'. Requires a specific proper noun prefix (at least one capitalized word) before the legal form to avoid matching generic terms.

**Content:**
```
\b([A-Z][A-Za-z\u00e4\u00f6\u00fc\u00df\-]+(?:\s+[A-Z][A-Za-z\u00e4\u00f6\u00fc\u00df\-]+)*\s+(?:GmbH\s*&\s*Co\s*KG|GmbH\s*&\s*Partner\s*KG|KG))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.367 | 0.003 | 0.005 | 30 | 11 | 19 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 11 | 19 | 3711 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_4`)


Norsee Technologien GmbH & Co KG und 2.

| Predicted | Gold |
|---|---|
| `Norsee Technologien GmbH & Co KG` | `Norsee Technologien GmbH & Co KG` |

**Example 1** (doc_id: `deanon_260716_TRAIN/2Ob193_23f`) (sent_id: `deanon_260716_TRAIN/2Ob193_23f_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte Hon.-Prof. PD Dr. Rassi, MMag. Sloboda, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Denise Markstaler, vertreten durch Weber Rechtsanwälte GmbH & Co KG in Wien 1, gegen die beklagte Partei Rut Adamheit, vertreten durch BEURLE Rechtsanwälte GmbH & Co KG in Linz, wegen Herausgabe (Streitwert 1.525.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2023, GZ 2 R 87/23m-32, mit dem das Urteil des Landesgerichts Salzburg vom 5. April 2023, GZ 8 Cg 9/23a-22, aufgehoben wurde zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Weber Rechtsanwälte GmbH & Co KG` | `Weber Rechtsanwälte GmbH & Co KG` |
| `BEURLE Rechtsanwälte GmbH & Co KG` | `BEURLE Rechtsanwälte GmbH & Co KG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Grohmann` (person)
- `Hon.-Prof. PD Dr. Rassi` (person)
- `MMag. Sloboda` (person)
- `Dr. Kikinger` (person)
- `Mag. Fitz` (person)
- `Denise Markstaler` (person)
- `Rut Adamheit` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Salzburg` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/3Ob209_21p`) (sent_id: `deanon_260716_TRAIN/3Ob209_21p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei APHU Solar GmbH & Co KG, Hochkreuth 39, 8144 Bischofegg, Österreich, vertreten durch DDr. Heinz Dietmar Schimanko, Rechtsanwalt in Wien, gegen die beklagte Partei Traun-Transport GmbH, Stauderstraße 30, 8200 Pircha, Österreich, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH & Co KG in Wien, wegen 7.906,82 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 7. Juni 2021, GZ 38 R 66/21v-16, mit dem das Urteil des Bezirksgerichts Favoriten vom 19. Jänner 2021, GZ 3 C 503/20f-12, abgeändert wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Bichler Zrzavy Rechtsanwälte GmbH & Co KG` | `Bichler Zrzavy Rechtsanwälte GmbH & Co KG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Höllwerth` (person)
- `Hon.-Prof. Dr. Brenn` (person)
- `Dr. Weixelbraun-Mohr` (person)
- `Dr. Kodek` (person)
- `Dr. Stefula` (person)
- `APHU Solar GmbH & Co KG` (organisation)
- `Hochkreuth 39, 8144 Bischofegg, Österreich` (address)
- `DDr. Heinz Dietmar Schimanko` (person)
- `Traun-Transport GmbH` (organisation)
- `Stauderstraße 30, 8200 Pircha, Österreich` (address)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/3Ob45_19t`) (sent_id: `deanon_260716_TRAIN/3Ob45_19t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Roch und Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Mag. Daniel Kutluk, vertreten durch Dr. Johannes Eltz, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Ferdinand Rittgerott, vertreten durch Piaty Müller-Mezin Schöller Rechtsanwälte GmbH & Co KG in Graz, wegen Einwendungen gegen den Anspruch (§ 35 EO), über die „außerordentliche“ Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 25. September 2018, GZ 4 R 102/18a-11, womit das Urteil des Bezirksgerichts Graz-West vom 27. Februar 2018, GZ 211 C 2/17g-7, bestätigt wurde, den Beschluss gefasst:  Spruch Die „außerordentliche“ Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Piaty Müller-Mezin Schöller Rechtsanwälte GmbH & Co KG` | `Piaty Müller-Mezin Schöller Rechtsanwälte GmbH & Co KG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hoch` (person)
- `Dr. Roch` (person)
- `Dr. Rassi` (person)
- `Dr. Weixelbraun-Mohr` (person)
- `Dr. Kodek` (person)
- `Mag. Daniel Kutluk` (person)
- `Dr. Johannes Eltz` (person)
- `Mag. Ferdinand Rittgerott` (person)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)
- `Bezirksgerichts Graz-West` (organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/4Ob180_10i`) (sent_id: `deanon_260716_TRAIN/4Ob180_10i_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Nimtz Pharma GmbH, Mildenbergstraße 11, 3072 Furth, Österreich, vertreten durch Berger Saurer Zöchbauer, Rechtsanwälte in Wien, gegen die beklagten Parteien 1) Unikel Landwirtschaft GmbH & Co KG und 2) Gode+Panköker Getränke GmbH, Martinsplatz 1-31, 9831 Kleindorf, Österreich, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Provisorialverfahren 36.000 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 6. August 2010, GZ 5 R 150/10f-7, womit der Beschluss des Handelsgerichts Wien vom 24. Juni 2010, GZ 11 Cg 117/10h-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Unikel Landwirtschaft GmbH & Co KG` | `Unikel Landwirtschaft GmbH & Co KG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schenk` (person)
- `Dr. Vogel` (person)
- `Dr. Jensik` (person)
- `Dr. Musger` (person)
- `Dr. Schwarzenbacher` (person)
- `Nimtz Pharma GmbH` (organisation)
- `Mildenbergstraße 11, 3072 Furth, Österreich` (address)
- `Berger Saurer Zöchbauer, Rechtsanwälte` (organisation)
- `Gode+Panköker Getränke GmbH` (organisation)
- `Martinsplatz 1-31, 9831 Kleindorf, Österreich` (address)
- `Gheneff - Rami - Sommer Rechtsanwälte KG` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/4Ob196_10t`) (sent_id: `deanon_260716_TRAIN/4Ob196_10t_4`)


Monderdorf Cloud GmbH, R.-Hamerling-Gasse 4, 6373 Jochberg, Österreich, beide vertreten durch Ruggenthaler Rechtsanwalts KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 62.000 EUR) über den außerordentlichen Revisionsrekurs der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Wien vom 20. September 2010, GZ 30 R 29/10w-9, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ruggenthaler Rechtsanwalts KG` | `Ruggenthaler Rechtsanwalts KG` |

**Missed by this rule (FN):**

- `Monderdorf Cloud GmbH` (organisation)
- `R.-Hamerling-Gasse 4, 6373 Jochberg, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/5Ob71_24p`) (sent_id: `deanon_260716_TRAIN/5Ob71_24p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Mag. Wurzer als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Painsi, Dr. Weixelbraun-Mohr, Dr. Steger und Dr. Pfurtscheller als weitere Richter in der Rechtssache der klagenden Partei Josefine Fretschner, vertreten durch die Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei AlpenDerlogverEvent GmbH, Am Kröpflmühlerberg 93, 3925 Kleinpertenschlag, Österreich, vertreten durch die Wolf Theiss Rechtsanwälte GmbH & Co KG in Wien, wegen 7.140 EUR und Feststellung (Streitwert 2.000 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Steyr als Berufungsgericht vom 8. Februar 2024, GZ 1 R 120/23z-43, mit dem das Urteil des Bezirksgerichts Steyr vom 28. September 2023, GZ 2 C 288/21x-39, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das Verfahren über die Revision der beklagten Partei wird bis zur Entscheidung des Gerichtshofs der Europäischen Union (EuGH) über die Vorabentscheidungsersuchen des Landgerichts Ravensburg (Deutschland) vom 9. November 2023, Rechtssache C-666/23, vom 9. November 2023, Rechtssache C-667/23, und vom 15. November 2023, Rechtssache C-668/23, unterbrochen.

| Predicted | Gold |
|---|---|
| `Wolf Theiss Rechtsanwälte GmbH & Co KG` | `Wolf Theiss Rechtsanwälte GmbH & Co KG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Mag. Painsi` (person)
- `Dr. Weixelbraun-Mohr` (person)
- `Dr. Steger` (person)
- `Dr. Pfurtscheller` (person)
- `Josefine Fretschner` (person)
- `Poduschka Anwaltsgesellschaft mbH` (organisation)
- `AlpenDerlogverEvent GmbH` (organisation)
- `Am Kröpflmühlerberg 93, 3925 Kleinpertenschlag, Österreich` (address)
- `Landesgerichts Steyr` (organisation)
- `Bezirksgerichts Steyr` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/6Ob146_18s`) (sent_id: `deanon_260716_TRAIN/6Ob146_18s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden und die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei RgR Dr.in Manuela Künemund, vertreten durch Mag. Max Verdino und andere Rechtsanwälte in St. Veit an der Glan, gegen die beklagte Partei Kleuß Maschinenbau GmbH, Friedensring 38, 9815 Penk, Österreich, vertreten durch PHH Prochaska Havranek Rechtsanwälte GmbH & Co KG in Wien, wegen 18.664,48 EUR und Feststellung, über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 6. Juni 2018, GZ 4 R 51/18d-12, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Klagenfurt vom 20. Februar 2018, GZ 28 Cg 75/17s-8, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `PHH Prochaska Havranek Rechtsanwälte GmbH & Co KG` | `PHH Prochaska Havranek Rechtsanwälte GmbH & Co KG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schramm` (person)
- `Dr. Gitschthaler` (person)
- `Univ.-Prof. Dr. Kodek` (person)
- `Dr. Nowotny` (person)
- `Dr. Faber` (person)
- `RgR Dr.in Manuela Künemund` (person)
- `Mag. Max Verdino` (person)
- `Kleuß Maschinenbau GmbH` (organisation)
- `Friedensring 38, 9815 Penk, Österreich` (address)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts Klagenfurt` (organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/9Ob68_22y`) (sent_id: `deanon_260716_TRAIN/9Ob68_22y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Dr. Hargassner, Mag. Korn, MMag. Sloboda und Dr. Annerl in der Rechtssache der klagenden Partei Niels Doerfel, vertreten durch Neubauer Fähnrich Rechtsanwälte GmbH & Co KG in Graz, gegen die beklagte Partei Gudrun Kovalschuk Gesellschaft m.b.H. (FN FN119735f ), FN297530m, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung und 19.490 EUR sA (Gesamtstreitwert: 19.490 EUR), über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 10. September 2019, GZ 4 R 89/19v-59, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 27. März 2019, GZ 20 Cg 15/18t-54, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Revisionsverfahren wird fortgesetzt.

| Predicted | Gold |
|---|---|
| `Neubauer Fähnrich Rechtsanwälte GmbH & Co KG` | `Neubauer Fähnrich Rechtsanwälte GmbH & Co KG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Fichtenau` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hargassner` (person)
- `Mag. Korn` (person)
- `MMag. Sloboda` (person)
- `Dr. Annerl` (person)
- `Niels Doerfel` (person)
- `Gudrun Kovalschuk` (person)
- `FN119735f` (business_register_number)
- `FN297530m` (business_register_number)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/9ObA76_13m`) (sent_id: `deanon_260716_TRAIN/9ObA76_13m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras, die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner und Mag. Ernst Bassler als weitere Richter in der Arbeitsrechtssache der klagenden Partei Adrian Leiße, BSc, vertreten durch Dr. H. Burmann ua, Rechtsanwälte in Innsbruck, gegen die beklagten Parteien 1. Logkraft-Verlag GmbH & Co KG, 2.

| Predicted | Gold |
|---|---|
| `Logkraft-Verlag GmbH & Co KG` | `Logkraft-Verlag GmbH & Co KG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kuras` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Dehn` (person)
- `Mag. Dr. Rolf Gleißner` (person)
- `Mag. Ernst` (person)
- `Adrian Leiße, BSc` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Brigitte Martz, geboren am 16. November 1978, wegen Kontaktrechts des Vaters Dr. Gustav Thöning, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Madeleine Musialik, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

**False Positives:**

- `Partner KG` — partial — pred is substring of gold: `Pieler & Pieler & Partner KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Mag. Ziegelbauer`(person)
- `Brigitte Martz`(person)
- `16. November 1978`(date)
- `Dr. Gustav Thöning`(person)
- `Pieler & Pieler & Partner KG`(organisation)
- `Dr. Madeleine Musialik`(person)
- `Kosch & Partner Rechtsanwälte GmbH`(organisation)
- `Landesgerichts Wiener Neustadt`(organisation)
- `Bezirksgerichts Wiener Neustadt`(organisation)
- `Obersten Gerichtshofs`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_5`)


Dr. Felix Cornils, Niederlande, beide vertreten durch Tramposch & Partner, Rechtsanwälte KG in Innsbruck, gegen die beklagte Partei Mag.a Constanze Rizzo, vertreten durch König Ermacora Klotz & Partner, Rechtsanwälte in Innsbruck, wegen je 15.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 1. Juli 2020, GZ 10 R 16/20h-49, mit dem das Urteil des Landesgerichts Innsbruck vom 6. Februar 2020, GZ 41 Cg 11/19i-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Rechtsanwälte KG` — partial — pred is substring of gold: `Tramposch & Partner, Rechtsanwälte KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Felix Cornils`(person)
- `Tramposch & Partner, Rechtsanwälte KG`(organisation)
- `Mag.a Constanze Rizzo`(person)
- `Oberlandesgerichts Innsbruck`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_6`)


Text Gründe: Mit dem angefochtenen Urteil wurden Bernhard Berti und Norbert Wierich von der wider sie erhobenen Anklage, sie hätten am 7. Februar 2009 in Sebastian-Stief-Gasse 48, 2632 Altendorf, Österreich /Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der Hauenschildt&Mesarec Medien GesmbH & Co KG, Susanne Schwarzhuber, durch die Vorgabe, die Donau-Transport GmbH sei eine zahlungsfähige Leasingnehmerin, somit durch Täuschung über Tatsachen, zum Abschluss eines Leasingvertrags über ein Rennfahrzeug für die Dauer von 24 Monaten zu einem monatlichen Entgelt von 10.698,10 Euro, somit zu einer Handlung verleitet, welche die TraunTouristik Werke GesmbH & Co KG in einem 50.000 Euro übersteigenden Betrag von insgesamt 235.358,20 Euro am Vermögen schädigte, gemäß § 259 Z 3 StPO (verfehlt auch von der rechtlichen Kategorie; vglLendl, WK-StPO § 259 Rz 1) freigesprochen.

**False Positives:**

- `Co KG` — partial — pred is substring of gold: `Hauenschildt&Mesarec Medien GesmbH & Co KG`
- `Co KG` — similar text (different position): `Hauenschildt&Mesarec Medien GesmbH & Co KG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bernhard Berti`(person)
- `Norbert Wierich`(person)
- `Sebastian-Stief-Gasse 48, 2632 Altendorf, Österreich`(address)
- `Hauenschildt&Mesarec Medien GesmbH & Co KG`(organisation)
- `Susanne Schwarzhuber`(person)
- `Donau-Transport GmbH`(organisation)
- `TraunTouristik Werke GesmbH & Co KG`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_9`)


Am 7. Februar 2009 schlossen die Angeklagten namens der genannten Gesellschaft mit der von Susanna Steen vertretenen Prentl Handel GesmbH & Co KG einen Leasingvertrag über einen Rennwagen samt Ersatzteilpaket.

**False Positives:**

- `Co KG` — partial — pred is substring of gold: `Prentl Handel GesmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Susanna Steen`(person)
- `Prentl Handel GesmbH & Co KG`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/1Ob152_24w`) (sent_id: `deanon_260716_TRAIN/1Ob152_24w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Musger als Vorsitzenden sowie die Hofrätin und die Hofräte Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Harald Adolphsen KG, FN FN214876m, vertreten durch Dr. Eva-Maria Bachmann-Lang, Dr. Christian Bachmann, Rechtsanwälte in Wien, gegen die beklagte Partei „ Alpen Donalcon “ OXS Bildung gmbH, FN FN067476g, vertreten durch die GRAF ISOLA Rechtsanwälte GmbH in Wien, wegen 51.843,91 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 3. Juli 2024, GZ 1 R 17/24p-39, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Harald Adolphsen KG` — partial — gold is substring of pred: `Harald Adolphsen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Musger`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Mag. Wessely-Kristöfel`(person)
- `Dr. Parzmayr`(person)
- `Harald Adolphsen`(person)
- `FN214876m`(business_register_number)
- `Dr. Eva-Maria Bachmann`(person)
- `Dr. Christian Bachmann`(person)
- `Alpen Donalcon`(organisation)
- `OXS Bildung gmbH`(organisation)
- `FN067476g`(business_register_number)
- `GRAF ISOLA Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/1Ob29_20a`) (sent_id: `deanon_260716_TRAIN/1Ob29_20a_19`)


Der Mann hat sich an einem Immobilienprojekt, das von einer GmbH & Co KG verwirklicht wird, beteiligt.

**False Positives:**

- `Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_260716_TRAIN/3Ob114_14g`) (sent_id: `deanon_260716_TRAIN/3Ob114_14g_4`)


Silvana Roellgen, MBA KG und 2. Dr. Nancy Achatzy, vertreten durch die erstklagende Partei, wider die beklagte Partei Dr. Theodora Jungverdorben, vertreten durch BMA Brandstätter Rechtsanwälte GmbH in Wien, wegen Einwendungen gegen den Anspruch (§ 35 EO), über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 30. April 2014, GZ 46 R 135/13p-43, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Innere Stadt Wien vom 30. Jänner 2013, GZ 75 C 17/11x-37, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `MBA KG` — positional overlap with gold: `Silvana Roellgen, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Silvana Roellgen, MBA`(person)
- `Dr. Nancy Achatzy`(person)
- `Dr. Theodora Jungverdorben`(person)
- `BMA Brandstätter Rechtsanwälte GmbH`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/3Ob114_14g`) (sent_id: `deanon_260716_TRAIN/3Ob114_14g_5`)


Begründung:  Rechtliche Beurteilung Die Erstklägerin (eine Rechtsanwalts KG), der Zweitkläger (deren Komplementär) und die Mutter des Zweitklägers (in Hinkunft: Pensionsberechtigte) führten als Kläger und Widerbeklagte ein Schiedsverfahren gegen den (hier) Beklagten (als ausgeschiedenen Komplementär) als Beklagten und Widerkläger, das mit einem Schiedsspruch vom 2. Mai 2011 endete.

**False Positives:**

- `Rechtsanwalts KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_260716_TRAIN/4Ob100_13d`) (sent_id: `deanon_260716_TRAIN/4Ob100_13d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Verein Karen Böckel, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei Düwall + Rief Daten -Aktiengesellschaft, Gassing/Burgweg 63, 4613 Mistelbach bei Wels, Österreich, vertreten durch Raits Bleiziffer Rechtsanwälte GmbH in Salzburg, und die Nebenintervenientin auf Seiten der beklagten Partei „ Eberhard Besemer ” Linda Hukauf, vertreten durch Dr. Peter Zöchbauer und andere Rechtsanwälte in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert 36.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz vom 19. April 2013, GZ 1 R 192/12d-14, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Langer Rechtsanwälte KG` — partial — pred is substring of gold: `Kosesnik-Wehrle & Langer Rechtsanwälte KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schenk`(person)
- `Dr. Vogel`(person)
- `Dr. Jensik`(person)
- `Dr. Musger`(person)
- `Dr. Schwarzenbacher`(person)
- `Karen Böckel`(person)
- `Kosesnik-Wehrle & Langer Rechtsanwälte KG`(organisation)
- `Düwall + Rief Daten -Aktiengesellschaft`(organisation)
- `Gassing/Burgweg 63, 4613 Mistelbach bei Wels, Österreich`(address)
- `Raits Bleiziffer Rechtsanwälte GmbH`(organisation)
- `Eberhard Besemer`(person)
- `Linda Hukauf`(person)
- `Dr. Peter Zöchbauer`(person)
- `Oberlandesgerichts Linz`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/4Ob119_22m`) (sent_id: `deanon_260716_TRAIN/4Ob119_22m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Kodek sowie die Hofräte Dr. Schwarzenbacher, Dr. Nowotny und Hon.-Prof. PD Dr. Rassi und die Hofrätin Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei Silvester Schusterius KG, Brunnsteinweg 3, 9602 Draschitz, Österreich, vertreten durch Dr. Franz Krainer, Rechtsanwalt in Graz, gegen die beklagte Partei TalVerlag Manufaktur GmbH, Dr. Leopold Bauer-Gasse 105, 4843 Hinterschlagen, Österreich, vertreten durch die Hohenberg Rechtsanwälte GmbH in Graz, wegen 84.521,61 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz vom 12. Mai 2022, GZ 5 R 170/21s-33, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Silvester Schusterius KG` — partial — gold is substring of pred: `Silvester Schusterius`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. Schwarzenbacher`(person)
- `Dr. Nowotny`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Mag. Istjan, LL.M.`(person)
- `Silvester Schusterius`(person)
- `Brunnsteinweg 3, 9602 Draschitz, Österreich`(address)
- `Dr. Franz Krainer`(person)
- `TalVerlag Manufaktur GmbH`(organisation)
- `Dr. Leopold Bauer-Gasse 105, 4843 Hinterschlagen, Österreich`(address)
- `Hohenberg Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Graz`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/4Ob180_10i`) (sent_id: `deanon_260716_TRAIN/4Ob180_10i_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Nimtz Pharma GmbH, Mildenbergstraße 11, 3072 Furth, Österreich, vertreten durch Berger Saurer Zöchbauer, Rechtsanwälte in Wien, gegen die beklagten Parteien 1) Unikel Landwirtschaft GmbH & Co KG und 2) Gode+Panköker Getränke GmbH, Martinsplatz 1-31, 9831 Kleindorf, Österreich, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Provisorialverfahren 36.000 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 6. August 2010, GZ 5 R 150/10f-7, womit der Beschluss des Handelsgerichts Wien vom 24. Juni 2010, GZ 11 Cg 117/10h-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Sommer Rechtsanwälte KG` — partial — pred is substring of gold: `Gheneff - Rami - Sommer Rechtsanwälte KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schenk`(person)
- `Dr. Vogel`(person)
- `Dr. Jensik`(person)
- `Dr. Musger`(person)
- `Dr. Schwarzenbacher`(person)
- `Nimtz Pharma GmbH`(organisation)
- `Mildenbergstraße 11, 3072 Furth, Österreich`(address)
- `Berger Saurer Zöchbauer, Rechtsanwälte`(organisation)
- `Unikel Landwirtschaft GmbH & Co KG`(organisation)
- `Gode+Panköker Getränke GmbH`(organisation)
- `Martinsplatz 1-31, 9831 Kleindorf, Österreich`(address)
- `Gheneff - Rami - Sommer Rechtsanwälte KG`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/5Ob146_16f`) (sent_id: `deanon_260716_TRAIN/5Ob146_16f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers Mag. Pamela Keilonat, vertreten durch Dr. Anke Reisch, Rechtsanwältin in Kitzbühel, gegen die Antragsgegnerin Hoch Dorfder GmbH & Co KG, Lichtensternweg 19, 4714 Meggenhofen, Österreich, vertreten durch Dr. Lisbeth Lass und Dr. Hans Christian Lass, Rechtsanwälte in Innsbruck, wegen § 52 Abs 1 Z 6 iVm § 20 Abs 3 WEG 2002, infolge des „außerordentlichen“ Revisionsrekurses des Antragstellers gegen den (richtig) Sachbeschluss des Landesgerichts Innsbruck vom 24. Mai 2016, GZ 4 R 128/16a-50, mit dem der Sachbeschluss des Bezirksgerichts Kitzbühel vom 14. März 2016, GZ 4 Msch 7/14x-36, abgeändert wurde, den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt. Begründung:  Rechtliche Beurteilung Der Antragsteller begehrt Rechnungslegung nach § 52 Abs 1 Z 6 iVm § 20 Abs 3 WEG 2002.

**False Positives:**

- `Antragsgegnerin Hoch Dorfder GmbH & Co KG` — partial — gold is substring of pred: `Hoch Dorfder GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Höllwerth`(person)
- `Dr. Grohmann`(person)
- `Mag. Wurzer`(person)
- `Mag. Painsi`(person)
- `Mag. Pamela Keilonat`(person)
- `Dr. Anke Reisch`(person)
- `Hoch Dorfder GmbH & Co KG`(organisation)
- `Lichtensternweg 19, 4714 Meggenhofen, Österreich`(address)
- `Dr. Lisbeth Lass`(person)
- `Dr. Hans Christian Lass`(person)
- `Landesgerichts Innsbruck`(organisation)
- `Bezirksgerichts Kitzbühel`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/5Ob259_15x`) (sent_id: `deanon_260716_TRAIN/5Ob259_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers Shoshana Dimpfel, vertreten durch Hofbauer & Wagner Rechtsanwälte KG in St. Pölten, gegen den Antragsgegner Adolf Beehr, vertreten durch Dr. Franz Gütlbauer, Dr. Siegfried Sieghartsleitner, Dr. Michael Pichlmair, Rechtsanwälte in Wels, wegen § 8 Abs 2 MRG (hier: wegen Abänderung des Sachbeschlusses des Bezirksgerichts Traun vom 18. März 2014, GZ 17 Msch 6/13m-8) über den „Rekurs“ des Antragsgegners gegen den Beschluss des Landesgerichts Linz als Rekursgericht vom 8. Oktober 2015, GZ 14 R 56/15a-22, mit dem der Beschluss des Bezirksgerichts Traun vom 25. Februar 2015, GZ 17 Msch 6/13m-18, bestätigt wurde, den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Wagner Rechtsanwälte KG` — partial — pred is substring of gold: `Hofbauer & Wagner Rechtsanwälte KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Höllwerth`(person)
- `Dr. Grohmann`(person)
- `Mag. Wurzer`(person)
- `Mag. Painsi`(person)
- `Shoshana Dimpfel`(person)
- `Hofbauer & Wagner Rechtsanwälte KG`(organisation)
- `Adolf Beehr`(person)
- `Dr. Franz Gütlbauer`(person)
- `Dr. Siegfried Sieghartsleitner`(person)
- `Dr. Michael Pichlmair`(person)
- `Bezirksgerichts Traun`(organisation)
- `Landesgerichts Linz`(organisation)
- `Bezirksgerichts Traun`(organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/6Ob105_20i`) (sent_id: `deanon_260716_TRAIN/6Ob105_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden, die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Jaden Ince, vertreten durch Mag. Erwin Falkner, Rechtsanwalt in Wien, gegen die beklagte Partei R. Enns Verfurt GmbH, Greifenberg 38, 4972 Windhag, Österreich, vertreten durch Hoffmann & Sykora Rechtsanwälte KG in Tulln, wegen 6.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts St. Pölten als Berufungsgericht vom 13. November 2019, GZ 21 R 208/19z-53, womit über Berufung der klagenden Partei das Urteil des Bezirksgerichts Tulln vom 23. Juni 2019, GZ 11 C 276/18p-49, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Sykora Rechtsanwälte KG` — partial — pred is substring of gold: `Hoffmann & Sykora Rechtsanwälte KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schramm`(person)
- `Hon.-Prof. Dr. Gitschthaler`(person)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. Nowotny`(person)
- `Dr. Faber`(person)
- `Jaden Ince`(person)
- `Mag. Erwin Falkner`(person)
- `Enns Verfurt GmbH`(organisation)
- `Greifenberg 38, 4972 Windhag, Österreich`(address)
- `Hoffmann & Sykora Rechtsanwälte KG`(organisation)
- `Landesgerichts St. Pölten`(organisation)
- `Bezirksgerichts Tulln`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/6Ob56_19g`) (sent_id: `deanon_260716_TRAIN/6Ob56_19g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1060 Wien, Linke Wienzeile 18, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei QUMV Pflege GmbH, Nordring 89q, 2770 Gutenstein, Österreich, vertreten durch Dr. Peter Lindinger Dr. Andreas Pramer GesbR, Rechtsanwälte in Linz, wegen Unterlassung und Urteilsveröffentlichung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2019, GZ 3 R 141/18b-17, mit dem über Berufungen der klagenden und der beklagten Partei das Urteil des Landesgerichts Linz vom 2. September 2018, GZ 31 Cg 4/18a-9, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Langer Rechtsanwälte KG` — partial — pred is substring of gold: `Kosesnik-Wehrle & Langer Rechtsanwälte KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schramm`(person)
- `Dr. Gitschthaler`(person)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. Nowotny`(person)
- `Dr. Faber`(person)
- `Verein für Konsumenteninformation`(organisation)
- `Kosesnik-Wehrle & Langer Rechtsanwälte KG`(organisation)
- `QUMV Pflege GmbH`(organisation)
- `Nordring 89q, 2770 Gutenstein, Österreich`(address)
- `Dr. Peter Lindinger`(person)
- `Dr. Andreas Pramer`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Linz`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/8Ob86_22p`) (sent_id: `deanon_260716_TRAIN/8Ob86_22p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen und Hofräte Dr. Tarmann-Prentner, Mag. Korn, Dr. Stefula und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Roland Buehn, Bakk. techn., vertreten durch Dr. Hannes Paulweber, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Silvius Tomzig, vertreten durch Dr. Roland Gabl Rechtsanwalts KG in Linz, wegen Unterhalt, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 2. Juni 2022, GZ 4 R 93/22p-66, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Roland Gabl Rechtsanwalts KG` — partial — pred is substring of gold: `Dr. Roland Gabl Rechtsanwalts KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Tarmann-Prentner`(person)
- `Mag. Korn`(person)
- `Dr. Stefula`(person)
- `Dr. Thunhart`(person)
- `Roland Buehn, Bakk. techn.`(person)
- `Dr. Hannes Paulweber`(person)
- `Silvius Tomzig`(person)
- `Dr. Roland Gabl Rechtsanwalts KG`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/9ObA144_14p`) (sent_id: `deanon_260716_TRAIN/9ObA144_14p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden und die Hofräte des Obersten Gerichtshofs Mag. Ziegelbauer und Dr. Hargassner sowie die fachkundigen Laienrichter KR Mag. Paul Kunsky und Harald Kohlruss als weitere Richter in der Arbeitsrechtssache der klagenden Partei Franziska Schönmeier, vertreten durch Held Berdnik Astner & Partner Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Heizung Bachkraftlog GmbH & Co KG, Schlangglfeld 48, 4980 Viehausen, Österreich, vertreten durch die Klein, Wuntschek & Partner Rechtsanwälte GmbH in Graz, wegen Kündigungsanfechtung, über die außerordentliche Revision und den „Kostenrekurs“ der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 26. September 2014, GZ 7 Ra 66/14a-25, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Heizung Bachkraftlog GmbH & Co KG` — partial — gold is substring of pred: `Heizung Bachkraftlog GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hopf`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Ziegelbauer`(person)
- `Dr. Hargassner`(person)
- `KR Mag. Paul Kunsky`(person)
- `Harald Kohlruss`(person)
- `Franziska Schönmeier`(person)
- `Held Berdnik Astner & Partner Rechtsanwälte GmbH`(organisation)
- `Heizung Bachkraftlog GmbH & Co KG`(organisation)
- `Schlangglfeld 48, 4980 Viehausen, Österreich`(address)
- `Klein, Wuntschek & Partner Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Graz`(organisation)

</details>

---

## `GmbH Company Names` 🏆

**F1:** 0.059 | **Precision:** 0.292 | **Recall:** 0.033  

**Format:** `regex`  
**Rule ID:** `dad0bfdb`  
**Description:**
Matches company names ending in 'GmbH' with any alphanumeric prefix, including multiple words, hyphens, and '&' symbols, ensuring the full name is captured.

**Content:**
```
(?<!Firma\s)(?<!Fa\.\s)\b([A-Z][A-Za-z\u00e4\u00f6\u00fc\u00df\-\d\s&]+(?:\s+[A-Z][A-Za-z\u00e4\u00f6\u00fc\u00df\-\d\s&]+)*\s+GmbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.292 | 0.033 | 0.059 | 449 | 131 | 318 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 131 | 318 | 3864 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der beim Landesgericht Linz zu AZ 3 Cg 46/21a anhängigen Rechtssache der klagenden Partei Hollengk Planung GmbH, Am Steindl 3, 9873 Döbriach, Österreich, vertreten durch Huber Berchtold Rechtsanwälte OG in Wien, gegen die beklagte Partei Wind Nexheimval GmbH, Wiesbergsiedlung 4, 8341 Pöllau, Österreich, vertreten durch ScherbaumSeebacher Rechtsanwälte GmbH in Graz, wegen 188.117,55 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN folgenden Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, zur Verhandlung und Entscheidung der Rechtssache anstelle des Landesgerichts Linz das Landesgericht Korneuburg zu bestimmen, wird abgewiesen.

| Predicted | Gold |
|---|---|
| `ScherbaumSeebacher Rechtsanwälte GmbH` | `ScherbaumSeebacher Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Landesgericht Linz` (organisation)
- `Hollengk Planung GmbH` (organisation)
- `Am Steindl 3, 9873 Döbriach, Österreich` (address)
- `Huber Berchtold Rechtsanwälte OG` (organisation)
- `Wind Nexheimval GmbH` (organisation)
- `Wiesbergsiedlung 4, 8341 Pöllau, Österreich` (address)
- `Landesgerichts Linz` (organisation)
- `Landesgericht Korneuburg` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie durch die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Hon.-Prof.in KzlR Iris Makowska, vertreten durch Skribe Rechtsanwaelte GmbH in Wien, gegen die beklagte Partei Dieter Apfelbacher Ltd, Am Fundbach 31w, 9170 Tratten, Österreich, wegen 400 EUR sA, über den Ordinationsantrag nach § 28 JN in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `Skribe Rechtsanwaelte GmbH` | `Skribe Rechtsanwaelte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Hon.-Prof.in KzlR Iris Makowska` (person)
- `Dieter Apfelbacher` (person)
- `Am Fundbach 31w, 9170 Tratten, Österreich` (address)
- `Bezirksgericht Schwechat` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Paulina Nüsken, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Oliver Eylart, Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `Skribe Rechtsanwälte GmbH` | `Skribe Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Paulina Nüsken` (person)
- `Oliver Eylart` (person)
- `Bezirksgericht Schwechat` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Eva Abdelrahman, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei Hochenadel Immobilien GmbH, Ritterhof 11, 2661 Graben, Österreich, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Lederer Rechtsanwalt GmbH` | `Lederer Rechtsanwalt GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Korn` (person)
- `Eva Abdelrahman` (person)
- `Dr. Karl-Heinz Plankel` (person)
- `Hochenadel Immobilien GmbH` (organisation)
- `Ritterhof 11, 2661 Graben, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Ob18_13i`) (sent_id: `deanon_260716_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei SüdSanitär Gruppe GmbH, Rinzendorf 28, 4501 Lindach, Österreich, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Kraft & Winternitz Rechtsanwälte GmbH` | `Kraft & Winternitz Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Verein für Konsumenteninformation` (organisation)
- `Dr. Walter Reichholf` (person)
- `SüdSanitär Gruppe GmbH` (organisation)
- `Rinzendorf 28, 4501 Lindach, Österreich` (address)
- `Handelsgerichts Wien` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Ralph Prusseit, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Akbayrak Metall GmbH, Schroateck 57, 4710 Niederweng, Österreich, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Skribe Rechtsanwälte GmbH` | `Skribe Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Hon.-Prof. PD Dr. Rassi` (person)
- `Dr. Steger` (person)
- `Dr. Annerl` (person)
- `Dr. Wallner-Friedl` (person)
- `Ralph Prusseit` (person)
- `Mag. Franz Eckl` (person)
- `Akbayrak Metall GmbH` (organisation)
- `Schroateck 57, 4710 Niederweng, Österreich` (address)
- `Landesgerichts Krems an der Donau` (organisation)
- `Bezirksgerichts Zwettl` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Heimcon Software GmbH, H - Am Hang 3, 4912 Rettenbrunn, Österreich, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, gegen die beklagte Partei Gunter Landwirtschaft GmbH, Schlossfeld 38, 9300 Graßdorf, Österreich, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, wegen 7.731,06 EUR und Feststellung (Streitwert 20.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse insgesamt 11.597,42 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 216/14h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Vavrovsky Heine Marth Rechtsanwälte GmbH` | `Vavrovsky Heine Marth Rechtsanwälte GmbH` |
| `Stolz & Schartner Rechtsanwälte GmbH` | `Stolz & Schartner Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Korn` (person)
- `Heimcon Software GmbH` (organisation)
- `H - Am Hang 3, 4912 Rettenbrunn, Österreich` (address)
- `Gunter Landwirtschaft GmbH` (organisation)
- `Schlossfeld 38, 9300 Graßdorf, Österreich` (address)
- `Oberlandesgerichts Linz` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei DDr.in Cornelia Rinaldo, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Conmon-Verlag Limited, Kroisegg 20, 4052 Fleckendorf, Österreich Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Brandl Talos Rechtsanwälte GmbH` | `Brandl Talos Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Mag. Schober` (person)
- `Dr. Annerl` (person)
- `DDr.in Cornelia Rinaldo` (person)
- `Dr. Sven Rudolf Thorstensen` (person)
- `Conmon-Verlag Limited` (organisation)
- `Kroisegg 20, 4052 Fleckendorf, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_4`)


Malik Schoch, geboren 7. November 2002, 2. 7. Juli 2025, geboren 10. Juli 2004, und 3. Alan Schindlmair, geboren 7. August 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Timon Schönswetter, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Doschek Rechtsanwalts GmbH` | `Doschek Rechtsanwalts GmbH` |

**Missed by this rule (FN):**

- `Malik Schoch` (person)
- `7. November` (date)
- `7. Juli 2025` (date)
- `10. Juli` (date)
- `Alan Schindlmair` (person)
- `7. August` (date)
- `Mag. Florian Kucera` (person)
- `Mag. Timon Schönswetter` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Döbling` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_5`)


Unter Alver GmbH, beide Granglitzweg 11, 3251 Kroißenberg, Österreich, beide vertreten durch Dr. Michael Schneditz-Bolfras und andere Rechtsanwälte in Gmunden, wegen Bucheinsicht (in eventu Rechnungslegung) und Zahlung (Streitwert: 70.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Teilurteil des Oberlandesgerichts Linz als Berufungsgericht vom 17. Februar 2014, GZ 3 R 13/14y-90, womit das Urteil des Landesgerichts Wels vom 27. November 2013 (in der mit Beschluss vom 12. Dezember 2013 berichtigten Fassung), GZ 2 Cg 78/10p-82 und -84, abgeändert wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Unter Alver GmbH` | `Unter Alver GmbH` |

**Missed by this rule (FN):**

- `Granglitzweg 11, 3251 Kroißenberg, Österreich` (address)
- `Dr. Michael Schneditz-Bolfras` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Wels` (organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Brigitte Martz, geboren am 16. November 1978, wegen Kontaktrechts des Vaters Dr. Gustav Thöning, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Madeleine Musialik, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

| Predicted | Gold |
|---|---|
| `Kosch & Partner Rechtsanwälte GmbH` | `Kosch & Partner Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Brigitte Martz` (person)
- `16. November 1978` (date)
- `Dr. Gustav Thöning` (person)
- `Pieler & Pieler & Partner KG` (organisation)
- `Dr. Madeleine Musialik` (person)
- `Landesgerichts Wiener Neustadt` (organisation)
- `Bezirksgerichts Wiener Neustadt` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Cassandra Wespi, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Bilek Lebensmittel GmbH in Liqu, Dreijochgasse 11, 4722 Stefansdorf, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Vogl Rechtsanwalt GmbH` | `Vogl Rechtsanwalt GmbH` |
| `Wess Kux Kispert & Eckert Rechtsanwalts GmbH` | `Wess Kux Kispert & Eckert Rechtsanwalts GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `DI Cassandra Wespi` (person)
- `Bilek Lebensmittel GmbH` (organisation)
- `Dreijochgasse 11, 4722 Stefansdorf, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_6`)


Text Gründe: Mit dem angefochtenen Urteil wurden Bernhard Berti und Norbert Wierich von der wider sie erhobenen Anklage, sie hätten am 7. Februar 2009 in Sebastian-Stief-Gasse 48, 2632 Altendorf, Österreich /Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der Hauenschildt&Mesarec Medien GesmbH & Co KG, Susanne Schwarzhuber, durch die Vorgabe, die Donau-Transport GmbH sei eine zahlungsfähige Leasingnehmerin, somit durch Täuschung über Tatsachen, zum Abschluss eines Leasingvertrags über ein Rennfahrzeug für die Dauer von 24 Monaten zu einem monatlichen Entgelt von 10.698,10 Euro, somit zu einer Handlung verleitet, welche die TraunTouristik Werke GesmbH & Co KG in einem 50.000 Euro übersteigenden Betrag von insgesamt 235.358,20 Euro am Vermögen schädigte, gemäß § 259 Z 3 StPO (verfehlt auch von der rechtlichen Kategorie; vglLendl, WK-StPO § 259 Rz 1) freigesprochen.

| Predicted | Gold |
|---|---|
| `Donau-Transport GmbH` | `Donau-Transport GmbH` |

**Missed by this rule (FN):**

- `Bernhard Berti` (person)
- `Norbert Wierich` (person)
- `Sebastian-Stief-Gasse 48, 2632 Altendorf, Österreich` (address)
- `Hauenschildt&Mesarec Medien GesmbH & Co KG` (organisation)
- `Susanne Schwarzhuber` (person)
- `TraunTouristik Werke GesmbH & Co KG` (organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_8`)


Nach den wesentlichen Feststellungen (US 3 bis 6) befand sich die UAMA Analyse Consulting GmbH in der zweiten Jahreshälfte 2008 in erheblichen Zahlungsschwierigkeiten.

| Predicted | Gold |
|---|---|
| `UAMA Analyse Consulting GmbH` | `UAMA Analyse Consulting GmbH` |

**Example 14** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_11`)


„Nachdem“ es für die Songül Bau GmbH notwendig geworden war, für die Aufnahme des Rennbetriebs 35.000 Euro in das Fahrzeug zu investieren, konnte aufgrund dessen schlechten Zustands kein Rennen erfolgreich beendet werden.

| Predicted | Gold |
|---|---|
| `Songül Bau GmbH` | `Songül Bau GmbH` |

**Example 15** (doc_id: `deanon_260716_TRAIN/17Ob10_19y`) (sent_id: `deanon_260716_TRAIN/17Ob10_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende und die Hofräte Dr. Musger und Priv.-Doz. Dr. Rassi, die Hofrätin Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Dr. Joshua Reupold, als Masseverwalter über das Vermögen der Wald-Versand Gesellschaft mbH, Kugelmannplatz 4, 5121 Döstling, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, gegen die beklagten Parteien 1. Johanna Baldczus, und 2. MedR Nadja Grela, beide vertreten durch Schöpf & Maurer, Rechtsanwalt in Salzburg, wegen 59.028,60 EUR sA, aus Anlass der außerordentlichen Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. April 2019, GZ 1 R 161/18d-52, mit dem das Urteil des Landesgerichts Salzburg vom 30. August 2018, GZ 57 Cg 10/17z-43, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das angefochtene Urteil wird, soweit es die Abweisung des Teilbegehens, die beklagten Parteien seien zur ungeteilten Hand schuldig, der klagenden Partei 18.168,21 EUR samt 4 % Zinsen seit 15.

| Predicted | Gold |
|---|---|
| `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` | `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Dr. Musger` (person)
- `Priv.-Doz. Dr. Rassi` (person)
- `Dr. Kodek` (person)
- `Dr. Stefula` (person)
- `Dr. Joshua Reupold` (person)
- `Wald-Versand Gesellschaft mbH` (organisation)
- `Kugelmannplatz 4, 5121 Döstling, Österreich` (address)
- `Johanna Baldczus` (person)
- `MedR Nadja Grela` (person)
- `Maurer` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Salzburg` (organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/17Ob10_20z`) (sent_id: `deanon_260716_TRAIN/17Ob10_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätinnen Mag. Malesich und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Pascal Alsweh, vertreten durch Stephan Briem Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Dr. Simone Pittruff als Treuhänder der Insolvenzgläubiger der Unter-Analyse Aktiengesellschaft, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH in Linz, wegen Feststellung (Streitwert 18.335,66 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. März 2020, GZ 1 R 31/20i-13, womit das Urteil des Landesgerichts Linz vom 9. Dezember 2019, GZ 4 Cg 73/18z-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Stephan Briem Rechtsanwalt GmbH` | `Stephan Briem Rechtsanwalt GmbH` |
| `Shamiyeh & Reiser Rechtsanwälte GmbH` | `Shamiyeh & Reiser Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Dr. Musger` (person)
- `Mag. Malesich` (person)
- `Dr. Kodek` (person)
- `Dr. Stefula` (person)
- `Pascal Alsweh` (person)
- `Dr. Simone Pittruff` (person)
- `Unter-Analyse Aktiengesellschaft` (organisation)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Linz` (organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/18OCg12_19t`) (sent_id: `deanon_260716_TRAIN/18OCg12_19t_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Veith und die Hofräte Dr. Höllwerth, Priv.-Doz. Dr. Rassi und Mag. Painsi als weitere Richter in der Schiedsrechtssache der klagenden Partei Energie Glanzgart GmbH, Waldelweg 28, 4201 Maierleiten, Österreich, vertreten durch die SRG Stock Rafaseder Gruszkiewicz Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Piedro Arnoult, Bulgarien, wegen Aufhebung eines Schiedsspruchs (Streitwert 257.397,45 EUR), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Klage wird als nicht zur Bestimmung einer Tagsatzung zur mündlichen Verhandlung geeignet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `SRG Stock Rafaseder Gruszkiewicz Rechtsanwälte GmbH` | `SRG Stock Rafaseder Gruszkiewicz Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Veith` (person)
- `Dr. Höllwerth` (person)
- `Priv.-Doz. Dr. Rassi` (person)
- `Mag. Painsi` (person)
- `Energie Glanzgart GmbH` (organisation)
- `Waldelweg 28, 4201 Maierleiten, Österreich` (address)
- `Piedro Arnoult` (person)

**Example 18** (doc_id: `deanon_260716_TRAIN/1Ob105_18z`) (sent_id: `deanon_260716_TRAIN/1Ob105_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Familienrechtssache des Antragstellers Ludmilla Bonauer, vertreten durch die Korp Rechtsanwalts GmbH, Andorf, gegen die Antragsgegnerin Henriette Geißendorf, vertreten durch die Puttinger Vogl Rechtsanwälte GmbH, Ried im Innkreis, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts Wels als Rekursgericht vom 2. Mai 2018, GZ 21 R 50/18d-32, mit dem der Rekurs des Antragstellers gegen den Beschluss des Bezirksgerichts Grieskirchen vom 8. Jänner 2018, GZ 8 Fam 37/16i-26, zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Korp Rechtsanwalts GmbH` | `Korp Rechtsanwalts GmbH` |
| `Puttinger Vogl Rechtsanwälte GmbH` | `Puttinger Vogl Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Ludmilla Bonauer` (person)
- `Henriette Geißendorf` (person)
- `Landesgerichts Wels` (organisation)
- `Bezirksgerichts Grieskirchen` (organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/1Ob109_18p`) (sent_id: `deanon_260716_TRAIN/1Ob109_18p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Parteien 1. Mag. Eva Voeglein, und 2. Ursula Preising, vertreten durch die HOHENBERG STRAUSS BUCHBAUER Rechtsanwälte GmbH, Graz, gegen die beklagte Partei Gemeinde Veit Faeser, vertreten durch Dr. Klaus Rainer, Rechtsanwalt in Graz, wegen 573.890,70 EUR sA, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 2. Mai 2018, GZ 5 R 172/17d-57, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 23. Oktober 2017, GZ 41 Cg 51/15m-47, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `HOHENBERG STRAUSS BUCHBAUER Rechtsanwälte GmbH` | `HOHENBERG STRAUSS BUCHBAUER Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Mag. Eva Voeglein` (person)
- `Ursula Preising` (person)
- `Veit Faeser` (person)
- `Dr. Klaus Rainer` (person)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/1Ob127_14d`) (sent_id: `deanon_260716_TRAIN/1Ob127_14d_4`)


Republik Österreich, vertreten durch die Finanzprokuratur in Wien, 2. Dr. Melinda Steenbekke, und 3. Naujox und Obermauer Luftfahrt GmbH, Kreuten 4, 3385 Uttendorf, Österreich, beide vertreten durch Dr. Hubert Simon, Rechtsanwalt in Wien, wegen Leistung und Feststellung, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. April 2014, GZ 7 R 21/14h-7, mit dem der Beschluss des Landesgerichts Leoben vom 30. Jänner 2014, GZ 2 Nc 2/14y-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Naujox und Obermauer Luftfahrt GmbH` | `Naujox und Obermauer Luftfahrt GmbH` |

**Missed by this rule (FN):**

- `Dr. Melinda Steenbekke` (person)
- `Kreuten 4, 3385 Uttendorf, Österreich` (address)
- `Dr. Hubert Simon` (person)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts Leoben` (organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/1Ob12_21b`) (sent_id: `deanon_260716_TRAIN/1Ob12_21b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Mag. Mathias Gumbel, vertreten durch die Huber & Partner Rechtsanwälte GmbH, Linz, gegen die beklagten Parteien 1. Otto Gerdhennrich, 2.

| Predicted | Gold |
|---|---|
| `Huber & Partner Rechtsanwälte GmbH` | `Huber & Partner Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Mag. Mathias Gumbel` (person)
- `Otto Gerdhennrich` (person)

**Example 22** (doc_id: `deanon_260716_TRAIN/1Ob12_21b`) (sent_id: `deanon_260716_TRAIN/1Ob12_21b_5`)


Zlatan Schempf, alle vertreten durch die Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte GmbH, Wien, wegen Feststellung und Räumung, über die außerordentliche Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. November 2020, GZ 2 R 122/20d-54, mit dem das Urteil des Landesgerichts Wels vom 27. Juli 2020, GZ 2 Cg 84/18g-47, in der Hauptsache bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte GmbH` | `Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Zlatan Schempf` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Wels` (organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/1Ob152_24w`) (sent_id: `deanon_260716_TRAIN/1Ob152_24w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Musger als Vorsitzenden sowie die Hofrätin und die Hofräte Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Harald Adolphsen KG, FN FN214876m, vertreten durch Dr. Eva-Maria Bachmann-Lang, Dr. Christian Bachmann, Rechtsanwälte in Wien, gegen die beklagte Partei „ Alpen Donalcon “ OXS Bildung gmbH, FN FN067476g, vertreten durch die GRAF ISOLA Rechtsanwälte GmbH in Wien, wegen 51.843,91 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 3. Juli 2024, GZ 1 R 17/24p-39, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `GRAF ISOLA Rechtsanwälte GmbH` | `GRAF ISOLA Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Musger` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Mag. Wessely-Kristöfel` (person)
- `Dr. Parzmayr` (person)
- `Harald Adolphsen` (person)
- `FN214876m` (business_register_number)
- `Dr. Eva-Maria Bachmann` (person)
- `Dr. Christian Bachmann` (person)
- `Alpen Donalcon` (organisation)
- `OXS Bildung gmbH` (organisation)
- `FN067476g` (business_register_number)
- `Oberlandesgerichts Wien` (organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/1Ob159_20v`) (sent_id: `deanon_260716_TRAIN/1Ob159_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und Hofrätinnen, Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Bachfen Entwicklung AG, Reisedt 4, 4770 Radlern, Österreich, vertreten durch Mag. Markus Stender, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. Musialek Getränke GmbH, 2.

| Predicted | Gold |
|---|---|
| `Musialek Getränke GmbH` | `Musialek Getränke GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Mag. Korn` (person)
- `Bachfen Entwicklung AG` (organisation)
- `Reisedt 4, 4770 Radlern, Österreich` (address)
- `Mag. Markus Stender` (person)

**Example 25** (doc_id: `deanon_260716_TRAIN/1Ob226_20x`) (sent_id: `deanon_260716_TRAIN/1Ob226_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Pia Geermann GmbH, Orise 28, 9135 Unterort, Österreich, vertreten durch Dr. Martin Leitner und andere, Rechtsanwälte in Wien, gegen die beklagte Partei Stadt Li Wachmeister, vertreten durch die Estermann Pock Rechtsanwälte GmbH, Wien, wegen 19.002,01 EUR, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 7. September 2020, GZ 14 R 61/20y-27, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 28. Jänner 2020, GZ 31 Cg 1/19y-22, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Estermann Pock Rechtsanwälte GmbH` | `Estermann Pock Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Pia Geermann` (person)
- `Orise 28, 9135 Unterort, Österreich` (address)
- `Dr. Martin Leitner` (person)
- `Li Wachmeister` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der beim Landesgericht Linz zu AZ 3 Cg 46/21a anhängigen Rechtssache der klagenden Partei Hollengk Planung GmbH, Am Steindl 3, 9873 Döbriach, Österreich, vertreten durch Huber Berchtold Rechtsanwälte OG in Wien, gegen die beklagte Partei Wind Nexheimval GmbH, Wiesbergsiedlung 4, 8341 Pöllau, Österreich, vertreten durch ScherbaumSeebacher Rechtsanwälte GmbH in Graz, wegen 188.117,55 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN folgenden Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, zur Verhandlung und Entscheidung der Rechtssache anstelle des Landesgerichts Linz das Landesgericht Korneuburg zu bestimmen, wird abgewiesen.

**False Positives:**

- `Rechtssache der klagenden Partei Hollengk Planung GmbH` — partial — gold is substring of pred: `Hollengk Planung GmbH`
- `Partei Wind Nexheimval GmbH` — partial — gold is substring of pred: `Wind Nexheimval GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Landesgericht Linz`(organisation)
- `Hollengk Planung GmbH`(organisation)
- `Am Steindl 3, 9873 Döbriach, Österreich`(address)
- `Huber Berchtold Rechtsanwälte OG`(organisation)
- `Wind Nexheimval GmbH`(organisation)
- `Wiesbergsiedlung 4, 8341 Pöllau, Österreich`(address)
- `ScherbaumSeebacher Rechtsanwälte GmbH`(organisation)
- `Landesgerichts Linz`(organisation)
- `Landesgericht Korneuburg`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Marlene Friss, Russische Föderation, gegen die verpflichtete Partei WestTelekom GmbH, Rehwald 11, 4723 Fronberg, Österreich, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

**False Positives:**

- `Partei WestTelekom GmbH` — partial — gold is substring of pred: `WestTelekom GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Marlene Friss`(person)
- `WestTelekom GmbH`(organisation)
- `Rehwald 11, 4723 Fronberg, Österreich`(address)
- `Bezirksgericht Innere Stadt Wien`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Ober-Automotive GmbH, Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei Katharina Rothschadl, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Hoch als weitere Richter in der Rechtssache der klagenden Partei Ober-Automotive GmbH` — positional overlap with gold: `Dr. Hoch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Ober-Automotive GmbH`(organisation)
- `Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich`(address)
- `Mag. Alexander Rimser`(person)
- `Katharina Rothschadl`(person)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Steidlen+Ysner Daten GmbH, Kaminweg 34, 8200 Laßnitzthal, Österreich, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Verlag Waldlemder GmbH, Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

**False Positives:**

- `Ysner Daten GmbH` — partial — pred is substring of gold: `Steidlen+Ysner Daten GmbH`
- `Partei Verlag Waldlemder GmbH` — partial — gold is substring of pred: `Verlag Waldlemder GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Landesgericht Linz`(organisation)
- `Steidlen+Ysner Daten GmbH`(organisation)
- `Kaminweg 34, 8200 Laßnitzthal, Österreich`(address)
- `Dr. Roland Kassowitz`(person)
- `Verlag Waldlemder GmbH`(organisation)
- `Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich`(address)
- `Prof. Haslinger`(person)
- `Landesgerichts Linz`(organisation)
- `Handelsgericht Wien`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_4`)


Text Begründung: Die klagende GmbH mit dem Sitz in Wien begehrt von der beklagten GmbH mit dem Sitz in Linz aus dem Titel des Schadenersatzes 174.624,53 EUR sA.

**False Positives:**

- `Die klagende GmbH mit dem Sitz in Wien begehrt von der beklagten GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Rechtssache der klagenden Partei Mur Dorftalnex Technologien -GmbH, Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich, vertreten durch Dr. Peter Lechner und Dr. Hermann Pfurtscheller, Rechtsanwälte in Innsbruck, und ihrer Nebenintervenientin Ober Dertri GmbH, Hintereggweg 93, 2070 Kleinhöflein, Österreich, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Rudolf Ketelhut GmbH, Fiebrichgasse 17, 5120 Seeleiten, Österreich, vertreten durch Rechtsanwaltskanzlei Dr. Bernhard Hämmerle GmbH in Innsbruck, und ihrer Nebenintervenientin Völkertz Energie GmbH, Brunnbachweg 19, 4653 Mayersdorf, Österreich, vertreten durch Dr. Franz Pechmann, Rechtsanwalt in Wien, wegen 696.238,34 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck vom 2. Oktober 2009, GZ 4 R 108/09b-167, mit dem das Urteil des Landesgerichts Innsbruck vom 23. Februar 2009, GZ 41 Cg 228/01z-152, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

**False Positives:**

- `Nebenintervenientin Ober Dertri GmbH` — partial — gold is substring of pred: `Ober Dertri GmbH`
- `Partei Rudolf Ketelhut GmbH` — partial — gold is substring of pred: `Rudolf Ketelhut`
- `Bernhard Hämmerle GmbH` — partial — pred is substring of gold: `Dr. Bernhard Hämmerle GmbH`
- `Nebenintervenientin Völkertz Energie GmbH` — partial — gold is substring of pred: `Völkertz Energie GmbH`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schinko`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Hon.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Mur Dorftalnex Technologien -GmbH`(organisation)
- `Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich`(address)
- `Dr. Peter Lechner`(person)
- `Dr. Hermann Pfurtscheller`(person)
- `Ober Dertri GmbH`(organisation)
- `Hintereggweg 93, 2070 Kleinhöflein, Österreich`(address)
- `Dr. Thomas Girardi`(person)
- `Rudolf Ketelhut`(person)
- `Fiebrichgasse 17, 5120 Seeleiten, Österreich`(address)
- `Dr. Bernhard Hämmerle GmbH`(organisation)
- `Völkertz Energie GmbH`(organisation)
- `Brunnbachweg 19, 4653 Mayersdorf, Österreich`(address)
- `Dr. Franz Pechmann`(person)
- `Oberlandesgerichts Innsbruck`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Eva Abdelrahman, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei Hochenadel Immobilien GmbH, Ritterhof 11, 2661 Graben, Österreich, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Hochenadel Immobilien GmbH` — partial — gold is substring of pred: `Hochenadel Immobilien GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Mag. Korn`(person)
- `Eva Abdelrahman`(person)
- `Dr. Karl-Heinz Plankel`(person)
- `Hochenadel Immobilien GmbH`(organisation)
- `Ritterhof 11, 2661 Graben, Österreich`(address)
- `Lederer Rechtsanwalt GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Juri Gerstl GmbH, Mutten 18, 3251 Schauboden, Österreich, vertreten durch Dr. Ralph Trischler, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, sowie die Nebenintervenientin auf Seiten der beklagten Partei Bundesbeschaffung GmbH, 1020 Wien, Lassallestraße 9b, vertreten durch die Olischar Rechtsanwaltsgesellschaft mbH in Wien, wegen 15.535 EUR sA, über den Revisionsrekurs der klagenden Partei (Revisionsinteresse: 7.460 EUR), gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 23. Februar 2023, GZ 16 R 168/22a-20, mit welchem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 5. September 2022, GZ 11 Cg 48/22t-12, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Thunhart als weitere Richter in der Rechtssache der klagenden Partei Juri Gerstl GmbH` — positional overlap with gold: `Dr. Thunhart`
- `Nebenintervenientin auf Seiten der beklagten Partei Bundesbeschaffung GmbH` — partial — gold is substring of pred: `Bundesbeschaffung GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Mag. Schober`(person)
- `Dr. Thunhart`(person)
- `Juri Gerstl`(person)
- `Mutten 18, 3251 Schauboden, Österreich`(address)
- `Dr. Ralph Trischler`(person)
- `Bundesbeschaffung GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_5`)


Anita Schetzel, vertreten durch die Summereder Pichler Wächter Rechtsanwälte GmbH in Leonding, wegen 12.750 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Wels als Berufungsgericht vom 13. Dezember 2023, GZ 21 R 277/23v-53, mit dem das Urteil des Bezirksgerichts Wels vom 23. August 2023, GZ 9 C 430/22s-47, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Die Revision wird in Ansehung der Klageforderungen von 2.700 EUR sA, 4.575 EUR sA und 450 EUR sA zurückgewiesen.

**False Positives:**

- `Summereder Pichler Wächter Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Anita Schetzel`(person)
- `Landesgerichts Wels`(organisation)
- `Bezirksgerichts Wels`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Ob18_13i`) (sent_id: `deanon_260716_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei SüdSanitär Gruppe GmbH, Rinzendorf 28, 4501 Lindach, Österreich, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Partei SüdSanitär Gruppe GmbH` — partial — gold is substring of pred: `SüdSanitär Gruppe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Verein für Konsumenteninformation`(organisation)
- `Dr. Walter Reichholf`(person)
- `SüdSanitär Gruppe GmbH`(organisation)
- `Rinzendorf 28, 4501 Lindach, Österreich`(address)
- `Kraft & Winternitz Rechtsanwälte GmbH`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Ralph Prusseit, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Akbayrak Metall GmbH, Schroateck 57, 4710 Niederweng, Österreich, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Gegnerin der gefährdeten Partei Akbayrak Metall GmbH` — partial — gold is substring of pred: `Akbayrak Metall GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Dr. Steger`(person)
- `Dr. Annerl`(person)
- `Dr. Wallner-Friedl`(person)
- `Ralph Prusseit`(person)
- `Mag. Franz Eckl`(person)
- `Akbayrak Metall GmbH`(organisation)
- `Schroateck 57, 4710 Niederweng, Österreich`(address)
- `Skribe Rechtsanwälte GmbH`(organisation)
- `Landesgerichts Krems an der Donau`(organisation)
- `Bezirksgerichts Zwettl`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Heimcon Software GmbH, H - Am Hang 3, 4912 Rettenbrunn, Österreich, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, gegen die beklagte Partei Gunter Landwirtschaft GmbH, Schlossfeld 38, 9300 Graßdorf, Österreich, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, wegen 7.731,06 EUR und Feststellung (Streitwert 20.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse insgesamt 11.597,42 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 216/14h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Korn als weitere Richter in der Rechtssache der klagenden Partei Heimcon Software GmbH` — positional overlap with gold: `Mag. Korn`
- `Partei Gunter Landwirtschaft GmbH` — partial — gold is substring of pred: `Gunter Landwirtschaft GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Mag. Korn`(person)
- `Heimcon Software GmbH`(organisation)
- `H - Am Hang 3, 4912 Rettenbrunn, Österreich`(address)
- `Vavrovsky Heine Marth Rechtsanwälte GmbH`(organisation)
- `Gunter Landwirtschaft GmbH`(organisation)
- `Schlossfeld 38, 9300 Graßdorf, Österreich`(address)
- `Stolz & Schartner Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Linz`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_82`)


Ein Geschäftsführer, der eine persönliche Bürgschaft für Schulden einer GmbH übernehme, sei mangels eines eigenen Unternehmens als Verbraucher anzusehen.

**False Positives:**

- `Bürgschaft für Schulden einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_152`)


Zwar wurde in der Entscheidung 1 Ob 188/09t davon ausgegangen, dass die Ratenvereinbarung dem Geschäftsführer einer GmbH insoweit nutze, als infolge Fortführung des Unternehmens dessen Existenzgrundlage zunächst erhalten bleibe (siehe auch 8 Ob 100/03v;

**False Positives:**

- `Ratenvereinbarung dem Geschäftsführer einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_15`)


Mit Vertrag vom 28. 3. 2007 wurden die Lizenznehmerinnen nach Firmenänderung als übertragende Gesellschaften mit der Albrucklog Event GmbH als übernehmende Gesellschaft verschmolzen, die am 26.

**False Positives:**

- `Lizenznehmerinnen nach Firmenänderung als übertragende Gesellschaften mit der Albrucklog Event GmbH` — partial — gold is substring of pred: `Albrucklog Event GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Albrucklog Event GmbH`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/10Ob28_19v`) (sent_id: `deanon_260716_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Bau Zorostfurt GmbH, Isbarystraße 47, 4152 Schölling, Österreich, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Buitenkamp und Rothauge Landwirtschaft GmbH, Gewerbegebiet Mathon 17, 3672 Reitern, Österreich, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Faber als weitere Richter in der Rechtssache der klagenden Partei Bau Zorostfurt GmbH` — positional overlap with gold: `Dr. Faber`
- `Partei Buitenkamp und Rothauge Landwirtschaft GmbH` — partial — gold is substring of pred: `Buitenkamp und Rothauge Landwirtschaft GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Bau Zorostfurt GmbH`(organisation)
- `Isbarystraße 47, 4152 Schölling, Österreich`(address)
- `Dr. Alexandra Slama`(person)
- `Buitenkamp und Rothauge Landwirtschaft GmbH`(organisation)
- `Gewerbegebiet Mathon 17, 3672 Reitern, Österreich`(address)
- `Grassner, Lenz, Thewanger & Partner, Rechtsanwälte`(organisation)
- `Oberlandesgerichts Linz`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_5`)


Text Begründung: [1] Mit Kreditvertrag 15. September 2016 räumte die Klägerin einer GmbH, einen Kredit über 1,85 Mio EUR ein, wobei ihr die Jahresabschlüsse 2012 bis 2015 zur Verfügung standen.

**False Positives:**

- `September 2016 räumte die Klägerin einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_6`)


Der Beklagte unterfertigte als (damals einziger) Geschäftsführer den Kreditvertrag für die GmbH und übernahm für den Kredit im Umfang von 500.000 EUR die persönliche Haftung als Bürge und Zahler.

**False Positives:**

- `Geschäftsführer den Kreditvertrag für die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_7`)


[2] Am 16. Jänner 2018 wurde über das Vermögen der GmbH das Insolvenzverfahren eröffnet und im August 2018 Masseunzulänglichkeit angezeigt.

**False Positives:**

- `Jänner 2018 wurde über das Vermögen der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_9`)


Er trat deswegen im Mai 2018 an die Klägerin heran, um eine Regelung seiner „persönlichen Haftungen“ über „rund 500.000 EUR“ aus der „Bürgschaft Norallex-Heizung GmbH“ zu erreichen.

**False Positives:**

- `Bürgschaft Norallex-Heizung GmbH` — partial — gold is substring of pred: `Norallex-Heizung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Norallex-Heizung GmbH`(organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_20`)


Darüber hinaus habe er vor Abschluss des Vergleichs sogar explizit darauf hingewiesen, dass mögliche Haftungen als ehemaliger Geschäftsführer der GmbH in der Aufstellung seiner Passiva nicht berücksichtigt seien.

**False Positives:**

- `Haftungen als ehemaliger Geschäftsführer der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_51`)


Auch in der Korrespondenz bzw den vom Beklagten erstatteten Vergleichsvorschlägen war immer nur von Verbindlichkeiten über 500.000 EUR aus seiner Haftung für Schulden der GmbH die Rede.

**False Positives:**

- `EUR aus seiner Haftung für Schulden der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_55`)


Die Verhandlungen bis zum Vergleichsabschluss beschränkten sich demnach durchgehend auf einen Nachlass bezüglich der dem Grunde und der Höhe nach unstrittigen Forderung aus der (vertraglichen) Haftung des Beklagten für die Schulden der GmbH.

**False Positives:**

- `Haftung des Beklagten für die Schulden der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_72`)


Zusammenfassend ergibt die Auslegung des Vergleichs, dass dieser nur die bis zu seinem Abschluss allein thematisierten Ansprüche aus der Haftung des Beklagten als Bürge und Zahler für die Verbindlichkeiten der GmbH, nicht aber etwaige andere, insbesondere deliktische Ansprüche der Klägerin umfasst.

**False Positives:**

- `Abschluss allein thematisierten Ansprüche aus der Haftung des Beklagten als Bürge und Zahler für die Verbindlichkeiten der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Partei Drau-Pharma GmbH` — partial — gold is substring of pred: `Drau-Pharma GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Mag. Korn`(person)
- `Langhansl+Antonewitz Chemie AG`(organisation)
- `Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich`(address)
- `Poinstingl & Partner Rechtsanwälte OG`(organisation)
- `Drau-Pharma GmbH`(organisation)
- `Strazzegasse 12, 8762 Oberzeiring, Österreich`(address)
- `Mag. Johannes Bügler`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Wiener Neustadt`(organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_10`)


Die Beklagte wies bei diesem Gespräch auch auf ihre angespannte wirtschaftliche Situation hin und dass sie im GmbH-Recht nicht so bewandert sei; sie gab an, dass sie eine Gewinnauszahlung aus der GmbH erreichen wolle.

**False Positives:**

- `Die Beklagte wies bei diesem Gespräch auch auf ihre angespannte wirtschaftliche Situation hin und dass sie im GmbH` — no gold match — likely missing annotation
- `Gewinnauszahlung aus der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 26** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Cassandra Wespi, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Bilek Lebensmittel GmbH in Liqu, Dreijochgasse 11, 4722 Stefansdorf, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei Bilek Lebensmittel GmbH` — partial — gold is substring of pred: `Bilek Lebensmittel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `DI Cassandra Wespi`(person)
- `Vogl Rechtsanwalt GmbH`(organisation)
- `Bilek Lebensmittel GmbH`(organisation)
- `Dreijochgasse 11, 4722 Stefansdorf, Österreich`(address)
- `Wess Kux Kispert & Eckert Rechtsanwalts GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_5`)


Text Begründung: Der Kläger erwarb als Verbraucher im Juni 2003 über Vermittlung eines selbständigen Vermögensberaters Kommanditanteile an der GBJU Getränke GmbH & Co KG im Nominale von 17.000 EUR zuzüglich 850 EUR Agio.

**False Positives:**

- `Der Kläger erwarb als Verbraucher im Juni 2003 über Vermittlung eines selbständigen Vermögensberaters Kommanditanteile an der GBJU Getränke GmbH` — positional overlap with gold: `GBJU Getränke GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `GBJU Getränke GmbH & Co KG`(organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_6`)


Text Entscheidungsgründe: Mit Bescheid vom 26. 4. 2010 lehnte die beklagte Partei den Antrag des Klägers auf Gewährung der Kostenerstattung für die Inanspruchnahme der QVAO Planung GmbH (im Folgenden kurz: GmbH) laut Rechnungen vom 2. 10. 2009 und 6. 11. 2009 in Höhe von insgesamt 540 EUR ab.

**False Positives:**

- `Partei den Antrag des Klägers auf Gewährung der Kostenerstattung für die Inanspruchnahme der QVAO Planung GmbH` — partial — gold is substring of pred: `QVAO Planung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `QVAO Planung GmbH`(organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_7`)


Mit seiner gegen den Bescheid fristgerecht erhobenen „sozialrechtlichen Klage“ begehrt der Kläger, die beklagte Partei schuldig zu erkennen, die Kosten für die Inanspruchnahme der GmbH laut Rechnungen vom 2. 10. 2009 und 6. 11. 2009 in Höhe von insgesamt 540 EUR zu übernehmen.

**False Positives:**

- `Kosten für die Inanspruchnahme der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_9`)


Nach Erhalt von Bewilligungen der beklagten Partei für physikalische Behandlungen habe er entsprechende Leistungen der GmbH in Anspruch genommen und dafür insgesamt 540 EUR bezahlt. Die Behandlung stelle eine Krankenbehandlung dar und sei medizinisch notwendig und erfolgreich gewesen.

**False Positives:**

- `Nach Erhalt von Bewilligungen der beklagten Partei für physikalische Behandlungen habe er entsprechende Leistungen der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_12`)


Dem für die GmbH tätigen Team gehörten renommierte Fachärzte für medizinische Unfallchirurgie sowie Sportärzte an.

**False Positives:**

- `Dem für die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_18`)


Es habe jedoch keine (natürliche) Person die genannten Leistungen verrechnet, sondern eine - ohne Bewilligung als Krankenanstalt bzw selbständiges Ambulatorium - tätige GmbH, sodass die Kostenerstattung zur Gänze abzulehnen gewesen sei.

**False Positives:**

- `Bewilligung als Krankenanstalt bzw selbständiges Ambulatorium - tätige GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_27`)


Der Kläger konsumierte die bewilligten Leistungen im September und November 2009 bei der Pharma Glanzsynstein GmbH.

**False Positives:**

- `Der Kläger konsumierte die bewilligten Leistungen im September und November 2009 bei der Pharma Glanzsynstein GmbH` — positional overlap with gold: `Pharma Glanzsynstein GmbH.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Pharma Glanzsynstein GmbH.`(organisation)

**Example 35** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_29`)


Zwischen der GmbH und der beklagten Partei besteht kein Vertragsverhältnis.

**False Positives:**

- `Zwischen der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_30`)


Die GmbH verfügt auch über keine Bewilligung als Krankenanstalt bzw selbständiges Ambulatorium im Sinne des WrKAG und über keinen ärztlichen Leiter.

**False Positives:**

- `Die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_32`)


Anhand dieser Vorgaben werden die von der GmbH entwickelten speziellen Trainingsmethoden angewandt.

**False Positives:**

- `Anhand dieser Vorgaben werden die von der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_38`)


Der Geschäftsführer der GmbH ist diplomierter Sportlehrer.

**False Positives:**

- `Der Geschäftsführer der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_53`)


Ein Kostenersatz sei auch dann nicht möglich, wenn man auf den eigentlichen Leistungserbringer, den Geschäftsführer der GmbH abstelle, der als diplomierter Sportlehrer über keine Berufsberechtigung iSd §§ 3 ff des Bundesgesetzes über die Regelung der gehobenen medizinisch-technischen Dienste (MTD-Gesetz) verfüge.

**False Positives:**

- `Geschäftsführer der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_137`)


Handelt es sich bei den von der GmbH angebotenen Trainings um Leistungen anderer Gesundheitsberufe, die nicht in § 135 Abs 1 ASVG aufgelistet sind, ist eine Analogie ausgeschlossen (siehe oben Pkt 1.1.).

**False Positives:**

- `Handelt es sich bei den von der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_23`)


Auch diesen Aspekt nimmt die Staatsanwaltschaft in der Rechtsrüge (Z 9 lit a) ausreichend in den Blick, indem sie auf - in Richtung der Erfüllung auch der objektiven Tatbestandsmerkmale der §§ 146, 147 Abs 3 StGB weisende - Beweisergebnisse zum vorliegenden Vertragsab-schluss trotz mangelnder finanzieller Ausstattung und Absicherung der Medien Lexsudtal GmbH hinweist.

**False Positives:**

- `Abs 3 StGB weisende - Beweisergebnisse zum vorliegenden Vertragsab-schluss trotz mangelnder finanzieller Ausstattung und Absicherung der Medien Lexsudtal GmbH` — partial — gold is substring of pred: `Medien Lexsudtal GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Medien Lexsudtal GmbH`(organisation)

**Example 42** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__3`)


Kopf Der Oberste Gerichtshof hat am 11. September 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Setz-Hummel in Gegenwart der Richteramtsanwärterin Mag. Leitner als Schriftführerin in der Medienrechtssache des Antragstellers Georgia Bruckmeir gegen die Antragsgegnerin MittelForschung GmbH und eine weitere Antragsgegnerin wegen § 6 Abs 1 und § 8a Abs 6 MedienG, AZ 91 Hv 49/17t des Landesgerichts für Strafsachen Wien, über die von der Generalprokuratur gegen die Urteile des Landesgerichts für Strafsachen Wien vom 26. März 2018 (ON 65 der Hv-Akten) und des Oberlandesgerichts Wien als Berufungsgericht vom 28. November 2018, AZ 17 Bs 153/18a (ON 74 der Hv-Akten), erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Holzleithner, des Vertreters des Antragstellers, Dr. Bauer, und des Vertreters der Antragsgegnerin Analyse Fenheim GmbH, Mag. Bauer, zu Recht erkannt:  Spruch

**False Positives:**

- `Leitner als Schriftführerin in der Medienrechtssache des Antragstellers Georgia Bruckmeir gegen die Antragsgegnerin MittelForschung GmbH` — positional overlap with gold: `Mag. Leitner`
- `Vertreters der Antragsgegnerin Analyse Fenheim GmbH` — partial — gold is substring of pred: `Analyse Fenheim GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Lendl`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Fürnkranz`(person)
- `Dr. Setz-Hummel`(person)
- `Mag. Leitner`(person)
- `Georgia Bruckmeir`(person)
- `MittelForschung GmbH`(organisation)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Mag. Holzleithner`(person)
- `Dr. Bauer`(person)
- `Analyse Fenheim GmbH`(organisation)
- `Mag. Bauer`(person)

**Example 43** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__4`)


In der Medienrechtssache des Antragstellers Univ.-Prof.in Laurin Schramm gegen die Antragsgegnerin CDL Luftfahrt GmbH wegen § 6 Abs 1 und § 8a Abs 6 MedienG, AZ 91 Hv 49/17t des Landesgerichts für Strafsachen Wien, verletzen die Urteile 1./ dieses Gerichts vom 26. März 2018 (ON 65) in seinem Punkt III./, womit der Antrag des Antragstellers, der Antragsgegnerin Drau-IT GmbH auch für die am 4. Juni 2017 auf dem Facebook-Account von www.

**False Positives:**

- `Laurin Schramm gegen die Antragsgegnerin CDL Luftfahrt GmbH` — positional overlap with gold: `Univ.-Prof.in Laurin Schramm`
- `Antragsgegnerin Drau-IT GmbH` — partial — gold is substring of pred: `Drau-IT GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof.in Laurin Schramm`(person)
- `CDL Luftfahrt GmbH`(organisation)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Drau-IT GmbH`(organisation)

**Example 44** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__7`)


Text Gründe: I./ In der Medienrechtssache des Antragstellers StR Anna Barkhausen gegen die Antragsgegnerin Tramoncon KI Consulting GmbH (als Medieninhaberin der Websites www.

**False Positives:**

- `In der Medienrechtssache des Antragstellers StR Anna Barkhausen gegen die Antragsgegnerin Tramoncon KI Consulting GmbH` — partial — gold is substring of pred: `StR Anna Barkhausen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `StR Anna Barkhausen`(person)
- `Tramoncon KI Consulting GmbH`(organisation)

**Example 45** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__10`)


für die dadurch zugefügte Kränkung wurde die Antragsgegnerin Tenholt Holz GmbH nach § 6 Abs 1 MedienG zur Zahlung einer Entschädigung sowie nach § 8a Abs 6 MedienG iVm § 34 Abs 1 MedienG zur Urteilsveröffentlichung verpflichtet.

**False Positives:**

- `Kränkung wurde die Antragsgegnerin Tenholt Holz GmbH` — partial — gold is substring of pred: `Tenholt Holz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tenholt Holz GmbH`(organisation)

**Example 46** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__11`)


Hingegen wurde (ua) der Antrag des Antragstellers, der Antragsgegnerin TraunMarine GmbH für die am selben Tag auf dem Facebook-Account von www.

**False Positives:**

- `Antragsgegnerin TraunMarine GmbH` — partial — gold is substring of pred: `TraunMarine GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `TraunMarine GmbH`(organisation)

**Example 47** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__21`)


Zur Begründung führte das Berufungsgericht – soweit im Folgenden von Relevanz – in ausdrücklicher Abkehr von einer früher vertretenen Rechtsansicht (Urteil des Oberlandesgerichts Wien vom 14. Februar 2018, AZ 17 Bs 212/17a = MR 2018, 7) wie folgt aus (US 32 f): Die Antragsgegnerin Berg-Finanzen Planung GmbH habe auf einer Website (www. Hermani & Grebner Logistik.at) und damit in einem Medium (§ 1 Abs 1 Z 1 MedienG) den Tatbestand der üblen Nachrede hergestellt;

**False Positives:**

- `Die Antragsgegnerin Berg-Finanzen Planung GmbH` — partial — gold is substring of pred: `Berg-Finanzen Planung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgerichts Wien`(organisation)
- `Berg-Finanzen Planung GmbH`(organisation)
- `Hermani & Grebner Logistik.at`(organisation)

**Example 48** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__34`)


Die Haftung des auf eigene Inhalte Verlinkenden als Content-Provider richtet sich daher nach den allgemeinen (straf-)rechtlichen Normen und soweit dieser – wie vorliegend – Medieninhaber ist, nach dem Mediengesetz (Reindl-Krauskopf/Salimi/Stricker, IT-Strafrecht [2018] Rz 3.3, 3.10 und 3.33;Koziol, Haftpflichtrecht II³ A/6/Rz 204;Zankl, E-Commerce-Gesetz, Kommentar2Rz 277), sodass § 17 ECG der geltend gemachten Verantwortlichkeit der Antragsgegnerin Kirmayer Heizung GmbH nach § 6 Abs 1 MedienG nicht entgegensteht.

**False Positives:**

- `ECG der geltend gemachten Verantwortlichkeit der Antragsgegnerin Kirmayer Heizung GmbH` — partial — gold is substring of pred: `Kirmayer Heizung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kirmayer Heizung GmbH`(organisation)

**Example 49** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__40`)


Voraussetzung für die geltend gemachte Haftung der Antragsgegnerin TUEU Garten GmbH nach § 6 Abs 1 MedienG ist, dass im Medium „Website“ (§ 1 Abs 1 Z 5a lit b MedienG) der objektive Tatbestand der üblen Nachrede hergestellt wurde.

**False Positives:**

- `Voraussetzung für die geltend gemachte Haftung der Antragsgegnerin TUEU Garten GmbH` — partial — gold is substring of pred: `TUEU Garten GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `TUEU Garten GmbH`(organisation)

**Example 50** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__60`)


Da sich diese Gesetzesverletzung nicht zum Nachteil der Antragsgegnerin Heimnexfen Planung Entwicklung GmbH, der als Medieninhaberin die Rechte des Angeklagten zukommen (§ 41 Abs 6 zweiter Satz MedienG), auswirkt, kommt ein Vorgehen nach § 292 letzter Satz StPO nicht in Betracht und hat es mit der Feststellung des Gesetzesverstoßes sein Bewenden.

**False Positives:**

- `Da sich diese Gesetzesverletzung nicht zum Nachteil der Antragsgegnerin Heimnexfen Planung Entwicklung GmbH` — partial — gold is substring of pred: `Heimnexfen Planung Entwicklung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Heimnexfen Planung Entwicklung GmbH`(organisation)

**Example 51** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_3`)


Kopf Der Oberste Gerichtshof hat am 11. Dezember 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in Gegenwart des Schriftführers Dr. Koller in der Medienrechtssache der Antragsteller Dr. Ludger Schäpan und Moses Rüßbült gegen die Antragsgegnerin Synzortal-Medien GmbH & Co KG wegen §§ 7 f MedienG, AZ 93 Hv 56/18p des Landesgerichts für Strafsachen Wien, über die von der Generalprokuratur gegen den Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 9. März 2020, AZ 18 Bs 340/19k (ON 27), erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Erste Generalanwältin Mag. Wachberger, der Vertreterin der Antragsteller Dr. Windhager und des Vertreters der Antragsgegnerin Mag. Hermetter, zu Recht erkannt:  Spruch

**False Positives:**

- `Ludger Schäpan und Moses Rüßbült gegen die Antragsgegnerin Synzortal-Medien GmbH` — positional overlap with gold: `Dr. Ludger Schäpan`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Lendl`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Fürnkranz`(person)
- `Dr. Mann`(person)
- `Dr. Koller`(person)
- `Dr. Ludger Schäpan`(person)
- `Moses Rüßbült`(person)
- `Synzortal-Medien GmbH & Co KG`(organisation)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Mag. Wachberger`(person)
- `Dr. Windhager`(person)
- `Mag. Hermetter`(person)

**Example 52** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_4`)


In der Medienrechtssache der Antragsteller Dr. Patrick Schneeweiss und Chen Hölzle gegen die Antragsgegnerin TQGK Versicherung Holding GmbH & Co KG wegen §§ 7 f MedienG, AZ 93 Hv 56/18p, verletzt der Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 9. März 2020, AZ 18 Bs 340/19k (ON 27), § 395 Abs 2 StPO (iVm § 41 Abs 1 MedienG).

**False Positives:**

- `Patrick Schneeweiss und Chen Hölzle gegen die Antragsgegnerin TQGK Versicherung Holding GmbH` — positional overlap with gold: `Dr. Patrick Schneeweiss`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Patrick Schneeweiss`(person)
- `Chen Hölzle`(person)
- `TQGK Versicherung Holding GmbH & Co KG`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 53** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_5`)


Text Gründe: In der Medienrechtssache der Antragsteller Dr. Wieland Skocdopole und Priv.-Doz.in Heidrun Aguera, BA MSc gegen die Antragsgegnerin Wald Fenkraftal GmbH & Co KG wegen §§ 7 f MedienG brachten die Antragsteller beim Landesgericht für Strafsachen Wien gesondert, jeweils in einem eigenen Schriftsatz aber vertreten durch dieselbe Rechtsanwältin selbständige Entschädigungsanträge gegen die Antragsgegnerin ein.

**False Positives:**

- `BA MSc gegen die Antragsgegnerin Wald Fenkraftal GmbH` — positional overlap with gold: `Priv.-Doz.in Heidrun Aguera, BA MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Wieland Skocdopole`(person)
- `Priv.-Doz.in Heidrun Aguera, BA MSc`(person)
- `Wald Fenkraftal GmbH & Co KG`(organisation)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 54** (doc_id: `deanon_260716_TRAIN/15Os9_12f`) (sent_id: `deanon_260716_TRAIN/15Os9_12f_5`)


Dieses Urteil sowie der gemäß § 494a Abs 1 StPO gefasste Beschluss werden aufgehoben und es wird in der Sache selbst zu Recht erkannt: Georg Hamker wird von dem wider ihn erhobenen Vorwurf, er habe in Joseph-Mohr-Straße 15, 5233 Erlach, Österreich mit dem Vorsatz, durch das Verhalten des Getäuschten sich oder einen Dritten unrechtmäßig zu bereichern, Bedienstete der Firma Meyerotto u. Pleuler Handel GmbH durch die Vorgabe, ein zahlungsfähiger und zahlungswilliger Kunde zu sein, zu nachgenannten Handlungen verleitet, die das genannte Unternehmen in einem 3.000 Euro, jedoch nicht 50.000 Euro übersteigenden Betrag am Vermögen schädigten, nämlich 1./ am 9. Juni 2010 zur Lieferung von Kaffee im Wert von 566,02 Euro;

**False Positives:**

- `Pleuler Handel GmbH` — partial — pred is substring of gold: `Meyerotto u. Pleuler Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Georg Hamker`(person)
- `Joseph-Mohr-Straße 15, 5233 Erlach, Österreich`(address)
- `Meyerotto u. Pleuler Handel GmbH`(organisation)

**Example 55** (doc_id: `deanon_260716_TRAIN/15Os9_12f`) (sent_id: `deanon_260716_TRAIN/15Os9_12f_7`)


Text Gründe: Mit dem unangefochten in Rechtskraft erwachsenen Urteil des Landesgerichts Feldkirch vom 4. Oktober 2011, GZ 24 Hv 84/11k-6, wurde Georg Höfs - abweichend von dem in Richtung §§ 146, 147 Abs 2 StGB erhobenen Strafantrag - des Vergehens des Betrugs nach § 146 StGB schuldig erkannt und zu einer teilweise bedingt nachgesehenen Geldstrafe verurteilt. Nach dem Schuldspruch hat er in Chikago 2. Gasse 8, 4613 Hupfau, Österreich mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz Bedienstete der (richtig:) Nobars und Huenecken E‑Commerce GmbH durch die Vorgabe, ein zahlungsfähiger und zahlungswilliger Kunde zu sein, zu Handlungen verleitet, die das genannte Unternehmen in einem 3.000 Euro nicht übersteigenden Betrag am Vermögen schädigten, nämlich 1./ am 9. Juni 2010 zur Lieferung von Kaffee im Wert von 566,02 Euro;

**False Positives:**

- `Commerce GmbH` — partial — pred is substring of gold: `Nobars und Huenecken E‑Commerce GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Feldkirch`(organisation)
- `Georg Höfs`(person)
- `Chikago 2. Gasse 8, 4613 Hupfau, Österreich`(address)
- `Nobars und Huenecken E‑Commerce GmbH`(organisation)

**Example 56** (doc_id: `deanon_260716_TRAIN/15Os9_12f`) (sent_id: `deanon_260716_TRAIN/15Os9_12f_9`)


Den weiters mit Strafantrag vom 1. September 2011 (ON 3) erhobenen Vorwurf, der Angeklagte habe am 8. Juli 2010 die Verfügungsberechtigten der Nexlexlog Holding GmbH auch zur leihweisen Überlassung einer Kaffeemaschine im Wert von 390 Euro und eines sogenannten Schokodispensers Exquisit im Wert von 1.328 Euro veranlasst, erachtete das Erstgericht für nicht erweislich.

**False Positives:**

- `Juli 2010 die Verfügungsberechtigten der Nexlexlog Holding GmbH` — partial — gold is substring of pred: `Nexlexlog Holding GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nexlexlog Holding GmbH`(organisation)

**Example 57** (doc_id: `deanon_260716_TRAIN/18OCg12_19t`) (sent_id: `deanon_260716_TRAIN/18OCg12_19t_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Veith und die Hofräte Dr. Höllwerth, Priv.-Doz. Dr. Rassi und Mag. Painsi als weitere Richter in der Schiedsrechtssache der klagenden Partei Energie Glanzgart GmbH, Waldelweg 28, 4201 Maierleiten, Österreich, vertreten durch die SRG Stock Rafaseder Gruszkiewicz Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Piedro Arnoult, Bulgarien, wegen Aufhebung eines Schiedsspruchs (Streitwert 257.397,45 EUR), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Klage wird als nicht zur Bestimmung einer Tagsatzung zur mündlichen Verhandlung geeignet zurückgewiesen.

**False Positives:**

- `Painsi als weitere Richter in der Schiedsrechtssache der klagenden Partei Energie Glanzgart GmbH` — positional overlap with gold: `Mag. Painsi`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Veith`(person)
- `Dr. Höllwerth`(person)
- `Priv.-Doz. Dr. Rassi`(person)
- `Mag. Painsi`(person)
- `Energie Glanzgart GmbH`(organisation)
- `Waldelweg 28, 4201 Maierleiten, Österreich`(address)
- `SRG Stock Rafaseder Gruszkiewicz Rechtsanwälte GmbH`(organisation)
- `Piedro Arnoult`(person)

**Example 58** (doc_id: `deanon_260716_TRAIN/1Nc1_15k`) (sent_id: `deanon_260716_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Große-Schulte & Seufer E‑Commerce GmbH, Untererb 31, 3033 Altlengbach, Österreich, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Wilbachkel Luftfahrt GmbH, Andrä Idl-Straße 79, 4791 Haselbach, Österreich, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

**False Positives:**

- `Commerce GmbH` — partial — pred is substring of gold: `Große-Schulte & Seufer E‑Commerce GmbH`
- `Partei Wilbachkel Luftfahrt GmbH` — partial — gold is substring of pred: `Wilbachkel Luftfahrt GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Landesgericht Wiener Neustadt`(organisation)
- `Große-Schulte & Seufer E‑Commerce GmbH`(organisation)
- `Untererb 31, 3033 Altlengbach, Österreich`(address)
- `Dr. Andreas Oberbichler`(person)
- `Dr. Michael Kramer`(person)
- `Wilbachkel Luftfahrt GmbH`(organisation)
- `Andrä Idl-Straße 79, 4791 Haselbach, Österreich`(address)
- `Mag. Maximilian Kocher`(person)
- `Landesgericht Feldkirch`(organisation)

**Example 59** (doc_id: `deanon_260716_TRAIN/1Ob139_18z`) (sent_id: `deanon_260716_TRAIN/1Ob139_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Verena Tappendorff Inc., Sankt Andrä im Sausal 24, 8552 Aichberg, Österreich, vertreten durch Mag. Ralph Kilches, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Sabine Martinsson, als Insolvenzverwalter im Insolvenzverfahren über das Vermögen der Touristik Synberbruck GmbH, Fridau 56l, 7433 Bergwerk, Österreich, vertreten durch die Haslinger/Nagele & Partner Rechtsanwälte GmbH, Linz, wegen Feststellung einer Insolvenzforderung (Streitwert 447.352,05 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 28. Juni 2018, GZ 1 R 83/18h-8, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Insolvenzverwalter im Insolvenzverfahren über das Vermögen der Touristik Synberbruck GmbH` — partial — gold is substring of pred: `Touristik Synberbruck GmbH`
- `Nagele & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Haslinger/Nagele & Partner Rechtsanwälte GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Parzmayr`(person)
- `Verena Tappendorff`(person)
- `Sankt Andrä im Sausal 24, 8552 Aichberg, Österreich`(address)
- `Mag. Ralph Kilches`(person)
- `Mag. Sabine Martinsson`(person)
- `Touristik Synberbruck GmbH`(organisation)
- `Fridau 56l, 7433 Bergwerk, Österreich`(address)
- `Haslinger/Nagele & Partner Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Linz`(organisation)

**Example 60** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Dr. Florenzia Münsterer, vertreten durch Rechtsanwälte Dr. Amhof & Dr. Damian GmbH in Wien, gegen die beklagte Partei MittelEnergie Werke Bank AG, Altlassing 110, 4183 Ahorn, Österreich, vertreten durch Urbanek Lind Schmied Reisch Rechtsanwälte OG in Wien, wegen 600.090 EUR sA, über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 25. Mai 2011, GZ 15 R 64/11h-54, mit dem das Urteil des Handelsgerichts Wien vom 14. Jänner 2011, GZ 16 Cg 20/10f-50, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Damian GmbH` — partial — pred is substring of gold: `Rechtsanwälte Dr. Amhof & Dr. Damian GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Dr. Grohmann`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Florenzia Münsterer`(person)
- `Rechtsanwälte Dr. Amhof & Dr. Damian GmbH`(organisation)
- `MittelEnergie Werke Bank`(organisation)
- `Altlassing 110, 4183 Ahorn, Österreich`(address)
- `Urbanek Lind Schmied Reisch Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 61** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_5`)


Text Begründung: Eine GmbH, deren Mehrheitsgesellschafter und Geschäftsführer ein Cousin des Klägers war, beabsichtigte, bei der beklagten Bank einen Kredit aufzunehmen, dessen Gewährung allerdings von der Bestellung einer Sicherheit abhängig gemacht wurde, zumal damals nur ungefähr die Hälfte des Gesamtobligos der GmbH bei der Beklagten von rund 6,6 Mio EUR besichert war.

**False Positives:**

- `Eine GmbH` — no gold match — likely missing annotation
- `Hälfte des Gesamtobligos der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 62** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_14`)


Die Beklagte gewährte daraufhin der GmbH den gewünschten Überbrückungskredit.

**False Positives:**

- `Die Beklagte gewährte daraufhin der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_15`)


Nachdem über das Vermögen der GmbH am 25.

**False Positives:**

- `Nachdem über das Vermögen der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_19`)


Von der wirtschaftlich schlechten Situation der GmbH hatte der Kläger erstmals wenige Tage vor der Konkurseröffnung erfahren.

**False Positives:**

- `Von der wirtschaftlich schlechten Situation der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_21`)


Die Beklagte sei schon ab Jänner 2005 aufgrund einer erfolgten Umschuldung vollständig über die ungünstige wirtschaftliche Situation der GmbH informiert gewesen und habe daher gewusst oder hätte zumindest wissen müssen, dass diese voraussichtlich nicht in der Lage sein werde, den Kredit zu tilgen.

**False Positives:**

- `Die Beklagte sei schon ab Jänner 2005 aufgrund einer erfolgten Umschuldung vollständig über die ungünstige wirtschaftliche Situation der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_22`)


Spätestens Ende September 2007 und damit vor der Interzession des Klägers sei die GmbH überschuldet gewesen.

**False Positives:**

- `Spätestens Ende September 2007 und damit vor der Interzession des Klägers sei die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_23`)


Die Beklagte habe ihre vorvertraglichen Aufklärungs-, Schutz- und Sorgfaltspflichten verletzt, indem sie den Kläger, der keine Zweifel an der Rückführung des Kredits durch die GmbH gehabt habe, davon nicht informiert habe;

**False Positives:**

- `Zweifel an der Rückführung des Kredits durch die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_32`)


Dieser sei sich auch der wirtschaftlichen Lage der GmbH voll bewusst gewesen.

**False Positives:**

- `Dieser sei sich auch der wirtschaftlichen Lage der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_39`)


Die vom Kläger zu stellende Sicherheit sei für alle Beteiligten erkennbar stets dergestalt mit der Kreditierung der Beklagten an die GmbH verbunden gewesen, dass ohne Sicherheit der Kredit nicht eingeräumt und ohne Kreditierung die Sicherheit nicht erforderlich würde.

**False Positives:**

- `Die vom Kläger zu stellende Sicherheit sei für alle Beteiligten erkennbar stets dergestalt mit der Kreditierung der Beklagten an die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_40`)


Da der Beklagten festgestelltermaßen bewusst gewesen sei, dass die Garantie letztlich zu Lasten des Klägers gehen würde, sei die hier gelegte Bankgarantie nicht als selbständiger, von jedem anderen Schuldverhältnis unabhängiger, einseitig verpflichtender Schuldvertrag anzusehen, sondern als eine zum Kredit an die GmbH akzessorische Verpflichtung des Klägers.

**False Positives:**

- `Kredit an die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_46`)


Den in dieser Bestimmung angeführten Varianten der Interzession sei gemeinsam, dass der Interzedent jeweils in eine unmittelbare vertragliche Beziehung zum Gläubiger tritt, was auch hier der Fall sei, sei der Bestellung der Bankgarantie durch den Kläger doch eine mündliche Vereinbarung mit der Beklagten vorangegangen, die für die weitere Kreditgewährung an die GmbH Sicherheiten gewollt habe.

**False Positives:**

- `Kreditgewährung an die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_59`)


Nach den maßgeblichen Tatsachenfeststellungen der Vorinstanzen hat sich der Kläger über Aufforderung der Beklagten schließlich bereit erklärt, zur Besicherung der Kreditforderungen der Beklagten gegen eine GmbH auf eigene Rechnung dafür zu sorgen, dass seine Hausbank eine Garantieerklärung (Bankgarantie) abgibt, und ein entsprechender Garantiebrief der Beklagten übermittelt wird.

**False Positives:**

- `Besicherung der Kreditforderungen der Beklagten gegen eine GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_63`)


Dies korrespondiert auch mit seinem eigenen erstinstanzlichen Vorbringen, wonach seine Hausbank die Bankgarantie zur Sicherung der Ansprüche der Beklagten gegen die GmbH ausstellen wollte und auch ausgestellt hat, nicht aber etwa zur Sicherung allfälliger Ansprüche der Beklagten gegen den Kläger aufgrund einer von ihm abgegebenen Interzessionserklärung.

**False Positives:**

- `Hausbank die Bankgarantie zur Sicherung der Ansprüche der Beklagten gegen die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_76`)


Er habe, nachdem seine Haftung aus der Interzession nach dem Konkurs der GmbH festgestanden sei, keine Erfüllungs- oder sonstige Handlung zugunsten der Beklagten gesetzt.

**False Positives:**

- `Haftung aus der Interzession nach dem Konkurs der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_81`)


Geht man davon aus, dass die bloß mündlich abgegebene Zusage, der Kläger werde zur Besicherung der Verbindlichkeiten der GmbH eine Bankgarantie beibringen, in sinngemäßer Anwendung des § 1346 Abs 2 ABGB mangels Schriftlichkeit formunwirksam war, war er vorerst nicht verpflichtet, die in dieser unwirksamen Vereinbarung versprochene Leistung, nämlich die Verschaffung einer Bankgarantie, zu erbringen.

**False Positives:**

- `Kläger werde zur Besicherung der Verbindlichkeiten der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_260716_TRAIN/1Ob178_19m`) (sent_id: `deanon_260716_TRAIN/1Ob178_19m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Hilde Dammrow, vertreten durch die Korn und Gärtner Rechtsanwälte OG, Salzburg, gegen die beklagte Partei Evelyn Allmutter, vertreten durch die Ferner Hornung & Partner Rechtsanwälte GmbH, Salzburg, wegen Wiederaufnahme des Verfahrens AZ 17 C 1538/16p des Bezirksgerichts Salzburg, über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 12. Juni 2019, GZ 22 R 163/19b-7, mit dem der Beschluss des Bezirksgerichts Salzburg vom 25. Jänner 2019, GZ 17 C 80/19f-2, mit einer Maßgabe bestätigt wurde, den Beschluss gefasst:  Spruch Dem außerordentlichen Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Ferner Hornung & Partner Rechtsanwälte GmbH` — partial — gold is substring of pred: `Hornung & Partner Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Parzmayr`(person)
- `Hilde Dammrow`(person)
- `Evelyn Allmutter`(person)
- `Hornung & Partner Rechtsanwälte GmbH`(organisation)
- `Bezirksgerichts Salzburg`(organisation)
- `Landesgerichts Salzburg`(organisation)
- `Bezirksgerichts Salzburg`(organisation)

**Example 77** (doc_id: `deanon_260716_TRAIN/1Ob182_17x`) (sent_id: `deanon_260716_TRAIN/1Ob182_17x_25`)


Nach dem von den Vorinstanzen zugrunde gelegten Sachverhalt beabsichtigt der Antragsgegner einer zur Unternehmensgruppe der Familie gehörenden GmbH, an der er nur mehr einen Geschäftsanteil von 1 % hält, der aber mit weitreichenden Sonderrechten ausgestattet ist, und die einen dringenden Finanzierungsbedarf in Höhe von 3 Mio EUR hat, ein Privatdarlehen in dieser Höhe zu gewähren, dass er wiederum durch Aufnahme eines entsprechenden Bankkredits finanzieren will, von dem bereits 1 Mio EUR an den Antragsgegner und von diesem an die GmbH geflossen sind.

**False Positives:**

- `Nach dem von den Vorinstanzen zugrunde gelegten Sachverhalt beabsichtigt der Antragsgegner einer zur Unternehmensgruppe der Familie gehörenden GmbH` — no gold match — likely missing annotation
- `Mio EUR an den Antragsgegner und von diesem an die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 78** (doc_id: `deanon_260716_TRAIN/1Ob182_17x`) (sent_id: `deanon_260716_TRAIN/1Ob182_17x_33`)


Jedenfalls als Teile der Aufteilungsmasse vorhanden sind derzeit eine im gemeinsamen Eigentum (je 50 %) stehende Liegenschaft mit der früheren Ehewohnung in Hinterriß-Tortal 17, 9334 Deinsberg, Österreich, eine im gemeinsamen Eigentum der Streitteile stehende Eigentumswohnung in Fächerturmgasse 35, 2392 Sulz im Wienerwald, Österreich, ein im gemeinsamen Eigentum stehendes Baugrundstück in Schildorf 4, 9560 Naßweg, Österreich, eine Eigentumswohnung des Antragsgegners in Constantin Greco ( Schlatzendorf 6m, 3250 Laimstetten, Österreich gasse), Gesellschaftsanteile (je 10 %) des Antragsgegners an zwei Kommanditgesellschaften (Verlustbeteiligungen) sowie eine Forderung des Antragsgegners gegen eine GmbH, deren Alleingesellschafter er ist, in Höhe von 341.500 EUR.

**False Positives:**

- `Forderung des Antragsgegners gegen eine GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hinterriß-Tortal 17, 9334 Deinsberg, Österreich`(address)
- `Fächerturmgasse 35, 2392 Sulz im Wienerwald, Österreich`(address)
- `Schildorf 4, 9560 Naßweg, Österreich`(address)
- `Constantin Greco`(person)
- `Schlatzendorf 6m, 3250 Laimstetten, Österreich`(address)

**Example 79** (doc_id: `deanon_260716_TRAIN/1Ob216_15v`) (sent_id: `deanon_260716_TRAIN/1Ob216_15v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Suleika Kranigk, vertreten durch Hon.-Prof. Dr. Michel Walter, Rechtsanwalt in Wien, gegen die beklagte Partei Kelfen Transport Solutions GmbH, Geßlgasse 35, 9911 Thal-Wilfern, Österreich, vertreten durch die Schlösser & Partner Rechtsanwälte OG, Graz, wegen 33.930 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 19. August 2015, GZ 13 R 74/15w-55, mit dem das Endurteil des Landesgerichts Korneuburg vom 26. Februar 2015, GZ 3 Cg 15/13h-50, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Kelfen Transport Solutions GmbH` — partial — gold is substring of pred: `Kelfen Transport Solutions GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Suleika Kranigk`(person)
- `Hon.-Prof. Dr. Michel Walter`(person)
- `Kelfen Transport Solutions GmbH`(organisation)
- `Geßlgasse 35, 9911 Thal-Wilfern, Österreich`(address)
- `Partner Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Korneuburg`(organisation)

**Example 80** (doc_id: `deanon_260716_TRAIN/1Ob224_20b`) (sent_id: `deanon_260716_TRAIN/1Ob224_20b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache klagenden Partei Rainer Baetzel, vertreten durch Dr. Harald Hauer, Rechtsanwalt in Wien, gegen die beklagte Partei Rimscha Versand GmbH in Liquidation, Götzau 193, 5452 Grub, Österreich, vertreten durch die Petsch Frosch Klein Arturo Rechtsanwälte OG, Wien, wegen 38.236,58 EUR sA und Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Oktober 2020, GZ 3 R 51/20x-50, mit dem das Urteil des Handelsgerichts Wien vom 24. Juli 2020, GZ 34 Cg 51/18h-45, bestätigt wurde, in nicht öffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Rimscha Versand GmbH` — partial — gold is substring of pred: `Rimscha Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Parzmayr`(person)
- `Rainer Baetzel`(person)
- `Dr. Harald Hauer`(person)
- `Rimscha Versand GmbH`(organisation)
- `Götzau 193, 5452 Grub, Österreich`(address)
- `Petsch Frosch Klein Arturo Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 81** (doc_id: `deanon_260716_TRAIN/1Ob226_20x`) (sent_id: `deanon_260716_TRAIN/1Ob226_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Pia Geermann GmbH, Orise 28, 9135 Unterort, Österreich, vertreten durch Dr. Martin Leitner und andere, Rechtsanwälte in Wien, gegen die beklagte Partei Stadt Li Wachmeister, vertreten durch die Estermann Pock Rechtsanwälte GmbH, Wien, wegen 19.002,01 EUR, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 7. September 2020, GZ 14 R 61/20y-27, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 28. Jänner 2020, GZ 31 Cg 1/19y-22, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Pia Geermann GmbH` — positional overlap with gold: `Dr. Parzmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Parzmayr`(person)
- `Pia Geermann`(person)
- `Orise 28, 9135 Unterort, Österreich`(address)
- `Dr. Martin Leitner`(person)
- `Li Wachmeister`(person)
- `Estermann Pock Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

</details>

---

## `AG Company Names` 🏆

**F1:** 0.009 | **Precision:** 0.205 | **Recall:** 0.004  

**Format:** `regex`  
**Rule ID:** `3b75292d`  
**Description:**
Matches company names ending in 'AG' with a preceding proper noun or alphanumeric prefix, allowing hyphens, plus signs, and multi-word names.

**Content:**
```
\b([A-Z][A-Za-z\u00e4\u00f6\u00fc\u00df\+\-]+(?:\s+[A-Z][A-Za-z\u00e4\u00f6\u00fc\u00df\+\-]+)*\s+AG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.205 | 0.004 | 0.009 | 88 | 18 | 70 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 18 | 70 | 3625 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/1Ob12_21b`) (sent_id: `deanon_260716_TRAIN/1Ob12_21b_34`)


Der von den Beklagten erhobene (und mit dem Fehlen der Passivlegitimation verbundene) Einwand, es sei auch das Ersitzungsverbot öffentlichen Wasserguts (oder eine Ersitzung gegenüber der Österreichische Bundesforste AG bzw deren Rechtsvorgänger) zu prüfen, scheitert schon daran.

| Predicted | Gold |
|---|---|
| `Bundesforste AG` | `Bundesforste AG` |

**Example 1** (doc_id: `deanon_260716_TRAIN/1Ob159_20v`) (sent_id: `deanon_260716_TRAIN/1Ob159_20v_4`)


Wien Derconlex AG, Dr. Theodor-Körner-Gasse 34, 9601 Pöckau, Österreich, vertreten durch Mag. Klemens Mayer, Mag. Stefan Herrmann Rechtsanwälte in Wien, wegen 410.325,23 EUR sA, über die außerordentliche Revision der klagenden Partei, gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Mai 2020, GZ 30 R 106/20h-73, mit dem das Urteil des Handelsgerichts Wien vom 15. Jänner 2020, GZ 10 Cg 15/16k-69, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Wien Derconlex AG` | `Wien Derconlex AG` |

**Missed by this rule (FN):**

- `Dr. Theodor-Körner-Gasse 34, 9601 Pöckau, Österreich` (address)
- `Mag. Klemens Mayer` (person)
- `Mag. Stefan Herrmann` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/23Os1_15t`) (sent_id: `deanon_260716_TRAIN/23Os1_15t_6`)


Text Gründe: Mit dem angefochtenen Erkenntnis wurde Dr. Xaver Springinsgut, Rechtsanwalt in St.Oswald - Rosennockstraße 31, 2051 Platt, Österreich, wegen des Verstoßes gegen die Bestimmungen des § 9 (Abs 1) RAO und des § 2 RL-BA der Disziplinarvergehen der Verletzung von Berufspflichten und der Beeinträchtigung von Ehre oder (richtig:) Ansehen des Standes nach § 1 Abs 1 erster und zweiter Fall DSt schuldig erkannt, weil er als Rechtsvertreter der Ehegatten Roman und Elfriede Jähnel in Anträgen auf Aufschiebung der Zwangsversteigerungen für seine Mandanten vom 5. September 2013 in näher bezeichneten Verfahren des Bezirksgerichts Innsbruck und des Bezirksgerichts Amstetten sowie in einer näher genannten Feststellungsklage an das Landesgericht Linz vom 7. Oktober 2013 und in einer Impugnationsklage an das Bezirksgericht Amstetten vom 10. Oktober 2013 jeweils vorgebracht hatte, seine Mandanten hätten sämtliche Verpflichtungen aus einer mit der Alpen Nexlex AG abgeschlossenen Vereinbarung vom 11. Dezember 2012, insbesondere jene zur unwiderruflichen Antragstellung auf Aufhebung der Höfeeigenschaft einer näher bezeichnenden Liegenschaft in Schulgartenweg 18, 9872 Grantsch, Österreich, eingehalten, obwohl ihm zum Zeitpunkt der Antragstellung und Klagseinbringung bekannt war, dass der Antrag auf Aufhebung der Höfeeigenschaft vom 13. Dezember 2012 bereits am 14. Juni 2013 von Roman Jiran, durch ihn vertreten, entgegen der zuvor genannten Vereinbarung vom 11. Dezember 2012 wieder zurückgezogen worden war.

| Predicted | Gold |
|---|---|
| `Alpen Nexlex AG` | `Alpen Nexlex AG` |

**Missed by this rule (FN):**

- `Dr. Xaver Springinsgut` (person)
- `St.Oswald - Rosennockstraße 31, 2051 Platt, Österreich` (address)
- `Elfriede Jähnel` (person)
- `Bezirksgerichts Innsbruck` (organisation)
- `Bezirksgerichts Amstetten` (organisation)
- `Landesgericht Linz` (organisation)
- `Bezirksgericht Amstetten` (organisation)
- `Schulgartenweg 18, 9872 Grantsch, Österreich` (address)
- `Roman Jiran` (person)

**Example 3** (doc_id: `deanon_260716_TRAIN/23Os1_15t`) (sent_id: `deanon_260716_TRAIN/23Os1_15t_7`)


Der Disziplinarbeschuldigte wurde hiefür nach § 16 Abs 1 Z 2 DSt zu einer Geldbuße von 3.500 Euro verurteilt.  Rechtliche Beurteilung Der vom Disziplinarbeschuldigten dagegen wegen Nichtigkeit (§ 281 Abs 1 Z 1, 4, 9 lit a und b StPO), Schuld und Strafe erhobenen Berufung kommt Berechtigung zu. Die Besetzungsrüge (Z 1) zeigt zwar keine Tatsachengrundlage für die reklamierte Ausgeschlossenheit des Vorsitzenden des Disziplinarrats wegen Befangenheit (§ 43 Abs 1 Z 3 StPO iVm § 77 Abs 3 DSt) auf, weil aufgrund der Mitteilung des Genannten vom 5. Dezember 2014, wonach er keine Veranlassung sehe, seine „rechtsgeschäftlichen Kontakte“ dem Disziplinarbeschuldigten gegenüber offenzulegen, entgegen dem rein spekulativen Berufungsstandpunkt nicht „anzunehmen ist, dass ein berufsbedingtes Naheverhältnis“ des Vorsitzenden des Disziplinarrats zur WDL Sanitär AG (Prozessgegnerin der vom Disziplinarbeschuldigten vertretenen Mandanten)“ besteht (vgl RIS-Justiz RS0125768, RS0097054).

| Predicted | Gold |
|---|---|
| `WDL Sanitär AG` | `WDL Sanitär AG` |

**Example 4** (doc_id: `deanon_260716_TRAIN/23Os1_15t`) (sent_id: `deanon_260716_TRAIN/23Os1_15t_10`)


Unkenntnis des Disziplinarbeschuldigten von den Gründen der Griete+Leine Technik AG für die beantragte Fortsetzung der Zwangsversteigerungsverfahren;

| Predicted | Gold |
|---|---|
| `Griete+Leine Technik AG` | `Griete+Leine Technik AG` |

**Example 5** (doc_id: `deanon_260716_TRAIN/2Nc25_11s`) (sent_id: `deanon_260716_TRAIN/2Nc25_11s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Laurence Voelkers, Bakk. techn., vertreten durch Dr. Thomas Praxmarer, Rechtsanwalt in Innsbruck, gegen die beklagten Parteien 1) HR Birgit Krolitzki, und 2) DonauBau Versicherungs AG Am Schierlinggrund 4, 8490 Hummersdorf, Österreich, beide vertreten durch Dr. Heribert Schar, Dr. Bernhard Schmidhammer, Rechtsanwälte in Innsbruck, wegen 21.664,61 EUR und Feststellung den Beschluss gefasst:  Spruch Es wird die Befangenheit sämtlicher Richterinnen und Richter des Oberlandesgerichts Innsbruck festgestellt. Zur (Verhandlung und) Entscheidung als Berufungsgericht im Verfahren 41 Cg 23/10s des Landesgerichts Innsbruck wird das Oberlandesgericht Linz als zuständig bestimmt (§ 30 JN).

| Predicted | Gold |
|---|---|
| `DonauBau Versicherungs AG` | `DonauBau Versicherungs AG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Baumann` (person)
- `Dr. Veith` (person)
- `Dr. E. Solé` (person)
- `Dr. Schwarzenbacher` (person)
- `Dr. Nowotny` (person)
- `Laurence Voelkers, Bakk. techn.` (person)
- `Dr. Thomas Praxmarer` (person)
- `HR Birgit Krolitzki` (person)
- `Am Schierlinggrund 4, 8490 Hummersdorf, Österreich` (address)
- `Dr. Heribert Schar` (person)
- `Dr. Bernhard Schmidhammer` (person)
- `Oberlandesgerichts Innsbruck` (organisation)
- `Landesgerichts Innsbruck` (organisation)
- `Oberlandesgericht Linz` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/2Ob115_10s`) (sent_id: `deanon_260716_TRAIN/2Ob115_10s_4`)


Uniber-Verlag AG, Jedretsberg 24, 4190 Brunnwald, Österreich, und 2. Fenuni AG, Wildschönauerstraße, Oberau 3, 8444 Reith, Österreich, beide vertreten durch die Liebenwein Rechtsanwälte GmbH in Wien, gegen die beklagten und widerklagenden Parteien 1.

| Predicted | Gold |
|---|---|
| `Uniber-Verlag AG` | `Uniber-Verlag AG` |
| `Fenuni AG` | `Fenuni AG` |

**Missed by this rule (FN):**

- `Jedretsberg 24, 4190 Brunnwald, Österreich` (address)
- `Wildschönauerstraße, Oberau 3, 8444 Reith, Österreich` (address)
- `Liebenwein Rechtsanwälte GmbH` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/2Ob85_11f`) (sent_id: `deanon_260716_TRAIN/2Ob85_11f_4`)


Guntram Wellenbring, vertreten durch Dr. Peter Sparer, Rechtsanwalt in Innsbruck, 2. Verbruckal AG, Stäpfle 16, 1020 Wien, Österreich, vertreten durch Dr. Harald Burmann und andere Rechtsanwälte in Innsbruck, und 3.

| Predicted | Gold |
|---|---|
| `Verbruckal AG` | `Verbruckal AG` |

**Missed by this rule (FN):**

- `Guntram Wellenbring` (person)
- `Dr. Peter` (person)
- `Stäpfle 16, 1020 Wien, Österreich` (address)
- `Dr. Harald Burmann` (person)

**Example 8** (doc_id: `deanon_260716_TRAIN/2Ob85_11f`) (sent_id: `deanon_260716_TRAIN/2Ob85_11f_5`)


See-Umwelt Manufaktur AG, Zosen 244, 9543 Sauboden, Österreich, vertreten durch Dr. Walter Heel, Rechtsanwalt in Innsbruck, wegen 62.404,99 EUR sA und Feststellung (Streitinteresse: 10.000 EUR), über die Revisionen der klagenden, der erstbeklagten und der zweitbeklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Jänner 2011, GZ 4 R 250/10m-85, womit infolge der Berufungen der klagenden, der erstbeklagten und der zweitbeklagten Partei das Urteil des Landesgerichts Innsbruck vom 25. August 2010, GZ 5 Cg 160/08w-74, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Sämtliche Revisionen werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `See-Umwelt Manufaktur AG` | `See-Umwelt Manufaktur AG` |

**Missed by this rule (FN):**

- `Zosen 244, 9543 Sauboden, Österreich` (address)
- `Dr. Walter Heel` (person)
- `Oberlandesgerichts Innsbruck` (organisation)
- `Landesgerichts Innsbruck` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/4Nc4_17a`) (sent_id: `deanon_260716_TRAIN/4Nc4_17a_5`)


Sanitär Norfurtwerk AG, Piburger Straße 20, 4204 Hadersdorf, Österreich, Deutschland, beide vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Gesamtstreitwert 69.500 EUR), über den Ordinationsantrag der Klägerinnen den Beschluss gefasst:  Spruch Dem Ordinationsantrag wird stattgegeben.

| Predicted | Gold |
|---|---|
| `Sanitär Norfurtwerk AG` | `Sanitär Norfurtwerk AG` |

**Missed by this rule (FN):**

- `Piburger Straße 20, 4204 Hadersdorf, Österreich` (address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH` (organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/4Ob9_20g`) (sent_id: `deanon_260716_TRAIN/4Ob9_20g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Vogel als Vorsitzenden und die Hofräte Dr. Schwarzenbacher, Hon.-Prof. Dr. Brenn, Priv.-Doz. Dr. Rassi und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Ingrid Marke, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1) ZTYW Solar Vertrieb GmbH, Hans-Woerle-Weg 13, 4852 Gahberg, Österreich, und 2) Hoch Fenfurtmon Systeme AG, Raxer Straße 24, 8952 Kienach, Österreich, beide vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 11.091,23 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 6. November 2019, GZ 2 R 158/19x-27, mit dem das Urteil des Landesgerichts Linz vom 29. August 2019, GZ 36 Cg 14/18h-22, bestätigt wurde, den Beschluss gefasst:  Spruch I. Das Revisionsverfahren zu 4 Ob 9/20g wird bis zur Vorabentscheidung des Gerichtshofs der Europäischen Union über das Vorabentscheidungsersuchen des Obersten Gerichtshofs vom 17.

| Predicted | Gold |
|---|---|
| `Hoch Fenfurtmon Systeme AG` | `Hoch Fenfurtmon Systeme AG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Vogel` (person)
- `Dr. Schwarzenbacher` (person)
- `Hon.-Prof. Dr. Brenn` (person)
- `Priv.-Doz. Dr. Rassi` (person)
- `MMag. Matzka` (person)
- `Ingrid Marke` (person)
- `Poduschka Anwaltsgesellschaft mbH` (organisation)
- `ZTYW Solar Vertrieb GmbH` (organisation)
- `Hans-Woerle-Weg 13, 4852 Gahberg, Österreich` (address)
- `Raxer Straße 24, 8952 Kienach, Österreich` (address)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Linz` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/5Ob141_23f`) (sent_id: `deanon_260716_TRAIN/5Ob141_23f_17`)


Ende des Jahres 2018 schloss er sich der deutschen Musterfeststellungsklage gegen die ONTJ Textil AG an.

| Predicted | Gold |
|---|---|
| `ONTJ Textil AG` | `ONTJ Textil AG` |

**Example 12** (doc_id: `deanon_260716_TRAIN/7Ob85_15y`) (sent_id: `deanon_260716_TRAIN/7Ob85_15y_5`)


Wiebel Möbel AG und 3. Hedicke+Janischewsky Heizung GmbH, beide Rev.

| Predicted | Gold |
|---|---|
| `Wiebel Möbel AG` | `Wiebel Möbel AG` |

**Missed by this rule (FN):**

- `Hedicke+Janischewsky Heizung GmbH` (organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/8Ob39_24d`) (sent_id: `deanon_260716_TRAIN/8Ob39_24d_6`)


Er brachte vor, über seine depotführende Bank in Graz mehrfach Aktien der Krautsch Analyse AG mit Sitz in Deutschland gekauft zu haben (und zwar, wie aus den von ihm vorgelegten Beilagen ersichtlich, „loco Düsseldorf“).

| Predicted | Gold |
|---|---|
| `Krautsch Analyse AG` | `Krautsch Analyse AG` |

**Example 14** (doc_id: `deanon_260716_TRAIN/8Ob39_24d`) (sent_id: `deanon_260716_TRAIN/8Ob39_24d_7`)


Er wirft der Beklagten vor, ihre Pflichten als Wirtschaftsprüferin der SüdChemie AG verletzt zu haben.

| Predicted | Gold |
|---|---|
| `SüdChemie AG` | `SüdChemie AG` |

**Example 15** (doc_id: `deanon_260716_TRAIN/8Ob39_24d`) (sent_id: `deanon_260716_TRAIN/8Ob39_24d_8`)


Hätte sie pflichtgemäß gehandelt und den von ihr geprüften Jahresabschlüssen den Bestätigungsvermerk versagt, hätte er die Aktien nicht gekauft und damit – wegen der kurz nach seinen Käufen von der EnnsMaschinenbau AG beantragten Insolvenzeröffnung – keinen Schaden erlitten.

| Predicted | Gold |
|---|---|
| `EnnsMaschinenbau AG` | `EnnsMaschinenbau AG` |

**Example 16** (doc_id: `deanon_260716_TRAIN/9Ob68_22y`) (sent_id: `deanon_260716_TRAIN/9Ob68_22y_108`)


Bei der gebotenen objektiven Betrachtung läge in der Mitwirkung der VW AG an der Verbesserung der Beklagten grundsätzlich noch kein ausreichender Grund für die Unzumutbarkeit des primären Gewährleistungsbehelfs, allerdings habe der Kläger auch negative Auswirkungen des für seinen Fahrzeugtyp entwickelten Software-Updates behauptet.

| Predicted | Gold |
|---|---|
| `VW AG` | `VW AG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Partei Langhansl+Antonewitz Chemie AG` — partial — gold is substring of pred: `Langhansl+Antonewitz Chemie AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Mag. Korn`(person)
- `Langhansl+Antonewitz Chemie AG`(organisation)
- `Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich`(address)
- `Poinstingl & Partner Rechtsanwälte OG`(organisation)
- `Drau-Pharma GmbH`(organisation)
- `Strazzegasse 12, 8762 Oberzeiring, Österreich`(address)
- `Mag. Johannes Bügler`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Wiener Neustadt`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a__16`)


Mit Urteil desselben Tages erkannte das Gericht den Angeklagten „im Sinne der Anklageschrift“ des Verbrechens des gewerbsmäßig und als Mitglied einer kriminellen Vereinigung durch Einbruch begangenen schweren Diebstahls nach §§ 127, 128 Abs 2, 129 Abs 1 Z 1, 130 Abs 1 erster und zweiter Fall, Abs 2 erster und zweiter Fall und 15 StGB sowie mehrerer Vergehen der Urkundenunterdrückung nach § 229 Abs 1 StGB schuldig, verhängte über ihn eine Freiheitsstrafe und verpflichtete ihn, an die Privatbeteiligte St Donau Triheim AG einen Geldbetrag zu bezahlen.

**False Positives:**

- `Privatbeteiligte St Donau Triheim AG` — partial — gold is substring of pred: `Donau Triheim AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Donau Triheim AG`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/1Ob159_20v`) (sent_id: `deanon_260716_TRAIN/1Ob159_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und Hofrätinnen, Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Bachfen Entwicklung AG, Reisedt 4, 4770 Radlern, Österreich, vertreten durch Mag. Markus Stender, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. Musialek Getränke GmbH, 2.

**False Positives:**

- `Partei Bachfen Entwicklung AG` — partial — gold is substring of pred: `Bachfen Entwicklung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Mag. Korn`(person)
- `Bachfen Entwicklung AG`(organisation)
- `Reisedt 4, 4770 Radlern, Österreich`(address)
- `Mag. Markus Stender`(person)
- `Musialek Getränke GmbH`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/1Ob163_21h`) (sent_id: `deanon_260716_TRAIN/1Ob163_21h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Christine Neemeyer, vertreten durch Mag. Dieter Koch und Mag. Natascha Jilek, Rechtsanwälte in Bruck an der Mur, gegen die beklagte Partei Synbach-Holz Bank AG, Bergbahnweg 7j, 4632 Oberthambach, Österreich, vertreten durch Mag. Martina Hosp ua, Rechtsanwälte in Salzburg, wegen Feststellung (Streitwert 103.488,18 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 21. Juni 2021, GZ 2 R 70/21h-19, mit dem das Urteil des Landesgerichts Salzburg vom 12. März 2021, GZ 10 Cg 52/20k-15, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Synbach-Holz Bank AG` — partial — gold is substring of pred: `Synbach-Holz Bank`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Parzmayr`(person)
- `Christine Neemeyer`(person)
- `Mag. Dieter Koch`(person)
- `Mag. Natascha Jilek`(person)
- `Synbach-Holz Bank`(organisation)
- `Bergbahnweg 7j, 4632 Oberthambach, Österreich`(address)
- `Mag. Martina Hosp`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Salzburg`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Dr. Florenzia Münsterer, vertreten durch Rechtsanwälte Dr. Amhof & Dr. Damian GmbH in Wien, gegen die beklagte Partei MittelEnergie Werke Bank AG, Altlassing 110, 4183 Ahorn, Österreich, vertreten durch Urbanek Lind Schmied Reisch Rechtsanwälte OG in Wien, wegen 600.090 EUR sA, über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 25. Mai 2011, GZ 15 R 64/11h-54, mit dem das Urteil des Handelsgerichts Wien vom 14. Jänner 2011, GZ 16 Cg 20/10f-50, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Partei MittelEnergie Werke Bank AG` — partial — gold is substring of pred: `MittelEnergie Werke Bank`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Dr. Grohmann`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Florenzia Münsterer`(person)
- `Rechtsanwälte Dr. Amhof & Dr. Damian GmbH`(organisation)
- `MittelEnergie Werke Bank`(organisation)
- `Altlassing 110, 4183 Ahorn, Österreich`(address)
- `Urbanek Lind Schmied Reisch Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/1Ob226_20x`) (sent_id: `deanon_260716_TRAIN/1Ob226_20x_52`)


C-620/17,Hochtief Solutions AG, Rn 35, jeweils mwN).

**False Positives:**

- `Hochtief Solutions AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_260716_TRAIN/1Ob56_17t`) (sent_id: `deanon_260716_TRAIN/1Ob56_17t_4`)


Gloria Hackenbuchner GmbH, Untere Kanalstraße 187, 2471 Hollern, Österreich, vertreten durch Mag. Manfred Sommerbauer und MMag. Dr. Michael Dohr LL.M., Rechtsanwälte in Wiener Neustadt, und 2. Nelleßen + Stümpfel Automotive AG, Villengasse 31, 8670 Krieglach, Österreich, vertreten durch die Kosch & Partner Rechtsanwälte GmbH, Wiener Neustadt, wegen 76.444,01 EUR sA über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Jänner 2017, GZ 1 R 164/16v-174, mit dem das Urteil des Handelsgerichts Wien vom 12. August 2016, GZ 65 Cg 12/15x-169, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Stümpfel Automotive AG` — partial — pred is substring of gold: `Nelleßen + Stümpfel Automotive AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gloria Hackenbuchner`(person)
- `Untere Kanalstraße 187, 2471 Hollern, Österreich`(address)
- `Mag. Manfred Sommerbauer`(person)
- `MMag. Dr. Michael Dohr LL.M.`(person)
- `Nelleßen + Stümpfel Automotive AG`(organisation)
- `Villengasse 31, 8670 Krieglach, Österreich`(address)
- `Kosch & Partner Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/23Os1_15t`) (sent_id: `deanon_260716_TRAIN/23Os1_15t_9`)


Denn die Beweisthemen (Geschäftsgrundlage der eingangs genannten Vereinbarung vom 11. Dezember 2012 mit der Bornwasser & Plöckinger Druck AG; von derselben intendierte Verwertung der Liegenschaften in Thalstraße 358X, 5232 Aigen, Österreich durch Zwangsversteigerung ungeachtet eines allfälligen Abverkaufs von Liegenschaften in Am Weinbühel 2, 5201 Wimm, Österreich ; Auftrag der Mandanten des Disziplinarbeschuldigten zur Zurückziehung des Antrags auf Aufhebung der Höfeeigenschaft;

**False Positives:**

- `Plöckinger Druck AG` — partial — pred is substring of gold: `Bornwasser & Plöckinger Druck AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bornwasser & Plöckinger Druck AG`(organisation)
- `Thalstraße 358X, 5232 Aigen, Österreich`(address)
- `Am Weinbühel 2, 5201 Wimm, Österreich`(address)

**Example 8** (doc_id: `deanon_260716_TRAIN/2Ob216_18f`) (sent_id: `deanon_260716_TRAIN/2Ob216_18f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden und den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé und die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Sandra Olbrechts, vertreten durch Mag. Martin Paar und Mag. Hermann Zwanzger, Rechtsanwälte in Wien, gegen die beklagte Partei Inn Kraftfengart AG, Julius Jax-Gasse 64, 4623 Waldenberg, Österreich, vertreten durch Dr. Helmut Weinzettl, Rechtsanwalt in Wiener Neustadt, wegen 14.817,50 EUR sA, über die Revisionen beider Parteien gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 27. Juni 2018, GZ 18 R 11/18y-64, mit welchem das Urteil des Bezirksgerichts Baden vom 28. Dezember 2017, GZ 7 C 1010/15x-58, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revisionen werden zurückgewiesen.

**False Positives:**

- `Partei Inn Kraftfengart AG` — partial — gold is substring of pred: `Inn Kraftfengart AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Veith`(person)
- `Dr. Musger`(person)
- `Dr. E. Solé`(person)
- `Dr. Nowotny`(person)
- `Mag. Pertmayr`(person)
- `Sandra Olbrechts`(person)
- `Mag. Martin Paar`(person)
- `Mag. Hermann Zwanzger`(person)
- `Inn Kraftfengart AG`(organisation)
- `Julius Jax-Gasse 64, 4623 Waldenberg, Österreich`(address)
- `Dr. Helmut Weinzettl`(person)
- `Landesgerichts Wiener Neustadt`(organisation)
- `Bezirksgerichts Baden`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/2Ob71_18g`) (sent_id: `deanon_260716_TRAIN/2Ob71_18g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé und den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Adrian Niel, vertreten durch Dr. Robert Eiter, Rechtsanwalt in Landeck, gegen die beklagte Partei Nexzor AG, Obernreith 59, 6094 Kristen, Österreich, Deutschland, vertreten durch Dr. Andreas Kolar, Rechtsanwalt in Innsbruck, wegen 17.260,29 EUR sA, über die Revision der klagenden Partei gegen das Teilurteil des Landesgerichts Innsbruck als Berufungsgericht vom 14. November 2017, GZ 1 R 188/17d-69, mit welchem das Urteil des Bezirksgerichts Landeck vom 18. Mai 2017, GZ 2 C 123/14w-63, teilweise abgeändert wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Nexzor AG` — partial — gold is substring of pred: `Nexzor AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Dr. Veith`(person)
- `Dr. Musger`(person)
- `Dr. E. Solé`(person)
- `Dr. Nowotny`(person)
- `Adrian Niel`(person)
- `Dr. Robert Eiter`(person)
- `Nexzor AG`(organisation)
- `Obernreith 59, 6094 Kristen, Österreich`(address)
- `Dr. Andreas Kolar`(person)
- `Landesgerichts Innsbruck`(organisation)
- `Bezirksgerichts Landeck`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/2Ob85_11f`) (sent_id: `deanon_260716_TRAIN/2Ob85_11f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Niklas Nikoloff, 9020 Klagenfurt, vertreten durch Mag. Michael Hirm, Rechtsanwalt in Klagenfurt, sowie der Nebenintervenientin auf Seiten der klagenden Partei Wetzlau+Härdle Versicherung AG, Maulwurfgasse 2, 4090 Stadl, Österreich, vertreten durch Dr. Martin Wuelz, Rechtsanwalt in Innsbruck, gegen die beklagten Parteien 1.

**False Positives:**

- `Partei Wetzlau+Härdle Versicherung AG` — partial — gold is substring of pred: `Wetzlau+Härdle Versicherung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Baumann`(person)
- `Dr. Veith`(person)
- `Dr. E. Solé`(person)
- `Dr. Schwarzenbacher`(person)
- `Dr. Nowotny`(person)
- `Niklas Nikoloff`(person)
- `Mag. Michael Hirm`(person)
- `Wetzlau+Härdle Versicherung AG`(organisation)
- `Maulwurfgasse 2, 4090 Stadl, Österreich`(address)
- `Dr. Martin Wuelz`(person)

**Example 11** (doc_id: `deanon_260716_TRAIN/3Ob72_20i`) (sent_id: `deanon_260716_TRAIN/3Ob72_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Marktgemeinde James Weyand, MA, vertreten durch Dr. Nader Karl Mahdi, Rechtsanwalt in Wattens, gegen die beklagte Partei Lützeler Garten AG, Esteplatz 2, 9064 Schöpfendorf, Österreich, vertreten durch Altenweisl Wallnöfer Watschinger Zimmermann Rechtsanwälte GmbH in Innsbruck, und die auf Seiten der beklagten Partei beigetretene Nebenintervenientin Demeyer u. Köktas Analyse GmbH, Zinkendorferstraße 100, 9321 Schöttlhof, Österreich, vertreten durch Dr. Christian Girardi, LL.M., Ing. Dr. Stefan Schwärzler, Mag. Daniel Pichler, Rechtsanwälte in Innsbruck, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. März 2020, GZ 1 R 5/20z-27, womit das Urteil des Landesgerichts Innsbruck vom 14. November 2019, GZ 12 Cg 33/19m-18, teilweise bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Partei Lützeler Garten AG` — partial — gold is substring of pred: `Lützeler Garten AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Roch`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Dr. Stefula`(person)
- `James Weyand, MA`(person)
- `Dr. Nader Karl Mahdi`(person)
- `Lützeler Garten AG`(organisation)
- `Esteplatz 2, 9064 Schöpfendorf, Österreich`(address)
- `Altenweisl Wallnöfer Watschinger Zimmermann Rechtsanwälte GmbH`(organisation)
- `Demeyer u. Köktas Analyse GmbH`(organisation)
- `Zinkendorferstraße 100, 9321 Schöttlhof, Österreich`(address)
- `Dr. Christian Girardi, LL.M.`(person)
- `Ing. Dr. Stefan Schwärzler`(person)
- `Mag. Daniel Pichler`(person)
- `Oberlandesgerichts Innsbruck`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/4Fsc1_10z`) (sent_id: `deanon_260716_TRAIN/4Fsc1_10z_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel und Dr. Jensik als weitere Richter in der Rechtssache der klagenden Partei GDH Metall AG, Weinzierl-Josef Pfeiffer-Str. 6, 3443 Gerersdorf, Österreich, vertreten durch Dr. Hartmut Mayer, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Finn Hierle, vertreten durch Mag. Gerhard Pilz, Rechtsanwalt, als Verfahrenshelfer, wegen 3.330,19 EUR sA (AZ 35 R 24/09b des Landesgerichts für Zivilrechtssachen Wien), zum Fristsetzungsantrag der beklagten Partei vom 28. Oktober 2009 an den Obersten Gerichtshof im Ablehnungsverfahren den Beschluss gefasst:  Spruch Der Fristsetzungsantrag wird zurückgewiesen.

**False Positives:**

- `Partei GDH Metall AG` — partial — gold is substring of pred: `GDH Metall AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schenk`(person)
- `Dr. Vogel`(person)
- `Dr. Jensik`(person)
- `GDH Metall AG`(organisation)
- `Weinzierl-Josef Pfeiffer-Str. 6, 3443 Gerersdorf, Österreich`(address)
- `Dr. Hartmut Mayer`(person)
- `Mag. Finn Hierle`(person)
- `Mag. Gerhard Pilz`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Obersten Gerichtshof`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/4Ob165_09g`) (sent_id: `deanon_260716_TRAIN/4Ob165_09g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Schenk als Vorsitzende sowie die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei DRH Cloud AG, Viertlerweg 451, 2533 Glashütten, Österreich, vertreten durch Ewald Weninger Rechtsanwalts GmbH in Wien, gegen die beklagte Partei West Steinfen AG, Josef-Kainzmayer-Gasse 9, 4271 Witzelsberg, Österreich, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Feststellung und Anfechtung (Streitwert: 101.000.000 EUR), im Verfahren über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Juni 2009, GZ 5 R 44/09s-15, womit das Urteil des Handelsgerichts Wien vom 26. Jänner 2008, GZ 19 Cg 98/08w-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Zurückziehung der außerordentlichen Revision der klagenden Partei dient zur Kenntnis.

**False Positives:**

- `Partei DRH Cloud AG` — partial — gold is substring of pred: `DRH Cloud AG`
- `Partei West Steinfen AG` — partial — gold is substring of pred: `West Steinfen AG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schenk`(person)
- `Dr. Vogel`(person)
- `Dr. Jensik`(person)
- `Dr. Musger`(person)
- `Dr. Schwarzenbacher`(person)
- `DRH Cloud AG`(organisation)
- `Viertlerweg 451, 2533 Glashütten, Österreich`(address)
- `Ewald Weninger Rechtsanwalts GmbH`(organisation)
- `West Steinfen AG`(organisation)
- `Josef-Kainzmayer-Gasse 9, 4271 Witzelsberg, Österreich`(address)
- `Schönherr Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/4Ob174_24b`) (sent_id: `deanon_260716_TRAIN/4Ob174_24b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Mag. Istjan, LL.M., und Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Greule Recycling GmbH, Staudenweg, Oberau 49, 3571 Stallegg, Österreich, vertreten durch Mag. Dieter Koch, Rechtsanwalt in Bruck an der Mur, gegen die beklagte Partei HEWQ IT Institut AG, Enengl-Florianiweg 15, 4892 Grubleiten, Österreich, vertreten durch die AHP Rechtsanwälte OG in Klagenfurt am Wörthersee, wegen 171.573,05 CHF sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 11. Juli 2024, GZ 4 R 62/24f-26, mit dem das Urteil des Landesgerichts Klagenfurt vom 31. Jänner 2024, GZ 20 Cg 40/23v-20, abgeändert wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Partei HEWQ IT Institut AG` — partial — gold is substring of pred: `HEWQ IT Institut AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schwarzenbacher`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Mag. Istjan, LL.M.`(person)
- `Mag. Waldstätten`(person)
- `Dr. Stiefsohn`(person)
- `Greule Recycling GmbH`(organisation)
- `Staudenweg, Oberau 49, 3571 Stallegg, Österreich`(address)
- `Mag. Dieter Koch`(person)
- `HEWQ IT Institut AG`(organisation)
- `Enengl-Florianiweg 15, 4892 Grubleiten, Österreich`(address)
- `AHP Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts Klagenfurt`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/4Ob19_10p`) (sent_id: `deanon_260716_TRAIN/4Ob19_10p_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei StadtEnergie Planung gesellschaft mbH,*****, vertreten durch Prof. Haslinger & Partner, Rechtsanwälte in Linz, gegen die beklagte Partei Deecken Event AG,*****, vertreten durch Rechtsanwälte Konrad & Schröttner OG in Graz, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 65.000 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 25. November 2009, GZ 6 R 169/09h-37, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Deecken Event AG` — partial — gold is substring of pred: `Deecken Event AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schenk`(person)
- `Dr. Vogel`(person)
- `Dr. Jensik`(person)
- `Dr. Musger`(person)
- `Dr. Schwarzenbacher`(person)
- `StadtEnergie Planung gesellschaft mbH`(organisation)
- `Prof. Haslinger & Partner, Rechtsanwälte`(organisation)
- `Deecken Event AG`(organisation)
- `Oberlandesgerichts Graz`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/4Ob64_18t`) (sent_id: `deanon_260716_TRAIN/4Ob64_18t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Vogel als Vorsitzenden sowie die Hofräte Dr. Schwarzenbacher, Hon.-Prof. Dr. Brenn, Dr. Rassi und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Mag. Florentin Jakobautzki, vertreten durch die Konrad Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Lischke&Rohleff Solar AG, Volkshausplatz 46, 3830 Pyhra, Österreich, vertreten durch die Binder Grösswang Rechtsanwälte GmbH in Wien, wegen 106.196,74 EUR sA und Feststellung (Streitwert 156.303,26 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 13. Oktober 2017, GZ 129 R 24/17y-24, womit das Urteil des Handelsgerichts Wien vom 2. August 2017, GZ 10 Cg 1/16a-19, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rohleff Solar AG` — partial — pred is substring of gold: `Lischke&Rohleff Solar AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Vogel`(person)
- `Dr. Schwarzenbacher`(person)
- `Hon.-Prof. Dr. Brenn`(person)
- `Dr. Rassi`(person)
- `MMag. Matzka`(person)
- `Mag. Florentin Jakobautzki`(person)
- `Konrad Rechtsanwälte GmbH`(organisation)
- `Lischke&Rohleff Solar AG`(organisation)
- `Volkshausplatz 46, 3830 Pyhra, Österreich`(address)
- `Binder Grösswang Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/5Ob102_24x`) (sent_id: `deanon_260716_TRAIN/5Ob102_24x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei ÖkR KzlR Sonja Doganoglu, wider die beklagte Partei Stoeberl Bau AG, Bernhard-Paumgartner-Weg 41, 3233 Hohenbrand, Österreich, Deutschland vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 13.607,40 EUR sA und Feststellung über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Ried im Innkreis als Berufungsgericht vom 13. März 2024, GZ 18 R 2/24k-29, mit dem das Urteil des Bezirksgerichts Schärding vom 6. November 2023, GZ 2 C 478/20g-24, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei Stoeberl Bau AG` — partial — gold is substring of pred: `Stoeberl Bau AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Jensik`(person)
- `Mag. Wurzer`(person)
- `Mag. Painsi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Steger`(person)
- `ÖkR KzlR Sonja Doganoglu`(person)
- `Stoeberl Bau AG`(organisation)
- `Bernhard-Paumgartner-Weg 41, 3233 Hohenbrand, Österreich`(address)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`(organisation)
- `Landesgerichts Ried im Innkreis`(organisation)
- `Bezirksgerichts Schärding`(organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/5Ob141_23f`) (sent_id: `deanon_260716_TRAIN/5Ob141_23f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Svenja Brochtrup, vertreten durch Poduschka Partner AnwaltsGmbH in Linz, gegen die beklagte Partei EnnsFinanzen AG, Bartlstraße 9, 8490 Zelting, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 19.600 EUR sA über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 22. Mai 2023, GZ 12 R 6/23y-34, mit dem das Urteil des Landesgerichts Wels vom 11. Jänner 2023, GZ 8 Cg 29/20s-29, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Partei EnnsFinanzen AG` — partial — gold is substring of pred: `EnnsFinanzen AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Jensik`(person)
- `Mag. Wurzer`(person)
- `Mag. Painsi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Steger`(person)
- `Svenja Brochtrup`(person)
- `EnnsFinanzen AG`(organisation)
- `Bartlstraße 9, 8490 Zelting, Österreich`(address)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Wels`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/5Ob221_22v`) (sent_id: `deanon_260716_TRAIN/5Ob221_22v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Berg-E‑Commerce Dienstleistungen GmbH in Liquidation, Rotundenplatz 78, 8403 Stangersdorf-Gewerbegebiet, Österreich, vertreten durch Mag. Gottfried Tazol, Rechtsanwalt in Völkermarkt, gegen die beklagte Partei Logistik Waldseecon AG, Am Kurplatz 2, 5761 Bachwinkl, Österreich, vertreten durch Mag. Alexander Todor-Kostic LL.M., Mag. Silke Todor-Kostic, Rechtsanwälte in Velden am Wörthersee, wegen 84.999,13 EUR sA, über die außerordentliche Revision der klagenden Partei (Revisionsinteresse 62.200,50 EUR sA) gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 12. Oktober 2022, GZ 5 R 74/22z-53, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Logistik Waldseecon AG` — partial — gold is substring of pred: `Logistik Waldseecon AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Jensik`(person)
- `Mag. Wurzer`(person)
- `Mag. Painsi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Steger`(person)
- `Berg-E‑Commerce Dienstleistungen GmbH`(organisation)
- `Rotundenplatz 78, 8403 Stangersdorf-Gewerbegebiet, Österreich`(address)
- `Mag. Gottfried Tazol`(person)
- `Logistik Waldseecon AG`(organisation)
- `Am Kurplatz 2, 5761 Bachwinkl, Österreich`(address)
- `Mag. Alexander Todor-Kostic`(person)
- `Mag. Silke Todor-Kostic`(person)
- `Oberlandesgerichts Graz`(organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/6Ob10_22x`) (sent_id: `deanon_260716_TRAIN/6Ob10_22x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Nowotny, Dr. Hofer-Zeni-Rennhofer, Dr. Faber und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Tralog-KI Versicherungs AG, Adolf Schwayer-Gasse 22, 3371 Hofa, Österreich, vertreten durch Musey Rechtsanwalt GmbH in Salzburg, gegen die beklagte Partei WaldRecycling GmbH, Georg-Rendl-Weg 28, 9065 Ebenthal, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 7.246.839 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 1. Dezember 2021, GZ 2 R 165/21d-49, womit das Teil- und Zwischenurteil des Landesgerichts Salzburg vom 6. September 2021, GZ 6 Cg 16/20m-45, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Tralog-KI Versicherungs AG` — partial — gold is substring of pred: `Tralog-KI Versicherungs AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Gitschthaler`(person)
- `Dr. Nowotny`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Faber`(person)
- `Mag. Pertmayr`(person)
- `Tralog-KI Versicherungs AG`(organisation)
- `Adolf Schwayer-Gasse 22, 3371 Hofa, Österreich`(address)
- `Musey Rechtsanwalt GmbH`(organisation)
- `WaldRecycling GmbH`(organisation)
- `Georg-Rendl-Weg 28, 9065 Ebenthal, Österreich`(address)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Salzburg`(organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/6Ob231_24z`) (sent_id: `deanon_260716_TRAIN/6Ob231_24z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Hofer-Zeni-Rennhofer als Vorsitzende sowie die Hofrätinnen und Hofräte Hon.-Prof. Dr. Faber, Mag. Pertmayr, Dr. Weber und Mag. Nigl LL.M. als weitere Richter in der Rechtssache der klagenden Partei Ing. Tiffany Jähncke, vertreten durch Poduschka Partner Anwaltsgesellschaft mbH in Linz, wider die beklagte Partei Sudconbach-Bau AG, Hart, Akazienstraße 15v, 4064 Oftering, Österreich, Deutschland, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 9.600 EUR sA, im Verfahren über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Linz als Berufungsgericht vom 7. Oktober 2024, GZ 6 R 57/24b-31, womit das Urteil des Bezirksgerichts Traun vom 16. Februar 2024, GZ 2 C 198/23z-22, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei vom 9. Dezember 2025 auf Fortsetzung des Verfahrens wird abgewiesen.

**False Positives:**

- `Partei Sudconbach-Bau AG` — partial — gold is substring of pred: `Sudconbach-Bau AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Hon.-Prof. Dr. Faber`(person)
- `Mag. Pertmayr`(person)
- `Dr. Weber`(person)
- `Mag. Nigl`(person)
- `Ing. Tiffany Jähncke`(person)
- `Poduschka Partner Anwaltsgesellschaft mbH`(organisation)
- `Sudconbach-Bau AG`(organisation)
- `Hart, Akazienstraße 15v, 4064 Oftering, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)
- `Landesgerichts Linz`(organisation)
- `Bezirksgerichts Traun`(organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_137`)


Der EuGH teilte die von einigen Mitgliedstaaten (darunter auch Österreich) geäußerte Rechtsansicht, eine Befristung des Widerrufsrechts sei aus Gründen der Rechtssicherheit unerlässlich, nicht (EuGH C-481/99 [Georg und Helga Heininger/Bayerische Hypo- und Vereinsbank AG]).

**False Positives:**

- `Vereinsbank AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_260716_TRAIN/6Ob47_25t`) (sent_id: `deanon_260716_TRAIN/6Ob47_25t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Hofer-Zeni-Rennhofer als Vorsitzende sowie die Hofrätinnen und Hofräte Dr. Faber, Mag. Pertmayr, Dr. Weber und Mag. Nigl LL.M. als weitere Richter in der Rechtssache der klagenden Partei Kimberly Schnellhardt, vertreten durch Dr. Alexander Amann LL.M., Rechtsanwalt in Gamprin-Bendern, Liechtenstein, wider die beklagte Partei Digital Trasudwerk AG, Galles 5, 8453 Kitzelsdorf, Österreich, Deutschland, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 71.888,75 EUR sA Zug um Zug gegen die Rückstellung eines Fahrzeugs, in eventu wegen 17.972,19 EUR sA und Feststellung, im Verfahren über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Jänner 2025, GZ 11 R 7/25t-63, den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Partei Digital Trasudwerk AG` — partial — gold is substring of pred: `Digital Trasudwerk AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Faber`(person)
- `Mag. Pertmayr`(person)
- `Dr. Weber`(person)
- `Mag. Nigl`(person)
- `Kimberly Schnellhardt`(person)
- `Dr. Alexander Amann LL.M.`(person)
- `Digital Trasudwerk AG`(organisation)
- `Galles 5, 8453 Kitzelsdorf, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/6Ob51_21z`) (sent_id: `deanon_260716_TRAIN/6Ob51_21z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Univ.-Prof. Dr. Kodek, Dr. Nowotny, Dr. Faber und Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei Mag. Fabienne Müffler, vertreten durch Dr. Wolfgang Haslinger, LL.M., Rechtsanwalt in Wien, gegen die beklagte Partei See Conlemgart Gruppe Bank Schlötels&Katzenberg Digital AG, C - Obersee 27A, 4963 Nöfing, Österreich, vertreten durch Dr. Anton Ehm und Mag. Thomas Mödlagl, Rechtsanwälte in Wien, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Jänner 2021, GZ 3 R 63/20m-18, mit dem das Urteil des Handelsgerichts Wien vom 7. September 2020, GZ 56 Cg 9/20x-14, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wirdFolge gegeben.

**False Positives:**

- `Katzenberg Digital AG` — partial — pred is substring of gold: `Schlötels&Katzenberg Digital AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Gitschthaler`(person)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. Nowotny`(person)
- `Dr. Faber`(person)
- `Mag. Istjan, LL.M.`(person)
- `Mag. Fabienne Müffler`(person)
- `Dr. Wolfgang Haslinger, LL.M.`(person)
- `See Conlemgart Gruppe Bank`(organisation)
- `Schlötels&Katzenberg Digital AG`(organisation)
- `C - Obersee 27A, 4963 Nöfing, Österreich`(address)
- `Dr. Anton Ehm`(person)
- `Mag. Thomas Mödlagl`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/7Nc6_13m`) (sent_id: `deanon_260716_TRAIN/7Nc6_13m_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Huber als Vorsitzende und die Hofrätinnen und Hofräte Dr. Hoch, Dr. Kalivoda, Mag. Dr. Wurdinger und Mag. Malesich als weitere Richter in der Arbeitsrechtssache der klagenden Partei Dr. Sabrina Dijkman, vertreten durch Dr. Clemens Gärner, Rechtsanwalt in Wien, gegen die beklagte Partei FPZE Metall AG, Jeitnerweg 110, 8773 Seiz, Österreich, vertreten durch Dr. Helmut Engelbrecht und andere Rechtsanwälte in Wien, wegen 4.868,07 EUR sA und Feststellung, über die Befangenheitsanzeige des Hofrats des Obersten Gerichtshofs Dr. Richard Hargassner im Verfahren 9 ObA 29/13z den Beschluss gefasst:  Spruch Der Hofrat des Obersten Gerichtshofs Dr. Richard Hargassner ist ausgeschlossen.

**False Positives:**

- `Partei FPZE Metall AG` — partial — gold is substring of pred: `FPZE Metall AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Huber`(person)
- `Dr. Hoch`(person)
- `Dr. Kalivoda`(person)
- `Mag. Dr. Wurdinger`(person)
- `Mag. Malesich`(person)
- `Dr. Sabrina Dijkman`(person)
- `Dr. Clemens Gärner`(person)
- `FPZE Metall AG`(organisation)
- `Jeitnerweg 110, 8773 Seiz, Österreich`(address)
- `Dr. Helmut Engelbrecht`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Richard Hargassner`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Richard Hargassner`(person)

**Example 26** (doc_id: `deanon_260716_TRAIN/7Ob110_13x`) (sent_id: `deanon_260716_TRAIN/7Ob110_13x_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Huber als Vorsitzende und die Hofrätinnen und Hofräte Dr. Hoch, Dr. Kalivoda, Mag. Dr. Wurdinger und Mag. Malesich als weitere Richter in der Rechtssache der klagenden Partei Gerdelbracht Telekom AG, KLG Gartengemeinde Adolfstor 4, 4352 Oberkalmberg, Österreich, vertreten durch Kunz Schima Wallentin Rechtsanwälte OG in Wien, gegen die beklagte Partei Mag. (FH) Franz Burgschmidt, vertreten durch Binder Grösswang Rechtsanwälte OG in Wien, wegen Erteilung von Auskünften, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. April 2013, GZ 11 R 75/13z-12, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Gerdelbracht Telekom AG` — partial — gold is substring of pred: `Gerdelbracht Telekom AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Huber`(person)
- `Dr. Hoch`(person)
- `Dr. Kalivoda`(person)
- `Mag. Dr. Wurdinger`(person)
- `Mag. Malesich`(person)
- `Gerdelbracht Telekom AG`(organisation)
- `KLG Gartengemeinde Adolfstor 4, 4352 Oberkalmberg, Österreich`(address)
- `Kunz Schima Wallentin Rechtsanwälte OG`(organisation)
- `Mag. (FH) Franz Burgschmidt`(person)
- `Binder Grösswang Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/7Ob113_17v`) (sent_id: `deanon_260716_TRAIN/7Ob113_17v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Dr. Höllwerth, Dr. E. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Camilla Löble, vertreten durch Waltl & Partner, Rechtsanwälte in Zell am See, gegen die beklagte Partei Sieckkötter Medien AG, 6.

**False Positives:**

- `Partei Sieckkötter Medien AG` — partial — gold is substring of pred: `Sieckkötter Medien AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Dr. Höllwerth`(person)
- `Dr. E. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Camilla Löble`(person)
- `Sieckkötter Medien AG`(organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/7Ob129_10m`) (sent_id: `deanon_260716_TRAIN/7Ob129_10m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Huber als Vorsitzende und die Hofräte des Obersten Gerichtshofs Dr. Schaumüller, Dr. Hoch, Dr. Kalivoda und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Mario Maiers AG, Krippau 33, 5652 Dienten am Hochkönig, Österreich, vertreten durch Mag. Dr. Hans Herwig Toriser, Rechtsanwalt in Klagenfurt, gegen die beklagte Partei Merlin Paolini, vertreten durch Dr. Erich Moser, Rechtsanwalt in Murau, wegen 11.000 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 12. April 2010, GZ 2 R 45/10w-27, womit das Urteil des Landesgerichts Leoben vom 28. Jänner 2010, GZ 7 Cg 130/09k-23, bestätigt wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Mario Maiers AG` — partial — gold is substring of pred: `Mario Maiers`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Huber`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schaumüller`(person)
- `Dr. Hoch`(person)
- `Dr. Kalivoda`(person)
- `Dr. Grohmann`(person)
- `Mario Maiers`(person)
- `Krippau 33, 5652 Dienten am Hochkönig, Österreich`(address)
- `Mag. Dr. Hans Herwig Toriser`(person)
- `Merlin Paolini`(person)
- `Dr. Erich Moser`(person)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts Leoben`(organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/7Ob137_17y`) (sent_id: `deanon_260716_TRAIN/7Ob137_17y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Dr. Höllwerth, Dr. E. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Dr. Elias Hemerle, vertreten durch die Breiteneder Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Mooshuber Planung AG, Schustergasse 57, 4682 Brunau, Österreich, vertreten durch die Binder Grösswang Rechtsanwälte GmbH in Wien, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 31. Mai 2017, GZ 4 R 19/17v-16, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Mooshuber Planung AG` — partial — gold is substring of pred: `Mooshuber Planung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Dr. Höllwerth`(person)
- `Dr. E. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Dr. Elias Hemerle`(person)
- `Breiteneder Rechtsanwalt GmbH`(organisation)
- `Mooshuber Planung AG`(organisation)
- `Schustergasse 57, 4682 Brunau, Österreich`(address)
- `Binder Grösswang Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/7Ob137_20b`) (sent_id: `deanon_260716_TRAIN/7Ob137_20b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende sowie die Hofrätin und die Hofräte Hon.-Prof. Dr. Höllwerth, Mag. Dr. Wurdinger, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Mag. Edwin Bornemeyer, vertreten durch die Pilz & Burghofer Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Thönniß Immobilien AG, Dürnstein in der Steiermark 55, 3920 Josefsdorf, Österreich, vertreten durch Mag. Dr. Otto Ranzenhofer, Rechtsanwalt in Wien, wegen 300.000 EUR sA, den Beschluss gefasst:  Spruch Das Urteil des Obersten Gerichtshofs vom 25. November 2020, AZ 7 Ob 137/20b, wird wie folgt berichtigt: Im Spruchpunkt 2. hat die Wortfolge: „samt 4 % Zinsen seit 3. 11. 2014“ zu entfallen.

**False Positives:**

- `Partei Thönniß Immobilien AG` — partial — gold is substring of pred: `Thönniß Immobilien AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Mag. Dr. Wurdinger`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Mag. Edwin Bornemeyer`(person)
- `Pilz & Burghofer Rechtsanwalts GmbH`(organisation)
- `Thönniß Immobilien AG`(organisation)
- `Dürnstein in der Steiermark 55, 3920 Josefsdorf, Österreich`(address)
- `Mag. Dr. Otto Ranzenhofer`(person)
- `Obersten Gerichtshofs`(organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/7Ob162_20d`) (sent_id: `deanon_260716_TRAIN/7Ob162_20d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Dorothea Waeger, Bakk. techn. BEd, vertreten durch Mag. Marco und Mag. Amelie Kunczicky, Rechtsanwälte in Mayrhofen, gegen die beklagte Partei OberVerlag AG, Thomas Alva Edison-Straße 158, 4843 Wörmansedt, Österreich, vertreten durch Mag. Thomas Anker und DI Mag. Nikolaus Gratl, Rechtsanwäte in Innsbruck, wegen Urkundeneinsicht, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. Juni 2020, GZ 4 R 55/20z-18, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei OberVerlag AG` — partial — gold is substring of pred: `OberVerlag AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Dr. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Dorothea Waeger, Bakk. techn. BEd`(person)
- `Mag. Marco`(person)
- `Mag. Amelie Kunczicky`(person)
- `OberVerlag AG`(organisation)
- `Thomas Alva Edison-Straße 158, 4843 Wörmansedt, Österreich`(address)
- `Mag. Thomas Anker`(person)
- `DI Mag. Nikolaus Gratl`(person)
- `Oberlandesgerichts Innsbruck`(organisation)

**Example 32** (doc_id: `deanon_260716_TRAIN/7Ob192_16k`) (sent_id: `deanon_260716_TRAIN/7Ob192_16k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende sowie die Hofrätinnen und Hofräte Dr. Höllwerth, Dr. E. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Mag. Mikolaj Frosch, vertreten durch Mag. Klaus Fürlinger und andere Rechtsanwälte in Linz, gegen die beklagte Partei RheinMarine AG, Zeiseleck 30, 4170 Sankt Oswald bei Haslach, Österreich, vertreten durch Mag. Gerlach Bachinger, Rechtsanwalt in Traun, wegen 25.452,37 EUR sA und Feststellung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 30. August 2016, GZ 6 R 148/16a-14, womit das Urteil des Landesgerichts Linz vom 20. Mai 2016, GZ 5 Cg 11/16m-10, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Partei RheinMarine AG` — partial — gold is substring of pred: `RheinMarine AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Dr. Höllwerth`(person)
- `Dr. E. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Mag. Mikolaj Frosch`(person)
- `Mag. Klaus Fürlinger`(person)
- `RheinMarine AG`(organisation)
- `Zeiseleck 30, 4170 Sankt Oswald bei Haslach, Österreich`(address)
- `Mag. Gerlach Bachinger`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Linz`(organisation)

**Example 33** (doc_id: `deanon_260716_TRAIN/7Ob201_12b`) (sent_id: `deanon_260716_TRAIN/7Ob201_12b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Dr. Huber als Vorsitzende und die Hofrätinnen und Hofräte Dr. Hoch, Dr. Kalivoda, Mag. Dr. Wurdinger und Mag. Malesich als weitere Richter in der Rechtssache der klagenden Partei Bundeskammer für Arbeiter und Angestellte, 1041 Wien, Prinz-Eugen-Straße 20-22, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Sudlex Heizung AG, Weißenbachstraße 12, 9376 Lichtegg, Österreich, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Unterlassung und Urteilsveröffentlichung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 9. November 2011, GZ 2 R 203/11d-11, womit das Urteil des Handelsgerichts Wien vom 26. Juni 2011, GZ 19 Cg 49/11v-5, teilweise abgeändert wurde, beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Sudlex Heizung AG` — partial — gold is substring of pred: `Sudlex Heizung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Huber`(person)
- `Dr. Hoch`(person)
- `Dr. Kalivoda`(person)
- `Mag. Dr. Wurdinger`(person)
- `Mag. Malesich`(person)
- `Dr. Walter Reichholf`(person)
- `Sudlex Heizung AG`(organisation)
- `Weißenbachstraße 12, 9376 Lichtegg, Österreich`(address)
- `Schönherr Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 34** (doc_id: `deanon_260716_TRAIN/7Ob203_24i`) (sent_id: `deanon_260716_TRAIN/7Ob203_24i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Dr. Wurdinger, Mag. Malesich, Dr. Weber und Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Christina Steenfath, vertreten durch Mag. Martin Wabra, Rechtsanwalt in Gmünd, gegen die beklagte Partei SüdSanitär AG, Rechenweg 4O, 3261 Ernegg, Österreich, vertreten durch die MUSEY rechtsanwalt gmbH in Salzburg, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. Oktober 2024, GZ 5 R 144/24v-49, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei SüdSanitär AG` — partial — gold is substring of pred: `SüdSanitär AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Solé`(person)
- `Mag. Dr. Wurdinger`(person)
- `Mag. Malesich`(person)
- `Dr. Weber`(person)
- `Mag. Fitz`(person)
- `Christina Steenfath`(person)
- `Mag. Martin Wabra`(person)
- `SüdSanitär AG`(organisation)
- `Rechenweg 4O, 3261 Ernegg, Österreich`(address)
- `MUSEY rechtsanwalt gmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 35** (doc_id: `deanon_260716_TRAIN/7Ob36_25g`) (sent_id: `deanon_260716_TRAIN/7Ob36_25g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Malesich, Dr. Weber, Mag. Fitz und Mag. Jelinek als weitere Richter in der Rechtssache der klagenden Partei Gundula Aichmann, vertreten durch Poduschka Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Plönnigs Technik AG, Wieden 35, 3390 Spielberg, Österreich, vertreten durch Themmer, Toth & Partner Rechtsanwälte GmbH in Wien, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 28. November 2024, GZ 1 R 124/24t-14, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 27. Juni 2024, GZ 21 C 604/23m-10, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei Plönnigs Technik AG` — partial — gold is substring of pred: `Plönnigs Technik AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Solé`(person)
- `Mag. Malesich`(person)
- `Dr. Weber`(person)
- `Mag. Fitz`(person)
- `Mag. Jelinek`(person)
- `Gundula Aichmann`(person)
- `Poduschka Partner Anwaltsgesellschaft mbH`(organisation)
- `Plönnigs Technik AG`(organisation)
- `Wieden 35, 3390 Spielberg, Österreich`(address)
- `Themmer, Toth & Partner Rechtsanwälte GmbH`(organisation)
- `Handelsgerichts Wien`(organisation)
- `Bezirksgerichts für Handelssachen Wien`(organisation)

**Example 36** (doc_id: `deanon_260716_TRAIN/7Ob45_19x`) (sent_id: `deanon_260716_TRAIN/7Ob45_19x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Dr. Arabella Venczel, vertreten durch Dr. Stefan Gloyer, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Berkenheger Analyse AG, Ebendorfer Hauptstraße 3, 8054 Graz, Österreich, vertreten durch Dr. Herbert Salficky, Rechtsanwalt in Wien, wegen 53.526,48 EUR sA und Feststellung, den Beschluss gefasst:  Spruch Das Urteil des Obersten Gerichtshofs vom 26. Juni 2019, zu 7 Ob 45/19x wird in seinen Entscheidungsgründen dahin berichtigt, dass es auf Seite 8 in Absatz 4 anstelle „Die Revision ist zulässig, sie ist im Sinn des Aufhebungsantrags auch berechtigt“ richtig „Die Revision ist zulässig, sie ist aber nicht berechtigt“ zu lauten hat.

**False Positives:**

- `Partei Berkenheger Analyse AG` — partial — gold is substring of pred: `Berkenheger Analyse AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Dr. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Dr. Arabella Venczel`(person)
- `Dr. Stefan Gloyer`(person)
- `Berkenheger Analyse AG`(organisation)
- `Ebendorfer Hauptstraße 3, 8054 Graz, Österreich`(address)
- `Dr. Herbert Salficky`(person)
- `Obersten Gerichtshofs`(organisation)

**Example 37** (doc_id: `deanon_260716_TRAIN/7Ob48_17k`) (sent_id: `deanon_260716_TRAIN/7Ob48_17k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und durch die Hofrätinnen und Hofräte Dr. Höllwerth, Dr. E. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Seetal Consulting GmbH, Diakoniestraße 19, 3251 Ameishaufen, Österreich, vertreten durch Aigner Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Rhein-Landwirtschaft AG, Starfach-Hohe Wand Weg 97, 3386 Würmling, Österreich, vertreten durch Dr. Josef Milchram, Dr. Anton Ehm und Mag. Thomas Mödlagl, Rechtsanwälte in Wien, wegen 1.373.171,48 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 20. Jänner 2017, GZ 1 R 160/16d-52, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Rhein-Landwirtschaft AG` — partial — gold is substring of pred: `Rhein-Landwirtschaft AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Dr. Höllwerth`(person)
- `Dr. E. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Seetal Consulting GmbH`(organisation)
- `Diakoniestraße 19, 3251 Ameishaufen, Österreich`(address)
- `Aigner Rechtsanwalts GmbH`(organisation)
- `Rhein-Landwirtschaft AG`(organisation)
- `Starfach-Hohe Wand Weg 97, 3386 Würmling, Österreich`(address)
- `Dr. Josef Milchram`(person)
- `Dr. Anton Ehm`(person)
- `Mag. Thomas Mödlagl`(person)
- `Oberlandesgerichts Linz`(organisation)

**Example 38** (doc_id: `deanon_260716_TRAIN/7Ob54_20x`) (sent_id: `deanon_260716_TRAIN/7Ob54_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende sowie die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Techn R Ramona Rössler, vertreten durch Mag. Astrid Roblyek, Rechtsanwältin in Klagenfurt am Wörthersee, gegen die beklagte Partei ZED Planung AG Haberditzlgasse 29, 9341 Kreuth, Österreich, vertreten durch Jarolim Partner Rechtsanwälte GmbH in Wien, wegen 7.339,70 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 31. Oktober 2019, GZ 4 R 325/19i-15, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 15. Juli 2019, GZ 15 C 998/18y-11, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei ZED Planung AG` — partial — gold is substring of pred: `ZED Planung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Dr. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Techn R Ramona Rössler`(person)
- `Mag. Astrid Roblyek`(person)
- `ZED Planung AG`(organisation)
- `Haberditzlgasse 29, 9341 Kreuth, Österreich`(address)
- `Jarolim Partner Rechtsanwälte GmbH`(organisation)
- `Landesgerichts Klagenfurt`(organisation)
- `Bezirksgerichts Klagenfurt`(organisation)

**Example 39** (doc_id: `deanon_260716_TRAIN/7Ob60_18a`) (sent_id: `deanon_260716_TRAIN/7Ob60_18a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Dr. Höllwerth, Dr. E. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Dr. Nadja Schlegermann, vertreten durch Dr. Josef Sailer, Rechtsanwalt in Bruck an der Leitha, gegen die beklagte Partei Felmerig Lebensmittel AG, Kleinmollsberg 18, 8213 Oberrettenbach, Österreich, vertreten durch Mag. Wolfgang Weilguni, Rechtsanwalt in Wien, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Jänner 2018, GZ 1 R 127/17d-15, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Felmerig Lebensmittel AG` — partial — gold is substring of pred: `Felmerig Lebensmittel AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Dr. Höllwerth`(person)
- `Dr. E. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Dr. Nadja Schlegermann`(person)
- `Dr. Josef Sailer`(person)
- `Felmerig Lebensmittel AG`(organisation)
- `Kleinmollsberg 18, 8213 Oberrettenbach, Österreich`(address)
- `Mag. Wolfgang Weilguni`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 40** (doc_id: `deanon_260716_TRAIN/7Ob6_20p`) (sent_id: `deanon_260716_TRAIN/7Ob6_20p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Ing. Roderich Florczyk, vertreten durch Dr. Norbert Nowak, Rechtsanwalt in Wien, gegen die beklagte Partei Mittel-Energie AG, Gaunitzhof 8, 4632 Breitwies, Österreich, vertreten durch die Schönherr Rechtsanwälte GmbH in Wien, wegen 6.342,73 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 8. November 2018, GZ 60 R 98/18v-12, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 15. Juni 2018, GZ 18 C 109/18p-8, abgeändert wurde, beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Mittel-Energie AG` — partial — gold is substring of pred: `Mittel-Energie AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Dr. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Ing. Roderich Florczyk`(person)
- `Dr. Norbert Nowak`(person)
- `Mittel-Energie AG`(organisation)
- `Gaunitzhof 8, 4632 Breitwies, Österreich`(address)
- `Schönherr Rechtsanwälte GmbH`(organisation)
- `Handelsgerichts Wien`(organisation)
- `Bezirksgerichts für Handelssachen Wien`(organisation)

**Example 41** (doc_id: `deanon_260716_TRAIN/7Ob79_10h`) (sent_id: `deanon_260716_TRAIN/7Ob79_10h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Huber als Vorsitzende und die Hofräte des Obersten Gerichtshofs Dr. Schaumüller, Dr. Hoch, Dr. Kalivoda und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Pascal Sitzman, vertreten durch Dr. Arnold Mayrhofer, Rechtsanwalt in Linz, gegen die beklagte Partei Achtermeier Handel AG, Stöbergasse 14, 3643 Loitzendorf, Österreich, vertreten durch Dr. Christian Ransmayr, Rechtsanwalt in Linz, wegen Feststellung, über die außerordentliche Revision des Klägers gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 8. März 2010, GZ 2 R 130/09i-82, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Achtermeier Handel AG` — partial — gold is substring of pred: `Achtermeier Handel AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Huber`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schaumüller`(person)
- `Dr. Hoch`(person)
- `Dr. Kalivoda`(person)
- `Dr. Roch`(person)
- `Pascal Sitzman`(person)
- `Dr. Arnold Mayrhofer`(person)
- `Achtermeier Handel AG`(organisation)
- `Stöbergasse 14, 3643 Loitzendorf, Österreich`(address)
- `Dr. Christian Ransmayr`(person)
- `Oberlandesgerichts Linz`(organisation)

**Example 42** (doc_id: `deanon_260716_TRAIN/7Ob85_15y`) (sent_id: `deanon_260716_TRAIN/7Ob85_15y_4`)


Isabel Nestle AG, Reinsbach 186, 9131 Dolina, Österreich, vertreten durch Jank Weiler Operenyi Rechtsanwälte OG in Wien, 2.

**False Positives:**

- `Isabel Nestle AG` — partial — gold is substring of pred: `Isabel Nestle`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Isabel Nestle`(person)
- `Reinsbach 186, 9131 Dolina, Österreich`(address)
- `Jank Weiler Operenyi Rechtsanwälte OG`(organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/7Ob92_19h`) (sent_id: `deanon_260716_TRAIN/7Ob92_19h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Karen Jansonius, vertreten durch Dr. Herwig Ernst, Rechtsanwalt in Korneuburg, gegen die beklagte Partei Schopf Automotive AG Grebien-Gasse 50, 4675 Dirisam, Österreich, vertreten durch Dr. Herbert Laimböck, Rechtsanwalt in Wien, wegen 521.151,28 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. April 2019, GZ 5 R 32/19s-29, womit das Urteil des Handelsgerichts Wien vom 14. Jänner 2019, GZ 10 Cg 70/17z-25, bestätigt wurde, beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Schopf Automotive AG` — partial — gold is substring of pred: `Schopf Automotive AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Dr. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Karen Jansonius`(person)
- `Dr. Herwig Ernst`(person)
- `Schopf Automotive AG`(organisation)
- `Grebien-Gasse 50, 4675 Dirisam, Österreich`(address)
- `Dr. Herbert Laimböck`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 44** (doc_id: `deanon_260716_TRAIN/7Ob94_20d`) (sent_id: `deanon_260716_TRAIN/7Ob94_20d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Mag. Juliana Mündelein, vertreten durch Brand Rechtsanwälte GmbH in Wien, gegen die beklagte Partei ACBK Elektro Solutions AG, Schwarzenseer Straße 25, 9560 Steuerberg, Österreich, vertreten durch Dorda Rechtsanwälte GmbH in Wien, wegen 16.354,47 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 31. Jänner 2020, GZ 1 R 120/19b-21, womit das Urteil des Handelsgerichts Wien vom 22. Juli 2019, GZ 16 Cg 50/18d-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei ACBK Elektro Solutions AG` — partial — gold is substring of pred: `ACBK Elektro Solutions AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Dr. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Mag. Juliana Mündelein`(person)
- `Brand Rechtsanwälte GmbH`(organisation)
- `ACBK Elektro Solutions AG`(organisation)
- `Schwarzenseer Straße 25, 9560 Steuerberg, Österreich`(address)
- `Dorda Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 45** (doc_id: `deanon_260716_TRAIN/8Ob35_23i`) (sent_id: `deanon_260716_TRAIN/8Ob35_23i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn und die Hofräte Dr. Stefula und Dr. Thunhart in der Rechtssache der klagenden Parteien 1. Bergstreser&Svarc Pharma, und 2. Hoppstetter + Roloff Solar AG, L.-Forstner-Straße 4, 9341 Edling, Österreich, beide vertreten durch Dr. Heinrich Fassl, Rechtsanwalt in Wien, wider die beklagte Partei DI Edmund Wewerinck, vertreten durch Dr. Andreas A. Lintl, Rechtsanwalt in Wien, wegen 59.868,50 EUR sA und 170.440,94 EUR sA, über die Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Wien vom 26. Jänner 2023, GZ 11 R 235/22t-206, mit welchem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 30. Mai 2022, GZ 20 Cg 11/15g-194, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Roloff Solar AG` — partial — pred is substring of gold: `Hoppstetter + Roloff Solar AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Tarmann-Prentner`(person)
- `Mag. Korn`(person)
- `Dr. Stefula`(person)
- `Dr. Thunhart`(person)
- `Bergstreser&Svarc Pharma`(organisation)
- `Hoppstetter + Roloff Solar AG`(organisation)
- `L.-Forstner-Straße 4, 9341 Edling, Österreich`(address)
- `Dr. Heinrich`(person)
- `DI Edmund Wewerinck`(person)
- `Dr. Andreas A. Lintl`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 46** (doc_id: `deanon_260716_TRAIN/8Ob39_24d`) (sent_id: `deanon_260716_TRAIN/8Ob39_24d_12`)


Die OberSoftware AG habe insofern auch Offenlegungspflichten in Österreich getroffen.

**False Positives:**

- `Die OberSoftware AG` — partial — gold is substring of pred: `OberSoftware AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OberSoftware AG`(organisation)

**Example 47** (doc_id: `deanon_260716_TRAIN/8ObA18_17f`) (sent_id: `deanon_260716_TRAIN/8ObA18_17f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Brenn als weitere Richter sowie die fachkundigen Laienrichter Mag. Dr. Bernhard Gruber und Harald Kohlruss in der Arbeitsrechtssache der klagenden Partei MedR Clemens Schepper, vertreten durch Freimüller/Obereder/Pilz Rechtsanwält_innen GmbH in Wien, gegen die beklagte Partei Muehleis & Klaese Technik AG, Rosentaler Weg 2k, 9811 St. Peter in Holz, Österreich, vertreten durch DLA Piper Weiss-Tessbach Rechtsanwälte GmbH in Wien, wegen Feststellung (Streitwert 282,56 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. November 2016, GZ 7 Ra 90/16f-19, mit dem das Urteil des Arbeits- und Sozialgerichts Wien vom 20. Juli 2016, GZ 33 Cga 50/16p-15, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Klaese Technik AG` — partial — pred is substring of gold: `Muehleis & Klaese Technik AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Prof. Dr. Spenling`(person)
- `Dr. Tarmann-Prentner`(person)
- `Dr. Brenn`(person)
- `Mag. Dr. Bernhard Gruber`(person)
- `Harald Kohlruss`(person)
- `MedR Clemens Schepper`(person)
- `Freimüller/Obereder/Pilz Rechtsanwält_innen GmbH`(organisation)
- `Muehleis & Klaese Technik AG`(organisation)
- `Rosentaler Weg 2k, 9811 St. Peter in Holz, Österreich`(address)
- `DLA Piper Weiss-Tessbach Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 48** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden und die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn sowie die fachkundigen Laienrichter Mag. Dr. Monika Lanz und Wolfgang Cadilek als weitere Richter in der Arbeitsrechtssache der klagenden Partei Hon.-Prof. Dieter Kovacs, vertreten durch Pfurtscheller Orgler Huber, Rechtsanwälte in Innsbruck, gegen die beklagte Partei ÖBB-Personenverkehr AG, Monsbergergasse 12, 6210 Astenberg, Österreich, vertreten durch die CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 3.963,75 EUR brutto sA, aus Anlass der (außerordentlichen) Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. Februar 2013, GZ 13 Ra 1/13i-16, mit dem das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 16. Oktober 2012, GZ 42 Cga 87/12h-12, abgeändert wurde, den Beschluss gefasst:  Spruch A.Dem Gerichtshof der Europäischen Union werden folgende Fragen zur Vorabentscheidung vorgelegt: 1.Ist Art 21 der Grundrechtecharta in Verbindung mit Art 7 Abs 1, Art 16 und Art 17 der Richtlinie 2000/78/EG dahin auszulegen, dass a)ein Arbeitnehmer, für den vom Arbeitgeber aufgrund einer gesetzlich normierten altersdiskriminierenden Anrechnung von Vordienstzeiten zunächst ein unrichtiger Vorrückungsstichtag festgesetzt wurde, in jedem Fall Anspruch auf Zahlung der Gehaltsdifferenz unter Zugrundelegung des diskriminierungsfreien Vorrückungsstichtags hat, b)oder aber dahin, dass der Mitgliedstaat die Möglichkeit hat, durch eine diskriminierungsfreie Anrechnung der Vordienstzeiten die Altersdiskriminierung auch ohne finanziellen Ausgleich (durch Neufestsetzung des Vorrückungsstichtags bei gleichzeitiger Verlängerung des Vorrückungszeitraums) zu beseitigen, insbesondere wenn diese entgeltneutrale Lösung die Liquidität des Arbeitgebers aufrechterhalten sowie einen übermäßigen Neuberechnungsaufwand vermeiden soll?

**False Positives:**

- `Personenverkehr AG` — partial — pred is substring of gold: `ÖBB-Personenverkehr AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Spenling`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Brenn`(person)
- `Mag. Dr. Monika Lanz`(person)
- `Wolfgang Cadilek`(person)
- `Hon.-Prof. Dieter Kovacs`(person)
- `Pfurtscheller Orgler Huber, Rechtsanwälte`(organisation)
- `ÖBB-Personenverkehr AG`(organisation)
- `Monsbergergasse 12, 6210 Astenberg, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Innsbruck`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 49** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_62`)


… .“ b) Neue Rechtslage: § 53a des Bundesbahngesetzes, BGBl I 2011/129 lautet: „(1) Für jene Bediensteten und Ruhegenussempfänger, die bis zum 31. Dezember 2004 bei den Österreichischen Bundesbahnen (ÖBB), einem ihrer Rechtsvorgänger oder ab Rechtswirksamkeit der angeordneten Spaltungs- und Umwandlungsvorgänge bei der ÖBB-Holding AG, den im 3.

**False Positives:**

- `Holding AG` — partial — pred is substring of gold: `ÖBB-Holding AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ÖBB`(organisation)
- `ÖBB-Holding AG`(organisation)

**Example 50** (doc_id: `deanon_260716_TRAIN/8ObA60_19k`) (sent_id: `deanon_260716_TRAIN/8ObA60_19k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn sowie die fachkundigen Laienrichter Johannes Püller (aus dem Kreis der Arbeitgeber) und Mag. Michaela Puhm (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden und widerbeklagten Partei KzlR Titus Tielken, vertreten durch Mag. Martin Stärker, Rechtsanwalt in Wien, gegen die beklagte und widerklagende Partei Alwaldnex Bau AG, Ebereschenweg 13, 4616 Bergern, Österreich, vertreten durch Dr. Max Pichler, Rechtsanwalt in Wien, wegen 115.729,26 EUR brutto sA und Feststellung (Streitwert 21.455,46 EUR) (AZ 23 Cga 20/18f) und 3.421,39 EUR sA (AZ 23 Cga 73/18z), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 28. August 2019, GZ 8 Ra 12/19x-19, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Alwaldnex Bau AG` — partial — gold is substring of pred: `Alwaldnex Bau AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Tarmann-Prentner`(person)
- `Mag. Korn`(person)
- `Johannes Püller`(person)
- `Mag. Michaela Puhm`(person)
- `KzlR Titus Tielken`(person)
- `Mag. Martin Stärker`(person)
- `Alwaldnex Bau AG`(organisation)
- `Ebereschenweg 13, 4616 Bergern, Österreich`(address)
- `Dr. Max Pichler`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 51** (doc_id: `deanon_260716_TRAIN/8ObA69_19h`) (sent_id: `deanon_260716_TRAIN/8ObA69_19h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch die Hofrätin Dr. Tarmann-Prentner als Vorsitzende, die Hofrätin Mag. Korn und den Hofrat Dr. Stefula als weitere Richter sowie die fachkundigen Laienrichter Mag. Thomas Stegmüller (aus dem Kreis der Arbeitgeber) und Gerald Fida (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Mag. Ingolf Marszalek, vertreten durch MMag. Dr. Susanne Binder-Novak, Rechtsanwältin in St. Pölten, gegen die beklagte Partei Tal Werklexlem AG, Waizbauerweg 12, 9651 Strajach, Österreich, vertreten durch Dr. Helmut Engelbrecht, Rechtsanwalt in Wien, wegen 14.426 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 26. September 2019, GZ 7 Ra 79/19t-15, in nichtöffentlicher Sitzung Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 2 ASGG, § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Tal Werklexlem AG` — partial — gold is substring of pred: `Tal Werklexlem AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Tarmann-Prentner`(person)
- `Mag. Korn`(person)
- `Dr. Stefula`(person)
- `Mag. Thomas Stegmüller`(person)
- `Gerald Fida`(person)
- `Mag. Ingolf Marszalek`(person)
- `MMag. Dr. Susanne Binder-Novak`(person)
- `Tal Werklexlem AG`(organisation)
- `Waizbauerweg 12, 9651 Strajach, Österreich`(address)
- `Dr. Helmut Engelbrecht`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 52** (doc_id: `deanon_260716_TRAIN/8ObA71_14w`) (sent_id: `deanon_260716_TRAIN/8ObA71_14w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden und durch die Hofrätin Dr. Tarmann-Prentner, den Hofrat Mag. Ziegelbauer, sowie die fachkundigen Laienrichter Mag. Andreas Mörk und Mag. Matthias Schachner als weitere Richter in der Arbeitsrechtssache der klagenden Partei Cynthia Schamel, vertreten durch Forcher-Mayr & Kantner Rechtsanwälte Partnerschaft in Innsbruck, gegen die beklagte Partei Werkglanz-Verlag AG, Blattbühel 46, 9073 Klagenfurt, Österreich, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Feststellung (Streitwert: 21.800 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 30. September 2014, GZ 15 Ra 92/14p-40, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Partei Werkglanz-Verlag AG` — partial — gold is substring of pred: `Werkglanz-Verlag AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Prof. Dr. Spenling`(person)
- `Dr. Tarmann-Prentner`(person)
- `Mag. Ziegelbauer`(person)
- `Mag. Andreas Mörk`(person)
- `Mag. Matthias Schachner`(person)
- `Cynthia Schamel`(person)
- `Forcher-Mayr & Kantner Rechtsanwälte Partnerschaft`(organisation)
- `Werkglanz-Verlag AG`(organisation)
- `Blattbühel 46, 9073 Klagenfurt, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Innsbruck`(organisation)

**Example 53** (doc_id: `deanon_260716_TRAIN/8ObA72_19z`) (sent_id: `deanon_260716_TRAIN/8ObA72_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Wessely-Kristöfel als weitere Richter sowie die fachkundigen Laienrichter Johannes Püller (aus dem Kreis der Arbeitgeber) und Mag. Michael Puhm (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Petra Tschurtschenthaler, vertreten durch Dr. Markus Orgler, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Uthe Getränke AG, Triester Bundesstraße 146, 3452 Trasdorf, Österreich, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 4.200,83 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 17. Oktober 2019, GZ 13 Ra 41/15z-30, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Uthe Getränke AG` — partial — gold is substring of pred: `Uthe Getränke AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Tarmann-Prentner`(person)
- `Mag. Wessely-Kristöfel`(person)
- `Johannes Püller`(person)
- `Mag. Michael Puhm`(person)
- `Petra Tschurtschenthaler`(person)
- `Dr. Markus Orgler`(person)
- `Uthe Getränke AG`(organisation)
- `Triester Bundesstraße 146, 3452 Trasdorf, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Innsbruck`(organisation)

**Example 54** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende, die Hofrätinnen und Hofräte des Obersten Gerichtshofs Dr. Hargassner, Mag. Korn, Dr. Thunhart und MMag. Sloboda als weitere Richter in der Rechtssache der klagenden Partei Lieselotte Mebesius, vertreten durch die Poduschka Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Ahrenhold Druck AG, Brunnbichlweg 19, 3261 Figelsberg, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 22.140,32 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 19. Juni 2019, GZ 2 R 92/19s-21, mit dem der Berufung der klagenden Partei gegen das Urteil des Landesgerichts Linz vom 12. April 2019, GZ 45 Cg 33/18v-17, nicht Folge gegeben wurde, den Beschluss gefasst:  Spruch I. Das mit Beschluss vom 15. April 2020, AZ 9 Ob 61/19i, bis zur Entscheidung des Gerichtshofs der Europäischen Union über den vom Obersten Gerichtshof am 17.

**False Positives:**

- `Partei Ahrenhold Druck AG` — partial — gold is substring of pred: `Ahrenhold Druck AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Fichtenau`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hargassner`(person)
- `Mag. Korn`(person)
- `Dr. Thunhart`(person)
- `MMag. Sloboda`(person)
- `Lieselotte Mebesius`(person)
- `Poduschka Partner Anwaltsgesellschaft mbH`(organisation)
- `Ahrenhold Druck AG`(organisation)
- `Brunnbichlweg 19, 3261 Figelsberg, Österreich`(address)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Linz`(organisation)
- `Obersten Gerichtshof`(organisation)

**Example 55** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_123`)


In einer weiteren Entscheidung in Zusammenhang mit Abschalteinrichtungen, der Rechtssache C-100/21,QBgegenMercedes-Benz Group AG, beantwortet der EuGH die an ihn gestellten Vorlagefragen wie folgt: „1. Art 18 Abs 1, Art 26 Abs 1 und Art 46 der Richtlinie 2007/46/EG in Verbindung mit Art 5 Abs 2 VO 715/2007/EG sind dahin auszulegen, dass sie neben allgemeinen Rechtsgütern die Einzelinteressen des individuellen Käufers eines Kraftfahrzeugs gegenüber dessen Hersteller schützen, wenn dieses Fahrzeug mit einer unzulässigen Abschalteinrichtung im Sinne von Art 5 Abs 2 dieser Verordnung ausgestattet ist.

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_125`)


In seiner Entscheidungsbegründung rekapituliert der EuGH zunächst, dass ein individueller Käufer, der ein Fahrzeug erwirbt, das zur Serie eines genehmigten Fahrzeugtyps gehört und somit mit einer Übereinstimmungsbescheinigung versehen ist, vernünftiger Weise erwarten kann, dass die VO 715/2007/EG und insbesondere deren Art 5 bei diesem Fahrzeug eingehalten werden (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 81 unter Hinweis auf C-145/20,Porsche Inter Auto und Volkswagen, Rn 54).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_127`)


[34] Konkret leitet der EuGH aus den Bestimmungen über die Übereinstimmungsbescheinigung (Art 18 Abs 1 und Art 26 Abs 1 der Rahmen-RL [RL 2007/46/EG des Europäischen Parlaments und des Rates vom 5. 9. 2007 zur Schaffung eines Rahmens für die Genehmigung von Kraftfahrzeugen und Kraftfahrzeuganhängern sowie von Systemen, Bauteilen und selbstständigen technischen Einheiten für diese Fahrzeuge; künftig: RL 2007/46/EG]) ab, dass die Übereinstimmungsbescheinigung „eine unmittelbare Verbindung zwischen dem Automobilhersteller und dem individuellen Käufer eines Kraftfahrzeugs herstellt, mit der diesem gewährleistet werden soll, dass das Fahrzeug mit den maßgeblichen Rechtsvorschriften der Union übereinstimmt“ (C-100/21,QBgegenMercedes-Benz Group AG, Rn 82).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_147`)


Für diesen Schadenersatzanspruch macht der EuGH grundsätzliche Vorgaben, nämlich in dem Sinn, dass die Mitgliedstaaten in einem solchen Fall einen Schadenersatzanspruch zu Gunsten eines Käufers gegenüber dem Hersteller vorzusehen haben, wenn dem Käufer durch diese Abschalteinrichtung ein Schaden entstanden ist (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 91).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_148`)


Dabei handelt es sich um einen im nationalen Recht wurzelnden Schadenersatzanspruch, der am unionsrechtlichen Effektivitätsgrundsatz zu messen ist (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 93), also eine wirksame, verhältnismäßige und abschreckende Sanktion für den Verstoß darstellen muss (vgl EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 90).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation
- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 60** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_149`)


Im Übrigen richten sich die Modalitäten dieses Schadenersatzanspruchs nach nationalem Recht (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 92), hier also unstrittig nach österreichischem Recht.

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_151`)


Eine unionsrechtliche Vorgabe eines Schadenersatzanspruchs ist das Vorliegen eines Schadens: Der EuGH betont, dass dem Käufer eines mit einer unzulässigen Abschalteinrichtung ausgestatteten Fahrzeugs ein Schadenersatzanspruch zusteht, wenn ihm ein Schaden entstanden ist (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 91).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_153`)


Als nachteilige Folge – vor der ein Fahrzeugkäufer durch das Unionsrecht geschützt werden soll – sieht der EuGH an, dass durch die Unzulässigkeit der Abschalteinrichtung die Gültigkeit der EG-Typengenehmigung und daran anschließend die der Übereinstimmungsbescheinigung in Frage gestellt werden, was wiederum (unter anderem) zu einer Unsicherheit über die Nutzungsmöglichkeit (Anmeldung, Verkauf oder Inbetriebnahme des Fahrzeugs) und „letztlich“ zu einem Schaden führen kann (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 84).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_173`)


Ebenso wenig lässt die Feststellung erkennen, ob der Kläger die Notwendigkeit des Software-Updates und die vom EuGH angesprochene Unsicherheit über die Nutzungsmöglichkeit des Fahrzeugs (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 84; vgl zu dieser Unsicherheit auch die mit der Entscheidung des EuGH vom 8.

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_260716_TRAIN/9Ob6_24h`) (sent_id: `deanon_260716_TRAIN/9Ob6_24h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende, die Hofrätinnen und Hofräte des Obersten Gerichtshofs Mag. Ziegelbauer, Dr. Hargassner, Mag. Korn und Dr. Stiefsohn in der Rechtssache der klagenden Partei Jennifer Franckh, vertreten durch Dr. Alexander Amann LL.M., Rechtsanwalt in Gamprin-Bendern, Fürstentum Liechtenstein, gegen die beklagte Partei DrauGarten AG, Wamprechtsham 54, 4926 Untereselbach, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 2.375 EUR und Feststellung (Streitwert: 4.000 EUR), über die Revision der beklagten Partei gegen das Zwischenurteil des Landesgerichts Wels als Berufungsgericht vom 25. Oktober 2023, GZ 22 R 198/23h-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Vöcklabruck vom 15. Juni 2023, GZ 13 C 630/22f-26, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I.Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei DrauGarten AG` — partial — gold is substring of pred: `DrauGarten AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Fichtenau`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Ziegelbauer`(person)
- `Dr. Hargassner`(person)
- `Mag. Korn`(person)
- `Dr. Stiefsohn`(person)
- `Jennifer Franckh`(person)
- `Dr. Alexander Amann LL.M.`(person)
- `DrauGarten AG`(organisation)
- `Wamprechtsham 54, 4926 Untereselbach, Österreich`(address)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`(organisation)
- `Landesgerichts Wels`(organisation)
- `Bezirksgerichts Vöcklabruck`(organisation)

**Example 65** (doc_id: `deanon_260716_TRAIN/9ObA134_09k`) (sent_id: `deanon_260716_TRAIN/9ObA134_09k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsrekursgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten des Obersten Gerichtshofs Dr. Rohrer als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Dr. Hradil und Dr. Hopf als weitere Richter in der Arbeitsrechtssache der klagenden Partei Frederike Geschwind, vertreten durch Dr. Andreas Lintl, Rechtsanwalt in Wien, gegen die beklagte Partei Sudbertri Garten AG, Mauerfeldstraße 26, 8753 Dietersdorf, Österreich, vertreten durch die Winkler Reich-Rohrwig Illedits Rechtsanwälte-Partnerschaft in Wien, wegen Kündigungsanfechtung, über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht in Arbeits- und Sozialrechtssachen vom 14. Oktober 2009, GZ 10 Ra 108/09i-17, womit der Beschluss des Landesgerichts Krems an der Donau als Arbeits- und Sozialgericht vom 13. August 2009, GZ 7 Cga 42/09b-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs der klagenden Partei wird gemäß § 526 Abs 2 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Sudbertri Garten AG` — partial — gold is substring of pred: `Sudbertri Garten AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Rohrer`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hradil`(person)
- `Dr. Hopf`(person)
- `Frederike Geschwind`(person)
- `Dr. Andreas Lintl`(person)
- `Sudbertri Garten AG`(organisation)
- `Mauerfeldstraße 26, 8753 Dietersdorf, Österreich`(address)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Krems an der Donau`(organisation)

**Example 66** (doc_id: `deanon_260716_TRAIN/9ObA41_14s`) (sent_id: `deanon_260716_TRAIN/9ObA41_14s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras, die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Mag. Gerald Fuchs und Peter Schönhofer als weitere Richter in der Arbeitsrechtssache der klagenden Partei Clarissa Bannwarth, vertreten durch Dr. Remo Sacherer, Rechtsanwalt in Wien, gegen die beklagte Partei Garten Bernexdorf AG, Sittestraße 49, 4203 Katzgraben, Österreich, vertreten durch Korn Rechtsanwälte OG in Wien, wegen Kündigungsanfechtung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Februar 2014, GZ 7 Ra 4/14f-29, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Partei Garten Bernexdorf AG` — partial — gold is substring of pred: `Garten Bernexdorf AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hopf`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Dehn`(person)
- `Mag. Gerald Fuchs`(person)
- `Peter Schönhofer`(person)
- `Clarissa Bannwarth`(person)
- `Dr. Remo Sacherer`(person)
- `Garten Bernexdorf AG`(organisation)
- `Sittestraße 49, 4203 Katzgraben, Österreich`(address)
- `Korn Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 67** (doc_id: `deanon_260716_TRAIN/9ObA8_20x`) (sent_id: `deanon_260716_TRAIN/9ObA8_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau und den Hofrat des Obersten Gerichtshofs Dr. Hargassner sowie die fachkundigen Laienrichter Dr. Ingomar Stupar (aus dem Kreis der Arbeitgeber) und Mag. Werner Pletzenauer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Mag. Dr. Hartmut Sperber, vertreten durch Moser Mutz Rechtsanwälte GesbR in Klagenfurt am Wörthersee, gegen die beklagte Partei HASK Software Betriebe AG, Alter Garten 34, 8490 Hummersdorf, Österreich, vertreten durch Wiedenbauer Mutz Winkler & Partner Rechtsanwälte GmbH in Klagenfurt am Wörthersee, wegen Kündigungsanfechtung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 18. Dezember 2019, GZ 7 Ra 70/19x-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei HASK Software Betriebe AG` — partial — gold is substring of pred: `HASK Software Betriebe AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hopf`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Fichtenau`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hargassner`(person)
- `Dr. Ingomar Stupar`(person)
- `Mag. Werner`(person)
- `Mag. Dr. Hartmut Sperber`(person)
- `Moser Mutz Rechtsanwälte GesbR`(organisation)
- `HASK Software Betriebe AG`(organisation)
- `Alter Garten 34, 8490 Hummersdorf, Österreich`(address)
- `Wiedenbauer Mutz Winkler & Partner Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Graz`(organisation)

</details>

---

## `German Federal Court of Finance Acronym` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7244a23f`  
**Description:**
Matches the BFH acronym which was missing from the rules.

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

## `AMS Acronym` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a542dc94`  
**Description:**
Matches the AMS acronym (Arbeitsmarktservice) as an organization.

**Content:**
```
\bAMS\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 1867 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/3Ob222_17v`) (sent_id: `deanon_260716_TRAIN/3Ob222_17v_8`)


Danach meldete er sich beim AMS als arbeitssuchend.

**False Positives:**

- `AMS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Pensionsversicherungsanstalt` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `87469955`  
**Description:**
Matches the full name of the pension insurance institution.

**Content:**
```
\bPensionsversicherungsanstalt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 3500 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Roland Soukup, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Pensionsversicherungsanstalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Dr. Gabriele Griehsel`(person)
- `Dr. Wolfgang Kozak`(person)
- `Roland Soukup`(person)
- `Mahringer Steinwender Bestebner Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Salzburg`(organisation)

</details>

---

## `ÖGK Acronym` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9af25d74`  
**Description:**
Matches the ÖGK (Österreichische Gesundheitskasse) acronym.

**Content:**
```
\b(ÖGK)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Common Legal Acronyms` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `cca48f49`  
**Description:**
Matches only specific, high-confidence legal acronyms (KAG, BMF) and removes generic terms.

**Content:**
```
\b(KAG|BMF)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Company with Fa. Prefix` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1f1eab92`  
**Description:**
Matches companies prefixed with 'Fa.' (Firma), ensuring it captures the full name including potential hyphens.

**Content:**
```
\bFa\.\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+&\s*Co\s*KG)?\s*(?:GmbH(?:\s*&\s*Co\s*KG)?|AG|KG))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `University of Vienna` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `253fe7e4`  
**Description:**
Matches 'Universität Wien' as an organization.

**Content:**
```
\bUniversit\u00e4t\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Federal Ministry of Interior` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c365c2a9`  
**Description:**
Matches the acronym 'BMI' (Bundesministerium für Inneres) in legal contexts.

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

## `Bundesamt für Soziales` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `66f16995`  
**Description:**
Matches the full name of the Federal Office for Social Affairs and Disability.

**Content:**
```
\bBundesamt(?:s)?\s+f\u00fcr\s+Soziales\s+und\s+Behindertenwesen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `OECD` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `491c7ed9`  
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

## `EU Court` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `45a9fba1`  
**Description:**
Matches the Court of Justice of the European Union.

**Content:**
```
\bGerichtshof\s+der\s+Europäischen\s+Union\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 8 | 0 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 8 | 2438 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/1Ob226_20x`) (sent_id: `deanon_260716_TRAIN/1Ob226_20x_51`)


Auch der Gerichtshof der Europäischen Union wies in diesem Zusammenhang darauf hin, dass der Kausalzusammenhang zwischen dem vom Geschädigten geltend gemachten Schaden und dem (unionsrechtlichen) Vergaberechtsverstoß eine Voraussetzung des Ersatzanspruchs ist (vgl EuGH C-568/08,Combinatie Sijker Infrabouwua, Rn 87;

**False Positives:**

- `Gerichtshof der Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/5Ob71_24p`) (sent_id: `deanon_260716_TRAIN/5Ob71_24p_23`)


Das Landgericht Ravensburg (Deutschland) hat dem Gerichtshof der Europäischen Union am 9.

**False Positives:**

- `Gerichtshof der Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_158`)


Was die gerichtliche Nachprüfbarkeit der Einhaltung dieser Voraussetzungen betrifft, billigt der Gerichtshof der Europäischen Union dem Unionsrechtsgesetzgeber im Rahmen der Ausübung der ihm übertragenen Zuständigkeiten ein weites Ermessen in Bereichen zu, in denen seine Tätigkeit sowohl politische als auch wirtschaftliche oder soziale Entscheidungen verlangt und in denen er komplexe Prüfungen und Beurteilungen vornehmen muss.

**False Positives:**

- `Gerichtshof der Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_260716_TRAIN/7Ob201_12b`) (sent_id: `deanon_260716_TRAIN/7Ob201_12b_5`)


Der Antrag der Revisionswerberin, der Oberste Gerichtshof möge ein Vorabentscheidungsersuchen an den Gerichtshof der Europäischen Union stellen, wird zurückgewiesen.

**False Positives:**

- `Gerichtshof der Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden und die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn sowie die fachkundigen Laienrichter Mag. Dr. Monika Lanz und Wolfgang Cadilek als weitere Richter in der Arbeitsrechtssache der klagenden Partei Hon.-Prof. Dieter Kovacs, vertreten durch Pfurtscheller Orgler Huber, Rechtsanwälte in Innsbruck, gegen die beklagte Partei ÖBB-Personenverkehr AG, Monsbergergasse 12, 6210 Astenberg, Österreich, vertreten durch die CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 3.963,75 EUR brutto sA, aus Anlass der (außerordentlichen) Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. Februar 2013, GZ 13 Ra 1/13i-16, mit dem das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 16. Oktober 2012, GZ 42 Cga 87/12h-12, abgeändert wurde, den Beschluss gefasst:  Spruch A.Dem Gerichtshof der Europäischen Union werden folgende Fragen zur Vorabentscheidung vorgelegt: 1.Ist Art 21 der Grundrechtecharta in Verbindung mit Art 7 Abs 1, Art 16 und Art 17 der Richtlinie 2000/78/EG dahin auszulegen, dass a)ein Arbeitnehmer, für den vom Arbeitgeber aufgrund einer gesetzlich normierten altersdiskriminierenden Anrechnung von Vordienstzeiten zunächst ein unrichtiger Vorrückungsstichtag festgesetzt wurde, in jedem Fall Anspruch auf Zahlung der Gehaltsdifferenz unter Zugrundelegung des diskriminierungsfreien Vorrückungsstichtags hat, b)oder aber dahin, dass der Mitgliedstaat die Möglichkeit hat, durch eine diskriminierungsfreie Anrechnung der Vordienstzeiten die Altersdiskriminierung auch ohne finanziellen Ausgleich (durch Neufestsetzung des Vorrückungsstichtags bei gleichzeitiger Verlängerung des Vorrückungszeitraums) zu beseitigen, insbesondere wenn diese entgeltneutrale Lösung die Liquidität des Arbeitgebers aufrechterhalten sowie einen übermäßigen Neuberechnungsaufwand vermeiden soll?

**False Positives:**

- `Gerichtshof der Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Spenling`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Brenn`(person)
- `Mag. Dr. Monika Lanz`(person)
- `Wolfgang Cadilek`(person)
- `Hon.-Prof. Dieter Kovacs`(person)
- `Pfurtscheller Orgler Huber, Rechtsanwälte`(organisation)
- `ÖBB-Personenverkehr AG`(organisation)
- `Monsbergergasse 12, 6210 Astenberg, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Innsbruck`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_133`)


Der Oberste Gerichtshof hat beschlossen, ein Vorabentscheidungsersuchen an den Gerichtshof der Europäischen Union zu stellen.

**False Positives:**

- `Gerichtshof der Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_141`)


Der Oberste Gerichtshof würde es begrüßen, wenn der Gerichtshof der Europäischen Union über das vorliegende Vorabentscheidungsersuchen und über die Vorlage des Oberlandesgerichts Innsbruck gemeinsam entscheiden würde.

**False Positives:**

- `Gerichtshof der Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Oberlandesgerichts Innsbruck`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/9Ob68_22y`) (sent_id: `deanon_260716_TRAIN/9Ob68_22y_148`)


3. 2020 legte der Oberste Gerichtshof zu 10 Ob 44/19x dem Gerichtshof der Europäischen Union gemäß Art 267 AEUV folgende Fragen zur Vorabentscheidung vor: 2.1.„1.

**False Positives:**

- `Gerichtshof der Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

</details>

---

## `Landespolizeidirektion Generic` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `506db2e2`  
**Description:**
Matches 'Landespolizeidirektion' followed by an optional state name or a single letter/identifier (e.g., 'X'), capturing the full entity.

**Content:**
```
\bLandespolizeidirektion(?:\s+(?:Burgenland|K\u00e4rnten|Nieder\u00f6sterreich|Ober\u00f6sterreich|Salzburg|Steiermark|Tirol|Vorarlberg|Wien|[A-Z]))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 3460 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/11Os59_13f`) (sent_id: `deanon_260716_TRAIN/11Os59_13f_22`)


Dass die Pistole im Abschlussbericht der Landespolizeidirektion Niederösterreich einmal als Luftdruckpistole (ON 4 S 11) und einmal als Faustfeuerwaffe (ON 4 S 9) bezeichnet wird, bedurfte keiner Erörterung in den Urteilsgründen (Z 5 zweiter Fall), weil es sich in beiden Fällen jedenfalls um eine (Schuss-)Waffe im Sinn der §§ 2, 3 WaffG handelt. Die Rechtsrüge (Z 10) vermisst Feststellungen „hinsichtlich Merkmalen und Eigenschaften dieser Luftdruckpistole“, unterlässt es aber, vorzubringen, weshalb die Konstatierungen, wonach es sich bei der Waffe um eine Luftdruckpistole, Marke Webley Stinger, 4,5 mm, mit der feste Geschosse verschossen werden, und demnach um keine Spielzeugpistole handelte (US 2, 6), zur rechtlichen Beurteilung nicht ausreichen sollten.

**False Positives:**

- `Landespolizeidirektion Niederösterreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Verwaltungsgericht City` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4b3b3e5d`  
**Description:**
Matches 'Verwaltungsgericht' followed by a city name, capturing the full entity.

**Content:**
```
\bVerwaltungsgericht\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 2440 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/1Ob226_20x`) (sent_id: `deanon_260716_TRAIN/1Ob226_20x_13`)


Da keines der Angebote – also auch nicht jenes der Klägerin – den Anforderungen der Ausschreibung entsprach, widerrief die Beklagte die Ausschreibung, was von der Klägerin vor dem Verwaltungsgericht Wien erfolglos bekämpft wurde.

**False Positives:**

- `Verwaltungsgericht Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/1Ob226_20x`) (sent_id: `deanon_260716_TRAIN/1Ob226_20x_16`)


Das von ihr (neuerlich) angerufene Verwaltungsgericht Wien stellte (in zwei Verfahren, die jeweils unterschiedliche Zeiträume betrafen) rechtskräftig fest, dass diese Vorgehensweise rechtswidrig war.

**False Positives:**

- `Verwaltungsgericht Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `FAÖ Acronym` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `655e9fee`  
**Description:**
Matches the 'FAÖ' acronym (Finanzamt Österreich) which was missing from the rules.

**Content:**
```
\bFA\u00d6\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesamtes für Soziales` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a80e7e1d`  
**Description:**
Matches the full name 'Bundesamtes für Soziales und Behindertenwesen' which was missing from the rules.

**Content:**
```
\bBundesamtes\s+f\u00fcr\s+Soziales\s+und\s+Behindertenwesen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `COFAG Acronym` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `21c54737`  
**Description:**
Matches the COFAG acronym as an organization, strictly excluding hyphenated compounds.

**Content:**
```
\bCOFAG\b(?!-)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BHAG Acronym` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f4ec9a56`  
**Description:**
Matches the BHAG acronym as an organization.

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

## `BM für Finanzen` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8ae78160`  
**Description:**
Matches 'BM für Finanzen' as an organization.

**Content:**
```
\bBM\s+f\u00fcr\s+Finanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `I AG Acronym` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `88dcc232`  
**Description:**
Matches 'I AG' as a standalone organization entity.

**Content:**
```
\bI\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wiener Gemeinderates` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b4490704`  
**Description:**
Matches 'Wiener Gemeinderates' as an organization.

**Content:**
```
\bWiener\s+Gemeinderates\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesministeriums für Finanzen` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a96d2238`  
**Description:**
Matches 'Bundesministeriums für Finanzen' (genitive) as an organization.

**Content:**
```
\bBundesministeriums\s+f\u00fcr\s+Finanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesministers für Arbeit` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `56dd640c`  
**Description:**
Matches 'Bundesministers für Arbeit, Soziales und Konsumentenschutz' as an organization.

**Content:**
```
\bBundesministers\s+f\u00fcr\s+Arbeit,?\s*Soziales\s+und\s+Konsumentenschutz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Names` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a736d867`  
**Description:**
Matches known specific company names including complex structures, ensuring 'Kraftost-Digital AG', 'Post AG', 'KPMG Alpen-Treuhand GmbH', 'Moser Rechtsanwalts-GmbH,' are captured.

**Content:**
```
\b(?:Kraftost-Digital\s+AG|Post\s+AG|Novotny\s+Getr\u00e4nke\s+GmbH|Hellfritsch\s+Immobilien\s+GmbH|xx\s+GmbH\s+Steuerberatung\s+und\s+Wirtschaftspr\u00fcfung|Versand\s+Seewil|Bruckdon-Cloud|yy\s+Wirtschaftstreuhand\s+Gesellschaft\s+mbH|Kantner\s+Wirtschaftstreuhand\s+und\s+Steuerberatungs\s+GmbH|GOBBS\s+Steuerberatungs\s+GmbH|Ernst\s+&\s+Young\s+Steuerberatungsgesellschaft\s+m\.b\.H\.?|Heinz\s+Neub\u00f6ck\s+Wirtschaftstreuhand\s+Gesellschaft\s+m\.b\.H\.?|BDO\s+Assurance\s+GmbH\s+Wirtschaftspr\u00fcfungs-\s+und\s+Steuerberatungsgesellschaft|Deutsche\s+Telekom\s+AG|Deutschen\s+Telekom\s+AG|SK\s+Telecom\s+Co\.\s+Ltd|T-Mobile\s+Austria\s+GmbH|A1\s+Telekom\s+Austria\s+AG|Hutchinson\s+Drei\s+Austria\s+GmbH|Bonafide\s+Treuhand\s+&\s+Revisions\s+GmbH|SNWG\s+Textil\s+GmbH|KPMG\s+Alpen-Treuhand\s+GmbH\s+Wirtschaftspr\u00fcfungs-\s+und\s+Steuerberatungsgesellschaft|Moser\s+Rechtsanwalts-GmbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `SK Telecom Specific` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c72da337`  
**Description:**
Matches 'SK Telecom' specifically, handling optional 'Co Ltd' suffix without capturing it, ensuring the full name is extracted.

**Content:**
```
\bSK\s+Telecom(?:\s+Co\.?\s+Ltd)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesfinanzgerichts Genitive` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `61fba8f1`  
**Description:**
Matches 'Bundesfinanzgerichts' (genitive form) which is often missed by the standard court rule. This is now redundant with the updated 'Specific Court Names' rule but kept for explicit priority if needed, or can be removed if the main rule covers it. Given the main rule now includes 'es|s', this specific rule is redundant and will be deleted.

**Content:**
```
\bBundesfinanzgerichts\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Amt für Betrugsbekämpfung` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2a60dccd`  
**Description:**
Matches the specific anti-fraud authority 'Amt für Betrugsbekämpfung' in any case or with genitive endings, capturing the full entity name.

**Content:**
```
\b(?:Amt|Amtes|Ämter|Ämtern)\s+f\u00fcr\s+Betrugsbek\u00e4mpfung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt für Großbetriebe` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `911075f1`  
**Description:**
Matches 'Finanzamt für Großbetriebe' as a specific organization entity.

**Content:**
```
\bFinanzamt\s+f\u00fcr\s+Gro\u00dfbetriebe\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Landesgericht with City` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `11fb1c29`  
**Description:**
Matches 'Landesgericht' or 'Landesgerichts' followed by a city name or identifier, capturing the full entity.

**Content:**
```
\bLandesgericht(?:es)?\s+[A-Z]\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Alpen-KI GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `268b0b28`  
**Description:**
Matches specific company names like 'Alpen-KI GmbH' which were missed by generic patterns.

**Content:**
```
\bAlpen-KI\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Treuhand-Union Villach` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9c1516d7`  
**Description:**
Matches specific company names like 'Treuhand-Union Villach Wirtschafts- treuhand- und Steuerberatungs GmbH'.

**Content:**
```
\bTreuhand-Union\s+Villach\s+Wirtschafts-\s+treuhand-\s+und\s+Steuerberatungs\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Court Names` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3346282c`  
**Description:**
Matches specific court names including genitive forms and the '(BFG)' suffix. Fixed to capture 'Landesgerichts' followed by a city name.

**Content:**
```
\b(Bundesfinanzgericht(?:es|s)?(?:\s*\(BFG\))?|Verwaltungsgerichtshof(?:es|s)?|Verfassungsgerichtshof(?:es|s)?|Landesgericht(?:es|s)\s+[A-Z][a-z]+)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FB + KG Acronym` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `bcb27140`  
**Description:**
Matches company names with '+' in the middle followed by 'KG', such as 'FB + KG', to capture the full entity.

**Content:**
```
\bFB\s*\+\s*KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Magistrat der Stadt` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `daee2831`  
**Description:**
Matches 'Magistrat' or 'Magistrats' followed by 'der Stadt' and city name, explicitly excluding trailing department info like 'Magistratsabteilung'.

**Content:**
```
\bMagistrat(?:s)?\s+der\s+Stadt\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Frontex Acronym` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6b1d2f2d`  
**Description:**
Matches the 'Frontex' organization acronym which was missing from the rules.

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

## `Bundesministerium für Finanzen` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b79f419f`  
**Description:**
Matches the full name 'Bundesministerium für Finanzen' including genitive forms.

**Content:**
```
\bBundesministeriums?\s+für\s+Finanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wiener Linien` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `accfe7aa`  
**Description:**
Matches the specific organization 'Wiener Linien'.

**Content:**
```
\bWiener\s+Linien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wiener Gemeindebezirk` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0d7fee8d`  
**Description:**
Matches 'Wiener Gemeindebezirk' as an organization entity.

**Content:**
```
\bWiener\s+Gemeindebezirk(?:s)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 756 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/7Ob92_19h`) (sent_id: `deanon_260716_TRAIN/7Ob92_19h_212`)


Wiener Gemeindebezirk nicht ohne weiteres gleichwertig ist.

**False Positives:**

- `Wiener Gemeindebezirk` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Rentenversicherung Bund` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `74dd07db`  
**Description:**
Matches 'Rentenversicherung Bund' as a specific organization entity.

**Content:**
```
\bRentenversicherung\s+Bund\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Deutschen Rentenversicherung Bund` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7a7eeb69`  
**Description:**
Matches 'Deutschen Rentenversicherung Bund' to capture the full genitive form of the pension insurance organization.

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

## `WGKK Acronym` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ea9c0e11`  
**Description:**
Matches the 'WGKK' acronym (Wiener Gebietskrankenkasse) as an organization.

**Content:**
```
\bWGKK\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesministerium für Inneres` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b31004b7`  
**Description:**
Matches the full name 'Bundesministerium für Inneres' as an organization.

**Content:**
```
\bBundesministerium\s+f\u00fcr\s+Inneres\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Mur Steinstein Specific` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `08559a06`  
**Description:**
Matches the specific entity 'Mur Steinstein' which was missed or incorrectly captured as part of a GmbH pattern. Ensures it captures the name even if followed by 'GmbH' in some contexts, but prioritizes the standalone name if that is the intended entity.

**Content:**
```
\bMur\s+Steinstein\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Stadt Wien Partial` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `dbd5feb1`  
**Description:**
Matches 'Stadt Wien' as an organization entity when it appears as a standalone reference or part of a larger context, ensuring it is captured even if not preceded by 'Magistrat'.

**Content:**
```
\bStadt\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 24 | 0 | 24 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 24 | 3622 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Ziegelbauer als Vorsitzenden sowie die Hofrätin Dr. Faber und die Hofräte Mag. Schober, Dr. Thunhart und Dr. Annerl als weitere Richter in der Pflegschaftssache der minderjährigen Meinrad Bruhnsen, geboren 30. Januar 2006, vertreten durch das Land Wien als Träger der Kinder- und Jugendhilfe (Magistrat der Stadt Wien, Rechtsvertretung Bezirke 1, 4 bis 9, 1060 Wien, Amerlingstraße 11), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch die Präsidentin des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 31. Oktober 2022, GZ 43 R 323/22a-17, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 9. Juni 2022, GZ 4 Pu 58/22a-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Stadt Wien` — similar text (different position): `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Mag. Schober`(person)
- `Dr. Thunhart`(person)
- `Dr. Annerl`(person)
- `Meinrad Bruhnsen`(person)
- `30. Januar`(date)
- `Magistrat der Stadt Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_6`)


Mit einstweiliger Verfügung des Bezirksgerichts Innere Stadt Wien vom 28. April 2022 wurde der Vater verpflichtet, dem Kind einen vorläufigen monatlichen Unterhaltsbeitrag in Höhe von 38 EUR zu leisten (ON 2).

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob57_13z`) (sent_id: `deanon_260716_TRAIN/10Ob57_13z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der Kinder Mikolaj Eleftheriadou, geboren am 9. August 1991, Helge Schuchmann, geboren am 30. September 1992, mj Isabel Rahnfeld, geboren am 22. Dezember 1998 und mj PhD Daniel Coutand, geboren am 18. Jänner 2001, wegen Unterhaltsvorschuss, infolge Revisionsrekurses des Vaters Mag. Dirk Hükelheim, vertreten durch Mag. Roland Marko, Rechtsanwalt in Wien, dieser vertreten durch Dr. Francisco Rumpf, Rechtsanwalt in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 7. Juni 2013, GZ 43 R 391/08f ua -U-458, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 12. November 2007, GZ 2 P 88/07t-U-238, abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Mikolaj Eleftheriadou`(person)
- `Helge Schuchmann`(person)
- `Isabel Rahnfeld`(person)
- `PhD Daniel Coutand`(person)
- `Mag. Dirk Hükelheim`(person)
- `Mag. Roland Marko`(person)
- `Dr. Francisco Rumpf`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_3`)


Kopf Der Oberste Gerichtshof hat am 14. August 2014 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, die Hofräte des Obersten Gerichtshofs Dr. Lässig, Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Anscheringer als Schriftführer in der Strafsache gegen Natascha von Bohr wegen Vergehen des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 erster und zweiter Fall, Abs 2 SMG in dem zu AZ 18 U 198/14k des Bezirksgerichts Innere Stadt Wien und AZ 18 U 266/14m des Bezirksgerichts Linz zwischen diesen Gerichten geführten Zuständigkeitsstreit den Beschluss gefasst:  Spruch Das Hauptverfahren ist vom Bezirksgericht Linz zu führen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Lässig`(person)
- `Dr. Nordmeyer`(person)
- `Dr. Oshidari`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Mann`(person)
- `Mag. Anscheringer`(person)
- `Natascha von Bohr`(person)
- `Bezirksgerichts Innere Stadt Wien`(organisation)
- `Bezirksgerichts Linz`(organisation)
- `Bezirksgericht Linz`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__3`)


Kopf Der Oberste Gerichtshof hat am 26. Februar 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Schriftführers Dr. Schöll in der Strafsache gegen Robert Ultsch wegen des Vergehens der Urkundenfälschung nach § 223 Abs 1 StGB und einer weiteren strafbaren Handlung, AZ 13 U 351/18d des Bezirksgerichts Innere Stadt Wien, über den auf den Beschluss des Landesgerichts für Strafsachen Wien als Berufungsgericht vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), bezogenen Antrag der Generalprokuratur auf außerordentliche Wiederaufnahme des Verfahrens und über ihre gegen den Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30 der U-Akten) zur Wahrung des Gesetzes erhobene Nichtigkeitsbeschwerde nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Schneider, zu Recht erkannt:  Spruch

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`
- `Stadt Wien` — similar text (different position): `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Lässig`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Mag. Michel`(person)
- `Dr. Oberressl`(person)
- `Dr. Brenner`(person)
- `Dr. Schöll`(person)
- `Robert Ultsch`(person)
- `Bezirksgerichts Innere Stadt Wien`(organisation)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)
- `Mag. Schneider`(person)

**Example 5** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__5`)


In Stattgebung des Antrags der Generalprokuratur wird im außerordentlichen Weg die Wiederaufnahme des Berufungsverfahrens verfügt, der Beschluss des Landesgerichts für Strafsachen Wien vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), aufgehoben und die Sache zur neuerlichen Entscheidung über die Berufung des Angeklagten gegen das Urteil des Bezirksgerichts Innere Stadt Wien vom 27. November 2018 (ON 19 der U-Akten) an das Landesgericht für Strafsachen Wien verwiesen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Strafsachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__6`)


2. Der Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30 der U-Akten) verletzt §§ 270 Abs 3, 271 Abs 7 StPO iVm §§ 447, 458 zweiter Satz StPO.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__7`)


Text Gründe: Mit Urteil des Bezirksgerichts Innere Stadt Wien (ON 19) wurde Robert Ulrici jeweils eines Vergehens der Urkundenfälschung nach § 223 Abs 1 StGB und der Verletzung der Unterhaltspflicht nach § 198 Abs 1 StGB schuldig erkannt und hiefür zu einer bedingt nachgesehenen Freiheitsstrafe verurteilt. Nach Verkündung des Urteils und erteilter Rechtsmittelbelehrung erklärte der – nicht durch einen Verteidiger vertretene (vgl § 57 Abs 2 dritter Satz StPO;Fabrizy, StPO13§ 57 Rz 10) – Angeklagte zunächst, auf Rechtsmittel zu verzichten (ON 18 S 5).

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innere Stadt Wien`(organisation)
- `Robert Ulrici`(person)

**Example 8** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__13`)


Mit Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30) wurden sowohl das Protokoll über die Hauptverhandlung (ON 18) als auch die Urteilsurschrift (ON 19) in Ansehung des „Verhandlungsdatum[s]“ von „23. 11. 2018“ auf „27. 11. 2018“ berichtigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__14`)


Rechtliche Beurteilung Wie die Generalprokuratur in ihrem Antrag auf außerordentliche Wiederaufnahme des Verfahrens zutreffend darlegt, bestehen gegen die Richtigkeit der dem Beschluss des Landesgerichts für Strafsachen Wien als Berufungsgericht vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23), zugrunde gelegten Tatsache, das erstinstanzliche Urteil sei am 23. November 2018 verkündet worden, erhebliche Bedenken: Die Verfügung des Bezirksgerichts Innere Stadt Wien vom 1. November 2018 auf Ladung des Angeklagten zur Hauptverhandlung am 27. November 2018 (ON 1 [unjournalisiert] S 6), das auf der letzten Seite der Urteilsurschrift angeführte Urteilsdatum „27. November 2018“ (ON 19 S 5), die im Verfahrensakt enthaltene (unjournalisierte) Äußerung der Staatsanwaltschaft Wien vom 15. November 2019, AZ 126 BAZ 822/11s, sowie der Berichtigungsbeschluss vom 4. Dezember 2019 (ON 30) legen qualifiziert nahe, dass das Urteil am27. November 2018verkündet wurde.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Strafsachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__18`)


Ebenso zutreffend führt die Generalprokuratur in ihrer zur Wahrung des Gesetzes erhobenen Nichtigkeitsbeschwerde aus, dass der Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30) in zweierlei Hinsicht das Gesetz verletzt: Die Ausfertigung der Urteilsurschrift mit unrichtigem Datum bewirkt ein – nicht die im § 260 Abs 1 Z 1 bis Z 3 und Abs 2 StPO erwähnten Punkte betreffendes – Formgebrechen, das (hier) der Richter des Bezirksgerichts allenfalls nach Anhörung der Beteiligten zu berichtigen hat (§ 270 Abs 3 erster Satz StPO iVm §§ 447, 458 zweiter Satz StPO;

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/1Ob61_18d`) (sent_id: `deanon_260716_TRAIN/1Ob61_18d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Johanna Moehrlin, vertreten durch Dr. Georg Kahlig und Mag. Gerhard Stauder, Rechtsanwälte in Wien, gegen die beklagte Partei DI Camilla Willoweit, vertreten durch Dr. Reinhard Schäfer, Rechtsanwalt in Wien, wegen Unterhalts, über die „außerordentliche“ Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 1. März 2018, GZ 45 R 517/17p-75, mit dem das Urteil des Bezirksgerichts Innere Stadt Wien vom 19. September 2017, GZ 4 C 50/14g-68, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.  Text Begründung: Das Erstgericht sprach der Klägerin rückständigen nachehelichen Unterhalt in Höhe von 24.081,48 EUR sA zu. Das Berufungsgericht gab der Berufung des Beklagten nicht Folge und bestätigte dieses Urteil.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Johanna Moehrlin`(person)
- `Dr. Georg Kahlig`(person)
- `Mag. Gerhard Stauder`(person)
- `DI Camilla Willoweit`(person)
- `Dr. Reinhard Schäfer`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/1Ob78_22k`) (sent_id: `deanon_260716_TRAIN/1Ob78_22k_5`)


Ihre Ehe wurde mit Urteil des Bezirksgerichts Innere Stadt Wien vom 24.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/3Ob114_14g`) (sent_id: `deanon_260716_TRAIN/3Ob114_14g_4`)


Silvana Roellgen, MBA KG und 2. Dr. Nancy Achatzy, vertreten durch die erstklagende Partei, wider die beklagte Partei Dr. Theodora Jungverdorben, vertreten durch BMA Brandstätter Rechtsanwälte GmbH in Wien, wegen Einwendungen gegen den Anspruch (§ 35 EO), über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 30. April 2014, GZ 46 R 135/13p-43, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Innere Stadt Wien vom 30. Jänner 2013, GZ 75 C 17/11x-37, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Silvana Roellgen, MBA`(person)
- `Dr. Nancy Achatzy`(person)
- `Dr. Theodora Jungverdorben`(person)
- `BMA Brandstätter Rechtsanwälte GmbH`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/3Ob185_22k`) (sent_id: `deanon_260716_TRAIN/3Ob185_22k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn und die Hofrätinnen Dr. Weixelbraun-Mohr, Dr. Kodek und Mag. Wessely-Kristöfel als weitere Richter in der Exekutionssache der betreibenden Partei Dr. Moritz Absmeier, vertreten durch Dr. Martin Neuwirth, Dr. Alexander Neurauter, Rechtsanwälte in Wien, gegen die verpflichtete Partei DENU Immobilien GmbH, Gürtel 12, 5145 Schmalzhofen, Österreich, vertreten durch Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH in Wien, wegen zwangsweiser Räumung, über den Revisionsrekurs der betreibenden Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 12. August 2022, GZ 40 R 104/22y-20, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 8. April 2022, GZ 49 E 11/22w-3, abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Hon.-Prof. Dr. Brenn`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Mag. Wessely-Kristöfel`(person)
- `Dr. Moritz Absmeier`(person)
- `Dr. Martin Neuwirth`(person)
- `Dr. Alexander Neurauter`(person)
- `DENU Immobilien GmbH`(organisation)
- `Gürtel 12, 5145 Schmalzhofen, Österreich`(address)
- `Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/5Ob106_20d`) (sent_id: `deanon_260716_TRAIN/5Ob106_20d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer, Mag. Painsi und Dr. Steger als weitere Richter in der Pflegschaftssache der mj Mathilda Dirichs, und Gregor Frysch, beide vorläufig in Obsorge der Mutter Melissa Noßmann, vertreten durch Mag. Wolfgang Doppelhofer, Rechtsanwalt in Wien, über den außerordentlichen Revisionsrekurs des Vaters Olaf Fleischhaker, vertreten durch Dr. Marco Nademleinsky, Rechtsanwalt in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 22. April 2020, GZ 42 R 466/19v-138, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 14. Oktober 2019, GZ 79 Ps 97/16d-121, bestätigt wurde, den Beschluss gefasst:  Spruch Dem außerordentlichen Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Jensik`(person)
- `Dr. Grohmann`(person)
- `Mag. Wurzer`(person)
- `Mag. Painsi`(person)
- `Dr. Steger`(person)
- `Mathilda Dirichs`(person)
- `Gregor Frysch`(person)
- `Melissa Noßmann`(person)
- `Mag. Wolfgang Doppelhofer`(person)
- `Olaf Fleischhaker`(person)
- `Dr. Marco Nademleinsky`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/5Ob152_12g`) (sent_id: `deanon_260716_TRAIN/5Ob152_12g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden, die Hofrätinnen Dr. Hurch und Dr. Lovrek sowie die Hofräte Dr. Höllwerth und Mag. Wurzer als weitere Richter in der Pflegschaftssache der minderjährigen Volker Staybl, geboren am 8. März 1994, wegen Obsorge, über den Revisionsrekurs der Mutter Ing. Adriana Kravchenko, vertreten durch Mag. Klaus Kabelka, Rechtsanwalt in Wien, über den Revisionsrekurs der Mutter gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 23. Mai 2012, GZ 42 R 195/12f-96, mit dem infolge Rekurses der Mutter der Beschluss des Bezirksgerichts Innere Stadt Wien vom 15. März 2012, GZ 59 Ps 21/10x-90, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Danzl`(person)
- `Dr. Hurch`(person)
- `Dr. Lovrek`(person)
- `Dr. Höllwerth`(person)
- `Mag. Wurzer`(person)
- `Volker Staybl`(person)
- `8. März 1994`(date)
- `Ing. Adriana Kravchenko`(person)
- `Mag. Klaus Kabelka`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/6Ob182_20p`) (sent_id: `deanon_260716_TRAIN/6Ob182_20p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden und die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des Minderjährigen ÖkR Techn R Mag.a Helge Cigan, geboren am 13. Dezember 2007, 3. September 1976, vertreten durch das Land Wien (Stadt Wien Kinder- und Jugendhilfe Rechtsvertretung Bezirk 22, 1220 Wien, Simone-de-Beauvoir-Platz 6) als Kinder- und Jugendhilfeträger, über den Revisionsrekurs des Vaters Quentin Martschinke, vertreten durch Anwaltssocietät Sattlegger Dorninger Steiner & Partner in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 25. Juni 2020, GZ 43 R 237/20a-31, mit dem der Beschluss des Bezirksgerichts Donaustadt vom 21. April 2020, GZ 1 P 135/18y-22, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wirdzurückgewiesen.

**False Positives:**

- `Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schramm`(person)
- `Hon.-Prof. Dr. Gitschthaler`(person)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. Nowotny`(person)
- `Dr. Faber`(person)
- `ÖkR Techn R Mag.a Helge Cigan`(person)
- `13. Dezember`(date)
- `3. September 1976`(date)
- `Quentin Martschinke`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Donaustadt`(organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/7Ob138_16v`) (sent_id: `deanon_260716_TRAIN/7Ob138_16v_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Höllwerth als Vorsitzenden und durch die Hofräte Mag. Wurzer, Mag. Malesich, Dr. Hofer-Zeni-Rennhofer und Dr. Singer als weitere Richter in der Rechtssache der gefährdeten Partei Theobald Schomäker, vertreten durch Suppan & Spiegl Rechtsanwälte GmbH in Wien, gegen den Gegner der gefährdeten Partei Berthold Hömann, vertreten durch Dr. Paul Luiki, Rechtsanwalt in Wien, dieser vertreten durch Dr. Romana Zeh-Gindl, Rechtsanwältin in Wien, wegen Erlassung einer einstweiligen Verfügung, infolge des außerordentlichen Revisionsrekurses des Gegners der gefährdeten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 30. Mai 2016, GZ 46 R 177/16v-26, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 19. Jänner 2016, GZ 26 C 1563/15w-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Akten werden dem Rekursgericht zur Ergänzung seiner Entscheidung durch den Ausspruch über den Wert seines Entscheidungsgegenstands übermittelt.  Text Begründung: Das Erstgericht erließ die nach § 382g EO beantragte einstweilige Verfügung zur Sicherung der auf §§ 16, 1328a ABGB und § 1330 ABGB gestützten Unterlassungsansprüche.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Höllwerth`(person)
- `Mag. Wurzer`(person)
- `Mag. Malesich`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Singer`(person)
- `Theobald Schomäker`(person)
- `Suppan & Spiegl Rechtsanwälte GmbH`(organisation)
- `Berthold Hömann`(person)
- `Dr. Paul Luiki`(person)
- `Dr. Romana Zeh-Gindl`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/7Ob180_16w`) (sent_id: `deanon_260716_TRAIN/7Ob180_16w_4`)


Dr. Anabel Heimboeckel, vertreten durch Rechtsanwälte Dr. Amhof & Dr. Damian GmbH in Wien, gegen die beklagte Partei Dominik Westerberger, vertreten durch Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG in Wien, wegen Ehescheidung, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 22. Juni 2016, GZ 42 R 130/16b-33, womit das Urteil des Bezirksgerichts Innere Stadt Wien vom 30. Dezember 2015, GZ 3 C 9/14w-27, bestätigt wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Anabel Heimboeckel`(person)
- `Rechtsanwälte Dr. Amhof & Dr. Damian GmbH`(organisation)
- `Dominik Westerberger`(person)
- `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/8Ob163_09t`) (sent_id: `deanon_260716_TRAIN/8Ob163_09t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsrekursgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner und die Hofräte Mag. Ziegelbauer und Dr. Brenn als weitere Richter in der Pflegschaftssache der mj OMedR Roderich Pruvot, geboren am 9. Februar 1955, und der mj Konrad Michailidis, geboren am 29. September 2000, beide wohnhaft bei ihrer Mutter Ing. KzlR Tatjana Pumpmeyer, über den außerordentlichen Revisionsrekurs des Vaters Vitus Welfle, geboren am 9. Dezember 2009, vertreten durch Mag. Theresia Brunhölzl, Rechtsanwältin in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 7. Juli 2009, GZ 42 R 210/09g-S-93, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 23. März 2009, GZ 88 P 65/08v-81b, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen (§ 71 Abs 3 AußStrG).

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Spenling`(person)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Tarmann-Prentner`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Brenn`(person)
- `OMedR Roderich Pruvot`(person)
- `9. Februar 1955`(date)
- `Konrad Michailidis`(person)
- `29. September 2000`(date)
- `Ing. KzlR Tatjana Pumpmeyer`(person)
- `Vitus Welfle`(person)
- `9. Dezember 2009`(date)
- `Mag. Theresia Brunhölzl`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/8Ob163_09t`) (sent_id: `deanon_260716_TRAIN/8Ob163_09t_5`)


Mit Beschluss des Bezirksgerichts Innere Stadt Wien vom 16. Mai 2006, GZ 9 C 58/06z-20, wurde die Ehe der Eltern einvernehmlich geschieden.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/8Ob163_09t`) (sent_id: `deanon_260716_TRAIN/8Ob163_09t_9`)


Mit einstweiliger Verfügung des Bezirksgerichts Innere Stadt Wien vom 8. Juni 2009 (ON S-91), also nach der Entscheidung des Erstgerichts, wurde dem Vater der Aufenthalt an näher bezeichneten Orten im Nahbereich der Mutter sowie der Kinder sowie das Zusammentreffen und die Kontaktaufnahme mit diesen untersagt, nachdem er anlässlich eines zufälligen Zusammentreffens am 13. Mai 2009 in Anwesenheit der Kinder die Mutter beschimpfte und bedrohte und deren neuen Ehegatten, der sie beschützen wollte, durch Würgen und einen Faustschlag ins Gesicht verletzte.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Bezirksgerichts Innere Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innere Stadt Wien`(organisation)

</details>

---

## `Wirtschaftsuniversität Wien` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `65845b0f`  
**Description:**
Matches the specific organization 'Wirtschaftsuniversität Wien' which was missing from the rules.

**Content:**
```
\bWirtschaftsuniversit\u00e4t\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `AGL Specific Entity` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e46497b2`  
**Description:**
Matches the specific entity 'AGL Wirtschaftstreuhand und Steuerberatungs GmbH' which was previously missed or partially captured.

**Content:**
```
\bAGL\s+Wirtschaftstreuhand\s+und\s+Steuerberatungs\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Verlag Derkel GmbH Specific` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `86657b24`  
**Description:**
Matches the specific company name 'Verlag Derkel GmbH' which was frequently missed or partially captured.

**Content:**
```
\bVerlag\s+Derkel\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Verwiltal-Pharma GmbH Specific` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `17c9f803`  
**Description:**
Matches the specific hyphenated company name 'Verwiltal-Pharma GmbH'.

**Content:**
```
\bVerwiltal-Pharma\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Central Liaison Office` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a8202412`  
**Description:**
Matches the specific organization 'Central Liaison Office' which was missing from the rules.

**Content:**
```
\bCentral\s+Liaison\s+Office\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Europäische Gerichtshof` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4f5e3e0b`  
**Description:**
Matches the specific organization 'Europäische Gerichtshof' which was missing from the rules.

**Content:**
```
\bEurop\u00e4ische\s+Gerichtshof\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 275 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/9Ob68_22y`) (sent_id: `deanon_260716_TRAIN/9Ob68_22y_151`)


3. Ist Art 3 Abs 6 der Richtlinie 1999/44/EG dahin auszulegen, dass eine Vertragswidrigkeit, die in der Ausstattung eines Fahrzeugs mit einer nach Art 3 Z 10 in Verbindung mit Art 5 Abs 2 VO (EG) 715/2007 unzulässigen Abschalteinrichtung liegt, dann als geringfügig im Sinn der genannten Bestimmung zu qualifizieren ist, wenn der Übernehmer das Fahrzeug in Kenntnis ihres Vorhandenseins und ihrer Wirkungsweise dennoch erworben hätte?“ [24]2.2.Mit Urteil vom 14. 7. 2022, C-145/20,Porsche Inter Auto und Volkswagen, hat der Europäische Gerichtshof die ihm gestellten Fragen wie folgt beantwortet: „1.Art. 2 Abs. 2 Buchst.

**False Positives:**

- `Europäische Gerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/9Ob68_22y`) (sent_id: `deanon_260716_TRAIN/9Ob68_22y_214`)


I.C.3.7.Der Europäische Gerichtshof hat darüber hinaus klargestellt, dass – ungeachtet des Vorliegens der in Art 5 Abs 2 Satz 2 lit a VO 715/2007/EU normierten Voraussetzungen – eine Abschalteinrichtung, die unter normalen Betriebsbedingungen den überwiegenden Teil des Jahres funktionieren müsste, damit der Motor vor Beschädigung oder Unfall geschützt und der sichere Betrieb des Fahrzeugs gewährleistet ist, nicht unter die Verbotsausnahme des Art 5 Abs 2 Satz 2 lit a VO 715/2007/EU fällt (Urteile C-145/20, Porsche Inter Auto und Volkswagen, Rn 73, 81;

**False Positives:**

- `Europäische Gerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Steinchen und Pflügler Specific` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `bde901d8`  
**Description:**
Matches the specific company name 'Steinchen und Pflügler Handel GmbH' which was frequently missed by the general GmbH pattern due to the 'und' connector.

**Content:**
```
\bSteinchen\s+und\s+Pflügler\s+Handel\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA Code Entity` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8173ee94`  
**Description:**
Matches 'FA' followed by a valid Finanzamt location (city, district, or code) or a specific multi-word location combination. Strictly excludes common verbs/prepositions.

**Content:**
```
\bFA\s+(?:(?:Freistadt\s+Rohrbach\s+Urfahr|Grieskirchen\s+Wels|Kirchdorf\s+Perg\s+Steyr|Spittal\s+Villach|Braunau\s+Ried\s+Schärding|Neunkirchen\s+Wr\.\s+Neustadt|Neunkirchen\s+Wiener\s+Neustadt|Hollabrunn\s+Korneuburg\s+Tulln|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Salzburg-Land|Salzburg-Stadt|Freistadt|Rohrbach|Urfahr|Linz|Graz|Salzburg|Wien|Innsbruck|Klagenfurt|Villach|Dornbirn|Feldkirch|Bludenz|Schwaz|Kitzbühel|Zell\s+am\s+See|Salzburg\s+Stadt|Salzburg\s+Land|Oberösterreich|Niederösterreich|Steiermark|Tirol|Vorarlberg|Burgenland|Kärnten|Lilienfeld\s+St\.\s+Pölten|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Schwechat\s+Gerasdorf|f\u00fcr\s+Geb\u00fchren|f\u00fcr\s+Gro\u00dfbetriebe|\u00d6sterreich|Eisenstadt\s+Oberwart|Graz-Umgebung|G\u00e4nserndorf\s+Mistelbach|Landeck\s+Reutte|Waldviertel|Bruck\s+Eisenstadt\s+Oberwart|Judenburg\s+Liezen|Spittal\s+Villach|Klagenfurt\s+Villach|Linz\s+Urfahr|Wels\s+Grieskirchen|Tirol\s+Ost|Tirol\s+West|Gmunden\s+V\u00f6cklabruck|Kufstein|Landeck|Reutte|Wien\s+9/18/19\s+Klosterneuburg|Wien\s+4/5/10|Wien\s+12/13/14\s+Purkersdorf|Wien\s+2/20/21/22|Wien\s+4/5/10|Wien\s+1/23|Wien\s+18|Wien\s+\d+(?:/\d+)*(?:\s+Schwechat\s+Gerasdorf)?|FA\s+\d+/\d+/\d+|FA\s+\w+\s+\d+/\d+/\d+|Steiermark\s+Mitte|Graz-Stadt|Baden\s+Mödling|Bregenz|Innsbruck|Grieskirchen\s+Wels|Hollabrunn\s+Korneuburg\s+Tulln|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Kirchdorf\s+Perg\s+Steyr|Salzburg-Land|Salzburg-Stadt|Freistadt\s+Rohrbach\s+Urfahr|Freistadt|Rohrbach|Urfahr|Linz|Graz|Salzburg|Wien|Innsbruck|Klagenfurt|Villach|Dornbirn|Feldkirch|Bludenz|Schwaz|Kitzbühel|Zell\s+am\s+See|Salzburg\s+Stadt|Salzburg\s+Land|Ober\u00f6sterreich|Nieder\u00f6sterreich|Steiermark|Tirol|Vorarlberg|Burgenland|K\u00e4rnten|Lilienfeld\s+St\.\s+P\u00f6lten|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Schwechat\s+Gerasdorf|f\u00fcr\s+Geb\u00fchren|\u00d6sterreich|Eisenstadt\s+Oberwart|Graz-Umgebung|G\u00e4nserndorf\s+Mistelbach|Landeck\s+Reutte|Waldviertel|Bruck\s+Eisenstadt\s+Oberwart|Judenburg\s+Liezen|Spittal\s+Villach|Klagenfurt\s+Villach|Linz\s+Urfahr|Wels\s+Grieskirchen|Tirol\s+Ost|Tirol\s+West|Gmunden\s+V\u00f6cklabruck|Kufstein|Landeck|Reutte|Wien\s+9/18/19\s+Klosterneuburg|Wien\s+4/5/10|\d+/\d+/\d+|\d+\s+\d+/\d+/\d+))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Full Entity` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9e5c99ba`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by specific known locations, codes, or multi-city combinations. Includes 'Österreich' and 'Spittal Villach' explicitly.

**Content:**
```
\bFinanzamt(?:es)?\s+(?:Wien\s+12/13/14\s+Purkersdorf|Wien\s+2/20/21/22|Wien\s+4/5/10|Wien\s+1/23|Wien\s+18|Wien\s+\d+(?:/\d+)*(?:\s+Schwechat\s+Gerasdorf)?|FA\s+\d+/\d+/\d+|FA\s+\w+\s+\d+/\d+/\d+|Steiermark\s+Mitte|Graz-Stadt|Braunau\s+Ried|Braunau\s+Ried\s+Sch\u00e4rding|Baden\s+M\u00f6dling|Bregenz|Neunkirchen\s+Wr\.\s+Neustadt|Neunkirchen\s+Wiener\s+Neustadt|Innsbruck|Grieskirchen\s+Wels|Hollabrunn\s+Korneuburg\s+Tulln|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Kirchdorf\s+Perg\s+Steyr|Salzburg-Land|Salzburg-Stadt|Freistadt\s+Rohrbach\s+Urfahr|Freistadt|Rohrbach|Urfahr|Linz|Graz|Salzburg|Wien|Innsbruck|Klagenfurt|Villach|Dornbirn|Feldkirch|Bludenz|Schwaz|Kitzb\u00fchel|Zell\s+am\s+See|Salzburg\s+Stadt|Salzburg\s+Land|Ober\u00f6sterreich|Nieder\u00f6sterreich|Steiermark|Tirol|Vorarlberg|Burgenland|K\u00e4rnten|Lilienfeld\s+St\.\s+P\u00f6lten|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Schwechat\s+Gerasdorf|f\u00fcr\s+Geb\u00fchren|\u00d6sterreich|Eisenstadt\s+Oberwart|Graz-Umgebung|G\u00e4nserndorf\s+Mistelbach|Landeck\s+Reutte|Waldviertel|Bruck\s+Eisenstadt\s+Oberwart|Judenburg\s+Liezen|Spittal\s+Villach|Klagenfurt\s+Villach|Linz\s+Urfahr|Wels\s+Grieskirchen|Tirol\s+Ost|Tirol\s+West|Gmunden\s+V\u00f6cklabruck|Kufstein|Landeck|Reutte|Wien\s+9/18/19\s+Klosterneuburg|Wien\s+4/5/10)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Zollamt Entity` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `09154e6f`  
**Description:**
Matches 'Zollamt' or 'Zollamtes' followed by optional location (e.g., 'Zollamt Linz Wels') or standalone, ensuring strict word boundaries.

**Content:**
```
\bZollamt(?:es)?(?:\s+(?:Linz\s+Wels|\w+))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 2796 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/15Os61_20i`) (sent_id: `deanon_260716_TRAIN/15Os61_20i_11`)


Nach den Sachverhaltsannahmen des Beschwerdegerichts ist Johann Rothmaler dringend verdächtig, in Am Spitalfeld 2, 9462 St. Peter im Lavanttal, Österreich und anderen Orten I. vorschriftswidrig Suchtgift 1. in einer das 25fache der Grenzmenge (§ 28b SMG) übersteigenden Menge anderen überlassen zu haben, indem er seit 2018 bis Mitte Dezember 2019 an Alexander Schuhardt wöchentlich zumindest ein Kilogramm „Speed“, enthaltend Amphetamin mit einem Reinheitsgehalt von zumindest 70 % weitergab, 2. aus dem Ausland aus- und nach Österreich eingeführt bzw dies versucht zu haben, indem er unbekannte Täter im „Darknet“ dazu bestimmte, 21,57 Gramm [richtig: 25,65 Gramm] Reinsubstanz MDMA sowie 200 Gramm „Speed-Paste“, enthaltend 74 % reines Amphetamin, auf dem Postweg an seine Wohnadresse zu versenden, wobei die zuerst genannte Sendung beim Zollamt Frankfurt/Deutschland sichergestellt wurde, II. am 14. Dezember 2019 im bewussten und gewollten Zusammenwirken mit Alexander Schlossmann Roberto Hampisch 1.

**False Positives:**

- `Zollamt Frankfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Johann Rothmaler`(person)
- `Am Spitalfeld 2, 9462 St. Peter im Lavanttal, Österreich`(address)
- `Alexander Schuhardt`(person)
- `Alexander Schlossmann`(person)
- `Roberto Hampisch`(person)

</details>

---

## `Finanzamt Standalone` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `97dedee7`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' as a standalone entity. Prioritized to catch cases where it appears without a specific location suffix.

**Content:**
```
\bFinanzamt(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 10 | 0 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 10 | 1772 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/3Ob99_10w`) (sent_id: `deanon_260716_TRAIN/3Ob99_10w_75`)


Der Rückstand beim Finanzamt betrage zum 30. Juni 2005 352.000 EUR, bei der beklagen Partei 157.000 EUR.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/3Ob99_10w`) (sent_id: `deanon_260716_TRAIN/3Ob99_10w_424`)


Der Schuldnerin war allerdings ohnehin ihre geradezu hoffnungslose Finanzsituation bekannt (vgl nur die Schreiben vom 7. Juli 2005, Beil ./E und vom 31. August 2005, Beil ./H, an die Banken zur Erreichung des Ausgleichs mit Hinweis ua auf ein negatives Eigenkapital per 30. Juni 2005 und einen Rückstand beim Finanzamt von 352.000 EUR, also auf eine klare Insolvenzsituation).

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_14`)


Die „Erfolgsprämien“ für die ihr für die Jahre 2009 und 2010 vom Finanzamt zuerkannten Forschungsprämien wurden der Klägerin von der Beklagten gezahlt. DieKlägerinerhob aufgrund der Nichtzahlung ihrer die Erfolgsprämie für das Jahr 2011 betreffenden Rechnung vom 7. 12. 2012 am 1. 12. 2015 Klage auf Zahlung von 65.850,37 EUR samt Zinsen.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_36`)


2012 erfolgte die Gutbuchung der Forschungsprämie 2011 auf dem Abgabenkonto der Beklagten durch das Finanzamt.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_37`)


Eine bescheidmäßige Erledigung erfolgt in solchen Fällen nicht, ein Bescheid wird in diesem Zusammenhang vom Finanzamt nur erlassen, wenn die beantragte Forschungsprämie nicht oder nicht zur Gänze gewährt wird.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_52`)


Im Zuge der Betriebsprüfungen durch das Finanzamt war die Klägerin noch zeitweise unterstützend bis in den Oktober 2014 hinein tätig, danach beendete sie ihre Tätigkeit für die Beklagte.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_54`)


Eine Gutbuchung einer Forschungsprämie für das Jahr 2012 durch das Finanzamt erfolgte bis zum Schluss der mündlichen Verhandlung erster Instanz durch das Finanzamt nicht am Abgabenkonto der Beklagten (unbestritten).

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation
- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 7** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_84`)


Das Erstgericht stützte vorliegend seine negative Feststellung – richtig: rechtliche Beurteilung – nun in erster Linie darauf (Ersturteil Seiten 7 f), dass der Geschäftsführer der Beklagten in Gesprächen mit dem Geschäftsführer der Klägerin stets darauf hingewiesen habe, er sei der Meinung, aufgrund der Zurückforderung der Forschungsprämien durch das Finanzamt nichts zu schulden und deshalb die offene Rechnung nicht bezahlen zu können.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_86`)


Gerade letzteres war hier aber nach der genannten (dislozierten) Feststellung der Fall: Der Geschäftsführer der Beklagten erklärte, wegen der Zurückforderung der Forschungsprämie durch das Finanzamt der Klägerin das in Rechnung gestellte Erfolgshonorar nicht bezahlen zu können.

**False Positives:**

- `Finanzamt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Finanzpolizei Entity` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `18c02c9f`  
**Description:**
Matches the specific organization 'Finanzpolizei' which was missing from the rules.

**Content:**
```
\bFinanzpolizei\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesfinanzgericht (BFG) Suffix` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `98d22604`  
**Description:**
Matches 'Bundesfinanzgericht' with optional genitive endings and the '(BFG)' suffix as a single entity, preventing split matches.

**Content:**
```
\bBundesfinanzgericht(?:es|s)?(?:\s*\(BFG\))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BFG Acronym Standalone` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `82863560`  
**Description:**
Matches the standalone acronym 'BFG' in legal contexts, ensuring it is captured as an organisation only when not part of a full name.

**Content:**
```
\bBFG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Fa. Company Names` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `286500ed`  
**Description:**
Matches company names prefixed with 'Fa.' (Firma), handling the specific case of 'Fa.Brocke Robotik GmbH' and similar structures.

**Content:**
```
\bFa\.([A-Z][A-Za-z\u00e4\u00f6\u00fc\u00df\-]+(?:\s+[A-Z][A-Za-z\u00e4\u00f6\u00fc\u00df\-]+)*\s+(?:GmbH|AG|KG|GmbH\s*&\s*Co\s*KG))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Landesgerichtes with City` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a1d1b740`  
**Description:**
Matches 'Landesgerichtes' or 'Landesgericht' followed by a city name or identifier, capturing the full court name and city.

**Content:**
```
\bLandesgericht(?:es)?(?:\s+f\u00fcr\s+)?([A-Z][A-Za-z\u00e4\u00f6\u00fc\u00df\s]+(?:\s+Ort)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 24 | 0 | 24 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 24 | 3696 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der zur AZ 38 Nc 13/08i beim Landesgericht für Zivilrechtssachen Wien anhängigen Ablehnungssache des Ablehnungswerbers Mag. Herwig Bortzlaff, über den Rekurs des Ablehnungswerbers gegen den Beschluss des Oberlandesgerichts Wien vom 10. November 2009, GZ 13 Nc 14/09x-2, womit ein Ablehnungsantrag zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Landesgericht für Zivilrechtssachen Wien anhängigen Ablehnungssache des Ablehnungswerbers Mag` — partial — gold is substring of pred: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schinko`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Hon.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Landesgericht für Zivilrechtssachen Wien`(organisation)
- `Mag. Herwig Bortzlaff`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_5`)


Im Zusammenhang mit diesem Verfahren wies das Landesgericht für Zivilrechtssachen Wien mit Beschluss vom 26.

**False Positives:**

- `Landesgericht für Zivilrechtssachen Wien mit Beschluss vom ` — partial — gold is substring of pred: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_12`)


Da mehrere Senate des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht an dem genannten Verhalten beteiligt gewesen seien, sei auch das gesamte Landesgericht für Zivilrechtssachen Wien als befangen anzusehen, über den nunmehr geltend gemachten Unterhaltsanspruch zu entscheiden.

**False Positives:**

- `Landesgericht für Zivilrechtssachen Wien als befangen anzusehen` — partial — gold is substring of pred: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_4`)


Text Gründe: Im Ermittlungsverfahren gegen Viktor Meisterernst und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und 3 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 703 St 3/11t (nunmehr AZ 713 St 24/18i) der Staatsanwaltschaft Wien, stellte der Beschuldigte Dr. Stefan Tydeck mit Schriftsatz vom 29. November 2017 – soweit im Folgenden von Relevanz – den Antrag auf Einstellung des Ermittlungsverfahrens „gemäß § 108 StPO“ (ON 558), welchen das Landesgericht für Strafsachen Wien mit Beschluss vom 22. Juni 2018, AZ 352 HR 214/11x, abwies (ON 644).

**False Positives:**

- `Landesgericht für Strafsachen Wien mit Beschluss vom ` — partial — gold is substring of pred: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Viktor Meisterernst`(person)
- `Dr. Stefan Tydeck`(person)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/13Os22_12b_13Ns16_12z_`) (sent_id: `deanon_260716_TRAIN/13Os22_12b_13Ns16_12z__4`)


Text Gründe: Das Landesgericht für Strafsachen Wien verhängte mit Beschluss vom 9. Dezember 2011 über Mag. Türkan Kirstin Bierwolf die Untersuchungshaft aus den Gründen der Tatbegehungsgefahr nach § 173 Abs 2 Z 3 lit b und lit d StPO (ON 12).

**False Positives:**

- `Landesgericht für Strafsachen Wien verhängte mit Beschluss vom ` — partial — gold is substring of pred: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Wien`(organisation)
- `Kirstin Bierwolf`(person)

**Example 5** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__6`)


Dem Landesgericht für Strafsachen Graz wird ein Vorgehen gemäß §§ 14 und 15 dieser Verordnung aufgetragen.

**False Positives:**

- `Landesgericht für Strafsachen Graz wird ein Vorgehen gemäß` — partial — gold is substring of pred: `Landesgericht für Strafsachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Graz`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__28`)


8. Das Landesgericht für Strafsachen Graz hätte demnach die Staatsanwaltschaft und den Angeklagten von der dauernden Verhinderung des Vorsitzenden des Schöffengerichts in Kenntnis setzen und vor Betrauung eines anderen Richters mit der Urteilsausfertigung nach ihrem Einverständnis fragen müssen.

**False Positives:**

- `Landesgericht für Strafsachen Graz hätte demnach die Staatsanwaltschaft und den Angeklagten von der dauernden Verhinderung des Vorsitzenden des Schöffengerichts in Kenntnis setzen und vor Betrauung eines anderen Richters mit der Urteilsausfertigung nach ihrem Einverständnis fragen müssen` — partial — gold is substring of pred: `Landesgericht für Strafsachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Graz`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__30`)


Mit Blick auf § 292 letzter Satz StPO sah sich der Oberste Gerichtshof veranlasst, dem Landesgericht für Strafsachen Graz aufzutragen, gemäß §§ 14 und 15 der Kaiserlichen Verordnung vorzugehen.

**False Positives:**

- `Landesgericht für Strafsachen Graz aufzutragen` — partial — gold is substring of pred: `Landesgericht für Strafsachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Landesgericht für Strafsachen Graz`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/13Os34_19b`) (sent_id: `deanon_260716_TRAIN/13Os34_19b_5`)


Dieser Beschluss wird aufgehoben und es wird dem Landesgericht für Strafsachen Graz aufgetragen, im Verfahren AZ 16 Hv 32/15a über den Widerruf zu entscheiden.

**False Positives:**

- `Landesgericht für Strafsachen Graz aufgetragen` — partial — gold is substring of pred: `Landesgericht für Strafsachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Graz`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_14`)


Die Sanktionsrüge (Z 11 zweiter Fall) wendet sich gegen die als nach § 33 Abs 1 Z 2 StGB strafschärfend gewertete Verurteilung des Angeklagten durch das Landesgericht für Strafsachen Wien vom 16. Februar 2012, AZ 62 Hv 10/12m, (ua) wegen Vergehen des unerlaubten Umgangs mit Suchtmitteln (US 4, 9; ON 97).

**False Positives:**

- `Landesgericht für Strafsachen Wien vom ` — partial — gold is substring of pred: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Wien`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__5`)


In Stattgebung des Antrags der Generalprokuratur wird im außerordentlichen Weg die Wiederaufnahme des Berufungsverfahrens verfügt, der Beschluss des Landesgerichts für Strafsachen Wien vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), aufgehoben und die Sache zur neuerlichen Entscheidung über die Berufung des Angeklagten gegen das Urteil des Bezirksgerichts Innere Stadt Wien vom 27. November 2018 (ON 19 der U-Akten) an das Landesgericht für Strafsachen Wien verwiesen.

**False Positives:**

- `Landesgericht für Strafsachen Wien verwiesen` — partial — gold is substring of pred: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Strafsachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__9`)


Die am 22. Februar 2019 – innerhalb der Frist des § 467 Abs 1 StPO (vgl Zustellnachweis an ON 19) – ausgeführte Berufung des Robert Unterdörfer (ON 21) wies das Landesgericht für Strafsachen Wien als Berufungsgericht mit Beschluss vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23), gemäß § 470 Z 1 StPO als unzulässig zurück, weil die am 27. November 2018 zur Post gegebene Rechtsmittelanmeldung gegen das am 23. November 2018 verkündete Urteil verspätet gewesen sei.

**False Positives:**

- `Landesgericht für Strafsachen Wien als Berufungsgericht mit Beschluss vom ` — partial — gold is substring of pred: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Robert Unterdörfer`(person)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/14Ns5_20a`) (sent_id: `deanon_260716_TRAIN/14Ns5_20a_5`)


Die Akten werden dem Oberlandesgericht Wien zurückgestellt. Gründe:  Rechtliche Beurteilung Der Wohnsitz des Angeklagten und Antragsgegners im Sprengel eines anderen Gerichts (ON 16 iVm ON 15 und ON 1 S 4 und 6) ist ebensowenig ein wichtiger Grund im Sinn des § 39 Abs 1 StPO wie der Umstand, dass sich der – von der Mindestsicherung lebende – Angeklagte die Kosten für die Anreise zum Landesgericht für Strafsachen Wien ersparen würde (RIS-Justiz RS0129146;

**False Positives:**

- `Landesgericht für Strafsachen Wien ersparen würde` — partial — gold is substring of pred: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgericht Wien`(organisation)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/14Os132_10h`) (sent_id: `deanon_260716_TRAIN/14Os132_10h_4`)


Text Gründe: Gegen Tomsilav Ayik ist beim Landesgericht für Strafsachen Wien ein - im Stadium der Hauptverhandlung befindliches - Verfahren wegen der Verbrechen des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und nach § 28a Abs 1 fünfter Fall, Abs 4 Z 3 SMG anhängig, in dem sich der Angeklagte seit 5. April 2010 in Untersuchungshaft befindet (ON 20).

**False Positives:**

- `Landesgericht für Strafsachen Wien ein` — partial — gold is substring of pred: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ayik`(person)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/15Os110_17s`) (sent_id: `deanon_260716_TRAIN/15Os110_17s_10`)


Aus Anlass eines vom Angeklagten am 17. Februar 2017 eingebrachten Antrags auf Aufhebung der Untersuchungshaft (ON 95) setzte das Landesgericht für Strafsachen Graz mit Beschluss vom 23. Februar 2017 die am 7. September 2016 verhängte (ON 11) – und danach wiederholt prolongierte (ON 32, 71) – Untersuchungshaft aus den Haftgründen der Flucht- und der Tatbegehungsgefahr nach § 173 Abs 2 Z 1 und Z 3 lit a StPO fort (ON 100).

**False Positives:**

- `Landesgericht für Strafsachen Graz mit Beschluss vom ` — partial — gold is substring of pred: `Landesgericht für Strafsachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Graz`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__57`)


Das Landesgericht für Strafsachen Wien und das Oberlandesgericht Wien als Berufungsgericht haben somit die (grundsätzliche) Verwirklichung des Entschädigungsanspruchs nach § 6 Abs 1 MedienG in Bezug auf die am 4. Juni 2017 auf dem Facebook-Account von www.

**False Positives:**

- `Landesgericht für Strafsachen Wien und das Oberlandesgericht Wien als Berufungsgericht haben somit die` — partial — gold is substring of pred: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Wien`(organisation)
- `Oberlandesgericht Wien`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_5`)


Text Gründe: In der Medienrechtssache der Antragsteller Dr. Wieland Skocdopole und Priv.-Doz.in Heidrun Aguera, BA MSc gegen die Antragsgegnerin Wald Fenkraftal GmbH & Co KG wegen §§ 7 f MedienG brachten die Antragsteller beim Landesgericht für Strafsachen Wien gesondert, jeweils in einem eigenen Schriftsatz aber vertreten durch dieselbe Rechtsanwältin selbständige Entschädigungsanträge gegen die Antragsgegnerin ein.

**False Positives:**

- `Landesgericht für Strafsachen Wien gesondert` — partial — gold is substring of pred: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Wieland Skocdopole`(person)
- `Priv.-Doz.in Heidrun Aguera, BA MSc`(person)
- `Wald Fenkraftal GmbH & Co KG`(organisation)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/1Nc71_10x`) (sent_id: `deanon_260716_TRAIN/1Nc71_10x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Dr. Grohmann als weitere Richter in der beim Landesgericht für Zivilrechtssachen Wien zu AZ 33 Cg 21/10s anhängigen Rechtssache der klagenden Partei Bachkraft Gesellschaft mbH, Salmweg 829, 4891 Schachen, Österreich, vertreten durch Dr. Gerhard Kornek, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 53.176,92 EUR sA, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Landesgericht für Zivilrechtssachen Wien zu AZ ` — partial — gold is substring of pred: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Dr. Grohmann`(person)
- `Landesgericht für Zivilrechtssachen Wien`(organisation)
- `Bachkraft Gesellschaft mbH`(organisation)
- `Salmweg 829, 4891 Schachen, Österreich`(address)
- `Dr. Gerhard Kornek`(person)

**Example 18** (doc_id: `deanon_260716_TRAIN/1Nc71_10x`) (sent_id: `deanon_260716_TRAIN/1Nc71_10x_8`)


Das Landesgericht für Zivilrechtssachen Wien legte die Akten dem Obersten Gerichtshof gemäß § 9 Abs 4 AHG vor.

**False Positives:**

- `Landesgericht für Zivilrechtssachen Wien legte die Akten dem Obersten Gerichtshof gemäß` — partial — gold is substring of pred: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)
- `Obersten Gerichtshof`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/1Ob78_22k`) (sent_id: `deanon_260716_TRAIN/1Ob78_22k_8`)


Das Landesgericht für Zivilrechtssachen Wien gab der gegen das Ersturteil gerichteten Berufung des Beklagten mit dem (dessen Verfahrenshelfer am 17.

**False Positives:**

- `Landesgericht für Zivilrechtssachen Wien gab der gegen das Ersturteil gerichteten Berufung des Beklagten mit dem` — partial — gold is substring of pred: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/1Ob78_22k`) (sent_id: `deanon_260716_TRAIN/1Ob78_22k_11`)


diese Entscheidung wurde vom Landesgericht für Zivilrechtssachen Wien später bestätigt.

**False Positives:**

- `Landesgericht für Zivilrechtssachen Wien später bestätigt` — partial — gold is substring of pred: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/4Fsc1_10z`) (sent_id: `deanon_260716_TRAIN/4Fsc1_10z_5`)


Diesen Ablehnungsantrag hat das Landesgericht für Zivilrechtssachen Wien am 19.

**False Positives:**

- `Landesgericht für Zivilrechtssachen Wien am ` — partial — gold is substring of pred: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/4Fsc1_10z`) (sent_id: `deanon_260716_TRAIN/4Fsc1_10z_11`)


9. 2009 hat das Landesgericht für Zivilrechtssachen Wien am 12.

**False Positives:**

- `Landesgericht für Zivilrechtssachen Wien am ` — partial — gold is substring of pred: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/4Nc30_22g`) (sent_id: `deanon_260716_TRAIN/4Nc30_22g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Kodek als Vorsitzenden sowie die Hofräte Dr. Schwarzenbacher und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Iris Gscheider, vertreten durch Dr. Sabine C.M. Deutsch, Rechtsanwältin in Riegersburg, gegen die beklagte Partei Mag. Annette Salzbauer, als Masseverwalter im Konkursverfahren über das Vermögen von Lynn Galleitner (AZ 26 S 10/21x des Landesgerichts für Zivilrechtssachen Graz), vertreten durch die GRAF ISOLA Rechtsanwälte GmbH in Graz, wegen Unterlassung, über den Delegierungsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der unmittelbar beim Obersten Gerichtshof eingebrachte Delegierungsantrag samt Beilagen wird dem Landesgericht für Zivilrechtssachen Graz als Erstgericht zu AZ 10 Cg 83/22z zur geschäftsordnungsgemäßen Behandlung übermittelt. Begründung:  Rechtliche Beurteilung [1]

**False Positives:**

- `Landesgericht für Zivilrechtssachen Graz als Erstgericht zu AZ ` — partial — gold is substring of pred: `Landesgericht für Zivilrechtssachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. Schwarzenbacher`(person)
- `MMag. Matzka`(person)
- `Iris Gscheider`(person)
- `Dr. Sabine C.M. Deutsch`(person)
- `Mag. Annette Salzbauer`(person)
- `Lynn Galleitner`(person)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)
- `GRAF ISOLA Rechtsanwälte GmbH`(organisation)
- `Obersten Gerichtshof`(organisation)
- `Landesgericht für Zivilrechtssachen Graz`(organisation)

</details>

---

## `Specific GmbH Company Names` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `de162888`  
**Description:**
Matches specific known company names that were missed by generic patterns, including 'Analyse Allexwald GmbH', 'Brocke Robotik GmbH', and 'c Stahl und Anlagenbau GmbH'.

**Content:**
```
\b(?:Analyse Allexwald|Brocke Robotik|c Stahl und Anlagenbau) GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `EASO Acronym` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a0460274`  
**Description:**
Matches the EASO (European Asylum Support Office) acronym.

**Content:**
```
\bEASO\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamts Österreich` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `04344446`  
**Description:**
Matches 'Finanzamts Österreich' as a specific organization entity.

**Content:**
```
\bFinanzamts\s+\u00d6sterreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesfinanzgericht Full Name` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `61a74230`  
**Description:**
Matches 'Bundesfinanzgericht' with optional genitive endings and the '(BFG)' suffix as a single entity, preventing split matches.

**Content:**
```
\bBundesfinanzgericht(?:es|s)?(?:\s*\(BFG\))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `KG Company Names Refined` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c166ca7e`  
**Description:**
Matches company names ending in 'KG' or 'GmbH & Co KG' with a proper noun prefix, ensuring 'Firma' is not included in the match.

**Content:**
```
\b([A-Z][A-Za-z\u00e4\u00f6\u00fc\u00df\-]+(?:\s+[A-Z][A-Za-z\u00e4\u00f6\u00fc\u00df\-]+)*\s+(?:GmbH\s*&\s*Co\s*KG|GmbH\s*&\s*Partner\s*KG|KG))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `AG Company Names Refined` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fa238ea9`  
**Description:**
Matches company names ending in 'AG' with a preceding proper noun or alphanumeric prefix, ensuring 'Firma' is not included.

**Content:**
```
\b([A-Z][A-Za-z\u00e4\u00f6\u00fc\u00df\+\-]+(?:\s+[A-Z][A-Za-z\u00e4\u00f6\u00fc\u00df\+\-]+)*\s+AG)\b
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

