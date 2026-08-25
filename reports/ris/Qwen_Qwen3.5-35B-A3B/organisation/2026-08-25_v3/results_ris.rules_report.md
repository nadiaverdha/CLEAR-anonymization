# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-08-25T21:23:58.674745

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/ris/Qwen_Qwen3.5-35B-A3B/organisation/2026-08-25_v3/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 100 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 80 |
| Validation documents | 20 |
| Test documents | 477 |
| Train sentences | 1351 |
| Validation sentences | 394 |
| Test sentences | 22727 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 5 |
| Max samples in prompt | 100 |
| Refinement iterations | 6 |
| Seed | 42 |
| Agentic | False |
| Enable Critic | True |
| Enable Prune | True |
| Critic Interval | 20 |
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

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 91.3% |
| True Positives | 671 |
| False Positives | 454 |
| False Negatives | 3343 |
| Total Gold Entities | 4014 |
| Micro Precision | 59.6% |
| Micro Recall | 16.7% |
| Micro F1 | 26.1% |
| Macro F1 | 26.1% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `MunicipalBodies` | 0.4% | 100.0% | 0.2% | 8 | 8 | 0 |
| `Verfassungsgerichtshof` | 0.9% | 100.0% | 0.4% | 18 | 18 | 0 |
| `Courts` | 25.6% | 92.5% | 14.8% | 643 | 595 | 48 |
| `KGCompanies` | 0.2% | 17.2% | 0.1% | 29 | 5 | 24 |
| `CompanyGmbH_Generic` | 1.6% | 12.7% | 0.9% | 275 | 35 | 240 |
| `CompanyAG` | 0.5% | 9.3% | 0.2% | 108 | 10 | 98 |
| `GenericFirma` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `TaxAuthorities` | 0.0% | 0.0% | 0.0% | 10 | 0 | 10 |
| `CompanyGmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `MinistryAbbreviations` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `KAG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BFH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `PoliceAuthorities` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `AMS` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Landesgericht` | 0.0% | 0.0% | 0.0% | 31 | 0 | 31 |
| `ÖGK` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `TaxAuthorityFA` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `UniversityWien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `MinistryBMI` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Pensionsversicherungsanstalt` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `SKTelecom` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `WienerGemeinderat` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BundesamtSoziales` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `PostAG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `MunicipalBodies` 

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `0bce244b`  
**Description:**
Matches 'Magistrat der Stadt Wien' and 'Magistrates der Stadt Wien' variations, handling plural forms, extra spaces, and optional department suffixes.

**Content:**
```
\b(?:Magistrat(?:es)?(?:\s+der\s+Stadt\s+Wien(?:,\s+Magistratsabteilung\s+\d+)?|der\s+Stadt\s+Wien)|Magistrates\s+der\s+Stadt\s+Wien(?:,\s+Magistratsabteilung\s+\d+)?)\b
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

## `Verfassungsgerichtshof` 🏆

**F1:** 0.009 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Rule ID:** `ff333e7c`  
**Description:**
Matches the Constitutional Court (Verfassungsgerichtshof) and its genitive form.

**Content:**
```
\bVerfassungsgerichtshof(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.009 | 18 | 18 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 18 | 0 | 3492 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_91`)


Das Berufungsgericht sehe sich daher nicht zu einer Antragstellung an den Verfassungsgerichtshof veranlasst.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 1** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_147`)


2. Seine Anregung, ein Gesetzesprüfungsver-fahren beim Verfassungsgerichtshof bezüglich der „von der beklagten Partei ins Treffen geführten gesetzlichen Bestimmungen“ einzuleiten, begründet der Kläger mit einer Verletzung des Gleichheitssatzes.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 2** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_158`)


Mangelhaft soll das Berufungsverfahren deshalb geblieben sein, weil das Berufungsgericht keinen Antrag an den Verfassungsgerichtshof gestellt hat: Hat der Oberste Gerichtshof oder ein zur Entscheidung in zweiter Instanz zuständiges Gericht gegen die Anwendung eines (Bundes- oder Landes-)Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken, so ist nach Art 89 Abs 2 B-VG von Amts wegen der Antrag auf Aufhebung dieses Gesetzes beim Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_162`)


Unterlässt ein Gericht die Anfechtung einer Norm beim Verfassungsgerichtshof, steht dagegen nach ständiger Rechtsprechung keiner Partei ein Rechtsmittel zu (RIS-Justiz RS0056514 [T10]).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 4** (doc_id: `deanon_260716_TRAIN/3Ob229_14v`) (sent_id: `deanon_260716_TRAIN/3Ob229_14v_44`)


Auch der Verfassungsgerichtshof hat in der vom Kläger zitierten Entscheidung B 97/91, B 284/91-303/91 (= VfSlg 13.006) zu einer - nicht dem § 38 Abs 6 OÖ ROG entsprechenden - Norm des früheren OÖ ROG 1972 eingeräumt, dass unter dem auch dort verwendeten Begriff „Grundstück“ nicht unbedingt nur ein einzelnes Grundstück verstanden werden kann, sondern gegebenenfalls auch mehrere Grundstücke, die miteinander eine „Einheit“ bilden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 5** (doc_id: `deanon_260716_TRAIN/3Ob26_23d`) (sent_id: `deanon_260716_TRAIN/3Ob26_23d_51`)


Vor diesem Hintergrund sprach der Verfassungsgerichtshof aus, dass durch die Öffentlicherklärung einesin der Natur schon bestehendenWeges durch Verordnung mangels Eigentumserwerbs in gesetzwidriger Weise Gemeingebrauch begründet werde.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 6** (doc_id: `deanon_260716_TRAIN/5Ob171_22s`) (sent_id: `deanon_260716_TRAIN/5Ob171_22s_66`)


In den vonRohregger(aaO) zitierten Entscheidungen bejahen auch der Verfassungsgerichtshof (B 1050/09) und der Verwaltungsgerichtshof (AW 2012/01/0032) die Bedeutung des § 10 RAO und der Vorgängerbestimmung des § 10 RL-BA 2015 für das öffentliche Interesse an dem Verbot der Doppelvertretung, weil es dem Schutz der durch einen Rechtsanwalt vertretenen Parteien diene, seine Einhaltung für das zwischen Rechtsanwalt und Klient bestehende Treueverhältnis für wesentlich erachtet werde und für das allgemeine Bild der Anwaltschaft in der Öffentlichkeit von Bedeutung sei.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 7** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_147`)


3.2.6.Auch der Verfassungsgerichtshof hat sich bereits mehrfach (G 164/2014;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 8** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_152`)


Der Verfassungsgerichtshof führte allerdings aus, dass die Bestimmungen des Fern- und Auswärtsgeschäfte-Gesetzes den Vorschriften der Verbraucherrechte-RL entsprächen, welche den Mitgliedstaaten keinen Spielraum bei der Umsetzung einräumten;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 9** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_154`)


Auch von einem Vorabentscheidungsersuchen an den EuGH sah der Verfassungsgerichtshof ab (ErwG 74).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 10** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_155`)


Darüber hinaus setzte sich der Verfassungsgerichtshof in diesem Erkenntnis mit Art 14 Abs 2 der Verbraucherrechte-RL, der durch § 15 Abs 4 FAGG umgesetzt wurde, auseinander und äußerte keine Zweifel an der Gültigkeit des Art 14 Abs 2 letzter Satz (entspricht § 15 Abs 4 letzter Satz FAGG): Der Verfassungsgerichtshof hat keine Zweifel an der Gültigkeit des Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 11** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_159`)


Der Verfassungsgerichtshof kann nun nicht erkennen, dass die Regelung des Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL diesen von der Rechtsprechung des Gerichtshofes der Europäischen Union aufgestellten Kriterien im Rahmen der Verhältnismäßigkeitsprüfung eines Unionsrechtsakts widerspricht: Die Bestimmungen der Verbraucherrechte-RL verfolgen das Ziel eines umfassenden Verbraucherschutzes bei Fernabsatzverträgen und außerhalb von Geschäftsräumen geschlossenen Verträgen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 12** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_161`)


Der Verfassungsgerichtshof hat keine Zweifel, dass die in Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL normierte Rechtsfolge für den Unternehmer bei mangelnder Belehrung über das Widerrufsrecht geeignet ist, das Ziel des umfassenden Verbraucherschutzes bei Fernabsatzverträgen und bei außerhalb von Geschäftsräumen geschlossenen Verträgen zu erreichen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 13** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_162`)


Der Verfassungsgerichtshof kann auch nicht erkennen, dass die Regelung des Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL über das hinausgeht, was zur Verfolgung des mit der Regelung verfolgten Ziels des umfassenden Verbraucherschutzes erforderlich ist.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 14** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_165`)


Der Verfassungsgerichtshof hat sohin keine Zweifel an deren Gültigkeit.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 15** (doc_id: `deanon_260716_TRAIN/8ObA72_19z`) (sent_id: `deanon_260716_TRAIN/8ObA72_19z_12`)


2. Dabei konnte sich der Oberste Gerichtshof auf einschlägige Judikatur sowohl des Verfassungsgerichtshofs als auch des EuGH stützen: 2.1 Der Verfassungsgerichtshof hat in seinem Erkenntnis G 450/2015 ua Parteianträge von ÖBB-Bediensteten (unter anderem auch des Klägers) abgewiesen, die § 53a und § 56 Abs 18 bis 24 BundesbahnG je idF BGBl I Nr 64/2015 als verfassungswidrig aufzuheben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Verfassungsgerichtshofs` (organisation)
- `ÖBB` (organisation)

</details>

---

## `Courts` 🏆

**F1:** 0.256 | **Precision:** 0.925 | **Recall:** 0.148  

**Format:** `regex`  
**Rule ID:** `03120a40`  
**Description:**
Matches court names including full names, abbreviations, and genitive forms. Now includes 'Landesgericht [Name]' pattern and 'Gerichtshof der Europäischen Union'.

**Content:**
```
\b(?:Verwaltungsgerichtshof(?:es)?|Bundesfinanzgericht(?:es)?|Bundesfinanzgerichts|B(?:undesfinanzgericht|FG)|Obersten\s+Gerichtshof(?:es)?|Landesgericht(?:s)?\s+[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)?|Gerichtshof\sder\sEuropäischen\sUnion)\b(?:\s*\(\s*BFG\s*\))?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.925 | 0.148 | 0.256 | 643 | 595 | 48 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 595 | 48 | 3412 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_14`)


Das Erstgericht legte den Akt dem Obersten Gerichtshof unter Hinweis auf den Verfahrensstand, aber entgegen § 31 Abs 3 JN ohne eigene Stellungnahme zur Zweckmäßigkeit, zur Entscheidung über den Delegierungsantrag vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_13`)


In ihrem gegen diesen Beschluss erhobenenRekursbeantragte die Klägerin hilfsweise (für den Fall, dass ihrem Rekurs nicht stattgegeben werden sollte) die Ordination gemäß § 28 JN an ein vom Obersten Gerichtshof zu benennendes Bezirksgericht (ON 34).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_23`)


2.1 Als Grundlage für eine Ordination kommt daher nur der Fall des § 28 Abs 1 Z 2 JN in Betracht, wonach die Bestimmung eines örtlich zuständigen Gerichts durch den Obersten Gerichtshof dann zulässig ist, wenn der Antragsteller seinen Wohnsitz im Inland hat und im Einzelfall die Rechtsverfolgung im Ausland nicht möglich oder unzumutbar wäre (RIS-Justiz RS0112108).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der beim Landesgericht Linz zu AZ 3 Cg 46/21a anhängigen Rechtssache der klagenden Partei Hollengk Planung GmbH, Am Steindl 3, 9873 Döbriach, Österreich, vertreten durch Huber Berchtold Rechtsanwälte OG in Wien, gegen die beklagte Partei Wind Nexheimval GmbH, Wiesbergsiedlung 4, 8341 Pöllau, Österreich, vertreten durch ScherbaumSeebacher Rechtsanwälte GmbH in Graz, wegen 188.117,55 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN folgenden Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, zur Verhandlung und Entscheidung der Rechtssache anstelle des Landesgerichts Linz das Landesgericht Korneuburg zu bestimmen, wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |
| `Landesgerichts Linz` | `Landesgerichts Linz` |
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Hollengk Planung GmbH` (organisation)
- `Am Steindl 3, 9873 Döbriach, Österreich` (address)
- `Huber Berchtold Rechtsanwälte OG` (organisation)
- `Wind Nexheimval GmbH` (organisation)
- `Wiesbergsiedlung 4, 8341 Pöllau, Österreich` (address)
- `ScherbaumSeebacher Rechtsanwälte GmbH` (organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_6`)


Die in Wien ansässige klagende Gesellschaft nimmt die in Linz ansässige beklagte Gesellschaft beim Landesgericht Linz auf restliche Honorare für Planungsleistungen für ein Bauvorhaben in Klosterneuburg bei Wien in Anspruch.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_12`)


[3] Bereits in der Klage beantragt dieKlägerindie Delegierung der Rechtssache an das Landesgericht Korneuburg.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_15`)


Die Verhandlung der Rechtssache im Gerichtssprengel des Bauvorhabens – dem Landesgericht Korneuburg – sei daher verfahrensökonomisch und zweckmäßig.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_19`)


Sowohl die Beklagte als auch ihre Geschäftsführer sowie fünf namhaft gemachte Zeugen hätten ihren Arbeitsplatz bzw Wohnsitz im Sprengel des Landesgerichts Linz.

| Predicted | Gold |
|---|---|
| `Landesgerichts Linz` | `Landesgerichts Linz` |

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_21`)


Die Delegierung an das Landesgericht Korneuburg wäre daher mit einer erheblichen Verteuerung des Verfahrens und einer Erschwerung des Gerichtszugangs verbunden.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_29`)


Die Rechtssache weist keinen eindeutigen Schwerpunkt zum Landesgericht Korneuburg auf.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_30`)


Zwar ist das Bauvorhaben im Sprengel des Landesgerichts Korneuburg situiert.

| Predicted | Gold |
|---|---|
| `Landesgerichts Korneuburg` | `Landesgerichts Korneuburg` |

**Example 11** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_31`)


Mehrere von der Beklagten namhaft gemachte Zeugen sind aber im Sprengel des angerufenen Landesgerichts Linz bzw in Oberösterreich wohnhaft.

| Predicted | Gold |
|---|---|
| `Landesgerichts Linz` | `Landesgerichts Linz` |

**Example 12** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_32`)


Damit kann nicht gesagt werden, dass die Gründe für eine Übertragung der Rechtssache vom Landesgericht Linz an das Landesgericht Korneuburg überwiegen.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 13** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_33`)


Dass die Rechtssache vom Landesgericht Korneuburg aller Voraussicht nach rasch und mit geringerem Kostenaufwand zu Ende geführt werden kann, ist nach dem bisherigen Vorbringen nicht zu erkennen.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 14** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_4`)


Das Bezirksgericht Mödling legte den Akt zur Entscheidung gemäß § 111 Abs 2 JN dem Obersten Gerichtshof vor (ON 8), ohne den Übertragungsbeschluss an die Parteien zuzustellen.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Missed by this rule (FN):**

- `Bezirksgericht Mödling` (organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_8`)


Andernfalls könnte eine Verschiebung der funktionellen Zuständigkeit eintreten, weil mangels Bestätigung des Übertragungsbeschlusses durch das Rekursgericht gar keine Grundlage für die Genehmigung einer Zuständigkeitsübertragung durch den Obersten Gerichtshof bestünde (9 Nc 15/14a;

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 16** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_4`)


Text Begründung: Mit ihrer erkennbar an den Obersten Gerichtshof gerichteten Eingabe vom 6.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 17** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_9`)


Das übertragende Gericht legte aufgrund dieser Weigerung den Akt dem Obersten Gerichtshof als gemeinsam übergeordnetem Gericht zur Entscheidung gemäß § 111 Abs 2 JN vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 18** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_5`)


[2] Das Bezirksgericht Graz-West legte den Akt daraufhin dem Obersten Gerichtshof zur Entscheidung gemäß § 111 Abs 2 JN vor, ohne den Übertragungsbeschluss den Parteien zuzustellen.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Missed by this rule (FN):**

- `Bezirksgericht Graz-West` (organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_15`)


Das Erstgericht wies die Klage wegen Fehlens eines inländischen Gerichtsstands und somit der österreichischen internationalen Zuständigkeit rechtskräftig zurück und legte daraufhin den Akt dem Obersten Gerichtshof zur Entscheidung über den hilfsweise gestellten Ordinationsantrag vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 20** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_21`)


[7] Letztlich legte das Bezirksgericht Josefstadt die Akten dem Obersten Gerichtshof zur Entscheidung des Zuständigkeitsstreits vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Missed by this rule (FN):**

- `Bezirksgericht Josefstadt` (organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_22`)


[8] Die vom Bezirksgericht Villach veranlasste Vorlage der Akten an den Obersten Gerichtshof ist verfrüht:  Rechtliche Beurteilung [9] Übertragungsbeschlüsse nach § 111 JN sind durch die Parteien anfechtbar (RIS-Justiz RS0046981 [insb T5]).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Missed by this rule (FN):**

- `Bezirksgericht Villach` (organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Steidlen+Ysner Daten GmbH, Kaminweg 34, 8200 Laßnitzthal, Österreich, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Verlag Waldlemder GmbH, Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |
| `Landesgerichts Linz` | `Landesgerichts Linz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Steidlen+Ysner Daten GmbH` (organisation)
- `Kaminweg 34, 8200 Laßnitzthal, Österreich` (address)
- `Dr. Roland Kassowitz` (person)
- `Verlag Waldlemder GmbH` (organisation)
- `Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich` (address)
- `Prof. Haslinger` (person)
- `Handelsgericht Wien` (organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_3`)


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

**Example 24** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_54`)


1. Auf die Ausführungen der Revision, die sich gegen die dem Aufhebungsbeschluss zugrundeliegende rechtliche Beurteilung des Berufungsgerichts wenden, ist vom Obersten Gerichtshof mangels Bekämpfbarkeit des Aufhebungsbeschlusses derzeit nicht einzugehen.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 25** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_3`)


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

**Example 26** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


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

**Example 27** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_23`)


Rechtliche Beurteilung Der Revisionsrekurs des Bundes ist entgegen dem den Obersten Gerichtshof nicht bindenden Ausspruch des Rekursgerichts (§ 71 Abs 1 AußStrG) mangels einer Rechtsfrage im Sinn des § 62 Abs 1 AußStrG nicht zulässig.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 28** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_3`)


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

**Example 29** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_20`)


Dieser Fall liegt hier aber nach den den Obersten Gerichtshof bindenden Feststellungen nicht vor, weil der Beklagte - entgegen den Ausführungen des Revisionswerbers - die aufgekündigte Wohnungnichtregelmäßig zu Wohnzwecken verwendet, sondern lediglich sporadisch, als Absteigequartier.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 30** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_27`)


Ein Kostenersatz für die ohne Freistellung durch den Obersten Gerichtshof eingebrachte Revisionsbeantwortung steht der Klägerin nach § 508a Abs 2 Satz 2 ZPO nicht zu (RIS-Justiz RS0043690 [T6, T7]).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 31** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_5`)


Anita Schetzel, vertreten durch die Summereder Pichler Wächter Rechtsanwälte GmbH in Leonding, wegen 12.750 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Wels als Berufungsgericht vom 13. Dezember 2023, GZ 21 R 277/23v-53, mit dem das Urteil des Bezirksgerichts Wels vom 23. August 2023, GZ 9 C 430/22s-47, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Die Revision wird in Ansehung der Klageforderungen von 2.700 EUR sA, 4.575 EUR sA und 450 EUR sA zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Wels` | `Landesgerichts Wels` |

**Missed by this rule (FN):**

- `Anita Schetzel` (person)
- `Bezirksgerichts Wels` (organisation)

**Example 32** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_144`)


Das Berufungsgericht hat – ausgehend von seiner vom Obersten Gerichtshof nicht geteilten Rechtsansicht – sowohl die Mängelrüge (Nichteinholung eines Gutachtens für den Bereich Pferdehaltung und Pferdesport) als auch die (auch) die Feststellungen zu den behaupteten Mängeln betreffende Beweisrüge der Berufung nicht erledigt, weshalb sein Verfahren mangelhaft geblieben ist.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 33** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_50`)


4. 2011 enthaltenen Hinweise weitere Aufträge erteilt habe, werden keine Umstände aufgezeigt, die einen vom Obersten Gerichtshof aufzugreifenden Fehler in der Beurteilung des Berufungsgerichts, der nicht fachkundigen Klägerin könne kein Mitverschulden am Entstehen des Schadens angelastet werden, begründen könnten.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 34** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_9`)


Die Revision der Beklagten ist entgegen dem – den Obersten Gerichtshof nicht bindenden – Zulassungsausspruch mangels Vorliegens einer Rechtsfrage von erheblicher Bedeutung im Sinn des § 502 Abs 1 ZPO nicht zulässig.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 35** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_11`)


Das Vorliegen einer Rechtsfrage von erheblicher Bedeutung ist nach dem Zeitpunkt der Entscheidung über das Rechtsmittel durch den Obersten Gerichtshof zu beurteilen.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 36** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_10`)


2008 erfolgte die Eintragung beim Firmenbuch des Landesgerichts Eisenstadt mit einer Niederlassung in Angyalföldstraße 52, 4193 Hayrl, Österreich.

| Predicted | Gold |
|---|---|
| `Landesgerichts Eisenstadt` | `Landesgerichts Eisenstadt` |

**Missed by this rule (FN):**

- `Angyalföldstraße 52, 4193 Hayrl, Österreich` (address)

**Example 37** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_5`)


Unter Alver GmbH, beide Granglitzweg 11, 3251 Kroißenberg, Österreich, beide vertreten durch Dr. Michael Schneditz-Bolfras und andere Rechtsanwälte in Gmunden, wegen Bucheinsicht (in eventu Rechnungslegung) und Zahlung (Streitwert: 70.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Teilurteil des Oberlandesgerichts Linz als Berufungsgericht vom 17. Februar 2014, GZ 3 R 13/14y-90, womit das Urteil des Landesgerichts Wels vom 27. November 2013 (in der mit Beschluss vom 12. Dezember 2013 berichtigten Fassung), GZ 2 Cg 78/10p-82 und -84, abgeändert wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts Wels` | `Landesgerichts Wels` |

**Missed by this rule (FN):**

- `Unter Alver GmbH` (organisation)
- `Granglitzweg 11, 3251 Kroißenberg, Österreich` (address)
- `Dr. Michael Schneditz-Bolfras` (person)
- `Oberlandesgerichts Linz` (organisation)

**Example 38** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_79`)


Rechtliche Beurteilung DieRevisionist entgegen dem - den Obersten Gerichtshof nicht bindenden (§ 508 Abs 1 ZPO) - Ausspruch des Berufungsgerichts zulässig, weil das Berufungsgericht von der ständigen Rechtsprechung des Obersten Gerichtshofs zur Beurteilung von Kündigungserklärungen abweicht;

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)

**Example 39** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_108`)


Dabei wird übersehen, dass im Rechtsmittelverfahren vor dem Obersten Gerichtshof Verweise in der Revision bzw Revisionsbeantwortung auf Ausführungen in anderen Schriftsätzen (zB der Berufung) nach ständiger Rechtsprechung unzulässig und unbeachtlich sind (RIS-Justiz RS0043579 und RS0043616; vgl auch RS0007029).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 40** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Brigitte Martz, geboren am 16. November 1978, wegen Kontaktrechts des Vaters Dr. Gustav Thöning, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Madeleine Musialik, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

| Predicted | Gold |
|---|---|
| `Landesgerichts Wiener Neustadt` | `Landesgerichts Wiener Neustadt` |

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
- `Kosch & Partner Rechtsanwälte GmbH` (organisation)
- `Bezirksgerichts Wiener Neustadt` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 41** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_39`)


2.1 Der gegen den abändernden Teil der Rekursentscheidung gerichtete – nach Freistellung durch den Obersten Gerichtshof vomVater beantwortete– Revisionsrekurs ist hingegen zulässig und im Sinne einer Aufhebung berechtigt.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 42** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_16`)


Die Verhängung der Ordnungsstrafe hingegen sei grundsätzlich durch Rekurs an den Obersten Gerichtshof bekämpfbar.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 43** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_19`)


Mit dem dagegen erhobenen Rekurs an den Obersten Gerichtshof verband der Rechtsmittelwerber einen Ablehnungsantrag gegen die Vorsitzende und die beiden weiteren Mitglieder des 13.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 44** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_25`)


Der Beschluss ist daher, da dem Ablehnungsantrag nicht stattgegeben wurde, gemäß § 24 Abs 2 JN uneingeschränkt an den Obersten Gerichtshof anfechtbar.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 45** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_27`)


Vor Eingehen auf das Rechtsmittel selbst ist vorerst die Frage zu prüfen, ob die Rekursschrift von einem Rechtsanwalt zu fertigen und daher durch den Obersten Gerichtshof das Verbesserungsverfahren einzuleiten wäre.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 46** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_3`)


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

**Example 47** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_26`)


Mit Beschluss des Erstgerichts vom 29. 11. 2013 (zugestellt am 9. 12. 2013) wurde dem Vertreter des Vaters in der Folge auch der ordentliche Revisionsrekurs „vom31. 1. 2013(ON 82)“ zur Verbesserung binnen 14 Tagen (gemäß dem Beschluss 10 Ob 29/13g [ON 93]) zurückgestellt. Den am 10. 12. 2013 im ERV eingebrachten verbesserten Revisionsrekurs legt das Erstgericht neuerlich dem Obersten Gerichtshof zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 48** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_35`)


das ordentliche Rechtsmittel ist jedoch entgegen dem - gemäß § 71 Abs 1 AußStrG den Obersten Gerichtshof nicht bindenden - Ausspruch des Rekursgerichts wegen Fehlens einer erheblichen Rechtsfrage nicht zulässig.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 49** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_3`)


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

**Example 50** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_10`)


Das Erstgericht wertete dieses Rechtsmittel als außerordentlichen Revisionsrekurs und ging davon aus, dass dieser sogleich dem Obersten Gerichtshof vorzulegen sei.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 51** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_15`)


Daraufhin legte das Erstgericht das Rechtsmittel dem Obersten Gerichtshof zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 52** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_20`)


Steht dem Rechtsmittelwerber nur der Rechtsbehelf der Zulassungsvorstellung nach § 63 Abs 1 AußStrG zur Verfügung, ist das Rechtsmittel nicht dem Obersten Gerichtshof vorzulegen, weil im Streitwertbereich des § 63 AußStrG Rechtsmittel gegen Entscheidungen, gegen die nach dem Ausspruch des § 59 Abs 1 Z 2 AußStrG der ordentliche Revisionsrekurs nicht zulässig ist, dem Gericht zweiter Instanz vorzulegen sind (§ 69 Abs 3 AußStrG).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 53** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Wiener Neustadt` | `Landesgerichts Wiener Neustadt` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Korn` (person)
- `Langhansl+Antonewitz Chemie AG` (organisation)
- `Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich` (address)
- `Poinstingl & Partner Rechtsanwälte OG` (organisation)
- `Drau-Pharma GmbH` (organisation)
- `Strazzegasse 12, 8762 Oberzeiring, Österreich` (address)
- `Mag. Johannes Bügler` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 54** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_40`)


Der Rekurs an den Obersten Gerichtshof sei zulässig, weil eine Klarstellung geboten erscheine, dass die bei Zwischenurteilen angenommene erweiterte Bindungswirkung auf die vorliegende Konstellation einer späteren Klagsausdehnung nach einem von der beklagten Partei unbekämpft gebliebenen Ausspruch über einen Teilausspruch keine Anwendung finde.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 55** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_44`)


Rechtliche Beurteilung Der Rekurs ist entgegen dem - den Obersten Gerichtshof nicht bindenden (§ 526 Abs 2 ZPO) - Ausspruch des Berufungsgerichts nicht zulässig, weil die im Zulassungsausspruch umschriebene Rechtsfrage nicht die Qualifikation des § 502 Abs 1 ZPO erfüllt. 1. Die klagende Partei macht geltend, dass das Erstgericht einen hypothetischen Kausalverlauf im Fall pflichtgemäßer Aufklärung sehr wohl thematisiert habe.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 56** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_54`)


Auch bei Teilurteilen sei eine Bindungswirkung vom Obersten Gerichtshof bejaht worden, wenn sowohl die Identität der Parteien als auch des rechtserzeugenden Sachverhalts gegeben sei, aber anstelle der inhaltlichen und wörtlichen Identität des Begehrens ein im Gesetz gegründeter Sachzusammenhang zwischen beiden Begehren bestehe.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 57** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_3`)


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

**Example 58** (doc_id: `deanon_260716_TRAIN/10Ob3_12g`) (sent_id: `deanon_260716_TRAIN/10Ob3_12g_3`)


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

**Example 59** (doc_id: `deanon_260716_TRAIN/10Ob3_12g`) (sent_id: `deanon_260716_TRAIN/10Ob3_12g_32`)


Demzufolge bestand für die zweite Instanz kein Hindernis, in der Berufungsentscheidung - für den Obersten Gerichtshof mangels offenkundiger Überbewertung bindend (RIS-Justiz RS0042515;

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 60** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_24`)


Der Revisionsrekurs ist entgegen dem – den Obersten Gerichtshof nicht bindenden (§ 71 Abs 1 AußStrG) – Ausspruch des Rekursgerichts nicht zulässig.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 61** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_51`)


Ein Zeitraum von „mehreren Jahren“, wie er bislang vom Obersten Gerichtshof zu beurteilen war, liegt somit nicht vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 62** (doc_id: `deanon_260716_TRAIN/10Ob41_14y`) (sent_id: `deanon_260716_TRAIN/10Ob41_14y_24`)


Die Zulassungsvorstellung ist mit der Ausführung des ordentlichen Revisionsrekurses zu verbinden (der gemäß § 65 Abs 3 Z 5 AußStrG von einem Rechtsanwalt zu unterfertigen ist) und - selbst wenn sie an den Obersten Gerichtshof gerichtet ist - zunächst demfunktional zuständigenRekursgericht zur Entscheidung über den Antrag auf Abänderung des Zulässigkeitsausspruchs zurückzuleiten;

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 63** (doc_id: `deanon_260716_TRAIN/10Ob41_14y`) (sent_id: `deanon_260716_TRAIN/10Ob41_14y_26`)


4. Der vom Rechtsmittelwerber eingebrachte Revisionsrekurs durfte daher nicht dem Obersten Gerichtshof vorgelegt werden, weil im Streitwertbereich des § 63 AußStrG Rechtsmittel gegen Entscheidungen, gegen die nach dem Ausspruch nach § 59 Abs 1 Z 2 AußStrG der ordentliche Revisionsrekurs nicht zulässig ist, dem Gericht zweiter Instanz vorzulegen sind (§ 69 Abs 3 AußStrG).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 64** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_5`)


Dr. Felix Cornils, Niederlande, beide vertreten durch Tramposch & Partner, Rechtsanwälte KG in Innsbruck, gegen die beklagte Partei Mag.a Constanze Rizzo, vertreten durch König Ermacora Klotz & Partner, Rechtsanwälte in Innsbruck, wegen je 15.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 1. Juli 2020, GZ 10 R 16/20h-49, mit dem das Urteil des Landesgerichts Innsbruck vom 6. Februar 2020, GZ 41 Cg 11/19i-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Dr. Felix Cornils` (person)
- `Tramposch & Partner, Rechtsanwälte KG` (organisation)
- `Mag.a Constanze Rizzo` (person)
- `Oberlandesgerichts Innsbruck` (organisation)

**Example 65** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_36`)


Es begründet daher keine vom Obersten Gerichtshof aufzugreifende Fehlbeurteilung, wenn das Berufungsgericht nicht nur eine intakte Geschwisterbeziehung, sondern eine intensive Gefühlsgemeinschaft, die jener in einer Kernfamilie annähernd entspricht, angenommen hat.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 66** (doc_id: `deanon_260716_TRAIN/10Ob43_19z`) (sent_id: `deanon_260716_TRAIN/10Ob43_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Othmar Mertl, vertreten durch Nitsch Pajor Zöllner Rechtsanwälte OG in Mödling, gegen die beklagte Partei Stadtgemeinde Malik Fridt, vertreten durch Krist Bubits Rechtsanwälte OG in Mödling, wegen 1.) 21.216,92 EUR sA und 2.) Feststellung (Streitwert: 2.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Februar 2019, GZ 12 R 96/18b-36, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Wiener Neustadt vom 31. August 2018, GZ 20 Cg 86/17h-31, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Wiener Neustadt` | `Landesgerichts Wiener Neustadt` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Othmar Mertl` (person)
- `Nitsch Pajor Zöllner Rechtsanwälte OG` (organisation)
- `Malik Fridt` (person)
- `Krist Bubits Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 67** (doc_id: `deanon_260716_TRAIN/10Ob43_19z`) (sent_id: `deanon_260716_TRAIN/10Ob43_19z_46`)


Rechtliche Beurteilung Die Revision ist entgegen dem den Obersten Gerichtshof nicht bindenden Zulassungsausspruch unzulässig.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 68** (doc_id: `deanon_260716_TRAIN/10Ob57_13z`) (sent_id: `deanon_260716_TRAIN/10Ob57_13z_26`)


Rechtliche Beurteilung Der Revisionsrekurs ist entgegen dem - den Obersten Gerichtshof nicht bindenden (§ 71 Abs 1 AußStrG) - Ausspruch des Rekursgerichts nicht zulässig.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 69** (doc_id: `deanon_260716_TRAIN/10Ob6_24s`) (sent_id: `deanon_260716_TRAIN/10Ob6_24s_3`)


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

**Example 70** (doc_id: `deanon_260716_TRAIN/10Ob6_24s`) (sent_id: `deanon_260716_TRAIN/10Ob6_24s_30`)


[8] Dagegen richtet sich der vomKlägererhobene, einheitlich als „außerordentlich“ bezeichneteRevisionsrekurs, den das Erstgericht dem Obersten Gerichtshof zur Entscheidung vorlegte.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 71** (doc_id: `deanon_260716_TRAIN/10Ob6_24s`) (sent_id: `deanon_260716_TRAIN/10Ob6_24s_62`)


Eine solche den Obersten Gerichtshof bindende, nicht weiter anfechtbare Entscheidung liegt auch dann vor, wenn die zweite Instanz – wie im vorliegenden Fall – den behaupteten Verstoß gegen leitende Verfahrensgrundsätze unter dem vom Kläger geltend gemachten Rekursgrund der Mangelhaftigkeit des Verfahrens behandelt und verneint hat.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 72** (doc_id: `deanon_260716_TRAIN/10Ob6_24s`) (sent_id: `deanon_260716_TRAIN/10Ob6_24s_72`)


Dem Obersten Gerichtshof ist daher die Überprüfung, ob das Rekursgericht das Vorliegen des Nichtigkeitsgrundes zu Recht verneint hat, verwehrt.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 73** (doc_id: `deanon_260716_TRAIN/10Ob6_24s`) (sent_id: `deanon_260716_TRAIN/10Ob6_24s_108`)


Er vermag solcherart keine vom Obersten Gerichtshof aufzugreifende Fehlbeurteilung des Rekursgerichts aufzuzeigen.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 74** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_3`)


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

**Example 75** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_3`)


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

**Example 76** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_4`)


In Stattgebung der Nichtigkeitsbeschwerde wird das angefochtene Urteil aufgehoben, eine neue Hauptverhandlung angeordnet und die Sache an das Landesgericht Salzburg verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Example 77** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_3`)


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

**Example 78** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_4`)


Gründe:  Rechtliche Beurteilung Mit dem angefochtenen Beschluss wurde die von Richard Lilienfein erhobene Nichtigkeitsbeschwerde gegen das Urteil des Landesgerichts Salzburg vom 17. Juni 2011, GZ 40 Hv 147/10g-538, als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Richard Lilienfein` (person)

**Example 79** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_6`)


Gegen das Urteil eines Einzelrichters sieht die Strafprozessordnung (von den Befugnissen der Generalprokuratur abgesehen) keine „Nichtigkeitsbeschwerde an den Obersten Gerichtshof“ vor (§§ 280, 489 Abs 1 StPO);

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 80** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_8`)


Die von Richard Leissner gegen das ihn freisprechende Urteil des Einzelrichters des Landesgerichts Salzburg vom 17. Juni 2011 ausdrücklich an den Obersten Gerichtshof gerichtete Nichtigkeitsbeschwerde wurde vom Erstgericht zutreffend gemäß § 285a Z 1 StPO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Missed by this rule (FN):**

- `Richard Leissner` (person)

**Example 81** (doc_id: `deanon_260716_TRAIN/11Os59_13f`) (sent_id: `deanon_260716_TRAIN/11Os59_13f_3`)


Kopf Der Oberste Gerichtshof hat am 28. Mai 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Kurzthaler als Schriftführer, in der Strafsache gegen Andreas Schiessl wegen des Verbrechens des schweren Raubes nach §§ 15, 142 Abs 1, 143 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Wiener Neustadt als Schöffengericht vom 28. Februar 2013, GZ 37 Hv 158/12k-13, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Wiener Neustadt` | `Landesgerichts Wiener Neustadt` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Zehetner` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Mag. Lendl` (person)
- `Mag. Michel` (person)
- `Dr. Oshidari` (person)
- `Mag. Kurzthaler` (person)
- `Andreas Schiessl` (person)

**Example 82** (doc_id: `deanon_260716_TRAIN/11Os67_16m`) (sent_id: `deanon_260716_TRAIN/11Os67_16m_3`)


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

**Example 83** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_4`)


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

**Example 84** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_5`)


Gründe:  Rechtliche Beurteilung Der gegen den Beschluss des Oberlandesgerichts Wien, mit dem eine Beschwerde des Gerald Wandscheer gegen den Beschluss des Landesgerichts Korneuburg vom 21. Februar 2018, GZ 606 Hv 1/17k-94, als verspätet zurückgewiesen worden war, gerichtete „Einspruch“ war ebenso zurückzuweisen, weil gegen derartige Entscheidungen eines Beschwerdegerichts kein weiterer Rechtszug vorgesehen ist (§ 89 Abs 6 StPO).

| Predicted | Gold |
|---|---|
| `Landesgerichts Korneuburg` | `Landesgerichts Korneuburg` |

**Missed by this rule (FN):**

- `Oberlandesgerichts Wien` (organisation)
- `Gerald Wandscheer` (person)

**Example 85** (doc_id: `deanon_260716_TRAIN/12Ns94_11m`) (sent_id: `deanon_260716_TRAIN/12Ns94_11m_3`)


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

**Example 86** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__9`)


Unter einem erging der Beschluss, gemäß § 494a Abs 1 Z 2 StPO vom Widerruf der zum AZ 36 Hv 118/05p des Landesgerichts Innsbruck und zum AZ 3 U 350/06d des Bezirksgerichts Kufstein jeweils gewährten bedingten Strafnachsicht abzusehen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Bezirksgerichts Kufstein` (organisation)

**Example 87** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_3`)


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

**Example 88** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_4`)


In Stattgebung der Nichtigkeitsbeschwerde wird das angefochtene Urteil, das im Übrigen unberührt bleibt, im Ausspruch über den Verfall aufgehoben, soweit er sich auf einen 35.353,95 Euro übersteigenden Betrag bezieht, und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an den Einzelrichter des Landesgerichts Innsbruck verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

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

**Example 4** (doc_id: `deanon_260716_TRAIN/10Ob30_19p`) (sent_id: `deanon_260716_TRAIN/10Ob30_19p_3`)


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

**Example 5** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_3`)


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

**Example 6** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_3`)


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

**Example 7** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_5`)


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

**Example 8** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_6`)


Text Gründe: Soweit für die Behandlung der Nichtigkeitsbeschwerde zur Wahrung des Gesetzes von Bedeutung wurde Thomas Maksym mit Urteil des Landesgerichts Krems an der Donau vom 13. März 2018 (ON 72) des Verbrechens des schweren gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 2 und Z 5, 129 Abs 1 Z 1, Z 2 und Z 3, 130 Abs 2 zweiter Fall und 15 StGB (I./) sowie der Vergehen der Urkundenunterdrückung nach § 229 Abs 1 StGB (II./) und des Betrugs nach § 146 StGB (III./) schuldig erkannt und zu einer Freiheitsstrafe verurteilt. Aus Anlass der (allein aufrechterhaltenen) Berufung des Angeklagten wegen des Ausspruchs über die Strafe (ON 86) hob der zuständige 21.

**False Positives:**

- `Landesgerichts Krems` — partial — pred is substring of gold: `Landesgerichts Krems an der Donau`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Thomas Maksym`(person)
- `Landesgerichts Krems an der Donau`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_10`)


Im zweiten Rechtsgang sprach die Einzelrichterin des Landesgerichts Krems an der Donau Thomas Muthardt mit Urteil vom 8. August 2018 (ON 100) neuerlich anklagekonform schuldig und verurteilte ihn zu einer Freiheitsstrafe.

**False Positives:**

- `Landesgerichts Krems` — partial — pred is substring of gold: `Landesgerichts Krems an der Donau`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Krems an der Donau`(organisation)
- `Thomas Muthardt`(person)

**Example 10** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_13`)


Dazu führte er aus, dass die genannten Richter das Urteil des Landesgerichts Krems an der Donau vom 13. März 2018 (ON 72) in amtswegiger Wahrnehmung des Nichtigkeitsgrundes des § 281 Abs 1 Z 9 lit a [der Sache nach Z 10] StPO „großteils aufgehoben“ und „dabei“ „die Tatfrage mit Hinweis auf die Strafbarkeit des angelasteten Verhaltens indizierende Verfahrensergebnisse mit voller Kognitionsbefugnis [beurteilt] und […] beweiswürdigend Stellung bezogen“ hätten.

**False Positives:**

- `Landesgerichts Krems` — partial — pred is substring of gold: `Landesgerichts Krems an der Donau`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Krems an der Donau`(organisation)

</details>

---

## `KGCompanies` 🏆

**F1:** 0.002 | **Precision:** 0.172 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `b006fbcc`  
**Description:**
Matches KG companies, strictly excluding legal context words like 'Anteile an der', 'der', 'bei', 'in', 'von', 'für', 'nach', 'vor', 'über', 'unter', 'mit', 'aus', 'auf', 'zu', 'um', 'bis', 'seit', 'durch', 'gegen', 'ohne', '§', and single letter names followed by KG.

**Content:**
```
(?<![A-Za-z])(?<!Anteile\s)(?<!der\s)(?<!an\s)(?<!bei\s)(?<!in\s)(?<!von\s)(?<!für\s)(?<!nach\s)(?<!vor\s)(?<!über\s)(?<!unter\s)(?<!mit\s)(?<!aus\s)(?<!auf\s)(?<!zu\s)(?<!um\s)(?<!bis\s)(?<!seit\s)(?<!durch\s)(?<!gegen\s)(?<!ohne\s)(?<!§\s)(?<![A-Z]\s)([A-Z][A-Za-z0-9\s&\-]{2,40}\s+KG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.172 | 0.001 | 0.002 | 29 | 5 | 24 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 24 | 3717 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_4`)


Norsee Technologien GmbH & Co KG und 2.

| Predicted | Gold |
|---|---|
| `Norsee Technologien GmbH & Co KG` | `Norsee Technologien GmbH & Co KG` |

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Brigitte Martz, geboren am 16. November 1978, wegen Kontaktrechts des Vaters Dr. Gustav Thöning, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Madeleine Musialik, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

| Predicted | Gold |
|---|---|
| `Pieler & Pieler & Partner KG` | `Pieler & Pieler & Partner KG` |

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
- `Dr. Madeleine Musialik` (person)
- `Kosch & Partner Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Wiener Neustadt` (organisation)
- `Bezirksgerichts Wiener Neustadt` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_6`)


Text Gründe: Mit dem angefochtenen Urteil wurden Bernhard Berti und Norbert Wierich von der wider sie erhobenen Anklage, sie hätten am 7. Februar 2009 in Sebastian-Stief-Gasse 48, 2632 Altendorf, Österreich /Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der Hauenschildt&Mesarec Medien GesmbH & Co KG, Susanne Schwarzhuber, durch die Vorgabe, die Donau-Transport GmbH sei eine zahlungsfähige Leasingnehmerin, somit durch Täuschung über Tatsachen, zum Abschluss eines Leasingvertrags über ein Rennfahrzeug für die Dauer von 24 Monaten zu einem monatlichen Entgelt von 10.698,10 Euro, somit zu einer Handlung verleitet, welche die TraunTouristik Werke GesmbH & Co KG in einem 50.000 Euro übersteigenden Betrag von insgesamt 235.358,20 Euro am Vermögen schädigte, gemäß § 259 Z 3 StPO (verfehlt auch von der rechtlichen Kategorie; vglLendl, WK-StPO § 259 Rz 1) freigesprochen.

| Predicted | Gold |
|---|---|
| `TraunTouristik Werke GesmbH & Co KG` | `TraunTouristik Werke GesmbH & Co KG` |

**Missed by this rule (FN):**

- `Bernhard Berti` (person)
- `Norbert Wierich` (person)
- `Sebastian-Stief-Gasse 48, 2632 Altendorf, Österreich` (address)
- `Hauenschildt&Mesarec Medien GesmbH & Co KG` (organisation)
- `Susanne Schwarzhuber` (person)
- `Donau-Transport GmbH` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_9`)


Am 7. Februar 2009 schlossen die Angeklagten namens der genannten Gesellschaft mit der von Susanna Steen vertretenen Prentl Handel GesmbH & Co KG einen Leasingvertrag über einen Rennwagen samt Ersatzteilpaket.

| Predicted | Gold |
|---|---|
| `Prentl Handel GesmbH & Co KG` | `Prentl Handel GesmbH & Co KG` |

**Missed by this rule (FN):**

- `Susanna Steen` (person)

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

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_5`)


Text Begründung: Der Kläger erwarb als Verbraucher im Juni 2003 über Vermittlung eines selbständigen Vermögensberaters Kommanditanteile an der GBJU Getränke GmbH & Co KG im Nominale von 17.000 EUR zuzüglich 850 EUR Agio.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `GBJU Getränke GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `GBJU Getränke GmbH & Co KG`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_6`)


Text Gründe: Mit dem angefochtenen Urteil wurden Bernhard Berti und Norbert Wierich von der wider sie erhobenen Anklage, sie hätten am 7. Februar 2009 in Sebastian-Stief-Gasse 48, 2632 Altendorf, Österreich /Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der Hauenschildt&Mesarec Medien GesmbH & Co KG, Susanne Schwarzhuber, durch die Vorgabe, die Donau-Transport GmbH sei eine zahlungsfähige Leasingnehmerin, somit durch Täuschung über Tatsachen, zum Abschluss eines Leasingvertrags über ein Rennfahrzeug für die Dauer von 24 Monaten zu einem monatlichen Entgelt von 10.698,10 Euro, somit zu einer Handlung verleitet, welche die TraunTouristik Werke GesmbH & Co KG in einem 50.000 Euro übersteigenden Betrag von insgesamt 235.358,20 Euro am Vermögen schädigte, gemäß § 259 Z 3 StPO (verfehlt auch von der rechtlichen Kategorie; vglLendl, WK-StPO § 259 Rz 1) freigesprochen.

**False Positives:**

- `Mesarec Medien GesmbH & Co KG` — partial — pred is substring of gold: `Hauenschildt&Mesarec Medien GesmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bernhard Berti`(person)
- `Norbert Wierich`(person)
- `Sebastian-Stief-Gasse 48, 2632 Altendorf, Österreich`(address)
- `Hauenschildt&Mesarec Medien GesmbH & Co KG`(organisation)
- `Susanne Schwarzhuber`(person)
- `Donau-Transport GmbH`(organisation)
- `TraunTouristik Werke GesmbH & Co KG`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/1Ob152_24w`) (sent_id: `deanon_260716_TRAIN/1Ob152_24w_3`)


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

**Example 3** (doc_id: `deanon_260716_TRAIN/1Ob29_20a`) (sent_id: `deanon_260716_TRAIN/1Ob29_20a_19`)


Der Mann hat sich an einem Immobilienprojekt, das von einer GmbH & Co KG verwirklicht wird, beteiligt.

**False Positives:**

- `GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_260716_TRAIN/2Ob193_23f`) (sent_id: `deanon_260716_TRAIN/2Ob193_23f_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte Hon.-Prof. PD Dr. Rassi, MMag. Sloboda, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Denise Markstaler, vertreten durch Weber Rechtsanwälte GmbH & Co KG in Wien 1, gegen die beklagte Partei Rut Adamheit, vertreten durch BEURLE Rechtsanwälte GmbH & Co KG in Linz, wegen Herausgabe (Streitwert 1.525.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2023, GZ 2 R 87/23m-32, mit dem das Urteil des Landesgerichts Salzburg vom 5. April 2023, GZ 8 Cg 9/23a-22, aufgehoben wurde zu Recht erkannt:  Spruch

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Weber Rechtsanwälte GmbH & Co KG`
- `GmbH & Co KG` — similar text (different position): `Weber Rechtsanwälte GmbH & Co KG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Grohmann`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `MMag. Sloboda`(person)
- `Dr. Kikinger`(person)
- `Mag. Fitz`(person)
- `Denise Markstaler`(person)
- `Weber Rechtsanwälte GmbH & Co KG`(organisation)
- `Rut Adamheit`(person)
- `BEURLE Rechtsanwälte GmbH & Co KG`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Salzburg`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/2Ob194_19x`) (sent_id: `deanon_260716_TRAIN/2Ob194_19x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden und den Hofrat Dr. Musger, die Hofrätin Dr. Solé und die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Haßtenteufel Umwelt GmbH & Co KG, Peter Zauner Weg 324, 5273 Wesen, Österreich, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Klagenfurt, gegen die beklagte Partei Isaak Tomzak, vertreten durch Dr. Maximilian Motschiunig, Rechtsanwalt in Klagenfurt, wegen Vertragsaufhebung und Abgabe einer Willenserklärung (Streitwert 35.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 1. Oktober 2019, GZ 2 R 141/19a, 2 R 142/19y-95, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Umwelt GmbH & Co KG` — partial — pred is substring of gold: `Haßtenteufel Umwelt GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Veith`(person)
- `Dr. Musger`(person)
- `Dr. Solé`(person)
- `Dr. Nowotny`(person)
- `Mag. Pertmayr`(person)
- `Haßtenteufel Umwelt GmbH & Co KG`(organisation)
- `Peter Zauner Weg 324, 5273 Wesen, Österreich`(address)
- `Gheneff - Rami - Sommer Rechtsanwälte OG`(organisation)
- `Isaak Tomzak`(person)
- `Dr. Maximilian Motschiunig`(person)
- `Oberlandesgerichts Graz`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/3Ob114_14g`) (sent_id: `deanon_260716_TRAIN/3Ob114_14g_4`)


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

**Example 7** (doc_id: `deanon_260716_TRAIN/3Ob114_14g`) (sent_id: `deanon_260716_TRAIN/3Ob114_14g_5`)


Begründung:  Rechtliche Beurteilung Die Erstklägerin (eine Rechtsanwalts KG), der Zweitkläger (deren Komplementär) und die Mutter des Zweitklägers (in Hinkunft: Pensionsberechtigte) führten als Kläger und Widerbeklagte ein Schiedsverfahren gegen den (hier) Beklagten (als ausgeschiedenen Komplementär) als Beklagten und Widerkläger, das mit einem Schiedsspruch vom 2. Mai 2011 endete.

**False Positives:**

- `Rechtsanwalts KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_260716_TRAIN/3Ob1_18w`) (sent_id: `deanon_260716_TRAIN/3Ob1_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Roch und Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Druck Steinnex GmbH, Josef-Wessely-Straße 15, 4171 Unterriedl, Österreich, vertreten durch Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG in Wien, gegen die beklagten Parteien 1.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hoch`(person)
- `Dr. Roch`(person)
- `Dr. Rassi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Druck Steinnex GmbH`(organisation)
- `Josef-Wessely-Straße 15, 4171 Unterriedl, Österreich`(address)
- `Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/3Ob209_21p`) (sent_id: `deanon_260716_TRAIN/3Ob209_21p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei APHU Solar GmbH & Co KG, Hochkreuth 39, 8144 Bischofegg, Österreich, vertreten durch DDr. Heinz Dietmar Schimanko, Rechtsanwalt in Wien, gegen die beklagte Partei Traun-Transport GmbH, Stauderstraße 30, 8200 Pircha, Österreich, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH & Co KG in Wien, wegen 7.906,82 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 7. Juni 2021, GZ 38 R 66/21v-16, mit dem das Urteil des Bezirksgerichts Favoriten vom 19. Jänner 2021, GZ 3 C 503/20f-12, abgeändert wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Partei APHU Solar GmbH & Co KG` — partial — gold is substring of pred: `APHU Solar GmbH & Co KG`
- `GmbH & Co KG` — similar text (different position): `APHU Solar GmbH & Co KG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Hon.-Prof. Dr. Brenn`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Dr. Stefula`(person)
- `APHU Solar GmbH & Co KG`(organisation)
- `Hochkreuth 39, 8144 Bischofegg, Österreich`(address)
- `DDr. Heinz Dietmar Schimanko`(person)
- `Traun-Transport GmbH`(organisation)
- `Stauderstraße 30, 8200 Pircha, Österreich`(address)
- `Bichler Zrzavy Rechtsanwälte GmbH & Co KG`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Favoriten`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/3Ob223_19v`) (sent_id: `deanon_260716_TRAIN/3Ob223_19v_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Priv.-Doz. Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr, Dr. Kodek und Mag. Wessely-Kristöfel als weitere Richter in der Exekutionssache der betreibenden Partei WestLebensmittel Betriebe GesmbH, Adalbert-Stifter-Platz 4, 3143 Gattring-Raking, Österreich, vertreten durch Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG in Wien, gegen die verpflichtete Partei Dkfm.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Roch`(person)
- `Priv.-Doz. Dr. Rassi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Mag. Wessely-Kristöfel`(person)
- `WestLebensmittel Betriebe GesmbH`(organisation)
- `Adalbert-Stifter-Platz 4, 3143 Gattring-Raking, Österreich`(address)
- `Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/3Ob45_19t`) (sent_id: `deanon_260716_TRAIN/3Ob45_19t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Roch und Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Mag. Daniel Kutluk, vertreten durch Dr. Johannes Eltz, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Ferdinand Rittgerott, vertreten durch Piaty Müller-Mezin Schöller Rechtsanwälte GmbH & Co KG in Graz, wegen Einwendungen gegen den Anspruch (§ 35 EO), über die „außerordentliche“ Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 25. September 2018, GZ 4 R 102/18a-11, womit das Urteil des Bezirksgerichts Graz-West vom 27. Februar 2018, GZ 211 C 2/17g-7, bestätigt wurde, den Beschluss gefasst:  Spruch Die „außerordentliche“ Revision wird zurückgewiesen.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Piaty Müller-Mezin Schöller Rechtsanwälte GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hoch`(person)
- `Dr. Roch`(person)
- `Dr. Rassi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Mag. Daniel Kutluk`(person)
- `Dr. Johannes Eltz`(person)
- `Mag. Ferdinand Rittgerott`(person)
- `Piaty Müller-Mezin Schöller Rechtsanwälte GmbH & Co KG`(organisation)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)
- `Bezirksgerichts Graz-West`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/3Ob49_11v`) (sent_id: `deanon_260716_TRAIN/3Ob49_11v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie durch den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Julius ZYR Automotive GmbH & Co KG, Schamingstraße 16, 8262 Reigersberg, Österreich, vertreten durch Dr. Wolfgang Dartmann und andere Rechtsanwälte in Linz, wider die beklagten Parteien 1. Friedrich Strahsburg und 2.

**False Positives:**

- `Partei Julius ZYR Automotive GmbH & Co KG` — partial — gold is substring of pred: `ZYR Automotive GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Prückner`(person)
- `Hon.-Prof. Dr. Neumayr`(person)
- `Dr. Lovrek`(person)
- `Dr. Jensik`(person)
- `Dr. Roch`(person)
- `ZYR Automotive GmbH & Co KG`(organisation)
- `Schamingstraße 16, 8262 Reigersberg, Österreich`(address)
- `Dr. Wolfgang Dartmann`(person)
- `Friedrich Strahsburg`(person)

**Example 13** (doc_id: `deanon_260716_TRAIN/4Ob119_22m`) (sent_id: `deanon_260716_TRAIN/4Ob119_22m_3`)


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

**Example 14** (doc_id: `deanon_260716_TRAIN/4Ob196_10t`) (sent_id: `deanon_260716_TRAIN/4Ob196_10t_4`)


Monderdorf Cloud GmbH, R.-Hamerling-Gasse 4, 6373 Jochberg, Österreich, beide vertreten durch Ruggenthaler Rechtsanwalts KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 62.000 EUR) über den außerordentlichen Revisionsrekurs der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Wien vom 20. September 2010, GZ 30 R 29/10w-9, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rechtsanwalts KG` — partial — pred is substring of gold: `Ruggenthaler Rechtsanwalts KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Monderdorf Cloud GmbH`(organisation)
- `R.-Hamerling-Gasse 4, 6373 Jochberg, Österreich`(address)
- `Ruggenthaler Rechtsanwalts KG`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/5Ob146_16f`) (sent_id: `deanon_260716_TRAIN/5Ob146_16f_3`)


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

**Example 16** (doc_id: `deanon_260716_TRAIN/5Ob71_24p`) (sent_id: `deanon_260716_TRAIN/5Ob71_24p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Mag. Wurzer als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Painsi, Dr. Weixelbraun-Mohr, Dr. Steger und Dr. Pfurtscheller als weitere Richter in der Rechtssache der klagenden Partei Josefine Fretschner, vertreten durch die Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei AlpenDerlogverEvent GmbH, Am Kröpflmühlerberg 93, 3925 Kleinpertenschlag, Österreich, vertreten durch die Wolf Theiss Rechtsanwälte GmbH & Co KG in Wien, wegen 7.140 EUR und Feststellung (Streitwert 2.000 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Steyr als Berufungsgericht vom 8. Februar 2024, GZ 1 R 120/23z-43, mit dem das Urteil des Bezirksgerichts Steyr vom 28. September 2023, GZ 2 C 288/21x-39, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das Verfahren über die Revision der beklagten Partei wird bis zur Entscheidung des Gerichtshofs der Europäischen Union (EuGH) über die Vorabentscheidungsersuchen des Landgerichts Ravensburg (Deutschland) vom 9. November 2023, Rechtssache C-666/23, vom 9. November 2023, Rechtssache C-667/23, und vom 15. November 2023, Rechtssache C-668/23, unterbrochen.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Wolf Theiss Rechtsanwälte GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Mag. Wurzer`(person)
- `Mag. Painsi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Steger`(person)
- `Dr. Pfurtscheller`(person)
- `Josefine Fretschner`(person)
- `Poduschka Anwaltsgesellschaft mbH`(organisation)
- `AlpenDerlogverEvent GmbH`(organisation)
- `Am Kröpflmühlerberg 93, 3925 Kleinpertenschlag, Österreich`(address)
- `Wolf Theiss Rechtsanwälte GmbH & Co KG`(organisation)
- `Landesgerichts Steyr`(organisation)
- `Bezirksgerichts Steyr`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/6Ob139_19p`) (sent_id: `deanon_260716_TRAIN/6Ob139_19p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Balthasar Teske, vertreten durch Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG in Wien, gegen die beklagte Partei Prof. Dr. Roderich Claaßens, vertreten durch Brauneis Klauser Prändl Rechtsanwälte GmbH in Wien, wegen Rechnungslegung und Zahlung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 22. April 2019, GZ 14 R 152/18b-16, womit das Teilurteil des Landesgerichts für Zivilrechtssachen Wien vom 27. September 2018, GZ 4 Cg 50/17b-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schramm`(person)
- `Dr. Gitschthaler`(person)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. Nowotny`(person)
- `Dr. Faber`(person)
- `Balthasar Teske`(person)
- `Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG`(organisation)
- `Dr. Roderich Claaßens`(person)
- `Brauneis Klauser Prändl Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/6Ob146_18s`) (sent_id: `deanon_260716_TRAIN/6Ob146_18s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden und die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei RgR Dr.in Manuela Künemund, vertreten durch Mag. Max Verdino und andere Rechtsanwälte in St. Veit an der Glan, gegen die beklagte Partei Kleuß Maschinenbau GmbH, Friedensring 38, 9815 Penk, Österreich, vertreten durch PHH Prochaska Havranek Rechtsanwälte GmbH & Co KG in Wien, wegen 18.664,48 EUR und Feststellung, über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 6. Juni 2018, GZ 4 R 51/18d-12, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Klagenfurt vom 20. Februar 2018, GZ 28 Cg 75/17s-8, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `PHH Prochaska Havranek Rechtsanwälte GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schramm`(person)
- `Dr. Gitschthaler`(person)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. Nowotny`(person)
- `Dr. Faber`(person)
- `RgR Dr.in Manuela Künemund`(person)
- `Mag. Max Verdino`(person)
- `Kleuß Maschinenbau GmbH`(organisation)
- `Friedensring 38, 9815 Penk, Österreich`(address)
- `PHH Prochaska Havranek Rechtsanwälte GmbH & Co KG`(organisation)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts Klagenfurt`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/8Ob86_22p`) (sent_id: `deanon_260716_TRAIN/8Ob86_22p_3`)


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

**Example 20** (doc_id: `deanon_260716_TRAIN/9Ob68_22y`) (sent_id: `deanon_260716_TRAIN/9Ob68_22y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Dr. Hargassner, Mag. Korn, MMag. Sloboda und Dr. Annerl in der Rechtssache der klagenden Partei Niels Doerfel, vertreten durch Neubauer Fähnrich Rechtsanwälte GmbH & Co KG in Graz, gegen die beklagte Partei Gudrun Kovalschuk Gesellschaft m.b.H. (FN FN119735f ), FN297530m, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung und 19.490 EUR sA (Gesamtstreitwert: 19.490 EUR), über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 10. September 2019, GZ 4 R 89/19v-59, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 27. März 2019, GZ 20 Cg 15/18t-54, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Revisionsverfahren wird fortgesetzt.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Neubauer Fähnrich Rechtsanwälte GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Fichtenau`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hargassner`(person)
- `Mag. Korn`(person)
- `MMag. Sloboda`(person)
- `Dr. Annerl`(person)
- `Niels Doerfel`(person)
- `Neubauer Fähnrich Rechtsanwälte GmbH & Co KG`(organisation)
- `Gudrun Kovalschuk`(person)
- `FN119735f`(business_register_number)
- `FN297530m`(business_register_number)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/9ObA144_14p`) (sent_id: `deanon_260716_TRAIN/9ObA144_14p_3`)


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

## `CompanyGmbH_Generic` 🏆

**F1:** 0.016 | **Precision:** 0.127 | **Recall:** 0.009  

**Format:** `regex`  
**Rule ID:** `367f6453`  
**Description:**
Matches GmbH companies with strict name length (min 5 chars before suffix), excludes legal context words, and ensures full name capture including '& Co' suffixes.

**Content:**
```
(?<![A-Za-z])(?<!Die\s)(?<!Der\s)(?<!Das\s)(?<!Die\s)(?<!Der\s)(?<!Das\s)(?<!Gesellschafter\s)(?<!Gesellschafterinnen\s)(?<!Komplementärin\s)(?<!Komplementär\s)(?<!Geschäftsführer\s)(?<!Firma\s)(?<!der\s)(?<!Firmen\s)(?<!an\s)(?<!bei\s)(?<!in\s)(?<!von\s)(?<!für\s)(?<!nach\s)(?<!vor\s)(?<!über\s)(?<!unter\s)(?<!mit\s)(?<!aus\s)(?<!auf\s)(?<!zu\s)(?<!am\s)(?<!um\s)(?<!bis\s)(?<!seit\s)(?<!durch\s)(?<!gegen\s)(?<!ohne\s)(?<!§)(?<!\d)([A-Z][A-Za-z0-9\s&\-\.]{5,50}(?:GmbH|m\.b\.H\.|GmbH\s&\sCo\sKG|GmbH\s&\sCo\sOG|m\.b\.H\s&\sCo\sKG|m\.b\.H\s&\sCo\sOG|Steuerberatungs-\sund\sWirtschaftsprüfungsgesellschaft))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.127 | 0.009 | 0.016 | 275 | 35 | 240 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 35 | 240 | 3960 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_5`)


Unter Alver GmbH, beide Granglitzweg 11, 3251 Kroißenberg, Österreich, beide vertreten durch Dr. Michael Schneditz-Bolfras und andere Rechtsanwälte in Gmunden, wegen Bucheinsicht (in eventu Rechnungslegung) und Zahlung (Streitwert: 70.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Teilurteil des Oberlandesgerichts Linz als Berufungsgericht vom 17. Februar 2014, GZ 3 R 13/14y-90, womit das Urteil des Landesgerichts Wels vom 27. November 2013 (in der mit Beschluss vom 12. Dezember 2013 berichtigten Fassung), GZ 2 Cg 78/10p-82 und -84, abgeändert wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Unter Alver GmbH` | `Unter Alver GmbH` |

**Missed by this rule (FN):**

- `Granglitzweg 11, 3251 Kroißenberg, Österreich` (address)
- `Dr. Michael Schneditz-Bolfras` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Wels` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_9`)


Er trat deswegen im Mai 2018 an die Klägerin heran, um eine Regelung seiner „persönlichen Haftungen“ über „rund 500.000 EUR“ aus der „Bürgschaft Norallex-Heizung GmbH“ zu erreichen.

| Predicted | Gold |
|---|---|
| `Norallex-Heizung GmbH` | `Norallex-Heizung GmbH` |

**Example 2** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_6`)


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

**Example 3** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_8`)


Nach den wesentlichen Feststellungen (US 3 bis 6) befand sich die UAMA Analyse Consulting GmbH in der zweiten Jahreshälfte 2008 in erheblichen Zahlungsschwierigkeiten.

| Predicted | Gold |
|---|---|
| `UAMA Analyse Consulting GmbH` | `UAMA Analyse Consulting GmbH` |

**Example 4** (doc_id: `deanon_260716_TRAIN/1Ob105_18z`) (sent_id: `deanon_260716_TRAIN/1Ob105_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Familienrechtssache des Antragstellers Ludmilla Bonauer, vertreten durch die Korp Rechtsanwalts GmbH, Andorf, gegen die Antragsgegnerin Henriette Geißendorf, vertreten durch die Puttinger Vogl Rechtsanwälte GmbH, Ried im Innkreis, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts Wels als Rekursgericht vom 2. Mai 2018, GZ 21 R 50/18d-32, mit dem der Rekurs des Antragstellers gegen den Beschluss des Bezirksgerichts Grieskirchen vom 8. Jänner 2018, GZ 8 Fam 37/16i-26, zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Korp Rechtsanwalts GmbH` | `Korp Rechtsanwalts GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Ludmilla Bonauer` (person)
- `Henriette Geißendorf` (person)
- `Puttinger Vogl Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Wels` (organisation)
- `Bezirksgerichts Grieskirchen` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/1Ob127_14d`) (sent_id: `deanon_260716_TRAIN/1Ob127_14d_4`)


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

**Example 6** (doc_id: `deanon_260716_TRAIN/2Ob115_10s`) (sent_id: `deanon_260716_TRAIN/2Ob115_10s_5`)


Seecon Verlag GmbH, Krengasse 31, 3911 Marbach am Walde, Österreich, und 2. Mag. Lena Zikorski, beide vertreten durch die Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH in Wien, wegen jeweils 50.000,50 EUR sA (Klagen) und 483.000 EUR sA (Widerklagen), über die außerordentliche Revision der klagenden und widerbeklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. April 2010, GZ 15 R 257/09p-58, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Seecon Verlag GmbH` | `Seecon Verlag GmbH` |

**Missed by this rule (FN):**

- `Krengasse 31, 3911 Marbach am Walde, Österreich` (address)
- `Mag. Lena Zikorski` (person)
- `Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/3Ob166_25w`) (sent_id: `deanon_260716_TRAIN/3Ob166_25w_4`)


Eduard Mauderer, vertreten durch Mag. Sarah Abel, Rechtsanwältin in Salzburg, und 2. Schmiede Digital GmbH, Pöllmühle 139H, 2095 Drosendorf Stadt, Österreich, vertreten durch die Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, wegen 7.164,36 EUR sA und Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 10. Juli 2025, GZ 53 R 145/25t-18, mit dem das Teilurteil des Bezirksgerichts Salzburg vom 12. März 2025, GZ 31 C 1179/24h-12, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Schmiede Digital GmbH` | `Schmiede Digital GmbH` |

**Missed by this rule (FN):**

- `Eduard Mauderer` (person)
- `Mag. Sarah Abel` (person)
- `Pöllmühle 139H, 2095 Drosendorf Stadt, Österreich` (address)
- `Mahringer Steinwender Bestebner Rechtsanwälte OG` (organisation)
- `Landesgerichts Salzburg` (organisation)
- `Bezirksgerichts Salzburg` (organisation)

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

- `Partei Ober-Automotive GmbH` — partial — gold is substring of pred: `Ober-Automotive GmbH`

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

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie durch die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Hon.-Prof.in KzlR Iris Makowska, vertreten durch Skribe Rechtsanwaelte GmbH in Wien, gegen die beklagte Partei Dieter Apfelbacher Ltd, Am Fundbach 31w, 9170 Tratten, Österreich, wegen 400 EUR sA, über den Ordinationsantrag nach § 28 JN in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Rechtsanwaelte GmbH` — partial — pred is substring of gold: `Skribe Rechtsanwaelte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Hon.-Prof.in KzlR Iris Makowska`(person)
- `Skribe Rechtsanwaelte GmbH`(organisation)
- `Dieter Apfelbacher`(person)
- `Am Fundbach 31w, 9170 Tratten, Österreich`(address)
- `Bezirksgericht Schwechat`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_3`)


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

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_4`)


Text Begründung: Die klagende GmbH mit dem Sitz in Wien begehrt von der beklagten GmbH mit dem Sitz in Linz aus dem Titel des Schadenersatzes 174.624,53 EUR sA.

**False Positives:**

- `Die klagende GmbH` — no gold match — likely missing annotation
- `Sitz in Wien begehrt von der beklagten GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 6** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Rechtssache der klagenden Partei Mur Dorftalnex Technologien -GmbH, Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich, vertreten durch Dr. Peter Lechner und Dr. Hermann Pfurtscheller, Rechtsanwälte in Innsbruck, und ihrer Nebenintervenientin Ober Dertri GmbH, Hintereggweg 93, 2070 Kleinhöflein, Österreich, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Rudolf Ketelhut GmbH, Fiebrichgasse 17, 5120 Seeleiten, Österreich, vertreten durch Rechtsanwaltskanzlei Dr. Bernhard Hämmerle GmbH in Innsbruck, und ihrer Nebenintervenientin Völkertz Energie GmbH, Brunnbachweg 19, 4653 Mayersdorf, Österreich, vertreten durch Dr. Franz Pechmann, Rechtsanwalt in Wien, wegen 696.238,34 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck vom 2. Oktober 2009, GZ 4 R 108/09b-167, mit dem das Urteil des Landesgerichts Innsbruck vom 23. Februar 2009, GZ 41 Cg 228/01z-152, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

**False Positives:**

- `Partei Mur Dorftalnex Technologien -GmbH` — partial — gold is substring of pred: `Mur Dorftalnex Technologien -GmbH`
- `Nebenintervenientin Ober Dertri GmbH` — partial — gold is substring of pred: `Ober Dertri GmbH`
- `Partei Rudolf Ketelhut GmbH` — partial — gold is substring of pred: `Rudolf Ketelhut`
- `Energie GmbH` — partial — pred is substring of gold: `Völkertz Energie GmbH`

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

**Example 7** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Eva Abdelrahman, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei Hochenadel Immobilien GmbH, Ritterhof 11, 2661 Graben, Österreich, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Hochenadel Immobilien GmbH` — partial — gold is substring of pred: `Hochenadel Immobilien GmbH`
- `Rechtsanwalt GmbH` — partial — pred is substring of gold: `Lederer Rechtsanwalt GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 8** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Juri Gerstl GmbH, Mutten 18, 3251 Schauboden, Österreich, vertreten durch Dr. Ralph Trischler, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, sowie die Nebenintervenientin auf Seiten der beklagten Partei Bundesbeschaffung GmbH, 1020 Wien, Lassallestraße 9b, vertreten durch die Olischar Rechtsanwaltsgesellschaft mbH in Wien, wegen 15.535 EUR sA, über den Revisionsrekurs der klagenden Partei (Revisionsinteresse: 7.460 EUR), gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 23. Februar 2023, GZ 16 R 168/22a-20, mit welchem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 5. September 2022, GZ 11 Cg 48/22t-12, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Partei Juri Gerstl GmbH` — partial — gold is substring of pred: `Juri Gerstl`
- `Partei Bundesbeschaffung GmbH` — partial — gold is substring of pred: `Bundesbeschaffung GmbH`

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

**Example 9** (doc_id: `deanon_260716_TRAIN/10Ob18_13i`) (sent_id: `deanon_260716_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei SüdSanitär Gruppe GmbH, Rinzendorf 28, 4501 Lindach, Österreich, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Gruppe GmbH` — partial — pred is substring of gold: `SüdSanitär Gruppe GmbH`

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

- `Partei Akbayrak Metall GmbH` — partial — gold is substring of pred: `Akbayrak Metall GmbH`

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

- `Partei Heimcon Software GmbH` — partial — gold is substring of pred: `Heimcon Software GmbH`
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

**Example 12** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_4`)


Malik Schoch, geboren 7. November 2002, 2. 7. Juli 2025, geboren 10. Juli 2004, und 3. Alan Schindlmair, geboren 7. August 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Timon Schönswetter, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Rechtsanwalts GmbH` — partial — pred is substring of gold: `Doschek Rechtsanwalts GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Malik Schoch`(person)
- `7. November`(date)
- `7. Juli 2025`(date)
- `10. Juli`(date)
- `Alan Schindlmair`(person)
- `7. August`(date)
- `Mag. Florian Kucera`(person)
- `Mag. Timon Schönswetter`(person)
- `Doschek Rechtsanwalts GmbH`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Döbling`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_15`)


Mit Vertrag vom 28. 3. 2007 wurden die Lizenznehmerinnen nach Firmenänderung als übertragende Gesellschaften mit der Albrucklog Event GmbH als übernehmende Gesellschaft verschmolzen, die am 26.

**False Positives:**

- `Gesellschaften mit der Albrucklog Event GmbH` — partial — gold is substring of pred: `Albrucklog Event GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Albrucklog Event GmbH`(organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/10Ob28_19v`) (sent_id: `deanon_260716_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Bau Zorostfurt GmbH, Isbarystraße 47, 4152 Schölling, Österreich, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Buitenkamp und Rothauge Landwirtschaft GmbH, Gewerbegebiet Mathon 17, 3672 Reitern, Österreich, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Bau Zorostfurt GmbH` — partial — gold is substring of pred: `Bau Zorostfurt GmbH`
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

**Example 15** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_55`)


Die Verhandlungen bis zum Vergleichsabschluss beschränkten sich demnach durchgehend auf einen Nachlass bezüglich der dem Grunde und der Höhe nach unstrittigen Forderung aus der (vertraglichen) Haftung des Beklagten für die Schulden der GmbH.

**False Positives:**

- `Schulden der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_72`)


Zusammenfassend ergibt die Auslegung des Vergleichs, dass dieser nur die bis zu seinem Abschluss allein thematisierten Ansprüche aus der Haftung des Beklagten als Bürge und Zahler für die Verbindlichkeiten der GmbH, nicht aber etwaige andere, insbesondere deliktische Ansprüche der Klägerin umfasst.

**False Positives:**

- `Verbindlichkeiten der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


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

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_7`)


Text Begründung: [1] Die Klägerin (eine Rechtsanwalts-GmbH) erbrachte der Beklagten gegenüber (durch einen Rechtsanwalt und einen Rechtsanwaltsanwärter ohne Prüfung) Rechtsberatungs- und Vertretungsleistungen in einer gesellschaftsrechtlichen Streitigkeit unter Mitgesellschaftern sowie Rechtsberatungsleistungen zu einer Testaments- und Pflichtteilsanfechtung.

**False Positives:**

- `Rechtsanwalts-GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_10`)


Die Beklagte wies bei diesem Gespräch auch auf ihre angespannte wirtschaftliche Situation hin und dass sie im GmbH-Recht nicht so bewandert sei; sie gab an, dass sie eine Gewinnauszahlung aus der GmbH erreichen wolle.

**False Positives:**

- `Situation hin und dass sie im GmbH` — no gold match — likely missing annotation
- `Gewinnauszahlung aus der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 20** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Cassandra Wespi, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Bilek Lebensmittel GmbH in Liqu, Dreijochgasse 11, 4722 Stefansdorf, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Rechtsanwalt GmbH` — partial — pred is substring of gold: `Vogl Rechtsanwalt GmbH`
- `Partei Bilek Lebensmittel GmbH` — partial — gold is substring of pred: `Bilek Lebensmittel GmbH`
- `Kux Kispert & Eckert Rechtsanwalts GmbH` — partial — pred is substring of gold: `Wess Kux Kispert & Eckert Rechtsanwalts GmbH`

> overlaps gold: 3  |  likely missing annotation: 0

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

**Example 21** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Anleger als Kommanditisten an einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_6`)


Text Entscheidungsgründe: Mit Bescheid vom 26. 4. 2010 lehnte die beklagte Partei den Antrag des Klägers auf Gewährung der Kostenerstattung für die Inanspruchnahme der QVAO Planung GmbH (im Folgenden kurz: GmbH) laut Rechnungen vom 2. 10. 2009 und 6. 11. 2009 in Höhe von insgesamt 540 EUR ab.

**False Positives:**

- `Inanspruchnahme der QVAO Planung GmbH` — partial — gold is substring of pred: `QVAO Planung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `QVAO Planung GmbH`(organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_7`)


Mit seiner gegen den Bescheid fristgerecht erhobenen „sozialrechtlichen Klage“ begehrt der Kläger, die beklagte Partei schuldig zu erkennen, die Kosten für die Inanspruchnahme der GmbH laut Rechnungen vom 2. 10. 2009 und 6. 11. 2009 in Höhe von insgesamt 540 EUR zu übernehmen.

**False Positives:**

- `Inanspruchnahme der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_9`)


Nach Erhalt von Bewilligungen der beklagten Partei für physikalische Behandlungen habe er entsprechende Leistungen der GmbH in Anspruch genommen und dafür insgesamt 540 EUR bezahlt. Die Behandlung stelle eine Krankenbehandlung dar und sei medizinisch notwendig und erfolgreich gewesen.

**False Positives:**

- `Behandlungen habe er entsprechende Leistungen der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_27`)


Der Kläger konsumierte die bewilligten Leistungen im September und November 2009 bei der Pharma Glanzsynstein GmbH.

**False Positives:**

- `November 2009 bei der Pharma Glanzsynstein GmbH` — positional overlap with gold: `Pharma Glanzsynstein GmbH.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Pharma Glanzsynstein GmbH.`(organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_29`)


Zwischen der GmbH und der beklagten Partei besteht kein Vertragsverhältnis.

**False Positives:**

- `Zwischen der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_32`)


Anhand dieser Vorgaben werden die von der GmbH entwickelten speziellen Trainingsmethoden angewandt.

**False Positives:**

- `Anhand dieser Vorgaben werden die von der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_137`)


Handelt es sich bei den von der GmbH angebotenen Trainings um Leistungen anderer Gesundheitsberufe, die nicht in § 135 Abs 1 ASVG aufgelistet sind, ist eine Analogie ausgeschlossen (siehe oben Pkt 1.1.).

**False Positives:**

- `Handelt es sich bei den von der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_23`)


Auch diesen Aspekt nimmt die Staatsanwaltschaft in der Rechtsrüge (Z 9 lit a) ausreichend in den Blick, indem sie auf - in Richtung der Erfüllung auch der objektiven Tatbestandsmerkmale der §§ 146, 147 Abs 3 StGB weisende - Beweisergebnisse zum vorliegenden Vertragsab-schluss trotz mangelnder finanzieller Ausstattung und Absicherung der Medien Lexsudtal GmbH hinweist.

**False Positives:**

- `Ausstattung und Absicherung der Medien Lexsudtal GmbH` — partial — gold is substring of pred: `Medien Lexsudtal GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Medien Lexsudtal GmbH`(organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__3`)


Kopf Der Oberste Gerichtshof hat am 11. September 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Setz-Hummel in Gegenwart der Richteramtsanwärterin Mag. Leitner als Schriftführerin in der Medienrechtssache des Antragstellers Georgia Bruckmeir gegen die Antragsgegnerin MittelForschung GmbH und eine weitere Antragsgegnerin wegen § 6 Abs 1 und § 8a Abs 6 MedienG, AZ 91 Hv 49/17t des Landesgerichts für Strafsachen Wien, über die von der Generalprokuratur gegen die Urteile des Landesgerichts für Strafsachen Wien vom 26. März 2018 (ON 65 der Hv-Akten) und des Oberlandesgerichts Wien als Berufungsgericht vom 28. November 2018, AZ 17 Bs 153/18a (ON 74 der Hv-Akten), erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Holzleithner, des Vertreters des Antragstellers, Dr. Bauer, und des Vertreters der Antragsgegnerin Analyse Fenheim GmbH, Mag. Bauer, zu Recht erkannt:  Spruch

**False Positives:**

- `Antragsgegnerin MittelForschung GmbH` — partial — gold is substring of pred: `MittelForschung GmbH`
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

**Example 31** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__4`)


In der Medienrechtssache des Antragstellers Univ.-Prof.in Laurin Schramm gegen die Antragsgegnerin CDL Luftfahrt GmbH wegen § 6 Abs 1 und § 8a Abs 6 MedienG, AZ 91 Hv 49/17t des Landesgerichts für Strafsachen Wien, verletzen die Urteile 1./ dieses Gerichts vom 26. März 2018 (ON 65) in seinem Punkt III./, womit der Antrag des Antragstellers, der Antragsgegnerin Drau-IT GmbH auch für die am 4. Juni 2017 auf dem Facebook-Account von www.

**False Positives:**

- `Antragsgegnerin CDL Luftfahrt GmbH` — partial — gold is substring of pred: `CDL Luftfahrt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof.in Laurin Schramm`(person)
- `CDL Luftfahrt GmbH`(organisation)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Drau-IT GmbH`(organisation)

**Example 32** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__7`)


Text Gründe: I./ In der Medienrechtssache des Antragstellers StR Anna Barkhausen gegen die Antragsgegnerin Tramoncon KI Consulting GmbH (als Medieninhaberin der Websites www.

**False Positives:**

- `Antragsgegnerin Tramoncon KI Consulting GmbH` — partial — gold is substring of pred: `Tramoncon KI Consulting GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `StR Anna Barkhausen`(person)
- `Tramoncon KI Consulting GmbH`(organisation)

**Example 33** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__10`)


für die dadurch zugefügte Kränkung wurde die Antragsgegnerin Tenholt Holz GmbH nach § 6 Abs 1 MedienG zur Zahlung einer Entschädigung sowie nach § 8a Abs 6 MedienG iVm § 34 Abs 1 MedienG zur Urteilsveröffentlichung verpflichtet.

**False Positives:**

- `Antragsgegnerin Tenholt Holz GmbH` — partial — gold is substring of pred: `Tenholt Holz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tenholt Holz GmbH`(organisation)

**Example 34** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__21`)


Zur Begründung führte das Berufungsgericht – soweit im Folgenden von Relevanz – in ausdrücklicher Abkehr von einer früher vertretenen Rechtsansicht (Urteil des Oberlandesgerichts Wien vom 14. Februar 2018, AZ 17 Bs 212/17a = MR 2018, 7) wie folgt aus (US 32 f): Die Antragsgegnerin Berg-Finanzen Planung GmbH habe auf einer Website (www. Hermani & Grebner Logistik.at) und damit in einem Medium (§ 1 Abs 1 Z 1 MedienG) den Tatbestand der üblen Nachrede hergestellt;

**False Positives:**

- `Die Antragsgegnerin Berg-Finanzen Planung GmbH` — partial — gold is substring of pred: `Berg-Finanzen Planung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgerichts Wien`(organisation)
- `Berg-Finanzen Planung GmbH`(organisation)
- `Hermani & Grebner Logistik.at`(organisation)

**Example 35** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__34`)


Die Haftung des auf eigene Inhalte Verlinkenden als Content-Provider richtet sich daher nach den allgemeinen (straf-)rechtlichen Normen und soweit dieser – wie vorliegend – Medieninhaber ist, nach dem Mediengesetz (Reindl-Krauskopf/Salimi/Stricker, IT-Strafrecht [2018] Rz 3.3, 3.10 und 3.33;Koziol, Haftpflichtrecht II³ A/6/Rz 204;Zankl, E-Commerce-Gesetz, Kommentar2Rz 277), sodass § 17 ECG der geltend gemachten Verantwortlichkeit der Antragsgegnerin Kirmayer Heizung GmbH nach § 6 Abs 1 MedienG nicht entgegensteht.

**False Positives:**

- `Heizung GmbH` — partial — pred is substring of gold: `Kirmayer Heizung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kirmayer Heizung GmbH`(organisation)

**Example 36** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__40`)


Voraussetzung für die geltend gemachte Haftung der Antragsgegnerin TUEU Garten GmbH nach § 6 Abs 1 MedienG ist, dass im Medium „Website“ (§ 1 Abs 1 Z 5a lit b MedienG) der objektive Tatbestand der üblen Nachrede hergestellt wurde.

**False Positives:**

- `Haftung der Antragsgegnerin TUEU Garten GmbH` — partial — gold is substring of pred: `TUEU Garten GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `TUEU Garten GmbH`(organisation)

**Example 37** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__60`)


Da sich diese Gesetzesverletzung nicht zum Nachteil der Antragsgegnerin Heimnexfen Planung Entwicklung GmbH, der als Medieninhaberin die Rechte des Angeklagten zukommen (§ 41 Abs 6 zweiter Satz MedienG), auswirkt, kommt ein Vorgehen nach § 292 letzter Satz StPO nicht in Betracht und hat es mit der Feststellung des Gesetzesverstoßes sein Bewenden.

**False Positives:**

- `Planung Entwicklung GmbH` — partial — pred is substring of gold: `Heimnexfen Planung Entwicklung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Heimnexfen Planung Entwicklung GmbH`(organisation)

**Example 38** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_3`)


Kopf Der Oberste Gerichtshof hat am 11. Dezember 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in Gegenwart des Schriftführers Dr. Koller in der Medienrechtssache der Antragsteller Dr. Ludger Schäpan und Moses Rüßbült gegen die Antragsgegnerin Synzortal-Medien GmbH & Co KG wegen §§ 7 f MedienG, AZ 93 Hv 56/18p des Landesgerichts für Strafsachen Wien, über die von der Generalprokuratur gegen den Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 9. März 2020, AZ 18 Bs 340/19k (ON 27), erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Erste Generalanwältin Mag. Wachberger, der Vertreterin der Antragsteller Dr. Windhager und des Vertreters der Antragsgegnerin Mag. Hermetter, zu Recht erkannt:  Spruch

**False Positives:**

- `Antragsgegnerin Synzortal-Medien GmbH` — positional overlap with gold: `Synzortal-Medien GmbH & Co KG`

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

**Example 39** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_4`)


In der Medienrechtssache der Antragsteller Dr. Patrick Schneeweiss und Chen Hölzle gegen die Antragsgegnerin TQGK Versicherung Holding GmbH & Co KG wegen §§ 7 f MedienG, AZ 93 Hv 56/18p, verletzt der Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 9. März 2020, AZ 18 Bs 340/19k (ON 27), § 395 Abs 2 StPO (iVm § 41 Abs 1 MedienG).

**False Positives:**

- `Antragsgegnerin TQGK Versicherung Holding GmbH` — positional overlap with gold: `TQGK Versicherung Holding GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Patrick Schneeweiss`(person)
- `Chen Hölzle`(person)
- `TQGK Versicherung Holding GmbH & Co KG`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 40** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_5`)


Text Gründe: In der Medienrechtssache der Antragsteller Dr. Wieland Skocdopole und Priv.-Doz.in Heidrun Aguera, BA MSc gegen die Antragsgegnerin Wald Fenkraftal GmbH & Co KG wegen §§ 7 f MedienG brachten die Antragsteller beim Landesgericht für Strafsachen Wien gesondert, jeweils in einem eigenen Schriftsatz aber vertreten durch dieselbe Rechtsanwältin selbständige Entschädigungsanträge gegen die Antragsgegnerin ein.

**False Positives:**

- `BA MSc gegen die Antragsgegnerin Wald Fenkraftal GmbH` — positional overlap with gold: `Priv.-Doz.in Heidrun Aguera, BA MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Wieland Skocdopole`(person)
- `Priv.-Doz.in Heidrun Aguera, BA MSc`(person)
- `Wald Fenkraftal GmbH & Co KG`(organisation)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 41** (doc_id: `deanon_260716_TRAIN/15Os9_12f`) (sent_id: `deanon_260716_TRAIN/15Os9_12f_5`)


Dieses Urteil sowie der gemäß § 494a Abs 1 StPO gefasste Beschluss werden aufgehoben und es wird in der Sache selbst zu Recht erkannt: Georg Hamker wird von dem wider ihn erhobenen Vorwurf, er habe in Joseph-Mohr-Straße 15, 5233 Erlach, Österreich mit dem Vorsatz, durch das Verhalten des Getäuschten sich oder einen Dritten unrechtmäßig zu bereichern, Bedienstete der Firma Meyerotto u. Pleuler Handel GmbH durch die Vorgabe, ein zahlungsfähiger und zahlungswilliger Kunde zu sein, zu nachgenannten Handlungen verleitet, die das genannte Unternehmen in einem 3.000 Euro, jedoch nicht 50.000 Euro übersteigenden Betrag am Vermögen schädigten, nämlich 1./ am 9. Juni 2010 zur Lieferung von Kaffee im Wert von 566,02 Euro;

**False Positives:**

- `Bedienstete der Firma Meyerotto u. Pleuler Handel GmbH` — partial — gold is substring of pred: `Meyerotto u. Pleuler Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Georg Hamker`(person)
- `Joseph-Mohr-Straße 15, 5233 Erlach, Österreich`(address)
- `Meyerotto u. Pleuler Handel GmbH`(organisation)

**Example 42** (doc_id: `deanon_260716_TRAIN/15Os9_12f`) (sent_id: `deanon_260716_TRAIN/15Os9_12f_7`)


Text Gründe: Mit dem unangefochten in Rechtskraft erwachsenen Urteil des Landesgerichts Feldkirch vom 4. Oktober 2011, GZ 24 Hv 84/11k-6, wurde Georg Höfs - abweichend von dem in Richtung §§ 146, 147 Abs 2 StGB erhobenen Strafantrag - des Vergehens des Betrugs nach § 146 StGB schuldig erkannt und zu einer teilweise bedingt nachgesehenen Geldstrafe verurteilt. Nach dem Schuldspruch hat er in Chikago 2. Gasse 8, 4613 Hupfau, Österreich mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz Bedienstete der (richtig:) Nobars und Huenecken E‑Commerce GmbH durch die Vorgabe, ein zahlungsfähiger und zahlungswilliger Kunde zu sein, zu Handlungen verleitet, die das genannte Unternehmen in einem 3.000 Euro nicht übersteigenden Betrag am Vermögen schädigten, nämlich 1./ am 9. Juni 2010 zur Lieferung von Kaffee im Wert von 566,02 Euro;

**False Positives:**

- `Commerce GmbH` — partial — pred is substring of gold: `Nobars und Huenecken E‑Commerce GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Feldkirch`(organisation)
- `Georg Höfs`(person)
- `Chikago 2. Gasse 8, 4613 Hupfau, Österreich`(address)
- `Nobars und Huenecken E‑Commerce GmbH`(organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/15Os9_12f`) (sent_id: `deanon_260716_TRAIN/15Os9_12f_9`)


Den weiters mit Strafantrag vom 1. September 2011 (ON 3) erhobenen Vorwurf, der Angeklagte habe am 8. Juli 2010 die Verfügungsberechtigten der Nexlexlog Holding GmbH auch zur leihweisen Überlassung einer Kaffeemaschine im Wert von 390 Euro und eines sogenannten Schokodispensers Exquisit im Wert von 1.328 Euro veranlasst, erachtete das Erstgericht für nicht erweislich.

**False Positives:**

- `Holding GmbH` — partial — pred is substring of gold: `Nexlexlog Holding GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nexlexlog Holding GmbH`(organisation)

**Example 44** (doc_id: `deanon_260716_TRAIN/17Ob10_20z`) (sent_id: `deanon_260716_TRAIN/17Ob10_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätinnen Mag. Malesich und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Pascal Alsweh, vertreten durch Stephan Briem Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Dr. Simone Pittruff als Treuhänder der Insolvenzgläubiger der Unter-Analyse Aktiengesellschaft, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH in Linz, wegen Feststellung (Streitwert 18.335,66 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. März 2020, GZ 1 R 31/20i-13, womit das Urteil des Landesgerichts Linz vom 9. Dezember 2019, GZ 4 Cg 73/18z-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Rechtsanwalt GmbH` — partial — pred is substring of gold: `Stephan Briem Rechtsanwalt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Dr. Musger`(person)
- `Mag. Malesich`(person)
- `Dr. Kodek`(person)
- `Dr. Stefula`(person)
- `Pascal Alsweh`(person)
- `Stephan Briem Rechtsanwalt GmbH`(organisation)
- `Dr. Simone Pittruff`(person)
- `Unter-Analyse Aktiengesellschaft`(organisation)
- `Shamiyeh & Reiser Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Linz`(organisation)

**Example 45** (doc_id: `deanon_260716_TRAIN/18OCg12_19t`) (sent_id: `deanon_260716_TRAIN/18OCg12_19t_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Veith und die Hofräte Dr. Höllwerth, Priv.-Doz. Dr. Rassi und Mag. Painsi als weitere Richter in der Schiedsrechtssache der klagenden Partei Energie Glanzgart GmbH, Waldelweg 28, 4201 Maierleiten, Österreich, vertreten durch die SRG Stock Rafaseder Gruszkiewicz Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Piedro Arnoult, Bulgarien, wegen Aufhebung eines Schiedsspruchs (Streitwert 257.397,45 EUR), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Klage wird als nicht zur Bestimmung einer Tagsatzung zur mündlichen Verhandlung geeignet zurückgewiesen.

**False Positives:**

- `Partei Energie Glanzgart GmbH` — partial — gold is substring of pred: `Energie Glanzgart GmbH`

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

**Example 46** (doc_id: `deanon_260716_TRAIN/1Nc1_15k`) (sent_id: `deanon_260716_TRAIN/1Nc1_15k_3`)


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

**Example 47** (doc_id: `deanon_260716_TRAIN/1Ob139_18z`) (sent_id: `deanon_260716_TRAIN/1Ob139_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Verena Tappendorff Inc., Sankt Andrä im Sausal 24, 8552 Aichberg, Österreich, vertreten durch Mag. Ralph Kilches, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Sabine Martinsson, als Insolvenzverwalter im Insolvenzverfahren über das Vermögen der Touristik Synberbruck GmbH, Fridau 56l, 7433 Bergwerk, Österreich, vertreten durch die Haslinger/Nagele & Partner Rechtsanwälte GmbH, Linz, wegen Feststellung einer Insolvenzforderung (Streitwert 447.352,05 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 28. Juni 2018, GZ 1 R 83/18h-8, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Synberbruck GmbH` — partial — pred is substring of gold: `Touristik Synberbruck GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 48** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Dr. Florenzia Münsterer, vertreten durch Rechtsanwälte Dr. Amhof & Dr. Damian GmbH in Wien, gegen die beklagte Partei MittelEnergie Werke Bank AG, Altlassing 110, 4183 Ahorn, Österreich, vertreten durch Urbanek Lind Schmied Reisch Rechtsanwälte OG in Wien, wegen 600.090 EUR sA, über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 25. Mai 2011, GZ 15 R 64/11h-54, mit dem das Urteil des Handelsgerichts Wien vom 14. Jänner 2011, GZ 16 Cg 20/10f-50, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Dr. Amhof & Dr. Damian GmbH` — partial — pred is substring of gold: `Rechtsanwälte Dr. Amhof & Dr. Damian GmbH`

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

**Example 49** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_5`)


Text Begründung: Eine GmbH, deren Mehrheitsgesellschafter und Geschäftsführer ein Cousin des Klägers war, beabsichtigte, bei der beklagten Bank einen Kredit aufzunehmen, dessen Gewährung allerdings von der Bestellung einer Sicherheit abhängig gemacht wurde, zumal damals nur ungefähr die Hälfte des Gesamtobligos der GmbH bei der Beklagten von rund 6,6 Mio EUR besichert war.

**False Positives:**

- `Gesamtobligos der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_19`)


Von der wirtschaftlich schlechten Situation der GmbH hatte der Kläger erstmals wenige Tage vor der Konkurseröffnung erfahren.

**False Positives:**

- `Von der wirtschaftlich schlechten Situation der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_21`)


Die Beklagte sei schon ab Jänner 2005 aufgrund einer erfolgten Umschuldung vollständig über die ungünstige wirtschaftliche Situation der GmbH informiert gewesen und habe daher gewusst oder hätte zumindest wissen müssen, dass diese voraussichtlich nicht in der Lage sein werde, den Kredit zu tilgen.

**False Positives:**

- `Situation der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_23`)


Die Beklagte habe ihre vorvertraglichen Aufklärungs-, Schutz- und Sorgfaltspflichten verletzt, indem sie den Kläger, der keine Zweifel an der Rückführung des Kredits durch die GmbH gehabt habe, davon nicht informiert habe;

**False Positives:**

- `Kredits durch die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_32`)


Dieser sei sich auch der wirtschaftlichen Lage der GmbH voll bewusst gewesen.

**False Positives:**

- `Dieser sei sich auch der wirtschaftlichen Lage der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_76`)


Er habe, nachdem seine Haftung aus der Interzession nach dem Konkurs der GmbH festgestanden sei, keine Erfüllungs- oder sonstige Handlung zugunsten der Beklagten gesetzt.

**False Positives:**

- `Haftung aus der Interzession nach dem Konkurs der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_81`)


Geht man davon aus, dass die bloß mündlich abgegebene Zusage, der Kläger werde zur Besicherung der Verbindlichkeiten der GmbH eine Bankgarantie beibringen, in sinngemäßer Anwendung des § 1346 Abs 2 ABGB mangels Schriftlichkeit formunwirksam war, war er vorerst nicht verpflichtet, die in dieser unwirksamen Vereinbarung versprochene Leistung, nämlich die Verschaffung einer Bankgarantie, zu erbringen.

**False Positives:**

- `Besicherung der Verbindlichkeiten der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_260716_TRAIN/1Ob182_17x`) (sent_id: `deanon_260716_TRAIN/1Ob182_17x_25`)


Nach dem von den Vorinstanzen zugrunde gelegten Sachverhalt beabsichtigt der Antragsgegner einer zur Unternehmensgruppe der Familie gehörenden GmbH, an der er nur mehr einen Geschäftsanteil von 1 % hält, der aber mit weitreichenden Sonderrechten ausgestattet ist, und die einen dringenden Finanzierungsbedarf in Höhe von 3 Mio EUR hat, ein Privatdarlehen in dieser Höhe zu gewähren, dass er wiederum durch Aufnahme eines entsprechenden Bankkredits finanzieren will, von dem bereits 1 Mio EUR an den Antragsgegner und von diesem an die GmbH geflossen sind.

**False Positives:**

- `Mio EUR an den Antragsgegner und von diesem an die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_260716_TRAIN/1Ob182_17x`) (sent_id: `deanon_260716_TRAIN/1Ob182_17x_33`)


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

**Example 58** (doc_id: `deanon_260716_TRAIN/1Ob216_15v`) (sent_id: `deanon_260716_TRAIN/1Ob216_15v_3`)


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

**Example 59** (doc_id: `deanon_260716_TRAIN/1Ob224_20b`) (sent_id: `deanon_260716_TRAIN/1Ob224_20b_3`)


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

**Example 60** (doc_id: `deanon_260716_TRAIN/1Ob226_20x`) (sent_id: `deanon_260716_TRAIN/1Ob226_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Pia Geermann GmbH, Orise 28, 9135 Unterort, Österreich, vertreten durch Dr. Martin Leitner und andere, Rechtsanwälte in Wien, gegen die beklagte Partei Stadt Li Wachmeister, vertreten durch die Estermann Pock Rechtsanwälte GmbH, Wien, wegen 19.002,01 EUR, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 7. September 2020, GZ 14 R 61/20y-27, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 28. Jänner 2020, GZ 31 Cg 1/19y-22, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Pia Geermann GmbH` — partial — gold is substring of pred: `Pia Geermann`

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

**Example 61** (doc_id: `deanon_260716_TRAIN/1Ob26_20k`) (sent_id: `deanon_260716_TRAIN/1Ob26_20k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Schrickel Luftfahrt GmbH, Grieselstein-Rosenberg 3, 3314 Ottendorf, Österreich, vertreten durch die Draxler Rexeis Sozietät von Rechtsanwälten OG, Graz, gegen die beklagte Partei Monika Peikert, vertreten durch Mag. Dr. Alfred Wansch, Rechtsanwalt in Wien, wegen Räumung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtsachen Wien als Berufungsgericht vom 13. November 2019, GZ 39 R 228/19x-70, mit dem das Urteil des Bezirksgerichts Hernals vom 30. April 2019, GZ 4 C 277/16f-64, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Schrickel Luftfahrt GmbH` — partial — gold is substring of pred: `Schrickel Luftfahrt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Parzmayr`(person)
- `Schrickel Luftfahrt GmbH`(organisation)
- `Grieselstein-Rosenberg 3, 3314 Ottendorf, Österreich`(address)
- `Draxler Rexeis Sozietät von Rechtsanwälten OG`(organisation)
- `Monika Peikert`(person)
- `Mag. Dr. Alfred Wansch`(person)
- `Bezirksgerichts Hernals`(organisation)

**Example 62** (doc_id: `deanon_260716_TRAIN/1Ob51_11y`) (sent_id: `deanon_260716_TRAIN/1Ob51_11y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei mj Luna Saar, vertreten durch Mag. Erich Frenner, Rechtsanwalt in Saalfelden, gegen die beklagte Partei Bernexwald Heizung GmbH, Viaduktstraße 131, 4814 Gmundnerberg, Österreich, vertreten durch Dr. Harald Schwendinger und Dr. Brigitte Piber Rechtsanwälte in Salzburg, wegen 5.100 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 30. Dezember 2010, GZ 53 R 273/10v-12, mit dem über die Berufung der beklagten Partei das Zwischenurteil des Bezirksgerichts Saalfelden vom 23. Juni 2010, GZ 2 C 454/10z-7, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei Bernexwald Heizung GmbH` — partial — gold is substring of pred: `Bernexwald Heizung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Dr. Grohmann`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Luna Saar`(person)
- `Mag. Erich Frenner`(person)
- `Bernexwald Heizung GmbH`(organisation)
- `Viaduktstraße 131, 4814 Gmundnerberg, Österreich`(address)
- `Dr. Harald Schwendinger`(person)
- `Dr. Brigitte Piber`(person)
- `Landesgerichts Salzburg`(organisation)
- `Bezirksgerichts Saalfelden`(organisation)

**Example 63** (doc_id: `deanon_260716_TRAIN/1Ob51_14b`) (sent_id: `deanon_260716_TRAIN/1Ob51_14b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Mittel-Landwirtschaft Betriebe GmbH, Baurat Schneider Straße 3, 4612 Finklham, Österreich, vertreten durch Dr. Arno Kempf, Rechtsanwalt in Spittal an der Drau, gegen die beklagten Parteien 1.

**False Positives:**

- `Partei Mittel-Landwirtschaft Betriebe GmbH` — partial — gold is substring of pred: `Mittel-Landwirtschaft Betriebe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Dr. Grohmann`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Mittel-Landwirtschaft Betriebe GmbH`(organisation)
- `Baurat Schneider Straße 3, 4612 Finklham, Österreich`(address)
- `Dr. Arno Kempf`(person)

**Example 64** (doc_id: `deanon_260716_TRAIN/1Ob53_25p`) (sent_id: `deanon_260716_TRAIN/1Ob53_25p_44`)


Dem Vorwurf, der Beklagte habe es verabsäumt, einem (irrtümlichen) Verkauf fremder Fahrzeuge und Maschinen durch die GmbH durch ein geeignetesKontrollsystem vorzubeugen(vgl RS0023927), sind die Feststellungen entgegenzuhalten: Er hatte ein System eingeführt, nach dem alle auf Betriebsliegenschaften der GmbH befindlichen Geräte und Maschinen in Listen eingetragen und die jeweiligen Eigentümer vermerkt wurden, sodass über im fremden Eigentum stehende Sachen keine Rechnung und kein Lieferschein ausgestellt werden konnten.

**False Positives:**

- `Verkauf fremder Fahrzeuge und Maschinen durch die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_260716_TRAIN/1Ob56_17t`) (sent_id: `deanon_260716_TRAIN/1Ob56_17t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Leonhard Lakmayer Ltd, Klauser Ried 27, 4880 Thalham, Österreich, vertreten durch Dr. Wolfgang G. Kretschmer, LL.M. Rechtsanwalt in Wien, gegen die beklagte Partei Frommenkord Technik GmbH, Wiesenthalgasse 20, 2000 Oberzögersdorf, Österreich, vertreten durch Dr. Herwig B. Schönbauer, Rechtsanwalt in Wien, und die Nebenintervenientinnen auf Seiten der beklagten Partei 1.

**False Positives:**

- `Partei Frommenkord Technik GmbH` — partial — gold is substring of pred: `Frommenkord Technik GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Leonhard Lakmayer`(person)
- `Klauser Ried 27, 4880 Thalham, Österreich`(address)
- `Dr. Wolfgang G. Kretschmer, LL.M.`(person)
- `Frommenkord Technik GmbH`(organisation)
- `Wiesenthalgasse 20, 2000 Oberzögersdorf, Österreich`(address)
- `Dr. Herwig B. Schönbauer`(person)

**Example 66** (doc_id: `deanon_260716_TRAIN/1Ob56_17t`) (sent_id: `deanon_260716_TRAIN/1Ob56_17t_4`)


Gloria Hackenbuchner GmbH, Untere Kanalstraße 187, 2471 Hollern, Österreich, vertreten durch Mag. Manfred Sommerbauer und MMag. Dr. Michael Dohr LL.M., Rechtsanwälte in Wiener Neustadt, und 2. Nelleßen + Stümpfel Automotive AG, Villengasse 31, 8670 Krieglach, Österreich, vertreten durch die Kosch & Partner Rechtsanwälte GmbH, Wiener Neustadt, wegen 76.444,01 EUR sA über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Jänner 2017, GZ 1 R 164/16v-174, mit dem das Urteil des Handelsgerichts Wien vom 12. August 2016, GZ 65 Cg 12/15x-169, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Gloria Hackenbuchner GmbH` — partial — gold is substring of pred: `Gloria Hackenbuchner`

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

**Example 67** (doc_id: `deanon_260716_TRAIN/1Ob72_13i`) (sent_id: `deanon_260716_TRAIN/1Ob72_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Bohnestengel Landwirtschaft -GmbH Leinmüllergasse 7, 8410 Wildon, Österreich, vertreten durch Mag. Rivo Killer, Rechtsanwalt in Wiener Neustadt, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 950.000 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Februar 2013, GZ 14 R 226/12a-26, mit dem das Urteil des Landesgerichts Wiener Neustadt vom 3. September 2012, GZ 25 Cg 25/12t-22, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Bohnestengel Landwirtschaft -GmbH` — partial — gold is substring of pred: `Bohnestengel Landwirtschaft -GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Dr. Grohmann`(person)
- `Mag. Wurzer`(person)
- `Mag. Wurdinger`(person)
- `Bohnestengel Landwirtschaft -GmbH`(organisation)
- `Leinmüllergasse 7, 8410 Wildon, Österreich`(address)
- `Mag. Rivo Killer`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Wiener Neustadt`(organisation)

**Example 68** (doc_id: `deanon_260716_TRAIN/1Ob93_17h`) (sent_id: `deanon_260716_TRAIN/1Ob93_17h_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Brechtold Textil GmbH, St. Anna Straße 10, 9564 Rottenstein, Österreich, Deutschland, vertreten durch Dr. Stefan Gulner, Rechtsanwalt in Wien, gegen die beklagte Partei ÖkR Ali Abramenko, vertreten durch die Maggi Brandl Kathollnig RechtsanwaltsGmbH-Studio Legale, Klagenfurt am Wörthersee, wegen 191.469 EUR sA, über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 10. April 2017, GZ 4 R 32/17h-28, mit dem der Beschluss des Landesgerichts Klagenfurt vom 25. Jänner 2017, GZ 49 Cg 60/14k-24, teilweise bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Partei Brechtold Textil GmbH` — partial — gold is substring of pred: `Brechtold Textil GmbH`
- `Maggi Brandl Kathollnig RechtsanwaltsGmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Brechtold Textil GmbH`(organisation)
- `St. Anna Straße 10, 9564 Rottenstein, Österreich`(address)
- `Dr. Stefan Gulner`(person)
- `ÖkR Ali Abramenko`(person)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts Klagenfurt`(organisation)

**Example 69** (doc_id: `deanon_260716_TRAIN/1Ob95_21h`) (sent_id: `deanon_260716_TRAIN/1Ob95_21h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Gawelzyk Pflege GmbH, Am See IX 247, 6320 Achleit, Österreich, vertreten durch die Zumtobel Kronberger Rechtsanwälte OG, Salzburg, gegen die beklagte Partei Loos und Woiciech Analyse GmbH, Rasenweg 21, 3441 Baumgarten am Tullnerfeld, Österreich, vertreten durch die Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH, Salzburg, wegen 135.656,39 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. April 2021, GZ 2 R 39/21z-27, mit dem das Urteil des Landesgerichts Ried im Innkreis vom 27. Jänner 2021, GZ 2 Cg 24/20i-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Gawelzyk Pflege GmbH` — partial — gold is substring of pred: `Gawelzyk Pflege GmbH`
- `Partei Loos und Woiciech Analyse GmbH` — partial — gold is substring of pred: `Loos und Woiciech Analyse GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Parzmayr`(person)
- `Gawelzyk Pflege GmbH`(organisation)
- `Am See IX 247, 6320 Achleit, Österreich`(address)
- `Zumtobel Kronberger Rechtsanwälte OG`(organisation)
- `Loos und Woiciech Analyse GmbH`(organisation)
- `Rasenweg 21, 3441 Baumgarten am Tullnerfeld, Österreich`(address)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Ried im Innkreis`(organisation)

**Example 70** (doc_id: `deanon_260716_TRAIN/2Ob159_18y`) (sent_id: `deanon_260716_TRAIN/2Ob159_18y_10`)


Er selbst war ua als Fenstermonteur in der GmbH tätig.

**False Positives:**

- `Er selbst war ua als Fenstermonteur in der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_260716_TRAIN/2Ob159_18y`) (sent_id: `deanon_260716_TRAIN/2Ob159_18y_19`)


In weiterer Folge brachte er – zusammengefasst – vor, der Verdienstentgang errechne sich aus dem Ausfall des hypothetischen Gewinns seiner GmbH, der erzielbar gewesen wäre, hätte das Unternehmen nicht geschlossen werden müssen (ON 8, vgl auch ON 45 und 51).

**False Positives:**

- `Ausfall des hypothetischen Gewinns seiner GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_260716_TRAIN/2Ob194_24d`) (sent_id: `deanon_260716_TRAIN/2Ob194_24d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte MMag. Sloboda, Dr. Thunhart, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Dagobert Drügemöller, vertreten durch Gottgeisl Leinsmer Weber Rechtsanwälte GmbH in Wien, wider die beklagte Partei Rosalinde Nölker, Malta, vertreten durch Mag. Simon Wallner Rechtsanwalt GmbH in Wien, wegen 30.895 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 1. Oktober 2024, GZ 12 R 72/24g-21, den Beschluss gefasst:  Spruch I. Der Antrag auf Unterbrechung des Revisionsverfahrens bis zur Entscheidung des Europäischen Gerichtshofs zu C-683/24 wird abgewiesen.

**False Positives:**

- `Simon Wallner Rechtsanwalt GmbH` — partial — pred is substring of gold: `Mag. Simon Wallner Rechtsanwalt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Grohmann`(person)
- `MMag. Sloboda`(person)
- `Dr. Thunhart`(person)
- `Dr. Kikinger`(person)
- `Mag. Fitz`(person)
- `Dagobert Drügemöller`(person)
- `Gottgeisl Leinsmer Weber Rechtsanwälte GmbH`(organisation)
- `Rosalinde Nölker`(person)
- `Mag. Simon Wallner Rechtsanwalt GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 73** (doc_id: `deanon_260716_TRAIN/3Nc11_13t`) (sent_id: `deanon_260716_TRAIN/3Nc11_13t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie die Hofräte Univ.-Prof Dr. Neumayr und Dr. Jensik als weitere Richter in der Ordinationssache der Antragstellerin Mikulska Textil GmbH, Kohleck 4, 6794 Partenen, Österreich, vertreten durch Dr. Clemens Thiele, Rechtsanwalt in Salzburg, gegen die Antragsgegnerin TraunWind GmbH, Ferdinand Schaller-Weg 1, 4131 Stieberberg, Österreich, wegen Exekutionsführung nach § 355 EO, infolge Antrags gemäß § 28 JN den Beschluss gefasst:  Spruch Für die Bewilligung und die Vollziehung der beabsichtigten Unterlassungsexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Textil GmbH` — partial — pred is substring of gold: `Mikulska Textil GmbH`
- `Antragsgegnerin TraunWind GmbH` — partial — gold is substring of pred: `TraunWind GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Prückner`(person)
- `Dr. Neumayr`(person)
- `Dr. Jensik`(person)
- `Mikulska Textil GmbH`(organisation)
- `Kohleck 4, 6794 Partenen, Österreich`(address)
- `Dr. Clemens Thiele`(person)
- `TraunWind GmbH`(organisation)
- `Ferdinand Schaller-Weg 1, 4131 Stieberberg, Österreich`(address)
- `Bezirksgericht Salzburg`(organisation)

**Example 74** (doc_id: `deanon_260716_TRAIN/3Nc39_24a`) (sent_id: `deanon_260716_TRAIN/3Nc39_24a_29`)


Als örtlich zuständiges Exekutionsgericht für die beabsichtigte Rechteexekution ist das Bezirksgericht Salzburg zu bestimmen, weil die Rhein Kraftnor.at GmbH als Registrierungsstelle der von der beabsichtigten Exekutionsführung betroffenen Domain der Verpflichteten im Sprengel dieses Gerichts ihren Sitz hat.

**False Positives:**

- `Rhein Kraftnor.at GmbH` — partial — gold is substring of pred: `Rhein Kraftnor.at`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Salzburg`(organisation)
- `Rhein Kraftnor.at`(organisation)

**Example 75** (doc_id: `deanon_260716_TRAIN/3Ob12_11b`) (sent_id: `deanon_260716_TRAIN/3Ob12_11b_6`)


Der titulierten Rechnungslegungsverpflichtung liegt nach den Feststellungen im Titelverfahren zu Grunde, dass der Oppositionskläger vom Privatkonto des Oppositionsbeklagten mit der ihm von diesem zur Verfügung gestellten Bankomatkarte insgesamt Barbeträge über 114.500 EUR behob, wobei der Oppositionskläger ebenfalls im Rechnungslegungszeitraum vom Konto der GmbH insgesamt Überweisungen über 79.000 EUR auf das Privatkonto des Oppositionsbeklagten veranlasste.

**False Positives:**

- `Rechnungslegungszeitraum vom Konto der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_260716_TRAIN/3Ob12_11b`) (sent_id: `deanon_260716_TRAIN/3Ob12_11b_29`)


5. Die Beurteilung des Berufungsgerichts, der Oppositionskläger habe ausreichend dargetan, dass die von ihm behobenen Beträge in Höhe von insgesamt 114.500 EUR in den Bilanzen der GmbH nicht verbucht wurden, weshalb er auch in diesem Umfang der Titelverpflichtung entsprochen habe, wirft ebenfalls keine im Rahmen einer außerordentlichen Revision aufzugreifende erhebliche Rechtsfrage auf: Es steht durch die gelegte Rechnung in Verbindung mit den Bilanzen der GmbH, in deren Besitz der Oppositionsbeklagte unstrittig ist, fest, dass weder der Gesamtbetrag von 114.500 EUR noch Teilbeträge davon in den Bilanzen der GmbH verbucht wurde.

**False Positives:**

- `EUR in den Bilanzen der GmbH` — no gold match — likely missing annotation
- `Rechnung in Verbindung mit den Bilanzen der GmbH` — no gold match — likely missing annotation
- `Bilanzen der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 77** (doc_id: `deanon_260716_TRAIN/3Ob139_20t`) (sent_id: `deanon_260716_TRAIN/3Ob139_20t_5`)


Text Begründung: [1] Mit Vertrag vom 5. August 2018 vereinbarten die Gegnerin der gefährdeten Partei (im Folgenden: Bestellerin) und eine Maschinenbau GmbH (im Folgenden: Werkunternehmerin) die Lieferung einer Kesselbodenfräsmaschine.

**False Positives:**

- `Maschinenbau GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_260716_TRAIN/3Ob147_20v`) (sent_id: `deanon_260716_TRAIN/3Ob147_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Glanzval Dienstleistungen GmbH, Otto-Hittmair-Platz 29, 9423 Steinberg-Hart, Österreich, vertreten durch Mag. Andreas Kleiber, Rechtsanwalt in Wien, gegen die beklagte Partei Gisela Filippovic, MBA verein Arthur Hoelle, vertreten durch Pflaum Karlberger Wiener Opetnik, Rechtsanwälte in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 22. Juli 2020, GZ 40 R 37/20t-27, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Glanzval Dienstleistungen GmbH` — partial — gold is substring of pred: `Glanzval Dienstleistungen GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Roch`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Dr. Stefula`(person)
- `Glanzval Dienstleistungen GmbH`(organisation)
- `Otto-Hittmair-Platz 29, 9423 Steinberg-Hart, Österreich`(address)
- `Mag. Andreas Kleiber`(person)
- `Gisela Filippovic, MBA`(person)
- `Arthur Hoelle`(person)
- `Pflaum Karlberger Wiener Opetnik, Rechtsanwälte`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 79** (doc_id: `deanon_260716_TRAIN/3Ob150_16d`) (sent_id: `deanon_260716_TRAIN/3Ob150_16d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Jensik und Dr. Roch und die Hofrätin Dr. Kodek als weitere Richter in der Exekutionssache der betreibenden Partei Fenmon Versicherung GmbH, Grundwiesenweg 291, 3141 Panzing, Österreich, vertreten durch Dr. Andrea Gesinger, Rechtsanwältin in Salzburg, gegen die verpflichtete Partei Unter Condon Consulting GmbH, Pengersdorf 5, 9556 Gößeberg, Österreich, vertreten durch Doschek Rechtsanwalts GmbH in Wien, wegen 9.718,32 EUR sA, über den Revisionsrekurs und Rekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 24. Mai 2016, GZ 22 R 132/16i, 133/16m-21, womit der Beschluss des Bezirksgerichts St. Johann im Pongau vom 17. März 2016, GZ 22 E 1592/15d-14, abgeändert und der Beschluss des Bezirksgerichts St. Johann im Pongau vom 6. April 2016, GZ 22 E 1592/15d-13, aufgehoben wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs und der Rekurs werden zurückgewiesen.

**False Positives:**

- `Partei Fenmon Versicherung GmbH` — partial — gold is substring of pred: `Fenmon Versicherung GmbH`
- `Partei Unter Condon Consulting GmbH` — partial — gold is substring of pred: `Unter Condon Consulting GmbH`
- `Rechtsanwalts GmbH` — partial — pred is substring of gold: `Doschek Rechtsanwalts GmbH`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hoch`(person)
- `Dr. Lovrek`(person)
- `Dr. Jensik`(person)
- `Dr. Roch`(person)
- `Dr. Kodek`(person)
- `Fenmon Versicherung GmbH`(organisation)
- `Grundwiesenweg 291, 3141 Panzing, Österreich`(address)
- `Dr. Andrea Gesinger`(person)
- `Unter Condon Consulting GmbH`(organisation)
- `Pengersdorf 5, 9556 Gößeberg, Österreich`(address)
- `Doschek Rechtsanwalts GmbH`(organisation)
- `Landesgerichts Salzburg`(organisation)
- `Bezirksgerichts St. Johann im Pongau`(organisation)
- `Bezirksgerichts St. Johann im Pongau`(organisation)

**Example 80** (doc_id: `deanon_260716_TRAIN/3Ob185_22k`) (sent_id: `deanon_260716_TRAIN/3Ob185_22k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn und die Hofrätinnen Dr. Weixelbraun-Mohr, Dr. Kodek und Mag. Wessely-Kristöfel als weitere Richter in der Exekutionssache der betreibenden Partei Dr. Moritz Absmeier, vertreten durch Dr. Martin Neuwirth, Dr. Alexander Neurauter, Rechtsanwälte in Wien, gegen die verpflichtete Partei DENU Immobilien GmbH, Gürtel 12, 5145 Schmalzhofen, Österreich, vertreten durch Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH in Wien, wegen zwangsweiser Räumung, über den Revisionsrekurs der betreibenden Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 12. August 2022, GZ 40 R 104/22y-20, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 8. April 2022, GZ 49 E 11/22w-3, abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Partei DENU Immobilien GmbH` — partial — gold is substring of pred: `DENU Immobilien GmbH`

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

**Example 81** (doc_id: `deanon_260716_TRAIN/3Ob1_18w`) (sent_id: `deanon_260716_TRAIN/3Ob1_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Roch und Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Druck Steinnex GmbH, Josef-Wessely-Straße 15, 4171 Unterriedl, Österreich, vertreten durch Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG in Wien, gegen die beklagten Parteien 1.

**False Positives:**

- `Partei Druck Steinnex GmbH` — partial — gold is substring of pred: `Druck Steinnex GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hoch`(person)
- `Dr. Roch`(person)
- `Dr. Rassi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Druck Steinnex GmbH`(organisation)
- `Josef-Wessely-Straße 15, 4171 Unterriedl, Österreich`(address)
- `Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG`(organisation)

**Example 82** (doc_id: `deanon_260716_TRAIN/3Ob209_21p`) (sent_id: `deanon_260716_TRAIN/3Ob209_21p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei APHU Solar GmbH & Co KG, Hochkreuth 39, 8144 Bischofegg, Österreich, vertreten durch DDr. Heinz Dietmar Schimanko, Rechtsanwalt in Wien, gegen die beklagte Partei Traun-Transport GmbH, Stauderstraße 30, 8200 Pircha, Österreich, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH & Co KG in Wien, wegen 7.906,82 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 7. Juni 2021, GZ 38 R 66/21v-16, mit dem das Urteil des Bezirksgerichts Favoriten vom 19. Jänner 2021, GZ 3 C 503/20f-12, abgeändert wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Traun-Transport GmbH` — partial — gold is substring of pred: `Traun-Transport GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Hon.-Prof. Dr. Brenn`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Dr. Stefula`(person)
- `APHU Solar GmbH & Co KG`(organisation)
- `Hochkreuth 39, 8144 Bischofegg, Österreich`(address)
- `DDr. Heinz Dietmar Schimanko`(person)
- `Traun-Transport GmbH`(organisation)
- `Stauderstraße 30, 8200 Pircha, Österreich`(address)
- `Bichler Zrzavy Rechtsanwälte GmbH & Co KG`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Favoriten`(organisation)

**Example 83** (doc_id: `deanon_260716_TRAIN/3Ob32_17b`) (sent_id: `deanon_260716_TRAIN/3Ob32_17b_79`)


Auch die damalige Ortsabwesenheit des Geschäftsführers der Verpflichteten verlangt keine andere Beurteilung, weil dieser – wie feststeht – „mit dem täglichen Geschäft, dem internen Postlauf und der Organisation in der GmbH weniger vertraut war“.

**False Positives:**

- `Postlauf und der Organisation in der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_260716_TRAIN/3Ob69_19x`) (sent_id: `deanon_260716_TRAIN/3Ob69_19x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Roch und Priv.-Doz. Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Matthew Pfneissl, vertreten durch Dr. Klaus Plätzer, Rechtsanwalt in Salzburg, gegen die beklagte Partei Allex GmbH, Zur Kühlen Luft 10, 3435 Erpersdorf, Österreich, vertreten durch Dr. Patrick Ruth, Rechtsanwalt in Innsbruck, wegen Unterlassung (Streitwert 50.000 EUR), über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 7. Februar 2019, GZ 3 R 164/18k-44, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Allex GmbH` — partial — gold is substring of pred: `Allex GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hoch`(person)
- `Dr. Roch`(person)
- `Priv.-Doz. Dr. Rassi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Matthew Pfneissl`(person)
- `Dr. Klaus Plätzer`(person)
- `Allex GmbH`(organisation)
- `Zur Kühlen Luft 10, 3435 Erpersdorf, Österreich`(address)
- `Dr. Patrick Ruth`(person)
- `Oberlandesgerichts Linz`(organisation)

**Example 85** (doc_id: `deanon_260716_TRAIN/3Ob72_20i`) (sent_id: `deanon_260716_TRAIN/3Ob72_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Marktgemeinde James Weyand, MA, vertreten durch Dr. Nader Karl Mahdi, Rechtsanwalt in Wattens, gegen die beklagte Partei Lützeler Garten AG, Esteplatz 2, 9064 Schöpfendorf, Österreich, vertreten durch Altenweisl Wallnöfer Watschinger Zimmermann Rechtsanwälte GmbH in Innsbruck, und die auf Seiten der beklagten Partei beigetretene Nebenintervenientin Demeyer u. Köktas Analyse GmbH, Zinkendorferstraße 100, 9321 Schöttlhof, Österreich, vertreten durch Dr. Christian Girardi, LL.M., Ing. Dr. Stefan Schwärzler, Mag. Daniel Pichler, Rechtsanwälte in Innsbruck, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. März 2020, GZ 1 R 5/20z-27, womit das Urteil des Landesgerichts Innsbruck vom 14. November 2019, GZ 12 Cg 33/19m-18, teilweise bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Analyse GmbH` — partial — pred is substring of gold: `Demeyer u. Köktas Analyse GmbH`

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

**Example 86** (doc_id: `deanon_260716_TRAIN/3Ob72_20i`) (sent_id: `deanon_260716_TRAIN/3Ob72_20i_22`)


Parallel dazu beauftragte die Klägerin im Herbst 2017 eine Ziviltechniker-GmbH mit der Beweissicherung und einer Grobkostenschätzung für die Sanierung.

**False Positives:**

- `Herbst 2017 eine Ziviltechniker-GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 87** (doc_id: `deanon_260716_TRAIN/3Ob72_20i`) (sent_id: `deanon_260716_TRAIN/3Ob72_20i_23`)


Diese GmbH arbeitete daraufhin zwei Varianten aus;

**False Positives:**

- `Diese GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_260716_TRAIN/3Ob99_10w`) (sent_id: `deanon_260716_TRAIN/3Ob99_10w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Senatspräsidenten Hon.-Prof. Dr. Sailer, den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und den Hofrat Dr. Jensik als weitere Richter in der Rechtssache der klagenden Partei Dr. Johannes Müller, Rechtsanwalt, Wien 3, Ditscheinergasse 2, als Masseverwalter im Konkurs der Wald-Event GmbH, gegen die beklagte Partei Wiener Gebietskrankenkasse, Wien 10, Wienerbergstraße 15-19, vertreten durch Preslmayr Rechtsanwälte OG in Wien, und der Nebenintervenienten auf der Seite der beklagten Partei 1.)

**False Positives:**

- `Masseverwalter im Konkurs der Wald-Event GmbH` — partial — gold is substring of pred: `Wald-Event GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Prückner`(person)
- `Hon.-Prof. Dr. Sailer`(person)
- `Hon.-Prof. Dr. Neumayr`(person)
- `Dr. Lovrek`(person)
- `Dr. Jensik`(person)
- `Dr. Johannes Müller`(person)
- `Wald-Event GmbH`(organisation)
- `Wiener Gebietskrankenkasse`(organisation)
- `Preslmayr Rechtsanwälte OG`(organisation)

**Example 89** (doc_id: `deanon_260716_TRAIN/3Ob99_10w`) (sent_id: `deanon_260716_TRAIN/3Ob99_10w_107`)


Nunmehr sei zusammenfassend geplant, dass 200.000 EUR durch den Investor und 500.000 EUR durch eine Bank finanziert würden, wobei die Bank durch eine persönliche Haftung der Gesellschafter über 250.000 EUR und den Forderungsverkauf der GmbH besichert sei.

**False Positives:**

- `EUR und den Forderungsverkauf der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 90** (doc_id: `deanon_260716_TRAIN/4Nc18_11a`) (sent_id: `deanon_260716_TRAIN/4Nc18_11a_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel und Dr. Jensik als weitere Richter in der Rechtssache der klagenden Partei Kosfelder+Gerasimowitsch KI GmbH, Webergarten 4c, 2534 Maria Raisenmarkt, Österreich, vertreten durch Dr. Christian Fuchshuber LL.M., Rechtsanwalt in Innsbruck, gegen die beklagte Partei Gastronomie Seezor GmbH, Psaltersteig 61, 4624 Felling, Österreich, vertreten durch Dr. Gerhard Strobich, Rechtsanwalt in Trofaiach, wegen 5.873,18 EUR sA, über den Delegierungsantrag der beklagten Partei den Beschluss gefasst:  Spruch Der Antrag, zur Verhandlung und Entscheidung in dieser Rechtssache anstelle des Bezirksgerichts Innsbruck das Bezirksgericht Leoben zu bestimmen, wird abgewiesen.

**False Positives:**

- `Gerasimowitsch KI GmbH` — partial — pred is substring of gold: `Kosfelder+Gerasimowitsch KI GmbH`
- `Partei Gastronomie Seezor GmbH` — partial — gold is substring of pred: `Gastronomie Seezor GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schenk`(person)
- `Dr. Vogel`(person)
- `Dr. Jensik`(person)
- `Kosfelder+Gerasimowitsch KI GmbH`(organisation)
- `Webergarten 4c, 2534 Maria Raisenmarkt, Österreich`(address)
- `Dr. Christian Fuchshuber LL.M.`(person)
- `Gastronomie Seezor GmbH`(organisation)
- `Psaltersteig 61, 4624 Felling, Österreich`(address)
- `Dr. Gerhard Strobich`(person)
- `Bezirksgerichts Innsbruck`(organisation)
- `Bezirksgericht Leoben`(organisation)

**Example 91** (doc_id: `deanon_260716_TRAIN/4Nc3_12x`) (sent_id: `deanon_260716_TRAIN/4Nc3_12x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel und Dr. Jensik als weitere Richter in der beim Landesgericht Innsbruck zu AZ 59 Cg 92/11x anhängigen Rechtssache der klagenden Partei Kelkel-Versicherung GmbH, Walkersdorf 16, 9761 Tröbelsberg, Österreich, vertreten durch Mag. Heinz Heher, Rechtsanwalt in Wien, gegen die beklagte Partei Zorzorzor GmbH, Großenbergstraße 43, 8561 Neudorf bei Sankt Johann ob Hohenburg, Österreich, vertreten durch Dr. Adrian Hollaender, Rechtsanwalt in Innsbruck, wegen Unterlassung, Urteilsveröffentlichung und 67.606 EUR sA, über die Delegierungsanträge der beklagten Partei gemäß § 31 Abs 2 JN, folgenden Beschluss gefasst:  Spruch Die Anträge der beklagten Partei, die Rechtssache an das „Landesgericht Wien“ bzw Handelsgericht Wien zu delegieren, werden abgewiesen.

**False Positives:**

- `Partei Kelkel-Versicherung GmbH` — partial — gold is substring of pred: `Kelkel-Versicherung GmbH`
- `Partei Zorzorzor GmbH` — partial — gold is substring of pred: `Zorzorzor GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schenk`(person)
- `Dr. Vogel`(person)
- `Dr. Jensik`(person)
- `Landesgericht Innsbruck`(organisation)
- `Kelkel-Versicherung GmbH`(organisation)
- `Walkersdorf 16, 9761 Tröbelsberg, Österreich`(address)
- `Mag. Heinz Heher`(person)
- `Zorzorzor GmbH`(organisation)
- `Großenbergstraße 43, 8561 Neudorf bei Sankt Johann ob Hohenburg, Österreich`(address)
- `Dr. Adrian Hollaender`(person)
- `Landesgericht Wien`(organisation)
- `Handelsgericht Wien`(organisation)

</details>

---

## `CompanyAG` 🏆

**F1:** 0.005 | **Precision:** 0.093 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `194d8105`  
**Description:**
Matches company names ending in AG with strict name length (min 5 chars before suffix), excludes legal context words, and prevents partial matches like 'Digital AG'.

**Content:**
```
(?<![A-Za-z])(?<!Firma\s)(?<!der\s)(?<!Firmen\s)(?<!Gesellschafter\s)(?<!Geschäftsführer\s)(?<!Betrieb\s)(?<!Die\s)(?<!an\s)(?<!Beschwerdesache\s)(?<!Gesellschaft\s)(?<!Fa\.\s)(?<!NoV)(?<!FL)(?<!Abs)(?<!\d)(?<!iSd\s)(?<!im\s)(?<!des\s)(?<!der\s)(?<!in\s)(?<!für\s)(?<!nach\s)(?<!vor\s)(?<!über\s)(?<!unter\s)(?<!bei\s)(?<!mit\s)(?<!aus\s)(?<!auf\s)(?<!zu\s)(?<!von\s)(?<!am\s)(?<!um\s)(?<!bis\s)(?<!seit\s)(?<!durch\s)(?<!gegen\s)(?<!ohne\s)(?<!§)(?<!\d)([A-Z][A-Za-z0-9\s&\-\.]{5,30}AG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.093 | 0.002 | 0.005 | 108 | 10 | 98 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 10 | 98 | 3633 |

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

**Example 2** (doc_id: `deanon_260716_TRAIN/2Nc25_11s`) (sent_id: `deanon_260716_TRAIN/2Nc25_11s_3`)


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

**Example 3** (doc_id: `deanon_260716_TRAIN/2Ob115_10s`) (sent_id: `deanon_260716_TRAIN/2Ob115_10s_4`)


Uniber-Verlag AG, Jedretsberg 24, 4190 Brunnwald, Österreich, und 2. Fenuni AG, Wildschönauerstraße, Oberau 3, 8444 Reith, Österreich, beide vertreten durch die Liebenwein Rechtsanwälte GmbH in Wien, gegen die beklagten und widerklagenden Parteien 1.

| Predicted | Gold |
|---|---|
| `Uniber-Verlag AG` | `Uniber-Verlag AG` |
| `Fenuni AG` | `Fenuni AG` |

**Missed by this rule (FN):**

- `Jedretsberg 24, 4190 Brunnwald, Österreich` (address)
- `Wildschönauerstraße, Oberau 3, 8444 Reith, Österreich` (address)
- `Liebenwein Rechtsanwälte GmbH` (organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/2Ob85_11f`) (sent_id: `deanon_260716_TRAIN/2Ob85_11f_4`)


Guntram Wellenbring, vertreten durch Dr. Peter Sparer, Rechtsanwalt in Innsbruck, 2. Verbruckal AG, Stäpfle 16, 1020 Wien, Österreich, vertreten durch Dr. Harald Burmann und andere Rechtsanwälte in Innsbruck, und 3.

| Predicted | Gold |
|---|---|
| `Verbruckal AG` | `Verbruckal AG` |

**Missed by this rule (FN):**

- `Guntram Wellenbring` (person)
- `Dr. Peter` (person)
- `Stäpfle 16, 1020 Wien, Österreich` (address)
- `Dr. Harald Burmann` (person)

**Example 5** (doc_id: `deanon_260716_TRAIN/2Ob85_11f`) (sent_id: `deanon_260716_TRAIN/2Ob85_11f_5`)


See-Umwelt Manufaktur AG, Zosen 244, 9543 Sauboden, Österreich, vertreten durch Dr. Walter Heel, Rechtsanwalt in Innsbruck, wegen 62.404,99 EUR sA und Feststellung (Streitinteresse: 10.000 EUR), über die Revisionen der klagenden, der erstbeklagten und der zweitbeklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Jänner 2011, GZ 4 R 250/10m-85, womit infolge der Berufungen der klagenden, der erstbeklagten und der zweitbeklagten Partei das Urteil des Landesgerichts Innsbruck vom 25. August 2010, GZ 5 Cg 160/08w-74, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Sämtliche Revisionen werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `See-Umwelt Manufaktur AG` | `See-Umwelt Manufaktur AG` |

**Missed by this rule (FN):**

- `Zosen 244, 9543 Sauboden, Österreich` (address)
- `Dr. Walter Heel` (person)
- `Oberlandesgerichts Innsbruck` (organisation)
- `Landesgerichts Innsbruck` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/4Ob9_20g`) (sent_id: `deanon_260716_TRAIN/4Ob9_20g_3`)


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

**Example 7** (doc_id: `deanon_260716_TRAIN/5Ob141_23f`) (sent_id: `deanon_260716_TRAIN/5Ob141_23f_17`)


Ende des Jahres 2018 schloss er sich der deutschen Musterfeststellungsklage gegen die ONTJ Textil AG an.

| Predicted | Gold |
|---|---|
| `ONTJ Textil AG` | `ONTJ Textil AG` |

**Example 8** (doc_id: `deanon_260716_TRAIN/8ObA18_17f`) (sent_id: `deanon_260716_TRAIN/8ObA18_17f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Brenn als weitere Richter sowie die fachkundigen Laienrichter Mag. Dr. Bernhard Gruber und Harald Kohlruss in der Arbeitsrechtssache der klagenden Partei MedR Clemens Schepper, vertreten durch Freimüller/Obereder/Pilz Rechtsanwält_innen GmbH in Wien, gegen die beklagte Partei Muehleis & Klaese Technik AG, Rosentaler Weg 2k, 9811 St. Peter in Holz, Österreich, vertreten durch DLA Piper Weiss-Tessbach Rechtsanwälte GmbH in Wien, wegen Feststellung (Streitwert 282,56 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. November 2016, GZ 7 Ra 90/16f-19, mit dem das Urteil des Arbeits- und Sozialgerichts Wien vom 20. Juli 2016, GZ 33 Cga 50/16p-15, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Muehleis & Klaese Technik AG` | `Muehleis & Klaese Technik AG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Prof. Dr. Spenling` (person)
- `Dr. Tarmann-Prentner` (person)
- `Dr. Brenn` (person)
- `Mag. Dr. Bernhard Gruber` (person)
- `Harald Kohlruss` (person)
- `MedR Clemens Schepper` (person)
- `Freimüller/Obereder/Pilz Rechtsanwält_innen GmbH` (organisation)
- `Rosentaler Weg 2k, 9811 St. Peter in Holz, Österreich` (address)
- `DLA Piper Weiss-Tessbach Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Antonewitz Chemie AG` — partial — pred is substring of gold: `Langhansl+Antonewitz Chemie AG`

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

**Example 1** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_30`)


Die GmbH verfügt auch über keine Bewilligung als Krankenanstalt bzw selbständiges Ambulatorium im Sinne des WrKAG und über keinen ärztlichen Leiter.

**False Positives:**

- `Ambulatorium im Sinne des WrKAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a__16`)


Mit Urteil desselben Tages erkannte das Gericht den Angeklagten „im Sinne der Anklageschrift“ des Verbrechens des gewerbsmäßig und als Mitglied einer kriminellen Vereinigung durch Einbruch begangenen schweren Diebstahls nach §§ 127, 128 Abs 2, 129 Abs 1 Z 1, 130 Abs 1 erster und zweiter Fall, Abs 2 erster und zweiter Fall und 15 StGB sowie mehrerer Vergehen der Urkundenunterdrückung nach § 229 Abs 1 StGB schuldig, verhängte über ihn eine Freiheitsstrafe und verpflichtete ihn, an die Privatbeteiligte St Donau Triheim AG einen Geldbetrag zu bezahlen.

**False Positives:**

- `St Donau Triheim AG` — partial — gold is substring of pred: `Donau Triheim AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Donau Triheim AG`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/1Ob159_20v`) (sent_id: `deanon_260716_TRAIN/1Ob159_20v_3`)


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

**Example 4** (doc_id: `deanon_260716_TRAIN/1Ob163_21h`) (sent_id: `deanon_260716_TRAIN/1Ob163_21h_3`)


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

**Example 5** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Dr. Florenzia Münsterer, vertreten durch Rechtsanwälte Dr. Amhof & Dr. Damian GmbH in Wien, gegen die beklagte Partei MittelEnergie Werke Bank AG, Altlassing 110, 4183 Ahorn, Österreich, vertreten durch Urbanek Lind Schmied Reisch Rechtsanwälte OG in Wien, wegen 600.090 EUR sA, über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 25. Mai 2011, GZ 15 R 64/11h-54, mit dem das Urteil des Handelsgerichts Wien vom 14. Jänner 2011, GZ 16 Cg 20/10f-50, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `MittelEnergie Werke Bank AG` — partial — gold is substring of pred: `MittelEnergie Werke Bank`

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

**Example 6** (doc_id: `deanon_260716_TRAIN/1Ob226_20x`) (sent_id: `deanon_260716_TRAIN/1Ob226_20x_52`)


C-620/17,Hochtief Solutions AG, Rn 35, jeweils mwN).

**False Positives:**

- `Hochtief Solutions AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_260716_TRAIN/1Ob56_17t`) (sent_id: `deanon_260716_TRAIN/1Ob56_17t_4`)


Gloria Hackenbuchner GmbH, Untere Kanalstraße 187, 2471 Hollern, Österreich, vertreten durch Mag. Manfred Sommerbauer und MMag. Dr. Michael Dohr LL.M., Rechtsanwälte in Wiener Neustadt, und 2. Nelleßen + Stümpfel Automotive AG, Villengasse 31, 8670 Krieglach, Österreich, vertreten durch die Kosch & Partner Rechtsanwälte GmbH, Wiener Neustadt, wegen 76.444,01 EUR sA über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Jänner 2017, GZ 1 R 164/16v-174, mit dem das Urteil des Handelsgerichts Wien vom 12. August 2016, GZ 65 Cg 12/15x-169, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Automotive AG` — partial — pred is substring of gold: `Nelleßen + Stümpfel Automotive AG`

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

**Example 8** (doc_id: `deanon_260716_TRAIN/23Os1_15t`) (sent_id: `deanon_260716_TRAIN/23Os1_15t_6`)


Text Gründe: Mit dem angefochtenen Erkenntnis wurde Dr. Xaver Springinsgut, Rechtsanwalt in St.Oswald - Rosennockstraße 31, 2051 Platt, Österreich, wegen des Verstoßes gegen die Bestimmungen des § 9 (Abs 1) RAO und des § 2 RL-BA der Disziplinarvergehen der Verletzung von Berufspflichten und der Beeinträchtigung von Ehre oder (richtig:) Ansehen des Standes nach § 1 Abs 1 erster und zweiter Fall DSt schuldig erkannt, weil er als Rechtsvertreter der Ehegatten Roman und Elfriede Jähnel in Anträgen auf Aufschiebung der Zwangsversteigerungen für seine Mandanten vom 5. September 2013 in näher bezeichneten Verfahren des Bezirksgerichts Innsbruck und des Bezirksgerichts Amstetten sowie in einer näher genannten Feststellungsklage an das Landesgericht Linz vom 7. Oktober 2013 und in einer Impugnationsklage an das Bezirksgericht Amstetten vom 10. Oktober 2013 jeweils vorgebracht hatte, seine Mandanten hätten sämtliche Verpflichtungen aus einer mit der Alpen Nexlex AG abgeschlossenen Vereinbarung vom 11. Dezember 2012, insbesondere jene zur unwiderruflichen Antragstellung auf Aufhebung der Höfeeigenschaft einer näher bezeichnenden Liegenschaft in Schulgartenweg 18, 9872 Grantsch, Österreich, eingehalten, obwohl ihm zum Zeitpunkt der Antragstellung und Klagseinbringung bekannt war, dass der Antrag auf Aufhebung der Höfeeigenschaft vom 13. Dezember 2012 bereits am 14. Juni 2013 von Roman Jiran, durch ihn vertreten, entgegen der zuvor genannten Vereinbarung vom 11. Dezember 2012 wieder zurückgezogen worden war.

**False Positives:**

- `Nexlex AG` — partial — pred is substring of gold: `Alpen Nexlex AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Xaver Springinsgut`(person)
- `St.Oswald - Rosennockstraße 31, 2051 Platt, Österreich`(address)
- `Elfriede Jähnel`(person)
- `Bezirksgerichts Innsbruck`(organisation)
- `Bezirksgerichts Amstetten`(organisation)
- `Landesgericht Linz`(organisation)
- `Bezirksgericht Amstetten`(organisation)
- `Alpen Nexlex AG`(organisation)
- `Schulgartenweg 18, 9872 Grantsch, Österreich`(address)
- `Roman Jiran`(person)

**Example 9** (doc_id: `deanon_260716_TRAIN/23Os1_15t`) (sent_id: `deanon_260716_TRAIN/23Os1_15t_9`)


Denn die Beweisthemen (Geschäftsgrundlage der eingangs genannten Vereinbarung vom 11. Dezember 2012 mit der Bornwasser & Plöckinger Druck AG; von derselben intendierte Verwertung der Liegenschaften in Thalstraße 358X, 5232 Aigen, Österreich durch Zwangsversteigerung ungeachtet eines allfälligen Abverkaufs von Liegenschaften in Am Weinbühel 2, 5201 Wimm, Österreich ; Auftrag der Mandanten des Disziplinarbeschuldigten zur Zurückziehung des Antrags auf Aufhebung der Höfeeigenschaft;

**False Positives:**

- `Druck AG` — partial — pred is substring of gold: `Bornwasser & Plöckinger Druck AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bornwasser & Plöckinger Druck AG`(organisation)
- `Thalstraße 358X, 5232 Aigen, Österreich`(address)
- `Am Weinbühel 2, 5201 Wimm, Österreich`(address)

**Example 10** (doc_id: `deanon_260716_TRAIN/23Os1_15t`) (sent_id: `deanon_260716_TRAIN/23Os1_15t_10`)


Unkenntnis des Disziplinarbeschuldigten von den Gründen der Griete+Leine Technik AG für die beantragte Fortsetzung der Zwangsversteigerungsverfahren;

**False Positives:**

- `Leine Technik AG` — partial — pred is substring of gold: `Griete+Leine Technik AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Griete+Leine Technik AG`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/2Ob216_18f`) (sent_id: `deanon_260716_TRAIN/2Ob216_18f_3`)


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

**Example 12** (doc_id: `deanon_260716_TRAIN/2Ob71_18g`) (sent_id: `deanon_260716_TRAIN/2Ob71_18g_3`)


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

**Example 13** (doc_id: `deanon_260716_TRAIN/2Ob85_11f`) (sent_id: `deanon_260716_TRAIN/2Ob85_11f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Niklas Nikoloff, 9020 Klagenfurt, vertreten durch Mag. Michael Hirm, Rechtsanwalt in Klagenfurt, sowie der Nebenintervenientin auf Seiten der klagenden Partei Wetzlau+Härdle Versicherung AG, Maulwurfgasse 2, 4090 Stadl, Österreich, vertreten durch Dr. Martin Wuelz, Rechtsanwalt in Innsbruck, gegen die beklagten Parteien 1.

**False Positives:**

- `Versicherung AG` — partial — pred is substring of gold: `Wetzlau+Härdle Versicherung AG`

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

**Example 14** (doc_id: `deanon_260716_TRAIN/2Ob89_17b`) (sent_id: `deanon_260716_TRAIN/2Ob89_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende, die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé sowie den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Dipl.-Ing. Eleonore Wagenbret, vertreten durch Posch, Schausberger & Lutz Rechtsanwälte GmbH in Wels, gegen die beklagten Parteien 1. Rudolfa Schoenmaekers, 2. Lorena Sieckkötter, und 3. TraunSanitär Dienstleistungen Versicherungs-AG, Georg Pfligersdorffer-Gasse 71, 3610 Maigen, Österreich, alle vertreten durch Mag. Dr. A. Michael Dallinger, Rechtsanwalt in Wels, wegen 187.040,19 EUR sA und Feststellung (Streitinteresse: 5.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 1. März 2017, GZ 6 R 30/17z-42, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dienstleistungen Versicherungs-AG` — partial — pred is substring of gold: `TraunSanitär Dienstleistungen Versicherungs-AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Dr. Veith`(person)
- `Dr. Musger`(person)
- `Dr. E. Solé`(person)
- `Dr. Nowotny`(person)
- `Dipl.-Ing. Eleonore Wagenbret`(person)
- `Posch, Schausberger & Lutz Rechtsanwälte GmbH`(organisation)
- `Rudolfa Schoenmaekers`(person)
- `Lorena Sieckkötter`(person)
- `TraunSanitär Dienstleistungen Versicherungs-AG`(organisation)
- `Georg Pfligersdorffer-Gasse 71, 3610 Maigen, Österreich`(address)
- `Mag. Dr. A. Michael Dallinger`(person)
- `Oberlandesgerichts Linz`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/3Ob72_20i`) (sent_id: `deanon_260716_TRAIN/3Ob72_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Marktgemeinde James Weyand, MA, vertreten durch Dr. Nader Karl Mahdi, Rechtsanwalt in Wattens, gegen die beklagte Partei Lützeler Garten AG, Esteplatz 2, 9064 Schöpfendorf, Österreich, vertreten durch Altenweisl Wallnöfer Watschinger Zimmermann Rechtsanwälte GmbH in Innsbruck, und die auf Seiten der beklagten Partei beigetretene Nebenintervenientin Demeyer u. Köktas Analyse GmbH, Zinkendorferstraße 100, 9321 Schöttlhof, Österreich, vertreten durch Dr. Christian Girardi, LL.M., Ing. Dr. Stefan Schwärzler, Mag. Daniel Pichler, Rechtsanwälte in Innsbruck, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. März 2020, GZ 1 R 5/20z-27, womit das Urteil des Landesgerichts Innsbruck vom 14. November 2019, GZ 12 Cg 33/19m-18, teilweise bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Garten AG` — partial — pred is substring of gold: `Lützeler Garten AG`

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

**Example 16** (doc_id: `deanon_260716_TRAIN/4Fsc1_10z`) (sent_id: `deanon_260716_TRAIN/4Fsc1_10z_3`)


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

**Example 17** (doc_id: `deanon_260716_TRAIN/4Nc4_17a`) (sent_id: `deanon_260716_TRAIN/4Nc4_17a_5`)


Sanitär Norfurtwerk AG, Piburger Straße 20, 4204 Hadersdorf, Österreich, Deutschland, beide vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Gesamtstreitwert 69.500 EUR), über den Ordinationsantrag der Klägerinnen den Beschluss gefasst:  Spruch Dem Ordinationsantrag wird stattgegeben.

**False Positives:**

- `Norfurtwerk AG` — partial — pred is substring of gold: `Sanitär Norfurtwerk AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Sanitär Norfurtwerk AG`(organisation)
- `Piburger Straße 20, 4204 Hadersdorf, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/4Ob165_09g`) (sent_id: `deanon_260716_TRAIN/4Ob165_09g_3`)


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

**Example 19** (doc_id: `deanon_260716_TRAIN/4Ob174_24b`) (sent_id: `deanon_260716_TRAIN/4Ob174_24b_3`)


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

**Example 20** (doc_id: `deanon_260716_TRAIN/4Ob19_10p`) (sent_id: `deanon_260716_TRAIN/4Ob19_10p_3`)


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

**Example 21** (doc_id: `deanon_260716_TRAIN/4Ob64_18t`) (sent_id: `deanon_260716_TRAIN/4Ob64_18t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Vogel als Vorsitzenden sowie die Hofräte Dr. Schwarzenbacher, Hon.-Prof. Dr. Brenn, Dr. Rassi und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Mag. Florentin Jakobautzki, vertreten durch die Konrad Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Lischke&Rohleff Solar AG, Volkshausplatz 46, 3830 Pyhra, Österreich, vertreten durch die Binder Grösswang Rechtsanwälte GmbH in Wien, wegen 106.196,74 EUR sA und Feststellung (Streitwert 156.303,26 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 13. Oktober 2017, GZ 129 R 24/17y-24, womit das Urteil des Handelsgerichts Wien vom 2. August 2017, GZ 10 Cg 1/16a-19, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Lischke&Rohleff Solar AG` — partial — gold is substring of pred: `Lischke&Rohleff Solar AG`

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

**Example 22** (doc_id: `deanon_260716_TRAIN/4Ob64_18t`) (sent_id: `deanon_260716_TRAIN/4Ob64_18t_16`)


4. Auf die Frage, ob die Informationserteilung durch den außenstehenden Berater dem Gebot vollständiger, richtiger und rechtzeitiger Beratung (RIS-Justiz RS0123046) im Lichte des § 17 Abs 3 Z 1 WAG 1996 entsprochen hat (vgl 3 Ob 190/16m mwN), muss hier nicht eingegangen werden.

**False Positives:**

- `Abs 3 Z 1 WAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_260716_TRAIN/5Ob102_24x`) (sent_id: `deanon_260716_TRAIN/5Ob102_24x_3`)


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

**Example 24** (doc_id: `deanon_260716_TRAIN/5Ob141_23f`) (sent_id: `deanon_260716_TRAIN/5Ob141_23f_3`)


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

**Example 25** (doc_id: `deanon_260716_TRAIN/5Ob221_22v`) (sent_id: `deanon_260716_TRAIN/5Ob221_22v_3`)


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

**Example 26** (doc_id: `deanon_260716_TRAIN/6Ob10_22x`) (sent_id: `deanon_260716_TRAIN/6Ob10_22x_3`)


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

**Example 27** (doc_id: `deanon_260716_TRAIN/6Ob118_16w`) (sent_id: `deanon_260716_TRAIN/6Ob118_16w_63`)


Der Oberste Gerichtshof hat in der Entscheidung 6 Ob 246/15t ausgesprochen, dass § 13 Z 3 und 4 WAG 1996 es einem Wertpapierdienstleister überlässt, in welcher Art und Weise er in der Anlageberatung seinen Kunden informiert.

**False Positives:**

- `Z 3 und 4 WAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/6Ob118_16w`) (sent_id: `deanon_260716_TRAIN/6Ob118_16w_115`)


Auch nach den Wohlverhaltensregeln des WAG 1996 sind Beratung und Aufklärung nicht vom Kunden nachzufragen, sondern von den in § 11 WAG 1996 genannten Rechtsträgern anzubieten.

**False Positives:**

- `Wohlverhaltensregeln des WAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_260716_TRAIN/6Ob231_24z`) (sent_id: `deanon_260716_TRAIN/6Ob231_24z_3`)


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

**Example 30** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_33`)


Diese Gesetzeslücke sei durch eine analoge Anwendung des § 14 Abs 3 FBG auf gemeinnützige Bauvereinigungen in sämtlichen möglichen Rechtsformen (also auch in der Rechtsform einer GmbH oder AG) anzuwenden.

**False Positives:**

- `GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_60`)


Dem Revisionsverband komme somit schon als solchem die Antrags- und Rechtsmittelbefugnis nach § 14 Abs 3 FBG zu. Eine Unterscheidung dahingehend, dass § 14 Abs 3 FBG dem Revisionsverband Parteistellung nur bei gemeinnützigen Bauvereinigungen in der Rechtsform einer Genossenschaft, nicht aber auch einer GmbH oder AG zuerkenne, wäre sachlich nicht gerechtfertigt.

**False Positives:**

- `GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_103`)


Wenn nun kraft ausdrücklicher gesetzlicher Vorschrift gemeinnützige Bauvereinigungen auch in den Rechtsformen einer GmbH oder AG erlaubt sind (§ 1 Abs 1 WGG) und gleichzeitig auch für diese die Pflicht statuiert wird, einem Revisionsverband anzugehören (§ 5 Abs 1 WGG), so ist auch für eine in der Rechtsform einer GmbH oder AG bestehende Bauvereinigung der Revisionsverband als „zuständig“ im Sinn von § 14 Abs 3 FBG und demgemäß insoweit als Amtspartei anzusehen.

**False Positives:**

- `GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_107`)


Es muss daher davon ausgegangen werden, dass sowohl der Gesetzgeber des FBG als auch der mehrfache (Novellen-)Gesetzgeber des WGG die Zuständigkeit des Revisionsverbands für Bauvereinigungen in der Rechtsform einer GmbH oder AG übersehen hat.

**False Positives:**

- `GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_108`)


Es liegt nach Ansicht des Senats daher insoweit eine durch Analogie zu füllende Gesetzeslücke dahingehend vor, dass der für eine gemeinnützige Bauvereinigung zuständige Revisionsverband auch dann Amtspartei im Sinne des § 14 Abs 3 FBG ist, wenn die Bauvereinigung nicht in der Rechtsform einer Erwerbs- und Wirtschaftsgenossenschaft, sondern einer GmbH oder AG besteht (in diesem Sinn auchSchwetz/Gahler, Wohnungsgemeinnützigkeit und Firmenbuch – Wechselwirkung und Spannungsbogen?

**False Positives:**

- `GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_137`)


Der EuGH teilte die von einigen Mitgliedstaaten (darunter auch Österreich) geäußerte Rechtsansicht, eine Befristung des Widerrufsrechts sei aus Gründen der Rechtssicherheit unerlässlich, nicht (EuGH C-481/99 [Georg und Helga Heininger/Bayerische Hypo- und Vereinsbank AG]).

**False Positives:**

- `Hypo- und Vereinsbank AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_260716_TRAIN/6Ob47_25t`) (sent_id: `deanon_260716_TRAIN/6Ob47_25t_3`)


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

**Example 37** (doc_id: `deanon_260716_TRAIN/6Ob51_21z`) (sent_id: `deanon_260716_TRAIN/6Ob51_21z_3`)


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

**Example 38** (doc_id: `deanon_260716_TRAIN/7Nc6_13m`) (sent_id: `deanon_260716_TRAIN/7Nc6_13m_3`)


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

**Example 39** (doc_id: `deanon_260716_TRAIN/7Ob110_13x`) (sent_id: `deanon_260716_TRAIN/7Ob110_13x_3`)


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

**Example 40** (doc_id: `deanon_260716_TRAIN/7Ob113_17v`) (sent_id: `deanon_260716_TRAIN/7Ob113_17v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Dr. Höllwerth, Dr. E. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Camilla Löble, vertreten durch Waltl & Partner, Rechtsanwälte in Zell am See, gegen die beklagte Partei Sieckkötter Medien AG, 6.

**False Positives:**

- `Medien AG` — partial — pred is substring of gold: `Sieckkötter Medien AG`

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

**Example 41** (doc_id: `deanon_260716_TRAIN/7Ob116_22t`) (sent_id: `deanon_260716_TRAIN/7Ob116_22t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Dr. Wurdinger, Mag. Malesich, Dr. Weber und Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Hedwig Konnertz, MSc, vertreten durch Dr. Christof Joham und Mag. Andreas Voggenberger, Rechtsanwälte in Eugendorf, gegen die beklagte Partei Noruniwald KI -AG, Teichterberg 14y, 3394 Wolfstein, Österreich, vertreten durch Dr. Haymo Modelhart und andere, Rechtsanwälte in Linz, wegen 9.132,90 EUR sA und Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 5. Mai 2022, GZ 53 R 51/22i-41, womit das Urteil des Bezirksgerichts Salzburg vom 26. Jänner 2022, GZ 12 C 675/20w-37, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei Noruniwald KI -AG` — partial — gold is substring of pred: `Noruniwald KI -AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Solé`(person)
- `Mag. Dr. Wurdinger`(person)
- `Mag. Malesich`(person)
- `Dr. Weber`(person)
- `Mag. Fitz`(person)
- `Hedwig Konnertz, MSc`(person)
- `Dr. Christof Joham`(person)
- `Mag. Andreas Voggenberger`(person)
- `Noruniwald KI -AG`(organisation)
- `Teichterberg 14y, 3394 Wolfstein, Österreich`(address)
- `Dr. Haymo Modelhart`(person)
- `Landesgerichts Salzburg`(organisation)
- `Bezirksgerichts Salzburg`(organisation)

**Example 42** (doc_id: `deanon_260716_TRAIN/7Ob129_10m`) (sent_id: `deanon_260716_TRAIN/7Ob129_10m_3`)


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

**Example 43** (doc_id: `deanon_260716_TRAIN/7Ob137_17y`) (sent_id: `deanon_260716_TRAIN/7Ob137_17y_3`)


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

**Example 44** (doc_id: `deanon_260716_TRAIN/7Ob137_20b`) (sent_id: `deanon_260716_TRAIN/7Ob137_20b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende sowie die Hofrätin und die Hofräte Hon.-Prof. Dr. Höllwerth, Mag. Dr. Wurdinger, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Mag. Edwin Bornemeyer, vertreten durch die Pilz & Burghofer Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Thönniß Immobilien AG, Dürnstein in der Steiermark 55, 3920 Josefsdorf, Österreich, vertreten durch Mag. Dr. Otto Ranzenhofer, Rechtsanwalt in Wien, wegen 300.000 EUR sA, den Beschluss gefasst:  Spruch Das Urteil des Obersten Gerichtshofs vom 25. November 2020, AZ 7 Ob 137/20b, wird wie folgt berichtigt: Im Spruchpunkt 2. hat die Wortfolge: „samt 4 % Zinsen seit 3. 11. 2014“ zu entfallen.

**False Positives:**

- `Immobilien AG` — partial — pred is substring of gold: `Thönniß Immobilien AG`

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

**Example 45** (doc_id: `deanon_260716_TRAIN/7Ob162_20d`) (sent_id: `deanon_260716_TRAIN/7Ob162_20d_3`)


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

**Example 46** (doc_id: `deanon_260716_TRAIN/7Ob192_16k`) (sent_id: `deanon_260716_TRAIN/7Ob192_16k_3`)


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

**Example 47** (doc_id: `deanon_260716_TRAIN/7Ob193_21i`) (sent_id: `deanon_260716_TRAIN/7Ob193_21i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätin und Hofräte Mag. Dr. Wurdinger, Mag. Malesich, MMag. Matzka und Dr. Weber als weitere Richter in der Rechtssache der klagenden Partei Zerweckh & Braunmöller Touristik GmbH, Albert-Böhler-Gasse 8, 9832 Stieflberg, Österreich, vertreten durch Schmid & Horn Rechtsanwälte GmbH in Graz, gegen die beklagte Partei VJHV Event Werke -AG, Oberpfälzer Weg 3, 4733 Eitzenberg, Österreich, vertreten durch Dr. Wolfgang Muchitsch, Rechtsanwalt in Graz, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 7. Oktober 2021, GZ 2 R 175/21d-15, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei VJHV Event Werke -AG` — partial — gold is substring of pred: `VJHV Event Werke -AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Mag. Dr. Wurdinger`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Dr. Weber`(person)
- `Zerweckh & Braunmöller Touristik GmbH`(organisation)
- `Albert-Böhler-Gasse 8, 9832 Stieflberg, Österreich`(address)
- `Schmid & Horn Rechtsanwälte GmbH`(organisation)
- `VJHV Event Werke -AG`(organisation)
- `Oberpfälzer Weg 3, 4733 Eitzenberg, Österreich`(address)
- `Dr. Wolfgang Muchitsch`(person)
- `Oberlandesgerichts Graz`(organisation)

**Example 48** (doc_id: `deanon_260716_TRAIN/7Ob201_12b`) (sent_id: `deanon_260716_TRAIN/7Ob201_12b_3`)


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

**Example 49** (doc_id: `deanon_260716_TRAIN/7Ob201_12b`) (sent_id: `deanon_260716_TRAIN/7Ob201_12b_269`)


Im Sinn von § 104 Abs 2 Z 2 VAG besteht der Grundsatz, dass Versicherte durch das Leistungsversprechen des Versicherers oder das vereinbarte Versicherungsentgelt ohne sachlichen Grund nicht begünstigt werden dürfen.

**False Positives:**

- `Abs 2 Z 2 VAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_260716_TRAIN/7Ob36_25g`) (sent_id: `deanon_260716_TRAIN/7Ob36_25g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Malesich, Dr. Weber, Mag. Fitz und Mag. Jelinek als weitere Richter in der Rechtssache der klagenden Partei Gundula Aichmann, vertreten durch Poduschka Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Plönnigs Technik AG, Wieden 35, 3390 Spielberg, Österreich, vertreten durch Themmer, Toth & Partner Rechtsanwälte GmbH in Wien, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 28. November 2024, GZ 1 R 124/24t-14, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 27. Juni 2024, GZ 21 C 604/23m-10, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Technik AG` — partial — pred is substring of gold: `Plönnigs Technik AG`

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

**Example 51** (doc_id: `deanon_260716_TRAIN/7Ob45_19x`) (sent_id: `deanon_260716_TRAIN/7Ob45_19x_3`)


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

**Example 52** (doc_id: `deanon_260716_TRAIN/7Ob48_17k`) (sent_id: `deanon_260716_TRAIN/7Ob48_17k_3`)


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

**Example 53** (doc_id: `deanon_260716_TRAIN/7Ob48_17k`) (sent_id: `deanon_260716_TRAIN/7Ob48_17k_16`)


2. Die Klägerin will auf das vorliegende Kreditverhältnis die Wohlverhaltensregeln des WAG 2007 angewendet wissen.

**False Positives:**

- `Wohlverhaltensregeln des WAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_260716_TRAIN/7Ob48_17k`) (sent_id: `deanon_260716_TRAIN/7Ob48_17k_17`)


2.1 Der Oberste Gerichtshof hat bereits ausgesprochen, dass es sich bei gewährten (endfälligen) Fremdwährungskrediten weder um eine Wertpapierdienstleistung noch um eine Anlagetätigkeit im Sinn des § 1 Z 2 WAG handelt. Ein Finanzinstrument nach § 1 Z 6 WAG liegt ebenfalls nicht vor, insbesondere auch nicht in Form eines Differenzgeschäfts nach § 1 Z 6 lit i WAG.

**False Positives:**

- `Z 6 lit i WAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

**Example 55** (doc_id: `deanon_260716_TRAIN/7Ob48_17k`) (sent_id: `deanon_260716_TRAIN/7Ob48_17k_20`)


Durch den expliziten Verweis in § 1 Z 2 lit b WAG 2007 auf § 1 Abs 1 Z 7 WAG fänden die Abschnitte 5 bis 11 des zweiten Hauptstücks des WAG 2007 auf den Devisenhandel (§ 1 Abs 1 Z 7 lit a BWG) Anwendung.

**False Positives:**

- `Z 2 lit b WAG` — no gold match — likely missing annotation
- `Abs 1 Z 7 WAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 56** (doc_id: `deanon_260716_TRAIN/7Ob48_17k`) (sent_id: `deanon_260716_TRAIN/7Ob48_17k_28`)


Dabei handelt es sich um ein Kreditgeschäft nach § 1 Z 3 BWG, in welchem Zusammenhang auf die Anwendung des WAG 2007 nicht verwiesen wird.

**False Positives:**

- `Anwendung des WAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_260716_TRAIN/7Ob54_20x`) (sent_id: `deanon_260716_TRAIN/7Ob54_20x_3`)


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

**Example 58** (doc_id: `deanon_260716_TRAIN/7Ob60_18a`) (sent_id: `deanon_260716_TRAIN/7Ob60_18a_3`)


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

**Example 59** (doc_id: `deanon_260716_TRAIN/7Ob6_20p`) (sent_id: `deanon_260716_TRAIN/7Ob6_20p_3`)


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

**Example 60** (doc_id: `deanon_260716_TRAIN/7Ob6_20p`) (sent_id: `deanon_260716_TRAIN/7Ob6_20p_34`)


1.3.Der bei Vertragsabschluss (bis 9. 12. 2007) geltende § 9a Abs 1 VAG (idF BGBl 1996/447) lautete soweit hier relevant: „(1)

**False Positives:**

- `Abs 1 VAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_260716_TRAIN/7Ob79_10h`) (sent_id: `deanon_260716_TRAIN/7Ob79_10h_3`)


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

**Example 62** (doc_id: `deanon_260716_TRAIN/7Ob85_15y`) (sent_id: `deanon_260716_TRAIN/7Ob85_15y_4`)


Isabel Nestle AG, Reinsbach 186, 9131 Dolina, Österreich, vertreten durch Jank Weiler Operenyi Rechtsanwälte OG in Wien, 2.

**False Positives:**

- `Isabel Nestle AG` — partial — gold is substring of pred: `Isabel Nestle`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Isabel Nestle`(person)
- `Reinsbach 186, 9131 Dolina, Österreich`(address)
- `Jank Weiler Operenyi Rechtsanwälte OG`(organisation)

**Example 63** (doc_id: `deanon_260716_TRAIN/7Ob92_19h`) (sent_id: `deanon_260716_TRAIN/7Ob92_19h_3`)


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

**Example 64** (doc_id: `deanon_260716_TRAIN/7Ob94_20d`) (sent_id: `deanon_260716_TRAIN/7Ob94_20d_3`)


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

**Example 65** (doc_id: `deanon_260716_TRAIN/8Ob35_23i`) (sent_id: `deanon_260716_TRAIN/8Ob35_23i_3`)


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

**Example 66** (doc_id: `deanon_260716_TRAIN/8Ob39_24d`) (sent_id: `deanon_260716_TRAIN/8Ob39_24d_6`)


Er brachte vor, über seine depotführende Bank in Graz mehrfach Aktien der Krautsch Analyse AG mit Sitz in Deutschland gekauft zu haben (und zwar, wie aus den von ihm vorgelegten Beilagen ersichtlich, „loco Düsseldorf“).

**False Positives:**

- `Aktien der Krautsch Analyse AG` — partial — gold is substring of pred: `Krautsch Analyse AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Krautsch Analyse AG`(organisation)

**Example 67** (doc_id: `deanon_260716_TRAIN/8Ob39_24d`) (sent_id: `deanon_260716_TRAIN/8Ob39_24d_12`)


Die OberSoftware AG habe insofern auch Offenlegungspflichten in Österreich getroffen.

**False Positives:**

- `Die OberSoftware AG` — partial — gold is substring of pred: `OberSoftware AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OberSoftware AG`(organisation)

**Example 68** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden und die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn sowie die fachkundigen Laienrichter Mag. Dr. Monika Lanz und Wolfgang Cadilek als weitere Richter in der Arbeitsrechtssache der klagenden Partei Hon.-Prof. Dieter Kovacs, vertreten durch Pfurtscheller Orgler Huber, Rechtsanwälte in Innsbruck, gegen die beklagte Partei ÖBB-Personenverkehr AG, Monsbergergasse 12, 6210 Astenberg, Österreich, vertreten durch die CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 3.963,75 EUR brutto sA, aus Anlass der (außerordentlichen) Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. Februar 2013, GZ 13 Ra 1/13i-16, mit dem das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 16. Oktober 2012, GZ 42 Cga 87/12h-12, abgeändert wurde, den Beschluss gefasst:  Spruch A.Dem Gerichtshof der Europäischen Union werden folgende Fragen zur Vorabentscheidung vorgelegt: 1.Ist Art 21 der Grundrechtecharta in Verbindung mit Art 7 Abs 1, Art 16 und Art 17 der Richtlinie 2000/78/EG dahin auszulegen, dass a)ein Arbeitnehmer, für den vom Arbeitgeber aufgrund einer gesetzlich normierten altersdiskriminierenden Anrechnung von Vordienstzeiten zunächst ein unrichtiger Vorrückungsstichtag festgesetzt wurde, in jedem Fall Anspruch auf Zahlung der Gehaltsdifferenz unter Zugrundelegung des diskriminierungsfreien Vorrückungsstichtags hat, b)oder aber dahin, dass der Mitgliedstaat die Möglichkeit hat, durch eine diskriminierungsfreie Anrechnung der Vordienstzeiten die Altersdiskriminierung auch ohne finanziellen Ausgleich (durch Neufestsetzung des Vorrückungsstichtags bei gleichzeitiger Verlängerung des Vorrückungszeitraums) zu beseitigen, insbesondere wenn diese entgeltneutrale Lösung die Liquidität des Arbeitgebers aufrechterhalten sowie einen übermäßigen Neuberechnungsaufwand vermeiden soll?

**False Positives:**

- `BB-Personenverkehr AG` — partial — pred is substring of gold: `ÖBB-Personenverkehr AG`

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

**Example 69** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_62`)


… .“ b) Neue Rechtslage: § 53a des Bundesbahngesetzes, BGBl I 2011/129 lautet: „(1) Für jene Bediensteten und Ruhegenussempfänger, die bis zum 31. Dezember 2004 bei den Österreichischen Bundesbahnen (ÖBB), einem ihrer Rechtsvorgänger oder ab Rechtswirksamkeit der angeordneten Spaltungs- und Umwandlungsvorgänge bei der ÖBB-Holding AG, den im 3.

**False Positives:**

- `BB-Holding AG` — partial — pred is substring of gold: `ÖBB-Holding AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `ÖBB`(organisation)
- `ÖBB-Holding AG`(organisation)

**Example 70** (doc_id: `deanon_260716_TRAIN/8ObA60_19k`) (sent_id: `deanon_260716_TRAIN/8ObA60_19k_3`)


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

**Example 71** (doc_id: `deanon_260716_TRAIN/8ObA60_19k`) (sent_id: `deanon_260716_TRAIN/8ObA60_19k_18`)


Unstrittig hat die Beklagte ihr Angebot im Bereich Anlageberatung im Zusammenhang mit einer Novellierung des WAG auf eine nicht unabhängige Beratung umgestellt, worauf sogar auf der Homepage der Beklagten ausdrücklich hingewiesen wurde.

**False Positives:**

- `Novellierung des WAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_260716_TRAIN/8ObA60_19k`) (sent_id: `deanon_260716_TRAIN/8ObA60_19k_24`)


Gerade wenn die Revision darauf verweist, dass zu wesentlichen Fragen des WAG 2018 Judikatur noch nicht vorliegt, daher viele Fragen der Auslegung der entsprechenden Bestimmungen noch nicht geklärt sind, ist nicht ohne weiteres davon auszugehen, dass ein bestimmtes Verständnis dieser Bestimmungen seitens des Arbeitgebers zum Austritt berechtigt, mag es auch vom Arbeitnehmer nicht geteilt werden.

**False Positives:**

- `Fragen des WAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_260716_TRAIN/8ObA69_19h`) (sent_id: `deanon_260716_TRAIN/8ObA69_19h_3`)


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

**Example 74** (doc_id: `deanon_260716_TRAIN/8ObA71_14w`) (sent_id: `deanon_260716_TRAIN/8ObA71_14w_3`)


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

**Example 75** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_3`)


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

**Example 76** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_123`)


In einer weiteren Entscheidung in Zusammenhang mit Abschalteinrichtungen, der Rechtssache C-100/21,QBgegenMercedes-Benz Group AG, beantwortet der EuGH die an ihn gestellten Vorlagefragen wie folgt: „1. Art 18 Abs 1, Art 26 Abs 1 und Art 46 der Richtlinie 2007/46/EG in Verbindung mit Art 5 Abs 2 VO 715/2007/EG sind dahin auszulegen, dass sie neben allgemeinen Rechtsgütern die Einzelinteressen des individuellen Käufers eines Kraftfahrzeugs gegenüber dessen Hersteller schützen, wenn dieses Fahrzeug mit einer unzulässigen Abschalteinrichtung im Sinne von Art 5 Abs 2 dieser Verordnung ausgestattet ist.

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_125`)


In seiner Entscheidungsbegründung rekapituliert der EuGH zunächst, dass ein individueller Käufer, der ein Fahrzeug erwirbt, das zur Serie eines genehmigten Fahrzeugtyps gehört und somit mit einer Übereinstimmungsbescheinigung versehen ist, vernünftiger Weise erwarten kann, dass die VO 715/2007/EG und insbesondere deren Art 5 bei diesem Fahrzeug eingehalten werden (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 81 unter Hinweis auf C-145/20,Porsche Inter Auto und Volkswagen, Rn 54).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_127`)


[34] Konkret leitet der EuGH aus den Bestimmungen über die Übereinstimmungsbescheinigung (Art 18 Abs 1 und Art 26 Abs 1 der Rahmen-RL [RL 2007/46/EG des Europäischen Parlaments und des Rates vom 5. 9. 2007 zur Schaffung eines Rahmens für die Genehmigung von Kraftfahrzeugen und Kraftfahrzeuganhängern sowie von Systemen, Bauteilen und selbstständigen technischen Einheiten für diese Fahrzeuge; künftig: RL 2007/46/EG]) ab, dass die Übereinstimmungsbescheinigung „eine unmittelbare Verbindung zwischen dem Automobilhersteller und dem individuellen Käufer eines Kraftfahrzeugs herstellt, mit der diesem gewährleistet werden soll, dass das Fahrzeug mit den maßgeblichen Rechtsvorschriften der Union übereinstimmt“ (C-100/21,QBgegenMercedes-Benz Group AG, Rn 82).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_147`)


Für diesen Schadenersatzanspruch macht der EuGH grundsätzliche Vorgaben, nämlich in dem Sinn, dass die Mitgliedstaaten in einem solchen Fall einen Schadenersatzanspruch zu Gunsten eines Käufers gegenüber dem Hersteller vorzusehen haben, wenn dem Käufer durch diese Abschalteinrichtung ein Schaden entstanden ist (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 91).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_148`)


Dabei handelt es sich um einen im nationalen Recht wurzelnden Schadenersatzanspruch, der am unionsrechtlichen Effektivitätsgrundsatz zu messen ist (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 93), also eine wirksame, verhältnismäßige und abschreckende Sanktion für den Verstoß darstellen muss (vgl EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 90).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation
- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 81** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_149`)


Im Übrigen richten sich die Modalitäten dieses Schadenersatzanspruchs nach nationalem Recht (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 92), hier also unstrittig nach österreichischem Recht.

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_151`)


Eine unionsrechtliche Vorgabe eines Schadenersatzanspruchs ist das Vorliegen eines Schadens: Der EuGH betont, dass dem Käufer eines mit einer unzulässigen Abschalteinrichtung ausgestatteten Fahrzeugs ein Schadenersatzanspruch zusteht, wenn ihm ein Schaden entstanden ist (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 91).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_153`)


Als nachteilige Folge – vor der ein Fahrzeugkäufer durch das Unionsrecht geschützt werden soll – sieht der EuGH an, dass durch die Unzulässigkeit der Abschalteinrichtung die Gültigkeit der EG-Typengenehmigung und daran anschließend die der Übereinstimmungsbescheinigung in Frage gestellt werden, was wiederum (unter anderem) zu einer Unsicherheit über die Nutzungsmöglichkeit (Anmeldung, Verkauf oder Inbetriebnahme des Fahrzeugs) und „letztlich“ zu einem Schaden führen kann (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 84).

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_173`)


Ebenso wenig lässt die Feststellung erkennen, ob der Kläger die Notwendigkeit des Software-Updates und die vom EuGH angesprochene Unsicherheit über die Nutzungsmöglichkeit des Fahrzeugs (EuGH C-100/21,QBgegenMercedes-Benz Group AG, Rn 84; vgl zu dieser Unsicherheit auch die mit der Entscheidung des EuGH vom 8.

**False Positives:**

- `QBgegenMercedes-Benz Group AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_260716_TRAIN/9Ob6_24h`) (sent_id: `deanon_260716_TRAIN/9Ob6_24h_3`)


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

**Example 86** (doc_id: `deanon_260716_TRAIN/9ObA112_19i`) (sent_id: `deanon_260716_TRAIN/9ObA112_19i_16`)


Es führte aus, ein Recht des Klägers auf Beschäftigung lasse sich grundsätzlich aus § 18 Abs 1 TAG ableiten.

**False Positives:**

- `Abs 1 TAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 87** (doc_id: `deanon_260716_TRAIN/9ObA120_19s`) (sent_id: `deanon_260716_TRAIN/9ObA120_19s_36`)


Das Berufungsgericht ließ die Revision zu, weil zur Frage, ob ein ideeller Schadenersatz nach § 1328a ABGB gebühre, wenn die Einführung und Verwendung von Kontrollmaßnahmen und technischen Systemen, die die Menschenwürde berührten, ohne Einhaltung der Vorgaben des § 96 Abs 1 Z 3 ArbVG bzw des § 10 Abs 1 AVRAG erfolgt sei, noch keine oberstgerichtliche Rechtsprechung vorliege.

**False Positives:**

- `Abs 1 AVRAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_260716_TRAIN/9ObA120_19s`) (sent_id: `deanon_260716_TRAIN/9ObA120_19s_61`)


Korrespondierend dazu normiert § 10 Abs 1 AVRAG, dass die Einführung und Verwendung von Kontrollmaßnahmen und technischen Systemen, welche die Menschenwürde berühren, unzulässig ist, es sei denn, diese Maßnahmen werden durch eine Betriebsvereinbarung iSd § 96 Abs 1 Z 3 ArbVG geregelt oder erfolgen in Betrieben, in denen kein Betriebsrat eingerichtet ist, mit Zustimmung des Arbeitnehmers.

**False Positives:**

- `Abs 1 AVRAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `deanon_260716_TRAIN/9ObA120_19s`) (sent_id: `deanon_260716_TRAIN/9ObA120_19s_68`)


3.1.Bei Maßnahmen oder Systemen, die – wie hier – die objektive Eignung zur Kontrolle der Arbeitnehmer erfüllen, ist dann gemäß § 96 Abs 1 Z 3 ArbVG bzw § 10 Abs 1 AVRAG weiters zu prüfen, ob dadurch die Menschenwürde berührt ist.

**False Positives:**

- `Abs 1 AVRAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 90** (doc_id: `deanon_260716_TRAIN/9ObA124_19d`) (sent_id: `deanon_260716_TRAIN/9ObA124_19d_6`)


Rechtliche Beurteilung 1.1 Soll der Arbeitnehmer iSd § 2d Abs 2 erster Satz AVRAG zum Rückersatz von Ausbildungskosten verpflichtet werden, muss nach ständiger Rechtsprechung darüber noch vor einer bestimmten Ausbildung eine schriftliche Vereinbarung geschlossen werden, aus der auch die konkrete Höhe der zu ersetzenden Ausbildungskosten hervorgeht (RS0127499).

**False Positives:**

- `Abs 2 erster Satz AVRAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `GenericFirma` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `03c11cff`  
**Description:**
Matches 'Firma' followed by a capitalized name that doesn't end in GmbH/m.b.H. (catching incomplete mentions or specific cases).

**Content:**
```
\bFirma\s+([A-Z][a-zA-Z0-9\s]+?)(?=\s*(?:in|mit|auf|der|die|das|ist|hat|ist|wurde|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `TaxAuthorities` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a24298d5`  
**Description:**
Matches Finanzamt variations, strictly requiring a location suffix or specific known names to avoid matching genitive forms like 'Finanzamtes' alone or trailing lists.

**Content:**
```
\bFinanz(?:amt(?:es)?(?:\s+(?:Braunau\sRied|Österreich|Waldviertel|Salzburg-Stadt|Neunkirchen\sWr\.\sNeustadt|Kirchdorf\sPerg\sSteyr|Wien\s1/23|Bregenz|St\.\sJohann\sTamsweg\sZell\sam\sSee|Baden\sMödling|Graz-Umgebung|Salzburg-Land|Wien\s2/20/21/22|Innsbruck|Österreich/FAÖ|für\sGroßbetriebe|Bruck\sEisenstadt\sOberwart|Hollabrunn\sKorneuburg\sTulln|Gebühren|Verkehrsteuern\sund\sGlücksspiel|Graz-Stadt|Steiermark\sMitte|Grieskirchen\sWels|Eisenstadt|Wien\s12/13/14\sPurkersdorf))?)\b
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

## `CompanyGmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `725ae3f8`  
**Description:**
Matches specific known company names including 'Fa.' prefix and en-dashes, ensuring exact matches without preceding context.

**Content:**
```
\b(?:Fa\.)?(?:Snajdr\sE[\u2011\-]Commerce|Glanzder\-Automotive|Jackobi\sund\sHorbank\sKI)\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `MinistryAbbreviations` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3eb2075a`  
**Description:**
Matches Bundesministeriums für Finanzen and its abbreviations BMF, BM für Finanzen.

**Content:**
```
\b(?:Bundesministeriums\sfür\sFinanzen|BMF|BM\sfür\sFinanzen)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `KAG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3856d842`  
**Description:**
Matches the specific abbreviation KAG which appears frequently in the text as an organization.

**Content:**
```
\bKAG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BFH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5d06e25b`  
**Description:**
Matches the German Federal Fiscal Court abbreviation BFH.

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

## `PoliceAuthorities` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7652b5fe`  
**Description:**
Matches 'Landespolizeidirektion' and similar police authority names, strictly bounded to prevent capturing trailing words.

**Content:**
```
\bLandespolizeidirektion(?:\s+(?:Wien))?\b
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

- `Landespolizeidirektion` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `AMS` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8df62c8b`  
**Description:**
Matches the abbreviation AMS (Arbeitsmarktservice) as an organization.

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

## `Landesgericht` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e3c4aa61`  
**Description:**
Matches Land Courts (Landesgericht) and its genitive form.

**Content:**
```
\bLandesgericht(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 31 | 0 | 31 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 31 | 3696 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der zur AZ 38 Nc 13/08i beim Landesgericht für Zivilrechtssachen Wien anhängigen Ablehnungssache des Ablehnungswerbers Mag. Herwig Bortzlaff, über den Rekurs des Ablehnungswerbers gegen den Beschluss des Oberlandesgerichts Wien vom 10. November 2009, GZ 13 Nc 14/09x-2, womit ein Ablehnungsantrag zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

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

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_12`)


Da mehrere Senate des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht an dem genannten Verhalten beteiligt gewesen seien, sei auch das gesamte Landesgericht für Zivilrechtssachen Wien als befangen anzusehen, über den nunmehr geltend gemachten Unterhaltsanspruch zu entscheiden.

**False Positives:**

- `Landesgericht` — similar text (different position): `Landesgerichts für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_4`)


Text Gründe: Im Ermittlungsverfahren gegen Viktor Meisterernst und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und 3 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 703 St 3/11t (nunmehr AZ 713 St 24/18i) der Staatsanwaltschaft Wien, stellte der Beschuldigte Dr. Stefan Tydeck mit Schriftsatz vom 29. November 2017 – soweit im Folgenden von Relevanz – den Antrag auf Einstellung des Ermittlungsverfahrens „gemäß § 108 StPO“ (ON 558), welchen das Landesgericht für Strafsachen Wien mit Beschluss vom 22. Juni 2018, AZ 352 HR 214/11x, abwies (ON 644).

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Viktor Meisterernst`(person)
- `Dr. Stefan Tydeck`(person)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_22`)


1./ Gemäß § 357 Abs 2 erster Satz StPO hat das Landesgericht den Antrag auf Wiederaufnahme des Strafverfahrens dem Gegner des Antragstellers mit der Belehrung zuzustellen, dass er seine Gegenäußerung binnen 14 Tagen überreichen könne.

**False Positives:**

- `Landesgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_260716_TRAIN/13Os22_12b_13Ns16_12z_`) (sent_id: `deanon_260716_TRAIN/13Os22_12b_13Ns16_12z__4`)


Text Gründe: Das Landesgericht für Strafsachen Wien verhängte mit Beschluss vom 9. Dezember 2011 über Mag. Türkan Kirstin Bierwolf die Untersuchungshaft aus den Gründen der Tatbegehungsgefahr nach § 173 Abs 2 Z 3 lit b und lit d StPO (ON 12).

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Wien`(organisation)
- `Kirstin Bierwolf`(person)

**Example 6** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__6`)


Dem Landesgericht für Strafsachen Graz wird ein Vorgehen gemäß §§ 14 und 15 dieser Verordnung aufgetragen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Graz`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__23`)


Seither besteht das Landesgericht als Schöffengericht aus nur einem (Berufs-)Richter und zwei Schöffen (§ 32 Abs 1 dritter Satz StPO).

**False Positives:**

- `Landesgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__28`)


8. Das Landesgericht für Strafsachen Graz hätte demnach die Staatsanwaltschaft und den Angeklagten von der dauernden Verhinderung des Vorsitzenden des Schöffengerichts in Kenntnis setzen und vor Betrauung eines anderen Richters mit der Urteilsausfertigung nach ihrem Einverständnis fragen müssen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Graz`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__30`)


Mit Blick auf § 292 letzter Satz StPO sah sich der Oberste Gerichtshof veranlasst, dem Landesgericht für Strafsachen Graz aufzutragen, gemäß §§ 14 und 15 der Kaiserlichen Verordnung vorzugehen.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Landesgericht für Strafsachen Graz`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/13Os34_19b`) (sent_id: `deanon_260716_TRAIN/13Os34_19b_5`)


Dieser Beschluss wird aufgehoben und es wird dem Landesgericht für Strafsachen Graz aufgetragen, im Verfahren AZ 16 Hv 32/15a über den Widerruf zu entscheiden.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Graz`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_14`)


Die Sanktionsrüge (Z 11 zweiter Fall) wendet sich gegen die als nach § 33 Abs 1 Z 2 StGB strafschärfend gewertete Verurteilung des Angeklagten durch das Landesgericht für Strafsachen Wien vom 16. Februar 2012, AZ 62 Hv 10/12m, (ua) wegen Vergehen des unerlaubten Umgangs mit Suchtmitteln (US 4, 9; ON 97).

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Wien`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__5`)


In Stattgebung des Antrags der Generalprokuratur wird im außerordentlichen Weg die Wiederaufnahme des Berufungsverfahrens verfügt, der Beschluss des Landesgerichts für Strafsachen Wien vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), aufgehoben und die Sache zur neuerlichen Entscheidung über die Berufung des Angeklagten gegen das Urteil des Bezirksgerichts Innere Stadt Wien vom 27. November 2018 (ON 19 der U-Akten) an das Landesgericht für Strafsachen Wien verwiesen.

**False Positives:**

- `Landesgericht` — similar text (different position): `Landesgerichts für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Strafsachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__9`)


Die am 22. Februar 2019 – innerhalb der Frist des § 467 Abs 1 StPO (vgl Zustellnachweis an ON 19) – ausgeführte Berufung des Robert Unterdörfer (ON 21) wies das Landesgericht für Strafsachen Wien als Berufungsgericht mit Beschluss vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23), gemäß § 470 Z 1 StPO als unzulässig zurück, weil die am 27. November 2018 zur Post gegebene Rechtsmittelanmeldung gegen das am 23. November 2018 verkündete Urteil verspätet gewesen sei.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Robert Unterdörfer`(person)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/13Os99_19m`) (sent_id: `deanon_260716_TRAIN/13Os99_19m_7`)


Die gegen diesen Ausspruch gerichtete Berufung des Privatbeteiligten (ON 23) wies das Oberlandesgericht Graz mit dem nunmehr angefochtenen Beschluss im Wesentlichen mit der Begründung zurück, auch im Verfahren vor dem Landesgericht als Einzelrichter stehe dem Privatbeteiligten die Berufung nur bei vollständiger Verweisung mit seinen Ansprüchen auf den Zivilrechtsweg (trotz Verurteilung) offen, während die Höhe des Zuspruchs nicht bekämpfbar sei (vgl zum kollegialgerichtlichen Verfahren § 283 Abs 4 iVm § 366 Abs 3 StPO).

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgericht Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgericht Graz`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/13Os99_19m`) (sent_id: `deanon_260716_TRAIN/13Os99_19m_11`)


Diese Regelung findet zufolge § 489 Abs 1 StPO auch im Verfahren vor dem Landesgericht als Einzelrichter Anwendung.

**False Positives:**

- `Landesgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_260716_TRAIN/14Ns5_20a`) (sent_id: `deanon_260716_TRAIN/14Ns5_20a_5`)


Die Akten werden dem Oberlandesgericht Wien zurückgestellt. Gründe:  Rechtliche Beurteilung Der Wohnsitz des Angeklagten und Antragsgegners im Sprengel eines anderen Gerichts (ON 16 iVm ON 15 und ON 1 S 4 und 6) ist ebensowenig ein wichtiger Grund im Sinn des § 39 Abs 1 StPO wie der Umstand, dass sich der – von der Mindestsicherung lebende – Angeklagte die Kosten für die Anreise zum Landesgericht für Strafsachen Wien ersparen würde (RIS-Justiz RS0129146;

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgericht Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgericht Wien`(organisation)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/14Os132_10h`) (sent_id: `deanon_260716_TRAIN/14Os132_10h_4`)


Text Gründe: Gegen Tomsilav Ayik ist beim Landesgericht für Strafsachen Wien ein - im Stadium der Hauptverhandlung befindliches - Verfahren wegen der Verbrechen des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und nach § 28a Abs 1 fünfter Fall, Abs 4 Z 3 SMG anhängig, in dem sich der Angeklagte seit 5. April 2010 in Untersuchungshaft befindet (ON 20).

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ayik`(person)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/15Os110_17s`) (sent_id: `deanon_260716_TRAIN/15Os110_17s_10`)


Aus Anlass eines vom Angeklagten am 17. Februar 2017 eingebrachten Antrags auf Aufhebung der Untersuchungshaft (ON 95) setzte das Landesgericht für Strafsachen Graz mit Beschluss vom 23. Februar 2017 die am 7. September 2016 verhängte (ON 11) – und danach wiederholt prolongierte (ON 32, 71) – Untersuchungshaft aus den Haftgründen der Flucht- und der Tatbegehungsgefahr nach § 173 Abs 2 Z 1 und Z 3 lit a StPO fort (ON 100).

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Graz`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/15Os43_13g`) (sent_id: `deanon_260716_TRAIN/15Os43_13g_11`)


Rechtliche Beurteilung Das Urteil des Landesgerichts Korneuburg vom 13. Juni 2012, GZ 505 Hv 5/11x-69, steht - wie die Generalprokuratur in ihrer Nichtigkeitsbeschwerde zur Wahrung des Gesetzes zutreffend ausführt - in seinem Punkt A./2./ mit dem Gesetz nicht im Einklang: Gemäß der auch für das Verfahren vor dem Landesgericht als Einzelrichter geltenden (§ 488 Abs 1 StPO) Bestimmung des § 270 Abs 4 StPO hat eine - unter den in dieser Vorschrift genannten, hier vorliegenden Voraussetzungen zulässigerweise - gekürzte Urteilsaus- fertigung die in § 270 Abs 2 StPO angeführten Angaben mit Ausnahme der Entscheidungsgründe, also auch die in § 260 StPO (§ 270 Abs 4 Z 1 StPO) genannten Punkte zu enthalten.

**False Positives:**

- `Landesgericht` — similar text (different position): `Landesgerichts Korneuburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Korneuburg`(organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__57`)


Das Landesgericht für Strafsachen Wien und das Oberlandesgericht Wien als Berufungsgericht haben somit die (grundsätzliche) Verwirklichung des Entschädigungsanspruchs nach § 6 Abs 1 MedienG in Bezug auf die am 4. Juni 2017 auf dem Facebook-Account von www.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Strafsachen Wien`(organisation)
- `Oberlandesgericht Wien`(organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_5`)


Text Gründe: In der Medienrechtssache der Antragsteller Dr. Wieland Skocdopole und Priv.-Doz.in Heidrun Aguera, BA MSc gegen die Antragsgegnerin Wald Fenkraftal GmbH & Co KG wegen §§ 7 f MedienG brachten die Antragsteller beim Landesgericht für Strafsachen Wien gesondert, jeweils in einem eigenen Schriftsatz aber vertreten durch dieselbe Rechtsanwältin selbständige Entschädigungsanträge gegen die Antragsgegnerin ein.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Strafsachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Wieland Skocdopole`(person)
- `Priv.-Doz.in Heidrun Aguera, BA MSc`(person)
- `Wald Fenkraftal GmbH & Co KG`(organisation)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/15Os97_10v`) (sent_id: `deanon_260716_TRAIN/15Os97_10v_4`)


Im Verfahren AZ 7 U 49/08s des Bezirksgerichts Innsbruck verletzt der Vorgang, dass es das Gericht unterließ, von seinem gemeinsam mit dem Urteil vom 4. August 2009 (unter Absehen vom Widerruf der Andreas Garthoff im Verfahren AZ 23 BE 29/06a des Landesgerichts Innsbruck gemäß § 46 Abs 2 StGB gewährten bedingten Entlassung) gefassten Beschluss auf Verlängerung der Probezeit unverzüglich dieses Landesgericht als Vollzugsgericht zu verständigen, § 494a Abs 7 StPO.

**False Positives:**

- `Landesgericht` — similar text (different position): `Landesgerichts Innsbruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Innsbruck`(organisation)
- `Andreas Garthoff`(person)
- `Landesgerichts Innsbruck`(organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/1Nc71_10x`) (sent_id: `deanon_260716_TRAIN/1Nc71_10x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Dr. Grohmann als weitere Richter in der beim Landesgericht für Zivilrechtssachen Wien zu AZ 33 Cg 21/10s anhängigen Rechtssache der klagenden Partei Bachkraft Gesellschaft mbH, Salmweg 829, 4891 Schachen, Österreich, vertreten durch Dr. Gerhard Kornek, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 53.176,92 EUR sA, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

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

**Example 24** (doc_id: `deanon_260716_TRAIN/1Nc71_10x`) (sent_id: `deanon_260716_TRAIN/1Nc71_10x_8`)


Das Landesgericht für Zivilrechtssachen Wien legte die Akten dem Obersten Gerichtshof gemäß § 9 Abs 4 AHG vor.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)
- `Obersten Gerichtshof`(organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/1Nc71_10x`) (sent_id: `deanon_260716_TRAIN/1Nc71_10x_10`)


Da dieser Tatbestand einer notwendigen und der Parteiendisposition entzogenen (1 Nc 24/09h) Delegierung im vorliegenden Fall erfüllt ist, ist ein Landesgericht außerhalb des Sprengels des Oberlandesgerichts Wien als zuständig zu bestimmen.

**False Positives:**

- `Landesgericht` — similar text (different position): `Oberlandesgerichts Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgerichts Wien`(organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/1Ob78_22k`) (sent_id: `deanon_260716_TRAIN/1Ob78_22k_8`)


Das Landesgericht für Zivilrechtssachen Wien gab der gegen das Ersturteil gerichteten Berufung des Beklagten mit dem (dessen Verfahrenshelfer am 17.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/1Ob78_22k`) (sent_id: `deanon_260716_TRAIN/1Ob78_22k_11`)


diese Entscheidung wurde vom Landesgericht für Zivilrechtssachen Wien später bestätigt.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/4Fsc1_10z`) (sent_id: `deanon_260716_TRAIN/4Fsc1_10z_5`)


Diesen Ablehnungsantrag hat das Landesgericht für Zivilrechtssachen Wien am 19.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/4Fsc1_10z`) (sent_id: `deanon_260716_TRAIN/4Fsc1_10z_11`)


9. 2009 hat das Landesgericht für Zivilrechtssachen Wien am 12.

**False Positives:**

- `Landesgericht` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/4Nc30_22g`) (sent_id: `deanon_260716_TRAIN/4Nc30_22g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Kodek als Vorsitzenden sowie die Hofräte Dr. Schwarzenbacher und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Iris Gscheider, vertreten durch Dr. Sabine C.M. Deutsch, Rechtsanwältin in Riegersburg, gegen die beklagte Partei Mag. Annette Salzbauer, als Masseverwalter im Konkursverfahren über das Vermögen von Lynn Galleitner (AZ 26 S 10/21x des Landesgerichts für Zivilrechtssachen Graz), vertreten durch die GRAF ISOLA Rechtsanwälte GmbH in Graz, wegen Unterlassung, über den Delegierungsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der unmittelbar beim Obersten Gerichtshof eingebrachte Delegierungsantrag samt Beilagen wird dem Landesgericht für Zivilrechtssachen Graz als Erstgericht zu AZ 10 Cg 83/22z zur geschäftsordnungsgemäßen Behandlung übermittelt. Begründung:  Rechtliche Beurteilung [1]

**False Positives:**

- `Landesgericht` — similar text (different position): `Landesgerichts für Zivilrechtssachen Graz`

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

## `ÖGK` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8e381a0a`  
**Description:**
Matches the specific abbreviation ÖGK (Österreichische Gesundheitskasse) as an organization.

**Content:**
```
\bÖGK\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `TaxAuthorityFA` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b23075c0`  
**Description:**
Matches 'FA' followed by a location, ensuring the match stops before common prepositions or end of sentence to avoid capturing 'vom' or other trailing words.

**Content:**
```
\bFA\s+([A-Z][a-zA-Z\s]+?)(?=\s+(?:vom|am|des|der|in|an|bei|mit|nach|vor|über|unter|auf|zu|von|für|gegen|ohne|durch|seit|bis|um|an|bei|mit|nach|vor|über|unter|auf|zu|von|für|gegen|ohne|durch|seit|bis|um|\.|,|\)|\]|\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `UniversityWien` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `67e7c8f3`  
**Description:**
Matches 'Universität Wien' which was previously missing.

**Content:**
```
\bUniversit\u00e4t\sWien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `MinistryBMI` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `393052ea`  
**Description:**
Matches 'BMI' (Bundesministerium für Inneres) as an organization.

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

## `Pensionsversicherungsanstalt` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `87469955`  
**Description:**
Matches the specific organization 'Pensionsversicherungsanstalt' which was missing.

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

## `SKTelecom` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `99ac9790`  
**Description:**
Matches 'SK Telecom' variations which appear frequently in legal texts regarding EU court cases.

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

## `WienerGemeinderat` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `965ee445`  
**Description:**
Matches 'Wiener Gemeinderat' and 'Wiener Gemeinderates' variations.

**Content:**
```
\bWiener\s+Gemeinderat(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BundesamtSoziales` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c51d21bb`  
**Description:**
Matches 'Bundesamt für Soziales und Behindertenwesen'.

**Content:**
```
\bBundesamt\s+für\s+Soziales\s+und\s+Behindertenwesen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `PostAG` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8d797d70`  
**Description:**
Matches 'Post AG' specifically to capture this common organization which was previously missed.

**Content:**
```
\bPost\s+AG\b
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

