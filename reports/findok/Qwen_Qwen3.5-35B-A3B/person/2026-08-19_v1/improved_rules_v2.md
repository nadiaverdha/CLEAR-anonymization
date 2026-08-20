# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-08-20T12:08:42.280200

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-08-19_v1/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 0 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 4042 |
| Validation documents | 1012 |
| Test documents | 477 |
| Train sentences | 7729 |
| Validation sentences | 2120 |
| Test sentences | 22727 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 30 |
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
| Accuracy (exact match) | 90.2% |
| True Positives | 3192 |
| False Positives | 3507 |
| False Negatives | 983 |
| Total Gold Entities | 4175 |
| Micro Precision | 47.6% |
| Micro Recall | 76.5% |
| Micro F1 | 58.7% |
| Macro F1 | 58.7% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Angeklagten Name` | 0.6% | 100.0% | 0.3% | 13 | 13 | 0 |
| `Title Name Full` | 0.0% | 100.0% | 0.0% | 1 | 1 | 0 |
| `Betroffenen Name` | 0.0% | 100.0% | 0.0% | 1 | 1 | 0 |
| `Name After Verb Subject` | 0.1% | 100.0% | 0.1% | 3 | 3 | 0 |
| `Mag Dr Title` | 4.6% | 97.1% | 2.4% | 102 | 99 | 3 |
| `Hyphenated Surname` | 73.9% | 94.3% | 60.8% | 2692 | 2539 | 153 |
| `Complex Title` | 14.9% | 94.1% | 8.1% | 358 | 337 | 21 |
| `MedR Title Pattern` | 0.3% | 85.7% | 0.1% | 7 | 6 | 1 |
| `Zeugen Name` | 0.5% | 76.9% | 0.2% | 13 | 10 | 3 |
| `KommR Title Pattern` | 0.1% | 66.7% | 0.0% | 3 | 2 | 1 |
| `Dr Name Initial` | 0.0% | 33.3% | 0.0% | 3 | 1 | 2 |
| `Mag.a Name` | 0.0% | 25.0% | 0.0% | 4 | 1 | 3 |
| `Standalone Name Legal Context` | 5.6% | 15.1% | 3.5% | 963 | 145 | 818 |
| `Dr Name Full` | 0.1% | 8.3% | 0.1% | 36 | 3 | 33 |
| `Role Title Name Full` | 0.0% | 7.1% | 0.0% | 14 | 1 | 13 |
| `Role Name Context` | 0.9% | 1.2% | 0.7% | 2434 | 30 | 2404 |
| `Complaint Case Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Deceased Person Context` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Dr Name List` | 0.0% | 0.0% | 0.0% | 24 | 0 | 24 |
| `Prof Dr Name List` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Ing Name List` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mag Dr Name List` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Dr Name Standalone` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Role Name Full` | 0.0% | 0.0% | 0.0% | 9 | 0 | 9 |
| `Name with Degree` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mag Name Full` | 0.0% | 0.0% | 0.0% | 6 | 0 | 6 |
| `Legal Role Context` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Genitive Person Name` | 0.0% | 0.0% | 0.0% | 9 | 0 | 9 |
| `Mimi Jueterbock Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Istvan Krautkrämer Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Angeklagten Name` 🏆

**F1:** 0.006 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `11b3e8c4`  
**Description:**
Matches names following 'Angeklagten' (defendant), ensuring only the name is captured, not the role.

**Content:**
```
Angeklagten\s+(?:(?:Dr\.|Mag\.|Hon\.-Prof\.|Univ\.-Prof\.|Priv\.-Doz\.|Prof\.|MMag\.|KR\.|OStR\.|StR\.|AR\.|Ing\.|DI\.|PhD\.|Dipl\.-Ing\.|Bakk\. iur\.|MBA|BSc|LL\.M\.|RgR|\u00d6kR|StR|OStR|KR|AR|VetR|PD|Mag\.a)\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.006 | 13 | 13 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 13 | 0 | 3688 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_16`)


So unterließ das Erstgericht die gebotene Auseinandersetzung (Z 5 zweiter Fall) mit den - dem konstatierten Vertrauen auf den Erhalt eines rennfertigen Fahrzeugs entgegenstehenden - Angaben des Angeklagten Warmund, wonach dieser bei einer zwei Tage vor Vertragsabschluss stattgefundenen Besichtigung festgestellt habe, dass der Rennwagen in einem „katastrophalen Zustand“ gewesen sei und „Unsummen investiert“ werden müssten, um diesen „überhaupt einsetzbar“ zu machen (ON 42 S 12 f).

| Predicted | Gold |
|---|---|
| `Warmund` | `Warmund` |

**Example 1** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_4`)


2005 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab und Hofrätin des Obersten Gerichtshofs Mag. Michel sind von der Entscheidung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Gerhard Boesl betreffend das Verfahren AZ 16 Hv20/14x des Landesgerichts für Strafsachen Wien ausgeschlossen.

| Predicted | Gold |
|---|---|
| `Gerhard Boesl` | `Gerhard Boesl` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Michel` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_6`)


Gründe:  Rechtliche Beurteilung Der Oberste Gerichtshof hat zu AZ 11 Os 5/15t über die gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 14. Oktober 2014, GZ 16 Hv 20/14x-3462, ergriffene Nichtigkeitsbeschwerde und Berufung des Angeklagten Gerhard Bugnenings zu entscheiden.

| Predicted | Gold |
|---|---|
| `Gerhard Bugnenings` | `Gerhard Bugnenings` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_19`)


Gegenständlich aber hatte das Oberlandesgericht Wien im ersten Rechtsgang die Tatfrage im Rahmen der Strafberufung des Angeklagten Thomas Marczynkowski entgegen der Ausführungen im angefochtenen Beschluss weder „in voller Kognitionsbefugnis“ zu beurteilen, noch bezog es in den Entscheidungsgründen hiezu beweiswürdigend Stellung.

| Predicted | Gold |
|---|---|
| `Thomas Marczynkowski` | `Thomas Marczynkowski` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_6`)


Text Gründe: In der Jugendstrafsache AZ 51 Hv 32/13i des Landesgerichts Feldkirch legte die Staatsanwaltschaft Feldkirch mit Strafantrag vom 18. April 2013, AZ 9 St 82/13f, dem am 23. August 1996 geborenen Angeklagten Johannes Bednorz als Vergehen der fortgesetzten Gewaltausübung nach § 107b Abs 1 und Abs 2 StGB (I./) sowie der Nötigung nach den §§ 15 Abs 1, 105 Abs 1 StGB (II./, III./1./), der gefährlichen Drohung nach § 107 Abs 1 StGB (III./2./) und der Sachbeschädigung nach § 125 StGB (III./3./) qualifiziertes Verhalten zum Nachteil der Sabrina Hemmersdorfer zur Last (ON 3).

| Predicted | Gold |
|---|---|
| `Johannes Bednorz` | `Johannes Bednorz` |

**Missed by this rule (FN):**

- `Landesgerichts Feldkirch` (organisation)
- `Sabrina Hemmersdorfer` (person)

**Example 5** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_11`)


Hierauf beantragte die Staatsanwaltschaft Feldkirch in dem Johannes Bergknecht betreffenden Verfahren AZ 51 Hv 32/13i des Landesgerichts Feldkirch am 12. März 2014 gemäß § 355 StPO iVm § 352 Abs 1 Z 1 StPO die Wiederaufnahme des Strafverfahrens im Umfang des am 5. Juni 2013 ergangenen Freispruchs des Angeklagten Johannes Bertrang, weil dieser durch die falsche Beweisaussage der Zeugin Sabrina Holzschuher herbeigeführt worden sei (ON 29).

| Predicted | Gold |
|---|---|
| `Johannes Bertrang` | `Johannes Bertrang` |

**Missed by this rule (FN):**

- `Johannes Bergknecht` (person)
- `Landesgerichts Feldkirch` (organisation)
- `Sabrina Holzschuher` (person)

**Example 6** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_19`)


Am 17. Oktober 2014 langte beim Landesgericht Feldkirch zu AZ 51 Hv 32/13i eine vom Verfahrenshilfeverteidiger im Verfahren AZ 39 Hv 64/14h dieses Landesgerichts verfasste Beschwerde des Angeklagten Johannes Bartlmäß (ON 42 im Akt AZ 51 Hv 32/13i des Landesgerichts Feldkirch) gegen den Beschluss des Landesgerichts Feldkirch vom 4. Mai 2014 auf Wiederaufnahme des Strafverfahrens ein.

| Predicted | Gold |
|---|---|
| `Johannes Bartlmäß` | `Johannes Bartlmäß` |

**Missed by this rule (FN):**

- `Landesgericht Feldkirch` (organisation)
- `Landesgerichts Feldkirch` (organisation)
- `Landesgerichts Feldkirch` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/14Os108_18s`) (sent_id: `deanon_260716_TRAIN/14Os108_18s_3`)


Kopf Der Oberste Gerichtshof hat am 13. November 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Kontrollorin Gsellmann als Schriftführerin in der Strafsache gegen Misha Riffart und andere Angeklagte wegen des Verbrechens des im Rahmen einer kriminellen Vereinigung gewerbsmäßig schweren und durch Einbruch begangenen Diebstahls nach §§ 127, 129 Abs 1 Z 2, Abs 2 Z 1, 130 Abs 2 und 3, jeweils iVm Abs 1 zweiter Fall, § 15 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Valeri Kunkelmann gegen das Urteil des Landesgerichts St. Pölten als Schöffengericht vom 28. Juni 2018, GZ 39 Hv 37/18x-157, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Valeri Kunkelmann` | `Valeri Kunkelmann` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Danek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Hetlinger` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Mann` (person)
- `Misha Riffart` (person)
- `Landesgerichts St. Pölten` (organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/14Os108_18s`) (sent_id: `deanon_260716_TRAIN/14Os108_18s_5`)


Dem Angeklagten Köhnecke fallen auch die Kosten des bisherigen Rechtsmittelverfahrens zur Last.

| Predicted | Gold |
|---|---|
| `Köhnecke` | `Köhnecke` |

**Example 9** (doc_id: `deanon_260716_TRAIN/14Os108_18s`) (sent_id: `deanon_260716_TRAIN/14Os108_18s_9`)


Rechtliche Beurteilung Der dagegen aus Z 5 und 10 des § 281 Abs 1 StPO ergriffenen Nichtigkeitsbeschwerde des Angeklagten Kretschmer kommt keine Berechtigung zu. Entgegen dem zu beiden Schuldspruchpunkten erhobenen Einwand der Mängelrüge liegt Unvollständigkeit (Z 5 zweiter Fall) zufolge Unterbleibens einer Erörterung der Verantwortungen der jeweils beteiligten Angeklagten nicht vor.

| Predicted | Gold |
|---|---|
| `Kretschmer` | `Kretschmer` |

**Example 10** (doc_id: `deanon_260716_TRAIN/14Os108_18s`) (sent_id: `deanon_260716_TRAIN/14Os108_18s_11`)


Die Gründe für ihre Überzeugung von seiner Täterschaft sowie einem einverständlichen Zusammenwirken von ihm und den Angeklagten Tumele und Mag. Helge Pankrat beim Einbruchsdiebstahl vom 30. Jänner 2018 wurden im Urteil dargelegt, womit die Tatrichter – wie die Beschwerde ohnehin einräumt – inhaltlich auch zum Ausdruck brachten, die leugnende Einlassung der beiden Letztgenannten durch die angeführten Beweisergebnisse für widerlegt erachtet zu haben.

| Predicted | Gold |
|---|---|
| `Tumele` | `Tumele` |

**Missed by this rule (FN):**

- `Mag. Helge Pankrat` (person)

**Example 11** (doc_id: `deanon_260716_TRAIN/14Os108_18s`) (sent_id: `deanon_260716_TRAIN/14Os108_18s_13`)


Zu I/E wurden die Depositionen der Angeklagten Reichenbach und Corinna Pumpenmeier ausdrücklich berücksichtigt und (unter vorangegangener Bezugnahme auf eine Reihe von Verfahrensergebnissen) ebenso als unglaubwürdig beurteilt wie die Behauptung des Beschwerdeführers und des Angeklagten Ruzicka, einander nicht zu kennen (US 15 f).

| Predicted | Gold |
|---|---|
| `Ruzicka` | `Ruzicka` |

**Missed by this rule (FN):**

- `Reichenbach` (person)
- `Corinna Pumpenmeier` (person)

**Example 12** (doc_id: `deanon_260716_TRAIN/14Os108_18s`) (sent_id: `deanon_260716_TRAIN/14Os108_18s_15`)


Dies gilt umso mehr für die Einlassung des Angeklagten Kandlbinder selbst, weil dieser von seinem Recht zu schweigen Gebrauch machte und sich zum eigentlichen Anklagevorwurf auf die Aussage beschränkte, nicht geständig zu sein (ON 156 S 42 f).

| Predicted | Gold |
|---|---|
| `Kandlbinder` | `Kandlbinder` |

</details>

---

## `Title Name Full` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `50468778`  
**Description:**
Matches complex titles (Mag., Dr., Prof., etc.) followed by full names, ensuring the entire name string is captured.

**Content:**
```
(?:Hon\.-Prof\.|Univ\.-Prof\.|Priv\.-Doz\.|PD|MMag\.|Bakk\. iur\.|Bakk\. phil\.|Dipl\. Kfm\.|Dipl\. Ing\.|Ing\. Mag\.|OStR\.|HR\.|StR\.|KR\.|AR\.|VetR\.|RgR|\u00d6kR|OMedR|DI\.|Ing\.|PhD|LL\.M\.|LLB|BSc|MBA|BEd|MedR|DDr\.)\s+(?:Dr\.)?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 0 | 1289 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/6Ob177_10p`) (sent_id: `deanon_260716_TRAIN/6Ob177_10p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Pimmer als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Dr. Schramm, Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Edgar Hoffschroer, BA, vertreten durch Dr. Karl Maier Rechtsanwaltsgesellschaft mbH in Knittelfeld, gegen die beklagte Partei Esra Kunhardt, vertreten durch Ing. Mag. Dr. Felix Jurak, Rechtsanwalt in Klagenfurt, und ihres Nebenintervenienten DI Paul Domgörgen, vertreten durch Frimmel/Anetter Rechtsanwaltsgesellschaft mbH in Klagenfurt, wegen 15.644,98 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 29. April 2010, GZ 4 R 15/10y-73, womit das Urteil des Landesgerichts Klagenfurt vom 27. Oktober 2009, GZ 20 Cg 183/06y-66, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ing. Mag. Dr. Felix Jurak` | `Ing. Mag. Dr. Felix Jurak` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Pimmer` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schramm` (person)
- `Dr. Gitschthaler` (person)
- `Univ.-Prof. Dr. Kodek` (person)
- `Dr. Nowotny` (person)
- `Edgar Hoffschroer, BA` (person)
- `Dr. Karl` (person)
- `Esra Kunhardt` (person)
- `DI Paul Domgörgen` (person)
- `Frimmel/Anetter Rechtsanwaltsgesellschaft mbH` (organisation)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts Klagenfurt` (organisation)

</details>

---

## `Betroffenen Name` 

**F1:** 0.000 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f1108b30`  
**Description:**
Matches names following 'Betroffenen' (concerned party), handling titles and hyphenated names.

**Content:**
```
Betroffenen\s+(?:(?:Dr\.|Mag\.|Hon\.-Prof\.|Univ.-Prof\.|Priv.-Doz\.|Prof\.|MMag\.|KR\.|OStR\.|StR\.|AR\.|Ing\.|DI\.|PhD\.|Dipl.-Ing\.|Bakk\. iur\.|MBA|BSc|LL\.M\.|RgR|\u00d6kR|StR|OStR|KR|AR|VetR|PD|Mag\.a)\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.000 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 0 | 1253 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/6Ob199_10y`) (sent_id: `deanon_260716_TRAIN/6Ob199_10y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Pimmer als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Dr. Schramm, Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny als weitere Richter in der Sachwalterschaftssache des Betroffenen Jaromir Hägerich, geboren am 17. August 1962, über den Revisionsrekurs des Betroffenen, vertreten durch Dr. Alexander Sporn, Rechtsanwalt in Wien, als Verfahrenshelfer, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 11. Dezember 2009, GZ 42 R 363/09g, 42 R 364/09d und 42 R 365/09a-240, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt. Begründung:  Rechtliche Beurteilung Nach § 62 Abs 3 AußStrG ist der ordentliche Revisionsrekurs - außer im Fall der nachträglichen Zulassungserklärung - jedenfalls unzulässig, wenn - wie im vorliegenden Fall - der Entscheidungsgegenstand an Geld oder Geldeswert 30.000 EUR (RIS-Justiz RS0125732) nicht übersteigt und das Rekursgericht den ordentlichen Revisionsrekurs nicht nach § 59 Abs 1 Z 2 AußStrG für zulässig erklärt hat.

| Predicted | Gold |
|---|---|
| `Jaromir Hägerich` | `Jaromir Hägerich` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Pimmer` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schramm` (person)
- `Dr. Gitschthaler` (person)
- `Univ.-Prof. Dr. Kodek` (person)
- `Dr. Nowotny` (person)
- `17. August 1962` (date)
- `Dr. Alexander Sporn` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

</details>

---

## `Name After Verb Subject` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `6f4a0fe2`  
**Description:**
Matches names that appear immediately after verbs indicating a person is the subject of a sentence (e.g., 'wurde [Name]'), often found in judgment summaries.

**Content:**
```
(?:wurde|wurden|ist|sind|war|waren|hat|haben|hatten|konnte|konnten|musste|mussten|durfte|durften|sollte|sollten|wird|werden|wurde|wurden)\s+([A-Z][a-zäöüß]+\s+[A-Z][a-zäöüß]+)\b(?=\s+(?:des|der|die|von|mit|durch|als|und|sowie|im|am|bei|nach|vor|über|unter|ohne|neben|zwischen|trotz|wegen|statt|außer|seit|während|bis|um|für|an|auf|in|,|\.|\(|\))|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 3 | 0 | 3958 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_14`)


Dennoch war Ottokar Laukeningkat (weiterhin) alleinverantwortlich für die Kontakte zu den Kunden, die Kalkulation der Aufträge und Angebote sowie deren Unterfertigung.

| Predicted | Gold |
|---|---|
| `Ottokar Laukeningkat` | `Ottokar Laukeningkat` |

**Example 1** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_6`)


Text Gründe: Mit dem angefochtenen Urteil wurden Bernhard Berti und Norbert Wierich von der wider sie erhobenen Anklage, sie hätten am 7. Februar 2009 in Sebastian-Stief-Gasse 48, 2632 Altendorf, Österreich /Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der Hauenschildt&Mesarec Medien GesmbH & Co KG, Susanne Schwarzhuber, durch die Vorgabe, die Donau-Transport GmbH sei eine zahlungsfähige Leasingnehmerin, somit durch Täuschung über Tatsachen, zum Abschluss eines Leasingvertrags über ein Rennfahrzeug für die Dauer von 24 Monaten zu einem monatlichen Entgelt von 10.698,10 Euro, somit zu einer Handlung verleitet, welche die TraunTouristik Werke GesmbH & Co KG in einem 50.000 Euro übersteigenden Betrag von insgesamt 235.358,20 Euro am Vermögen schädigte, gemäß § 259 Z 3 StPO (verfehlt auch von der rechtlichen Kategorie; vglLendl, WK-StPO § 259 Rz 1) freigesprochen.

| Predicted | Gold |
|---|---|
| `Bernhard Berti` | `Bernhard Berti` |

**Missed by this rule (FN):**

- `Norbert Wierich` (person)
- `Sebastian-Stief-Gasse 48, 2632 Altendorf, Österreich` (address)
- `Hauenschildt&Mesarec Medien GesmbH & Co KG` (organisation)
- `Susanne Schwarzhuber` (person)
- `Donau-Transport GmbH` (organisation)
- `TraunTouristik Werke GesmbH & Co KG` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/15Os43_13g`) (sent_id: `deanon_260716_TRAIN/15Os43_13g_7`)


RIS-Justiz RS0119509) des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 zweiter und dritter Fall SMG (A./1./), (richtig:) des Vergehens der Vorbereitung von Suchtgifthandel nach § 28 Abs 1 zweiter Satz, Abs 2 und Abs 4 SMG (A./2./), des Vergehens des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 zweiter Fall, Abs 2 SMG (A./3./), (richtig:) der Vergehen des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 (richtig:) zweiter und dritter Fall, Abs 2 SMG (B./I./) und des Vergehens des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 2, Abs 2 SMG (B./II./) schuldig erkannt und unter Anwendung des § 28 Abs 1 StGB nach § 28 Abs 4 SMG zu einer für eine Probezeit von drei Jahren bedingt nachgesehenen Freiheitsstrafe von sechs Monaten verurteilt. Nach dem Inhalt des Schuldspruchs hat Manfred Börekci in Aussichtsstraße 10, 4201 Aschlberg, Österreich A./ im Zeitraum von 2006 bis zum 8. Oktober 2009 1./ vorschriftswidrig Cannabis mit einem Reinheitsgehalt von zumindest 123 Gramm Delta 9-THC erzeugt und besessen, indem er eine unbekannte Menge an Cannabispflanzen anbaute, erntete, die Blüten trocknete und jedenfalls zum Teil Cannabisharz daraus gewann;

| Predicted | Gold |
|---|---|
| `Manfred Börekci` | `Manfred Börekci` |

**Missed by this rule (FN):**

- `Aussichtsstraße 10, 4201 Aschlberg, Österreich` (address)

</details>

---

## `Mag Dr Title` 🏆

**F1:** 0.046 | **Precision:** 0.971 | **Recall:** 0.024  

**Format:** `regex`  
**Rule ID:** `a76e8424`  
**Description:**
Specifically matches 'Mag. Dr.' or 'Dr. Mag.' followed by full names to ensure the full title sequence is captured.

**Content:**
```
(?:Mag\.\s+Dr\.|Dr\.\s+Mag\.)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.971 | 0.024 | 0.046 | 102 | 99 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 99 | 3 | 3935 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Mag. Kevin Maassen, vertreten durch Dr. Clemens Lintschinger, Rechtsanwalt in Wien, gegen die beklagte Partei Hon.-Prof. Friedhelm Adde, vertreten durch Mag. Dr. Georg Backhausen, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 27. Jänner 2016, GZ 38 R 265/15z-45, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Georg Backhausen` | `Mag. Dr. Georg Backhausen` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Ziegelbauer` (person)
- `Mag. Kevin Maassen` (person)
- `Dr. Clemens Lintschinger` (person)
- `Hon.-Prof. Friedhelm Adde` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10ObS99_15d`) (sent_id: `deanon_260716_TRAIN/10ObS99_15d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die fachkundigen Laienrichter Mag. Dr. Wolfgang Höfle (aus dem Kreis der Arbeitgeber) und Ing. Thomas Bauer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Willibald Kollowrat, BEd, vertreten durch Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH in Graz, gegen die beklagte Partei Versicherungsanstalt für Eisenbahnen und Bergbau, Linke Wienzeile 48-52, 1060 Wien, vertreten durch Dr. Marie-Luise Safranek, Rechtsanwältin in Graz, wegen Wochengeld, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Juni 2015, GZ 7 Rs 28/15i-9, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 25. Februar 2015, GZ 36 Cgs 216/14d-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wolfgang Höfle` | `Mag. Dr. Wolfgang Höfle` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Ing. Thomas Bauer` (person)
- `Willibald Kollowrat, BEd` (person)
- `Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH` (organisation)
- `Versicherungsanstalt für Eisenbahnen und Bergbau` (organisation)
- `Dr. Marie-Luise Safranek` (person)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/1Nc10_18p`) (sent_id: `deanon_260716_TRAIN/1Nc10_18p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Dr. Wurdinger als weitere Richter in dem beim Oberlandesgericht Graz zu AZ 5 R 5/15t anhängigen Rechtsmittelverfahren des Antragstellers Mag. Angelika Tränkel, wegen Verfahrenshilfe, den Beschluss gefasst:  Spruch Zur Entscheidung über den Rekurs des Antragstellers gegen den Beschluss des Landesgerichts Klagenfurt vom 28. Juli 2014, GZ 29 Nc 1/14b-22, wird das Oberlandesgericht Wien als zuständig bestimmt.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Oberlandesgericht Graz` (organisation)
- `Mag. Angelika Tränkel` (person)
- `Landesgerichts Klagenfurt` (organisation)
- `Oberlandesgericht Wien` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/1Ob103_20h`) (sent_id: `deanon_260716_TRAIN/1Ob103_20h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Kodek, Mag. Wurzer, Mag. Dr. Wurdinger und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Uwe Zanello, vertreten durch Mag. Peter Mayerhofer, Rechtsanwalt in Wiener Neustadt, gegen die beklagte Partei Janet Angelbeck, vertreten durch Dr. Alfred Steinbuch, Rechtsanwalt in Neunkirchen, wegen Ehescheidung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 26. März 2020, GZ 16 R 45/20m-22, mit dem das Urteil des Bezirksgerichts Neunkirchen vom 23. Dezember 2019, GZ 12 C 12/18s-18, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Univ.-Prof. Dr. Kodek` (person)
- `Mag. Wurzer` (person)
- `Dr. Parzmayr` (person)
- `Uwe Zanello` (person)
- `Mag. Peter Mayerhofer` (person)
- `Janet Angelbeck` (person)
- `Dr. Alfred Steinbuch` (person)
- `Landesgerichts Wiener Neustadt` (organisation)
- `Bezirksgerichts Neunkirchen` (organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/1Ob105_18z`) (sent_id: `deanon_260716_TRAIN/1Ob105_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Familienrechtssache des Antragstellers Ludmilla Bonauer, vertreten durch die Korp Rechtsanwalts GmbH, Andorf, gegen die Antragsgegnerin Henriette Geißendorf, vertreten durch die Puttinger Vogl Rechtsanwälte GmbH, Ried im Innkreis, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts Wels als Rekursgericht vom 2. Mai 2018, GZ 21 R 50/18d-32, mit dem der Rekurs des Antragstellers gegen den Beschluss des Bezirksgerichts Grieskirchen vom 8. Jänner 2018, GZ 8 Fam 37/16i-26, zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Ludmilla Bonauer` (person)
- `Korp Rechtsanwalts GmbH` (organisation)
- `Henriette Geißendorf` (person)
- `Puttinger Vogl Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Wels` (organisation)
- `Bezirksgerichts Grieskirchen` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/1Ob109_18p`) (sent_id: `deanon_260716_TRAIN/1Ob109_18p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Parteien 1. Mag. Eva Voeglein, und 2. Ursula Preising, vertreten durch die HOHENBERG STRAUSS BUCHBAUER Rechtsanwälte GmbH, Graz, gegen die beklagte Partei Gemeinde Veit Faeser, vertreten durch Dr. Klaus Rainer, Rechtsanwalt in Graz, wegen 573.890,70 EUR sA, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 2. Mai 2018, GZ 5 R 172/17d-57, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 23. Oktober 2017, GZ 41 Cg 51/15m-47, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Mag. Eva Voeglein` (person)
- `Ursula Preising` (person)
- `HOHENBERG STRAUSS BUCHBAUER Rechtsanwälte GmbH` (organisation)
- `Veit Faeser` (person)
- `Dr. Klaus Rainer` (person)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/1Ob121_25p`) (sent_id: `deanon_260716_TRAIN/1Ob121_25p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Dr. Wurdinger als Vorsitzenden sowie die Hofrätin und die Hofräte Dr. Steger, Mag. Wessely-Kristöfel, Dr. Parzmayr und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Severin Griguschies, vertreten durch Mag. Michael Lang, Rechtsanwalt in Wien, gegen die beklagte Partei Ilhan Sieper, vertreten durch Thomas Wagner-Szemethy, LL.M., Rechtsanwalt in Schwechat, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts Korneuburg als Berufungsgericht vom 13. Mai 2025, GZ 22 R 38/25f-28, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Steger` (person)
- `Mag. Wessely-Kristöfel` (person)
- `Dr. Parzmayr` (person)
- `Dr. Vollmaier` (person)
- `Severin Griguschies` (person)
- `Mag. Michael Lang` (person)
- `Ilhan Sieper` (person)
- `Thomas Wagner-Szemethy, LL.M.` (person)
- `Landesgerichts Korneuburg` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/1Ob127_14d`) (sent_id: `deanon_260716_TRAIN/1Ob127_14d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Dr. Rocco Reichl, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Rocco Reichl` (person)

**Example 8** (doc_id: `deanon_260716_TRAIN/1Ob128_17f`) (sent_id: `deanon_260716_TRAIN/1Ob128_17f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Familienrechtssache des Antragstellers Mag. Josefine Rehn, vertreten durch die Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG, Wien, gegen die Antragsgegnerin Susanne Lürkens, vertreten durch Mag. Anna-Maria Freiberger, Rechtsanwältin in Wien, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 24. April 2017, GZ 45 R 66/17i, 67/17m-19, mit dem die Beschlüsse des Bezirksgerichts Liesing vom 4. Jänner 2017, GZ 7 Fam 30/16m-12, und vom 17. Jänner 2017, GZ 7 Fam 30/16m-14, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Mag. Josefine Rehn` (person)
- `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG` (organisation)
- `Susanne Lürkens` (person)
- `Mag. Anna-Maria Freiberger` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Liesing` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/1Ob12_21b`) (sent_id: `deanon_260716_TRAIN/1Ob12_21b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Mag. Mathias Gumbel, vertreten durch die Huber & Partner Rechtsanwälte GmbH, Linz, gegen die beklagten Parteien 1. Otto Gerdhennrich, 2.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Mag. Mathias Gumbel` (person)
- `Huber & Partner Rechtsanwälte GmbH` (organisation)
- `Otto Gerdhennrich` (person)

**Example 10** (doc_id: `deanon_260716_TRAIN/1Ob139_18z`) (sent_id: `deanon_260716_TRAIN/1Ob139_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Verena Tappendorff Inc., Sankt Andrä im Sausal 24, 8552 Aichberg, Österreich, vertreten durch Mag. Ralph Kilches, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Sabine Martinsson, als Insolvenzverwalter im Insolvenzverfahren über das Vermögen der Touristik Synberbruck GmbH, Fridau 56l, 7433 Bergwerk, Österreich, vertreten durch die Haslinger/Nagele & Partner Rechtsanwälte GmbH, Linz, wegen Feststellung einer Insolvenzforderung (Streitwert 447.352,05 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 28. Juni 2018, GZ 1 R 83/18h-8, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Verena Tappendorff` (person)
- `Sankt Andrä im Sausal 24, 8552 Aichberg, Österreich` (address)
- `Mag. Ralph Kilches` (person)
- `Mag. Sabine Martinsson` (person)
- `Touristik Synberbruck GmbH` (organisation)
- `Fridau 56l, 7433 Bergwerk, Österreich` (address)
- `Haslinger/Nagele & Partner Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Linz` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/1Ob142_19t`) (sent_id: `deanon_260716_TRAIN/1Ob142_19t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der Antragstellerin Mag. Kassandra Christoforidou, vertreten Dr. Brigitte Birnbaum und Dr. Rainer Toperczer, Rechtsanwälte in Wien, gegen den Antragsgegner Dr. Otto Einhenkel, vertreten durch die Anwaltssocietät Sattlegger Dorninger Steiner & Partner OG, Linz, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse gemäß §§ 81 ff EheG, über die außerordentlichen Revisionsrekurse beider Parteien gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 9. Juli 2019, GZ 45 R 554/18f-162, mit dem der Beschluss des Bezirksgerichts Fünfhaus vom 25. Oktober 2018, GZ 4 Fam 68/14k-156, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Der Revisionsrekurs des Antragsgegners wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Mag. Kassandra Christoforidou` (person)
- `Dr. Brigitte Birnbaum` (person)
- `Dr. Rainer Toperczer` (person)
- `Dr. Otto Einhenkel` (person)
- `Anwaltssocietät Sattlegger Dorninger Steiner & Partner OG` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Fünfhaus` (organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/1Ob152_24w`) (sent_id: `deanon_260716_TRAIN/1Ob152_24w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Musger als Vorsitzenden sowie die Hofrätin und die Hofräte Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Harald Adolphsen KG, FN FN214876m, vertreten durch Dr. Eva-Maria Bachmann-Lang, Dr. Christian Bachmann, Rechtsanwälte in Wien, gegen die beklagte Partei „ Alpen Donalcon “ OXS Bildung gmbH, FN FN067476g, vertreten durch die GRAF ISOLA Rechtsanwälte GmbH in Wien, wegen 51.843,91 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 3. Juli 2024, GZ 1 R 17/24p-39, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Musger` (person)
- `Mag. Wurzer` (person)
- `Mag. Wessely-Kristöfel` (person)
- `Dr. Parzmayr` (person)
- `Harald Adolphsen` (person)
- `FN214876m` (business_register_number)
- `Dr. Eva-Maria Bachmann` (person)
- `Dr. Christian Bachmann` (person)
- `Alpen Donalcon` (organisation)
- `OXS Bildung gmbH` (organisation)
- `FN067476g` (business_register_number)
- `GRAF ISOLA Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/1Ob159_20v`) (sent_id: `deanon_260716_TRAIN/1Ob159_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und Hofrätinnen, Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Bachfen Entwicklung AG, Reisedt 4, 4770 Radlern, Österreich, vertreten durch Mag. Markus Stender, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. Musialek Getränke GmbH, 2.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Mag. Korn` (person)
- `Bachfen Entwicklung AG` (organisation)
- `Reisedt 4, 4770 Radlern, Österreich` (address)
- `Mag. Markus Stender` (person)
- `Musialek Getränke GmbH` (organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/1Ob160_12d`) (sent_id: `deanon_260716_TRAIN/1Ob160_12d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der außerstreitigen Rechtssache der Antragstellerin Dipl. Kff. OSR Evamaria Ishak, vertreten durch Dr. Karl-Peter Hasch, Rechtsanwalt in Villach, gegen den Antragsgegner Niklas Damianidis, vertreten durch Mag. Hanno Stromberger, Rechtsanwalt in Villach, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse über den Revisionsrekurs der Antragstellerin gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 31. Mai 2012, GZ 2 R 85/12w-11, mit dem der Beschluss des Bezirksgerichts Villach vom 13. März 2012, GZ 38 Fam 98/11s-7, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Dr. Grohmann` (person)
- `Mag. Wurzer` (person)
- `Dipl. Kff. OSR Evamaria Ishak` (person)
- `Dr. Karl-Peter Hasch` (person)
- `Niklas Damianidis` (person)
- `Mag. Hanno Stromberger` (person)
- `Landesgerichts Klagenfurt` (organisation)
- `Bezirksgerichts Villach` (organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/1Ob163_21h`) (sent_id: `deanon_260716_TRAIN/1Ob163_21h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Christine Neemeyer, vertreten durch Mag. Dieter Koch und Mag. Natascha Jilek, Rechtsanwälte in Bruck an der Mur, gegen die beklagte Partei Synbach-Holz Bank AG, Bergbahnweg 7j, 4632 Oberthambach, Österreich, vertreten durch Mag. Martina Hosp ua, Rechtsanwälte in Salzburg, wegen Feststellung (Streitwert 103.488,18 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 21. Juni 2021, GZ 2 R 70/21h-19, mit dem das Urteil des Landesgerichts Salzburg vom 12. März 2021, GZ 10 Cg 52/20k-15, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Christine Neemeyer` (person)
- `Mag. Dieter Koch` (person)
- `Mag. Natascha Jilek` (person)
- `Synbach-Holz Bank` (organisation)
- `Bergbahnweg 7j, 4632 Oberthambach, Österreich` (address)
- `Mag. Martina Hosp` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Salzburg` (organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/1Ob169_15g`) (sent_id: `deanon_260716_TRAIN/1Ob169_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Dalibor Jonetzko, vertreten durch Dr. Johannes Öhlböck, LL.M., Rechtsanwalt in Wien, gegen die beklagte Partei Stadt Waltraud Wedekämper, vertreten durch Dr. Josef Milchram, Rechtsanwalt in Wien, wegen 100.000 EUR sA und Feststellung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Mai 2015, GZ 14 R 140/14g-16, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 21. August 2014, GZ 31 Cg 14/14b-12, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dalibor Jonetzko` (person)
- `Dr. Johannes Öhlböck, LL.M.` (person)
- `Waltraud Wedekämper` (person)
- `Dr. Josef Milchram` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/1Ob171_22m`) (sent_id: `deanon_260716_TRAIN/1Ob171_22m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Musger als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Aloisa Dewitz, vertreten durch Mag. Klaus Mayer, Rechtsanwalt in Premstätten, gegen die beklagte Partei Tilles Software Limited, Dr.Wilhelm Steingötter-Straße 39, 4881 Wald, Österreich, vertreten durch Dr. Fabian Maschke, Rechtsanwalt in Wien, wegen 36.070 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 3. August 2022, GZ 4 R 98/22x-24, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Musger` (person)
- `Mag. Wurzer` (person)
- `Mag. Wessely-Kristöfel` (person)
- `Dr. Parzmayr` (person)
- `Aloisa Dewitz` (person)
- `Mag. Klaus Mayer` (person)
- `Tilles Software Limited` (organisation)
- `Dr.Wilhelm Steingötter-Straße 39, 4881 Wald, Österreich` (address)
- `Dr. Fabian Maschke` (person)
- `Oberlandesgerichts Graz` (organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Dr. Florenzia Münsterer, vertreten durch Rechtsanwälte Dr. Amhof & Dr. Damian GmbH in Wien, gegen die beklagte Partei MittelEnergie Werke Bank AG, Altlassing 110, 4183 Ahorn, Österreich, vertreten durch Urbanek Lind Schmied Reisch Rechtsanwälte OG in Wien, wegen 600.090 EUR sA, über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 25. Mai 2011, GZ 15 R 64/11h-54, mit dem das Urteil des Handelsgerichts Wien vom 14. Jänner 2011, GZ 16 Cg 20/10f-50, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Dr. Grohmann` (person)
- `Mag. Wurzer` (person)
- `Dr. Florenzia Münsterer` (person)
- `Rechtsanwälte Dr. Amhof & Dr. Damian GmbH` (organisation)
- `MittelEnergie Werke Bank` (organisation)
- `Altlassing 110, 4183 Ahorn, Österreich` (address)
- `Urbanek Lind Schmied Reisch Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/1Ob174_19y`) (sent_id: `deanon_260716_TRAIN/1Ob174_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Theophil Mielewzyk, vertreten durch Dr. Hannes Paulweber, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Liu Jantschar, vertreten durch die Heiss & Heiss Rechtsanwälte OG, Innsbruck, wegen 137.664,28 EUR sA sowie Feststellung (Streitwert 15.000 EUR), über die außerordentliche Revision der beklagten Partei gegen das (richtig) Teilzwischenurteil des Oberlandesgerichts Innsbruck vom 18. Juli 2019, GZ 1 R 76/19i-74, mit dem das Urteil des Landesgerichts Innsbruck vom 21. Februar 2019, GZ 8 Cg 119/16z-68, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Theophil Mielewzyk` (person)
- `Dr. Hannes Paulweber` (person)
- `Liu Jantschar` (person)
- `Heiss & Heiss Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Innsbruck` (organisation)
- `Landesgerichts Innsbruck` (organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/1Ob178_19m`) (sent_id: `deanon_260716_TRAIN/1Ob178_19m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Hilde Dammrow, vertreten durch die Korn und Gärtner Rechtsanwälte OG, Salzburg, gegen die beklagte Partei Evelyn Allmutter, vertreten durch die Ferner Hornung & Partner Rechtsanwälte GmbH, Salzburg, wegen Wiederaufnahme des Verfahrens AZ 17 C 1538/16p des Bezirksgerichts Salzburg, über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 12. Juni 2019, GZ 22 R 163/19b-7, mit dem der Beschluss des Bezirksgerichts Salzburg vom 25. Jänner 2019, GZ 17 C 80/19f-2, mit einer Maßgabe bestätigt wurde, den Beschluss gefasst:  Spruch Dem außerordentlichen Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Hilde Dammrow` (person)
- `Evelyn Allmutter` (person)
- `Hornung & Partner Rechtsanwälte GmbH` (organisation)
- `Bezirksgerichts Salzburg` (organisation)
- `Landesgerichts Salzburg` (organisation)
- `Bezirksgerichts Salzburg` (organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/1Ob179_12y`) (sent_id: `deanon_260716_TRAIN/1Ob179_12y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Pflegschaftssache des mj Traude Wedtrat, geboren am 13. Juli 2006, vertreten durch Mag. Heinz Wolfbauer, Rechtsanwalt in Wien, wegen Unterhalts, über den Revisionsrekurs des Vaters Dr. Rainer Steinstrass, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 29. Mai 2012, GZ 43 R 254/12i-106, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Döbling vom 28. März 2012, GZ 10 Pu 131/09b-100, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Dr. Grohmann` (person)
- `Mag. Wurzer` (person)
- `Traude Wedtrat` (person)
- `Mag. Heinz Wolfbauer` (person)
- `Dr. Rainer Steinstrass` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Döbling` (organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/1Ob182_17x`) (sent_id: `deanon_260716_TRAIN/1Ob182_17x_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Dr. Wurdinger, und die Hofrätinnen Dr. Hofer-Zeni-Rennhofer und Dr. Kodek in der Rechtssache der gefährdeten Partei Aloisa Moosleitner, vertreten durch die Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG, Wien, gegen die gefährdete Partei Catharina Uppenbrink, vertreten durch Dr. Alexander Haas, Rechtsanwalt in Seiersberg-Pirka, wegen Erlassung einer einstweiligen Verfügung nach § 382 Z 8 lit c zweiter Fall EO, über den außerordentlichen Revisionsrekurs der gefährdeten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 11. September 2017, GZ 1 R 213/17a-221, mit dem der Beschluss des Bezirksgerichts Fürstenfeld vom 25. Juli 2017, GZ 23 Fam 27/15p-207, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch 1.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Kodek` (person)
- `Aloisa Moosleitner` (person)
- `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG` (organisation)
- `Catharina Uppenbrink` (person)
- `Dr. Alexander Haas` (person)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)
- `Bezirksgerichts Fürstenfeld` (organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/1Ob186_12b`) (sent_id: `deanon_260716_TRAIN/1Ob186_12b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Thomas Plüm, vertreten durch Kammler & Koll Rechtsanwälte OG in Freistadt, gegen die beklagte Partei Patrick Dimpfel, vertreten durch Mag. Klaus Burgholzer, Rechtsanwalt in Linz, wegen 100.000 EUR sA und Feststellung (Streitwert: 5.000 EUR), über die außerordentliche Revision der klagenden Partei (Revisionsinteresse: 70.000 EUR sA) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. Juli 2012, GZ 2 R 79/12v-22, mit dem das Urteil des Landesgerichts Linz vom 27. Februar 2012, GZ 5 Cg 61/11d-18, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Dr. Grohmann` (person)
- `Mag. Wurzer` (person)
- `Thomas Plüm` (person)
- `Kammler & Koll Rechtsanwälte OG` (organisation)
- `Patrick Dimpfel` (person)
- `Mag. Klaus Burgholzer` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Linz` (organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/1Ob192_11h`) (sent_id: `deanon_260716_TRAIN/1Ob192_11h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Hierle Sanitär Limited, London, Zirkinger Straße 3, 8082 Glatzau, Österreich, vertreten durch Thum Weinreich Schwarz Fuchsbauer Rechtsanwälte OG in St. Pölten, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 1,8 Mio EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Juni 2011, GZ 14 R 214/10h-39, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 3. September 2010, GZ 33 Cg 3/09t-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Dr. Grohmann` (person)
- `Mag. Wurzer` (person)
- `Hierle Sanitär Limited` (organisation)
- `Zirkinger Straße 3, 8082 Glatzau, Österreich` (address)
- `Thum Weinreich Schwarz Fuchsbauer Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/1Ob216_15v`) (sent_id: `deanon_260716_TRAIN/1Ob216_15v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Suleika Kranigk, vertreten durch Hon.-Prof. Dr. Michel Walter, Rechtsanwalt in Wien, gegen die beklagte Partei Kelfen Transport Solutions GmbH, Geßlgasse 35, 9911 Thal-Wilfern, Österreich, vertreten durch die Schlösser & Partner Rechtsanwälte OG, Graz, wegen 33.930 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 19. August 2015, GZ 13 R 74/15w-55, mit dem das Endurteil des Landesgerichts Korneuburg vom 26. Februar 2015, GZ 3 Cg 15/13h-50, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Suleika Kranigk` (person)
- `Hon.-Prof. Dr. Michel Walter` (person)
- `Kelfen Transport Solutions GmbH` (organisation)
- `Geßlgasse 35, 9911 Thal-Wilfern, Österreich` (address)
- `Partner Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts Korneuburg` (organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/1Ob216_19z`) (sent_id: `deanon_260716_TRAIN/1Ob216_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat des Obersten Gerichtshofs Mag. Wurzer als Vorsitzenden sowie die Hofräte und Hofrätinnen Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer, Dr. Parzmayr und Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Charles Adlwarth, MMSc, Haidspitzgasse 53R, 4294 Rehberg, Österreich, vertreten durch Dr. Michael Pallauf, LL.M., und andere, Rechtsanwälte in Salzburg, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 41.978,49 EUR sA sowie Feststellung (Streitwert 40.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. September 2019, GZ 14 R 75/19f-18, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 24. April 2019, GZ 33 Cg 26/18p-14, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Dr. Faber` (person)
- `Charles Adlwarth` (person)
- `Haidspitzgasse 53R, 4294 Rehberg, Österreich` (address)
- `Dr. Michael Pallauf, LL.M.` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/1Ob224_19a`) (sent_id: `deanon_260716_TRAIN/1Ob224_19a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Thassilo John, vertreten durch Dr. Johannes Kirschner, Rechtsanwalt in Wels, gegen die beklagte Partei Mona Kutzner, vertreten durch Dr. Widukind W. Nordmeyer und Dr. Thomas Kitzberger, Rechtsanwälte in Wels, wegen 30.600 EUR sA, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 28. Oktober 2019, GZ 6 R 131/19f-16, mit dem der Beschluss des Landesgerichts Wels vom 13. September 2019, GZ 36 Cg 25/19g-11, abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Thassilo John` (person)
- `Dr. Johannes Kirschner` (person)
- `Mona Kutzner` (person)
- `Dr. Widukind W. Nordmeyer` (person)
- `Dr. Thomas Kitzberger` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Wels` (organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/1Ob224_20b`) (sent_id: `deanon_260716_TRAIN/1Ob224_20b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache klagenden Partei Rainer Baetzel, vertreten durch Dr. Harald Hauer, Rechtsanwalt in Wien, gegen die beklagte Partei Rimscha Versand GmbH in Liquidation, Götzau 193, 5452 Grub, Österreich, vertreten durch die Petsch Frosch Klein Arturo Rechtsanwälte OG, Wien, wegen 38.236,58 EUR sA und Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Oktober 2020, GZ 3 R 51/20x-50, mit dem das Urteil des Handelsgerichts Wien vom 24. Juli 2020, GZ 34 Cg 51/18h-45, bestätigt wurde, in nicht öffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Rainer Baetzel` (person)
- `Dr. Harald Hauer` (person)
- `Rimscha Versand GmbH` (organisation)
- `Götzau 193, 5452 Grub, Österreich` (address)
- `Petsch Frosch Klein Arturo Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/1Ob226_20x`) (sent_id: `deanon_260716_TRAIN/1Ob226_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Pia Geermann GmbH, Orise 28, 9135 Unterort, Österreich, vertreten durch Dr. Martin Leitner und andere, Rechtsanwälte in Wien, gegen die beklagte Partei Stadt Li Wachmeister, vertreten durch die Estermann Pock Rechtsanwälte GmbH, Wien, wegen 19.002,01 EUR, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 7. September 2020, GZ 14 R 61/20y-27, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 28. Jänner 2020, GZ 31 Cg 1/19y-22, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Pia Geermann` (person)
- `Orise 28, 9135 Unterort, Österreich` (address)
- `Dr. Martin Leitner` (person)
- `Li Wachmeister` (person)
- `Estermann Pock Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/1Ob22_24b`) (sent_id: `deanon_260716_TRAIN/1Ob22_24b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Musger als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der gefährdeten Partei Caroline Traboldt, vertreten durch Mag. Stefan Hotz, Rechtsanwalt in Wien, gegen den Gegner der gefährdeten Partei Mag. Brigitte von Obstfelder, vertreten durch Dr. Kristina Venturini, Rechtsanwältin in Wien, wegen Ehescheidung, hier wegen vorläufigen Unterhalts, über den außerordentlichen Revisionsrekurs der gefährdeten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 13. Dezember 2023, GZ 44 R 314/23m-203, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionrekurs wird mangels der Voraussetzungen des § 528 Abs 1 ZPO (iVm §§ 78, 402 Abs 4 EO) zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Musger` (person)
- `Mag. Wurzer` (person)
- `Mag. Wessely-Kristöfel` (person)
- `Dr. Parzmayr` (person)
- `Caroline Traboldt` (person)
- `Mag. Stefan Hotz` (person)
- `Mag. Brigitte von Obstfelder` (person)
- `Dr. Kristina Venturini` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/1Ob26_20k`) (sent_id: `deanon_260716_TRAIN/1Ob26_20k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Schrickel Luftfahrt GmbH, Grieselstein-Rosenberg 3, 3314 Ottendorf, Österreich, vertreten durch die Draxler Rexeis Sozietät von Rechtsanwälten OG, Graz, gegen die beklagte Partei Monika Peikert, vertreten durch Mag. Dr. Alfred Wansch, Rechtsanwalt in Wien, wegen Räumung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtsachen Wien als Berufungsgericht vom 13. November 2019, GZ 39 R 228/19x-70, mit dem das Urteil des Bezirksgerichts Hernals vom 30. April 2019, GZ 4 C 277/16f-64, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |
| `Mag. Dr. Alfred Wansch` | `Mag. Dr. Alfred Wansch` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Schrickel Luftfahrt GmbH` (organisation)
- `Grieselstein-Rosenberg 3, 3314 Ottendorf, Österreich` (address)
- `Draxler Rexeis Sozietät von Rechtsanwälten OG` (organisation)
- `Monika Peikert` (person)
- `Bezirksgerichts Hernals` (organisation)

**Example 32** (doc_id: `deanon_260716_TRAIN/1Ob29_20a`) (sent_id: `deanon_260716_TRAIN/1Ob29_20a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Familienrechtssache der Antragstellerin Evamaria Konopatsch, vertreten durch Dr. Walter Mardetschläger und andere Rechtsanwälte in Wien, gegen den Antragsgegner Lubomir Strässle, vertreten durch Dr. Peter Paul Wolf, Rechtsanwalt in Wien, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den außerordentlichen Revisionsrekurs der Antragstellerin gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 19. Dezember 2019, GZ 43 R 586/19y-81, mit dem der Beschluss des Bezirksgerichts Donaustadt vom 17. Oktober 2019, GZ 29 Fam 7/18w-71, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Evamaria Konopatsch` (person)
- `Dr. Walter Mardetschläger` (person)
- `Lubomir Strässle` (person)
- `Dr. Peter` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)

**Example 33** (doc_id: `deanon_260716_TRAIN/1Ob32_17p`) (sent_id: `deanon_260716_TRAIN/1Ob32_17p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Alexandra Astfalke, vertreten durch Dr. Gerhard Schatzlmayr, Rechtsanwalt in Schwanenstadt, gegen die beklagte Partei Dr. Sean Rudloph, vertreten durch Dr. Robert Galler und Dr. Rudolf Höpflinger, Rechtsanwälte in Salzburg, wegen Ehescheidung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts Wels als Berufungsgericht vom 14. Dezember 2016, GZ 21 R 291/16t-22, mit dem das Urteil des Bezirksgerichts Gmunden vom 22. Juli 2016, GZ 1 C 26/15t-15, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Alexandra Astfalke` (person)
- `Dr. Gerhard Schatzlmayr` (person)
- `Dr. Sean Rudloph` (person)
- `Dr. Robert Galler` (person)
- `Dr. Rudolf Höpflinger` (person)
- `Landesgerichts Wels` (organisation)
- `Bezirksgerichts Gmunden` (organisation)

**Example 34** (doc_id: `deanon_260716_TRAIN/1Ob34_20m`) (sent_id: `deanon_260716_TRAIN/1Ob34_20m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Pflegschaftssache der mj Selma Amboß, geboren am 5. Juli 2004, wegen Unterhalts, über den Revisionsrekurs des Kindes, vertreten durch das Land Niederösterreich (Kinder- und Jugendhilfeträger), gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 1. Oktober 2019, GZ 16 R 284/19g-102, mit dem der Beschluss des Bezirksgerichts Mödling vom 2. August 2019, GZ 2 Pu 193/14y-97, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.  Text Begründung: Das Kind befindet sich in Pflege und Erziehung der Mutter.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Selma Amboß` (person)
- `5. Juli` (date)
- `Landesgerichts Wiener Neustadt` (organisation)
- `Bezirksgerichts Mödling` (organisation)

**Example 35** (doc_id: `deanon_260716_TRAIN/1Ob34_22i`) (sent_id: `deanon_260716_TRAIN/1Ob34_22i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Vivian Frenkmann, vertreten durch Dr. Günter Wappel, Rechtsanwalt in Wien, gegen die beklagte Partei Erna Mitterneder, vertreten durch Mag. Petra Thurner, Rechtsanwältin in Wien, wegen Feststellung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 15. Dezember 2021, GZ 42 R 332/21s-55, mit dem das Urteil des Bezirksgerichts Fünfhaus vom 14. Juni 2021, GZ 3 C 23/19x-50, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.  Text Begründung: [1]

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Wessely-Kristöfel` (person)
- `Dr. Parzmayr` (person)
- `Vivian Frenkmann` (person)
- `Dr. Günter Wappel` (person)
- `Erna Mitterneder` (person)
- `Mag. Petra Thurner` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Fünfhaus` (organisation)

**Example 36** (doc_id: `deanon_260716_TRAIN/1Ob37_16x`) (sent_id: `deanon_260716_TRAIN/1Ob37_16x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Pflegschaftssache des mj Priv.-Doz. Wieland Dancke, geboren am 9. August 2013, über den außerordentlichen Revisionsrekurs der Mutter Deborah Hänsdieke, vertreten durch Dr. Stefan Glaser, Rechtsanwalt in Ried im Innkreis, gegen den Beschluss des Landesgerichts Ried im Innkreis als Rekursgericht vom 18. Dezember 2015, GZ 6 R 147/15g-59, mit dem der Beschluss des Bezirksgerichts Ried im Innkreis vom 1. September 2015, GZ 1 Ps 96/14h-51, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Priv.-Doz. Wieland Dancke` (person)
- `Deborah Hänsdieke` (person)
- `Dr. Stefan Glaser` (person)
- `Landesgerichts Ried im Innkreis` (organisation)
- `Bezirksgerichts Ried im Innkreis` (organisation)

**Example 37** (doc_id: `deanon_260716_TRAIN/1Ob43_20k`) (sent_id: `deanon_260716_TRAIN/1Ob43_20k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Pflegschaftssache des mj Marcel Batman, geboren am 25. Juli 2005, wegen Unterhalts, über den Revisionsrekurs des Kindes, vertreten durch das Land Niederösterreich (Kinder- und Jugendhilfeträger), gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 3. Juni 2019, GZ 16 R 156/19h-51, mit dem der Beschluss des Bezirksgerichts Mödling vom 9. April 2019, GZ 13 Pu 27/14t-44, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.  Text Begründung: Das Kind befindet sich in Pflege und Erziehung der (berufstätigen) Mutter.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Marcel Batman` (person)
- `25. Juli` (date)
- `Landesgerichts Wiener Neustadt` (organisation)
- `Bezirksgerichts Mödling` (organisation)

**Example 38** (doc_id: `deanon_260716_TRAIN/1Ob51_11y`) (sent_id: `deanon_260716_TRAIN/1Ob51_11y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei mj Luna Saar, vertreten durch Mag. Erich Frenner, Rechtsanwalt in Saalfelden, gegen die beklagte Partei Bernexwald Heizung GmbH, Viaduktstraße 131, 4814 Gmundnerberg, Österreich, vertreten durch Dr. Harald Schwendinger und Dr. Brigitte Piber Rechtsanwälte in Salzburg, wegen 5.100 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 30. Dezember 2010, GZ 53 R 273/10v-12, mit dem über die Berufung der beklagten Partei das Zwischenurteil des Bezirksgerichts Saalfelden vom 23. Juni 2010, GZ 2 C 454/10z-7, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Dr. Grohmann` (person)
- `Mag. Wurzer` (person)
- `Luna Saar` (person)
- `Mag. Erich Frenner` (person)
- `Bernexwald Heizung GmbH` (organisation)
- `Viaduktstraße 131, 4814 Gmundnerberg, Österreich` (address)
- `Dr. Harald Schwendinger` (person)
- `Dr. Brigitte Piber` (person)
- `Landesgerichts Salzburg` (organisation)
- `Bezirksgerichts Saalfelden` (organisation)

**Example 39** (doc_id: `deanon_260716_TRAIN/1Ob51_14b`) (sent_id: `deanon_260716_TRAIN/1Ob51_14b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Mittel-Landwirtschaft Betriebe GmbH, Baurat Schneider Straße 3, 4612 Finklham, Österreich, vertreten durch Dr. Arno Kempf, Rechtsanwalt in Spittal an der Drau, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Dr. Grohmann` (person)
- `Mag. Wurzer` (person)
- `Mittel-Landwirtschaft Betriebe GmbH` (organisation)
- `Baurat Schneider Straße 3, 4612 Finklham, Österreich` (address)
- `Dr. Arno Kempf` (person)

**Example 40** (doc_id: `deanon_260716_TRAIN/1Ob53_25p`) (sent_id: `deanon_260716_TRAIN/1Ob53_25p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Dr. Wurdinger als Vorsitzenden sowie die Hofrätin und die Hofräte Dr. Steger, Mag. Wessely-Kristöfel, Dr. Parzmayr und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Gottfried Lügenbiehl, vertreten durch die ANWALTGMBH Rinner Teuchtmann in Linz, gegen die beklagte Partei Ing. Marlene Fahlandt, vertreten durch die Wintersberger Rechtsanwälte GmbH in Ried im Innkreis, wegen 200.500 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 30. Jänner 2025, GZ 1 R 2/25g-86, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Steger` (person)
- `Mag. Wessely-Kristöfel` (person)
- `Dr. Parzmayr` (person)
- `Dr. Vollmaier` (person)
- `Gottfried Lügenbiehl` (person)
- `ANWALTGMBH Rinner Teuchtmann` (organisation)
- `Ing. Marlene Fahlandt` (person)
- `Wintersberger Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Linz` (organisation)

**Example 41** (doc_id: `deanon_260716_TRAIN/1Ob55_13i`) (sent_id: `deanon_260716_TRAIN/1Ob55_13i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Pflegschaftssache des mj Laurentia Bickendorf, geboren am 16. Dezember 2000, vertreten durch die Mutter Susanne Gschwändler, vertreten durch Mag. Herbert Premur, Rechtsanwalt in Klagenfurt, wegen pflegschaftsgerichtlicher Genehmigung einer Klage, über den außerordentlichen Revisionsrekurs des Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 12. Februar 2013, GZ 44 R 61/13s-101, mit dem der Beschluss des Bezirksgerichts Döbling vom 6. Dezember 2012, GZ 2 Ps 94/11f-98, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Dr. Grohmann` (person)
- `Mag. Wurzer` (person)
- `Laurentia Bickendorf` (person)
- `16. Dezember` (date)
- `Susanne Gschwändler` (person)
- `Mag. Herbert Premur` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Döbling` (organisation)

**Example 42** (doc_id: `deanon_260716_TRAIN/1Ob56_17t`) (sent_id: `deanon_260716_TRAIN/1Ob56_17t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Leonhard Lakmayer Ltd, Klauser Ried 27, 4880 Thalham, Österreich, vertreten durch Dr. Wolfgang G. Kretschmer, LL.M. Rechtsanwalt in Wien, gegen die beklagte Partei Frommenkord Technik GmbH, Wiesenthalgasse 20, 2000 Oberzögersdorf, Österreich, vertreten durch Dr. Herwig B. Schönbauer, Rechtsanwalt in Wien, und die Nebenintervenientinnen auf Seiten der beklagten Partei 1.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Leonhard Lakmayer` (person)
- `Klauser Ried 27, 4880 Thalham, Österreich` (address)
- `Dr. Wolfgang G. Kretschmer, LL.M.` (person)
- `Frommenkord Technik GmbH` (organisation)
- `Wiesenthalgasse 20, 2000 Oberzögersdorf, Österreich` (address)
- `Dr. Herwig B. Schönbauer` (person)

**Example 43** (doc_id: `deanon_260716_TRAIN/1Ob56_21y`) (sent_id: `deanon_260716_TRAIN/1Ob56_21y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Parteien 1. Dipl. Kfm. Christian Capotosto und 2. Maria Türing, vertreten durch Dr. Serpil Dogan, Rechtsanwältin in Feldkirch, gegen die beklagte Partei Republik Österreich (Bund), vertreten durch die Finanzprokuratur in Wien, und den Nebenintervenienten auf Seite der beklagten Partei RgR Caroline Dietrichs, vertreten durch Dr. Bertram Grass und Mag. Christoph Dorner, Rechtsanwälte in Bregenz, wegen 60.300 EUR sA und Feststellung (Erstklägerin) und 66.300 EUR sA und Feststellung (Zweitkläger), über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 27. Jänner 2021, GZ 4 R 171/20h-41, mit dem das Urteil des Landesgerichts Feldkirch vom 2. Oktober 2020, GZ 4 Cg 14/19k-35, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Dipl. Kfm. Christian Capotosto` (person)
- `Maria Türing` (person)
- `Dr. Serpil Dogan` (person)
- `RgR Caroline Dietrichs` (person)
- `Dr. Bertram Grass und Mag. Christoph Dorner` (person)
- `Oberlandesgerichts Innsbruck` (organisation)
- `Landesgerichts Feldkirch` (organisation)

**Example 44** (doc_id: `deanon_260716_TRAIN/1Ob57_16p`) (sent_id: `deanon_260716_TRAIN/1Ob57_16p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der außerstreitigen Familienrechtssache der Antragstellerin und gefährdeten Partei Kai Luxenburg, vertreten durch Mag. Nikolaus Vasak, Rechtsanwalt in Wien, gegen den Antragsgegner und Gegner der gefährdeten Partei PhD Marion Westenrieder, vertreten durch Dr. Josef Lindlbauer, Rechtsanwalt in Enns, wegen (einstweiligen) Unterhalts, über den Revisionsrekurs des Antragsgegners gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 17. September 2015, GZ 16 R 271/15i-77, mit dem der Beschluss des Bezirksgerichts Mödling vom 29. Juni 2015, GZ 2 Fam 68/14f-58, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Kai Luxenburg` (person)
- `Mag. Nikolaus Vasak` (person)
- `PhD Marion Westenrieder` (person)
- `Dr. Josef Lindlbauer` (person)
- `Landesgerichts Wiener Neustadt` (organisation)
- `Bezirksgerichts Mödling` (organisation)

**Example 45** (doc_id: `deanon_260716_TRAIN/1Ob60_22p`) (sent_id: `deanon_260716_TRAIN/1Ob60_22p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Pflegschaftssache des mj Melissa Sotiriadis, geboren am 11. Januar 2011, über den außerordentlichen Revisionsrekurs der Mutter PhD Ronja Jakobietz, vertreten durch Mag. Elisabeth Mace, Rechtsanwältin in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 11. Jänner 2022, GZ 48 R 263/21p-80, mit dem der Beschluss des Bezirksgerichts Floridsdorf vom 25. Oktober 2021, GZ 1 Ps 110/18i-71, bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Wessely-Kristöfel` (person)
- `Dr. Parzmayr` (person)
- `Melissa Sotiriadis` (person)
- `11. Januar` (date)
- `PhD Ronja Jakobietz` (person)
- `Mag. Elisabeth Mace` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Floridsdorf` (organisation)

**Example 46** (doc_id: `deanon_260716_TRAIN/1Ob61_18d`) (sent_id: `deanon_260716_TRAIN/1Ob61_18d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Johanna Moehrlin, vertreten durch Dr. Georg Kahlig und Mag. Gerhard Stauder, Rechtsanwälte in Wien, gegen die beklagte Partei DI Camilla Willoweit, vertreten durch Dr. Reinhard Schäfer, Rechtsanwalt in Wien, wegen Unterhalts, über die „außerordentliche“ Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 1. März 2018, GZ 45 R 517/17p-75, mit dem das Urteil des Bezirksgerichts Innere Stadt Wien vom 19. September 2017, GZ 4 C 50/14g-68, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.  Text Begründung: Das Erstgericht sprach der Klägerin rückständigen nachehelichen Unterhalt in Höhe von 24.081,48 EUR sA zu. Das Berufungsgericht gab der Berufung des Beklagten nicht Folge und bestätigte dieses Urteil.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Johanna Moehrlin` (person)
- `Dr. Georg Kahlig` (person)
- `Mag. Gerhard Stauder` (person)
- `DI Camilla Willoweit` (person)
- `Dr. Reinhard Schäfer` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Innere Stadt Wien` (organisation)

**Example 47** (doc_id: `deanon_260716_TRAIN/1Ob66_13g_1Ob67_13d_`) (sent_id: `deanon_260716_TRAIN/1Ob66_13g_1Ob67_13d__3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohman, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Dr. Catharina Zachow, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Dr. Grohman` (person)
- `Mag. Wurzer` (person)
- `Dr. Catharina Zachow` (person)

**Example 48** (doc_id: `deanon_260716_TRAIN/1Ob77_15b`) (sent_id: `deanon_260716_TRAIN/1Ob77_15b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Shoshana Grosse-Brockhoff, vertreten durch Dr. Günther Loibner, Rechtsanwalt in Wien, gegen die beklagte Partei Yelec Zameit, vertreten durch Dr. Markus Bernhauser, Rechtsanwalt in Wien, wegen Einwilligung in die Einverleibung des Eigentumsrechts, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 23. Dezember 2014, GZ 15 R 234/14p-32, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 26. August 2014, GZ 17 Cg 98/13a-23, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Shoshana Grosse-Brockhoff` (person)
- `Dr. Günther Loibner` (person)
- `Yelec Zameit` (person)
- `Dr. Markus Bernhauser` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 49** (doc_id: `deanon_260716_TRAIN/1Ob78_22k`) (sent_id: `deanon_260716_TRAIN/1Ob78_22k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. HR Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Familienrechtssache des Antragstellers Dr. Erhard Hörl, vertreten durch den Erwachsenenvertreter Dr. Carla Hoffner, Rechtsanwalt in Wien, gegen die Antragsgegnerin Juliana Inderwiedenstraße, vertreten durch Dr. Karl Newole, Rechtsanwalt in Wien, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. Dezember 2021, GZ 44 R 449/21m-15, mit dem der Beschluss des Bezirksgerichts Josefstadt vom 29. November 2021, GZ 25 Fam 3/21k-10, bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. HR Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Wessely-Kristöfel` (person)
- `Dr. Parzmayr` (person)
- `Dr. Erhard Hörl` (person)
- `Dr. Carla Hoffner` (person)
- `Juliana Inderwiedenstraße` (person)
- `Dr. Karl Newole` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Josefstadt` (organisation)

**Example 50** (doc_id: `deanon_260716_TRAIN/1Ob7_18p`) (sent_id: `deanon_260716_TRAIN/1Ob7_18p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Familienrechtssache des Antragstellers Hon.-Prof.in Linda Helmers, vertreten durch die GKP Gabl Kogler Leitner Stöglehner Bodingbauer Rechtsanwälte OG, Linz, gegen die Antragsgegnerin Ramona Borkert, vertreten durch die ANWALTGMBH Rinner Teuchtmann, Linz, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse nach den §§ 81 ff EheG, über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts Linz als Rekursgericht vom 15. November 2017, GZ 15 R 484/17b-10, mit dem der Beschluss des Bezirksgerichts Urfahr vom 28. September 2017, GZ 13 Fam 22/17v-5, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Hon.-Prof.in Linda Helmers` (person)
- `Bodingbauer Rechtsanwälte OG` (organisation)
- `Ramona Borkert` (person)
- `ANWALTGMBH Rinner Teuchtmann` (organisation)
- `Landesgerichts Linz` (organisation)
- `Bezirksgerichts Urfahr` (organisation)

**Example 51** (doc_id: `deanon_260716_TRAIN/1Ob80_20a`) (sent_id: `deanon_260716_TRAIN/1Ob80_20a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Kodek, Mag. Wurzer, Mag. Dr. Wurdinger und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Li Bartelsen, vertreten durch Dr. Rafaela Golda-Zajc, Rechtsanwältin in Mondsee, gegen die beklagte Partei Wieland Schnier, vertreten durch Dr. Hartmut Ramsauer, Rechtsanwalt in Salzburg, wegen Ehescheidung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts Wels als Berufungsgericht vom 4. Dezember 2019, GZ 21 R 243/19p-77, mit dem das Urteil des Bezirksgerichts Vöcklabruck vom 29. Juli 2019, GZ 48 C 13/17w-73, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Univ.-Prof. Dr. Kodek` (person)
- `Mag. Wurzer` (person)
- `Dr. Parzmayr` (person)
- `Li Bartelsen` (person)
- `Dr. Rafaela Golda-Zajc` (person)
- `Wieland Schnier` (person)
- `Dr. Hartmut Ramsauer` (person)
- `Landesgerichts Wels` (organisation)
- `Bezirksgerichts Vöcklabruck` (organisation)

**Example 52** (doc_id: `deanon_260716_TRAIN/1Ob85_16f`) (sent_id: `deanon_260716_TRAIN/1Ob85_16f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Janis Ringler, Deutschland, vertreten durch Dr. Günther Klepp und andere, Rechtsanwälte in Linz, gegen die beklagte Partei Dr. Hermine Seib, vertreten durch Mag. Dagmar Hoppstädter, Rechtsanwältin in Weißkirchen an der Traun, wegen 39.000 EUR und Vertragsaufhebung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 31. März 2016, GZ 4 R 169/15y-28, mit dem das Urteil des Landesgerichts Linz vom 19. August 2015, GZ 5 Cg 79/14h-24, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Janis Ringler` (person)
- `Dr. Günther Klepp` (person)
- `Dr. Hermine Seib` (person)
- `Mag. Dagmar Hoppstädter` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Linz` (organisation)

**Example 53** (doc_id: `deanon_260716_TRAIN/1Ob86_16b`) (sent_id: `deanon_260716_TRAIN/1Ob86_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der außerstreitigen Rechtssache des Antragstellers Ing. Nadja Ortgiese, vertreten durch Dr. Franz Marschall und Mag. René Heinz, Rechtsanwälte in Wien, gegen die Antragsgegnerin Agatha Unterdörfer, vertreten durch Dr. Hermann Heller und Mag. Bernd Gahler, Rechtsanwälte in Wien, wegen nachehelicher Vermögensaufteilung, im Verfahren über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 16. Februar 2015, GZ 44 R 15/15d-27, mit dem der Rekurs des Antragstellers gegen den Beschluss des Bezirksgerichts Döbling vom 2. Dezember 2014, GZ 7 Fam 39/14y-20, zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das Verfahren vor dem Obersten Gerichtshof ist durch Rücknahme des außerordentlichen Revisionsrekurses beendet.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Ing. Nadja Ortgiese` (person)
- `Franz Marschall und Mag` (person)
- `Agatha Unterdörfer` (person)
- `Dr. Hermann Heller` (person)
- `Mag. Bernd Gahler` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Döbling` (organisation)
- `Obersten Gerichtshof` (organisation)

**Example 54** (doc_id: `deanon_260716_TRAIN/1Ob93_17h`) (sent_id: `deanon_260716_TRAIN/1Ob93_17h_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Brechtold Textil GmbH, St. Anna Straße 10, 9564 Rottenstein, Österreich, Deutschland, vertreten durch Dr. Stefan Gulner, Rechtsanwalt in Wien, gegen die beklagte Partei ÖkR Ali Abramenko, vertreten durch die Maggi Brandl Kathollnig RechtsanwaltsGmbH-Studio Legale, Klagenfurt am Wörthersee, wegen 191.469 EUR sA, über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 10. April 2017, GZ 4 R 32/17h-28, mit dem der Beschluss des Landesgerichts Klagenfurt vom 25. Jänner 2017, GZ 49 Cg 60/14k-24, teilweise bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Brechtold Textil GmbH` (organisation)
- `St. Anna Straße 10, 9564 Rottenstein, Österreich` (address)
- `Dr. Stefan Gulner` (person)
- `ÖkR Ali Abramenko` (person)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts Klagenfurt` (organisation)

**Example 55** (doc_id: `deanon_260716_TRAIN/1Ob95_21h`) (sent_id: `deanon_260716_TRAIN/1Ob95_21h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Gawelzyk Pflege GmbH, Am See IX 247, 6320 Achleit, Österreich, vertreten durch die Zumtobel Kronberger Rechtsanwälte OG, Salzburg, gegen die beklagte Partei Loos und Woiciech Analyse GmbH, Rasenweg 21, 3441 Baumgarten am Tullnerfeld, Österreich, vertreten durch die Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH, Salzburg, wegen 135.656,39 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. April 2021, GZ 2 R 39/21z-27, mit dem das Urteil des Landesgerichts Ried im Innkreis vom 27. Jänner 2021, GZ 2 Cg 24/20i-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Gawelzyk Pflege GmbH` (organisation)
- `Am See IX 247, 6320 Achleit, Österreich` (address)
- `Zumtobel Kronberger Rechtsanwälte OG` (organisation)
- `Loos und Woiciech Analyse GmbH` (organisation)
- `Rasenweg 21, 3441 Baumgarten am Tullnerfeld, Österreich` (address)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Ried im Innkreis` (organisation)

**Example 56** (doc_id: `deanon_260716_TRAIN/4Ob226_21w`) (sent_id: `deanon_260716_TRAIN/4Ob226_21w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Schwarzenbacher als Vorsitzenden und die Hofrätinnen und Hofräte, Hon.-Prof. PD Dr. Rassi, MMag. Matzka, Dr. Faber und Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei James Skrypczik, vertreten durch Mag. Dr. Stefan Rieder, Rechtsanwalt in Salzburg, gegen die beklagte Partei G-*gesellschaft mbH, Frenzelstraße 73, 8102 Thoneben, Österreich, vertreten durch Univ.-Prof. Dr. Friedrich Harrer und Dr. Iris Harrer-Hörzinger, Rechtsanwälte in Salzburg, wegen 40.070 EUR und Feststellung (Gesamtstreitwert 45.070 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. September 2021, GZ 6 R 93/21w-69, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Stefan Rieder` | `Mag. Dr. Stefan Rieder` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schwarzenbacher` (person)
- `Hon.-Prof. PD Dr. Rassi` (person)
- `MMag. Matzka` (person)
- `Dr. Faber` (person)
- `Mag. Istjan, LL.M.` (person)
- `James Skrypczik` (person)
- `Frenzelstraße 73, 8102 Thoneben, Österreich` (address)
- `Univ.-Prof. Dr. Friedrich Harrer` (person)
- `Dr. Iris Harrer-Hörzinger` (person)
- `Oberlandesgerichts Linz` (organisation)

**Example 57** (doc_id: `deanon_260716_TRAIN/4Ob24_20p`) (sent_id: `deanon_260716_TRAIN/4Ob24_20p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Vogel als Vorsitzenden und die Hofräte Dr. Schwarzenbacher, Hon.-Prof. Dr. Brenn, Priv.-Doz. Dr. Rassi und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Parteien 1. MittelLogunitraForschung Consulting GmbH, In der Hofau 11, 3623 Leopolds, Österreich, 2. BZLB Umwelt GmbH, Lahnweg 79, 9572 Messaneggen, Österreich, beide vertreten durch Partnerschaft SCHUPPICH SPORN & WINISCHHOFER Rechtsanwälte in Wien, gegen die beklagte Partei Fennex Elektro GmbH, Rohner 20, 9470 Johannesberg, Österreich, vertreten durch PISTOTNIK & KRILYSZYN Rechtsanwälte in Wien, und die Nebenintervenientin auf Seiten der beklagten Partei Mittel Tranexber GmbH, Eichhaltweg 18, 4582 Seebach, Österreich, vertreten durch Mag. Dr. Dirk Just, Rechtsanwalt in Wien, wegen zuletzt 4.264.783,18 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. November 2019, GZ 129 R 91/19d-367, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Dirk Just` | `Mag. Dr. Dirk Just` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Vogel` (person)
- `Dr. Schwarzenbacher` (person)
- `Hon.-Prof. Dr. Brenn` (person)
- `Priv.-Doz. Dr. Rassi` (person)
- `MMag. Matzka` (person)
- `MittelLogunitraForschung Consulting GmbH` (organisation)
- `In der Hofau 11, 3623 Leopolds, Österreich` (address)
- `BZLB Umwelt GmbH` (organisation)
- `Lahnweg 79, 9572 Messaneggen, Österreich` (address)
- `SCHUPPICH SPORN & WINISCHHOFER Rechtsanwälte` (organisation)
- `Fennex Elektro GmbH` (organisation)
- `Rohner 20, 9470 Johannesberg, Österreich` (address)
- `PISTOTNIK & KRILYSZYN Rechtsanwälte` (organisation)
- `Mittel Tranexber GmbH` (organisation)
- `Eichhaltweg 18, 4582 Seebach, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)

**Example 58** (doc_id: `deanon_260716_TRAIN/6Ob2_12f`) (sent_id: `deanon_260716_TRAIN/6Ob2_12f_5`)


Alnexval Metall Manufaktur GmbH, Dir.-Mayrstraße 52, 4242 Auerbach, Österreich, 2. Kleingloms 2, 4860 Untergallaberg, Österreich, beide vertreten durch Mag. Dr. Till Hausmann, Rechtsanwalt in Wien, wegen Räumung, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 25. Oktober 2011, GZ 40 R 334/11f-49, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Mag. Dr. Till Hausmann` | `Mag. Dr. Till Hausmann` |

**Missed by this rule (FN):**

- `Alnexval Metall Manufaktur GmbH` (organisation)
- `Dir.-Mayrstraße 52, 4242 Auerbach, Österreich` (address)
- `Kleingloms 2, 4860 Untergallaberg, Österreich` (address)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 59** (doc_id: `deanon_260716_TRAIN/7Nc4_12s`) (sent_id: `deanon_260716_TRAIN/7Nc4_12s_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Huber als Vorsitzende und die Hofräte des Obersten Gerichtshofs Dr. Schaumüller, Dr. Hoch, Dr. Kalivoda und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache des Antragstellers (gefährdete Partei) Techn R Dr. Ignaz Waidlich, gegen die Antragsgegner (Gegner der gefährdeten Partei) 1.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Huber` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schaumüller` (person)
- `Dr. Hoch` (person)
- `Dr. Kalivoda` (person)
- `Techn R Dr. Ignaz Waidlich` (person)

**Example 60** (doc_id: `deanon_260716_TRAIN/7Nc6_13m`) (sent_id: `deanon_260716_TRAIN/7Nc6_13m_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Huber als Vorsitzende und die Hofrätinnen und Hofräte Dr. Hoch, Dr. Kalivoda, Mag. Dr. Wurdinger und Mag. Malesich als weitere Richter in der Arbeitsrechtssache der klagenden Partei Dr. Sabrina Dijkman, vertreten durch Dr. Clemens Gärner, Rechtsanwalt in Wien, gegen die beklagte Partei FPZE Metall AG, Jeitnerweg 110, 8773 Seiz, Österreich, vertreten durch Dr. Helmut Engelbrecht und andere Rechtsanwälte in Wien, wegen 4.868,07 EUR sA und Feststellung, über die Befangenheitsanzeige des Hofrats des Obersten Gerichtshofs Dr. Richard Hargassner im Verfahren 9 ObA 29/13z den Beschluss gefasst:  Spruch Der Hofrat des Obersten Gerichtshofs Dr. Richard Hargassner ist ausgeschlossen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Huber` (person)
- `Dr. Hoch` (person)
- `Dr. Kalivoda` (person)
- `Mag. Malesich` (person)
- `Dr. Sabrina Dijkman` (person)
- `Dr. Clemens Gärner` (person)
- `FPZE Metall AG` (organisation)
- `Jeitnerweg 110, 8773 Seiz, Österreich` (address)
- `Dr. Helmut Engelbrecht` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Richard Hargassner` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Richard Hargassner` (person)

**Example 61** (doc_id: `deanon_260716_TRAIN/7Ob110_13x`) (sent_id: `deanon_260716_TRAIN/7Ob110_13x_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Huber als Vorsitzende und die Hofrätinnen und Hofräte Dr. Hoch, Dr. Kalivoda, Mag. Dr. Wurdinger und Mag. Malesich als weitere Richter in der Rechtssache der klagenden Partei Gerdelbracht Telekom AG, KLG Gartengemeinde Adolfstor 4, 4352 Oberkalmberg, Österreich, vertreten durch Kunz Schima Wallentin Rechtsanwälte OG in Wien, gegen die beklagte Partei Mag. (FH) Franz Burgschmidt, vertreten durch Binder Grösswang Rechtsanwälte OG in Wien, wegen Erteilung von Auskünften, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. April 2013, GZ 11 R 75/13z-12, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Huber` (person)
- `Dr. Hoch` (person)
- `Dr. Kalivoda` (person)
- `Mag. Malesich` (person)
- `Gerdelbracht Telekom AG` (organisation)
- `KLG Gartengemeinde Adolfstor 4, 4352 Oberkalmberg, Österreich` (address)
- `Kunz Schima Wallentin Rechtsanwälte OG` (organisation)
- `Mag. (FH) Franz Burgschmidt` (person)
- `Binder Grösswang Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 62** (doc_id: `deanon_260716_TRAIN/7Ob112_11p`) (sent_id: `deanon_260716_TRAIN/7Ob112_11p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Huber als Vorsitzende und die Hofräte des Obersten Gerichtshofs Dr. Schaumüller, Dr. Hoch, Dr. Kalivoda und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Ing. Linn Düwel, vertreten durch Dr. Josef Lachmann, Rechtsanwalt in Wien, gegen die beklagte Partei Dr. Peter Tschoepke, vertreten durch Dr. Christine Kolbitsch, Rechtsanwältin in Wien, wegen Ehescheidung, über die außerordentliche Revision der Beklagten gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 6. April 2011, GZ 42 R 147/11w-38, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Huber` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schaumüller` (person)
- `Dr. Hoch` (person)
- `Dr. Kalivoda` (person)
- `Ing. Linn Düwel` (person)
- `Dr. Josef Lachmann` (person)
- `Dr. Peter Tschoepke` (person)
- `Dr. Christine Kolbitsch` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 63** (doc_id: `deanon_260716_TRAIN/7Ob116_22t`) (sent_id: `deanon_260716_TRAIN/7Ob116_22t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Dr. Wurdinger, Mag. Malesich, Dr. Weber und Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Hedwig Konnertz, MSc, vertreten durch Dr. Christof Joham und Mag. Andreas Voggenberger, Rechtsanwälte in Eugendorf, gegen die beklagte Partei Noruniwald KI -AG, Teichterberg 14y, 3394 Wolfstein, Österreich, vertreten durch Dr. Haymo Modelhart und andere, Rechtsanwälte in Linz, wegen 9.132,90 EUR sA und Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 5. Mai 2022, GZ 53 R 51/22i-41, womit das Urteil des Bezirksgerichts Salzburg vom 26. Jänner 2022, GZ 12 C 675/20w-37, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Solé` (person)
- `Mag. Malesich` (person)
- `Dr. Weber` (person)
- `Mag. Fitz` (person)
- `Hedwig Konnertz, MSc` (person)
- `Dr. Christof Joham` (person)
- `Mag. Andreas Voggenberger` (person)
- `Noruniwald KI -AG` (organisation)
- `Teichterberg 14y, 3394 Wolfstein, Österreich` (address)
- `Dr. Haymo Modelhart` (person)
- `Landesgerichts Salzburg` (organisation)
- `Bezirksgerichts Salzburg` (organisation)

**Example 64** (doc_id: `deanon_260716_TRAIN/7Ob129_10m`) (sent_id: `deanon_260716_TRAIN/7Ob129_10m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Huber als Vorsitzende und die Hofräte des Obersten Gerichtshofs Dr. Schaumüller, Dr. Hoch, Dr. Kalivoda und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Mario Maiers AG, Krippau 33, 5652 Dienten am Hochkönig, Österreich, vertreten durch Mag. Dr. Hans Herwig Toriser, Rechtsanwalt in Klagenfurt, gegen die beklagte Partei Merlin Paolini, vertreten durch Dr. Erich Moser, Rechtsanwalt in Murau, wegen 11.000 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 12. April 2010, GZ 2 R 45/10w-27, womit das Urteil des Landesgerichts Leoben vom 28. Jänner 2010, GZ 7 Cg 130/09k-23, bestätigt wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Mag. Dr. Hans Herwig Toriser` | `Mag. Dr. Hans Herwig Toriser` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Huber` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schaumüller` (person)
- `Dr. Hoch` (person)
- `Dr. Kalivoda` (person)
- `Dr. Grohmann` (person)
- `Mario Maiers` (person)
- `Krippau 33, 5652 Dienten am Hochkönig, Österreich` (address)
- `Merlin Paolini` (person)
- `Dr. Erich Moser` (person)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts Leoben` (organisation)

**Example 65** (doc_id: `deanon_260716_TRAIN/7Ob130_16t`) (sent_id: `deanon_260716_TRAIN/7Ob130_16t_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und durch die Hofräte Dr. Höllwerth, Mag. Dr. Wurdinger, Mag. Malesich und Dr. Singer als weitere Richter in der Sachwalterschaftssache des Betroffenen Prof. Dr. Shirley Laaken, vertreten durch den Verfahrens- und einstweiligen Sachwalter Dr. Christian Fuchshuber, LL.M., Rechtsanwalt in Innsbruck, ehemaliger Verfahrens- und einstweiliger Sachwalter Univ.-Prof. Dr. Bernhard Sandberger, vertreten durch Dr. Klaus Rinner, Rechtsanwalt in Innsbruck, den Beschluss gefasst:  Spruch Der Schriftsatz des ehemaligen Verfahrens- und einstweiligen Sachwalters vom 4. Oktober 2016 wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Dr. Höllwerth` (person)
- `Mag. Malesich` (person)
- `Dr. Singer` (person)
- `Dr. Shirley Laaken` (person)
- `Dr. Christian Fuchshuber, LL.M.` (person)
- `Dr. Bernhard Sandberger` (person)
- `Dr. Klaus Rinner` (person)

**Example 66** (doc_id: `deanon_260716_TRAIN/7Ob137_20b`) (sent_id: `deanon_260716_TRAIN/7Ob137_20b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende sowie die Hofrätin und die Hofräte Hon.-Prof. Dr. Höllwerth, Mag. Dr. Wurdinger, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Mag. Edwin Bornemeyer, vertreten durch die Pilz & Burghofer Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Thönniß Immobilien AG, Dürnstein in der Steiermark 55, 3920 Josefsdorf, Österreich, vertreten durch Mag. Dr. Otto Ranzenhofer, Rechtsanwalt in Wien, wegen 300.000 EUR sA, den Beschluss gefasst:  Spruch Das Urteil des Obersten Gerichtshofs vom 25. November 2020, AZ 7 Ob 137/20b, wird wie folgt berichtigt: Im Spruchpunkt 2. hat die Wortfolge: „samt 4 % Zinsen seit 3. 11. 2014“ zu entfallen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |
| `Mag. Dr. Otto Ranzenhofer` | `Mag. Dr. Otto Ranzenhofer` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Hon.-Prof. Dr. Höllwerth` (person)
- `Mag. Malesich` (person)
- `MMag. Matzka` (person)
- `Mag. Edwin Bornemeyer` (person)
- `Pilz & Burghofer Rechtsanwalts GmbH` (organisation)
- `Thönniß Immobilien AG` (organisation)
- `Dürnstein in der Steiermark 55, 3920 Josefsdorf, Österreich` (address)
- `Obersten Gerichtshofs` (organisation)

**Example 67** (doc_id: `deanon_260716_TRAIN/7Ob161_11v`) (sent_id: `deanon_260716_TRAIN/7Ob161_11v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Huber als Vorsitzende und die Hofräte des Obersten Gerichtshofs Dr. Schaumüller, Dr. Hoch, Dr. Kalivoda und Mag. Dr. Wurdinger als weitere Richter in den verbundenen Rechtssachen der klagenden und widerbeklagten Partei DI Wilhelm Firnekaes, vertreten durch Putz & Partner, Rechtsanwälte in Wien, gegen die beklagte und widerklagende Partei IYJW Bildung GmbH, Seeufer-Siedlung 53, 3033 Höfer, Österreich, vertreten durch die Rechtsanwälte Dr. Amhof & Dr. Damian GmbH, Wien, wegen jeweils 17.571,77 EUR (sA), über die „außerordentliche“ Revision der Beklagten gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 31. Mai 2011, GZ 3 R 42/10h-91, mit dem das Urteil des Handelsgerichts Wien vom 18. März 2010, GZ 35 Cg 42/04x (35 Cg 8/08b)-87, bestätigt wurde, den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.  Text Begründung: Der Kläger und Widerbeklagte (im Folgenden Kläger) hat im Auftrag der Beklagten und Widerklägerin (im Folgenden Beklagte) für diese Planungs- und Prüfingenieurtätigkeiten durchgeführt.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Huber` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schaumüller` (person)
- `Dr. Hoch` (person)
- `Dr. Kalivoda` (person)
- `DI Wilhelm Firnekaes` (person)
- `IYJW Bildung GmbH` (organisation)
- `Seeufer-Siedlung 53, 3033 Höfer, Österreich` (address)
- `Rechtsanwälte Dr. Amhof & Dr. Damian GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 68** (doc_id: `deanon_260716_TRAIN/7Ob172_21a`) (sent_id: `deanon_260716_TRAIN/7Ob172_21a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätin und Hofräte Mag. Dr. Wurdinger, Mag. Malesich, MMag. Matzka und Dr. Weber als weitere Richter in der Rechtssache der klagenden Partei Dr. Shirley Steidten, vertreten durch Koch Jilek Rechtsanwälte Partnerschaft in Bruck an der Mur, gegen die beklagte Partei WienMonlemalTextil Aktiengesellschaft, Ernst Wolf-Gasse 216, 4650 Schußstatt, Österreich, vertreten durch Dr. Andreas A. Lintl, Rechtsanwalt in Wien, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 15. Juli 2021, GZ 4 R 53/21b-25, womit das Urteil des Landesgerichts Leoben vom 16. Dezember 2020, GZ 5 Cg 57/19z-19, bestätigt wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Mag. Malesich` (person)
- `MMag. Matzka` (person)
- `Dr. Weber` (person)
- `Dr. Shirley Steidten` (person)
- `Koch Jilek Rechtsanwälte Partnerschaft` (organisation)
- `WienMonlemalTextil Aktiengesellschaft` (organisation)
- `Ernst Wolf-Gasse 216, 4650 Schußstatt, Österreich` (address)
- `Dr. Andreas A. Lintl` (person)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts Leoben` (organisation)

**Example 69** (doc_id: `deanon_260716_TRAIN/7Ob180_16w`) (sent_id: `deanon_260716_TRAIN/7Ob180_16w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und durch die Hofräte Dr. Höllwerth, Mag. Dr. Wurdinger, Mag. Malesich und Dr. Singer als weitere Richter in der Rechtssache der klagenden Partei Prim.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Dr. Höllwerth` (person)
- `Mag. Malesich` (person)
- `Dr. Singer` (person)

**Example 70** (doc_id: `deanon_260716_TRAIN/7Ob193_21i`) (sent_id: `deanon_260716_TRAIN/7Ob193_21i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätin und Hofräte Mag. Dr. Wurdinger, Mag. Malesich, MMag. Matzka und Dr. Weber als weitere Richter in der Rechtssache der klagenden Partei Zerweckh & Braunmöller Touristik GmbH, Albert-Böhler-Gasse 8, 9832 Stieflberg, Österreich, vertreten durch Schmid & Horn Rechtsanwälte GmbH in Graz, gegen die beklagte Partei VJHV Event Werke -AG, Oberpfälzer Weg 3, 4733 Eitzenberg, Österreich, vertreten durch Dr. Wolfgang Muchitsch, Rechtsanwalt in Graz, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 7. Oktober 2021, GZ 2 R 175/21d-15, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Mag. Malesich` (person)
- `MMag. Matzka` (person)
- `Dr. Weber` (person)
- `Zerweckh & Braunmöller Touristik GmbH` (organisation)
- `Albert-Böhler-Gasse 8, 9832 Stieflberg, Österreich` (address)
- `Schmid & Horn Rechtsanwälte GmbH` (organisation)
- `VJHV Event Werke -AG` (organisation)
- `Oberpfälzer Weg 3, 4733 Eitzenberg, Österreich` (address)
- `Dr. Wolfgang Muchitsch` (person)
- `Oberlandesgerichts Graz` (organisation)

**Example 71** (doc_id: `deanon_260716_TRAIN/7Ob201_12b`) (sent_id: `deanon_260716_TRAIN/7Ob201_12b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Dr. Huber als Vorsitzende und die Hofrätinnen und Hofräte Dr. Hoch, Dr. Kalivoda, Mag. Dr. Wurdinger und Mag. Malesich als weitere Richter in der Rechtssache der klagenden Partei Bundeskammer für Arbeiter und Angestellte, 1041 Wien, Prinz-Eugen-Straße 20-22, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Sudlex Heizung AG, Weißenbachstraße 12, 9376 Lichtegg, Österreich, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Unterlassung und Urteilsveröffentlichung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 9. November 2011, GZ 2 R 203/11d-11, womit das Urteil des Handelsgerichts Wien vom 26. Juni 2011, GZ 19 Cg 49/11v-5, teilweise abgeändert wurde, beschlossen und zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Huber` (person)
- `Dr. Hoch` (person)
- `Dr. Kalivoda` (person)
- `Mag. Malesich` (person)
- `Dr. Walter Reichholf` (person)
- `Sudlex Heizung AG` (organisation)
- `Weißenbachstraße 12, 9376 Lichtegg, Österreich` (address)
- `Schönherr Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 72** (doc_id: `deanon_260716_TRAIN/7Ob203_24i`) (sent_id: `deanon_260716_TRAIN/7Ob203_24i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Dr. Wurdinger, Mag. Malesich, Dr. Weber und Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Christina Steenfath, vertreten durch Mag. Martin Wabra, Rechtsanwalt in Gmünd, gegen die beklagte Partei SüdSanitär AG, Rechenweg 4O, 3261 Ernegg, Österreich, vertreten durch die MUSEY rechtsanwalt gmbH in Salzburg, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. Oktober 2024, GZ 5 R 144/24v-49, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Solé` (person)
- `Mag. Malesich` (person)
- `Dr. Weber` (person)
- `Mag. Fitz` (person)
- `Christina Steenfath` (person)
- `Mag. Martin Wabra` (person)
- `SüdSanitär AG` (organisation)
- `Rechenweg 4O, 3261 Ernegg, Österreich` (address)
- `MUSEY rechtsanwalt gmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 73** (doc_id: `deanon_260716_TRAIN/7Ob229_13x`) (sent_id: `deanon_260716_TRAIN/7Ob229_13x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Dr. Huber als Vorsitzende und die Hofrätinnen und Hofräte Dr. Hoch, Dr. Kalivoda, Mag. Dr. Wurdinger und Mag. Malesich als weitere Richter in der Rechtssache der klagenden Partei Kimberly Rempp, vertreten durch Dr. Peter Krassnig, Rechtsanwalt in Klagenfurt, gegen die beklagte Partei Dr. Tanja Sassenscheidt, vertreten durch Mag. Alexander Todor-Kostic, Mag. Silke Todor-Kostic, Rechtsanwälte in Velden, wegen Feststellung (in eventu Vertragsaufhebung), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 27. September 2013, GZ 5 R 79/13x-266, den Beschluss gefasst:  Spruch Der in der außerordentlichen Revision enthaltene Rekurs gegen die Verwerfung der Berufung wegen Nichtigkeit und die außerordentliche Revision werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Huber` (person)
- `Dr. Hoch` (person)
- `Dr. Kalivoda` (person)
- `Mag. Malesich` (person)
- `Kimberly Rempp` (person)
- `Dr. Peter` (person)
- `Dr. Tanja Sassenscheidt` (person)
- `Mag. Alexander Todor-Kostic` (person)
- `Mag. Silke Todor-Kostic` (person)
- `Oberlandesgerichts Graz` (organisation)

**Example 74** (doc_id: `deanon_260716_TRAIN/7Ob22_24x`) (sent_id: `deanon_260716_TRAIN/7Ob22_24x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Dr. Wurdinger, Mag. Malesich, Dr. Weber und Mag. Fitz als weitere Richter in der Rechtssache der gefährdeten Partei DI Hartwig Jullien, vertreten durch Dr. Kristina Venturini, Rechtsanwältin in Wien, gegen den Gegner der gefährdeten Partei DDr.in Juri Thias, vertreten durch Dr. Waltraud Künstl, Rechtsanwältin in Wien, wegen einstweiliger Verfügung gemäß § 382b und § 382c EO, über den außerordentlichen Revisionsrekurs des Gegners der gefährdeten Partei gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 29. Dezember 2023, GZ 16 R 312/23f-4, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO, § 78 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Solé` (person)
- `Mag. Malesich` (person)
- `Dr. Weber` (person)
- `Mag. Fitz` (person)
- `DI Hartwig Jullien` (person)
- `Dr. Kristina Venturini` (person)
- `DDr.in Juri Thias` (person)
- `Dr. Waltraud Künstl` (person)
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 75** (doc_id: `deanon_260716_TRAIN/7Ob259_10d`) (sent_id: `deanon_260716_TRAIN/7Ob259_10d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Huber als Vorsitzende und durch die Hofräte Dr. Hoch, Dr. Kalivoda, Dr. Roch und Mag. Dr. Wurdinger als weitere Richter in den verbundenen Rechtssachen der klagenden und widerbeklagten Partei Maule Digital Rechtsanwälte GmbH, Zur Fischwasserung 33, 4090 Stadl, Österreich, gegen die beklagte und widerklagende Partei Mag. Wolfgang Kojima, vertreten durch GKP Gabl Kogler Papesch Leitner Rechtsanwälte OG in Linz, wegen 63.833,25 EUR sA (Klage) und 15.000 EUR sA (Widerklage), über die außerordentliche Revision der beklagten und widerklagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 9. November 2010, GZ 15 R 64/10g-89, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Huber` (person)
- `Dr. Hoch` (person)
- `Dr. Kalivoda` (person)
- `Dr. Roch` (person)
- `Maule Digital Rechtsanwälte GmbH` (organisation)
- `Zur Fischwasserung 33, 4090 Stadl, Österreich` (address)
- `Mag. Wolfgang Kojima` (person)
- `GKP Gabl Kogler Papesch Leitner Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 76** (doc_id: `deanon_260716_TRAIN/7Ob3_16s`) (sent_id: `deanon_260716_TRAIN/7Ob3_16s_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und durch die Hofräte Dr. Höllwerth, Mag. Dr. Wurdinger, Mag. Malesich und Dr. Singer als weitere Richter in der Pflegschaftssache der Minderjährigen Marcel Dietlof, und Egon Bahnecke, Mutter Mag. Svenja Niekamp, diese vertreten durch Mag. Arno Pajek, LL.M., Rechtsanwalt in Wien, wegen Obsorge, über den außerordentlichen Revisionsrekurs des Vaters Dr. Volker Muellers, vertreten durch Mag. Walter Pirker, Rechtsanwalt in Wien, gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 27. November 2015, GZ 3 R 163/15b-550, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Dr. Höllwerth` (person)
- `Mag. Malesich` (person)
- `Dr. Singer` (person)
- `Marcel Dietlof` (person)
- `Egon Bahnecke` (person)
- `Mag. Svenja Niekamp` (person)
- `Mag. Arno Pajek, LL.M.` (person)
- `Dr. Volker Muellers` (person)
- `Mag. Walter Pirker` (person)
- `Landesgerichts Klagenfurt` (organisation)

**Example 77** (doc_id: `deanon_260716_TRAIN/7Ob4_12g`) (sent_id: `deanon_260716_TRAIN/7Ob4_12g_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Huber als Vorsitzende und die Hofräte des Obersten Gerichtshofs Dr. Schaumüller, Dr. Hoch, Dr. Kalivoda und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei UnterEnergie GmbH, Leuchterstraße 21, 8853 Seebach, Österreich, vertreten durch Dr. Roland Kometer, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Synmonwil GmbH, Nadernberg 12, 4904 Atzbach, Österreich, vertreten durch Rainer Kurbos, Rechtsanwalt in Graz, wegen 8.635,55 EUR sA, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Landesgerichts Innsbruck als Rekursgericht vom 25. Oktober 2011, GZ 1 R 84/11a-18, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Huber` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schaumüller` (person)
- `Dr. Hoch` (person)
- `Dr. Kalivoda` (person)
- `UnterEnergie GmbH` (organisation)
- `Leuchterstraße 21, 8853 Seebach, Österreich` (address)
- `Dr. Roland Kometer` (person)
- `Synmonwil GmbH` (organisation)
- `Nadernberg 12, 4904 Atzbach, Österreich` (address)
- `Rainer Kurbos` (person)
- `Landesgerichts Innsbruck` (organisation)

**Example 78** (doc_id: `deanon_260716_TRAIN/7Ob85_15y`) (sent_id: `deanon_260716_TRAIN/7Ob85_15y_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und durch die Hofräte Dr. Höllwerth, Mag. Dr. Wurdinger, Mag. Malesich und Dr. Singer als weitere Richter in der Rechtssache der klagenden Partei Volkmar Hojnatzki, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft in Wien, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wurdinger` | `Mag. Dr. Wurdinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Dr. Höllwerth` (person)
- `Mag. Malesich` (person)
- `Dr. Singer` (person)
- `Volkmar Hojnatzki` (person)
- `Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft` (organisation)

**Example 79** (doc_id: `deanon_260716_TRAIN/8Ob39_24d`) (sent_id: `deanon_260716_TRAIN/8Ob39_24d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Tarmann-Prentner als Vorsitzende sowie die Hofräte MMag. Matzka, Dr. Stefula, Dr. Thunhart und Mag. Dr. Sengstschmid als weitere Richter in der Rechtssache der klagenden Partei Helena Seuboth, vertreten durch Mag. Dieter Koch, Rechtsanwalt in Bruck an der Mur, gegen die beklagte Partei Springl Technik GmbH Josef-Weber-Straße 87h, 2565 Schwechatbach, Österreich, vertreten durch die DORDA Rechtsanwälte GmbH in Wien, wegen 112.655,74 EUR sA, über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. Februar 2024, GZ 2 R 8/24z-20.2, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Sengstschmid` | `Mag. Dr. Sengstschmid` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Tarmann-Prentner` (person)
- `MMag. Matzka` (person)
- `Dr. Stefula` (person)
- `Dr. Thunhart` (person)
- `Helena Seuboth` (person)
- `Mag. Dieter Koch` (person)
- `Springl Technik GmbH` (organisation)
- `Josef-Weber-Straße 87h, 2565 Schwechatbach, Österreich` (address)
- `DORDA Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Graz` (organisation)

**Example 80** (doc_id: `deanon_260716_TRAIN/8Ob94_14b`) (sent_id: `deanon_260716_TRAIN/8Ob94_14b_4`)


Karsten Straehler, 2. Mag. Dr. Noel Seidenzahl, ebendort, beide vertreten durch Dr. Michael Günther, Rechtsanwalt in Wien, gegen die beklagte Partei Anneliese Schoellhammer, vertreten durch Dr. Peter Wagner, Rechtsanwalt in Wien, wegen Räumung, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 13. Juni 2014, GZ 39 R 121/14d-76, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Mag. Dr. Noel Seidenzahl` | `Mag. Dr. Noel Seidenzahl` |

**Missed by this rule (FN):**

- `Karsten Straehler` (person)
- `Dr. Michael Günther` (person)
- `Anneliese Schoellhammer` (person)
- `Dr. Peter Wagner` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 81** (doc_id: `deanon_260716_TRAIN/8Ob97_23g`) (sent_id: `deanon_260716_TRAIN/8Ob97_23g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner und die Hofräte MMag. Matzka, Dr. Stefula und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Ost Unibersud GmbH, Am Hochberg 13, 7304 Kleinwarasdorf, Österreich, vertreten durch Dr. Hanno Hofmann, Rechtsanwalt in Graz, gegen die beklagte Partei Debald KI GmbH, Josef Lienhart-Weg 46, 3542 Reisling, Österreich, vertreten durch Mag. Dr. Günther Schmied, Rechtsanwalt in Graz, wegen Übergabeauftrags, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 21. Juni 2023, GZ 5 R 26/23i-49, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Graz-West vom 29. Dezember 2022, GZ 111 C 5/22w-45, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Mag. Dr. Günther Schmied` | `Mag. Dr. Günther Schmied` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Kuras` (person)
- `Dr. Tarmann-Prentner` (person)
- `MMag. Matzka` (person)
- `Dr. Stefula` (person)
- `Dr. Thunhart` (person)
- `Ost Unibersud GmbH` (organisation)
- `Am Hochberg 13, 7304 Kleinwarasdorf, Österreich` (address)
- `Dr. Hanno Hofmann` (person)
- `Debald KI GmbH` (organisation)
- `Josef Lienhart-Weg 46, 3542 Reisling, Österreich` (address)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)
- `Bezirksgerichts Graz-West` (organisation)

**Example 82** (doc_id: `deanon_260716_TRAIN/8ObA10_12x`) (sent_id: `deanon_260716_TRAIN/8ObA10_12x_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Spenling als Vorsitzenden, die Hofräte Hon.-Prof. Dr. Kuras und Mag. Ziegelbauer sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner und Mag. Manuela Majeranowski als weitere Richter in der Arbeitsrechtssache der klagenden Partei Techn R Laurin Tommke, vertreten durch Hasch & Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Zorlex Verlag Gesellschaft mbH, Poeschlstraße 16, 4904 Hippelsberg, Österreich, vertreten durch Mag. Klaus F. Lughofer LLM, Rechtsanwalt in Linz, wegen Feststellung (Streitwert: 30.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. November 2011, GZ 11 Ra 92/11w-10, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Linz als Arbeits- und Sozialgericht vom 31. August 2011, GZ 11 Cga 101/11d-5, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Mag. Dr. Rolf Gleißner` | `Mag. Dr. Rolf Gleißner` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Spenling` (person)
- `Hon.-Prof. Dr. Kuras` (person)
- `Mag. Ziegelbauer` (person)
- `Mag. Manuela Majeranowski` (person)
- `Techn R Laurin Tommke` (person)
- `Hasch & Partner Anwaltsgesellschaft mbH` (organisation)
- `Zorlex Verlag Gesellschaft mbH` (organisation)
- `Poeschlstraße 16, 4904 Hippelsberg, Österreich` (address)
- `Mag. Klaus F. Lughofer LLM` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Linz` (organisation)

**Example 83** (doc_id: `deanon_260716_TRAIN/8ObA18_17f`) (sent_id: `deanon_260716_TRAIN/8ObA18_17f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Brenn als weitere Richter sowie die fachkundigen Laienrichter Mag. Dr. Bernhard Gruber und Harald Kohlruss in der Arbeitsrechtssache der klagenden Partei MedR Clemens Schepper, vertreten durch Freimüller/Obereder/Pilz Rechtsanwält_innen GmbH in Wien, gegen die beklagte Partei Muehleis & Klaese Technik AG, Rosentaler Weg 2k, 9811 St. Peter in Holz, Österreich, vertreten durch DLA Piper Weiss-Tessbach Rechtsanwälte GmbH in Wien, wegen Feststellung (Streitwert 282,56 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. November 2016, GZ 7 Ra 90/16f-19, mit dem das Urteil des Arbeits- und Sozialgerichts Wien vom 20. Juli 2016, GZ 33 Cga 50/16p-15, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Mag. Dr. Bernhard Gruber` | `Mag. Dr. Bernhard Gruber` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Prof. Dr. Spenling` (person)
- `Dr. Tarmann-Prentner` (person)
- `Dr. Brenn` (person)
- `Harald Kohlruss` (person)
- `MedR Clemens Schepper` (person)
- `Freimüller/Obereder/Pilz Rechtsanwält_innen GmbH` (organisation)
- `Muehleis & Klaese Technik AG` (organisation)
- `Rosentaler Weg 2k, 9811 St. Peter in Holz, Österreich` (address)
- `DLA Piper Weiss-Tessbach Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 84** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden und die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn sowie die fachkundigen Laienrichter Mag. Dr. Monika Lanz und Wolfgang Cadilek als weitere Richter in der Arbeitsrechtssache der klagenden Partei Hon.-Prof. Dieter Kovacs, vertreten durch Pfurtscheller Orgler Huber, Rechtsanwälte in Innsbruck, gegen die beklagte Partei ÖBB-Personenverkehr AG, Monsbergergasse 12, 6210 Astenberg, Österreich, vertreten durch die CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 3.963,75 EUR brutto sA, aus Anlass der (außerordentlichen) Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. Februar 2013, GZ 13 Ra 1/13i-16, mit dem das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 16. Oktober 2012, GZ 42 Cga 87/12h-12, abgeändert wurde, den Beschluss gefasst:  Spruch A.Dem Gerichtshof der Europäischen Union werden folgende Fragen zur Vorabentscheidung vorgelegt: 1.Ist Art 21 der Grundrechtecharta in Verbindung mit Art 7 Abs 1, Art 16 und Art 17 der Richtlinie 2000/78/EG dahin auszulegen, dass a)ein Arbeitnehmer, für den vom Arbeitgeber aufgrund einer gesetzlich normierten altersdiskriminierenden Anrechnung von Vordienstzeiten zunächst ein unrichtiger Vorrückungsstichtag festgesetzt wurde, in jedem Fall Anspruch auf Zahlung der Gehaltsdifferenz unter Zugrundelegung des diskriminierungsfreien Vorrückungsstichtags hat, b)oder aber dahin, dass der Mitgliedstaat die Möglichkeit hat, durch eine diskriminierungsfreie Anrechnung der Vordienstzeiten die Altersdiskriminierung auch ohne finanziellen Ausgleich (durch Neufestsetzung des Vorrückungsstichtags bei gleichzeitiger Verlängerung des Vorrückungszeitraums) zu beseitigen, insbesondere wenn diese entgeltneutrale Lösung die Liquidität des Arbeitgebers aufrechterhalten sowie einen übermäßigen Neuberechnungsaufwand vermeiden soll?

| Predicted | Gold |
|---|---|
| `Mag. Dr. Monika Lanz` | `Mag. Dr. Monika Lanz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Spenling` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kuras` (person)
- `Dr. Brenn` (person)
- `Wolfgang Cadilek` (person)
- `Hon.-Prof. Dieter Kovacs` (person)
- `Pfurtscheller Orgler Huber, Rechtsanwälte` (organisation)
- `ÖBB-Personenverkehr AG` (organisation)
- `Monsbergergasse 12, 6210 Astenberg, Österreich` (address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Innsbruck` (organisation)
- `Landesgerichts Innsbruck` (organisation)

**Example 85** (doc_id: `deanon_260716_TRAIN/8ObA27_16b`) (sent_id: `deanon_260716_TRAIN/8ObA27_16b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten des Obersten Gerichtshofs Prof. Dr. Spenling als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Brenn sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner und Wolfgang Cadilek als weitere Richter in der Arbeitsrechtssache der klagenden Partei ICZK Lebensmittel GesmbH, Zur Wasserkaserne 11, 4743 Böcklarn, Österreich, vertreten durch Dr. Alexander Milavec, Rechtsanwalt in Wien, gegen die beklagte Partei Dworzak + Lüdeker Garten Gesellschaft mbH, Seeweingärten I 4, 5574 Göriach, Österreich, vertreten durch die Jirovec & Partner Rechtsanwalts GmbH in Wien, wegen 1.450 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 18. Februar 2016, GZ 8 Ra 69/15y-24, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO iVm § 2 Abs 1 ASGG).

| Predicted | Gold |
|---|---|
| `Mag. Dr. Rolf Gleißner` | `Mag. Dr. Rolf Gleißner` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Spenling` (person)
- `Dr. Tarmann-Prentner` (person)
- `Dr. Brenn` (person)
- `Wolfgang Cadilek` (person)
- `ICZK Lebensmittel GesmbH` (organisation)
- `Zur Wasserkaserne 11, 4743 Böcklarn, Österreich` (address)
- `Dr. Alexander Milavec` (person)
- `Dworzak + Lüdeker Garten Gesellschaft mbH` (organisation)
- `Seeweingärten I 4, 5574 Göriach, Österreich` (address)
- `Jirovec & Partner Rechtsanwalts GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 86** (doc_id: `deanon_260716_TRAIN/8ObA52_24s`) (sent_id: `deanon_260716_TRAIN/8ObA52_24s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch die Senatspräsidentin Dr. Tarmann-Prentner als Vorsitzende, die Hofräte MMag. Matzka und Mag. Dr. Sengstschmid sowie die fachkundigen Laienrichter Johannes Püller (aus dem Kreis der Arbeitgeber) und Alexander Leitner (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Maria Zedelmaier, vertreten durch Mag. Harald Lajlar, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Medien Sudvergart GmbH, Rainbacher Straße 93I, 3525 Rabenhof, Österreich, vertreten durch Dr. Peter Klaunzer, Rechtsanwalt in Innsbruck, wegen 67.966,83 EUR brutto und 1.705,45 EUR netto sA sowie Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 26. September 2024, GZ 15 Ra 18/24w-40, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Sengstschmid` | `Mag. Dr. Sengstschmid` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Tarmann-Prentner` (person)
- `MMag. Matzka` (person)
- `Johannes Püller` (person)
- `Maria Zedelmaier` (person)
- `Mag. Harald Lajlar` (person)
- `Medien Sudvergart GmbH` (organisation)
- `Rainbacher Straße 93I, 3525 Rabenhof, Österreich` (address)
- `Dr. Peter Klaunzer` (person)
- `Oberlandesgerichts Innsbruck` (organisation)

**Example 87** (doc_id: `deanon_260716_TRAIN/8ObA74_19v`) (sent_id: `deanon_260716_TRAIN/8ObA74_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Wessely-Kristöfel als weitere Richter sowie die fachkundigen Laienrichter Mag. Thomas Stegmüller (aus dem Kreis der Arbeitgeber) und Gerald Fida (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Mag. OStR Dipl. Kfm. Albert Jellinek, vertreten durch Mag. Dr. Johannes Winkler, Rechtsanwalt in Linz, gegen die beklagte Partei Rhein Trazor GmbH, Erste Straße 10, 5151 Gastein, Österreich, vertreten durch MM Metzler & Musel Rechtsanwälte GmbH in Linz, wegen 18.229,17 EUR brutto sA und Ausstellung eines Dienstzeugnisses, über die außerordentliche Revision der klagenden Partei (Revisionsinteresse 18.229,17 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 28. Oktober 2019, GZ 11 Ra 63/19t-15, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Johannes Winkler` | `Mag. Dr. Johannes Winkler` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Kuras` (person)
- `Dr. Tarmann-Prentner` (person)
- `Mag. Wessely-Kristöfel` (person)
- `Mag. Thomas Stegmüller` (person)
- `Gerald Fida` (person)
- `Mag. OStR Dipl. Kfm. Albert Jellinek` (person)
- `Rhein Trazor GmbH` (organisation)
- `Erste Straße 10, 5151 Gastein, Österreich` (address)
- `MM Metzler & Musel Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Linz` (organisation)

**Example 88** (doc_id: `deanon_260716_TRAIN/9Ob16_16t`) (sent_id: `deanon_260716_TRAIN/9Ob16_16t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin Hon.-Prof. Dr. Dehn, den Hofrat Dr. Hargassner und die Hofrätin Mag. Korn und den Hofrat Dr. Gitschthaler als weitere Richter in der Rechtssache der klagenden Partei Marianne Adamske, vertreten durch Mag. Emanuel Boesch, Rechtsanwalt in Wien, gegen die beklagten Partei Tosca Beilhack, vertreten durch Mag. Dr. Martin Deuretsbacher, Rechtsanwalt in Wien, wegen 54.610,57 EUR sA, über die außerordentliche Revision der beklagten Partei (Revisionsinteresse 52.758,30 EUR sA) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. Februar 2016, GZ 15 R 183/15i-95, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Martin Deuretsbacher` | `Mag. Dr. Martin Deuretsbacher` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Hon.-Prof. Dr. Dehn` (person)
- `Dr. Hargassner` (person)
- `Mag. Korn` (person)
- `Dr. Gitschthaler` (person)
- `Marianne Adamske` (person)
- `Mag. Emanuel Boesch` (person)
- `Tosca Beilhack` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 89** (doc_id: `deanon_260716_TRAIN/9Ob20_20m`) (sent_id: `deanon_260716_TRAIN/9Ob20_20m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätinnen und Hofräte des Obersten Gerichtshofs Dr. Fichtenau, Dr. Hargassner, Mag. Korn und Dr. Stefula in der Rechtssache der klagenden Partei Mag. Dr. Serena Morgenbrod, vertreten durch TELOS Law Group Winalek, Nikodem, Weinzinger, Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Dr. Frederike Luebcke, vertreten durch tws Rechtsanwälte og in St. Pölten, wegen 10.010 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts St. Pölten als Berufungsgericht vom 22. Jänner 2020, GZ 21 R 241/19b-38, mit dem der Berufung der klagenden Partei gegen das Urteil des Bezirksgerichts Melk vom 23. Mai 2019, GZ 20 C 28/18g-34, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision der klagenden Partei wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Serena Morgenbrod` | `Mag. Dr. Serena Morgenbrod` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Fichtenau` (person)
- `Dr. Hargassner` (person)
- `Mag. Korn` (person)
- `Dr. Stefula` (person)
- `Dr. Frederike Luebcke` (person)
- `Landesgerichts St. Pölten` (organisation)
- `Bezirksgerichts Melk` (organisation)

**Example 90** (doc_id: `deanon_260716_TRAIN/9Ob57_22f`) (sent_id: `deanon_260716_TRAIN/9Ob57_22f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende, die Hofrätinnen und Hofräte des Obersten Gerichtshofs Mag. Ziegelbauer, Dr. Dehn, Dr. Hargassner und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Esra Rötker, vertreten durch Mag. Dr. Alfred Wansch, Rechtsanwalt in Wien, gegen die beklagte Partei OberMöbel GmbH, Herderplatz 35, 4722 Rittberg, Österreich, vertreten durch Mag. Johannes Zach, Rechtsanwalt in Weigelsdorf, wegen Zuhaltung eines Mietvertrags (Streitwert 3.000 EUR), über die „außerordentliche Revision“ der beklagten Partei gegen das Urteil des Landesgerichts Korneuburg als Berufungsgericht vom 8. März 2022, GZ 22 R 364/21s-39, mit dem das Urteil des Bezirksgerichts Schwechat vom 15. Juni 2021, GZ 3 C 60/20d-33, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Alfred Wansch` | `Mag. Dr. Alfred Wansch` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Fichtenau` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Ziegelbauer` (person)
- `Dr. Dehn` (person)
- `Dr. Hargassner` (person)
- `Mag. Korn` (person)
- `Esra Rötker` (person)
- `OberMöbel GmbH` (organisation)
- `Herderplatz 35, 4722 Rittberg, Österreich` (address)
- `Mag. Johannes Zach` (person)
- `Landesgerichts Korneuburg` (organisation)
- `Bezirksgerichts Schwechat` (organisation)

**Example 91** (doc_id: `deanon_260716_TRAIN/9ObA109_13i`) (sent_id: `deanon_260716_TRAIN/9ObA109_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras, die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner und Mag. Thomas Kallab als weitere Richter in der Arbeitsrechtssache der klagenden Partei PhD Mag.a Traude Eyssner, gegen die beklagte Partei Mag. Siegmund Liepinsky, vertreten durch Hochleitner Rechtsanwälte GmbH in Linz, wegen 3.674,41 EUR brutto abzüglich 181,96 EUR netto sA (Revisionsinteresse 1.572,49 EUR brutto sA), über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 23. Mai 2013, GZ 8 Ra 36/13t-44, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Mag. Dr. Rolf Gleißner` | `Mag. Dr. Rolf Gleißner` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kuras` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Dehn` (person)
- `Mag. Thomas Kallab` (person)
- `PhD Mag.a Traude Eyssner` (person)
- `Mag. Siegmund Liepinsky` (person)
- `Hochleitner Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 92** (doc_id: `deanon_260716_TRAIN/9ObA30_19f`) (sent_id: `deanon_260716_TRAIN/9ObA30_19f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätinnen Hon.-Prof. Dr. Dehn und Mag. Korn sowie die fachkundigen Laienrichter Mag. Dr. Bernhard Gruber und ADir.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Bernhard Gruber` | `Mag. Dr. Bernhard Gruber` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Hon.-Prof. Dr. Dehn` (person)
- `Mag. Korn` (person)

**Example 93** (doc_id: `deanon_260716_TRAIN/9ObA55_12x`) (sent_id: `deanon_260716_TRAIN/9ObA55_12x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten des Obersten Gerichtshofs Dr. Rohrer als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Hopf, die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Mag. Dr. Wolfgang Höfle und Dr. Peter Schnöller in der Arbeitsrechtssache der klagenden Partei KommR Svetlana Burgholt, vertreten durch Dr. Gerhard Hiebler, Dr. Gerd Grebenjak, Rechtsanwälte in Leoben, wider die beklagte Partei Katharina Hoentzsch GmbH, Kirchtratten 6, 3386 Weghof, Österreich, vertreten durch Dr. Annemarie Stipanitz-Schreiner, Dr. Helmut Klement, Rechtsanwälte in Graz, wegen 56.109 EUR sA, infolge der außerordentlichen Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 24. Februar 2012, GZ 6 Ra 85/11h-31, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Mag. Dr. Wolfgang Höfle` | `Mag. Dr. Wolfgang Höfle` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Rohrer` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Dehn` (person)
- `Dr. Peter Schnöller` (person)
- `KommR Svetlana Burgholt` (person)
- `Dr. Gerhard Hiebler` (person)
- `Dr. Gerd Grebenjak` (person)
- `Katharina Hoentzsch` (person)
- `Kirchtratten 6, 3386 Weghof, Österreich` (address)
- `Dr. Annemarie Stipanitz-Schreiner` (person)
- `Dr. Helmut Klement` (person)
- `Oberlandesgerichts Graz` (organisation)

**Example 94** (doc_id: `deanon_260716_TRAIN/9ObA76_13m`) (sent_id: `deanon_260716_TRAIN/9ObA76_13m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras, die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner und Mag. Ernst Bassler als weitere Richter in der Arbeitsrechtssache der klagenden Partei Adrian Leiße, BSc, vertreten durch Dr. H. Burmann ua, Rechtsanwälte in Innsbruck, gegen die beklagten Parteien 1. Logkraft-Verlag GmbH & Co KG, 2.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Rolf Gleißner` | `Mag. Dr. Rolf Gleißner` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kuras` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Dehn` (person)
- `Mag. Ernst` (person)
- `Adrian Leiße, BSc` (person)
- `Logkraft-Verlag GmbH & Co KG` (organisation)

**Example 95** (doc_id: `deanon_260716_TRAIN/9ObA82_20d`) (sent_id: `deanon_260716_TRAIN/9ObA82_20d_3`)


Kopf Der Oberste Gerichtshof hat als Revisions- und Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau und den Hofrat des Obersten Gerichtshofs Dr. Hargassner sowie die fachkundigen Laienrichter Mag. Dr. Bernhard Gruber (aus dem Kreis der Arbeitgeber) und Angela Taschek (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Marktgemeinde KommR KommR Piedro Leyendecker, vertreten durch Ehrenhöfer & Häusler Rechtsanwälte GmbH in Wiener Neustadt, gegen die beklagte Partei Milena Leinhaas, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, wegen 28.428,01 EUR sA, über den Rekurs und die außerordentliche Revision der klagenden Partei gegen den Beschluss (I.) und das Urteil (II.) des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 22. Juli 2020, GZ 9 Ra 111/19p-25, mit dem das Urteil des Landesgerichts Wiener Neustadt als Arbeits- und Sozialgericht vom 17. September 2019, GZ 9 Cga 126/18g-21, aus Anlass der Berufung der beklagten Partei hinsichtlich der Rückforderung einer Zahlung als nichtig aufgehoben und die Klage zurückgewiesen wurde und über Berufung der beklagen Partei hinsichtlich des Anspruchs nach dem OrgHG abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird teilweise Folge gegeben und der angefochtene Beschluss des Berufungsgerichts ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Bernhard Gruber` | `Mag. Dr. Bernhard Gruber` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Fichtenau` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hargassner` (person)
- `KommR KommR Piedro Leyendecker` (person)
- `Ehrenhöfer & Häusler Rechtsanwälte GmbH` (organisation)
- `Milena Leinhaas` (person)
- `Kosch & Partner Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 96** (doc_id: `deanon_260716_TRAIN/9ObA8_20x`) (sent_id: `deanon_260716_TRAIN/9ObA8_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau und den Hofrat des Obersten Gerichtshofs Dr. Hargassner sowie die fachkundigen Laienrichter Dr. Ingomar Stupar (aus dem Kreis der Arbeitgeber) und Mag. Werner Pletzenauer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Mag. Dr. Hartmut Sperber, vertreten durch Moser Mutz Rechtsanwälte GesbR in Klagenfurt am Wörthersee, gegen die beklagte Partei HASK Software Betriebe AG, Alter Garten 34, 8490 Hummersdorf, Österreich, vertreten durch Wiedenbauer Mutz Winkler & Partner Rechtsanwälte GmbH in Klagenfurt am Wörthersee, wegen Kündigungsanfechtung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 18. Dezember 2019, GZ 7 Ra 70/19x-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Hartmut Sperber` | `Mag. Dr. Hartmut Sperber` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Fichtenau` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hargassner` (person)
- `Dr. Ingomar Stupar` (person)
- `Mag. Werner` (person)
- `Moser Mutz Rechtsanwälte GesbR` (organisation)
- `HASK Software Betriebe AG` (organisation)
- `Alter Garten 34, 8490 Hummersdorf, Österreich` (address)
- `Wiedenbauer Mutz Winkler & Partner Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Graz` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/9Ob27_18p`) (sent_id: `deanon_260716_TRAIN/9Ob27_18p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsrekursgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Dehn, Dr. Hargassner, Mag. Korn und Dr. Stefula in der Rechtssache der klagenden Partei Thilo Aust, vertreten durch Mag. Dr. Surena Ettefagh, Rechtsanwalt in Frastanz, gegen die beklagte Partei Milan Turnherr, vertreten durch Achammer & Mennel Rechtsanwälte OG in Feldkirch, wegen Feststellung, Löschung von Grundbuchseintragungen und Räumung (Streitwert: 19.440 EUR sA), über den Revisionsrekurs der beklagten Partei gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 18. Jänner 2018, GZ 1 R 8/18m-150, mit dem der Rekurs der beklagten Partei gegen den Beschluss des Bezirksgerichts Bezau vom 30. Oktober 2015, GZ 5 C 39/14w-86, zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Mag. Dr. Surena Ettefagh` — partial — gold is substring of pred: `Dr. Surena Ettefagh`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hopf`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Dehn`(person)
- `Dr. Hargassner`(person)
- `Mag. Korn`(person)
- `Dr. Stefula`(person)
- `Thilo Aust`(person)
- `Dr. Surena Ettefagh`(person)
- `Milan Turnherr`(person)
- `Achammer & Mennel Rechtsanwälte OG`(organisation)
- `Landesgerichts Feldkirch`(organisation)
- `Bezirksgerichts Bezau`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/9ObA118_18w`) (sent_id: `deanon_260716_TRAIN/9ObA118_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Hon.-Prof. Dr. Dehn, den Hofrat des Obersten Gerichtshofs Dr. Hargassner sowie die fachkundigen Laienrichter Mag. Dr. Ingomar Stupar und ADir.

**False Positives:**

- `Mag. Dr. Ingomar Stupar` — partial — gold is substring of pred: `Dr. Ingomar Stupar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hopf`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Dehn`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hargassner`(person)
- `Dr. Ingomar Stupar`(person)

**Example 2** (doc_id: `deanon_260716_TRAIN/9ObA18_19s`) (sent_id: `deanon_260716_TRAIN/9ObA18_19s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Hon.-Prof. Dr. Dehn und den Hofrat des Obersten Gerichtshofs Dr. Hargassner sowie die fachkundigen Laienrichter Mag. Dr. Ingomar Stupar und ADir.

**False Positives:**

- `Mag. Dr. Ingomar Stupar` — partial — gold is substring of pred: `Dr. Ingomar Stupar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hopf`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Dehn`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hargassner`(person)
- `Dr. Ingomar Stupar`(person)

</details>

---

## `Hyphenated Surname` 🏆

**F1:** 0.739 | **Precision:** 0.943 | **Recall:** 0.608  

**Format:** `regex`  
**Rule ID:** `2b8414a9`  
**Description:**
Specifically targets hyphenated surnames (e.g., Bachner-Foregger, Hofer-Zeni-Rennhofer) following titles or in lists to ensure the full name is captured.

**Content:**
```
(?:Dr\.|Mag\.|Prof\.|MMag\.|Ing\.|DI\.|PhD\.|Dipl\.-Ing\.|Bakk\.\s+iur\.|MBA|BSc|LL\.M\.|Hon\.-Prof\.|Univ\.-Prof\.|Priv\.-Doz\.|PD|OMedR|HR|VetR|Techn|StR|OStR|KR|AR|RgR|ÖkR)\s+([A-Z][a-zäöüß]+(?:\s*[A-Z][a-zäöüß]+)*(?:\s*-[A-Z][a-zäöüß]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.943 | 0.608 | 0.739 | 2692 | 2539 | 153 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2539 | 153 | 1636 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Jason Langeloh, vertreten durch die Mag. Martin Rützler, Rechtsanwalt in Dornbirn, gegen die beklagte Partei, Selma Einoeder, vertreten durch Mag. Alexander Gerngross und Mag. Klaus Köck, Rechtsanwälte in Premstätten bei Graz, wegen 6.795,66 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 223 C 1313/24w des Bezirksgerichts Graz-Ost den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an das Bezirksgericht Dornbirn wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Schober` | `Mag. Schober` |
| `Dr. Vollmaier` | `Dr. Vollmaier` |
| `Mag. Martin Rützler` | `Mag. Martin Rützler` |
| `Mag. Alexander Gerngross` | `Mag. Alexander Gerngross` |
| `Mag. Klaus Köck` | `Mag. Klaus Köck` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Jason Langeloh` (person)
- `Selma Einoeder` (person)
- `Bezirksgerichts Graz-Ost` (organisation)
- `Bezirksgericht Dornbirn` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Kordelia Meelis, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Fatima Tengel, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Dr. Grohmann` | `Dr. Grohmann` |
| `Mag. Ernst Michael Lang` | `Mag. Ernst Michael Lang` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Kordelia Meelis` (person)
- `Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft` (organisation)
- `Fatima Tengel` (person)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der beim Landesgericht Linz zu AZ 3 Cg 46/21a anhängigen Rechtssache der klagenden Partei Hollengk Planung GmbH, Am Steindl 3, 9873 Döbriach, Österreich, vertreten durch Huber Berchtold Rechtsanwälte OG in Wien, gegen die beklagte Partei Wind Nexheimval GmbH, Wiesbergsiedlung 4, 8341 Pöllau, Österreich, vertreten durch ScherbaumSeebacher Rechtsanwälte GmbH in Graz, wegen 188.117,55 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN folgenden Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, zur Verhandlung und Entscheidung der Rechtssache anstelle des Landesgerichts Linz das Landesgericht Korneuburg zu bestimmen, wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Dr. Grohmann` | `Dr. Grohmann` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Landesgericht Linz` (organisation)
- `Hollengk Planung GmbH` (organisation)
- `Am Steindl 3, 9873 Döbriach, Österreich` (address)
- `Huber Berchtold Rechtsanwälte OG` (organisation)
- `Wind Nexheimval GmbH` (organisation)
- `Wiesbergsiedlung 4, 8341 Pöllau, Österreich` (address)
- `ScherbaumSeebacher Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Linz` (organisation)
- `Landesgericht Korneuburg` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Schramm als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Florens Drehkopf, LLB, geboren am 16. Dezember 1952, AZ 7 P 203/15g des Bezirksgerichts Mödling, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Mödling zurückgestellt.  Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

| Predicted | Gold |
|---|---|
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Florens Drehkopf, LLB` (person)
- `16. Dezember 1952` (date)
- `Bezirksgerichts Mödling` (organisation)
- `Bezirksgericht Mödling` (organisation)
- `Bezirksgericht Mödling` (organisation)
- `Bezirksgericht Judenburg` (organisation)
- `Bezirksgerichts Judenburg` (organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Marlene Friss, Russische Föderation, gegen die verpflichtete Partei WestTelekom GmbH, Rehwald 11, 4723 Fronberg, Österreich, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hradil` | `Dr. Hradil` |
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Hoch` | `Dr. Hoch` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Marlene Friss` (person)
- `WestTelekom GmbH` (organisation)
- `Rehwald 11, 4723 Fronberg, Österreich` (address)
- `Bezirksgericht Innere Stadt Wien` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und die Hofräte Dr. Fellinger und Dr. Schramm als weitere Richter in der Pflegschaftssache der Minderjährigen Gerhard Lohrmann, geboren am 10. August 1983, und Veit Künneken, geboren am 31. Mai 1967, AZ 2 PS 117/09t des Bezirksgerichts Feldkirchen, infolge Vorlage zur Genehmigung der Übertragung gemäß § 111 JN an das Bezirksgericht Neunkirchen, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Übertragung der Zuständigkeit zur Besorgung dieser Pflegschaftssache an das Bezirksgericht Neunkirchen wird genehmigt.

| Predicted | Gold |
|---|---|
| `Dr. Schinko` | `Dr. Schinko` |
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Schramm` | `Dr. Schramm` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Gerhard Lohrmann` (person)
- `10. August 1983` (date)
- `Veit Künneken` (person)
- `31. Mai 1967` (date)
- `Bezirksgerichts Feldkirchen` (organisation)
- `Bezirksgericht Neunkirchen` (organisation)
- `Bezirksgericht Neunkirchen` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen Selma Eichler, LLM, geboren 13. September 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt. Begründung:  Rechtliche Beurteilung [1] Mit Beschluss vom 12.

| Predicted | Gold |
|---|---|
| `Dr. Nowotny` | `Dr. Nowotny` |
| `Mag. Ziegelbauer` | `Mag. Ziegelbauer` |
| `Dr. Faber` | `Dr. Faber` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Selma Eichler, LLM` (person)
- `13. September` (date)
- `Bezirksgerichts Graz-West` (organisation)
- `Bezirksgericht Graz-West` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Ober-Automotive GmbH, Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei Katharina Rothschadl, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hradil` | `Dr. Hradil` |
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Hoch` | `Dr. Hoch` |
| `Mag. Alexander Rimser` | `Mag. Alexander Rimser` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Ober-Automotive GmbH` (organisation)
- `Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich` (address)
- `Katharina Rothschadl` (person)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin mj Dietlind Schiewick, geboren 23. Oktober 2017, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Vöcklabruck, 4840 Vöcklabruck, Sportplatzstraße 1–3), deren Mutter Gisela Akcakaya, MSc, und des Antragsgegners Ernst Hartjens, Russische Föderation, wegen Feststellung der Abstammung, aufgrund der vom Bezirksgericht Josefstadt verfügten Vorlage des Akts AZ 23 Fam 2/21y zur Entscheidung gemäß § 111 Abs 2 JN den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Villach zurückgestellt.  Text Begründung: [1] Gegenstand des Verfahrens ist der Antrag auf Feststellung der Abstammung der zum Zeitpunkt der Antragstellung am 24.

| Predicted | Gold |
|---|---|
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Mag. Ziegelbauer` | `Mag. Ziegelbauer` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dietlind Schiewick` (person)
- `23. Oktober` (date)
- `Bezirkshauptmannschaft Vöcklabruck` (organisation)
- `Gisela Akcakaya, MSc` (person)
- `Ernst Hartjens` (person)
- `Bezirksgericht Josefstadt` (organisation)
- `Bezirksgericht Villach` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie durch die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Hon.-Prof.in KzlR Iris Makowska, vertreten durch Skribe Rechtsanwaelte GmbH in Wien, gegen die beklagte Partei Dieter Apfelbacher Ltd, Am Fundbach 31w, 9170 Tratten, Österreich, wegen 400 EUR sA, über den Ordinationsantrag nach § 28 JN in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Dr. Grohmann` | `Dr. Grohmann` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Hon.-Prof.in KzlR Iris Makowska` (person)
- `Skribe Rechtsanwaelte GmbH` (organisation)
- `Dieter Apfelbacher` (person)
- `Am Fundbach 31w, 9170 Tratten, Österreich` (address)
- `Bezirksgericht Schwechat` (organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Paulina Nüsken, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Oliver Eylart, Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `Mag. Ziegelbauer` | `Mag. Ziegelbauer` |
| `Dr. Faber` | `Dr. Faber` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Paulina Nüsken` (person)
- `Skribe Rechtsanwälte GmbH` (organisation)
- `Oliver Eylart` (person)
- `Bezirksgericht Schwechat` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger und Hon.-Prof. Dr. Neumayr als weitere Richter in der Verlassenschaftssache nach dem am 9. September 2009 verstorbenen, zuletzt in Zum Wetterkreuz 15, 5121 Hofstadt, Österreich, wohnhaft gewesenen Manfred Johann Puff, AZ 1 A 349/09w des Bezirksgerichts Kitzbühel, über den Delegierungsantrag der Karin Ciliberto, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, den B e s c h l u s s gefasst:  Spruch Dem Delegierungsantrag wird stattgegeben.

| Predicted | Gold |
|---|---|
| `Dr. Schinko` | `Dr. Schinko` |
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Mag. Maximilian Kocher` | `Mag. Maximilian Kocher` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Zum Wetterkreuz 15, 5121 Hofstadt, Österreich` (address)
- `Manfred Johann Puff` (person)
- `Bezirksgerichts Kitzbühel` (organisation)
- `Karin Ciliberto` (person)

**Example 12** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Steidlen+Ysner Daten GmbH, Kaminweg 34, 8200 Laßnitzthal, Österreich, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Verlag Waldlemder GmbH, Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

| Predicted | Gold |
|---|---|
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Roland Kassowitz` | `Dr. Roland Kassowitz` |
| `Prof. Haslinger` | `Prof. Haslinger` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Landesgericht Linz` (organisation)
- `Steidlen+Ysner Daten GmbH` (organisation)
- `Kaminweg 34, 8200 Laßnitzthal, Österreich` (address)
- `Verlag Waldlemder GmbH` (organisation)
- `Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich` (address)
- `Landesgerichts Linz` (organisation)
- `Handelsgericht Wien` (organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Rechtssache der klagenden Partei Mur Dorftalnex Technologien -GmbH, Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich, vertreten durch Dr. Peter Lechner und Dr. Hermann Pfurtscheller, Rechtsanwälte in Innsbruck, und ihrer Nebenintervenientin Ober Dertri GmbH, Hintereggweg 93, 2070 Kleinhöflein, Österreich, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Rudolf Ketelhut GmbH, Fiebrichgasse 17, 5120 Seeleiten, Österreich, vertreten durch Rechtsanwaltskanzlei Dr. Bernhard Hämmerle GmbH in Innsbruck, und ihrer Nebenintervenientin Völkertz Energie GmbH, Brunnbachweg 19, 4653 Mayersdorf, Österreich, vertreten durch Dr. Franz Pechmann, Rechtsanwalt in Wien, wegen 696.238,34 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck vom 2. Oktober 2009, GZ 4 R 108/09b-167, mit dem das Urteil des Landesgerichts Innsbruck vom 23. Februar 2009, GZ 41 Cg 228/01z-152, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Schinko` | `Dr. Schinko` |
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Hoch` | `Dr. Hoch` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Peter Lechner` | `Dr. Peter Lechner` |
| `Dr. Hermann Pfurtscheller` | `Dr. Hermann Pfurtscheller` |
| `Dr. Thomas Girardi` | `Dr. Thomas Girardi` |
| `Dr. Franz Pechmann` | `Dr. Franz Pechmann` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Mur Dorftalnex Technologien -GmbH` (organisation)
- `Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich` (address)
- `Ober Dertri GmbH` (organisation)
- `Hintereggweg 93, 2070 Kleinhöflein, Österreich` (address)
- `Rudolf Ketelhut` (person)
- `Fiebrichgasse 17, 5120 Seeleiten, Österreich` (address)
- `Dr. Bernhard Hämmerle GmbH` (organisation)
- `Völkertz Energie GmbH` (organisation)
- `Brunnbachweg 19, 4653 Mayersdorf, Österreich` (address)
- `Oberlandesgerichts Innsbruck` (organisation)
- `Landesgerichts Innsbruck` (organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Schneidergruberweg 37, 5132 Reith, Österreich, vertreten durch Dr. Alois Schneider, Rechtsanwalt in Rattenberg, wider die beklagte Partei Dario von Ebers, vertreten durch Dr. Walter Hausberger, Dr. Katharina Moritz und Dr. Alfred Schmidt, Rechtsanwälte in Wörgl, wegen Entfernung und Unterlassung (Revisionsinteresse 10.000 EUR), infolge Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 3. November 2017, GZ 3 R 172/17s-22, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Rattenberg vom 17. Mai 2017, GZ 3 C 401/15k-18, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Dr. Grohmann` | `Dr. Grohmann` |
| `Mag. Ziegelbauer` | `Mag. Ziegelbauer` |
| `Dr. Stefula` | `Dr. Stefula` |
| `Dr. Alois Schneider` | `Dr. Alois Schneider` |
| `Dr. Walter Hausberger` | `Dr. Walter Hausberger` |
| `Dr. Katharina Moritz` | `Dr. Katharina Moritz` |
| `Dr. Alfred Schmidt` | `Dr. Alfred Schmidt` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Schneidergruberweg 37, 5132 Reith, Österreich` (address)
- `Dario von Ebers` (person)
- `Landesgerichts Innsbruck` (organisation)
- `Bezirksgerichts Rattenberg` (organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Bartholomäus Junghahn, geboren am 8. Mai 1999, und der minderjährigen HR Sophie Elefteriadis, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Hradil` | `Dr. Hradil` |
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Hoch` | `Dr. Hoch` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `HR Sophie Elefteriadis` | `HR Sophie Elefteriadis` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Bartholomäus Junghahn` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_8`)


Mit Beschluss vom 11. 1. 2010 verpflichtete das Erstgericht den Vater, ab 5. 5. 2009 bis auf weiteres, längstens jedoch bis zur Selbsterhaltungsfähigkeit der Kinder, einen monatlichen Unterhaltsbetrag von 210 EUR für den minderjährigen Torsten Jakobic und von 180 EUR für die minderjährige ÖkR Kerstin Engelbreth zu zahlen.

| Predicted | Gold |
|---|---|
| `ÖkR Kerstin Engelbreth` | `ÖkR Kerstin Engelbreth` |

**Missed by this rule (FN):**

- `Torsten Jakobic` (person)

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Eva Abdelrahman, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei Hochenadel Immobilien GmbH, Ritterhof 11, 2661 Graben, Österreich, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Mag. Korn` | `Mag. Korn` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Eva Abdelrahman` (person)
- `Dr. Karl-Heinz Plankel` (person)
- `Hochenadel Immobilien GmbH` (organisation)
- `Ritterhof 11, 2661 Graben, Österreich` (address)
- `Lederer Rechtsanwalt GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_6`)


Text Entscheidungsgründe: Über Vermittlung der Beklagten und nach Beratung durch deren Mitarbeiter Ing. Doris Waeltermann erwarb die Klägerin im Mai 2007 um 20.000 EUR Immofinanz- und Immoeast-Aktien.

| Predicted | Gold |
|---|---|
| `Ing. Doris Waeltermann` | `Ing. Doris Waeltermann` |

**Example 19** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_7`)


Als sie einen Kursverfall dieser Aktien 2008/2009 zu einem nicht mehr näher feststellbaren Zeitpunkt wahrnahm, stellte sie erstmals fest, dass sie mit diesen Aktien ein Finanzprodukt erworben hatte, das weder dem Inhalt der Beratung des Ing. Lisa Widders noch vom Risiko und der Risikostreuung im „Portfolio“ her dem entsprach, was sie 2007 hatte erwerben wollen.

| Predicted | Gold |
|---|---|
| `Ing. Lisa Widders` | `Ing. Lisa Widders` |

**Example 20** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_9`)


Mit der am 30. 8. 2010 eingebrachten Klage begehrte die Klägerin von der Beklagten Zahlung von 20.000 EUR sA wegen fehlerhafter Anlageberatung durch deren Mitarbeiter Ing. Marion Woltz im Zusammenhang mit dem Erwerb von Immofinanz- und Immoeast-Aktien.

| Predicted | Gold |
|---|---|
| `Ing. Marion Woltz` | `Ing. Marion Woltz` |

**Example 21** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Juri Gerstl GmbH, Mutten 18, 3251 Schauboden, Österreich, vertreten durch Dr. Ralph Trischler, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, sowie die Nebenintervenientin auf Seiten der beklagten Partei Bundesbeschaffung GmbH, 1020 Wien, Lassallestraße 9b, vertreten durch die Olischar Rechtsanwaltsgesellschaft mbH in Wien, wegen 15.535 EUR sA, über den Revisionsrekurs der klagenden Partei (Revisionsinteresse: 7.460 EUR), gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 23. Februar 2023, GZ 16 R 168/22a-20, mit welchem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 5. September 2022, GZ 11 Cg 48/22t-12, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Ziegelbauer` | `Mag. Ziegelbauer` |
| `Dr. Faber` | `Dr. Faber` |
| `Mag. Schober` | `Mag. Schober` |
| `Dr. Thunhart` | `Dr. Thunhart` |
| `Dr. Ralph Trischler` | `Dr. Ralph Trischler` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Juri Gerstl` (person)
- `Mutten 18, 3251 Schauboden, Österreich` (address)
- `Bundesbeschaffung GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Leander Lindlahr, geboren am 1. August 2011, und des mj Yussuf Prussog, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Hradil` | `Dr. Hradil` |
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Hoch` | `Dr. Hoch` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Leander Lindlahr` (person)
- `Yussuf Prussog` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des minderjährigen Cedric Annamüller, geboren am 8. März 2007, 16. Mai 1964, vertreten durch das Land Kärnten als Kinder- und Jugendhilfeträger (Magistrat der Landeshauptstadt Klagenfurt, Abteilung für Jugend und Familie, Bahnhofstraße 35, 9010 Klagenfurt am Wörthersee), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Graz, gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 8. Jänner 2016, GZ 4 R 283/15g-16, womit der Beschluss des Bezirksgerichts Klagenfurt vom 17. November 2015, GZ 1 Pu 69/10x-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Mag. Ziegelbauer` | `Mag. Ziegelbauer` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Cedric Annamüller` (person)
- `8. März` (date)
- `16. Mai 1964` (date)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts Klagenfurt` (organisation)
- `Bezirksgerichts Klagenfurt` (organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludmilla von Amelunxen, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, gegen die beklagte Partei Svetlana Leinhäuser, vertreten durch Dr. Thomas Brückl, Mag. Christian Breit, Rechtsanwälte in Ried im Innkreis, wegen 1.778,52 EUR und Unterlassung (Streitwert 2.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Wels als Berufungsgericht vom 25. Jänner 2023, GZ 21 R 2/23b-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Grieskirchen vom 27. Oktober 2022, GZ 3 C 642/20h-27, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Mag. Ziegelbauer` | `Mag. Ziegelbauer` |
| `Dr. Faber` | `Dr. Faber` |
| `Mag. Schober` | `Mag. Schober` |
| `Dr. Annerl` | `Dr. Annerl` |
| `Dr. Bernhard Birek` | `Dr. Bernhard Birek` |
| `Dr. Thomas Brückl` | `Dr. Thomas Brückl` |
| `Mag. Christian Breit` | `Mag. Christian Breit` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Ludmilla von Amelunxen` (person)
- `Svetlana Leinhäuser` (person)
- `Landesgerichts Wels` (organisation)
- `Bezirksgerichts Grieskirchen` (organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Mag. Kevin Maassen, vertreten durch Dr. Clemens Lintschinger, Rechtsanwalt in Wien, gegen die beklagte Partei Hon.-Prof. Friedhelm Adde, vertreten durch Mag. Dr. Georg Backhausen, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 27. Jänner 2016, GZ 38 R 265/15z-45, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Mag. Ziegelbauer` | `Mag. Ziegelbauer` |
| `Mag. Kevin Maassen` | `Mag. Kevin Maassen` |
| `Dr. Clemens Lintschinger` | `Dr. Clemens Lintschinger` |
| `Hon.-Prof. Friedhelm Adde` | `Hon.-Prof. Friedhelm Adde` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Mag. Dr. Georg Backhausen` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden, die Hofräte Mag. Schober, Dr. Annerl und Dr. Vollmaier sowie die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Ing. Mag. Pamela Gotterbauer, vertreten durch Mag. Helwig Schuster, Rechtsanwalt in Melk, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Mag. Schober` | `Mag. Schober` |
| `Dr. Annerl` | `Dr. Annerl` |
| `Dr. Vollmaier` | `Dr. Vollmaier` |
| `Dr. Wallner-Friedl` | `Dr. Wallner-Friedl` |
| `Mag. Helwig Schuster` | `Mag. Helwig Schuster` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Ing. Mag. Pamela Gotterbauer` (person)

**Example 27** (doc_id: `deanon_260716_TRAIN/10Ob18_13i`) (sent_id: `deanon_260716_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei SüdSanitär Gruppe GmbH, Rinzendorf 28, 4501 Lindach, Österreich, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Dr. Hradil` | `Dr. Hradil` |
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Hoch` | `Dr. Hoch` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Dr. Walter Reichholf` | `Dr. Walter Reichholf` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Verein für Konsumenteninformation` (organisation)
- `SüdSanitär Gruppe GmbH` (organisation)
- `Rinzendorf 28, 4501 Lindach, Österreich` (address)
- `Kraft & Winternitz Rechtsanwälte GmbH` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Ralph Prusseit, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Akbayrak Metall GmbH, Schroateck 57, 4710 Niederweng, Österreich, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Steger` | `Dr. Steger` |
| `Dr. Annerl` | `Dr. Annerl` |
| `Dr. Wallner-Friedl` | `Dr. Wallner-Friedl` |
| `Mag. Franz Eckl` | `Mag. Franz Eckl` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Hon.-Prof. PD Dr. Rassi` (person)
- `Ralph Prusseit` (person)
- `Akbayrak Metall GmbH` (organisation)
- `Schroateck 57, 4710 Niederweng, Österreich` (address)
- `Skribe Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Krems an der Donau` (organisation)
- `Bezirksgerichts Zwettl` (organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Heimcon Software GmbH, H - Am Hang 3, 4912 Rettenbrunn, Österreich, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, gegen die beklagte Partei Gunter Landwirtschaft GmbH, Schlossfeld 38, 9300 Graßdorf, Österreich, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, wegen 7.731,06 EUR und Feststellung (Streitwert 20.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse insgesamt 11.597,42 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 216/14h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Mag. Korn` | `Mag. Korn` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Heimcon Software GmbH` (organisation)
- `H - Am Hang 3, 4912 Rettenbrunn, Österreich` (address)
- `Vavrovsky Heine Marth Rechtsanwälte GmbH` (organisation)
- `Gunter Landwirtschaft GmbH` (organisation)
- `Schlossfeld 38, 9300 Graßdorf, Österreich` (address)
- `Stolz & Schartner Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Linz` (organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der minderjährigen Annabelle Thurnher, geboren am 24. Juni 2001, vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung, Bezirk 10, 1100 Wien, Van der Nüll-Gasse 20), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 17. September 2009, GZ 44 R 454/09d-38, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Favoriten vom 16. Juni 2009, GZ 40 P 36/08f-U-26, teilweise abgeändert wurde, den B e s c h l u s s gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Schinko` | `Dr. Schinko` |
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Hoch` | `Dr. Hoch` |
| `Dr. Schramm` | `Dr. Schramm` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Annabelle Thurnher` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei DDr.in Cornelia Rinaldo, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Conmon-Verlag Limited, Kroisegg 20, 4052 Fleckendorf, Österreich Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Ziegelbauer` | `Mag. Ziegelbauer` |
| `Dr. Faber` | `Dr. Faber` |
| `Mag. Schober` | `Mag. Schober` |
| `Dr. Annerl` | `Dr. Annerl` |
| `Dr. Sven Rudolf Thorstensen` | `Dr. Sven Rudolf Thorstensen` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `DDr.in Cornelia Rinaldo` (person)
- `Conmon-Verlag Limited` (organisation)
- `Kroisegg 20, 4052 Fleckendorf, Österreich` (address)
- `Brandl Talos Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 32** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der Kinder 1.

| Predicted | Gold |
|---|---|
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Dr. Grohmann` | `Dr. Grohmann` |
| `Mag. Ziegelbauer` | `Mag. Ziegelbauer` |
| `Dr. Faber` | `Dr. Faber` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)

**Example 33** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_4`)


Malik Schoch, geboren 7. November 2002, 2. 7. Juli 2025, geboren 10. Juli 2004, und 3. Alan Schindlmair, geboren 7. August 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Timon Schönswetter, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Florian Kucera` | `Mag. Florian Kucera` |
| `Mag. Timon Schönswetter` | `Mag. Timon Schönswetter` |

**Missed by this rule (FN):**

- `Malik Schoch` (person)
- `7. November` (date)
- `7. Juli 2025` (date)
- `10. Juli` (date)
- `Alan Schindlmair` (person)
- `7. August` (date)
- `Doschek Rechtsanwalts GmbH` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Döbling` (organisation)

**Example 34** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr.Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei AXA Software Institut Gesellschaft mbH, Fuchsgrabengasse 27K, 8330 Untergiem, Österreich, vertreten durch Mag. Oliver Simoncic, Rechtsanwalt in St. Pölten, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Mag. Korn` | `Mag. Korn` |
| `Mag. Oliver Simoncic` | `Mag. Oliver Simoncic` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr.Neumayr` (person)
- `AXA Software Institut Gesellschaft mbH` (organisation)
- `Fuchsgrabengasse 27K, 8330 Untergiem, Österreich` (address)

**Example 35** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_4`)


Enns-Umwelt Consulting Limited, Alpineweg 221, 5730 Jochbergthurn, Österreich, 2. Ing. Lara Markart, letztere vertreten durch Radel Stampf Supper Rechtsanwälte OG in Mattersburg, wegen 160.422,79 EUR sA, infolge Revision der klagenden Partei (Revisionsinteresse 107.422,79 EUR sA) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Jänner 2015, GZ 4 R 119/14w-32, womit das Urteil des Landesgerichts St. Pölten vom 25. April 2014, GZ 37 Cg 96/13f-28, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Ing. Lara Markart` | `Ing. Lara Markart` |

**Missed by this rule (FN):**

- `Enns-Umwelt` (organisation)
- `Alpineweg 221, 5730 Jochbergthurn, Österreich` (address)
- `Radel Stampf Supper Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts St. Pölten` (organisation)

**Example 36** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_11`)


Da Ottokar Leuthäusser wegen eines Konkurses die Geschäftsführertätigkeit in Österreich nicht mehr ausüben konnte, fungierte vorerst Ing. Gerald Stoecks als handelsrechtlicher Geschäftsführer;

| Predicted | Gold |
|---|---|
| `Ing. Gerald Stoecks` | `Ing. Gerald Stoecks` |

**Missed by this rule (FN):**

- `Ottokar Leuthäusser` (person)

**Example 37** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_13`)


Am 12. 9. 2012 wurde der Zweitbeklagte auf Ersuchen des Ottokar Loehner als Nachfolger des Ing. Gerald Schmieden auch handelsrechtlicher Geschäftsführer.

| Predicted | Gold |
|---|---|
| `Ing. Gerald Schmieden` | `Ing. Gerald Schmieden` |

**Missed by this rule (FN):**

- `Ottokar Loehner` (person)

**Example 38** (doc_id: `deanon_260716_TRAIN/10Ob26_10m`) (sent_id: `deanon_260716_TRAIN/10Ob26_10m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der mj 1.)

| Predicted | Gold |
|---|---|
| `Dr. Schinko` | `Dr. Schinko` |
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Hoch` | `Dr. Hoch` |
| `Dr. Schramm` | `Dr. Schramm` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Neumayr` (person)

**Example 39** (doc_id: `deanon_260716_TRAIN/10Ob26_10m`) (sent_id: `deanon_260716_TRAIN/10Ob26_10m_5`)


Lars Ballogh, geboren am 3. Juli 2003, alle vertreten durch das Land Wien als Jugendwohlfahrtsträger (Amt für Jugend und Familie - Rechtsfürsorge Bezirke 17., 18. und 19., 1190 Wien, Gatterburggasse 12-14), wegen Unterhaltsvorschuss, über den „außerordentlichen Revisionsrekurs“ des Vaters Mag. Anton Bohmert, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. April 2009, GZ 44 R 193/08w-U140, womit der als Zulassungsvorstellung zu wertende „außerordentliche Revisionsrekurs“ des Vaters zurückgewiesen wurde, den Beschluss gefasst:  Spruch Der „außerordentliche Revisionsrekurs“ wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Anton Bohmert` | `Mag. Anton Bohmert` |

**Missed by this rule (FN):**

- `Lars Ballogh` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 40** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei James Jooß, vertreten durch Dr. Klaus Schiller, Rechtsanwalt in Schwanenstadt, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Dr. Hradil` | `Dr. Hradil` |
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Hoch` | `Dr. Hoch` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Dr. Klaus Schiller` | `Dr. Klaus Schiller` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `James Jooß` (person)

**Example 41** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_5`)


Unter Alver GmbH, beide Granglitzweg 11, 3251 Kroißenberg, Österreich, beide vertreten durch Dr. Michael Schneditz-Bolfras und andere Rechtsanwälte in Gmunden, wegen Bucheinsicht (in eventu Rechnungslegung) und Zahlung (Streitwert: 70.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Teilurteil des Oberlandesgerichts Linz als Berufungsgericht vom 17. Februar 2014, GZ 3 R 13/14y-90, womit das Urteil des Landesgerichts Wels vom 27. November 2013 (in der mit Beschluss vom 12. Dezember 2013 berichtigten Fassung), GZ 2 Cg 78/10p-82 und -84, abgeändert wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Michael Schneditz-Bolfras` | `Dr. Michael Schneditz-Bolfras` |

**Missed by this rule (FN):**

- `Unter Alver GmbH` (organisation)
- `Granglitzweg 11, 3251 Kroißenberg, Österreich` (address)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Wels` (organisation)

**Example 42** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_41`)


Ein Schreiben von Dr. Hagen Janischewsky mit dem Inhalt, dass die Lizenzverträge einvernehmlich aufgehoben oder beendet worden seien, erreichte den Kläger nie.

| Predicted | Gold |
|---|---|
| `Dr. Hagen Janischewsky` | `Dr. Hagen Janischewsky` |

**Example 43** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Brigitte Martz, geboren am 16. November 1978, wegen Kontaktrechts des Vaters Dr. Gustav Thöning, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Madeleine Musialik, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

| Predicted | Gold |
|---|---|
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Dr. Grohmann` | `Dr. Grohmann` |
| `Mag. Ziegelbauer` | `Mag. Ziegelbauer` |
| `Dr. Gustav Thöning` | `Dr. Gustav Thöning` |
| `Dr. Madeleine Musialik` | `Dr. Madeleine Musialik` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Brigitte Martz` (person)
- `16. November 1978` (date)
- `Pieler & Pieler & Partner KG` (organisation)
- `Kosch & Partner Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Wiener Neustadt` (organisation)
- `Bezirksgerichts Wiener Neustadt` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 44** (doc_id: `deanon_260716_TRAIN/10Ob28_19v`) (sent_id: `deanon_260716_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Bau Zorostfurt GmbH, Isbarystraße 47, 4152 Schölling, Österreich, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Buitenkamp und Rothauge Landwirtschaft GmbH, Gewerbegebiet Mathon 17, 3672 Reitern, Österreich, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Dr. Grohmann` | `Dr. Grohmann` |
| `Mag. Ziegelbauer` | `Mag. Ziegelbauer` |
| `Dr. Faber` | `Dr. Faber` |
| `Dr. Alexandra Slama` | `Dr. Alexandra Slama` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Bau Zorostfurt GmbH` (organisation)
- `Isbarystraße 47, 4152 Schölling, Österreich` (address)
- `Buitenkamp und Rothauge Landwirtschaft GmbH` (organisation)
- `Gewerbegebiet Mathon 17, 3672 Reitern, Österreich` (address)
- `Grassner, Lenz, Thewanger & Partner, Rechtsanwälte` (organisation)
- `Oberlandesgerichts Linz` (organisation)

**Example 45** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der zur AZ 38 Nc 13/08i beim Landesgericht für Zivilrechtssachen Wien anhängigen Ablehnungssache des Ablehnungswerbers Mag. Herwig Bortzlaff, über den Rekurs des Ablehnungswerbers gegen den Beschluss des Oberlandesgerichts Wien vom 10. November 2009, GZ 13 Nc 14/09x-2, womit ein Ablehnungsantrag zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Schinko` | `Dr. Schinko` |
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Hoch` | `Dr. Hoch` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Mag. Herwig Bortzlaff` | `Mag. Herwig Bortzlaff` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Landesgericht für Zivilrechtssachen Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 46** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_6`)


11. 2008, GZ 38 Nc 13/08i-2, den Ablehnungsantrag des Mag. Herwig Berkenbrink in dessen Rekurs gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 13.

| Predicted | Gold |
|---|---|
| `Mag. Herwig Berkenbrink` | `Mag. Herwig Berkenbrink` |

**Missed by this rule (FN):**

- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 47** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_9`)


Senat in der Besetzung Senatspräsidentin Dr. Sandra Hilt, Mag. Manuel Kumas und MMMag. Gottfried Fegbeitel mit Beschluss vom 3. 8. 2009, AZ 11 R 105/09f, keine Folge und verhängte über den Ablehnungswerber wegen beleidigender Äußerungen im Rechtsmittel eine Ordnungsstrafe von 1.600 EUR.

| Predicted | Gold |
|---|---|
| `Dr. Sandra Hilt` | `Dr. Sandra Hilt` |
| `Mag. Manuel Kumas` | `Mag. Manuel Kumas` |

**Missed by this rule (FN):**

- `MMMag. Gottfried Fegbeitel` (person)

**Example 48** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_13`)


Senat des Oberlandesgerichts Wien in der Besetzung Senatspräsidentin Dr. Paolo Barley sowie Mag. Klarissa Hausteiner und Mag. Viola Brauch als weitere Richter den Ablehnungsantrag des Ablehnungswerbers vom 24. 8. 2009 zurück.

| Predicted | Gold |
|---|---|
| `Dr. Paolo Barley` | `Dr. Paolo Barley` |
| `Mag. Klarissa Hausteiner` | `Mag. Klarissa Hausteiner` |
| `Mag. Viola Brauch` | `Mag. Viola Brauch` |

**Missed by this rule (FN):**

- `Oberlandesgerichts Wien` (organisation)

**Example 49** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Jaden Meyerjohann, geboren am 3. Juli 2020, Leroy Jungschmidt, geboren am 28. Mai 1965 und Clemens Theocharakis, geboren am 25. März 1999, in Pflege und Erziehung der Mutter Emanuela Janischefsky, vertreten durch das Land Vorarlberg als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Feldkirch, Schlossgraben 1, 6800 Feldkirch), wegen Gewährung von Unterhaltsvorschuss, über den Revisionsrekurs des Vaters Ashley Biesert, vertreten durch Mag. Hans-Christian Obernberger, Rechtsanwalt in Feldkirch, gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 12. Juli 2011, GZ 3 R 198/11g, 3 R 199/11d, 3 R 200/11a-18, womit die Beschlüsse des Bezirksgerichts Feldkirch vom 18. Mai 2011, GZ 12 Pu 141/11f-4 bis 6, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hradil` | `Dr. Hradil` |
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Hoch` | `Dr. Hoch` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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
- `Landesgerichts Feldkirch` (organisation)
- `Bezirksgerichts Feldkirch` (organisation)

**Example 50** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch und Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der minderjährigen Karsten Alberter, geboren am 2. April 2010, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Wien-Umgebung, Fachgebiet Jugendwohlfahrt), 3400 Klosterneuburg, Leopoldstraße 21, über das als „Berufung“ bezeichnete Rechtsmittel des Vaters Helmut Dreilich, gegen den Beschluss des Landesgerichts Korneuburg als Rekursgericht vom 25. März 2013, GZ 23 R 30/13v-53, womit der Beschluss des Bezirksgerichts Schwechat vom 27. August 2012, GZ 8 Pu 190/11i-39, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.  Text Begründung: Verfahrensgegenstand ist die Festsetzung des gesetzlichen Unterhalts für die mj Lena Amini.

| Predicted | Gold |
|---|---|
| `Dr. Hradil` | `Dr. Hradil` |
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Hoch` | `Dr. Hoch` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Karsten Alberter` (person)
- `2. April 2010` (date)
- `Helmut Dreilich` (person)
- `Landesgerichts Korneuburg` (organisation)
- `Bezirksgerichts Schwechat` (organisation)
- `Lena Amini` (person)

**Example 51** (doc_id: `deanon_260716_TRAIN/10Ob30_19p`) (sent_id: `deanon_260716_TRAIN/10Ob30_19p_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der minderjährigen Maja Dolleschell, geboren 14. August 2009, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Melk, 3390 Melk, Abt Karl-Straße 25a) wegen Unterhaltsvorschüssen, über den Revisionsrekurs des Kindes gegen den Beschluss des Landesgerichts St. Pölten als Rekursgericht vom 23. Jänner 2019, GZ 23 R 6/19h-52, mit dem der Beschluss des Bezirksgerichts Melk vom 21. November 2018, GZ 22 Pu 194/16m-42, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Dr. Grohmann` | `Dr. Grohmann` |
| `Mag. Ziegelbauer` | `Mag. Ziegelbauer` |
| `Dr. Faber` | `Dr. Faber` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Maja Dolleschell` (person)
- `14. August` (date)
- `Bezirkshauptmannschaft Melk` (organisation)
- `Landesgerichts St. Pölten` (organisation)
- `Bezirksgerichts Melk` (organisation)

**Example 52** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende, den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber sowie die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Leander Andermann, vertreten durch Dr. Martin Leitner, Rechtsanwalt in Wien, gegen die beklagte Partei Ing. Ferdinand Abramova, vertreten durch Mag. Wilhelm Deutschmann MBA und Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M., Rechtsanwälte in Linz, wegen 500.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 11. Mai 2022, GZ 2 R 64/22b-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Ziegelbauer` | `Mag. Ziegelbauer` |
| `Dr. Faber` | `Dr. Faber` |
| `Mag. Schober` | `Mag. Schober` |
| `Dr. Annerl` | `Dr. Annerl` |
| `Dr. Martin Leitner` | `Dr. Martin Leitner` |
| `Ing. Ferdinand Abramova` | `Ing. Ferdinand Abramova` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Leander Andermann` (person)
- `Mag. Wilhelm Deutschmann MBA` (person)
- `Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M.` (person)
- `Oberlandesgerichts Linz` (organisation)

**Example 53** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_11`)


Nach längeren Verhandlungen unterfertigte die Klägerin am 18. Dezember 2018 folgende Erklärung: „1. Wir haben gegen Ing. Kai Achler [...] ('der Schuldner') eine Forderung von 500.000,00 EUR (in Worten[richtig:]fünfhunderttausend).

| Predicted | Gold |
|---|---|
| `Ing. Kai Achler` | `Ing. Kai Achler` |

**Example 54** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Mag. Korn` | `Mag. Korn` |
| `Mag. Johannes Bügler` | `Mag. Johannes Bügler` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Langhansl+Antonewitz Chemie AG` (organisation)
- `Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich` (address)
- `Poinstingl & Partner Rechtsanwälte OG` (organisation)
- `Drau-Pharma GmbH` (organisation)
- `Strazzegasse 12, 8762 Oberzeiring, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 55** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Karim Mielewczik, gegen die beklagte Partei Dr. Sandro Gädecken, vertreten durch Ing. Dr. Stefan Krall und Dr. Oliver Kühnl, Rechtsanwälte in Innsbruck, wegen 9.456 EUR sA (Revisionsinteresse 9.268,50 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 25. Februar 2025, GZ 21 R 434/24f-29, mit dem das Urteil des Bezirksgerichts Seekirchen am Wallersee vom 5. September 2024, GZ 2 C 1107/23d-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Annerl` | `Dr. Annerl` |
| `Dr. Vollmaier` | `Dr. Vollmaier` |
| `Dr. Wallner-Friedl` | `Dr. Wallner-Friedl` |
| `Dr. Sandro Gädecken` | `Dr. Sandro Gädecken` |
| `Dr. Oliver Kühnl` | `Dr. Oliver Kühnl` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Hon.-Prof. PD Dr. Rassi` (person)
- `Karim Mielewczik` (person)
- `Ing. Dr. Stefan Krall` (person)
- `Landesgerichts Salzburg` (organisation)
- `Bezirksgerichts Seekirchen` (organisation)

**Example 56** (doc_id: `deanon_260716_TRAIN/10Ob3_12g`) (sent_id: `deanon_260716_TRAIN/10Ob3_12g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Maja Pirkmayr, vertreten durch Dr. Georg Gorton und DDr. Birgit Gorton, Rechtsanwälte in Klagenfurt, gegen die beklagte Partei Ing. Emanuel Puff, vertreten durch Dr. Gottfried Kassin, Rechtsanwalt in St. Veit an der Glan, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 26. Mai 2011, GZ 2 R 83/11z-49, mit dem das Urteil des Bezirksgerichts St. Veit an der Glan vom 29. Oktober 2010, GZ 3 C 333/09h-34, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hradil` | `Dr. Hradil` |
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Hoch` | `Dr. Hoch` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Dr. Georg Gorton` | `Dr. Georg Gorton` |
| `Ing. Emanuel Puff` | `Ing. Emanuel Puff` |
| `Dr. Gottfried Kassin` | `Dr. Gottfried Kassin` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Maja Pirkmayr` (person)
- `DDr. Birgit Gorton` (person)
- `Landesgerichts Klagenfurt` (organisation)

**Example 57** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Ziegelbauer als Vorsitzenden sowie die Hofrätin Dr. Faber und die Hofräte Mag. Schober, Dr. Thunhart und Dr. Annerl als weitere Richter in der Pflegschaftssache der minderjährigen Meinrad Bruhnsen, geboren 30. Januar 2006, vertreten durch das Land Wien als Träger der Kinder- und Jugendhilfe (Magistrat der Stadt Wien, Rechtsvertretung Bezirke 1, 4 bis 9, 1060 Wien, Amerlingstraße 11), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch die Präsidentin des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 31. Oktober 2022, GZ 43 R 323/22a-17, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 9. Juni 2022, GZ 4 Pu 58/22a-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Ziegelbauer` | `Mag. Ziegelbauer` |
| `Dr. Faber` | `Dr. Faber` |
| `Mag. Schober` | `Mag. Schober` |
| `Dr. Thunhart` | `Dr. Thunhart` |
| `Dr. Annerl` | `Dr. Annerl` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Meinrad Bruhnsen` (person)
- `30. Januar` (date)
- `Magistrat der Stadt Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Innere Stadt Wien` (organisation)

**Example 58** (doc_id: `deanon_260716_TRAIN/10Ob41_14y`) (sent_id: `deanon_260716_TRAIN/10Ob41_14y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in den verbundenen Familienrechtssachen des Antragstellers DI Dr. Bodo Kaczynski, geboren am 25. Juli 1975, vertreten durch Mag. Werner Thurner, Rechtsanwalt in Graz, gegen die Antragsgegnerinnen 1. Wolfgang Lombardini, geboren am 4. Dezember 2022, 2. Livia Löblein, geboren am 11. Januar 1966, vertreten durch Mörth Ecker Filzmaier, Rechtsanwalts-Partnerschaft in Graz, wegen Unterhalt, über den Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 24. September 2013, GZ 2 R 11/13x-76, womit der Beschluss des Bezirksgerichts Graz-Ost vom 26. November 2012, GZ 231 Fam 14/11a, 231 Fam 17/11t, 231 Fam 18/11i-60, teilweise bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.  Text Begründung: DasErstgerichtsetzte den monatlichen Unterhalt für die Erstantragsgegnerin ab 1. 2. 2011 von 390 EUR um 30 EUR auf 360 EUR herab (Punkt 1);

| Predicted | Gold |
|---|---|
| `Dr. Hradil` | `Dr. Hradil` |
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Hoch` | `Dr. Hoch` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Mag. Werner Thurner` | `Mag. Werner Thurner` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `DI Dr. Bodo Kaczynski` (person)
- `25. Juli 1975` (date)
- `Wolfgang Lombardini` (person)
- `4. Dezember 2022` (date)
- `Livia Löblein` (person)
- `11. Januar 1966` (date)
- `Mörth Ecker Filzmaier, Rechtsanwalts-Partnerschaft` (organisation)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)
- `Bezirksgerichts Graz-Ost` (organisation)

**Example 59** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Parteien 2.)

| Predicted | Gold |
|---|---|
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Dr. Grohmann` | `Dr. Grohmann` |
| `Mag. Ziegelbauer` | `Mag. Ziegelbauer` |
| `Dr. Faber` | `Dr. Faber` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)

**Example 60** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_4`)


Dr. Serge Schieferle, Niederlande, und 3.)

| Predicted | Gold |
|---|---|
| `Dr. Serge Schieferle` | `Dr. Serge Schieferle` |

**Example 61** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_5`)


Dr. Felix Cornils, Niederlande, beide vertreten durch Tramposch & Partner, Rechtsanwälte KG in Innsbruck, gegen die beklagte Partei Mag.a Constanze Rizzo, vertreten durch König Ermacora Klotz & Partner, Rechtsanwälte in Innsbruck, wegen je 15.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 1. Juli 2020, GZ 10 R 16/20h-49, mit dem das Urteil des Landesgerichts Innsbruck vom 6. Februar 2020, GZ 41 Cg 11/19i-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Felix Cornils` | `Dr. Felix Cornils` |

**Missed by this rule (FN):**

- `Tramposch & Partner, Rechtsanwälte KG` (organisation)
- `Mag.a Constanze Rizzo` (person)
- `Oberlandesgerichts Innsbruck` (organisation)
- `Landesgerichts Innsbruck` (organisation)

**Example 62** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Pflegschaftssache 1. der mj Emma Mittelstaedt, geboren am 21. Mai 2025 und 2. des mj Milena Roesche, geboren am 25. Juni 1957, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung Bezirk 22, 1220 Wien, Hirschstettner Straße 19-21/Stiege N), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 10. Dezember 2014, GZ 42 R 343/13x, 42 R 344/13v und 42 R 345/13s-106, womit den Rekursen der Minderjährigen gegen den Beschluss des Bezirksgerichts Donaustadt vom 14. März 2013, GZ 3 Pu 61/12x-40, teilweise Folge gegeben wurde (Pkt 1 des Spruchs), dem Rekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen die Beschlüsse des Bezirksgerichts Donaustadt (jeweils) vom 6. Juni 2013, GZ 3 Pu 61/12x-49 und 3 Pu 61/12x-50, Folge gegeben (Pkt 2a des Spruchs), und aus Anlass des Rekurses die Anträge der Minderjährigen auf Gewährung von Unterhaltsvorschüssen zur Gänze abgewiesen wurden (Pkt 2b des Spruchs), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Mag. Korn` | `Mag. Korn` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Emma Mittelstaedt` (person)
- `21. Mai 2025` (date)
- `Milena Roesche` (person)
- `25. Juni 1957` (date)
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)

**Example 63** (doc_id: `deanon_260716_TRAIN/10Ob43_19z`) (sent_id: `deanon_260716_TRAIN/10Ob43_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Othmar Mertl, vertreten durch Nitsch Pajor Zöllner Rechtsanwälte OG in Mödling, gegen die beklagte Partei Stadtgemeinde Malik Fridt, vertreten durch Krist Bubits Rechtsanwälte OG in Mödling, wegen 1.) 21.216,92 EUR sA und 2.) Feststellung (Streitwert: 2.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Februar 2019, GZ 12 R 96/18b-36, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Wiener Neustadt vom 31. August 2018, GZ 20 Cg 86/17h-31, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Dr. Grohmann` | `Dr. Grohmann` |
| `Mag. Ziegelbauer` | `Mag. Ziegelbauer` |
| `Dr. Faber` | `Dr. Faber` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Othmar Mertl` (person)
- `Nitsch Pajor Zöllner Rechtsanwälte OG` (organisation)
- `Malik Fridt` (person)
- `Krist Bubits Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 64** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und den Hofrat Dr. Schramm, die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin Scarlett Achatzi, gegen den Antragsgegner Mag. Ewald Aszmutat, wegen Unterhalt, infolge Rekurses des Antragsgegners gegen den Beschluss des Oberlandesgerichts Wien vom 4. Jänner 2017, GZ 12 Nc 28/16h-3, womit der Ablehnungsantrag des Antragsgegners zurückgewiesen wurde, sowie über den Ablehnungsantrag gegen alle Richter des Oberlandesgerichts Wien, folgenden Beschluss gefasst:  Spruch 1.

| Predicted | Gold |
|---|---|
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Dr. Grohmann` | `Dr. Grohmann` |
| `Mag. Ziegelbauer` | `Mag. Ziegelbauer` |
| `Mag. Ewald Aszmutat` | `Mag. Ewald Aszmutat` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Scarlett Achatzi` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 65** (doc_id: `deanon_260716_TRAIN/10Ob57_13z`) (sent_id: `deanon_260716_TRAIN/10Ob57_13z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der Kinder Mikolaj Eleftheriadou, geboren am 9. August 1991, Helge Schuchmann, geboren am 30. September 1992, mj Isabel Rahnfeld, geboren am 22. Dezember 1998 und mj PhD Daniel Coutand, geboren am 18. Jänner 2001, wegen Unterhaltsvorschuss, infolge Revisionsrekurses des Vaters Mag. Dirk Hükelheim, vertreten durch Mag. Roland Marko, Rechtsanwalt in Wien, dieser vertreten durch Dr. Francisco Rumpf, Rechtsanwalt in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 7. Juni 2013, GZ 43 R 391/08f ua -U-458, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 12. November 2007, GZ 2 P 88/07t-U-238, abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hradil` | `Dr. Hradil` |
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Hoch` | `Dr. Hoch` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Mag. Dirk Hükelheim` | `Mag. Dirk Hükelheim` |
| `Mag. Roland Marko` | `Mag. Roland Marko` |
| `Dr. Francisco Rumpf` | `Dr. Francisco Rumpf` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mikolaj Eleftheriadou` (person)
- `Helge Schuchmann` (person)
- `Isabel Rahnfeld` (person)
- `PhD Daniel Coutand` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Innere Stadt Wien` (organisation)

**Example 66** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Cassandra Wespi, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Bilek Lebensmittel GmbH in Liqu, Dreijochgasse 11, 4722 Stefansdorf, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Dr. Grohmann` | `Dr. Grohmann` |
| `Mag. Ziegelbauer` | `Mag. Ziegelbauer` |
| `Dr. Faber` | `Dr. Faber` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `DI Cassandra Wespi` (person)
- `Vogl Rechtsanwalt GmbH` (organisation)
- `Bilek Lebensmittel GmbH` (organisation)
- `Dreijochgasse 11, 4722 Stefansdorf, Österreich` (address)
- `Wess Kux Kispert & Eckert Rechtsanwalts GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 67** (doc_id: `deanon_260716_TRAIN/10Ob6_24s`) (sent_id: `deanon_260716_TRAIN/10Ob6_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Dr. Weber, Mag. Schober, Dr. Annerl und Dr. Vollmaier als weitere Richter in der Rechtssache des (ehemaligen) Klägers und Gegners der gefährdeten Parteien Agatha von der Heide, vertreten durch MMag. Dr. Sebastian Pribas, Rechtsanwalt in Dornbirn, als Verfahrenshelfer, dieser vertreten durch Mag. Benedikt Walch, Rechtsanwalt in Lech am Arlberg, gegen die (ehemals) Beklagte und erstgefährdete Partei Alva Sengül, sowie die zweitgefährdete Partei mj Selina Birkmeir, und die drittgefährdete Partei mj Harald Ladwig, LLM, alle wohnhaft in In der Klaus 72, 4785 Bach, Österreich, und vertreten durch Mag. German Bertsch, Rechtsanwalt in Feldkirch, wegen Ehescheidung sowie einstweiligem Ehegatten- und Kindesunterhalt, über den außerordentlichen Revisionsrekurs des Gegners der gefährdeten Parteien gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 22. September 2022, GZ 3 R 187/22f-323, womit der Beschluss des Bezirksgerichts Feldkirch vom 29. April 2022, GZ 2 C 23/17g-306, bestätigt wurde, den Beschluss gefasst:  Spruch In Ansehung der auf Zahlung von einstweiligem Ehegattenunterhalt gerichteten Begehren wird der außerordentliche Revisionsrekurs gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Weber` | `Dr. Weber` |
| `Mag. Schober` | `Mag. Schober` |
| `Dr. Annerl` | `Dr. Annerl` |
| `Dr. Vollmaier` | `Dr. Vollmaier` |
| `Mag. Benedikt Walch` | `Mag. Benedikt Walch` |
| `Mag. German Bertsch` | `Mag. German Bertsch` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Agatha von der Heide` (person)
- `MMag. Dr. Sebastian Pribas` (person)
- `Alva Sengül` (person)
- `Selina Birkmeir` (person)
- `Harald Ladwig, LLM` (person)
- `In der Klaus 72, 4785 Bach, Österreich` (address)
- `Landesgerichts Feldkirch` (organisation)
- `Bezirksgerichts Feldkirch` (organisation)

**Example 68** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Ing. Christian Stangl-Brachnik, MA BA und Mag. Claudia Gründel (beide aus dem Kreis der Arbeitgeber) als weitere Richter in der Sozialrechtssache der klagenden Partei Mathias Jendl, vertreten durch Dr. Thomas Stampfer und Dr. Christoph Orgler, Rechtsanwälte in Graz, gegen die beklagte Partei Sozialversicherungsanstalt der Bauern, 1031 Wien, Ghegastraße 1, vertreten durch Dr. Michael Stögerer, Rechtsanwalt in Wien, wegen Ausgleichszulage, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2017, GZ 7 Rs 37/17s-11, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. April 2017, GZ 43 Cgs 113/17p-7, teils bestätigt und teils abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Mag. Claudia Gründel` | `Mag. Claudia Gründel` |
| `Dr. Thomas Stampfer` | `Dr. Thomas Stampfer` |
| `Dr. Christoph Orgler` | `Dr. Christoph Orgler` |
| `Dr. Michael Stögerer` | `Dr. Michael Stögerer` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Ing. Christian Stangl-Brachnik, MA BA` (person)
- `Mathias Jendl` (person)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)

**Example 69** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, den Hofrat Dr. Fellinger und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter KR Hermann Furtner (aus dem Kreis der Arbeitgeber) und AR Angelika Neuhauser (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Birgit Jaros, vertreten durch Dr. Herbert Pochieser, Rechtsanwalt in Wien, gegen die beklagte Partei Wiener Gebietskrankenkasse, 1100 Wien, Wienerbergstraße 15-19, vertreten durch Dr. Heinz Edelmann, Rechtsanwalt in Wien, wegen Kostenerstattung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 11. September 2012, GZ 8 Rs 49/12b-28, womit das Urteil des Arbeits- und Sozialgerichts Wien vom 21. November 2011, GZ 17 Cgs 120/10a-24, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Hradil` | `Dr. Hradil` |
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `KR Hermann Furtner` | `KR Hermann Furtner` |
| `AR Angelika Neuhauser` | `AR Angelika Neuhauser` |
| `Dr. Herbert Pochieser` | `Dr. Herbert Pochieser` |
| `Dr. Heinz Edelmann` | `Dr. Heinz Edelmann` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Birgit Jaros` (person)
- `Wiener Gebietskrankenkasse` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 70** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Roland Soukup, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Dr. Gabriele Griehsel` | `Dr. Gabriele Griehsel` |
| `Dr. Wolfgang Kozak` | `Dr. Wolfgang Kozak` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Roland Soukup` (person)
- `Mahringer Steinwender Bestebner Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Salzburg` (organisation)

**Example 71** (doc_id: `deanon_260716_TRAIN/10ObS99_15d`) (sent_id: `deanon_260716_TRAIN/10ObS99_15d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die fachkundigen Laienrichter Mag. Dr. Wolfgang Höfle (aus dem Kreis der Arbeitgeber) und Ing. Thomas Bauer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Willibald Kollowrat, BEd, vertreten durch Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH in Graz, gegen die beklagte Partei Versicherungsanstalt für Eisenbahnen und Bergbau, Linke Wienzeile 48-52, 1060 Wien, vertreten durch Dr. Marie-Luise Safranek, Rechtsanwältin in Graz, wegen Wochengeld, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Juni 2015, GZ 7 Rs 28/15i-9, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 25. Februar 2015, GZ 36 Cgs 216/14d-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Ing. Thomas Bauer` | `Ing. Thomas Bauer` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Mag. Dr. Wolfgang Höfle` (person)
- `Willibald Kollowrat, BEd` (person)
- `Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH` (organisation)
- `Versicherungsanstalt für Eisenbahnen und Bergbau` (organisation)
- `Dr. Marie-Luise Safranek` (person)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)

**Example 72** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_3`)


Kopf Der Oberste Gerichtshof hat am 15. Jänner 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart der Richteramtsanwärterin Dr. Parapatits als Schriftführerin, in der Strafsache gegen Bernhard Buddäus und Norbert Wehrhahn wegen des Verbrechens des schweren Betrugs nach §§ 146, 147 Abs 3 StGB über die Nichtigkeitsbeschwerde und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 29. März 2012, GZ 31 Hv 51/10y-84, nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Angeklagten sowie des Verteidigers des Zweitangeklagten Mag. Rienmüller zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Zehetner` | `Dr. Zehetner` |
| `Dr. Schwab` | `Dr. Schwab` |
| `Mag. Lendl` | `Mag. Lendl` |
| `Mag. Michel` | `Mag. Michel` |
| `Dr. Oshidari` | `Dr. Oshidari` |
| `Dr. Parapatits` | `Dr. Parapatits` |
| `Mag. Höpler` | `Mag. Höpler` |
| `Mag. Rienmüller` | `Mag. Rienmüller` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Bernhard Buddäus` (person)
- `Norbert Wehrhahn` (person)
- `Landesgerichts Salzburg` (organisation)

**Example 73** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_3`)


Kopf Der Oberste Gerichtshof hat am 17. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Sommer als Schriftführer, in der Strafsache gegen Richard Lindt wegen des Vergehens der vorsätzlichen Beeinträchtigung der Umwelt nach § 180 Abs 2 Z 1, Z 2 StGB und einer weiteren strafbaren Handlung, AZ 40 Hv 147/10g des Landesgerichts Salzburg, über die Beschwerde des Genannten gegen den Beschluss dieses Gerichts vom 7. September 2011, ON 547, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Zehetner` | `Dr. Zehetner` |
| `Dr. Schwab` | `Dr. Schwab` |
| `Mag. Lendl` | `Mag. Lendl` |
| `Mag. Michel` | `Mag. Michel` |
| `Dr. Michel-Kwapinski` | `Dr. Michel-Kwapinski` |
| `Mag. Sommer` | `Mag. Sommer` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Richard Lindt` (person)
- `Landesgerichts Salzburg` (organisation)

**Example 74** (doc_id: `deanon_260716_TRAIN/11Os59_13f`) (sent_id: `deanon_260716_TRAIN/11Os59_13f_3`)


Kopf Der Oberste Gerichtshof hat am 28. Mai 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Kurzthaler als Schriftführer, in der Strafsache gegen Andreas Schiessl wegen des Verbrechens des schweren Raubes nach §§ 15, 142 Abs 1, 143 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Wiener Neustadt als Schöffengericht vom 28. Februar 2013, GZ 37 Hv 158/12k-13, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Zehetner` | `Dr. Zehetner` |
| `Dr. Schwab` | `Dr. Schwab` |
| `Mag. Lendl` | `Mag. Lendl` |
| `Mag. Michel` | `Mag. Michel` |
| `Dr. Oshidari` | `Dr. Oshidari` |
| `Mag. Kurzthaler` | `Mag. Kurzthaler` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Andreas Schiessl` (person)
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 75** (doc_id: `deanon_260716_TRAIN/11Os67_16m`) (sent_id: `deanon_260716_TRAIN/11Os67_16m_3`)


Kopf Der Oberste Gerichtshof hat am 13. September 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Rathgeb als Schriftführerin in der Strafsache gegen Daniel Kur wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 1 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 22. April 2016, GZ 22 Hv 14/16s-43, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Schwab` | `Dr. Schwab` |
| `Dr. Bachner-Foregger` | `Dr. Bachner-Foregger` |
| `Mag. Michel` | `Mag. Michel` |
| `Mag. Fürnkranz` | `Mag. Fürnkranz` |
| `Dr. Oberressl` | `Dr. Oberressl` |
| `Mag. Rathgeb` | `Mag. Rathgeb` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Daniel Kur` (person)
- `Landesgerichts Innsbruck` (organisation)

**Example 76** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_4`)


Augst 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Vizepräsidentin des Obersten Gerichtshofs Mag. Marek, die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Wieser als Schriftführerin in der Maßnahmenvollzugssache des Gerald Winand wegen bedingter Nachsicht einer mit Freiheitsentziehung verbundenen vorbeugenden Maßnahme (§ 21 Abs 1 StGB) über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien vom 16. Mai 2018, AZ 22 Bs 119/18p (AZ 606 Hv 1/17k des Landesgerichts Korneuburg), nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Schwab` | `Dr. Schwab` |
| `Mag. Marek` | `Mag. Marek` |
| `Dr. Bachner-Foregger` | `Dr. Bachner-Foregger` |
| `Mag. Fürnkranz` | `Mag. Fürnkranz` |
| `Dr. Oberressl` | `Dr. Oberressl` |
| `Mag. Wieser` | `Mag. Wieser` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Gerald Winand` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts Korneuburg` (organisation)

**Example 77** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_3`)


Kopf Der Oberste Gerichtshof hat am 18. März 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski im Verfahren zur Unterbringung des Mag. Herwig Bäseke in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB, AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz gemäß § 62 Abs 1 zweiter Satz OGH-Geo 2019 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger sowie Mag. Fürnkranz sind von der Entscheidung über die Anträge des Mag. Herwig Berto auf Erneuerung des Strafverfahrens AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, ausgeschlossen.

| Predicted | Gold |
|---|---|
| `Dr. Oshidari` | `Dr. Oshidari` |
| `Dr. Michel-Kwapinski` | `Dr. Michel-Kwapinski` |
| `Mag. Herwig Bäseke` | `Mag. Herwig Bäseke` |
| `Dr. Schwab` | `Dr. Schwab` |
| `Dr. Bachner-Foregger` | `Dr. Bachner-Foregger` |
| `Mag. Fürnkranz` | `Mag. Fürnkranz` |
| `Dr. Schwab` | `Dr. Schwab` |
| `Dr. Bachner-Foregger` | `Dr. Bachner-Foregger` |
| `Mag. Fürnkranz` | `Mag. Fürnkranz` |
| `Mag. Herwig Berto` | `Mag. Herwig Berto` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `OGH` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 78** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_4`)


An ihre Stelle treten Senatspräsident des Obersten Gerichtshofs Dr. Solé sowie Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Setz-Hummel.

| Predicted | Gold |
|---|---|
| `Dr. Michel-Kwapinski` | `Dr. Michel-Kwapinski` |
| `Dr. Setz-Hummel` | `Dr. Setz-Hummel` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Dr. Solé` (person)
- `Obersten Gerichtshofs` (organisation)

**Example 79** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_6`)


Senatspräsident des Obersten Gerichtshofs Dr. Schwab sowie Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz sind Mitglieder des zuständigen 11.

| Predicted | Gold |
|---|---|
| `Dr. Schwab` | `Dr. Schwab` |
| `Dr. Bachner-Foregger` | `Dr. Bachner-Foregger` |
| `Mag. Fürnkranz` | `Mag. Fürnkranz` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 80** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_8`)


Der vorliegende Antrag des Mag. Herwig Bleuler bezieht sich auf das Urteil des Oberlandesgerichts Wien vom 21. August 2019, AZ 17 Bs 168/19h, mit dem der Berufung des Betroffenen gegen das Urteil des Landesgerichts für Strafsachen Wien vom 14. November 2018, GZ 22 Hv 7/18k-350, nicht Folge gegeben wurde.

| Predicted | Gold |
|---|---|
| `Mag. Herwig Bleuler` | `Mag. Herwig Bleuler` |

**Missed by this rule (FN):**

- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 81** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_12`)


Senatspräsident des Obersten Gerichtshofs Dr. Solé sowie Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Setz-Hummel treten aufgrund der laufenden Vertretungsregelung der Geschäftsverteilung des Obersten Gerichtshofs an deren Stelle (§ 45 Abs 2 StPO).

| Predicted | Gold |
|---|---|
| `Dr. Michel-Kwapinski` | `Dr. Michel-Kwapinski` |
| `Dr. Setz-Hummel` | `Dr. Setz-Hummel` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Dr. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 82** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_3`)


Kopf Der Oberste Gerichtshof hat am 16. März 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Brenner in der Strafvollzugssache des Oliver Pekarek, AZ 39 Ns 43/15i des Landesgerichts Krems an der Donau, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `Dr. Brenner` | `Dr. Brenner` |
| `Dr. Schwab` | `Dr. Schwab` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Oliver Pekarek` (person)
- `Landesgerichts Krems an der Donau` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `OGH` (organisation)

**Example 83** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_4`)


2005 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab ist von der Entscheidung über die Beschwerde des Oliver Paukstat gegen den Beschluss des Oberlandesgerichts Wien vom 8. Februar 2016, AZ 32 Bs 12/16y, ausgeschlossen.

| Predicted | Gold |
|---|---|
| `Dr. Schwab` | `Dr. Schwab` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Oliver Paukstat` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 84** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_5`)


An Stelle der nunmehr als Vorsitzende einschreitenden Hofrätin des Obersten Gerichtshofs Dr. Bachner-Foregger tritt Hofrat des Obersten Gerichtshofs Dr. Nordmeyer.

| Predicted | Gold |
|---|---|
| `Dr. Bachner-Foregger` | `Dr. Bachner-Foregger` |
| `Dr. Nordmeyer` | `Dr. Nordmeyer` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 85** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_7`)


Senatspräsident des Obersten Gerichtshofs Dr. Schwab ist Vorsitzender des zuständigen 11.

| Predicted | Gold |
|---|---|
| `Dr. Schwab` | `Dr. Schwab` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)

**Example 86** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_9`)


An der angefochtenen Entscheidung des Oberlandesgerichts Wien hat die mit ihm in einem Angehörigenverhältnis im Sinne des § 72 StGB stehende Senatspräsidentin des Oberlandesgerichts Dr. Christine Schwab als Richterin mitgewirkt.

| Predicted | Gold |
|---|---|
| `Dr. Christine Schwab` | `Dr. Christine Schwab` |

**Missed by this rule (FN):**

- `Oberlandesgerichts Wien` (organisation)

**Example 87** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_10`)


Als deren Angehöriger (§ 72 StGB) ist Senatspräsident des Obersten Gerichtshofs Dr. Schwab gemäß § 43 Abs 3 StPO von der Entscheidung über die vorliegende Beschwerde ausgeschlossen.

| Predicted | Gold |
|---|---|
| `Dr. Schwab` | `Dr. Schwab` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)

**Example 88** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_11`)


Hofrat des Obersten Gerichtshofs Dr. Nordmeyer tritt aufgrund der laufenden Vertretungsregelung der Geschäftsverteilung des Obersten Gerichtshofs anstelle der nunmehr als Vorsitzende einschreitenden Hofrätin des Obersten Gerichtshofs Dr. Bachner-Foregger (§ 45 Abs 2 StPO).

| Predicted | Gold |
|---|---|
| `Dr. Nordmeyer` | `Dr. Nordmeyer` |
| `Dr. Bachner-Foregger` | `Dr. Bachner-Foregger` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 89** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_3`)


Kopf Der Oberste Gerichtshof hat am 11. März 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Dr. Oshidari als weitere Richter in der Strafsache gegen Gerhard Bukowska wegen des Verbrechens des schweren gewerbsmäßigen Betrugs nach §§ 146, 147 Abs 3, 148 erster Fall, 15 Abs 1 StGB und weiterer strafbarer Handlungen, AZ 16 Hv 20/14x des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätin des Obersten Gerichtshofs Mag. Michel gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `Dr. Oshidari` | `Dr. Oshidari` |
| `Dr. Schwab` | `Dr. Schwab` |
| `Mag. Michel` | `Mag. Michel` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Gerhard Bukowska` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `OGH` (organisation)

**Example 90** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_4`)


2005 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab und Hofrätin des Obersten Gerichtshofs Mag. Michel sind von der Entscheidung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Gerhard Boesl betreffend das Verfahren AZ 16 Hv20/14x des Landesgerichts für Strafsachen Wien ausgeschlossen.

| Predicted | Gold |
|---|---|
| `Dr. Schwab` | `Dr. Schwab` |
| `Mag. Michel` | `Mag. Michel` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Gerhard Boesl` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 91** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_5`)


An deren Stelle treten Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski.

| Predicted | Gold |
|---|---|
| `Dr. Nordmeyer` | `Dr. Nordmeyer` |
| `Dr. Michel-Kwapinski` | `Dr. Michel-Kwapinski` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 92** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_7`)


Senatspräsident des Obersten Gerichtshofs Dr. Schwab ist Vorsitzender, Hofrätin des Obersten Gerichtshofs Mag. Michel ist Mitglied des zuständigen 11.

| Predicted | Gold |
|---|---|
| `Dr. Schwab` | `Dr. Schwab` |
| `Mag. Michel` | `Mag. Michel` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 93** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_9`)


1. Senatspräsident des Obersten Gerichtshofs Dr. Schwab zeigt seine Ausgeschlossenheit unter Hinweis auf die (Vor-)Entscheidung des Obersten Gerichtshofs vom 8. August 2013, GZ 12 Ns 48/13z-3, sowie den Umstand an, dass er mit Senatspräsidentin des Oberlandesgerichts Wien Dr. Christine Schwab, die an mehreren (vom Anzeiger im einzelnen bezeichneten) früheren Entscheidungen dieses Gerichts in dieser Sache mit Bezug auf die Prüfung des Tatverdachts teilgenommen hat, im Angehörigenverhältnis des § 72 StGB stehe.

| Predicted | Gold |
|---|---|
| `Dr. Schwab` | `Dr. Schwab` |
| `Dr. Christine Schwab` | `Dr. Christine Schwab` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 94** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_15`)


Senatspräsident des Obersten Gerichtshofs Dr. Schwab ist damit von der Entscheidung über das vorliegende Rechtsmittel ausgeschlossen.

| Predicted | Gold |
|---|---|
| `Dr. Schwab` | `Dr. Schwab` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)

**Example 95** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_16`)


2. Hofrätin des Obersten Gerichtshofs Mag. Michel war in diesem Verfahren zu 1 OStA 74/08s als Staatsanwältin tätig, sodass sie gemäß § 43 Abs 1 Z 1 StPO als Richterin vom gesamten Verfahren ausgeschlossen ist.

| Predicted | Gold |
|---|---|
| `Mag. Michel` | `Mag. Michel` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)

**Example 96** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_17`)


3. An die Stelle der Ausgeschlossenen treten aufgrund der laufenden Vertretungsregelung Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski. (§ 45 Abs 2 StPO).

| Predicted | Gold |
|---|---|
| `Dr. Nordmeyer` | `Dr. Nordmeyer` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 97** (doc_id: `deanon_260716_TRAIN/12Ns94_11m`) (sent_id: `deanon_260716_TRAIN/12Ns94_11m_3`)


Kopf Der Oberste Gerichtshof hat am 28. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in der Strafsache gegen Mag. Herwig Bernts wegen des Vergehens des Widerstands gegen die Staatsgewalt nach § 269 Abs 1 erster Fall StGB und anderer strafbarer Handlungen, AZ 20 Hv 38/11f des Landesgerichts Linz, über den Antrag des Angeklagten auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

| Predicted | Gold |
|---|---|
| `Dr. Michel-Kwapinski` | `Dr. Michel-Kwapinski` |
| `Mag. Herwig Bernts` | `Mag. Herwig Bernts` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Landesgerichts Linz` (organisation)
- `OGH` (organisation)

**Example 98** (doc_id: `deanon_260716_TRAIN/12Ns94_11m`) (sent_id: `deanon_260716_TRAIN/12Ns94_11m_6`)


Der nunmehr vorliegende Antrag des Mag. Herwig Billmeir enthält gegenüber seinen früheren Anträgen kein neues Vorbringen, weshalb er zurückzuweisen war (res iudicata).

| Predicted | Gold |
|---|---|
| `Mag. Herwig Billmeir` | `Mag. Herwig Billmeir` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_19`)


DasRekursgerichtgab dem Rekurs der beiden Minderjährigen Folge und änderte die Beschlüsse des Erstgerichts jeweils dahin ab, dass den Minderjährigen auch für den Monat Februar 2010 monatliche Unterhaltsvorschüsse in Höhe von 210 EUR (für den minderjährigen Ariadne Jefferys ) und von 180 EUR (für die minderjährige OStR Univ.-Prof.in Sascha Elfferding ) gewährt wurden.

**False Positives:**

- `OStR Univ` — partial — pred is substring of gold: `OStR Univ.-Prof.in Sascha Elfferding`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ariadne Jefferys`(person)
- `OStR Univ.-Prof.in Sascha Elfferding`(person)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Eva Abdelrahman, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei Hochenadel Immobilien GmbH, Ritterhof 11, 2661 Graben, Österreich, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Karl-Heinz` — partial — pred is substring of gold: `Dr. Karl-Heinz Plankel`

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

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr.Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei AXA Software Institut Gesellschaft mbH, Fuchsgrabengasse 27K, 8330 Untergiem, Österreich, vertreten durch Mag. Oliver Simoncic, Rechtsanwalt in St. Pölten, gegen die beklagten Parteien 1.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr.Neumayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr.Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Mag. Korn`(person)
- `AXA Software Institut Gesellschaft mbH`(organisation)
- `Fuchsgrabengasse 27K, 8330 Untergiem, Österreich`(address)
- `Mag. Oliver Simoncic`(person)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_9`)


Senat in der Besetzung Senatspräsidentin Dr. Sandra Hilt, Mag. Manuel Kumas und MMMag. Gottfried Fegbeitel mit Beschluss vom 3. 8. 2009, AZ 11 R 105/09f, keine Folge und verhängte über den Ablehnungswerber wegen beleidigender Äußerungen im Rechtsmittel eine Ordnungsstrafe von 1.600 EUR.

**False Positives:**

- `MMag. Gottfried Fegbeitel` — partial — pred is substring of gold: `MMMag. Gottfried Fegbeitel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Sandra Hilt`(person)
- `Mag. Manuel Kumas`(person)
- `MMMag. Gottfried Fegbeitel`(person)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Jaden Meyerjohann, geboren am 3. Juli 2020, Leroy Jungschmidt, geboren am 28. Mai 1965 und Clemens Theocharakis, geboren am 25. März 1999, in Pflege und Erziehung der Mutter Emanuela Janischefsky, vertreten durch das Land Vorarlberg als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Feldkirch, Schlossgraben 1, 6800 Feldkirch), wegen Gewährung von Unterhaltsvorschuss, über den Revisionsrekurs des Vaters Ashley Biesert, vertreten durch Mag. Hans-Christian Obernberger, Rechtsanwalt in Feldkirch, gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 12. Juli 2011, GZ 3 R 198/11g, 3 R 199/11d, 3 R 200/11a-18, womit die Beschlüsse des Bezirksgerichts Feldkirch vom 18. Mai 2011, GZ 12 Pu 141/11f-4 bis 6, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Mag. Hans-Christian` — partial — pred is substring of gold: `Mag. Hans-Christian Obernberger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Jaden Meyerjohann`(person)
- `3. Juli 2020`(date)
- `Leroy Jungschmidt`(person)
- `28. Mai 1965`(date)
- `Clemens Theocharakis`(person)
- `25. März 1999`(date)
- `Emanuela Janischefsky`(person)
- `Bezirkshauptmannschaft Feldkirch`(organisation)
- `Ashley Biesert`(person)
- `Mag. Hans-Christian Obernberger`(person)
- `Landesgerichts Feldkirch`(organisation)
- `Bezirksgerichts Feldkirch`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende, den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber sowie die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Leander Andermann, vertreten durch Dr. Martin Leitner, Rechtsanwalt in Wien, gegen die beklagte Partei Ing. Ferdinand Abramova, vertreten durch Mag. Wilhelm Deutschmann MBA und Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M., Rechtsanwälte in Linz, wegen 500.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 11. Mai 2022, GZ 2 R 64/22b-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Mag. Wilhelm Deutschmann` — partial — pred is substring of gold: `Mag. Wilhelm Deutschmann MBA`
- `Priv.-Doz. Mag` — partial — pred is substring of gold: `Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M.`
- `Dr. Henriette Boscheinen-Duursma` — partial — pred is substring of gold: `Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M.`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Mag. Schober`(person)
- `Dr. Annerl`(person)
- `Leander Andermann`(person)
- `Dr. Martin Leitner`(person)
- `Ing. Ferdinand Abramova`(person)
- `Mag. Wilhelm Deutschmann MBA`(person)
- `Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M.`(person)
- `Oberlandesgerichts Linz`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Ob3_12g`) (sent_id: `deanon_260716_TRAIN/10Ob3_12g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Maja Pirkmayr, vertreten durch Dr. Georg Gorton und DDr. Birgit Gorton, Rechtsanwälte in Klagenfurt, gegen die beklagte Partei Ing. Emanuel Puff, vertreten durch Dr. Gottfried Kassin, Rechtsanwalt in St. Veit an der Glan, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 26. Mai 2011, GZ 2 R 83/11z-49, mit dem das Urteil des Bezirksgerichts St. Veit an der Glan vom 29. Oktober 2010, GZ 3 C 333/09h-34, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Birgit Gorton` — partial — pred is substring of gold: `DDr. Birgit Gorton`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Maja Pirkmayr`(person)
- `Dr. Georg Gorton`(person)
- `DDr. Birgit Gorton`(person)
- `Ing. Emanuel Puff`(person)
- `Dr. Gottfried Kassin`(person)
- `Landesgerichts Klagenfurt`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Ob41_14y`) (sent_id: `deanon_260716_TRAIN/10Ob41_14y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in den verbundenen Familienrechtssachen des Antragstellers DI Dr. Bodo Kaczynski, geboren am 25. Juli 1975, vertreten durch Mag. Werner Thurner, Rechtsanwalt in Graz, gegen die Antragsgegnerinnen 1. Wolfgang Lombardini, geboren am 4. Dezember 2022, 2. Livia Löblein, geboren am 11. Januar 1966, vertreten durch Mörth Ecker Filzmaier, Rechtsanwalts-Partnerschaft in Graz, wegen Unterhalt, über den Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 24. September 2013, GZ 2 R 11/13x-76, womit der Beschluss des Bezirksgerichts Graz-Ost vom 26. November 2012, GZ 231 Fam 14/11a, 231 Fam 17/11t, 231 Fam 18/11i-60, teilweise bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.  Text Begründung: DasErstgerichtsetzte den monatlichen Unterhalt für die Erstantragsgegnerin ab 1. 2. 2011 von 390 EUR um 30 EUR auf 360 EUR herab (Punkt 1);

**False Positives:**

- `Dr. Bodo Kaczynski` — partial — pred is substring of gold: `DI Dr. Bodo Kaczynski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `DI Dr. Bodo Kaczynski`(person)
- `25. Juli 1975`(date)
- `Mag. Werner Thurner`(person)
- `Wolfgang Lombardini`(person)
- `4. Dezember 2022`(date)
- `Livia Löblein`(person)
- `11. Januar 1966`(date)
- `Mörth Ecker Filzmaier, Rechtsanwalts-Partnerschaft`(organisation)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)
- `Bezirksgerichts Graz-Ost`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Ing. Christian Stangl-Brachnik, MA BA und Mag. Claudia Gründel (beide aus dem Kreis der Arbeitgeber) als weitere Richter in der Sozialrechtssache der klagenden Partei Mathias Jendl, vertreten durch Dr. Thomas Stampfer und Dr. Christoph Orgler, Rechtsanwälte in Graz, gegen die beklagte Partei Sozialversicherungsanstalt der Bauern, 1031 Wien, Ghegastraße 1, vertreten durch Dr. Michael Stögerer, Rechtsanwalt in Wien, wegen Ausgleichszulage, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2017, GZ 7 Rs 37/17s-11, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. April 2017, GZ 43 Cgs 113/17p-7, teils bestätigt und teils abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Ing. Christian Stangl-Brachnik` — partial — pred is substring of gold: `Ing. Christian Stangl-Brachnik, MA BA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Ing. Christian Stangl-Brachnik, MA BA`(person)
- `Mag. Claudia Gründel`(person)
- `Mathias Jendl`(person)
- `Dr. Thomas Stampfer`(person)
- `Dr. Christoph Orgler`(person)
- `Dr. Michael Stögerer`(person)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/10ObS99_15d`) (sent_id: `deanon_260716_TRAIN/10ObS99_15d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die fachkundigen Laienrichter Mag. Dr. Wolfgang Höfle (aus dem Kreis der Arbeitgeber) und Ing. Thomas Bauer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Willibald Kollowrat, BEd, vertreten durch Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH in Graz, gegen die beklagte Partei Versicherungsanstalt für Eisenbahnen und Bergbau, Linke Wienzeile 48-52, 1060 Wien, vertreten durch Dr. Marie-Luise Safranek, Rechtsanwältin in Graz, wegen Wochengeld, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Juni 2015, GZ 7 Rs 28/15i-9, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 25. Februar 2015, GZ 36 Cgs 216/14d-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Reinhard Tögl Rechtsanwaltsgesellschaft` — partial — pred is substring of gold: `Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH`
- `Dr. Marie-Luise` — partial — pred is substring of gold: `Dr. Marie-Luise Safranek`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Mag. Dr. Wolfgang Höfle`(person)
- `Ing. Thomas Bauer`(person)
- `Willibald Kollowrat, BEd`(person)
- `Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH`(organisation)
- `Versicherungsanstalt für Eisenbahnen und Bergbau`(organisation)
- `Dr. Marie-Luise Safranek`(person)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_17`)


3. An die Stelle der Ausgeschlossenen treten aufgrund der laufenden Vertretungsregelung Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski. (§ 45 Abs 2 StPO).

**False Positives:**

- `Dr. Michel-Kwapinski` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Obersten Gerichtshofs`(organisation)

</details>

---

## `Complex Title` 🏆

**F1:** 0.149 | **Precision:** 0.941 | **Recall:** 0.081  

**Format:** `regex`  
**Rule ID:** `1b2723fb`  
**Description:**
Matches complex academic/legal titles (Mag., Dr., Prof., etc.) followed by full names, including hyphenated names and combined titles.

**Content:**
```
(?:Hon\.-Prof\.|Univ\.-Prof\.|Priv\.-Doz\.|Prof\.\s+Dr\.|Dr\.\s+Prof\.|MMag\.|Mag\.\s+Dr\.|Dr\.\s+Mag\.|PhD\s+|DI\s+|Ing\.\s+|OMedR\s+|HR\s+OMedR\s+|VetR\s+Techn\s+|Dipl\.-Ing\.|Bakk\.\s+iur\.|MBA|BSc|LL\.M\.|RgR|\u00d6kR|StR|OStR|KR|AR|VetR|PD|Prof\.in|Univ\.-Prof\.in|MMag\.in|DDr\.|DDr\.in|Hon\.-Prof\.in|Univ\.-Prof\.in)\s+(?:Dr\.)?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.941 | 0.081 | 0.149 | 358 | 337 | 21 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 337 | 21 | 3838 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Jason Langeloh, vertreten durch die Mag. Martin Rützler, Rechtsanwalt in Dornbirn, gegen die beklagte Partei, Selma Einoeder, vertreten durch Mag. Alexander Gerngross und Mag. Klaus Köck, Rechtsanwälte in Premstätten bei Graz, wegen 6.795,66 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 223 C 1313/24w des Bezirksgerichts Graz-Ost den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an das Bezirksgericht Dornbirn wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Nowotny` | `Hon.-Prof. Dr. Nowotny` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Schober` (person)
- `Dr. Vollmaier` (person)
- `Jason Langeloh` (person)
- `Mag. Martin Rützler` (person)
- `Selma Einoeder` (person)
- `Mag. Alexander Gerngross` (person)
- `Mag. Klaus Köck` (person)
- `Bezirksgerichts Graz-Ost` (organisation)
- `Bezirksgericht Dornbirn` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Kordelia Meelis, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Fatima Tengel, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Kordelia Meelis` (person)
- `Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft` (organisation)
- `Fatima Tengel` (person)
- `Mag. Ernst Michael Lang` (person)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der beim Landesgericht Linz zu AZ 3 Cg 46/21a anhängigen Rechtssache der klagenden Partei Hollengk Planung GmbH, Am Steindl 3, 9873 Döbriach, Österreich, vertreten durch Huber Berchtold Rechtsanwälte OG in Wien, gegen die beklagte Partei Wind Nexheimval GmbH, Wiesbergsiedlung 4, 8341 Pöllau, Österreich, vertreten durch ScherbaumSeebacher Rechtsanwälte GmbH in Graz, wegen 188.117,55 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN folgenden Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, zur Verhandlung und Entscheidung der Rechtssache anstelle des Landesgerichts Linz das Landesgericht Korneuburg zu bestimmen, wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Landesgericht Linz` (organisation)
- `Hollengk Planung GmbH` (organisation)
- `Am Steindl 3, 9873 Döbriach, Österreich` (address)
- `Huber Berchtold Rechtsanwälte OG` (organisation)
- `Wind Nexheimval GmbH` (organisation)
- `Wiesbergsiedlung 4, 8341 Pöllau, Österreich` (address)
- `ScherbaumSeebacher Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Linz` (organisation)
- `Landesgericht Korneuburg` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Schramm als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Florens Drehkopf, LLB, geboren am 16. Dezember 1952, AZ 7 P 203/15g des Bezirksgerichts Mödling, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Mödling zurückgestellt.  Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Florens Drehkopf, LLB` (person)
- `16. Dezember 1952` (date)
- `Bezirksgerichts Mödling` (organisation)
- `Bezirksgericht Mödling` (organisation)
- `Bezirksgericht Mödling` (organisation)
- `Bezirksgericht Judenburg` (organisation)
- `Bezirksgerichts Judenburg` (organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin mj Dietlind Schiewick, geboren 23. Oktober 2017, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Vöcklabruck, 4840 Vöcklabruck, Sportplatzstraße 1–3), deren Mutter Gisela Akcakaya, MSc, und des Antragsgegners Ernst Hartjens, Russische Föderation, wegen Feststellung der Abstammung, aufgrund der vom Bezirksgericht Josefstadt verfügten Vorlage des Akts AZ 23 Fam 2/21y zur Entscheidung gemäß § 111 Abs 2 JN den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Villach zurückgestellt.  Text Begründung: [1] Gegenstand des Verfahrens ist der Antrag auf Feststellung der Abstammung der zum Zeitpunkt der Antragstellung am 24.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fichtenau` (person)
- `Mag. Ziegelbauer` (person)
- `Dietlind Schiewick` (person)
- `23. Oktober` (date)
- `Bezirkshauptmannschaft Vöcklabruck` (organisation)
- `Gisela Akcakaya, MSc` (person)
- `Ernst Hartjens` (person)
- `Bezirksgericht Josefstadt` (organisation)
- `Bezirksgericht Villach` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie durch die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Hon.-Prof.in KzlR Iris Makowska, vertreten durch Skribe Rechtsanwaelte GmbH in Wien, gegen die beklagte Partei Dieter Apfelbacher Ltd, Am Fundbach 31w, 9170 Tratten, Österreich, wegen 400 EUR sA, über den Ordinationsantrag nach § 28 JN in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Hon.-Prof.in KzlR Iris Makowska` (person)
- `Skribe Rechtsanwaelte GmbH` (organisation)
- `Dieter Apfelbacher` (person)
- `Am Fundbach 31w, 9170 Tratten, Österreich` (address)
- `Bezirksgericht Schwechat` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Paulina Nüsken, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Oliver Eylart, Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Paulina Nüsken` (person)
- `Skribe Rechtsanwälte GmbH` (organisation)
- `Oliver Eylart` (person)
- `Bezirksgericht Schwechat` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger und Hon.-Prof. Dr. Neumayr als weitere Richter in der Verlassenschaftssache nach dem am 9. September 2009 verstorbenen, zuletzt in Zum Wetterkreuz 15, 5121 Hofstadt, Österreich, wohnhaft gewesenen Manfred Johann Puff, AZ 1 A 349/09w des Bezirksgerichts Kitzbühel, über den Delegierungsantrag der Karin Ciliberto, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, den B e s c h l u s s gefasst:  Spruch Dem Delegierungsantrag wird stattgegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Neumayr` | `Hon.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Zum Wetterkreuz 15, 5121 Hofstadt, Österreich` (address)
- `Manfred Johann Puff` (person)
- `Bezirksgerichts Kitzbühel` (organisation)
- `Karin Ciliberto` (person)
- `Mag. Maximilian Kocher` (person)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Steidlen+Ysner Daten GmbH, Kaminweg 34, 8200 Laßnitzthal, Österreich, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Verlag Waldlemder GmbH, Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Landesgericht Linz` (organisation)
- `Steidlen+Ysner Daten GmbH` (organisation)
- `Kaminweg 34, 8200 Laßnitzthal, Österreich` (address)
- `Dr. Roland Kassowitz` (person)
- `Verlag Waldlemder GmbH` (organisation)
- `Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich` (address)
- `Prof. Haslinger` (person)
- `Landesgerichts Linz` (organisation)
- `Handelsgericht Wien` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Rechtssache der klagenden Partei Mur Dorftalnex Technologien -GmbH, Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich, vertreten durch Dr. Peter Lechner und Dr. Hermann Pfurtscheller, Rechtsanwälte in Innsbruck, und ihrer Nebenintervenientin Ober Dertri GmbH, Hintereggweg 93, 2070 Kleinhöflein, Österreich, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Rudolf Ketelhut GmbH, Fiebrichgasse 17, 5120 Seeleiten, Österreich, vertreten durch Rechtsanwaltskanzlei Dr. Bernhard Hämmerle GmbH in Innsbruck, und ihrer Nebenintervenientin Völkertz Energie GmbH, Brunnbachweg 19, 4653 Mayersdorf, Österreich, vertreten durch Dr. Franz Pechmann, Rechtsanwalt in Wien, wegen 696.238,34 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck vom 2. Oktober 2009, GZ 4 R 108/09b-167, mit dem das Urteil des Landesgerichts Innsbruck vom 23. Februar 2009, GZ 41 Cg 228/01z-152, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Neumayr` | `Hon.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
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
- `Landesgerichts Innsbruck` (organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Schneidergruberweg 37, 5132 Reith, Österreich, vertreten durch Dr. Alois Schneider, Rechtsanwalt in Rattenberg, wider die beklagte Partei Dario von Ebers, vertreten durch Dr. Walter Hausberger, Dr. Katharina Moritz und Dr. Alfred Schmidt, Rechtsanwälte in Wörgl, wegen Entfernung und Unterlassung (Revisionsinteresse 10.000 EUR), infolge Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 3. November 2017, GZ 3 R 172/17s-22, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Rattenberg vom 17. Mai 2017, GZ 3 C 401/15k-18, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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
- `Landesgerichts Innsbruck` (organisation)
- `Bezirksgerichts Rattenberg` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Eva Abdelrahman, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei Hochenadel Immobilien GmbH, Ritterhof 11, 2661 Graben, Österreich, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Korn` (person)
- `Eva Abdelrahman` (person)
- `Dr. Karl-Heinz Plankel` (person)
- `Hochenadel Immobilien GmbH` (organisation)
- `Ritterhof 11, 2661 Graben, Österreich` (address)
- `Lederer Rechtsanwalt GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Juri Gerstl GmbH, Mutten 18, 3251 Schauboden, Österreich, vertreten durch Dr. Ralph Trischler, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, sowie die Nebenintervenientin auf Seiten der beklagten Partei Bundesbeschaffung GmbH, 1020 Wien, Lassallestraße 9b, vertreten durch die Olischar Rechtsanwaltsgesellschaft mbH in Wien, wegen 15.535 EUR sA, über den Revisionsrekurs der klagenden Partei (Revisionsinteresse: 7.460 EUR), gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 23. Februar 2023, GZ 16 R 168/22a-20, mit welchem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 5. September 2022, GZ 11 Cg 48/22t-12, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Lovrek` | `Hon.-Prof. Dr. Lovrek` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Mag. Schober` (person)
- `Dr. Thunhart` (person)
- `Juri Gerstl` (person)
- `Mutten 18, 3251 Schauboden, Österreich` (address)
- `Dr. Ralph Trischler` (person)
- `Bundesbeschaffung GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des minderjährigen Cedric Annamüller, geboren am 8. März 2007, 16. Mai 1964, vertreten durch das Land Kärnten als Kinder- und Jugendhilfeträger (Magistrat der Landeshauptstadt Klagenfurt, Abteilung für Jugend und Familie, Bahnhofstraße 35, 9010 Klagenfurt am Wörthersee), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Graz, gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 8. Jänner 2016, GZ 4 R 283/15g-16, womit der Beschluss des Bezirksgerichts Klagenfurt vom 17. November 2015, GZ 1 Pu 69/10x-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Ziegelbauer` (person)
- `Cedric Annamüller` (person)
- `8. März` (date)
- `16. Mai 1964` (date)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts Klagenfurt` (organisation)
- `Bezirksgerichts Klagenfurt` (organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludmilla von Amelunxen, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, gegen die beklagte Partei Svetlana Leinhäuser, vertreten durch Dr. Thomas Brückl, Mag. Christian Breit, Rechtsanwälte in Ried im Innkreis, wegen 1.778,52 EUR und Unterlassung (Streitwert 2.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Wels als Berufungsgericht vom 25. Jänner 2023, GZ 21 R 2/23b-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Grieskirchen vom 27. Oktober 2022, GZ 3 C 642/20h-27, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Lovrek` | `Hon.-Prof. Dr. Lovrek` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Mag. Schober` (person)
- `Dr. Annerl` (person)
- `Ludmilla von Amelunxen` (person)
- `Dr. Bernhard Birek` (person)
- `Svetlana Leinhäuser` (person)
- `Dr. Thomas Brückl` (person)
- `Mag. Christian Breit` (person)
- `Landesgerichts Wels` (organisation)
- `Bezirksgerichts Grieskirchen` (organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Mag. Kevin Maassen, vertreten durch Dr. Clemens Lintschinger, Rechtsanwalt in Wien, gegen die beklagte Partei Hon.-Prof. Friedhelm Adde, vertreten durch Mag. Dr. Georg Backhausen, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 27. Jänner 2016, GZ 38 R 265/15z-45, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Ziegelbauer` (person)
- `Mag. Kevin Maassen` (person)
- `Dr. Clemens Lintschinger` (person)
- `Hon.-Prof. Friedhelm Adde` (person)
- `Mag. Dr. Georg Backhausen` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden, die Hofräte Mag. Schober, Dr. Annerl und Dr. Vollmaier sowie die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Ing. Mag. Pamela Gotterbauer, vertreten durch Mag. Helwig Schuster, Rechtsanwalt in Melk, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Nowotny` | `Hon.-Prof. Dr. Nowotny` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Schober` (person)
- `Dr. Annerl` (person)
- `Dr. Vollmaier` (person)
- `Dr. Wallner-Friedl` (person)
- `Ing. Mag. Pamela Gotterbauer` (person)
- `Mag. Helwig Schuster` (person)

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Ralph Prusseit, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Akbayrak Metall GmbH, Schroateck 57, 4710 Niederweng, Österreich, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Nowotny` | `Hon.-Prof. Dr. Nowotny` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. PD Dr. Rassi` (person)
- `Dr. Steger` (person)
- `Dr. Annerl` (person)
- `Dr. Wallner-Friedl` (person)
- `Ralph Prusseit` (person)
- `Mag. Franz Eckl` (person)
- `Akbayrak Metall GmbH` (organisation)
- `Schroateck 57, 4710 Niederweng, Österreich` (address)
- `Skribe Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Krems an der Donau` (organisation)
- `Bezirksgerichts Zwettl` (organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Heimcon Software GmbH, H - Am Hang 3, 4912 Rettenbrunn, Österreich, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, gegen die beklagte Partei Gunter Landwirtschaft GmbH, Schlossfeld 38, 9300 Graßdorf, Österreich, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, wegen 7.731,06 EUR und Feststellung (Streitwert 20.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse insgesamt 11.597,42 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 216/14h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Korn` (person)
- `Heimcon Software GmbH` (organisation)
- `H - Am Hang 3, 4912 Rettenbrunn, Österreich` (address)
- `Vavrovsky Heine Marth Rechtsanwälte GmbH` (organisation)
- `Gunter Landwirtschaft GmbH` (organisation)
- `Schlossfeld 38, 9300 Graßdorf, Österreich` (address)
- `Stolz & Schartner Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Linz` (organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der minderjährigen Annabelle Thurnher, geboren am 24. Juni 2001, vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung, Bezirk 10, 1100 Wien, Van der Nüll-Gasse 20), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 17. September 2009, GZ 44 R 454/09d-38, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Favoriten vom 16. Juni 2009, GZ 40 P 36/08f-U-26, teilweise abgeändert wurde, den B e s c h l u s s gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Neumayr` | `Hon.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Annabelle Thurnher` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei DDr.in Cornelia Rinaldo, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Conmon-Verlag Limited, Kroisegg 20, 4052 Fleckendorf, Österreich Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Mag. Schober` (person)
- `Dr. Annerl` (person)
- `DDr.in Cornelia Rinaldo` (person)
- `Dr. Sven Rudolf Thorstensen` (person)
- `Conmon-Verlag Limited` (organisation)
- `Kroisegg 20, 4052 Fleckendorf, Österreich` (address)
- `Brandl Talos Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der Kinder 1.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)

**Example 22** (doc_id: `deanon_260716_TRAIN/10Ob26_10m`) (sent_id: `deanon_260716_TRAIN/10Ob26_10m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der mj 1.)

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Neumayr` | `Hon.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)

**Example 23** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Brigitte Martz, geboren am 16. November 1978, wegen Kontaktrechts des Vaters Dr. Gustav Thöning, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Madeleine Musialik, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
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
- `Landesgerichts Wiener Neustadt` (organisation)
- `Bezirksgerichts Wiener Neustadt` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/10Ob28_19v`) (sent_id: `deanon_260716_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Bau Zorostfurt GmbH, Isbarystraße 47, 4152 Schölling, Österreich, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Buitenkamp und Rothauge Landwirtschaft GmbH, Gewerbegebiet Mathon 17, 3672 Reitern, Österreich, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Bau Zorostfurt GmbH` (organisation)
- `Isbarystraße 47, 4152 Schölling, Österreich` (address)
- `Dr. Alexandra Slama` (person)
- `Buitenkamp und Rothauge Landwirtschaft GmbH` (organisation)
- `Gewerbegebiet Mathon 17, 3672 Reitern, Österreich` (address)
- `Grassner, Lenz, Thewanger & Partner, Rechtsanwälte` (organisation)
- `Oberlandesgerichts Linz` (organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der zur AZ 38 Nc 13/08i beim Landesgericht für Zivilrechtssachen Wien anhängigen Ablehnungssache des Ablehnungswerbers Mag. Herwig Bortzlaff, über den Rekurs des Ablehnungswerbers gegen den Beschluss des Oberlandesgerichts Wien vom 10. November 2009, GZ 13 Nc 14/09x-2, womit ein Ablehnungsantrag zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Neumayr` | `Hon.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Landesgericht für Zivilrechtssachen Wien` (organisation)
- `Mag. Herwig Bortzlaff` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/10Ob30_19p`) (sent_id: `deanon_260716_TRAIN/10Ob30_19p_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der minderjährigen Maja Dolleschell, geboren 14. August 2009, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Melk, 3390 Melk, Abt Karl-Straße 25a) wegen Unterhaltsvorschüssen, über den Revisionsrekurs des Kindes gegen den Beschluss des Landesgerichts St. Pölten als Rekursgericht vom 23. Jänner 2019, GZ 23 R 6/19h-52, mit dem der Beschluss des Bezirksgerichts Melk vom 21. November 2018, GZ 22 Pu 194/16m-42, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Maja Dolleschell` (person)
- `14. August` (date)
- `Bezirkshauptmannschaft Melk` (organisation)
- `Landesgerichts St. Pölten` (organisation)
- `Bezirksgerichts Melk` (organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende, den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber sowie die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Leander Andermann, vertreten durch Dr. Martin Leitner, Rechtsanwalt in Wien, gegen die beklagte Partei Ing. Ferdinand Abramova, vertreten durch Mag. Wilhelm Deutschmann MBA und Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M., Rechtsanwälte in Linz, wegen 500.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 11. Mai 2022, GZ 2 R 64/22b-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Lovrek` | `Hon.-Prof. Dr. Lovrek` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Mag. Schober` (person)
- `Dr. Annerl` (person)
- `Leander Andermann` (person)
- `Dr. Martin Leitner` (person)
- `Ing. Ferdinand Abramova` (person)
- `Mag. Wilhelm Deutschmann MBA` (person)
- `Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M.` (person)
- `Oberlandesgerichts Linz` (organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
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
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Karim Mielewczik, gegen die beklagte Partei Dr. Sandro Gädecken, vertreten durch Ing. Dr. Stefan Krall und Dr. Oliver Kühnl, Rechtsanwälte in Innsbruck, wegen 9.456 EUR sA (Revisionsinteresse 9.268,50 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 25. Februar 2025, GZ 21 R 434/24f-29, mit dem das Urteil des Bezirksgerichts Seekirchen am Wallersee vom 5. September 2024, GZ 2 C 1107/23d-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Nowotny` | `Hon.-Prof. Dr. Nowotny` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. PD Dr. Rassi` (person)
- `Dr. Annerl` (person)
- `Dr. Vollmaier` (person)
- `Dr. Wallner-Friedl` (person)
- `Karim Mielewczik` (person)
- `Dr. Sandro Gädecken` (person)
- `Ing. Dr. Stefan Krall` (person)
- `Dr. Oliver Kühnl` (person)
- `Landesgerichts Salzburg` (organisation)
- `Bezirksgerichts Seekirchen` (organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Parteien 2.)

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)

**Example 31** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Pflegschaftssache 1. der mj Emma Mittelstaedt, geboren am 21. Mai 2025 und 2. des mj Milena Roesche, geboren am 25. Juni 1957, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung Bezirk 22, 1220 Wien, Hirschstettner Straße 19-21/Stiege N), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 10. Dezember 2014, GZ 42 R 343/13x, 42 R 344/13v und 42 R 345/13s-106, womit den Rekursen der Minderjährigen gegen den Beschluss des Bezirksgerichts Donaustadt vom 14. März 2013, GZ 3 Pu 61/12x-40, teilweise Folge gegeben wurde (Pkt 1 des Spruchs), dem Rekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen die Beschlüsse des Bezirksgerichts Donaustadt (jeweils) vom 6. Juni 2013, GZ 3 Pu 61/12x-49 und 3 Pu 61/12x-50, Folge gegeben (Pkt 2a des Spruchs), und aus Anlass des Rekurses die Anträge der Minderjährigen auf Gewährung von Unterhaltsvorschüssen zur Gänze abgewiesen wurden (Pkt 2b des Spruchs), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Korn` (person)
- `Emma Mittelstaedt` (person)
- `21. Mai 2025` (date)
- `Milena Roesche` (person)
- `25. Juni 1957` (date)
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)

**Example 32** (doc_id: `deanon_260716_TRAIN/10Ob43_19z`) (sent_id: `deanon_260716_TRAIN/10Ob43_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Othmar Mertl, vertreten durch Nitsch Pajor Zöllner Rechtsanwälte OG in Mödling, gegen die beklagte Partei Stadtgemeinde Malik Fridt, vertreten durch Krist Bubits Rechtsanwälte OG in Mödling, wegen 1.) 21.216,92 EUR sA und 2.) Feststellung (Streitwert: 2.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Februar 2019, GZ 12 R 96/18b-36, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Wiener Neustadt vom 31. August 2018, GZ 20 Cg 86/17h-31, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Othmar Mertl` (person)
- `Nitsch Pajor Zöllner Rechtsanwälte OG` (organisation)
- `Malik Fridt` (person)
- `Krist Bubits Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 33** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und den Hofrat Dr. Schramm, die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin Scarlett Achatzi, gegen den Antragsgegner Mag. Ewald Aszmutat, wegen Unterhalt, infolge Rekurses des Antragsgegners gegen den Beschluss des Oberlandesgerichts Wien vom 4. Jänner 2017, GZ 12 Nc 28/16h-3, womit der Ablehnungsantrag des Antragsgegners zurückgewiesen wurde, sowie über den Ablehnungsantrag gegen alle Richter des Oberlandesgerichts Wien, folgenden Beschluss gefasst:  Spruch 1.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Scarlett Achatzi` (person)
- `Mag. Ewald Aszmutat` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 34** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Cassandra Wespi, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Bilek Lebensmittel GmbH in Liqu, Dreijochgasse 11, 4722 Stefansdorf, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `DI Cassandra Wespi` (person)
- `Vogl Rechtsanwalt GmbH` (organisation)
- `Bilek Lebensmittel GmbH` (organisation)
- `Dreijochgasse 11, 4722 Stefansdorf, Österreich` (address)
- `Wess Kux Kispert & Eckert Rechtsanwalts GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 35** (doc_id: `deanon_260716_TRAIN/10Ob6_24s`) (sent_id: `deanon_260716_TRAIN/10Ob6_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Dr. Weber, Mag. Schober, Dr. Annerl und Dr. Vollmaier als weitere Richter in der Rechtssache des (ehemaligen) Klägers und Gegners der gefährdeten Parteien Agatha von der Heide, vertreten durch MMag. Dr. Sebastian Pribas, Rechtsanwalt in Dornbirn, als Verfahrenshelfer, dieser vertreten durch Mag. Benedikt Walch, Rechtsanwalt in Lech am Arlberg, gegen die (ehemals) Beklagte und erstgefährdete Partei Alva Sengül, sowie die zweitgefährdete Partei mj Selina Birkmeir, und die drittgefährdete Partei mj Harald Ladwig, LLM, alle wohnhaft in In der Klaus 72, 4785 Bach, Österreich, und vertreten durch Mag. German Bertsch, Rechtsanwalt in Feldkirch, wegen Ehescheidung sowie einstweiligem Ehegatten- und Kindesunterhalt, über den außerordentlichen Revisionsrekurs des Gegners der gefährdeten Parteien gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 22. September 2022, GZ 3 R 187/22f-323, womit der Beschluss des Bezirksgerichts Feldkirch vom 29. April 2022, GZ 2 C 23/17g-306, bestätigt wurde, den Beschluss gefasst:  Spruch In Ansehung der auf Zahlung von einstweiligem Ehegattenunterhalt gerichteten Begehren wird der außerordentliche Revisionsrekurs gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Nowotny` | `Hon.-Prof. Dr. Nowotny` |
| `MMag. Dr. Sebastian Pribas` | `MMag. Dr. Sebastian Pribas` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Weber` (person)
- `Mag. Schober` (person)
- `Dr. Annerl` (person)
- `Dr. Vollmaier` (person)
- `Agatha von der Heide` (person)
- `Mag. Benedikt Walch` (person)
- `Alva Sengül` (person)
- `Selina Birkmeir` (person)
- `Harald Ladwig, LLM` (person)
- `In der Klaus 72, 4785 Bach, Österreich` (address)
- `Mag. German Bertsch` (person)
- `Landesgerichts Feldkirch` (organisation)
- `Bezirksgerichts Feldkirch` (organisation)

**Example 36** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Ing. Christian Stangl-Brachnik, MA BA und Mag. Claudia Gründel (beide aus dem Kreis der Arbeitgeber) als weitere Richter in der Sozialrechtssache der klagenden Partei Mathias Jendl, vertreten durch Dr. Thomas Stampfer und Dr. Christoph Orgler, Rechtsanwälte in Graz, gegen die beklagte Partei Sozialversicherungsanstalt der Bauern, 1031 Wien, Ghegastraße 1, vertreten durch Dr. Michael Stögerer, Rechtsanwalt in Wien, wegen Ausgleichszulage, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2017, GZ 7 Rs 37/17s-11, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. April 2017, GZ 43 Cgs 113/17p-7, teils bestätigt und teils abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Ing. Christian Stangl-Brachnik, MA BA` (person)
- `Mag. Claudia Gründel` (person)
- `Mathias Jendl` (person)
- `Dr. Thomas Stampfer` (person)
- `Dr. Christoph Orgler` (person)
- `Dr. Michael Stögerer` (person)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)

**Example 37** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Roland Soukup, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Dr. Gabriele Griehsel` (person)
- `Dr. Wolfgang Kozak` (person)
- `Roland Soukup` (person)
- `Mahringer Steinwender Bestebner Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Salzburg` (organisation)

**Example 38** (doc_id: `deanon_260716_TRAIN/10ObS99_15d`) (sent_id: `deanon_260716_TRAIN/10ObS99_15d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die fachkundigen Laienrichter Mag. Dr. Wolfgang Höfle (aus dem Kreis der Arbeitgeber) und Ing. Thomas Bauer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Willibald Kollowrat, BEd, vertreten durch Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH in Graz, gegen die beklagte Partei Versicherungsanstalt für Eisenbahnen und Bergbau, Linke Wienzeile 48-52, 1060 Wien, vertreten durch Dr. Marie-Luise Safranek, Rechtsanwältin in Graz, wegen Wochengeld, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Juni 2015, GZ 7 Rs 28/15i-9, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 25. Februar 2015, GZ 36 Cgs 216/14d-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Mag. Dr. Wolfgang Höfle` (person)
- `Ing. Thomas Bauer` (person)
- `Willibald Kollowrat, BEd` (person)
- `Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH` (organisation)
- `Versicherungsanstalt für Eisenbahnen und Bergbau` (organisation)
- `Dr. Marie-Luise Safranek` (person)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)

**Example 39** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_3`)


Kopf Der Oberste Gerichtshof hat am 16. März 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Brenner in der Strafvollzugssache des Oliver Pekarek, AZ 39 Ns 43/15i des Landesgerichts Krems an der Donau, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Schroll` | `Hon.-Prof. Dr. Schroll` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Brenner` (person)
- `Oliver Pekarek` (person)
- `Landesgerichts Krems an der Donau` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `OGH` (organisation)

**Example 40** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_3`)


Kopf Der Oberste Gerichtshof hat am 11. März 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Dr. Oshidari als weitere Richter in der Strafsache gegen Gerhard Bukowska wegen des Verbrechens des schweren gewerbsmäßigen Betrugs nach §§ 146, 147 Abs 3, 148 erster Fall, 15 Abs 1 StGB und weiterer strafbarer Handlungen, AZ 16 Hv 20/14x des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätin des Obersten Gerichtshofs Mag. Michel gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Schroll` | `Hon.-Prof. Dr. Schroll` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Dr. Oshidari` (person)
- `Gerhard Bukowska` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Michel` (person)
- `OGH` (organisation)

**Example 41** (doc_id: `deanon_260716_TRAIN/12Ns94_11m`) (sent_id: `deanon_260716_TRAIN/12Ns94_11m_3`)


Kopf Der Oberste Gerichtshof hat am 28. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in der Strafsache gegen Mag. Herwig Bernts wegen des Vergehens des Widerstands gegen die Staatsgewalt nach § 269 Abs 1 erster Fall StGB und anderer strafbarer Handlungen, AZ 20 Hv 38/11f des Landesgerichts Linz, über den Antrag des Angeklagten auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Schroll` | `Hon.-Prof. Dr. Schroll` |
| `Hon.-Prof. Dr. Kirchbacher` | `Hon.-Prof. Dr. Kirchbacher` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Herwig Bernts` (person)
- `Landesgerichts Linz` (organisation)
- `OGH` (organisation)

**Example 42** (doc_id: `deanon_260716_TRAIN/12Os152_12p`) (sent_id: `deanon_260716_TRAIN/12Os152_12p_3`)


Kopf Der Oberste Gerichtshof hat am 13. Dezember 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Fruhmann als Schriftführerin in der Strafsache gegen unbekannte Täter wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB, AZ 130 Bl 65/12s des Landesgerichts für Strafsachen Wien, über die Beschwerde des Gebhard Sayin gegen den Beschluss des Oberlandesgerichts Wien vom 23. Oktober 2012, AZ 17 Bs 410/12m, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Schroll` | `Hon.-Prof. Dr. Schroll` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Michel` (person)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Fruhmann` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Gebhard Sayin` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/12Os17_18v`) (sent_id: `deanon_260716_TRAIN/12Os17_18v_3`)


Kopf Der Oberste Gerichtshof hat am 15. März 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. T. Solé, Dr. Oshidari, Dr. Michel-Kwapinski und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Ettel als Schriftführerin in der Maßnahmenvollzugssache des Andreas Wegele, AZ 181 BE 143/17y des Landesgerichts für Strafsachen Wien, über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien vom 9. Jänner 2018, AZ 131 Bs 370/17z, und seinen Antrag auf Bewilligung der Verfahrenshilfe nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Schroll` | `Hon.-Prof. Dr. Schroll` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Dr. Oshidari` (person)
- `Dr. Michel-Kwapinski` (person)
- `Dr. Brenner` (person)
- `Mag. Ettel` (person)
- `Andreas Wegele` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 44** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__3`)


Kopf Der Oberste Gerichtshof hat am 10. Juni 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Holzweber als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll, Dr. Schwab, Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Gotsmy als Schriftführer in der Strafsache gegen Jennifer Janauscheck wegen des Vergehens des Raufhandels nach § 91 Abs 2 zweiter Fall StGB über die von der Generalprokuratur gegen das Urteil des Bezirksgerichts Kufstein vom 30. Jänner 2008, GZ 3 U 166/07x-49, und den unter einem gefassten Beschluss gemäß § 494a Abs 1 Z 2 StPO erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Eisenmenger, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Schroll` | `Hon.-Prof. Dr. Schroll` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Holzweber` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Hetlinger` (person)
- `Mag. Gotsmy` (person)
- `Jennifer Janauscheck` (person)
- `Bezirksgerichts Kufstein` (organisation)
- `Dr. Eisenmenger` (person)

**Example 45** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_3`)


Kopf Der Oberste Gerichtshof hat am 8. April 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Holzweber als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll, Dr. Schwab, Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger in Gegenwart der Richteramtsanwärterin Mag. Bayer als Schriftführerin in der Strafsache gegen Dr. Ernst-Peter Nepomuk Lieschke wegen des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB über die Beschwerde des Verurteilten gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 19. Jänner 2010, AZ 20 Bs 461/09d (GZ 20 Hv 73/09p-19 des Landesgerichts St. Pölten), nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Schroll` | `Hon.-Prof. Dr. Schroll` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Holzweber` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Hetlinger` (person)
- `Mag. Bayer` (person)
- `Dr. Ernst` (person)
- `Nepomuk Lieschke` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts St. Pölten` (organisation)

**Example 46** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_3`)


Kopf Der Oberste Gerichtshof hat am 20. Juni 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Müller als Schriftführerin in der Strafsache gegen Maximilian Gompertz wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB und anderer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Graz als Jugendschöffengericht vom 10. Dezember 2012, GZ 14 Hv 110/12b-39, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Schroll` | `Hon.-Prof. Dr. Schroll` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Michel` (person)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Müller` (person)
- `Maximilian Gompertz` (person)
- `Landesgerichts für Strafsachen Graz` (organisation)

**Example 47** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_3`)


Kopf Der Oberste Gerichtshof hat am 5. März 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden, die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Brenner als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Kaltenbrunner als Schriftführerin in der Strafsache gegen Johannes Barkhof wegen des Vergehens der fortgesetzten Gewaltausübung nach § 107b Abs 1 und Abs 2 StGB und weiterer strafbarer Handlungen, AZ 51 Hv 32/13i des Landesgerichts Feldkirch, über die von der Generalprokuratur gegen den Beschluss des genannten Gerichts vom 4. Mai 2014, GZ 51 Hv 32/13i-35, und weitere Vorgänge erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Eisenmenger, und der Verteidigerin Mag. Reisinger zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Schroll` | `Hon.-Prof. Dr. Schroll` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Dr. Brenner` (person)
- `Mag. Kaltenbrunner` (person)
- `Johannes Barkhof` (person)
- `Landesgerichts Feldkirch` (organisation)
- `Dr. Eisenmenger` (person)
- `Mag. Reisinger` (person)

**Example 48** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_3`)


Kopf Der Oberste Gerichtshof hat am 14. August 2014 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, die Hofräte des Obersten Gerichtshofs Dr. Lässig, Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Anscheringer als Schriftführer in der Strafsache gegen Natascha von Bohr wegen Vergehen des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 erster und zweiter Fall, Abs 2 SMG in dem zu AZ 18 U 198/14k des Bezirksgerichts Innere Stadt Wien und AZ 18 U 266/14m des Bezirksgerichts Linz zwischen diesen Gerichten geführten Zuständigkeitsstreit den Beschluss gefasst:  Spruch Das Hauptverfahren ist vom Bezirksgericht Linz zu führen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Kirchbacher` | `Hon.-Prof. Dr. Kirchbacher` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
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
- `Bezirksgericht Linz` (organisation)

**Example 49** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__3`)


Kopf Der Oberste Gerichtshof hat am 11. Oktober 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Nikola Manderscheidt wegen des Vergehens des schweren Betrugs nach §§ 12 dritter Fall, 146, 147 Abs 1 Z 1 StGB, AZ 41 Hv 49/15k des Landesgerichts Salzburg, über die von der Generalprokuratur gegen das Urteil des Landesgerichts Salzburg vom 28. Oktober 2015, GZ 41 Hv 49/15k-33, und den unter einem gefassten Beschluss auf Absehen vom Widerruf einer bedingten Strafnachsicht erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin MMag. Jenichl, des Verurteilten sowie seines Verteidigers Mag. Wolm zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Kirchbacher` | `Hon.-Prof. Dr. Kirchbacher` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Mag. Wetter` (person)
- `Nikola Manderscheidt` (person)
- `Landesgerichts Salzburg` (organisation)
- `Landesgerichts Salzburg` (organisation)
- `MMag. Jenichl` (person)
- `Mag. Wolm` (person)

**Example 50** (doc_id: `deanon_260716_TRAIN/13Os126_17d`) (sent_id: `deanon_260716_TRAIN/13Os126_17d_3`)


Kopf Der Oberste Gerichtshof hat am 6. Dezember 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Schuber als Schriftführer in der Strafsache gegen Mehdi Rekemeyer wegen des Verbrechens des Raubes nach §§ 15, 142 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 19. Juli 2017, GZ 63 Hv 56/17d-44, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Anordnung von Bewährungshilfe nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Kirchbacher` | `Hon.-Prof. Dr. Kirchbacher` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Mag. Schuber` (person)
- `Mehdi Rekemeyer` (person)
- `Landesgerichts Salzburg` (organisation)

**Example 51** (doc_id: `deanon_260716_TRAIN/13Os155_15s`) (sent_id: `deanon_260716_TRAIN/13Os155_15s_3`)


Kopf Der Oberste Gerichtshof hat am 9. März 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtswärters Mag. Schönmann als Schriftführer in der Strafsache gegen Thomas Enulait wegen des Verbrechens des schweren sexuellen Missbrauchs von Unmündigen nach § 206 Abs 1 und 3 erster Fall StGB sowie weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts St. Pölten als Schöffengericht vom 1. September 2015, GZ 20 Hv 13/15y-53, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde und die Berufung wegen des Ausspruchs über die Schuld werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Kirchbacher` | `Hon.-Prof. Dr. Kirchbacher` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Mag. Schönmann` (person)
- `Thomas Enulait` (person)
- `Landesgerichts St. Pölten` (organisation)

**Example 52** (doc_id: `deanon_260716_TRAIN/13Os16_15z`) (sent_id: `deanon_260716_TRAIN/13Os16_15z_3`)


Kopf Der Oberste Gerichtshof hat am 25. Februar 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Bachl als Schriftführerin in der Strafsache gegen Mag. Johanna Fletcher wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB, AZ 3 St 166/14k der Staatsanwaltschaft Wels, über die Beschwerde des Herbert Onesseit gegen den Beschluss des Oberlandesgerichts Linz vom 9. Jänner 2015, AZ 7 Bs 218/14d (ON 12), nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Kirchbacher` | `Hon.-Prof. Dr. Kirchbacher` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Mag. Bachl` (person)
- `Mag. Johanna Fletcher` (person)
- `Herbert Onesseit` (person)
- `Oberlandesgerichts Linz` (organisation)

**Example 53** (doc_id: `deanon_260716_TRAIN/13Os22_12b_13Ns16_12z_`) (sent_id: `deanon_260716_TRAIN/13Os22_12b_13Ns16_12z__3`)


Kopf Der Oberste Gerichtshof hat am 5. April 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. Lässig und die Hofrätin des Obersten Gerichtshofs Mag. Marek in Gegenwart der Richteramtsanwärterin MMag. Linzner als Schriftführerin im Verfahren zur Unterbringung der Mag. Türkan Maja Besold in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB, AZ 33 Hv 24/12g des Landesgerichts für Strafsachen Wien, über die Grundrechtsbeschwerde der Betroffenen nach Einsichtnahme durch die Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Grundrechtsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Kirchbacher` | `Hon.-Prof. Dr. Kirchbacher` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Marek` (person)
- `MMag. Linzner` (person)
- `Maja Besold` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 54** (doc_id: `deanon_260716_TRAIN/13Os23_15d`) (sent_id: `deanon_260716_TRAIN/13Os23_15d_3`)


Kopf Der Oberste Gerichtshof hat am 15. April 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Ableidinger als Schriftführerin in der Strafsache gegen Karl Wolniak wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 26. November 2014, GZ 31 Hv 87/14k-77, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Kirchbacher` | `Hon.-Prof. Dr. Kirchbacher` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Mag. Ableidinger` (person)
- `Karl Wolniak` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 55** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__3`)


Kopf Der Oberste Gerichtshof hat am 5. Juli 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Temper als Schriftführerin in der Strafsache gegen Erik Jirouch wegen des Verbrechens des Suchtgifthandels nach § 28a

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Kirchbacher` | `Hon.-Prof. Dr. Kirchbacher` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Marek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Dr. Oshidari` (person)
- `Mag. Temper` (person)
- `Erik Jirouch` (person)

**Example 56** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_3`)


Kopf Der Oberste Gerichtshof hat am 28. Juni 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Plesser als Schriftführer in der Strafsache gegen Aissa Bussmann wegen des Verbrechens des Suchtgifthandels nach § 28a

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Kirchbacher` | `Hon.-Prof. Dr. Kirchbacher` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Mag. Plesser` (person)
- `Aissa Bussmann` (person)

**Example 57** (doc_id: `deanon_260716_TRAIN/13Os74_17g`) (sent_id: `deanon_260716_TRAIN/13Os74_17g_3`)


Kopf Der Oberste Gerichtshof hat am 6. September 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Michael Wakup wegen des Verbrechens des sexuellen Missbrauchs einer wehrlosen oder psychisch beeinträchtigten Person nach §§ 15, 205 Abs 1 StGB sowie weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Linz als Schöffengericht vom 21. März 2017, GZ 22 Hv 1/17p-32, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Widerruf bedingter Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Kirchbacher` | `Hon.-Prof. Dr. Kirchbacher` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Mag. Wetter` (person)
- `Michael Wakup` (person)
- `Landesgerichts Linz` (organisation)

**Example 58** (doc_id: `deanon_260716_TRAIN/13Os78_12p`) (sent_id: `deanon_260716_TRAIN/13Os78_12p_3`)


Kopf Der Oberste Gerichtshof hat am 30. August 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Temper als Schriftführerin in der Strafsache gegen Michael Lengjel und andere Beschuldigte wegen des Vergehens des schweren Betrugs nach §§ 146, 147 Abs 2 StGB sowie weiterer strafbarer Handlungen, AZ 21 Bl 5/11k des Landesgerichts Innsbruck, über die Beschwerden der Anna Wynand und des DI Georg Lu Brian Waltemate gegen den Beschluss des Oberlandesgerichts Innsbruck vom 29. Mai 2012, AZ 6 Bs 220/12x, 221/12v, 222/12s, 223/12p und 224/12k, nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerden werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Kirchbacher` | `Hon.-Prof. Dr. Kirchbacher` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Marek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Dr. Oshidari` (person)
- `Mag. Temper` (person)
- `Michael Lengjel` (person)
- `Landesgerichts Innsbruck` (organisation)
- `Anna Wynand` (person)
- `Brian Waltemate` (person)
- `Oberlandesgerichts Innsbruck` (organisation)

**Example 59** (doc_id: `deanon_260716_TRAIN/13Os97_11f`) (sent_id: `deanon_260716_TRAIN/13Os97_11f_3`)


Kopf Der Oberste Gerichtshof hat am 25. August 2011 durch den Vizepräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Ratz als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in Gegenwart der Richteramtsanwärterin Mag. Einwagner als Schriftführerin in der Strafsache gegen Ernst Grießbaum wegen Verbrechen des sexuellen Missbrauchs einer wehrlosen oder psychisch beeinträchtigten Person nach §§ 205 Abs 1 und 15 StGB sowie einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 5. Jänner 2011, GZ 39 Hv 110/09g-63, nach Einsichtnahme durch die Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde und die Berufung wegen des Ausspruchs über die Schuld werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Ratz` | `Hon.-Prof. Dr. Ratz` |
| `Hon.-Prof. Dr. Kirchbacher` | `Hon.-Prof. Dr. Kirchbacher` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Marek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Mag. Einwagner` (person)
- `Ernst Grießbaum` (person)
- `Landesgerichts Salzburg` (organisation)

**Example 60** (doc_id: `deanon_260716_TRAIN/15Os115_18b`) (sent_id: `deanon_260716_TRAIN/15Os115_18b_3`)


Kopf Der Oberste Gerichtshof hat am 26. September 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Ertl, LL.M., als Schriftführer in der Strafsache gegen Arijan Peschak wegen des Verbrechens des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Wels als Schöffengericht vom 14. Juni 2018, GZ 39 Hv 7/18a-76, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Kirchbacher` | `Hon.-Prof. Dr. Kirchbacher` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Lendl` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Fürnkranz` (person)
- `Dr. Mann` (person)
- `Mag. Ertl, LL.M.` (person)
- `Arijan Peschak` (person)
- `Landesgerichts Wels` (organisation)

**Example 61** (doc_id: `deanon_260716_TRAIN/15Os61_20i`) (sent_id: `deanon_260716_TRAIN/15Os61_20i_3`)


Kopf Der Oberste Gerichtshof hat am 15. Juni 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski in der Strafsache gegen Johann Riemenschneider und einen anderen wegen des Verbrechens des Suchtgifthandels nach § 28a

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Kirchbacher` | `Hon.-Prof. Dr. Kirchbacher` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Lendl` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Johann Riemenschneider` (person)

**Example 62** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__3`)


Kopf Der Oberste Gerichtshof hat am 11. September 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Setz-Hummel in Gegenwart der Richteramtsanwärterin Mag. Leitner als Schriftführerin in der Medienrechtssache des Antragstellers Georgia Bruckmeir gegen die Antragsgegnerin MittelForschung GmbH und eine weitere Antragsgegnerin wegen § 6 Abs 1 und § 8a Abs 6 MedienG, AZ 91 Hv 49/17t des Landesgerichts für Strafsachen Wien, über die von der Generalprokuratur gegen die Urteile des Landesgerichts für Strafsachen Wien vom 26. März 2018 (ON 65 der Hv-Akten) und des Oberlandesgerichts Wien als Berufungsgericht vom 28. November 2018, AZ 17 Bs 153/18a (ON 74 der Hv-Akten), erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Holzleithner, des Vertreters des Antragstellers, Dr. Bauer, und des Vertreters der Antragsgegnerin Analyse Fenheim GmbH, Mag. Bauer, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Kirchbacher` | `Hon.-Prof. Dr. Kirchbacher` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Lendl` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Fürnkranz` (person)
- `Dr. Setz-Hummel` (person)
- `Mag. Leitner` (person)
- `Georgia Bruckmeir` (person)
- `MittelForschung GmbH` (organisation)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Mag. Holzleithner` (person)
- `Dr. Bauer` (person)
- `Analyse Fenheim GmbH` (organisation)
- `Mag. Bauer` (person)

**Example 63** (doc_id: `deanon_260716_TRAIN/15Os71_21m`) (sent_id: `deanon_260716_TRAIN/15Os71_21m_3`)


Kopf Der Oberste Gerichtshof hat am 2. August 2021 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in der Strafsache gegen unbekannte Täter zum Nachteil des DI Robert Leichtlein wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB und einer weiteren strafbaren Handlung, AZ 49 Bl 31/20w des Landesgerichts Salzburg, über die Beschwerde des DI Laurin Beekman gegen den Beschluss des Oberlandesgerichts Linz vom 23. Oktober 2020, GZ 8 Bs 90/20x-1, nach Einsichtnahme in die Akten durch die Generalprokuratur nichtöffentlich (§ 62 Abs 1 zweiter Satz OGH-Geo 2019) den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Kirchbacher` | `Hon.-Prof. Dr. Kirchbacher` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Lendl` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Fürnkranz` (person)
- `Dr. Mann` (person)
- `DI Robert Leichtlein` (person)
- `Landesgerichts Salzburg` (organisation)
- `DI Laurin Beekman` (person)
- `Oberlandesgerichts Linz` (organisation)
- `OGH` (organisation)

**Example 64** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_3`)


Kopf Der Oberste Gerichtshof hat am 11. Dezember 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in Gegenwart des Schriftführers Dr. Koller in der Medienrechtssache der Antragsteller Dr. Ludger Schäpan und Moses Rüßbült gegen die Antragsgegnerin Synzortal-Medien GmbH & Co KG wegen §§ 7 f MedienG, AZ 93 Hv 56/18p des Landesgerichts für Strafsachen Wien, über die von der Generalprokuratur gegen den Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 9. März 2020, AZ 18 Bs 340/19k (ON 27), erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Erste Generalanwältin Mag. Wachberger, der Vertreterin der Antragsteller Dr. Windhager und des Vertreters der Antragsgegnerin Mag. Hermetter, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Kirchbacher` | `Hon.-Prof. Dr. Kirchbacher` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Lendl` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Fürnkranz` (person)
- `Dr. Mann` (person)
- `Dr. Koller` (person)
- `Dr. Ludger Schäpan` (person)
- `Moses Rüßbült` (person)
- `Synzortal-Medien GmbH & Co KG` (organisation)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Mag. Wachberger` (person)
- `Dr. Windhager` (person)
- `Mag. Hermetter` (person)

**Example 65** (doc_id: `deanon_260716_TRAIN/17Ob10_19y`) (sent_id: `deanon_260716_TRAIN/17Ob10_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende und die Hofräte Dr. Musger und Priv.-Doz. Dr. Rassi, die Hofrätin Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Dr. Joshua Reupold, als Masseverwalter über das Vermögen der Wald-Versand Gesellschaft mbH, Kugelmannplatz 4, 5121 Döstling, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, gegen die beklagten Parteien 1. Johanna Baldczus, und 2. MedR Nadja Grela, beide vertreten durch Schöpf & Maurer, Rechtsanwalt in Salzburg, wegen 59.028,60 EUR sA, aus Anlass der außerordentlichen Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. April 2019, GZ 1 R 161/18d-52, mit dem das Urteil des Landesgerichts Salzburg vom 30. August 2018, GZ 57 Cg 10/17z-43, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das angefochtene Urteil wird, soweit es die Abweisung des Teilbegehens, die beklagten Parteien seien zur ungeteilten Hand schuldig, der klagenden Partei 18.168,21 EUR samt 4 % Zinsen seit 15.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Lovrek` | `Hon.-Prof. Dr. Lovrek` |
| `Priv.-Doz. Dr. Rassi` | `Priv.-Doz. Dr. Rassi` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Musger` (person)
- `Dr. Kodek` (person)
- `Dr. Stefula` (person)
- `Dr. Joshua Reupold` (person)
- `Wald-Versand Gesellschaft mbH` (organisation)
- `Kugelmannplatz 4, 5121 Döstling, Österreich` (address)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` (organisation)
- `Johanna Baldczus` (person)
- `MedR Nadja Grela` (person)
- `Maurer` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Salzburg` (organisation)

**Example 66** (doc_id: `deanon_260716_TRAIN/17Ob10_20z`) (sent_id: `deanon_260716_TRAIN/17Ob10_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätinnen Mag. Malesich und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Pascal Alsweh, vertreten durch Stephan Briem Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Dr. Simone Pittruff als Treuhänder der Insolvenzgläubiger der Unter-Analyse Aktiengesellschaft, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH in Linz, wegen Feststellung (Streitwert 18.335,66 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. März 2020, GZ 1 R 31/20i-13, womit das Urteil des Landesgerichts Linz vom 9. Dezember 2019, GZ 4 Cg 73/18z-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Lovrek` | `Hon.-Prof. Dr. Lovrek` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Musger` (person)
- `Mag. Malesich` (person)
- `Dr. Kodek` (person)
- `Dr. Stefula` (person)
- `Pascal Alsweh` (person)
- `Stephan Briem Rechtsanwalt GmbH` (organisation)
- `Dr. Simone Pittruff` (person)
- `Unter-Analyse Aktiengesellschaft` (organisation)
- `Shamiyeh & Reiser Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Linz` (organisation)

**Example 67** (doc_id: `deanon_260716_TRAIN/17Ob20_19v`) (sent_id: `deanon_260716_TRAIN/17Ob20_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie die Hofrätinnen und Hofräte Dr. Musger, Mag. Malesich, Dr. Kodek und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Wolfram Pylypchuk, vertreten durch Dr. Johann Kuzmich, Rechtsanwalt in Nebersdorf, gegen die beklagte Partei Hermann Dühmke, vertreten durch Mag. Alfons Umschaden, Rechtsanwalt in Wien, wegen 15.620 EUR sA und Feststellung (Streitwert 3.000 EUR), über die Revision der beklagten Partei gegen das Zwischen- und Teilurteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Juni 2019, GZ 14 R 31/19k-36, mit welchem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 21. Dezember 2018, GZ 59 Cg 19/16x-31 teilweise abgeändert wurde, in nicht öffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Lovrek` | `Hon.-Prof. Dr. Lovrek` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Musger` (person)
- `Mag. Malesich` (person)
- `Dr. Kodek` (person)
- `Dr. Stefula` (person)
- `Wolfram Pylypchuk` (person)
- `Dr. Johann Kuzmich` (person)
- `Hermann Dühmke` (person)
- `Mag. Alfons Umschaden` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 68** (doc_id: `deanon_260716_TRAIN/17Os3_14s`) (sent_id: `deanon_260716_TRAIN/17Os3_14s_3`)


Kopf Der Oberste Gerichtshof hat am 12. Mai 2014 durch den Präsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Ratz als Vorsitzenden, die Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek und Hon.-Prof. Dr. Kirchbacher sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Kotanko als Schriftführerin in der Strafsache gegen Arno Enste wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Feldkirch als Schöffengericht vom 24. September 2013, GZ 50 Hv 37/13t-48, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Ratz` | `Hon.-Prof. Dr. Ratz` |
| `Hon.-Prof. Dr. Kirchbacher` | `Hon.-Prof. Dr. Kirchbacher` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Danek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Dr. Oshidari` (person)
- `Mag. Kotanko` (person)
- `Arno Enste` (person)
- `Landesgerichts Feldkirch` (organisation)

**Example 69** (doc_id: `deanon_260716_TRAIN/18OCg12_19t`) (sent_id: `deanon_260716_TRAIN/18OCg12_19t_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Veith und die Hofräte Dr. Höllwerth, Priv.-Doz. Dr. Rassi und Mag. Painsi als weitere Richter in der Schiedsrechtssache der klagenden Partei Energie Glanzgart GmbH, Waldelweg 28, 4201 Maierleiten, Österreich, vertreten durch die SRG Stock Rafaseder Gruszkiewicz Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Piedro Arnoult, Bulgarien, wegen Aufhebung eines Schiedsspruchs (Streitwert 257.397,45 EUR), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Klage wird als nicht zur Bestimmung einer Tagsatzung zur mündlichen Verhandlung geeignet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Neumayr` | `Univ.-Prof. Dr. Neumayr` |
| `Priv.-Doz. Dr. Rassi` | `Priv.-Doz. Dr. Rassi` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Veith` (person)
- `Dr. Höllwerth` (person)
- `Mag. Painsi` (person)
- `Energie Glanzgart GmbH` (organisation)
- `Waldelweg 28, 4201 Maierleiten, Österreich` (address)
- `SRG Stock Rafaseder Gruszkiewicz Rechtsanwälte GmbH` (organisation)
- `Piedro Arnoult` (person)

**Example 70** (doc_id: `deanon_260716_TRAIN/18OCg2_24d`) (sent_id: `deanon_260716_TRAIN/18OCg2_24d_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Hon.-Prof. PD Dr. Rassi als Vorsitzenden sowie den Senatspräsidenten Hon.-Prof. Dr. Nowotny, den Hofrat Mag. Painsi, die Hofrätin Dr. Kodek und den Hofrat Dr. Thunhart in der Rechtssache der klagenden Partei Janis Klooth, vertreten durch Mag. Robert Levovnik, Rechtsanwalt in Klagenfurt am Wörthersee, gegen die beklagte Partei Wendy Jannßen, vertreten durch Mag. Michael Wirrer, Rechtsanwalt in Wien, wegen Aufhebung eines Schiedsspruchs (Streitwert 3.600 EUR), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Klage wird zurückgewiesen und das bisherige Verfahren als nichtig aufgehoben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Nowotny` | `Hon.-Prof. Dr. Nowotny` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. PD Dr. Rassi` (person)
- `Mag. Painsi` (person)
- `Dr. Kodek` (person)
- `Dr. Thunhart` (person)
- `Janis Klooth` (person)
- `Mag. Robert Levovnik` (person)
- `Wendy Jannßen` (person)
- `Mag. Michael Wirrer` (person)

**Example 71** (doc_id: `deanon_260716_TRAIN/1Nc10_18p`) (sent_id: `deanon_260716_TRAIN/1Nc10_18p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Dr. Wurdinger als weitere Richter in dem beim Oberlandesgericht Graz zu AZ 5 R 5/15t anhängigen Rechtsmittelverfahren des Antragstellers Mag. Angelika Tränkel, wegen Verfahrenshilfe, den Beschluss gefasst:  Spruch Zur Entscheidung über den Rekurs des Antragstellers gegen den Beschluss des Landesgerichts Klagenfurt vom 28. Juli 2014, GZ 29 Nc 1/14b-22, wird das Oberlandesgericht Wien als zuständig bestimmt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Sailer` | `Hon.-Prof. Dr. Sailer` |
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Dr. Wurdinger` (person)
- `Oberlandesgericht Graz` (organisation)
- `Mag. Angelika Tränkel` (person)
- `Landesgerichts Klagenfurt` (organisation)
- `Oberlandesgericht Wien` (organisation)

**Example 72** (doc_id: `deanon_260716_TRAIN/1Nc1_15k`) (sent_id: `deanon_260716_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Große-Schulte & Seufer E‑Commerce GmbH, Untererb 31, 3033 Altlengbach, Österreich, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Wilbachkel Luftfahrt GmbH, Andrä Idl-Straße 79, 4791 Haselbach, Österreich, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Sailer` | `Hon.-Prof. Dr. Sailer` |
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Landesgericht Wiener Neustadt` (organisation)
- `Große-Schulte & Seufer E‑Commerce GmbH` (organisation)
- `Untererb 31, 3033 Altlengbach, Österreich` (address)
- `Dr. Andreas Oberbichler` (person)
- `Dr. Michael Kramer` (person)
- `Wilbachkel Luftfahrt GmbH` (organisation)
- `Andrä Idl-Straße 79, 4791 Haselbach, Österreich` (address)
- `Mag. Maximilian Kocher` (person)
- `Landesgericht Feldkirch` (organisation)

**Example 73** (doc_id: `deanon_260716_TRAIN/1Nc71_10x`) (sent_id: `deanon_260716_TRAIN/1Nc71_10x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Dr. Grohmann als weitere Richter in der beim Landesgericht für Zivilrechtssachen Wien zu AZ 33 Cg 21/10s anhängigen Rechtssache der klagenden Partei Bachkraft Gesellschaft mbH, Salmweg 829, 4891 Schachen, Österreich, vertreten durch Dr. Gerhard Kornek, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 53.176,92 EUR sA, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch 1.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Sailer` | `Hon.-Prof. Dr. Sailer` |
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Grohmann` (person)
- `Landesgericht für Zivilrechtssachen Wien` (organisation)
- `Bachkraft Gesellschaft mbH` (organisation)
- `Salmweg 829, 4891 Schachen, Österreich` (address)
- `Dr. Gerhard Kornek` (person)

**Example 74** (doc_id: `deanon_260716_TRAIN/1Ob103_20h`) (sent_id: `deanon_260716_TRAIN/1Ob103_20h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Kodek, Mag. Wurzer, Mag. Dr. Wurdinger und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Uwe Zanello, vertreten durch Mag. Peter Mayerhofer, Rechtsanwalt in Wiener Neustadt, gegen die beklagte Partei Janet Angelbeck, vertreten durch Dr. Alfred Steinbuch, Rechtsanwalt in Neunkirchen, wegen Ehescheidung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 26. März 2020, GZ 16 R 45/20m-22, mit dem das Urteil des Bezirksgerichts Neunkirchen vom 23. Dezember 2019, GZ 12 C 12/18s-18, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |
| `Univ.-Prof. Dr. Kodek` | `Univ.-Prof. Dr. Kodek` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Parzmayr` (person)
- `Uwe Zanello` (person)
- `Mag. Peter Mayerhofer` (person)
- `Janet Angelbeck` (person)
- `Dr. Alfred Steinbuch` (person)
- `Landesgerichts Wiener Neustadt` (organisation)
- `Bezirksgerichts Neunkirchen` (organisation)

**Example 75** (doc_id: `deanon_260716_TRAIN/1Ob105_18z`) (sent_id: `deanon_260716_TRAIN/1Ob105_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Familienrechtssache des Antragstellers Ludmilla Bonauer, vertreten durch die Korp Rechtsanwalts GmbH, Andorf, gegen die Antragsgegnerin Henriette Geißendorf, vertreten durch die Puttinger Vogl Rechtsanwälte GmbH, Ried im Innkreis, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts Wels als Rekursgericht vom 2. Mai 2018, GZ 21 R 50/18d-32, mit dem der Rekurs des Antragstellers gegen den Beschluss des Bezirksgerichts Grieskirchen vom 8. Jänner 2018, GZ 8 Fam 37/16i-26, zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Ludmilla Bonauer` (person)
- `Korp Rechtsanwalts GmbH` (organisation)
- `Henriette Geißendorf` (person)
- `Puttinger Vogl Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Wels` (organisation)
- `Bezirksgerichts Grieskirchen` (organisation)

**Example 76** (doc_id: `deanon_260716_TRAIN/1Ob109_18p`) (sent_id: `deanon_260716_TRAIN/1Ob109_18p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Parteien 1. Mag. Eva Voeglein, und 2. Ursula Preising, vertreten durch die HOHENBERG STRAUSS BUCHBAUER Rechtsanwälte GmbH, Graz, gegen die beklagte Partei Gemeinde Veit Faeser, vertreten durch Dr. Klaus Rainer, Rechtsanwalt in Graz, wegen 573.890,70 EUR sA, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 2. Mai 2018, GZ 5 R 172/17d-57, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 23. Oktober 2017, GZ 41 Cg 51/15m-47, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Mag. Eva Voeglein` (person)
- `Ursula Preising` (person)
- `HOHENBERG STRAUSS BUCHBAUER Rechtsanwälte GmbH` (organisation)
- `Veit Faeser` (person)
- `Dr. Klaus Rainer` (person)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)

**Example 77** (doc_id: `deanon_260716_TRAIN/1Ob127_14d`) (sent_id: `deanon_260716_TRAIN/1Ob127_14d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Dr. Rocco Reichl, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Sailer` | `Hon.-Prof. Dr. Sailer` |
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Rocco Reichl` (person)

**Example 78** (doc_id: `deanon_260716_TRAIN/1Ob128_17f`) (sent_id: `deanon_260716_TRAIN/1Ob128_17f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Familienrechtssache des Antragstellers Mag. Josefine Rehn, vertreten durch die Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG, Wien, gegen die Antragsgegnerin Susanne Lürkens, vertreten durch Mag. Anna-Maria Freiberger, Rechtsanwältin in Wien, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 24. April 2017, GZ 45 R 66/17i, 67/17m-19, mit dem die Beschlüsse des Bezirksgerichts Liesing vom 4. Jänner 2017, GZ 7 Fam 30/16m-12, und vom 17. Jänner 2017, GZ 7 Fam 30/16m-14, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Sailer` | `Hon.-Prof. Dr. Sailer` |
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Mag. Josefine Rehn` (person)
- `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG` (organisation)
- `Susanne Lürkens` (person)
- `Mag. Anna-Maria Freiberger` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Liesing` (organisation)

**Example 79** (doc_id: `deanon_260716_TRAIN/1Ob12_21b`) (sent_id: `deanon_260716_TRAIN/1Ob12_21b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Mag. Mathias Gumbel, vertreten durch die Huber & Partner Rechtsanwälte GmbH, Linz, gegen die beklagten Parteien 1. Otto Gerdhennrich, 2.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Mag. Mathias Gumbel` (person)
- `Huber & Partner Rechtsanwälte GmbH` (organisation)
- `Otto Gerdhennrich` (person)

**Example 80** (doc_id: `deanon_260716_TRAIN/1Ob139_18z`) (sent_id: `deanon_260716_TRAIN/1Ob139_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Verena Tappendorff Inc., Sankt Andrä im Sausal 24, 8552 Aichberg, Österreich, vertreten durch Mag. Ralph Kilches, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Sabine Martinsson, als Insolvenzverwalter im Insolvenzverfahren über das Vermögen der Touristik Synberbruck GmbH, Fridau 56l, 7433 Bergwerk, Österreich, vertreten durch die Haslinger/Nagele & Partner Rechtsanwälte GmbH, Linz, wegen Feststellung einer Insolvenzforderung (Streitwert 447.352,05 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 28. Juni 2018, GZ 1 R 83/18h-8, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Verena Tappendorff` (person)
- `Sankt Andrä im Sausal 24, 8552 Aichberg, Österreich` (address)
- `Mag. Ralph Kilches` (person)
- `Mag. Sabine Martinsson` (person)
- `Touristik Synberbruck GmbH` (organisation)
- `Fridau 56l, 7433 Bergwerk, Österreich` (address)
- `Haslinger/Nagele & Partner Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Linz` (organisation)

**Example 81** (doc_id: `deanon_260716_TRAIN/1Ob142_19t`) (sent_id: `deanon_260716_TRAIN/1Ob142_19t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der Antragstellerin Mag. Kassandra Christoforidou, vertreten Dr. Brigitte Birnbaum und Dr. Rainer Toperczer, Rechtsanwälte in Wien, gegen den Antragsgegner Dr. Otto Einhenkel, vertreten durch die Anwaltssocietät Sattlegger Dorninger Steiner & Partner OG, Linz, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse gemäß §§ 81 ff EheG, über die außerordentlichen Revisionsrekurse beider Parteien gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 9. Juli 2019, GZ 45 R 554/18f-162, mit dem der Beschluss des Bezirksgerichts Fünfhaus vom 25. Oktober 2018, GZ 4 Fam 68/14k-156, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Der Revisionsrekurs des Antragsgegners wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Mag. Kassandra Christoforidou` (person)
- `Dr. Brigitte Birnbaum` (person)
- `Dr. Rainer Toperczer` (person)
- `Dr. Otto Einhenkel` (person)
- `Anwaltssocietät Sattlegger Dorninger Steiner & Partner OG` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Fünfhaus` (organisation)

**Example 82** (doc_id: `deanon_260716_TRAIN/1Ob159_20v`) (sent_id: `deanon_260716_TRAIN/1Ob159_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und Hofrätinnen, Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Bachfen Entwicklung AG, Reisedt 4, 4770 Radlern, Österreich, vertreten durch Mag. Markus Stender, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. Musialek Getränke GmbH, 2.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Mag. Korn` (person)
- `Bachfen Entwicklung AG` (organisation)
- `Reisedt 4, 4770 Radlern, Österreich` (address)
- `Mag. Markus Stender` (person)
- `Musialek Getränke GmbH` (organisation)

**Example 83** (doc_id: `deanon_260716_TRAIN/1Ob160_10a`) (sent_id: `deanon_260716_TRAIN/1Ob160_10a_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte Dr. Fichtenau, Dr. Grohmann, Univ.-Prof. Dr. Kodek und Dr. E. Solé als weitere Richter in der Pflegschaftssache des am 10. August 2000 geborenen mj Nino Küntzelmann, über den außerordentlichen Revisionsrekurs des Vaters Daniel Kohlhase, vertreten durch Mag. Stefan Aberer, Rechtsanwalt in Bregenz, gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 27. Juli 2010, GZ 3 R 247/10m-60, mit dem der Beschluss des Bezirksgerichts Bregenz vom 22. Juni 2010, GZ 24 PS 46/09s-52, bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |
| `Univ.-Prof. Dr. Kodek` | `Univ.-Prof. Dr. Kodek` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Dr. E. Solé` (person)
- `Nino Küntzelmann` (person)
- `Daniel Kohlhase` (person)
- `Mag. Stefan Aberer` (person)
- `Landesgerichts Feldkirch` (organisation)
- `Bezirksgerichts Bregenz` (organisation)

**Example 84** (doc_id: `deanon_260716_TRAIN/1Ob160_12d`) (sent_id: `deanon_260716_TRAIN/1Ob160_12d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der außerstreitigen Rechtssache der Antragstellerin Dipl. Kff. OSR Evamaria Ishak, vertreten durch Dr. Karl-Peter Hasch, Rechtsanwalt in Villach, gegen den Antragsgegner Niklas Damianidis, vertreten durch Mag. Hanno Stromberger, Rechtsanwalt in Villach, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse über den Revisionsrekurs der Antragstellerin gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 31. Mai 2012, GZ 2 R 85/12w-11, mit dem der Beschluss des Bezirksgerichts Villach vom 13. März 2012, GZ 38 Fam 98/11s-7, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Sailer` | `Hon.-Prof. Dr. Sailer` |
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Grohmann` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dipl. Kff. OSR Evamaria Ishak` (person)
- `Dr. Karl-Peter Hasch` (person)
- `Niklas Damianidis` (person)
- `Mag. Hanno Stromberger` (person)
- `Landesgerichts Klagenfurt` (organisation)
- `Bezirksgerichts Villach` (organisation)

**Example 85** (doc_id: `deanon_260716_TRAIN/1Ob163_21h`) (sent_id: `deanon_260716_TRAIN/1Ob163_21h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Christine Neemeyer, vertreten durch Mag. Dieter Koch und Mag. Natascha Jilek, Rechtsanwälte in Bruck an der Mur, gegen die beklagte Partei Synbach-Holz Bank AG, Bergbahnweg 7j, 4632 Oberthambach, Österreich, vertreten durch Mag. Martina Hosp ua, Rechtsanwälte in Salzburg, wegen Feststellung (Streitwert 103.488,18 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 21. Juni 2021, GZ 2 R 70/21h-19, mit dem das Urteil des Landesgerichts Salzburg vom 12. März 2021, GZ 10 Cg 52/20k-15, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Christine Neemeyer` (person)
- `Mag. Dieter Koch` (person)
- `Mag. Natascha Jilek` (person)
- `Synbach-Holz Bank` (organisation)
- `Bergbahnweg 7j, 4632 Oberthambach, Österreich` (address)
- `Mag. Martina Hosp` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Salzburg` (organisation)

**Example 86** (doc_id: `deanon_260716_TRAIN/1Ob169_15g`) (sent_id: `deanon_260716_TRAIN/1Ob169_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Dalibor Jonetzko, vertreten durch Dr. Johannes Öhlböck, LL.M., Rechtsanwalt in Wien, gegen die beklagte Partei Stadt Waltraud Wedekämper, vertreten durch Dr. Josef Milchram, Rechtsanwalt in Wien, wegen 100.000 EUR sA und Feststellung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Mai 2015, GZ 14 R 140/14g-16, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 21. August 2014, GZ 31 Cg 14/14b-12, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Sailer` | `Hon.-Prof. Dr. Sailer` |
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dalibor Jonetzko` (person)
- `Dr. Johannes Öhlböck, LL.M.` (person)
- `Waltraud Wedekämper` (person)
- `Dr. Josef Milchram` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 87** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Dr. Florenzia Münsterer, vertreten durch Rechtsanwälte Dr. Amhof & Dr. Damian GmbH in Wien, gegen die beklagte Partei MittelEnergie Werke Bank AG, Altlassing 110, 4183 Ahorn, Österreich, vertreten durch Urbanek Lind Schmied Reisch Rechtsanwälte OG in Wien, wegen 600.090 EUR sA, über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 25. Mai 2011, GZ 15 R 64/11h-54, mit dem das Urteil des Handelsgerichts Wien vom 14. Jänner 2011, GZ 16 Cg 20/10f-50, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Sailer` | `Hon.-Prof. Dr. Sailer` |
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Grohmann` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Florenzia Münsterer` (person)
- `Rechtsanwälte Dr. Amhof & Dr. Damian GmbH` (organisation)
- `MittelEnergie Werke Bank` (organisation)
- `Altlassing 110, 4183 Ahorn, Österreich` (address)
- `Urbanek Lind Schmied Reisch Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 88** (doc_id: `deanon_260716_TRAIN/1Ob174_19y`) (sent_id: `deanon_260716_TRAIN/1Ob174_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Theophil Mielewzyk, vertreten durch Dr. Hannes Paulweber, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Liu Jantschar, vertreten durch die Heiss & Heiss Rechtsanwälte OG, Innsbruck, wegen 137.664,28 EUR sA sowie Feststellung (Streitwert 15.000 EUR), über die außerordentliche Revision der beklagten Partei gegen das (richtig) Teilzwischenurteil des Oberlandesgerichts Innsbruck vom 18. Juli 2019, GZ 1 R 76/19i-74, mit dem das Urteil des Landesgerichts Innsbruck vom 21. Februar 2019, GZ 8 Cg 119/16z-68, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Theophil Mielewzyk` (person)
- `Dr. Hannes Paulweber` (person)
- `Liu Jantschar` (person)
- `Heiss & Heiss Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Innsbruck` (organisation)
- `Landesgerichts Innsbruck` (organisation)

**Example 89** (doc_id: `deanon_260716_TRAIN/1Ob178_19m`) (sent_id: `deanon_260716_TRAIN/1Ob178_19m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Hilde Dammrow, vertreten durch die Korn und Gärtner Rechtsanwälte OG, Salzburg, gegen die beklagte Partei Evelyn Allmutter, vertreten durch die Ferner Hornung & Partner Rechtsanwälte GmbH, Salzburg, wegen Wiederaufnahme des Verfahrens AZ 17 C 1538/16p des Bezirksgerichts Salzburg, über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 12. Juni 2019, GZ 22 R 163/19b-7, mit dem der Beschluss des Bezirksgerichts Salzburg vom 25. Jänner 2019, GZ 17 C 80/19f-2, mit einer Maßgabe bestätigt wurde, den Beschluss gefasst:  Spruch Dem außerordentlichen Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Hilde Dammrow` (person)
- `Evelyn Allmutter` (person)
- `Hornung & Partner Rechtsanwälte GmbH` (organisation)
- `Bezirksgerichts Salzburg` (organisation)
- `Landesgerichts Salzburg` (organisation)
- `Bezirksgerichts Salzburg` (organisation)

**Example 90** (doc_id: `deanon_260716_TRAIN/1Ob179_12y`) (sent_id: `deanon_260716_TRAIN/1Ob179_12y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Pflegschaftssache des mj Traude Wedtrat, geboren am 13. Juli 2006, vertreten durch Mag. Heinz Wolfbauer, Rechtsanwalt in Wien, wegen Unterhalts, über den Revisionsrekurs des Vaters Dr. Rainer Steinstrass, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 29. Mai 2012, GZ 43 R 254/12i-106, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Döbling vom 28. März 2012, GZ 10 Pu 131/09b-100, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Sailer` | `Hon.-Prof. Dr. Sailer` |
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Grohmann` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Traude Wedtrat` (person)
- `Mag. Heinz Wolfbauer` (person)
- `Dr. Rainer Steinstrass` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Döbling` (organisation)

**Example 91** (doc_id: `deanon_260716_TRAIN/1Ob182_17x`) (sent_id: `deanon_260716_TRAIN/1Ob182_17x_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Dr. Wurdinger, und die Hofrätinnen Dr. Hofer-Zeni-Rennhofer und Dr. Kodek in der Rechtssache der gefährdeten Partei Aloisa Moosleitner, vertreten durch die Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG, Wien, gegen die gefährdete Partei Catharina Uppenbrink, vertreten durch Dr. Alexander Haas, Rechtsanwalt in Seiersberg-Pirka, wegen Erlassung einer einstweiligen Verfügung nach § 382 Z 8 lit c zweiter Fall EO, über den außerordentlichen Revisionsrekurs der gefährdeten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 11. September 2017, GZ 1 R 213/17a-221, mit dem der Beschluss des Bezirksgerichts Fürstenfeld vom 25. Juli 2017, GZ 23 Fam 27/15p-207, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch 1.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Kodek` (person)
- `Aloisa Moosleitner` (person)
- `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG` (organisation)
- `Catharina Uppenbrink` (person)
- `Dr. Alexander Haas` (person)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)
- `Bezirksgerichts Fürstenfeld` (organisation)

**Example 92** (doc_id: `deanon_260716_TRAIN/1Ob186_12b`) (sent_id: `deanon_260716_TRAIN/1Ob186_12b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Thomas Plüm, vertreten durch Kammler & Koll Rechtsanwälte OG in Freistadt, gegen die beklagte Partei Patrick Dimpfel, vertreten durch Mag. Klaus Burgholzer, Rechtsanwalt in Linz, wegen 100.000 EUR sA und Feststellung (Streitwert: 5.000 EUR), über die außerordentliche Revision der klagenden Partei (Revisionsinteresse: 70.000 EUR sA) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. Juli 2012, GZ 2 R 79/12v-22, mit dem das Urteil des Landesgerichts Linz vom 27. Februar 2012, GZ 5 Cg 61/11d-18, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Sailer` | `Hon.-Prof. Dr. Sailer` |
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Grohmann` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Thomas Plüm` (person)
- `Kammler & Koll Rechtsanwälte OG` (organisation)
- `Patrick Dimpfel` (person)
- `Mag. Klaus Burgholzer` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Linz` (organisation)

**Example 93** (doc_id: `deanon_260716_TRAIN/1Ob192_11h`) (sent_id: `deanon_260716_TRAIN/1Ob192_11h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Hierle Sanitär Limited, London, Zirkinger Straße 3, 8082 Glatzau, Österreich, vertreten durch Thum Weinreich Schwarz Fuchsbauer Rechtsanwälte OG in St. Pölten, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 1,8 Mio EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Juni 2011, GZ 14 R 214/10h-39, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 3. September 2010, GZ 33 Cg 3/09t-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Sailer` | `Hon.-Prof. Dr. Sailer` |
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Grohmann` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Hierle Sanitär Limited` (organisation)
- `Zirkinger Straße 3, 8082 Glatzau, Österreich` (address)
- `Thum Weinreich Schwarz Fuchsbauer Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 94** (doc_id: `deanon_260716_TRAIN/1Ob216_15v`) (sent_id: `deanon_260716_TRAIN/1Ob216_15v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Suleika Kranigk, vertreten durch Hon.-Prof. Dr. Michel Walter, Rechtsanwalt in Wien, gegen die beklagte Partei Kelfen Transport Solutions GmbH, Geßlgasse 35, 9911 Thal-Wilfern, Österreich, vertreten durch die Schlösser & Partner Rechtsanwälte OG, Graz, wegen 33.930 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 19. August 2015, GZ 13 R 74/15w-55, mit dem das Endurteil des Landesgerichts Korneuburg vom 26. Februar 2015, GZ 3 Cg 15/13h-50, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dr. Sailer` | `Hon.-Prof. Dr. Sailer` |
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |
| `Hon.-Prof. Dr. Michel Walter` | `Hon.-Prof. Dr. Michel Walter` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Suleika Kranigk` (person)
- `Kelfen Transport Solutions GmbH` (organisation)
- `Geßlgasse 35, 9911 Thal-Wilfern, Österreich` (address)
- `Partner Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts Korneuburg` (organisation)

**Example 95** (doc_id: `deanon_260716_TRAIN/1Ob224_19a`) (sent_id: `deanon_260716_TRAIN/1Ob224_19a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Thassilo John, vertreten durch Dr. Johannes Kirschner, Rechtsanwalt in Wels, gegen die beklagte Partei Mona Kutzner, vertreten durch Dr. Widukind W. Nordmeyer und Dr. Thomas Kitzberger, Rechtsanwälte in Wels, wegen 30.600 EUR sA, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 28. Oktober 2019, GZ 6 R 131/19f-16, mit dem der Beschluss des Landesgerichts Wels vom 13. September 2019, GZ 36 Cg 25/19g-11, abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Thassilo John` (person)
- `Dr. Johannes Kirschner` (person)
- `Mona Kutzner` (person)
- `Dr. Widukind W. Nordmeyer` (person)
- `Dr. Thomas Kitzberger` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Wels` (organisation)

**Example 96** (doc_id: `deanon_260716_TRAIN/1Ob224_20b`) (sent_id: `deanon_260716_TRAIN/1Ob224_20b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache klagenden Partei Rainer Baetzel, vertreten durch Dr. Harald Hauer, Rechtsanwalt in Wien, gegen die beklagte Partei Rimscha Versand GmbH in Liquidation, Götzau 193, 5452 Grub, Österreich, vertreten durch die Petsch Frosch Klein Arturo Rechtsanwälte OG, Wien, wegen 38.236,58 EUR sA und Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Oktober 2020, GZ 3 R 51/20x-50, mit dem das Urteil des Handelsgerichts Wien vom 24. Juli 2020, GZ 34 Cg 51/18h-45, bestätigt wurde, in nicht öffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Rainer Baetzel` (person)
- `Dr. Harald Hauer` (person)
- `Rimscha Versand GmbH` (organisation)
- `Götzau 193, 5452 Grub, Österreich` (address)
- `Petsch Frosch Klein Arturo Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 97** (doc_id: `deanon_260716_TRAIN/1Ob226_20x`) (sent_id: `deanon_260716_TRAIN/1Ob226_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Pia Geermann GmbH, Orise 28, 9135 Unterort, Österreich, vertreten durch Dr. Martin Leitner und andere, Rechtsanwälte in Wien, gegen die beklagte Partei Stadt Li Wachmeister, vertreten durch die Estermann Pock Rechtsanwälte GmbH, Wien, wegen 19.002,01 EUR, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 7. September 2020, GZ 14 R 61/20y-27, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 28. Jänner 2020, GZ 31 Cg 1/19y-22, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Pia Geermann` (person)
- `Orise 28, 9135 Unterort, Österreich` (address)
- `Dr. Martin Leitner` (person)
- `Li Wachmeister` (person)
- `Estermann Pock Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 98** (doc_id: `deanon_260716_TRAIN/1Ob26_20k`) (sent_id: `deanon_260716_TRAIN/1Ob26_20k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Schrickel Luftfahrt GmbH, Grieselstein-Rosenberg 3, 3314 Ottendorf, Österreich, vertreten durch die Draxler Rexeis Sozietät von Rechtsanwälten OG, Graz, gegen die beklagte Partei Monika Peikert, vertreten durch Mag. Dr. Alfred Wansch, Rechtsanwalt in Wien, wegen Räumung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtsachen Wien als Berufungsgericht vom 13. November 2019, GZ 39 R 228/19x-70, mit dem das Urteil des Bezirksgerichts Hernals vom 30. April 2019, GZ 4 C 277/16f-64, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Schrickel Luftfahrt GmbH` (organisation)
- `Grieselstein-Rosenberg 3, 3314 Ottendorf, Österreich` (address)
- `Draxler Rexeis Sozietät von Rechtsanwälten OG` (organisation)
- `Monika Peikert` (person)
- `Mag. Dr. Alfred Wansch` (person)
- `Bezirksgerichts Hernals` (organisation)

**Example 99** (doc_id: `deanon_260716_TRAIN/1Ob29_20a`) (sent_id: `deanon_260716_TRAIN/1Ob29_20a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Familienrechtssache der Antragstellerin Evamaria Konopatsch, vertreten durch Dr. Walter Mardetschläger und andere Rechtsanwälte in Wien, gegen den Antragsgegner Lubomir Strässle, vertreten durch Dr. Peter Paul Wolf, Rechtsanwalt in Wien, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den außerordentlichen Revisionsrekurs der Antragstellerin gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 19. Dezember 2019, GZ 43 R 586/19y-81, mit dem der Beschluss des Bezirksgerichts Donaustadt vom 17. Oktober 2019, GZ 29 Fam 7/18w-71, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dr. Bydlinski` | `Univ.-Prof. Dr. Bydlinski` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Evamaria Konopatsch` (person)
- `Dr. Walter Mardetschläger` (person)
- `Lubomir Strässle` (person)
- `Dr. Peter` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Ralph Prusseit, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Akbayrak Metall GmbH, Schroateck 57, 4710 Niederweng, Österreich, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `PD Dr. Rassi` — partial — pred is substring of gold: `Hon.-Prof. PD Dr. Rassi`

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

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Karim Mielewczik, gegen die beklagte Partei Dr. Sandro Gädecken, vertreten durch Ing. Dr. Stefan Krall und Dr. Oliver Kühnl, Rechtsanwälte in Innsbruck, wegen 9.456 EUR sA (Revisionsinteresse 9.268,50 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 25. Februar 2025, GZ 21 R 434/24f-29, mit dem das Urteil des Bezirksgerichts Seekirchen am Wallersee vom 5. September 2024, GZ 2 C 1107/23d-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `PD Dr. Rassi` — partial — pred is substring of gold: `Hon.-Prof. PD Dr. Rassi`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Dr. Annerl`(person)
- `Dr. Vollmaier`(person)
- `Dr. Wallner-Friedl`(person)
- `Karim Mielewczik`(person)
- `Dr. Sandro Gädecken`(person)
- `Ing. Dr. Stefan Krall`(person)
- `Dr. Oliver Kühnl`(person)
- `Landesgerichts Salzburg`(organisation)
- `Bezirksgerichts Seekirchen`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/18OCg2_24d`) (sent_id: `deanon_260716_TRAIN/18OCg2_24d_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Hon.-Prof. PD Dr. Rassi als Vorsitzenden sowie den Senatspräsidenten Hon.-Prof. Dr. Nowotny, den Hofrat Mag. Painsi, die Hofrätin Dr. Kodek und den Hofrat Dr. Thunhart in der Rechtssache der klagenden Partei Janis Klooth, vertreten durch Mag. Robert Levovnik, Rechtsanwalt in Klagenfurt am Wörthersee, gegen die beklagte Partei Wendy Jannßen, vertreten durch Mag. Michael Wirrer, Rechtsanwalt in Wien, wegen Aufhebung eines Schiedsspruchs (Streitwert 3.600 EUR), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Klage wird zurückgewiesen und das bisherige Verfahren als nichtig aufgehoben.

**False Positives:**

- `PD Dr. Rassi` — partial — pred is substring of gold: `Hon.-Prof. PD Dr. Rassi`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Mag. Painsi`(person)
- `Dr. Kodek`(person)
- `Dr. Thunhart`(person)
- `Janis Klooth`(person)
- `Mag. Robert Levovnik`(person)
- `Wendy Jannßen`(person)
- `Mag. Michael Wirrer`(person)

</details>

---

## `MedR Title Pattern` 

**F1:** 0.003 | **Precision:** 0.857 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `693cd5c7`  
**Description:**
Matches 'MedR' title followed by name, e.g., 'MedR Juri Uhlemann'.

**Content:**
```
MedR\s+([A-Z][a-zäöüß]+\s+[A-Z][a-zäöüß]+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.857 | 0.001 | 0.003 | 7 | 6 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 6 | 1 | 2944 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/17Ob10_19y`) (sent_id: `deanon_260716_TRAIN/17Ob10_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende und die Hofräte Dr. Musger und Priv.-Doz. Dr. Rassi, die Hofrätin Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Dr. Joshua Reupold, als Masseverwalter über das Vermögen der Wald-Versand Gesellschaft mbH, Kugelmannplatz 4, 5121 Döstling, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, gegen die beklagten Parteien 1. Johanna Baldczus, und 2. MedR Nadja Grela, beide vertreten durch Schöpf & Maurer, Rechtsanwalt in Salzburg, wegen 59.028,60 EUR sA, aus Anlass der außerordentlichen Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. April 2019, GZ 1 R 161/18d-52, mit dem das Urteil des Landesgerichts Salzburg vom 30. August 2018, GZ 57 Cg 10/17z-43, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das angefochtene Urteil wird, soweit es die Abweisung des Teilbegehens, die beklagten Parteien seien zur ungeteilten Hand schuldig, der klagenden Partei 18.168,21 EUR samt 4 % Zinsen seit 15.

| Predicted | Gold |
|---|---|
| `MedR Nadja Grela` | `MedR Nadja Grela` |

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
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` (organisation)
- `Johanna Baldczus` (person)
- `Maurer` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Salzburg` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/3Ob37_25z`) (sent_id: `deanon_260716_TRAIN/3Ob37_25z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Brenn als Vorsitzenden sowie die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und die Hofräte Dr. Stefula und Mag. Schober als weitere Richter in der Rechtssache der klagenden Partei MedR Peter Reitschmied, vertreten durch MMag. Eva Kathrein, Rechtsanwältin in Innsbruck, gegen die beklagte Partei Annkathrin Peperkock, vertreten durch Ing. MMag. Dr. Gerhard Benda, Rechtsanwalt in Innsbruck, wegen 5.505 EUR sA, über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Innsbruck als Berufungsgericht vom 21. Oktober 2024, GZ 2 R 116/24h-16.1, mit dem die Berufung gegen das Versäumungsurteil des Bezirksgerichts Innsbruck vom 11. Juni 2024, GZ 30 C 63/24g-10, zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `MedR Peter Reitschmied` | `MedR Peter Reitschmied` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Brenn` (person)
- `Dr. Weixelbraun-Mohr` (person)
- `Dr. Kodek` (person)
- `Dr. Stefula` (person)
- `Mag. Schober` (person)
- `MMag. Eva Kathrein` (person)
- `Annkathrin Peperkock` (person)
- `MMag. Dr. Gerhard Benda` (person)
- `Landesgerichts Innsbruck` (organisation)
- `Bezirksgerichts Innsbruck` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/4Ob68_14z`) (sent_id: `deanon_260716_TRAIN/4Ob68_14z_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Dario Marchand, gegen die beklagte Partei MedR Sonja Poliscuk, wegen Wiederaufnahme des Verfahrens AZ 4 Ob 24/14d (3 C 1367/12a des Bezirksgerichts Dornbirn), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch 1.

| Predicted | Gold |
|---|---|
| `MedR Sonja Poliscuk` | `MedR Sonja Poliscuk` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schenk` (person)
- `Dr. Vogel` (person)
- `Dr. Jensik` (person)
- `Dr. Musger` (person)
- `Dr. Schwarzenbacher` (person)
- `Dario Marchand` (person)
- `Bezirksgerichts Dornbirn` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/5Ob177_20w`) (sent_id: `deanon_260716_TRAIN/5Ob177_20w_5`)


MedR Heinz Tahir, vertreten durch die Schmid & Horn Rechtsanwälte GmbH, Graz, gegen die Antragsgegner 1. Arch.

| Predicted | Gold |
|---|---|
| `MedR Heinz Tahir` | `MedR Heinz Tahir` |

**Missed by this rule (FN):**

- `Schmid & Horn Rechtsanwälte GmbH` (organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/8Ob123_18y`) (sent_id: `deanon_260716_TRAIN/8Ob123_18y_59`)


Felizia Jarosz war zu diesem Zeitpunkt bereits mündig, MedR Heidemarie Abdelrahman hat am 12.

| Predicted | Gold |
|---|---|
| `MedR Heidemarie Abdelrahman` | `MedR Heidemarie Abdelrahman` |

**Missed by this rule (FN):**

- `Felizia Jarosz` (person)

**Example 5** (doc_id: `deanon_260716_TRAIN/8ObA18_17f`) (sent_id: `deanon_260716_TRAIN/8ObA18_17f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Brenn als weitere Richter sowie die fachkundigen Laienrichter Mag. Dr. Bernhard Gruber und Harald Kohlruss in der Arbeitsrechtssache der klagenden Partei MedR Clemens Schepper, vertreten durch Freimüller/Obereder/Pilz Rechtsanwält_innen GmbH in Wien, gegen die beklagte Partei Muehleis & Klaese Technik AG, Rosentaler Weg 2k, 9811 St. Peter in Holz, Österreich, vertreten durch DLA Piper Weiss-Tessbach Rechtsanwälte GmbH in Wien, wegen Feststellung (Streitwert 282,56 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. November 2016, GZ 7 Ra 90/16f-19, mit dem das Urteil des Arbeits- und Sozialgerichts Wien vom 20. Juli 2016, GZ 33 Cga 50/16p-15, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `MedR Clemens Schepper` | `MedR Clemens Schepper` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Prof. Dr. Spenling` (person)
- `Dr. Tarmann-Prentner` (person)
- `Dr. Brenn` (person)
- `Mag. Dr. Bernhard Gruber` (person)
- `Harald Kohlruss` (person)
- `Freimüller/Obereder/Pilz Rechtsanwält_innen GmbH` (organisation)
- `Muehleis & Klaese Technik AG` (organisation)
- `Rosentaler Weg 2k, 9811 St. Peter in Holz, Österreich` (address)
- `DLA Piper Weiss-Tessbach Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/7Ob180_16w`) (sent_id: `deanon_260716_TRAIN/7Ob180_16w_41`)


Er empfand es, als würden die Beklagte und Mag. MedR Diego Dentzin in der Öffentlichkeit „herumturteln“.

**False Positives:**

- `MedR Diego Dentzin` — partial — pred is substring of gold: `Mag. MedR Diego Dentzin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. MedR Diego Dentzin`(person)

</details>

---

## `Zeugen Name` 🏆

**F1:** 0.005 | **Precision:** 0.769 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `3d151e4a`  
**Description:**
Matches names following 'Zeugen' (witness), handling titles and hyphenated names.

**Content:**
```
Zeugen\s+(?:(?:Dr\.|Mag\.|Hon\.-Prof\.|Univ.-Prof\.|Priv.-Doz\.|Prof\.|MMag\.|KR\.|OStR\.|StR\.|AR\.|Ing\.|DI\.|PhD\.|Dipl.-Ing\.|Bakk\. iur\.|MBA|BSc|LL\.M\.|RgR|\u00d6kR|StR|OStR|KR|AR|VetR|PD|Mag\.a)\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.769 | 0.002 | 0.005 | 13 | 10 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 10 | 3 | 3542 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__4`)


Im Verfahren AZ 28 U 165/17y des Bezirksgerichts Leopoldstadt verletzen 1./ die Durchführung der Hauptverhandlung und Urteilsfällung am 26. September 2018 in Abwesenheit des Angeklagten § 427 Abs 1 StPO, 2./ die Verlesung des die Vernehmung des Zeugen Alexander Struttmann beinhaltenden Teils des Hauptverhandlungsprotokolls vom 28. Februar 2018 (ON 9) in der Hauptverhandlung am 26. September 2018 § 252 Abs 1 StPO iVm § 447 StPO, 3./ der unter einem mit dem Urteil vom 26. September 2018 (ON 25) gefasste Beschluss auf Widerruf der Nenad Pohlmann mit Urteil des Landesgerichts für Strafsachen Wien vom 28. Jänner 2015, AZ 162 Hv 117/14k, gewährten bedingten Strafnachsicht § 494a Abs 3 StPO und 4./ das Urteil vom 26. September 2018 (ON 25) § 31 Abs 1 StGB.

| Predicted | Gold |
|---|---|
| `Alexander Struttmann` | `Alexander Struttmann` |

**Missed by this rule (FN):**

- `Bezirksgerichts Leopoldstadt` (organisation)
- `Nenad Pohlmann` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__10`)


Im Anschluss an die Vernehmung des Zeugen Alexander Schwienefoth (ON 9 S 2 f) vertagte die Richterin des Bezirksgerichts die Hauptverhandlung zur Vorführung des Angeklagten (ON 9 S 3).

| Predicted | Gold |
|---|---|
| `Alexander Schwienefoth` | `Alexander Schwienefoth` |

**Example 2** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__12`)


Nach Eröffnung des Beweisverfahrens verlas die Richterin des Bezirksgerichts unter anderem die vom Zeugen Alexander Sagenmüller in der Hauptverhandlung am 28. Februar 2018 abgelegte Aussage (ON 9 S 2 f; ON 24 S 2).

| Predicted | Gold |
|---|---|
| `Alexander Sagenmüller` | `Alexander Sagenmüller` |

**Example 3** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__25`)


Da eine solche Zustimmung des Angeklagten wegen dessen Abwesenheit nicht vorlag (vgl RIS-Justiz RS0117012, RS0099242 [T7]), widersprach die Verlesung des die Vernehmung des Zeugen Alexander Sief beinhaltenden Teils des Protokolls der Hauptverhandlung vom 28. Februar 2018 (ON 9 S 2 f) in der (gemäß § 276a zweiter Satz StPO wiederholten) Hauptverhandlung am 26. September 2018 § 252 Abs 1 iVm § 447 StPO.

| Predicted | Gold |
|---|---|
| `Alexander Sief` | `Alexander Sief` |

**Example 4** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_11`)


Die Behauptung einer Verletzung des § 252 Abs 1 StPO (§ 281 Abs 1 Z 3 StPO) übergeht das Protokoll der Hauptverhandlung vom 10. Dezember 2012, wonach der gesamte Akteninhalt - beinhaltend auch die Aussagen der Zeugen Ines Mätzel, Barbara Nellen und Baldur Neander vor der Kriminalpolizei - einverständlich (§ 252 Abs 1 Z 4 StPO) verlesen worden ist (ON 38 S 16).

| Predicted | Gold |
|---|---|
| `Ines Mätzel` | `Ines Mätzel` |

**Missed by this rule (FN):**

- `Barbara Nellen` (person)
- `Baldur Neander` (person)

**Example 5** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_12`)


Durch die Abweisung des in der Hauptverhandlung vom 10. Dezember 2012 gestellten Antrags „auf Einvernahme der Zeugen Baldur Nauendorff und Barbara Neithardt zur Glaubwürdigkeit und Verhalten des Ares Mittas ... zum normalen Verhalten und zum Charakter des Opfers“ zum Beweis, dass es schwer einzuschüchtern sei und ein mehrmonatiges Schweigen über die inkriminierten Vorfälle „unwahrscheinlich“ und eine Verhaltensänderung erst zu Ostern 2011 aufgetreten sei (ON 38 S 14, 16), wurden Verteidigungsrechte des Angeklagten nicht verletzt, weil der Beweisantrag auf einen Erkundungsbeweis ohne erhebliches (Ratz, WK-StPO § 281 Rz 340) Beweisthema abzielte, zumal das Beweisbegehren - im Gegensatz zur darüber hinaus gehenden Verfahrensrüge - auf keine habituelle Falschbezichtigungstendenz im Sinn einer notorischen Lügenhaftigkeit (vgl 15 Os 54/05p;

| Predicted | Gold |
|---|---|
| `Baldur Nauendorff` | `Baldur Nauendorff` |

**Missed by this rule (FN):**

- `Barbara Neithardt` (person)
- `Mittas` (person)

**Example 6** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_17`)


Unter dem Gesichtspunkt der Unvollständigkeit kann zwar auch die Beurteilung der Überzeugungskraft von Aussagen mangelhaft erscheinen, wenn sich das Gericht mit gegen die Glaubwürdigkeit sprechenden Beweisergebnissen nicht auseinandergesetzt hat (RIS-Justiz RS0119422), doch haben die Tatrichter die widersprüchlichen Angaben des Zeugen Ares Mergans ohnedies erörtert (US 5 f) und auch die Angaben der Zeugen Barbara Novikowa und Baldur Newton, wonach dieser öfter lüge, in ihre Überlegungen miteinbezogen(US 6).

| Predicted | Gold |
|---|---|
| `Barbara Novikowa` | `Barbara Novikowa` |

**Missed by this rule (FN):**

- `Mergans` (person)
- `Baldur Newton` (person)

**Example 7** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_18`)


Mit dem Vorbringen, die erkennenden Richter hätten nur pauschal auf die Aussagen der Zeugen Barbara Nicoletti, Baldur Nafziger, Roderich Neimayer und Ines Mairhans verwiesen, ohne sich mit ihnen näher auseinanderzusetzen, übergeht der Beschwerdeführer die erstgerichtlichen Erwägungen in Ansehung der Zeugen Barbara Neger, Baldur Nessmann und Ines Masmann (US 6).

| Predicted | Gold |
|---|---|
| `Barbara Nicoletti` | `Barbara Nicoletti` |
| `Barbara Neger` | `Barbara Neger` |

**Missed by this rule (FN):**

- `Baldur Nafziger` (person)
- `Roderich Neimayer` (person)
- `Ines Mairhans` (person)
- `Baldur Nessmann` (person)
- `Ines Masmann` (person)

**Example 8** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_19`)


Darüber hinaus macht die Rüge nicht deutlich, weshalb die Angaben des Zeugen Roderich Neckell (der das Opfer als aggressives Kind darstellte, das sich nichts gefallen lässt;

| Predicted | Gold |
|---|---|
| `Roderich Neckell` | `Roderich Neckell` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_16`)


Insoweit sich die Mängelrüge mit dem Aussageverhalten des Zeugen Ares Masurkewitz auseinandersetzt, lässt sie außer Acht, dass der zur Überzeugung der Tatrichter von der Glaubwürdigkeit von Zeugen aufgrund des in der Hauptverhandlung gewonnenen persönlichen Eindrucks führende kritisch-psychologische Vorgang als solcher einer Anfechtung mit Nichtigkeitsbeschwerde entrückt ist (RIS-Justiz RS0106588;Ratz, WK-StPO § 281 Rz 431).

**False Positives:**

- `Ares Masurkewitz` — partial — gold is substring of pred: `Masurkewitz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Masurkewitz`(person)

**Example 1** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_17`)


Unter dem Gesichtspunkt der Unvollständigkeit kann zwar auch die Beurteilung der Überzeugungskraft von Aussagen mangelhaft erscheinen, wenn sich das Gericht mit gegen die Glaubwürdigkeit sprechenden Beweisergebnissen nicht auseinandergesetzt hat (RIS-Justiz RS0119422), doch haben die Tatrichter die widersprüchlichen Angaben des Zeugen Ares Mergans ohnedies erörtert (US 5 f) und auch die Angaben der Zeugen Barbara Novikowa und Baldur Newton, wonach dieser öfter lüge, in ihre Überlegungen miteinbezogen(US 6).

**False Positives:**

- `Ares Mergans` — partial — gold is substring of pred: `Mergans`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mergans`(person)
- `Barbara Novikowa`(person)
- `Baldur Newton`(person)

**Example 2** (doc_id: `deanon_260716_TRAIN/7Ob22_24x`) (sent_id: `deanon_260716_TRAIN/7Ob22_24x_16`)


Der Antragsgegner, der den Zeugen Jehovas beigetreten war, setzt die Antragstellerin immer wieder unter psychischen Druck, indem er ihr Feiern und das Tragen von Röcken verbot.

**False Positives:**

- `Jehovas` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `KommR Title Pattern` 

**F1:** 0.001 | **Precision:** 0.667 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1cfd4b3d`  
**Description:**
Matches 'KommR' title followed by name, e.g., 'KommR Gregor Luethgarth'.

**Content:**
```
KommR\s+([A-Z][a-zäöüß]+\s+[A-Z][a-zäöüß]+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.667 | 0.000 | 0.001 | 3 | 2 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 1 | 1941 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/3Ob26_23d`) (sent_id: `deanon_260716_TRAIN/3Ob26_23d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Anton Reuschel, vertreten durch Mag. Christopher Schmied, Rechtsanwalt in Salzburg, gegen die beklagte Partei Marktgemeinde KommR Frieda Goetzens, vertreten durch Ebner Aichinger Guggenberger Rechtsanwälte GmbH in Salzburg, wegen Feststellung einer Dienstbarkeit und Beseitigung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 7. Dezember 2022, GZ 3 R 142/22f-17, womit das Urteil des Landesgerichts Salzburg vom 29. September 2022, GZ 9 Cg 47/22w-12, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `KommR Frieda Goetzens` | `KommR Frieda Goetzens` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Höllwerth` (person)
- `Hon.-Prof. Dr. Brenn` (person)
- `Dr. Weixelbraun-Mohr` (person)
- `Dr. Kodek` (person)
- `Dr. Stefula` (person)
- `Anton Reuschel` (person)
- `Mag. Christopher Schmied` (person)
- `Ebner Aichinger Guggenberger Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Salzburg` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/9ObA55_12x`) (sent_id: `deanon_260716_TRAIN/9ObA55_12x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten des Obersten Gerichtshofs Dr. Rohrer als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Hopf, die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Mag. Dr. Wolfgang Höfle und Dr. Peter Schnöller in der Arbeitsrechtssache der klagenden Partei KommR Svetlana Burgholt, vertreten durch Dr. Gerhard Hiebler, Dr. Gerd Grebenjak, Rechtsanwälte in Leoben, wider die beklagte Partei Katharina Hoentzsch GmbH, Kirchtratten 6, 3386 Weghof, Österreich, vertreten durch Dr. Annemarie Stipanitz-Schreiner, Dr. Helmut Klement, Rechtsanwälte in Graz, wegen 56.109 EUR sA, infolge der außerordentlichen Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 24. Februar 2012, GZ 6 Ra 85/11h-31, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `KommR Svetlana Burgholt` | `KommR Svetlana Burgholt` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Rohrer` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Dehn` (person)
- `Mag. Dr. Wolfgang Höfle` (person)
- `Dr. Peter Schnöller` (person)
- `Dr. Gerhard Hiebler` (person)
- `Dr. Gerd Grebenjak` (person)
- `Katharina Hoentzsch` (person)
- `Kirchtratten 6, 3386 Weghof, Österreich` (address)
- `Dr. Annemarie Stipanitz-Schreiner` (person)
- `Dr. Helmut Klement` (person)
- `Oberlandesgerichts Graz` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/9ObA82_20d`) (sent_id: `deanon_260716_TRAIN/9ObA82_20d_3`)


Kopf Der Oberste Gerichtshof hat als Revisions- und Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau und den Hofrat des Obersten Gerichtshofs Dr. Hargassner sowie die fachkundigen Laienrichter Mag. Dr. Bernhard Gruber (aus dem Kreis der Arbeitgeber) und Angela Taschek (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Marktgemeinde KommR KommR Piedro Leyendecker, vertreten durch Ehrenhöfer & Häusler Rechtsanwälte GmbH in Wiener Neustadt, gegen die beklagte Partei Milena Leinhaas, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, wegen 28.428,01 EUR sA, über den Rekurs und die außerordentliche Revision der klagenden Partei gegen den Beschluss (I.) und das Urteil (II.) des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 22. Juli 2020, GZ 9 Ra 111/19p-25, mit dem das Urteil des Landesgerichts Wiener Neustadt als Arbeits- und Sozialgericht vom 17. September 2019, GZ 9 Cga 126/18g-21, aus Anlass der Berufung der beklagten Partei hinsichtlich der Rückforderung einer Zahlung als nichtig aufgehoben und die Klage zurückgewiesen wurde und über Berufung der beklagen Partei hinsichtlich des Anspruchs nach dem OrgHG abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird teilweise Folge gegeben und der angefochtene Beschluss des Berufungsgerichts ersatzlos aufgehoben.

**False Positives:**

- `KommR Piedro Leyendecker` — partial — pred is substring of gold: `KommR KommR Piedro Leyendecker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hopf`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Fichtenau`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hargassner`(person)
- `Mag. Dr. Bernhard Gruber`(person)
- `KommR KommR Piedro Leyendecker`(person)
- `Ehrenhöfer & Häusler Rechtsanwälte GmbH`(organisation)
- `Milena Leinhaas`(person)
- `Kosch & Partner Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Wiener Neustadt`(organisation)

</details>

---

## `Dr Name Initial` 

**F1:** 0.000 | **Precision:** 0.333 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `550c9063`  
**Description:**
Matches Dr. followed by an initial and a surname, or multiple initials, to capture names like 'Dr. A. Kodek'.

**Content:**
```
Dr\.\s+([A-Z]\.(?:\s+[A-Z]\.)?\s+[A-Z][a-zäöüß]+(?:\s+-[A-Z][a-zäöüß]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.000 | 0.000 | 3 | 1 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 2 | 2198 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/9ObA44_11b`) (sent_id: `deanon_260716_TRAIN/9ObA44_11b_5`)


Dr. Wolfgang List, Rechtsanwalt in Wien, wider die beklagte Partei und Gegnerin der gefährdeten Partei Traude Uszpelkat, vertreten durch Dr. J. Pfurtscheller, Dr. Orgler, Mag. Huber, Rechtsanwälte in Innsbruck, wegen Feststellung des Fortbestands eines Arbeitsverhältnisses, in eventu Anfechtung einer Kündigung nach § 105 ArbVG (Streitwert jeweils 31.000 EUR), in eventu 18.957 EUR sA, hier Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der klagenden und gefährdeten Partei gegen den Beschluss des Oberlandesgerichts Innsbruck als Rekursgericht in Arbeits- und Sozialrechtssachen vom 24. Februar 2011, GZ 15 Ra 11/11x-15, mit dem infolge Rekurses der klagenden und gefährdeten Partei der Beschluss des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 9. Dezember 2010, GZ 43 Cga 126/10y-8, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. J. Pfurtscheller` | `Dr. J. Pfurtscheller` |

**Missed by this rule (FN):**

- `Dr. Wolfgang List` (person)
- `Traude Uszpelkat` (person)
- `Dr. Orgler` (person)
- `Mag. Huber` (person)
- `Oberlandesgerichts Innsbruck` (organisation)
- `Landesgerichts Innsbruck` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/2Ob89_17b`) (sent_id: `deanon_260716_TRAIN/2Ob89_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende, die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé sowie den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Dipl.-Ing. Eleonore Wagenbret, vertreten durch Posch, Schausberger & Lutz Rechtsanwälte GmbH in Wels, gegen die beklagten Parteien 1. Rudolfa Schoenmaekers, 2. Lorena Sieckkötter, und 3. TraunSanitär Dienstleistungen Versicherungs-AG, Georg Pfligersdorffer-Gasse 71, 3610 Maigen, Österreich, alle vertreten durch Mag. Dr. A. Michael Dallinger, Rechtsanwalt in Wels, wegen 187.040,19 EUR sA und Feststellung (Streitinteresse: 5.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 1. März 2017, GZ 6 R 30/17z-42, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. A. Michael` — partial — pred is substring of gold: `Mag. Dr. A. Michael Dallinger`

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

**Example 1** (doc_id: `deanon_260716_TRAIN/9ObA76_13m`) (sent_id: `deanon_260716_TRAIN/9ObA76_13m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras, die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner und Mag. Ernst Bassler als weitere Richter in der Arbeitsrechtssache der klagenden Partei Adrian Leiße, BSc, vertreten durch Dr. H. Burmann ua, Rechtsanwälte in Innsbruck, gegen die beklagten Parteien 1. Logkraft-Verlag GmbH & Co KG, 2.

**False Positives:**

- `Dr. H. Burmann` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hopf`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Dehn`(person)
- `Mag. Dr. Rolf Gleißner`(person)
- `Mag. Ernst`(person)
- `Adrian Leiße, BSc`(person)
- `Logkraft-Verlag GmbH & Co KG`(organisation)

</details>

---

## `Mag.a Name` 

**F1:** 0.000 | **Precision:** 0.250 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2b572518`  
**Description:**
Matches Mag.a (female Magister) followed by full names, including hyphenated surnames.

**Content:**
```
Mag\.a\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+-[A-Z][a-zäöüß]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.250 | 0.000 | 0.000 | 4 | 1 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 3 | 3816 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_5`)


Dr. Felix Cornils, Niederlande, beide vertreten durch Tramposch & Partner, Rechtsanwälte KG in Innsbruck, gegen die beklagte Partei Mag.a Constanze Rizzo, vertreten durch König Ermacora Klotz & Partner, Rechtsanwälte in Innsbruck, wegen je 15.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 1. Juli 2020, GZ 10 R 16/20h-49, mit dem das Urteil des Landesgerichts Innsbruck vom 6. Februar 2020, GZ 41 Cg 11/19i-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag.a Constanze Rizzo` | `Mag.a Constanze Rizzo` |

**Missed by this rule (FN):**

- `Dr. Felix Cornils` (person)
- `Tramposch & Partner, Rechtsanwälte KG` (organisation)
- `Oberlandesgerichts Innsbruck` (organisation)
- `Landesgerichts Innsbruck` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/6Ob182_20p`) (sent_id: `deanon_260716_TRAIN/6Ob182_20p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden und die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des Minderjährigen ÖkR Techn R Mag.a Helge Cigan, geboren am 13. Dezember 2007, 3. September 1976, vertreten durch das Land Wien (Stadt Wien Kinder- und Jugendhilfe Rechtsvertretung Bezirk 22, 1220 Wien, Simone-de-Beauvoir-Platz 6) als Kinder- und Jugendhilfeträger, über den Revisionsrekurs des Vaters Quentin Martschinke, vertreten durch Anwaltssocietät Sattlegger Dorninger Steiner & Partner in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 25. Juni 2020, GZ 43 R 237/20a-31, mit dem der Beschluss des Bezirksgerichts Donaustadt vom 21. April 2020, GZ 1 P 135/18y-22, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wirdzurückgewiesen.

**False Positives:**

- `Mag.a Helge Cigan` — partial — pred is substring of gold: `ÖkR Techn R Mag.a Helge Cigan`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 1** (doc_id: `deanon_260716_TRAIN/9ObA109_13i`) (sent_id: `deanon_260716_TRAIN/9ObA109_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras, die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner und Mag. Thomas Kallab als weitere Richter in der Arbeitsrechtssache der klagenden Partei PhD Mag.a Traude Eyssner, gegen die beklagte Partei Mag. Siegmund Liepinsky, vertreten durch Hochleitner Rechtsanwälte GmbH in Linz, wegen 3.674,41 EUR brutto abzüglich 181,96 EUR netto sA (Revisionsinteresse 1.572,49 EUR brutto sA), über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 23. Mai 2013, GZ 8 Ra 36/13t-44, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Mag.a Traude Eyssner` — partial — pred is substring of gold: `PhD Mag.a Traude Eyssner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hopf`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Dehn`(person)
- `Mag. Dr. Rolf Gleißner`(person)
- `Mag. Thomas Kallab`(person)
- `PhD Mag.a Traude Eyssner`(person)
- `Mag. Siegmund Liepinsky`(person)
- `Hochleitner Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/9ObA4_13y`) (sent_id: `deanon_260716_TRAIN/9ObA4_13y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Werner Rodlauer und Mag. Robert Brunner als weitere Richter in der Arbeitsrechtssache der klagenden Partei OSR Mag.a Amber Mittelhäußer, vertreten durch Dr. Susanne Kuen, Rechtsanwältin in Wien, gegen die beklagte Partei Klaussen Metall GmbH, Urlakenstraße 5W, 3912 Kleingöttfritz, Österreich, vertreten durch Fellner Wratzfeld & Partner Rechtsanwälte GmbH in Wien, wegen 125.731,44 EUR sA, über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 30. Oktober 2012, GZ 11 Ra 82/12a-74, mit dem das Urteil des Landesgerichts Steyr als Arbeits- und Sozialgericht vom 31. Juli 2012, GZ 9 Cga 245/08g-70, aufgehoben und die Rechtssache an das Erstgericht zurückverwiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Mag.a Amber Mittelhäußer` — partial — pred is substring of gold: `OSR Mag.a Amber Mittelhäußer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hopf`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Dehn`(person)
- `Mag. Robert Brunner`(person)
- `OSR Mag.a Amber Mittelhäußer`(person)
- `Dr. Susanne Kuen`(person)
- `Klaussen Metall GmbH`(organisation)
- `Urlakenstraße 5W, 3912 Kleingöttfritz, Österreich`(address)
- `Fellner Wratzfeld & Partner Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Steyr`(organisation)

</details>

---

## `Standalone Name Legal Context` 🏆

**F1:** 0.056 | **Precision:** 0.151 | **Recall:** 0.035  

**Format:** `regex`  
**Rule ID:** `693bfd60`  
**Description:**
Matches standalone first and last names in legal contexts where they are the subject or object of a crime/proceeding, using specific German legal prepositions and verbs to avoid matching court names. Requires two capitalized words to distinguish from single-word nouns.

**Content:**
```
(?:wurde|gegen|des|der|die|von|mit|durch|als|und|sowie|im|am|bei|nach|vor|über|unter|ohne|neben|zwischen|trotz|wegen|statt|außer|seit|während|bis|um|für|an|auf|in)\s+([A-Z][a-zäöüß]+\s+[A-Z][a-zäöüß]+(?:\s+-[A-Z][a-zäöüß]+)*)\b(?=\s+(?:des|der|die|von|mit|durch|als|und|sowie|im|am|bei|nach|vor|über|unter|ohne|neben|zwischen|trotz|wegen|statt|außer|seit|während|bis|um|für|an|auf|in|,|\.|\(|\))|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.151 | 0.035 | 0.056 | 963 | 145 | 818 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 145 | 818 | 4016 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_5`)


Text B e g r ü n d u n g : Die minderjährige Annabelle ist das eheliche Kind der Andrea Tiedens und des Tunde Anthony Tkaceva.

| Predicted | Gold |
|---|---|
| `Andrea Tiedens` | `Andrea Tiedens` |

**Missed by this rule (FN):**

- `Tunde Anthony Tkaceva` (person)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_8`)


Laut der Aktenlage wurde sie von Ottokar Lienhard in Großbritannien mit dem Hauptsitz in Kreuzbühelgasse 27, 5204 Steindorf, Österreich Hampshire gegründet und ins britische Firmenbuch eingetragen.

| Predicted | Gold |
|---|---|
| `Ottokar Lienhard` | `Ottokar Lienhard` |

**Missed by this rule (FN):**

- `Kreuzbühelgasse 27, 5204 Steindorf, Österreich` (address)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_13`)


Am 12. 9. 2012 wurde der Zweitbeklagte auf Ersuchen des Ottokar Loehner als Nachfolger des Ing. Gerald Schmieden auch handelsrechtlicher Geschäftsführer.

| Predicted | Gold |
|---|---|
| `Ottokar Loehner` | `Ottokar Loehner` |

**Missed by this rule (FN):**

- `Ing. Gerald Schmieden` (person)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_16`)


Entgegen der Zusicherung des Ottokar Luxenburg anlässlich der Übernahme der handelsrechtlichen Geschäftsführerstellung kam es nie dazu, dass der Zweitbeklagte Einsicht in Buchhaltungsunterlagen, Baustellenabrechnungen und Kalkulationen erhielt. Er hatte keine Zeichnungsbefugnis für das Firmenkonto;

| Predicted | Gold |
|---|---|
| `Ottokar Luxenburg` | `Ottokar Luxenburg` |

**Example 4** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_30`)


Zweck dieser Lizenzvereinbarungen war, dem Kläger, der der Cousin des Ashley Jankunas (des geschäftsführenden Gesellschafters der Lizenznehmerinnen) ist, auf diese „steuerprivilegierte Weise“ seine Mitwirkung an der Prüfung von Heizanlagen(-teilen) und an der Weiterentwicklung dieser Heizanlagen, aber auch die dem Patent zugrunde liegende Erfindung abzugelten.

| Predicted | Gold |
|---|---|
| `Ashley Jankunas` | `Ashley Jankunas` |

**Example 5** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_84`)


Die Revisionsbeantwortung hält dem - soweit noch von Bedeutung - entgegen, anders als das Erstgericht habe das Berufungsgericht die Äußerungen des Klägers in seinem Gespräch mit Karsten Jodwerschat im Jahr 2006 nach den oberstgerichtlich judizierten Grundsätzen nicht als eine Kündigungserklärung ausgelegt.

| Predicted | Gold |
|---|---|
| `Karsten Jodwerschat` | `Karsten Jodwerschat` |

**Example 6** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_4`)


Text Begründung: Beim Bezirksgericht Innere Stadt Wien ist zur AZ 2 P 88/07t ein Pflegschaftsverfahren betreffend die mj Kinder Basil Biewer anhängig.

| Predicted | Gold |
|---|---|
| `Basil Biewer` | `Basil Biewer` |

**Missed by this rule (FN):**

- `Bezirksgericht Innere Stadt Wien` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_25`)


Mit dem nunmehr angefochtenen Beschluss vom 10. 12. 2014 (ON 106) gab das Rekursgericht dem Rekurs der Minderjährigen teilweise Folge und änderte den Titelbeschluss dahingehend ab, dass die Unterhaltspflicht ab 1. 3. 2012 mit monatlich insgesamt 220 EUR für Ludmilla Waßerthal und mit 160 EUR für Dipl. Kfm. Elias Meroldt festgesetzt wurde (Punkt 1 des Spruchs).

| Predicted | Gold |
|---|---|
| `Ludmilla Waßerthal` | `Ludmilla Waßerthal` |

**Missed by this rule (FN):**

- `Dipl. Kfm. Elias Meroldt` (person)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Ob57_13z`) (sent_id: `deanon_260716_TRAIN/10Ob57_13z_10`)


8. 2009 zuerkannte, und zwar in Höhe von (jeweils) 80 EUR monatlich für Ewald Eilderts und Enrico Steidel, von 70 EUR monatlich für KommR Techn R Elmira Roßmeir und von 60 EUR für Matthäus Christakopoulou. Es ging bei seiner Entscheidung aufgrund der Aktenlage davon aus, dass das gegenständliche Unterhaltsverfahren seit 12.

| Predicted | Gold |
|---|---|
| `Ewald Eilderts` | `Ewald Eilderts` |

**Missed by this rule (FN):**

- `Enrico Steidel` (person)
- `KommR Techn R Elmira Roßmeir` (person)
- `Matthäus Christakopoulou` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_19`)


Ist über die internationale Zuständigkeit bereits eine rechtskräftige Entscheidung ergangen, ist der Oberste Gerichtshof an diese Entscheidung gebunden (Garberin Fasching/Konecny3§ 28 JN Rz 25;

**False Positives:**

- `Oberste Gerichtshof` — type mismatch — same span as gold: `Oberste Gerichtshof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_6`)


Die in Wien ansässige klagende Gesellschaft nimmt die in Linz ansässige beklagte Gesellschaft beim Landesgericht Linz auf restliche Honorare für Planungsleistungen für ein Bauvorhaben in Klosterneuburg bei Wien in Anspruch.

**False Positives:**

- `Landesgericht Linz` — type mismatch — same span as gold: `Landesgericht Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Linz`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_29`)


Die Rechtssache weist keinen eindeutigen Schwerpunkt zum Landesgericht Korneuburg auf.

**False Positives:**

- `Landesgericht Korneuburg` — type mismatch — same span as gold: `Landesgericht Korneuburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Korneuburg`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_5`)


Die Mutter und die Kinder sind Staatsangehörige der Russischen Föderation und als Asylwerber im Inland aufhältig.

**False Positives:**

- `Russischen Föderation` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_6`)


Der Antragsgegner wohnt in der Russischen Förderation (Tschetschenien).

**False Positives:**

- `Russischen Förderation` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_23`)


Ohne rechtskräftigen Übertragungsbeschluss nach § 111 Abs 1 JN kommt eine Entscheidung des Obersten Gerichtshofs nach § 111 Abs 2 JN nicht in Betracht (RS0047067).

**False Positives:**

- `Obersten Gerichtshofs` — type mismatch — same span as gold: `Obersten Gerichtshofs`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_4`)


Text Begründung: Die Klägerin macht gegen die beklagte Partei, eine ägyptische Fluglinie, Ansprüche nach der Verordnung (EG) 261/2004 des Europäischen Parlaments und des Rates vom 11. Februar 2004 über eine gemeinsame Regelung für Ausgleichs- und Unterstützungsleistungen für Fluggäste im Fall der Nichtbeförderung und bei Annullierung oder großer Verspätung von Flügen (EU-Fluggastrechte-VO) geltend.

**False Positives:**

- `Europäischen Parlaments` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_5`)


Der in Österreich wohnhafte Kläger erhob gegen das beklagte Luftfahrtunternehmen mit Sitz im Vereinigten Königreich Klage auf Zahlung von 82,39 EUR sA aufgrund der Verordnung (EG) Nr 261/2004 des Europäischen Parlaments und des Rates vom 11. Februar 2004 über eine gemeinsame Regelung für Ausgleichs- und Unterstützungsleistungen für Fluggäste im Fall der Nichtbeförderung und bei Annullierung oder großer Verspätung von Flügen (EU-FluggastVO).

**False Positives:**

- `Europäischen Parlaments` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_21`)


[7] 4.1 Der Oberste Gerichtshof hat Ordinationsanträgen bereits in einer Vielzahl von Entscheidungen stattgegeben, wenn der Kläger Ansprüche nach der EU-FluggastVO sonst in einem Drittstaat einklagen müsste und zwischen diesem Drittstaat und Österreich kein Vollstreckungsübereinkommen besteht (zB 6 Nc 1/19b ZVR 2019/114, 259 [Mayr];

**False Positives:**

- `Kläger Ansprüche` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_24`)


[8] 4.2 Auch im Verhältnis zu dem seit 1. 1. 2021 als Drittstaat anzusehenden Vereinigten Königreich Großbritannien und Nordirland (vgl Art 126 des Abkommens über den Austritt des Vereinigten Königreichs Großbritannien und Nordirland aus der Europäischen Union und der Europäischen Atomgemeinschaft, ABl C 384 1/1 [idF: Austrittsabkommen]) liegt eine vergleichbare Situation vor: [9] 4.3 Entscheidungen eines britischen Gerichts, die in einem nach dem Ablauf des 31.

**False Positives:**

- `Europäischen Union` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_8`)


Die - durch einen Notar mit Kanzleisitz in Wien vertretene - Witwe und die beiden minderjährigen Kinder des Verstorbenen, für die ein Rechtsanwalt mit Kanzleisitz in Wien als Kollisionskurator bestellt wurde, halten sich nach dem von ihnen bestätigten Antragsvorbringen ebenfalls im Sprengel des Bezirksgerichts Mödling auf.

**False Positives:**

- `Bezirksgerichts Mödling` — type mismatch — same span as gold: `Bezirksgerichts Mödling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Mödling`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_6`)


Die Leistungen der beklagten Partei seien in Bezug auf Trittschallschutz-Decke und Bodenaufbau Nassräume und Technikräume mangelhaft, wodurch der klagenden Partei (in Form von Sanierungskosten und Mietzinsentgang) ein Schaden in Höhe des Klagsbetrags entstanden sei.

**False Positives:**

- `Bodenaufbau Nassräume` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_11`)


Das mangelhafte Objekt befinde sich in Wien, weshalb Sachverständige in Wien Befund aufzunehmen hätten.

**False Positives:**

- `Wien Befund` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_83`)


Eine Vereinbarung, wonach die Beklagte Zahlungen wegen Gewährleistungsansprüchen nicht zurückhalten dürfe (s RIS-Justiz RS0016592), wurde nämlich weder behauptet noch festgestellt. Dass die Beklagte Vorleistungspflichtige der Vorschüsse ist, führt nicht dazu, dass sie insoweit das Preisminderungsrecht nicht mit Einrede, sondern mit Klage geltend machen müsste, macht doch das Gesetz die Geltendmachung von Gewährleistungsrechten nicht von der Erfüllung der eigenen Verbindlichkeit abhängig.

**False Positives:**

- `Beklagte Zahlungen` — no gold match — likely missing annotation
- `Beklagte Vorleistungspflichtige` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 14** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Schneidergruberweg 37, 5132 Reith, Österreich, vertreten durch Dr. Alois Schneider, Rechtsanwalt in Rattenberg, wider die beklagte Partei Dario von Ebers, vertreten durch Dr. Walter Hausberger, Dr. Katharina Moritz und Dr. Alfred Schmidt, Rechtsanwälte in Wörgl, wegen Entfernung und Unterlassung (Revisionsinteresse 10.000 EUR), infolge Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 3. November 2017, GZ 3 R 172/17s-22, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Rattenberg vom 17. Mai 2017, GZ 3 C 401/15k-18, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Landesgerichts Innsbruck` — type mismatch — same span as gold: `Landesgerichts Innsbruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Stefula`(person)
- `Schneidergruberweg 37, 5132 Reith, Österreich`(address)
- `Dr. Alois Schneider`(person)
- `Dario von Ebers`(person)
- `Dr. Walter Hausberger`(person)
- `Dr. Katharina Moritz`(person)
- `Dr. Alfred Schmidt`(person)
- `Landesgerichts Innsbruck`(organisation)
- `Bezirksgerichts Rattenberg`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_44`)


DasBerufungsgerichtgab der Berufung des Beklagten Folge und wies das Klagebegehren ab.

**False Positives:**

- `Beklagten Folge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_102`)


Vielmehr ist der Wegfall des Sonderrechts Voraussetzung für die Löschung der Anmerkung nach Artikel V TirGARG.

**False Positives:**

- `Sonderrechts Voraussetzung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Bartholomäus Junghahn, geboren am 8. Mai 1999, und der minderjährigen HR Sophie Elefteriadis, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Zivilrechtssachen Wien` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Bartholomäus Junghahn`(person)
- `HR Sophie Elefteriadis`(person)
- `Magistrat der Stadt Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Favoriten`(organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_19`)


DasRekursgerichtgab dem Rekurs der beiden Minderjährigen Folge und änderte die Beschlüsse des Erstgerichts jeweils dahin ab, dass den Minderjährigen auch für den Monat Februar 2010 monatliche Unterhaltsvorschüsse in Höhe von 210 EUR (für den minderjährigen Ariadne Jefferys ) und von 180 EUR (für die minderjährige OStR Univ.-Prof.in Sascha Elfferding ) gewährt wurden.

**False Positives:**

- `Sascha Elfferding` — partial — pred is substring of gold: `OStR Univ.-Prof.in Sascha Elfferding`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ariadne Jefferys`(person)
- `OStR Univ.-Prof.in Sascha Elfferding`(person)

**Example 19** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Eva Abdelrahman, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei Hochenadel Immobilien GmbH, Ritterhof 11, 2661 Graben, Österreich, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Oberlandesgerichts Wien` — type mismatch — same span as gold: `Oberlandesgerichts Wien`

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

**Example 20** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_9`)


Mit der am 30. 8. 2010 eingebrachten Klage begehrte die Klägerin von der Beklagten Zahlung von 20.000 EUR sA wegen fehlerhafter Anlageberatung durch deren Mitarbeiter Ing. Marion Woltz im Zusammenhang mit dem Erwerb von Immofinanz- und Immoeast-Aktien.

**False Positives:**

- `Beklagten Zahlung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ing. Marion Woltz`(person)

**Example 21** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_15`)


Mit dem am Montag, dem 1. 7. 2013, im Elektronischen Rechtsverkehr beim Erstgericht eingebrachten Schriftsatz beantragte die Klägerin die Fortsetzung des Verfahrens.

**False Positives:**

- `Elektronischen Rechtsverkehr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_65`)


Die Klage wurde daher lange vor Ablauf der Verjährungsfrist eingebracht und der Fortsetzungsantrag rund sechs Monate nach dem Ablauf der ursprünglichen Verjährungsfrist gestellt. In der Entscheidung 6 Ob 822/81 (RIS-Justiz RS0034674) ist der Oberste Gerichtshof in einem Fall, in dem Ruhen des Verfahrens eingetreten war und beinahe ein Jahr nach Ablauf der dreijährigen Verjährungsfrist andauerte, von einer Verjährung mangels gehöriger Fortsetzung ausgegangen.

**False Positives:**

- `Oberste Gerichtshof` — type mismatch — same span as gold: `Oberste Gerichtshof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Juri Gerstl GmbH, Mutten 18, 3251 Schauboden, Österreich, vertreten durch Dr. Ralph Trischler, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, sowie die Nebenintervenientin auf Seiten der beklagten Partei Bundesbeschaffung GmbH, 1020 Wien, Lassallestraße 9b, vertreten durch die Olischar Rechtsanwaltsgesellschaft mbH in Wien, wegen 15.535 EUR sA, über den Revisionsrekurs der klagenden Partei (Revisionsinteresse: 7.460 EUR), gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 23. Februar 2023, GZ 16 R 168/22a-20, mit welchem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 5. September 2022, GZ 11 Cg 48/22t-12, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Oberlandesgerichts Wien` — type mismatch — same span as gold: `Oberlandesgerichts Wien`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 24** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_32`)


Nach ständiger Rechtsprechung des Obersten Gerichtshofs umfasst dieser Schadenersatzanspruch auch die Vertretungskosten im Zusammenhang mit einem auf Nichtigerklärung einer vergaberechtswidrigen Ausschreibung gerichteten Verfahren (RIS-Justiz RS0121198;

**False Positives:**

- `Obersten Gerichtshofs` — type mismatch — same span as gold: `Obersten Gerichtshofs`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Leander Lindlahr, geboren am 1. August 2011, und des mj Yussuf Prussog, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Zivilrechtssachen Wien` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Leander Lindlahr`(person)
- `Yussuf Prussog`(person)
- `Magistrat der Stadt Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Bezirksgerichts Donaustadt`(organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des minderjährigen Cedric Annamüller, geboren am 8. März 2007, 16. Mai 1964, vertreten durch das Land Kärnten als Kinder- und Jugendhilfeträger (Magistrat der Landeshauptstadt Klagenfurt, Abteilung für Jugend und Familie, Bahnhofstraße 35, 9010 Klagenfurt am Wörthersee), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Graz, gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 8. Jänner 2016, GZ 4 R 283/15g-16, womit der Beschluss des Bezirksgerichts Klagenfurt vom 17. November 2015, GZ 1 Pu 69/10x-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Landesgerichts Klagenfurt` — type mismatch — same span as gold: `Landesgerichts Klagenfurt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Mag. Ziegelbauer`(person)
- `Cedric Annamüller`(person)
- `8. März`(date)
- `16. Mai 1964`(date)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts Klagenfurt`(organisation)
- `Bezirksgerichts Klagenfurt`(organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_34`)


Eine Antragsprüfung durch das Gericht ist nur erforderlich, wenn aufgrund der Aktenlage Zweifel an der Richtigkeit der Erklärung bestehen.

**False Positives:**

- `Aktenlage Zweifel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludmilla von Amelunxen, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, gegen die beklagte Partei Svetlana Leinhäuser, vertreten durch Dr. Thomas Brückl, Mag. Christian Breit, Rechtsanwälte in Ried im Innkreis, wegen 1.778,52 EUR und Unterlassung (Streitwert 2.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Wels als Berufungsgericht vom 25. Jänner 2023, GZ 21 R 2/23b-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Grieskirchen vom 27. Oktober 2022, GZ 3 C 642/20h-27, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Landesgerichts Wels` — type mismatch — same span as gold: `Landesgerichts Wels`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Mag. Schober`(person)
- `Dr. Annerl`(person)
- `Ludmilla von Amelunxen`(person)
- `Dr. Bernhard Birek`(person)
- `Svetlana Leinhäuser`(person)
- `Dr. Thomas Brückl`(person)
- `Mag. Christian Breit`(person)
- `Landesgerichts Wels`(organisation)
- `Bezirksgerichts Grieskirchen`(organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_95`)


In einem solchen Fall kann der Oberste Gerichtshof durch Urteil in der Sache selbst erkennen (§ 519 Abs 2 Satz 3 ZPO), sodass der Beschluss des Berufungsgerichts aufzuheben und die klageabweisende Entscheidung des Erstgerichts wiederherzustellen war.

**False Positives:**

- `Oberste Gerichtshof` — type mismatch — same span as gold: `Oberste Gerichtshof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Mag. Kevin Maassen, vertreten durch Dr. Clemens Lintschinger, Rechtsanwalt in Wien, gegen die beklagte Partei Hon.-Prof. Friedhelm Adde, vertreten durch Mag. Dr. Georg Backhausen, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 27. Jänner 2016, GZ 38 R 265/15z-45, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Zivilrechtssachen Wien` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Mag. Ziegelbauer`(person)
- `Mag. Kevin Maassen`(person)
- `Dr. Clemens Lintschinger`(person)
- `Hon.-Prof. Friedhelm Adde`(person)
- `Mag. Dr. Georg Backhausen`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_5`)


Anita Schetzel, vertreten durch die Summereder Pichler Wächter Rechtsanwälte GmbH in Leonding, wegen 12.750 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Wels als Berufungsgericht vom 13. Dezember 2023, GZ 21 R 277/23v-53, mit dem das Urteil des Bezirksgerichts Wels vom 23. August 2023, GZ 9 C 430/22s-47, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Die Revision wird in Ansehung der Klageforderungen von 2.700 EUR sA, 4.575 EUR sA und 450 EUR sA zurückgewiesen.

**False Positives:**

- `Landesgerichts Wels` — type mismatch — same span as gold: `Landesgerichts Wels`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Anita Schetzel`(person)
- `Landesgerichts Wels`(organisation)
- `Bezirksgerichts Wels`(organisation)

**Example 32** (doc_id: `deanon_260716_TRAIN/10Ob18_13i`) (sent_id: `deanon_260716_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei SüdSanitär Gruppe GmbH, Rinzendorf 28, 4501 Lindach, Österreich, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Handelsgerichts Wien` — type mismatch — same span as gold: `Handelsgerichts Wien`

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

**Example 33** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_3`)


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

**Example 34** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_19`)


[4] Dem Netzzugangsvertrag zwischen den Parteien liegen die Allgemeinen Bedingungen für den Zugang zum Verteilernetz der Antragsgegnerin (AB-VN) zugrunde.

**False Positives:**

- `Allgemeinen Bedingungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_26`)


2. Die erforderlichen Mess-, Steuer- und Datenübertragungseinrichtungen (im Folgenden: Messeinrichtungen) werden von Convaluni Elektro nach den technischen Erfordernissen und unter Berücksichtigung der berechtigten Interessen des Netzkunden hinsichtlich Art, Zahl, Ort und Größe festgelegt, eingebaut, überwacht, entfernt und erneuert, soweit nichts anderes vereinbart oder in der Systemnutzungsentgelt-Verordnung vorgesehen oder in den geltenden technischen Regeln festgelegt wurde.

**False Positives:**

- `Convaluni Elektro` — type mismatch — same span as gold: `Convaluni Elektro`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Convaluni Elektro`(organisation)

**Example 36** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Heimcon Software GmbH, H - Am Hang 3, 4912 Rettenbrunn, Österreich, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, gegen die beklagte Partei Gunter Landwirtschaft GmbH, Schlossfeld 38, 9300 Graßdorf, Österreich, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, wegen 7.731,06 EUR und Feststellung (Streitwert 20.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse insgesamt 11.597,42 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 216/14h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Oberlandesgerichts Linz` — type mismatch — same span as gold: `Oberlandesgerichts Linz`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 37** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_16`)


Mit Urteil des Bezirksgerichts Bezirksgericht für Handelssachen Wien vom 21.

**False Positives:**

- `Bezirksgerichts Bezirksgericht` — positional overlap with gold: `Bezirksgericht für Handelssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht für Handelssachen Wien`(organisation)

**Example 38** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_26`)


Weiters habe sie der Klägerin Zinsen und Prozesskosten, zu deren Zahlung sie im Verfahren vor dem Bezirksgericht Bezirksgericht Hall (in Tirol) verurteilt worden war, sowie die Kosten deren eigener Vertretung in diesem Verfahren zu ersetzen.

**False Positives:**

- `Klägerin Zinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Hall (in Tirol)`(organisation)

**Example 39** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der minderjährigen Annabelle Thurnher, geboren am 24. Juni 2001, vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung, Bezirk 10, 1100 Wien, Van der Nüll-Gasse 20), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 17. September 2009, GZ 44 R 454/09d-38, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Favoriten vom 16. Juni 2009, GZ 40 P 36/08f-U-26, teilweise abgeändert wurde, den B e s c h l u s s gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Zivilrechtssachen Wien` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schinko`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Hon.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Annabelle Thurnher`(person)
- `Magistrat der Stadt Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Favoriten`(organisation)

**Example 40** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_31`)


DasRekursgerichtgab dem vom Vater dagegen erhobenen Rekurs teilweise Folge, indem es der Minderjährigen Unterhaltsvorschüsse in Höhe von 100 EUR monatlich gewährte und das Mehrbegehren von 170 EUR monatlich abwies.

**False Positives:**

- `Minderjährigen Unterhaltsvorschüsse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei DDr.in Cornelia Rinaldo, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Conmon-Verlag Limited, Kroisegg 20, 4052 Fleckendorf, Österreich Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Oberlandesgerichts Wien` — type mismatch — same span as gold: `Oberlandesgerichts Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Mag. Schober`(person)
- `Dr. Annerl`(person)
- `DDr.in Cornelia Rinaldo`(person)
- `Dr. Sven Rudolf Thorstensen`(person)
- `Conmon-Verlag Limited`(organisation)
- `Kroisegg 20, 4052 Fleckendorf, Österreich`(address)
- `Brandl Talos Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 42** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_15`)


2010 geltenden Fassung des GSpG hat der Oberste Gerichtshof bereits in der – einen nahezu identen Sachverhalt betreffenden – Entscheidung 6 Ob 229/21a klargestellt, dass zwar das in § 21 Abs 2 Z 1 GSpG (bzw § 14 Abs 2 Z 1 GSpG) idF vor dem Budgetbegleitgesetz 2011 normierte Sitzerfordernis unionsrechtswidrig war und nach der Rechtsprechung des EuGH ein Mitgliedstaat keine (verwaltungs-)strafrechtlichen Sanktionen wegen einer nicht erfüllten Verwaltungsformalität verhängen darf, wenn er die Erfüllung dieser Formalität unter Verstoß gegen das Unionsrecht abgelehnt oder vereitelt hat, dass aber dieser Grundsatz schon deshalb nicht auf die vorliegende Konstellation übertragbar ist, weil die „Nichtigkeitssanktion“ im Sinn des § 879 Abs 1 ABGB keine vergleichbare staatliche Sanktion repressiver Natur darstellt. Weiters führte der Oberste Gerichtshof in der zitierten Entscheidung 6 Ob 229/21a aus, dass die zivilrechtliche Unerlaubtheit des Spiels eine Strafbarkeit im Sinn des § 168 StGB nicht voraussetzt (4 Ob 70/22f mwH; RS0102178 [T10]).

**False Positives:**

- `Oberste Gerichtshof` — similar text (different position): `Oberste Gerichtshof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Oberste Gerichtshof`(organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_4`)


Malik Schoch, geboren 7. November 2002, 2. 7. Juli 2025, geboren 10. Juli 2004, und 3. Alan Schindlmair, geboren 7. August 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Timon Schönswetter, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Zivilrechtssachen Wien` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Wien`

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

**Example 44** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_4`)


Enns-Umwelt Consulting Limited, Alpineweg 221, 5730 Jochbergthurn, Österreich, 2. Ing. Lara Markart, letztere vertreten durch Radel Stampf Supper Rechtsanwälte OG in Mattersburg, wegen 160.422,79 EUR sA, infolge Revision der klagenden Partei (Revisionsinteresse 107.422,79 EUR sA) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Jänner 2015, GZ 4 R 119/14w-32, womit das Urteil des Landesgerichts St. Pölten vom 25. April 2014, GZ 37 Cg 96/13f-28, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Oberlandesgerichts Wien` — type mismatch — same span as gold: `Oberlandesgerichts Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Enns-Umwelt`(organisation)
- `Alpineweg 221, 5730 Jochbergthurn, Österreich`(address)
- `Ing. Lara Markart`(person)
- `Radel Stampf Supper Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts St. Pölten`(organisation)

**Example 45** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_10`)


2008 erfolgte die Eintragung beim Firmenbuch des Landesgerichts Eisenstadt mit einer Niederlassung in Angyalföldstraße 52, 4193 Hayrl, Österreich.

**False Positives:**

- `Landesgerichts Eisenstadt` — type mismatch — same span as gold: `Landesgerichts Eisenstadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts Eisenstadt`(organisation)
- `Angyalföldstraße 52, 4193 Hayrl, Österreich`(address)

**Example 46** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_16`)


Entgegen der Zusicherung des Ottokar Luxenburg anlässlich der Übernahme der handelsrechtlichen Geschäftsführerstellung kam es nie dazu, dass der Zweitbeklagte Einsicht in Buchhaltungsunterlagen, Baustellenabrechnungen und Kalkulationen erhielt. Er hatte keine Zeichnungsbefugnis für das Firmenkonto;

**False Positives:**

- `Zweitbeklagte Einsicht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ottokar Luxenburg`(person)

**Example 47** (doc_id: `deanon_260716_TRAIN/10Ob26_10m`) (sent_id: `deanon_260716_TRAIN/10Ob26_10m_5`)


Lars Ballogh, geboren am 3. Juli 2003, alle vertreten durch das Land Wien als Jugendwohlfahrtsträger (Amt für Jugend und Familie - Rechtsfürsorge Bezirke 17., 18. und 19., 1190 Wien, Gatterburggasse 12-14), wegen Unterhaltsvorschuss, über den „außerordentlichen Revisionsrekurs“ des Vaters Mag. Anton Bohmert, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. April 2009, GZ 44 R 193/08w-U140, womit der als Zulassungsvorstellung zu wertende „außerordentliche Revisionsrekurs“ des Vaters zurückgewiesen wurde, den Beschluss gefasst:  Spruch Der „außerordentliche Revisionsrekurs“ wird zurückgewiesen.

**False Positives:**

- `Zivilrechtssachen Wien` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lars Ballogh`(person)
- `Mag. Anton Bohmert`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 48** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_5`)


Unter Alver GmbH, beide Granglitzweg 11, 3251 Kroißenberg, Österreich, beide vertreten durch Dr. Michael Schneditz-Bolfras und andere Rechtsanwälte in Gmunden, wegen Bucheinsicht (in eventu Rechnungslegung) und Zahlung (Streitwert: 70.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Teilurteil des Oberlandesgerichts Linz als Berufungsgericht vom 17. Februar 2014, GZ 3 R 13/14y-90, womit das Urteil des Landesgerichts Wels vom 27. November 2013 (in der mit Beschluss vom 12. Dezember 2013 berichtigten Fassung), GZ 2 Cg 78/10p-82 und -84, abgeändert wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Oberlandesgerichts Linz` — type mismatch — same span as gold: `Oberlandesgerichts Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unter Alver GmbH`(organisation)
- `Granglitzweg 11, 3251 Kroißenberg, Österreich`(address)
- `Dr. Michael Schneditz-Bolfras`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Wels`(organisation)

**Example 49** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_43`)


Am 15. 2. und 5. 3. 2008 führten der Kläger und der nunmehrige Geschäftsführer der Beklagten Gespräche über eine allfällige künftige Mitarbeit des Klägers an der Entwicklungsarbeit der Beklagten.

**False Positives:**

- `Beklagten Gespräche` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_66`)


DasBerufungsgerichtgab der Berufung des Klägers Folge und änderte die Entscheidung des Erstgerichts als Teilurteil dahin ab, dass es die Beklagten verpflichtete, dem Kläger Bucheinsicht gemäß Punkt 1 seines Begehrens zu gewähren.

**False Positives:**

- `Klägers Folge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_98`)


Dies umso mehr als der Kläger danach gar keine Tätigkeiten mehr für die Lizenznehmerinnen entfaltete und erst im Jahr 2008 mit dem Geschäftsführer der Beklagten Verhandlungen über eine allfällige künftige Mitarbeit aufnahm.

**False Positives:**

- `Beklagten Verhandlungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_260716_TRAIN/10Ob28_19v`) (sent_id: `deanon_260716_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Bau Zorostfurt GmbH, Isbarystraße 47, 4152 Schölling, Österreich, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Buitenkamp und Rothauge Landwirtschaft GmbH, Gewerbegebiet Mathon 17, 3672 Reitern, Österreich, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Oberlandesgerichts Linz` — type mismatch — same span as gold: `Oberlandesgerichts Linz`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 53** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der zur AZ 38 Nc 13/08i beim Landesgericht für Zivilrechtssachen Wien anhängigen Ablehnungssache des Ablehnungswerbers Mag. Herwig Bortzlaff, über den Rekurs des Ablehnungswerbers gegen den Beschluss des Oberlandesgerichts Wien vom 10. November 2009, GZ 13 Nc 14/09x-2, womit ein Ablehnungsantrag zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Zivilrechtssachen Wien` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

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

**Example 54** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_5`)


Im Zusammenhang mit diesem Verfahren wies das Landesgericht für Zivilrechtssachen Wien mit Beschluss vom 26.

**False Positives:**

- `Zivilrechtssachen Wien` — partial — pred is substring of gold: `Landesgericht für Zivilrechtssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 55** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_11`)


Senats des Oberlandesgerichts Wien wegen Befangenheit ab.

**False Positives:**

- `Oberlandesgerichts Wien` — type mismatch — same span as gold: `Oberlandesgerichts Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgerichts Wien`(organisation)

**Example 56** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_13`)


Senat des Oberlandesgerichts Wien in der Besetzung Senatspräsidentin Dr. Paolo Barley sowie Mag. Klarissa Hausteiner und Mag. Viola Brauch als weitere Richter den Ablehnungsantrag des Ablehnungswerbers vom 24. 8. 2009 zurück.

**False Positives:**

- `Oberlandesgerichts Wien` — type mismatch — same span as gold: `Oberlandesgerichts Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgerichts Wien`(organisation)
- `Dr. Paolo Barley`(person)
- `Mag. Klarissa Hausteiner`(person)
- `Mag. Viola Brauch`(person)

**Example 57** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_22`)


Senat des Oberlandesgerichts Wien (AZ 12 Nc 44/09a) entschieden, dass dieser offenbar rechtsmissbräuchlich erhobene Ablehnungsantrag nicht zum Gegenstand einer gerichtlichen Entscheidung gemacht werden müsse.

**False Positives:**

- `Oberlandesgerichts Wien` — type mismatch — same span as gold: `Oberlandesgerichts Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgerichts Wien`(organisation)

**Example 58** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_36`)


Senats des Oberlandesgerichts Wien aufzuzeigen.

**False Positives:**

- `Oberlandesgerichts Wien` — type mismatch — same span as gold: `Oberlandesgerichts Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgerichts Wien`(organisation)

**Example 59** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Jaden Meyerjohann, geboren am 3. Juli 2020, Leroy Jungschmidt, geboren am 28. Mai 1965 und Clemens Theocharakis, geboren am 25. März 1999, in Pflege und Erziehung der Mutter Emanuela Janischefsky, vertreten durch das Land Vorarlberg als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Feldkirch, Schlossgraben 1, 6800 Feldkirch), wegen Gewährung von Unterhaltsvorschuss, über den Revisionsrekurs des Vaters Ashley Biesert, vertreten durch Mag. Hans-Christian Obernberger, Rechtsanwalt in Feldkirch, gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 12. Juli 2011, GZ 3 R 198/11g, 3 R 199/11d, 3 R 200/11a-18, womit die Beschlüsse des Bezirksgerichts Feldkirch vom 18. Mai 2011, GZ 12 Pu 141/11f-4 bis 6, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Landesgerichts Feldkirch` — type mismatch — same span as gold: `Landesgerichts Feldkirch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Jaden Meyerjohann`(person)
- `3. Juli 2020`(date)
- `Leroy Jungschmidt`(person)
- `28. Mai 1965`(date)
- `Clemens Theocharakis`(person)
- `25. März 1999`(date)
- `Emanuela Janischefsky`(person)
- `Bezirkshauptmannschaft Feldkirch`(organisation)
- `Ashley Biesert`(person)
- `Mag. Hans-Christian Obernberger`(person)
- `Landesgerichts Feldkirch`(organisation)
- `Bezirksgerichts Feldkirch`(organisation)

**Example 60** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_19`)


Nach Vorlage des Revisionsrekurses stellte der Oberste Gerichtshof mit Beschluss vom 25.

**False Positives:**

- `Oberste Gerichtshof` — type mismatch — same span as gold: `Oberste Gerichtshof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

**Example 61** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_39`)


2.1. Der Wirkungskreis in Kindschafts- und Sachwalterschaftsangelegenheiten umfasst die Geschäfte in Pflegschaftsangelegenheiten (§ 19 Abs 1 RpflG idF BGBl I 2009/30), zu denen alle Angelegenheiten des Kindschaftsrechts (Eltern-Kind-Verhältnisses im Sinn des Dritten Hauptstücks des ABGB), soweit sie minderjährige Kinder betreffen, zählen.

**False Positives:**

- `Dritten Hauptstücks` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_58`)


Auch in der Präambel zu Protokoll 2 über die einheitliche Auslegung des Übereinkommens und den Ständigen Ausschuss des (hier bei der Vorfragenprüfung anzuwenden) Lugano-Übereinkommens 2007 ist festgehalten, dass dieses Übereinkommen Teil des Gemeinschaftsrechts wird und der Gerichtshof der Europäischen Gemeinschaften deshalb für Entscheidungen über die Auslegung dieses Übereinkommens in Bezug auf dessen Anwendung durch die Gerichte zuständig ist.

**False Positives:**

- `Europäischen Gemeinschaften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_81`)


Nach dem Unterhaltsherabsetzungsantrag des Vaters vom 20. 12. 2011 (Band I, ON 29 und ON 30) wurde mit der Vorschussgewährung ohnehin bereits teilweise innegehalten, sodass anstatt der ursprünglich gewährten 791,50 EUR monatlich pro Kind nunmehr - wie der Vater beantragte - nur noch monatliche Unterhaltsvorschüsse von 300 EUR für Delila Maschmeier, 340 EUR für DDr.in Helena Jakobskötter und 330 EUR für Jaromir Tägder zur Auszahlung gelangen (Band I, ON 31, vgl auch Band II, ON 75, womit das Rekursgericht dem Erstgericht die Fortsetzung des Unterhaltsherabsetzungsverfahrens auftrug).

**False Positives:**

- `Helena Jakobskötter` — partial — pred is substring of gold: `DDr.in Helena Jakobskötter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Delila Maschmeier`(person)
- `DDr.in Helena Jakobskötter`(person)
- `Jaromir Tägder`(person)

**Example 64** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch und Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der minderjährigen Karsten Alberter, geboren am 2. April 2010, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Wien-Umgebung, Fachgebiet Jugendwohlfahrt), 3400 Klosterneuburg, Leopoldstraße 21, über das als „Berufung“ bezeichnete Rechtsmittel des Vaters Helmut Dreilich, gegen den Beschluss des Landesgerichts Korneuburg als Rekursgericht vom 25. März 2013, GZ 23 R 30/13v-53, womit der Beschluss des Bezirksgerichts Schwechat vom 27. August 2012, GZ 8 Pu 190/11i-39, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.  Text Begründung: Verfahrensgegenstand ist die Festsetzung des gesetzlichen Unterhalts für die mj Lena Amini.

**False Positives:**

- `Landesgerichts Korneuburg` — type mismatch — same span as gold: `Landesgerichts Korneuburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Karsten Alberter`(person)
- `2. April 2010`(date)
- `Helmut Dreilich`(person)
- `Landesgerichts Korneuburg`(organisation)
- `Bezirksgerichts Schwechat`(organisation)
- `Lena Amini`(person)

**Example 65** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende, den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber sowie die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Leander Andermann, vertreten durch Dr. Martin Leitner, Rechtsanwalt in Wien, gegen die beklagte Partei Ing. Ferdinand Abramova, vertreten durch Mag. Wilhelm Deutschmann MBA und Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M., Rechtsanwälte in Linz, wegen 500.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 11. Mai 2022, GZ 2 R 64/22b-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Oberlandesgerichts Linz` — type mismatch — same span as gold: `Oberlandesgerichts Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Mag. Schober`(person)
- `Dr. Annerl`(person)
- `Leander Andermann`(person)
- `Dr. Martin Leitner`(person)
- `Ing. Ferdinand Abramova`(person)
- `Mag. Wilhelm Deutschmann MBA`(person)
- `Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M.`(person)
- `Oberlandesgerichts Linz`(organisation)

**Example 66** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_35`)


[12] 1. Voranzustellen ist, dass die Vorinstanzen Wirkungen und Reichweite des erzielten außergerichtlichen Ausgleichs zu Recht nach den Bestimmungen über den Vergleich (§§ 1380 ff ABGB) beurteilt haben (RS0032499).

**False Positives:**

- `Vorinstanzen Wirkungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Oberlandesgerichts Wien` — type mismatch — same span as gold: `Oberlandesgerichts Wien`

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

**Example 68** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Karim Mielewczik, gegen die beklagte Partei Dr. Sandro Gädecken, vertreten durch Ing. Dr. Stefan Krall und Dr. Oliver Kühnl, Rechtsanwälte in Innsbruck, wegen 9.456 EUR sA (Revisionsinteresse 9.268,50 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 25. Februar 2025, GZ 21 R 434/24f-29, mit dem das Urteil des Bezirksgerichts Seekirchen am Wallersee vom 5. September 2024, GZ 2 C 1107/23d-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Landesgerichts Salzburg` — type mismatch — same span as gold: `Landesgerichts Salzburg`
- `Bezirksgerichts Seekirchen` — type mismatch — same span as gold: `Bezirksgerichts Seekirchen`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Dr. Annerl`(person)
- `Dr. Vollmaier`(person)
- `Dr. Wallner-Friedl`(person)
- `Karim Mielewczik`(person)
- `Dr. Sandro Gädecken`(person)
- `Ing. Dr. Stefan Krall`(person)
- `Dr. Oliver Kühnl`(person)
- `Landesgerichts Salzburg`(organisation)
- `Bezirksgerichts Seekirchen`(organisation)

**Example 69** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_37`)


In dem genannten Verfahren wurden der gefasste Gesellschafterbeschluss, womit die Ausschüttung des Gewinnanteils abgelehnt wurde, für nichtig erklärt, die weiteren Klagebegehren – unter Hinweis auf die Rechtsprechung des Obersten Gerichtshofs (RS0109584; insbesondere 6 Ob 169/16w) – abgewiesen und die Beklagte zum Kostenersatz in Höhe von 6.348,42 EUR verpflichtet.

**False Positives:**

- `Obersten Gerichtshofs` — type mismatch — same span as gold: `Obersten Gerichtshofs`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)

**Example 70** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_164`)


[42]5.2.1.Eine Anfechtungsklage kann nach der Rechtsprechung des Obersten Gerichtshofs mit dem Begehren auf Feststellung des tatsächlich zustandegekommenen Beschlusses verbunden werden („positive Beschlussfeststellungsklage“), wenn das Beschlussergebnis unzutreffend festgestellt wurde (RS0109584).

**False Positives:**

- `Obersten Gerichtshofs` — type mismatch — same span as gold: `Obersten Gerichtshofs`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)

**Example 71** (doc_id: `deanon_260716_TRAIN/10Ob3_12g`) (sent_id: `deanon_260716_TRAIN/10Ob3_12g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Maja Pirkmayr, vertreten durch Dr. Georg Gorton und DDr. Birgit Gorton, Rechtsanwälte in Klagenfurt, gegen die beklagte Partei Ing. Emanuel Puff, vertreten durch Dr. Gottfried Kassin, Rechtsanwalt in St. Veit an der Glan, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 26. Mai 2011, GZ 2 R 83/11z-49, mit dem das Urteil des Bezirksgerichts St. Veit an der Glan vom 29. Oktober 2010, GZ 3 C 333/09h-34, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Landesgerichts Klagenfurt` — type mismatch — same span as gold: `Landesgerichts Klagenfurt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Maja Pirkmayr`(person)
- `Dr. Georg Gorton`(person)
- `DDr. Birgit Gorton`(person)
- `Ing. Emanuel Puff`(person)
- `Dr. Gottfried Kassin`(person)
- `Landesgerichts Klagenfurt`(organisation)

**Example 72** (doc_id: `deanon_260716_TRAIN/10Ob3_12g`) (sent_id: `deanon_260716_TRAIN/10Ob3_12g_23`)


Wenn sich der Kläger mit dem Feststellungsbegehren auf einen Wasserzins von 1,30 EUR/m³ festlegen könne, wären für die Zukunft Rechtsstreitigkeiten über seine diesbezüglichen Ansprüche verhindert, sodass die Zulässigkeit der Feststellungsklage gegeben sein könnte.

**False Positives:**

- `Zukunft Rechtsstreitigkeiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Ziegelbauer als Vorsitzenden sowie die Hofrätin Dr. Faber und die Hofräte Mag. Schober, Dr. Thunhart und Dr. Annerl als weitere Richter in der Pflegschaftssache der minderjährigen Meinrad Bruhnsen, geboren 30. Januar 2006, vertreten durch das Land Wien als Träger der Kinder- und Jugendhilfe (Magistrat der Stadt Wien, Rechtsvertretung Bezirke 1, 4 bis 9, 1060 Wien, Amerlingstraße 11), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch die Präsidentin des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 31. Oktober 2022, GZ 43 R 323/22a-17, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 9. Juni 2022, GZ 4 Pu 58/22a-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Zivilrechtssachen Wien` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Wien`

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

**Example 74** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_26`)


Im Verfahren ist nicht strittig, dass Flüchtlinge nach der Genfer Flüchtlingskonvention (BGBl 1955/55, GFK) und dem Flüchtlingsprotokoll (BGBl 1974/78) österreichischen Staatsbürgern im Sinn des § 2 Abs 1 UVG gleichgestellt sind und daher Anspruch auf Unterhaltsvorschüsse haben (10 Ob 11/20w;

**False Positives:**

- `Genfer Flüchtlingskonvention` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_260716_TRAIN/10Ob41_14y`) (sent_id: `deanon_260716_TRAIN/10Ob41_14y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in den verbundenen Familienrechtssachen des Antragstellers DI Dr. Bodo Kaczynski, geboren am 25. Juli 1975, vertreten durch Mag. Werner Thurner, Rechtsanwalt in Graz, gegen die Antragsgegnerinnen 1. Wolfgang Lombardini, geboren am 4. Dezember 2022, 2. Livia Löblein, geboren am 11. Januar 1966, vertreten durch Mörth Ecker Filzmaier, Rechtsanwalts-Partnerschaft in Graz, wegen Unterhalt, über den Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 24. September 2013, GZ 2 R 11/13x-76, womit der Beschluss des Bezirksgerichts Graz-Ost vom 26. November 2012, GZ 231 Fam 14/11a, 231 Fam 17/11t, 231 Fam 18/11i-60, teilweise bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.  Text Begründung: DasErstgerichtsetzte den monatlichen Unterhalt für die Erstantragsgegnerin ab 1. 2. 2011 von 390 EUR um 30 EUR auf 360 EUR herab (Punkt 1);

**False Positives:**

- `Zivilrechtssachen Graz` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Graz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `DI Dr. Bodo Kaczynski`(person)
- `25. Juli 1975`(date)
- `Mag. Werner Thurner`(person)
- `Wolfgang Lombardini`(person)
- `4. Dezember 2022`(date)
- `Livia Löblein`(person)
- `11. Januar 1966`(date)
- `Mörth Ecker Filzmaier, Rechtsanwalts-Partnerschaft`(organisation)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)
- `Bezirksgerichts Graz-Ost`(organisation)

**Example 76** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_5`)


Dr. Felix Cornils, Niederlande, beide vertreten durch Tramposch & Partner, Rechtsanwälte KG in Innsbruck, gegen die beklagte Partei Mag.a Constanze Rizzo, vertreten durch König Ermacora Klotz & Partner, Rechtsanwälte in Innsbruck, wegen je 15.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 1. Juli 2020, GZ 10 R 16/20h-49, mit dem das Urteil des Landesgerichts Innsbruck vom 6. Februar 2020, GZ 41 Cg 11/19i-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Oberlandesgerichts Innsbruck` — type mismatch — same span as gold: `Oberlandesgerichts Innsbruck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Felix Cornils`(person)
- `Tramposch & Partner, Rechtsanwälte KG`(organisation)
- `Mag.a Constanze Rizzo`(person)
- `Oberlandesgerichts Innsbruck`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 77** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Pflegschaftssache 1. der mj Emma Mittelstaedt, geboren am 21. Mai 2025 und 2. des mj Milena Roesche, geboren am 25. Juni 1957, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung Bezirk 22, 1220 Wien, Hirschstettner Straße 19-21/Stiege N), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 10. Dezember 2014, GZ 42 R 343/13x, 42 R 344/13v und 42 R 345/13s-106, womit den Rekursen der Minderjährigen gegen den Beschluss des Bezirksgerichts Donaustadt vom 14. März 2013, GZ 3 Pu 61/12x-40, teilweise Folge gegeben wurde (Pkt 1 des Spruchs), dem Rekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen die Beschlüsse des Bezirksgerichts Donaustadt (jeweils) vom 6. Juni 2013, GZ 3 Pu 61/12x-49 und 3 Pu 61/12x-50, Folge gegeben (Pkt 2a des Spruchs), und aus Anlass des Rekurses die Anträge der Minderjährigen auf Gewährung von Unterhaltsvorschüssen zur Gänze abgewiesen wurden (Pkt 2b des Spruchs), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Zivilrechtssachen Wien` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Wien`
- `Bezirksgerichts Donaustadt` — similar text (different position): `Bezirksgerichts Donaustadt`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Mag. Korn`(person)
- `Emma Mittelstaedt`(person)
- `21. Mai 2025`(date)
- `Milena Roesche`(person)
- `25. Juni 1957`(date)
- `Magistrat der Stadt Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Donaustadt`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Bezirksgerichts Donaustadt`(organisation)

**Example 78** (doc_id: `deanon_260716_TRAIN/10Ob43_19z`) (sent_id: `deanon_260716_TRAIN/10Ob43_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Othmar Mertl, vertreten durch Nitsch Pajor Zöllner Rechtsanwälte OG in Mödling, gegen die beklagte Partei Stadtgemeinde Malik Fridt, vertreten durch Krist Bubits Rechtsanwälte OG in Mödling, wegen 1.) 21.216,92 EUR sA und 2.) Feststellung (Streitwert: 2.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Februar 2019, GZ 12 R 96/18b-36, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Wiener Neustadt vom 31. August 2018, GZ 20 Cg 86/17h-31, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Oberlandesgerichts Wien` — type mismatch — same span as gold: `Oberlandesgerichts Wien`

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

**Example 79** (doc_id: `deanon_260716_TRAIN/10Ob43_19z`) (sent_id: `deanon_260716_TRAIN/10Ob43_19z_50`)


Ein Handlauf – wie ihn der Oberste Gerichtshof in der Entscheidung 2 Ob 2288/96a für erforderlich halte – habe jedoch gefehlt. Durch die Querung des Weges verursache die Eisbearbeitungsmaschine auf dem Weg Eisflächen.

**False Positives:**

- `Oberste Gerichtshof` — type mismatch — same span as gold: `Oberste Gerichtshof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

**Example 80** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_8`)


Am 20. 9. 2016 beantragte die Antragstellerin beim Bezirksgericht Josefstadt die Erhöhung der monatlichen Unterhaltszahlung auf 440 EUR ab 1. 9. 2016.

**False Positives:**

- `Bezirksgericht Josefstadt` — type mismatch — same span as gold: `Bezirksgericht Josefstadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Josefstadt`(organisation)

**Example 81** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_9`)


Im Rahmen seiner Äußerung zu diesem Unterhaltserhöhungsantrag lehnte der Antragsgegner jeweils alle Richter des Bezirksgerichts Josefstadt und des diesem übergeordneten Landesgerichts für Zivilrechtssachen Wien ab.

**False Positives:**

- `Bezirksgerichts Josefstadt` — type mismatch — same span as gold: `Bezirksgerichts Josefstadt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgerichts Josefstadt`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 82** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_12`)


Da mehrere Senate des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht an dem genannten Verhalten beteiligt gewesen seien, sei auch das gesamte Landesgericht für Zivilrechtssachen Wien als befangen anzusehen, über den nunmehr geltend gemachten Unterhaltsanspruch zu entscheiden.

**False Positives:**

- `Zivilrechtssachen Wien` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Wien`
- `Zivilrechtssachen Wien` — similar text (different position): `Landesgerichts für Zivilrechtssachen Wien`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Landesgericht für Zivilrechtssachen Wien`(organisation)

**Example 83** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_32`)


2.2 Von diesen Grundsätzen der Rechtsprechung ist das Oberlandesgericht Wien bei seiner Entscheidung nicht abgewichen, wenn es den Ablehnungsantrag gegen alle Richter und Richterinnen des Landesgerichts für Zivilrechtssachen Wien und des Bezirksgerichts Josefstadt als nicht dem Gesetz gemäß ausgeführt zurückgewiesen hat.

**False Positives:**

- `Zivilrechtssachen Wien` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Wien`
- `Bezirksgerichts Josefstadt` — type mismatch — same span as gold: `Bezirksgerichts Josefstadt`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgericht Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Josefstadt`(organisation)

**Example 84** (doc_id: `deanon_260716_TRAIN/10Ob57_13z`) (sent_id: `deanon_260716_TRAIN/10Ob57_13z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der Kinder Mikolaj Eleftheriadou, geboren am 9. August 1991, Helge Schuchmann, geboren am 30. September 1992, mj Isabel Rahnfeld, geboren am 22. Dezember 1998 und mj PhD Daniel Coutand, geboren am 18. Jänner 2001, wegen Unterhaltsvorschuss, infolge Revisionsrekurses des Vaters Mag. Dirk Hükelheim, vertreten durch Mag. Roland Marko, Rechtsanwalt in Wien, dieser vertreten durch Dr. Francisco Rumpf, Rechtsanwalt in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 7. Juni 2013, GZ 43 R 391/08f ua -U-458, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 12. November 2007, GZ 2 P 88/07t-U-238, abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Zivilrechtssachen Wien` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Wien`

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

**Example 85** (doc_id: `deanon_260716_TRAIN/10Ob57_13z`) (sent_id: `deanon_260716_TRAIN/10Ob57_13z_22`)


Das Rekursgericht sprach aus, dass zur Frage, ob die Höhe von Unterhaltsvorschüssen gemäß § 4 Z 2 UVG eine von Amts wegen zu berücksichtigende Frage der Bemessung oder eine Frage der Versagung von Vorschüssen gemäß § 7 UVG sei, noch keine Rechtsprechung des Obersten Gerichtshofs vorliege, sodass der ordentliche Revisionsrekurs zulässig sei.

**False Positives:**

- `Obersten Gerichtshofs` — type mismatch — same span as gold: `Obersten Gerichtshofs`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)

**Example 86** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Cassandra Wespi, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Bilek Lebensmittel GmbH in Liqu, Dreijochgasse 11, 4722 Stefansdorf, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Oberlandesgerichts Wien` — type mismatch — same span as gold: `Oberlandesgerichts Wien`

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

**Example 87** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_30`)


Rechtliche Beurteilung Die Revision ist nicht zulässig, weil der Oberste Gerichtshof mittlerweile in der Entscheidung 9 Ob 60/19t vom 30.

**False Positives:**

- `Oberste Gerichtshof` — type mismatch — same span as gold: `Oberste Gerichtshof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

**Example 88** (doc_id: `deanon_260716_TRAIN/10Ob6_24s`) (sent_id: `deanon_260716_TRAIN/10Ob6_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Dr. Weber, Mag. Schober, Dr. Annerl und Dr. Vollmaier als weitere Richter in der Rechtssache des (ehemaligen) Klägers und Gegners der gefährdeten Parteien Agatha von der Heide, vertreten durch MMag. Dr. Sebastian Pribas, Rechtsanwalt in Dornbirn, als Verfahrenshelfer, dieser vertreten durch Mag. Benedikt Walch, Rechtsanwalt in Lech am Arlberg, gegen die (ehemals) Beklagte und erstgefährdete Partei Alva Sengül, sowie die zweitgefährdete Partei mj Selina Birkmeir, und die drittgefährdete Partei mj Harald Ladwig, LLM, alle wohnhaft in In der Klaus 72, 4785 Bach, Österreich, und vertreten durch Mag. German Bertsch, Rechtsanwalt in Feldkirch, wegen Ehescheidung sowie einstweiligem Ehegatten- und Kindesunterhalt, über den außerordentlichen Revisionsrekurs des Gegners der gefährdeten Parteien gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 22. September 2022, GZ 3 R 187/22f-323, womit der Beschluss des Bezirksgerichts Feldkirch vom 29. April 2022, GZ 2 C 23/17g-306, bestätigt wurde, den Beschluss gefasst:  Spruch In Ansehung der auf Zahlung von einstweiligem Ehegattenunterhalt gerichteten Begehren wird der außerordentliche Revisionsrekurs gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Landesgerichts Feldkirch` — type mismatch — same span as gold: `Landesgerichts Feldkirch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Dr. Weber`(person)
- `Mag. Schober`(person)
- `Dr. Annerl`(person)
- `Dr. Vollmaier`(person)
- `Agatha von der Heide`(person)
- `MMag. Dr. Sebastian Pribas`(person)
- `Mag. Benedikt Walch`(person)
- `Alva Sengül`(person)
- `Selina Birkmeir`(person)
- `Harald Ladwig, LLM`(person)
- `In der Klaus 72, 4785 Bach, Österreich`(address)
- `Mag. German Bertsch`(person)
- `Landesgerichts Feldkirch`(organisation)
- `Bezirksgerichts Feldkirch`(organisation)

**Example 89** (doc_id: `deanon_260716_TRAIN/10Ob6_24s`) (sent_id: `deanon_260716_TRAIN/10Ob6_24s_115`)


Die Rechtsprechung, wonach Aufwandsentschädigungen (Diäten, Taggeld, Nächtigungsgeld, Reisekostenentschädigungen und dergleichen) regelmäßig zur Hälfte in die Unterhaltsbemessungsgrundlage einzubeziehen sind, sofern der Unterhaltspflichtige nicht nachweist, dass diese darüber hinaus der Abdeckung berufsbedingter Mehrausgaben dienen (RS0047442 [T4]), soll nicht etwa auf eine allgemeine Vermutungsregel zugunsten des Unterhaltspflichtigen hinauslaufen, wonach diese Entschädigungen im Zweifelnurzur Hälfte als in die Unterhaltsbemessungsgrundlage einzubeziehende Einnahmen des Unterhaltspflichtigen zu behandeln wären.

**False Positives:**

- `Zweifelnurzur Hälfte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 90** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Ing. Christian Stangl-Brachnik, MA BA und Mag. Claudia Gründel (beide aus dem Kreis der Arbeitgeber) als weitere Richter in der Sozialrechtssache der klagenden Partei Mathias Jendl, vertreten durch Dr. Thomas Stampfer und Dr. Christoph Orgler, Rechtsanwälte in Graz, gegen die beklagte Partei Sozialversicherungsanstalt der Bauern, 1031 Wien, Ghegastraße 1, vertreten durch Dr. Michael Stögerer, Rechtsanwalt in Wien, wegen Ausgleichszulage, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2017, GZ 7 Rs 37/17s-11, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. April 2017, GZ 43 Cgs 113/17p-7, teils bestätigt und teils abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Oberlandesgerichts Graz` — type mismatch — same span as gold: `Oberlandesgerichts Graz`
- `Zivilrechtssachen Graz` — partial — pred is substring of gold: `Landesgerichts für Zivilrechtssachen Graz`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Ing. Christian Stangl-Brachnik, MA BA`(person)
- `Mag. Claudia Gründel`(person)
- `Mathias Jendl`(person)
- `Dr. Thomas Stampfer`(person)
- `Dr. Christoph Orgler`(person)
- `Dr. Michael Stögerer`(person)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)

**Example 91** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_51`)


Das Berufungsgericht ließ die Revision zu, weil sich der Oberste Gerichtshof mit der Frage, ob auf die Ausgleichszulage eines nach § 21 Abs 1 StGB untergebrachten Pensionsberechtigten ungeachtet der Legalzession des § 173 Abs 4 BSVG der Sachbezug der vollen freien Station anzurechnen ist, noch nicht befasst habe.

**False Positives:**

- `Oberste Gerichtshof` — type mismatch — same span as gold: `Oberste Gerichtshof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

</details>

---

## `Dr Name Full` 💣

**F1:** 0.001 | **Precision:** 0.083 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `39607e50`  
**Description:**
Matches Dr. followed by full names, explicitly allowing hyphenated surnames and multi-word names, with strict word boundary.

**Content:**
```
Dr\.\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.083 | 0.001 | 0.001 | 36 | 3 | 33 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 3 | 33 | 3431 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/6Ob139_19p`) (sent_id: `deanon_260716_TRAIN/6Ob139_19p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Balthasar Teske, vertreten durch Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG in Wien, gegen die beklagte Partei Prof. Dr. Roderich Claaßens, vertreten durch Brauneis Klauser Prändl Rechtsanwälte GmbH in Wien, wegen Rechnungslegung und Zahlung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 22. April 2019, GZ 14 R 152/18b-16, womit das Teilurteil des Landesgerichts für Zivilrechtssachen Wien vom 27. September 2018, GZ 4 Cg 50/17b-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Roderich Claaßens` | `Dr. Roderich Claaßens` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schramm` (person)
- `Dr. Gitschthaler` (person)
- `Univ.-Prof. Dr. Kodek` (person)
- `Dr. Nowotny` (person)
- `Dr. Faber` (person)
- `Balthasar Teske` (person)
- `Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG` (organisation)
- `Brauneis Klauser Prändl Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/7Ob130_16t`) (sent_id: `deanon_260716_TRAIN/7Ob130_16t_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und durch die Hofräte Dr. Höllwerth, Mag. Dr. Wurdinger, Mag. Malesich und Dr. Singer als weitere Richter in der Sachwalterschaftssache des Betroffenen Prof. Dr. Shirley Laaken, vertreten durch den Verfahrens- und einstweiligen Sachwalter Dr. Christian Fuchshuber, LL.M., Rechtsanwalt in Innsbruck, ehemaliger Verfahrens- und einstweiliger Sachwalter Univ.-Prof. Dr. Bernhard Sandberger, vertreten durch Dr. Klaus Rinner, Rechtsanwalt in Innsbruck, den Beschluss gefasst:  Spruch Der Schriftsatz des ehemaligen Verfahrens- und einstweiligen Sachwalters vom 4. Oktober 2016 wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Shirley Laaken` | `Dr. Shirley Laaken` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Dr. Höllwerth` (person)
- `Mag. Dr. Wurdinger` (person)
- `Mag. Malesich` (person)
- `Dr. Singer` (person)
- `Dr. Christian Fuchshuber, LL.M.` (person)
- `Dr. Bernhard Sandberger` (person)
- `Dr. Klaus Rinner` (person)

**Example 2** (doc_id: `deanon_260716_TRAIN/9Ob2_19p`) (sent_id: `deanon_260716_TRAIN/9Ob2_19p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsrekursgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätinnen und Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Dehn, Dr. Hargassner, Mag. Korn und Dr. Stefula in der Pflegschaftssache der mj OSR Noah Glaesser, geboren am 8. März 2015, wohnhaft bei der Mutter Mag. Bettina Ewerting, vertreten durch Dr. Karin Prutsch ua, Rechtsanwälte in Graz, Vater Prof. Dr. Oleg Bohl, vertreten durch BHF Briefer Hülle Frohner Rechtsanwälte OG in Wien, wegen Unterhalt, über den „außerordentlichen Revisionsrekurs“ der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 6. November 2018, GZ 1 R 240/18y-24, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt. Begründung:  Rechtliche Beurteilung Gemäß § 62 Abs 3 AußStrG ist der Revisionsrekurs – außer im Fall des § 63 Abs 3 AußStrG – jedenfalls unzulässig, wenn der Entscheidungsgegenstand an Geld oder Geldeswert insgesamt 30.000 EUR nicht übersteigt und das Rekursgericht nach § 59 Abs 1 Z 2 AußStrG den ordentlichen Revisionsrekurs für nicht zulässig erklärt hat.

| Predicted | Gold |
|---|---|
| `Dr. Oleg Bohl` | `Dr. Oleg Bohl` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Dehn` (person)
- `Dr. Hargassner` (person)
- `Mag. Korn` (person)
- `Dr. Stefula` (person)
- `OSR Noah Glaesser` (person)
- `8. März` (date)
- `Mag. Bettina Ewerting` (person)
- `Dr. Karin Prutsch` (person)
- `BHF Briefer Hülle Frohner Rechtsanwälte OG` (organisation)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/13Fss3_19y`) (sent_id: `deanon_260716_TRAIN/13Fss3_19y_3`)


Kopf Der Oberste Gerichtshof hat am 21. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und die Hofrätin des Obersten Gerichtshofs Dr. Brenner über den von Ing. Sebastian Novko im Verfahren AZ 5 Bl 6/19v des Landesgerichts für Strafsachen Graz gestellten Fristsetzungsantrag nach Einsichtnahme der Generalprokuratur in die Akten und Abstimmung gemäß § 62 Abs 1 zweiter Satz OGH-Geo 2019 den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Dr. Lässig` — partial — pred is substring of gold: `Prof. Dr. Lässig`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Lässig`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Brenner`(person)
- `Ing. Sebastian Novko`(person)
- `Landesgerichts für Strafsachen Graz`(organisation)
- `OGH`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/13Os105_19v`) (sent_id: `deanon_260716_TRAIN/13Os105_19v_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Lendl, Mag. Michel und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Roman Ueberlein und einen weiteren Angeklagten wegen des Verbrechens des schweren gewerbsmäßig durch Einbruch begangenen Diebstahls nach §§ 127, 128 Abs 1 Z 5, 129 Abs 2 Z 1 (iVm Abs 1 Z 1), 130 Abs 3 (iVm Abs 1 erster Fall) und 15 StGB sowie einer weiteren strafbaren Handlung, AZ 37 Hv 122/18b des Landesgerichts Innsbruck, über den Antrag des Verurteilten Roman Urbath auf Erneuerung des Strafverfahrens nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Dr. Lässig` — partial — pred is substring of gold: `Prof. Dr. Lässig`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Lässig`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Mag. Lendl`(person)
- `Mag. Michel`(person)
- `Dr. Brenner`(person)
- `Dr. Ondreasova`(person)
- `Roman Ueberlein`(person)
- `Landesgerichts Innsbruck`(organisation)
- `Roman Urbath`(person)

**Example 2** (doc_id: `deanon_260716_TRAIN/13Os108_19k`) (sent_id: `deanon_260716_TRAIN/13Os108_19k_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Alois Petraschek und andere Beschuldigte wegen des Vergehens der Untreue nach § 153 Abs 1 und 2 StGB aF und weiterer strafbarer Handlungen, AZ 5 Bl 6/19v des Landesgerichts für Strafsachen Graz, über die Anträge des Sebastian Neuhäußer auf Erneuerung des Strafverfahrens und auf Verlängerung der Frist zur Einbringung eines solchen Antrags nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Anträge werden zurückgewiesen.

**False Positives:**

- `Dr. Lässig` — partial — pred is substring of gold: `Prof. Dr. Lässig`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Lässig`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Mag. Michel`(person)
- `Dr. Oberressl`(person)
- `Dr. Brenner`(person)
- `Dr. Ondreasova`(person)
- `Alois Petraschek`(person)
- `Landesgerichts für Strafsachen Graz`(organisation)
- `Sebastian Neuhäußer`(person)

**Example 3** (doc_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a__3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Zoltan Schoenwiese wegen des Verbrechens des gewerbsmäßig und als Mitglied einer kriminellen Vereinigung durch Einbruch begangenen schweren Diebstahls nach §§ 127, 128 Abs 2, 129 Abs 1 Z 1, 130 Abs 1 erster und zweiter Fall, Abs 2 erster und zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 25 Hv 30/17m des Landesgerichts Eisenstadt, über die von der Generalprokuratur gegen das Urteil dieses Gerichts vom 6. Juni 2017 (ON 155) und einen Vorgang erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, und der Verteidigerin Mag. Urak zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Lässig` — partial — pred is substring of gold: `Prof. Dr. Lässig`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Lässig`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Mag. Michel`(person)
- `Dr. Oberressl`(person)
- `Dr. Brenner`(person)
- `Dr. Ondreasova`(person)
- `Zoltan Schoenwiese`(person)
- `Landesgerichts Eisenstadt`(organisation)
- `Mag. Höpler`(person)
- `Mag. Urak`(person)

**Example 4** (doc_id: `deanon_260716_TRAIN/13Os117_19h`) (sent_id: `deanon_260716_TRAIN/13Os117_19h_3`)


Kopf Der Oberste Gerichtshof hat am 26. Februar 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Schriftführers Dr. Schöll in der Strafsache gegen Martin Pfaffenberg wegen des Verbrechens der absichtlichen schweren Körperverletzung nach § 87 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 5. September 2019, GZ 43 Hv 73/19x-48, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Dr. Lässig` — partial — pred is substring of gold: `Prof. Dr. Lässig`

> overlaps gold: 1  |  likely missing annotation: 0

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
- `Martin Pfaffenberg`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/13Os34_19b`) (sent_id: `deanon_260716_TRAIN/13Os34_19b_3`)


Kopf Der Oberste Gerichtshof hat am 29. Mai 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Mag. Korner in der Strafsache gegen Wolfgang Weide wegen des Vergehens des Betrugs nach § 146 StGB, AZ 10 U 13/17b des Bezirksgerichts Weiz, über die von der Generalprokuratur gegen den Beschluss dieses Gerichts vom 25. Juli 2018 (ON 69) erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Ulrich, zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Lässig` — partial — pred is substring of gold: `Prof. Dr. Lässig`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Lässig`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Mag. Michel`(person)
- `Dr. Oberressl`(person)
- `Dr. Brenner`(person)
- `Mag. Korner`(person)
- `Wolfgang Weide`(person)
- `Bezirksgerichts Weiz`(organisation)
- `Dr. Ulrich`(person)

**Example 6** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__3`)


Kopf Der Oberste Gerichtshof hat am 26. Februar 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Schriftführers Dr. Schöll in der Strafsache gegen Robert Ultsch wegen des Vergehens der Urkundenfälschung nach § 223 Abs 1 StGB und einer weiteren strafbaren Handlung, AZ 13 U 351/18d des Bezirksgerichts Innere Stadt Wien, über den auf den Beschluss des Landesgerichts für Strafsachen Wien als Berufungsgericht vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), bezogenen Antrag der Generalprokuratur auf außerordentliche Wiederaufnahme des Verfahrens und über ihre gegen den Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30 der U-Akten) zur Wahrung des Gesetzes erhobene Nichtigkeitsbeschwerde nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Schneider, zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Lässig` — partial — pred is substring of gold: `Prof. Dr. Lässig`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 7** (doc_id: `deanon_260716_TRAIN/13Os99_19m`) (sent_id: `deanon_260716_TRAIN/13Os99_19m_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Christoph Holthuijsen wegen des Verbrechens der schweren Körperverletzung nach § 84 Abs 4 StGB, AZ 18 Hv 37/19b des Landesgerichts Klagenfurt, über die von der Generalprokuratur gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 21. August 2019, AZ 10 Bs 221/19d, ergriffene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Verteidigerin Mag. Sternad und des Privatbeteiligtenvertreters Mag. Höllwerth zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Lässig` — partial — pred is substring of gold: `Prof. Dr. Lässig`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Lässig`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Mag. Michel`(person)
- `Dr. Oberressl`(person)
- `Dr. Brenner`(person)
- `Dr. Ondreasova`(person)
- `Christoph Holthuijsen`(person)
- `Landesgerichts Klagenfurt`(organisation)
- `Oberlandesgerichts Graz`(organisation)
- `Mag. Höpler`(person)
- `Mag. Sternad`(person)
- `Mag. Höllwerth`(person)

**Example 8** (doc_id: `deanon_260716_TRAIN/14Ns52_18k`) (sent_id: `deanon_260716_TRAIN/14Ns52_18k_3`)


Kopf Der Oberste Gerichtshof hat am 13. November 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in der Strafsache gegen Daniel Bruchmüller wegen der Vergehen des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 erster und zweiter Fall, Abs 2 SMG in dem zu AZ 4 U 118/18k des Bezirksgerichts St. Pölten und zu AZ 18 U 242/18p des Bezirksgerichts Linz zwischen diesen Gerichten geführten Zuständigkeitsstreit nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung gemäß § 60 Abs 1 Satz 2 OGH-Geo.

**False Positives:**

- `Dr. Danek` — partial — pred is substring of gold: `Prof. Dr. Danek`

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
- `Daniel Bruchmüller`(person)
- `Bezirksgerichts St. Pölten`(organisation)
- `Bezirksgerichts Linz`(organisation)
- `OGH`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/14Ns5_20a`) (sent_id: `deanon_260716_TRAIN/14Ns5_20a_3`)


Kopf Der Oberste Gerichtshof hat am 24. Februar 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden sowie die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in der Straf- und Medienrechtssache der Privatanklägerin und Antragstellerin Petra Schwegle gegen den Angeklagten und Antragsgegner Holger Voelke wegen des Vergehens der üblen Nachrede nach § 111 StGB und einer weiteren strafbaren Handlung sowie § 6 Abs 1 und § 34 Abs 1 MedienG, AZ 92 Hv 58/19a des Landesgerichts für Strafsachen Wien, über den Antrag des Angeklagten und Antragsgegners auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

**False Positives:**

- `Dr. Danek` — partial — pred is substring of gold: `Prof. Dr. Danek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Danek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Hetlinger`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Petra Schwegle`(person)
- `Holger Voelke`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `OGH`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/14Os108_18s`) (sent_id: `deanon_260716_TRAIN/14Os108_18s_3`)


Kopf Der Oberste Gerichtshof hat am 13. November 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Kontrollorin Gsellmann als Schriftführerin in der Strafsache gegen Misha Riffart und andere Angeklagte wegen des Verbrechens des im Rahmen einer kriminellen Vereinigung gewerbsmäßig schweren und durch Einbruch begangenen Diebstahls nach §§ 127, 129 Abs 1 Z 2, Abs 2 Z 1, 130 Abs 2 und 3, jeweils iVm Abs 1 zweiter Fall, § 15 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Valeri Kunkelmann gegen das Urteil des Landesgerichts St. Pölten als Schöffengericht vom 28. Juni 2018, GZ 39 Hv 37/18x-157, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Dr. Danek` — partial — pred is substring of gold: `Prof. Dr. Danek`

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

**Example 11** (doc_id: `deanon_260716_TRAIN/14Os133_19v`) (sent_id: `deanon_260716_TRAIN/14Os133_19v_3`)


Kopf Der Oberste Gerichtshof hat am 14. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Mann und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Finanzstrafsache gegen Dr. Peter Johanni wegen des Finanzvergehens der Abgabenhinterziehung nach §§ 33 Abs 1, 13 FinStrG, AZ 14 Hv 3/10a des Landesgerichts für Strafsachen Wien, über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 23. Oktober 2019, AZ 23 Bs 323/19x, nach Einsichtnahme der Generalprokuratur in die Akten den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Dr. Danek` — partial — pred is substring of gold: `Prof. Dr. Danek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Danek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Hetlinger`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Mann`(person)
- `Dr. Setz-Hummel`(person)
- `Mag. Hauer`(person)
- `Dr. Peter Johanni`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/15Ns104_16m`) (sent_id: `deanon_260716_TRAIN/15Ns104_16m_3`)


Kopf Der Oberste Gerichtshof hat am 28. Dezember 2016 durch den Senatspräsident des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Mag. Lendl und Dr. Mann in der Strafsache gegen Markus Herdemertens wegen des Vergehens des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 erster und zweiter Fall und Abs 2 SMG, AZ 2 U 63/16z des Bezirksgerichts Bad Ischl, über den Antrag der Staatsanwaltschaft Wels auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

**False Positives:**

- `Dr. Danek` — partial — pred is substring of gold: `Prof. Dr. Danek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Danek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Lendl`(person)
- `Dr. Mann`(person)
- `Markus Herdemertens`(person)
- `Bezirksgerichts Bad Ischl`(organisation)
- `OGH`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/15Os107_16y`) (sent_id: `deanon_260716_TRAIN/15Os107_16y_3`)


Kopf Der Oberste Gerichtshof hat am 16. November 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Beran als Schriftführer in der Strafsache gegen Peter Eckehardt wegen des Vergehens der üblen Nachrede nach § 111 Abs 1 StGB und einer weiteren strafbaren Handlung, über die von der Generalprokuratur gegen den Beschluss des Bezirksgerichts Steyr vom 7. Mai 2013, GZ 5 U 44/12h-39, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Janda, sowie des Angeklagten zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Danek` — partial — pred is substring of gold: `Prof. Dr. Danek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Danek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Lendl`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Fürnkranz`(person)
- `Dr. Mann`(person)
- `Mag. Beran`(person)
- `Peter Eckehardt`(person)
- `Bezirksgerichts Steyr`(organisation)
- `Dr. Janda`(person)

**Example 14** (doc_id: `deanon_260716_TRAIN/15Os110_17s`) (sent_id: `deanon_260716_TRAIN/15Os110_17s_3`)


Kopf Der Oberste Gerichtshof hat am 19. September 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden und den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Shafiqullah Kira Nesselrodt und andere Angeklagte wegen des Verbrechens der absichtlichen schweren Körperverletzung nach §§ 15, 87 Abs 1 StGB, AZ 24 Hv 4/16v des Landesgerichts für Strafsachen Graz, über die Grundrechtsbeschwerde des Shafiqullah Erwin Nungässer gegen den Beschluss des Oberlandesgerichts Graz als Beschwerdegericht vom 8. März 2017, AZ 10 Bs 65/17k (ON 107 der Hv-Akten), nach Anhörung der Generalprokuratur zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Danek` — partial — pred is substring of gold: `Prof. Dr. Danek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Danek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Lendl`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Mann`(person)
- `Mag. Wetter`(person)
- `Kira Nesselrodt`(person)
- `Landesgerichts für Strafsachen Graz`(organisation)
- `Erwin Nungässer`(person)
- `Oberlandesgerichts Graz`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/15Os178_15p`) (sent_id: `deanon_260716_TRAIN/15Os178_15p_3`)


Kopf Der Oberste Gerichtshof hat am 1. Juli 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden in der Strafsache des Privatanklägers Mag. Ralph Kreickenbaum gegen Martin Rick wegen des Vergehens der üblen Nachrede nach § 111 Abs 1 und Abs 2 StGB, AZ 91 Hv 75/09d des Landesgerichts für Strafsachen Wien über den Antrag des Privatanklägers auf Verlängerung der Frist zur Äußerung zur Stellungnahme der Generalprokuratur den Beschluss gefasst:  Spruch Der Antrag des Privatanklägers Mag. Ralph Klosterkötter vom 27. Juni 2016 auf Verlängerung der Frist zur Äußerung zur Stellungnahme der Generalprokuratur wird abgewiesen.

**False Positives:**

- `Dr. Danek` — partial — pred is substring of gold: `Prof. Dr. Danek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Danek`(person)
- `Mag. Ralph Kreickenbaum`(person)
- `Martin Rick`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Mag. Ralph Klosterkötter`(person)

**Example 16** (doc_id: `deanon_260716_TRAIN/15Os50_15i`) (sent_id: `deanon_260716_TRAIN/15Os50_15i_3`)


Kopf Der Oberste Gerichtshof hat am 10. Juni 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann als weitere Richter in Gegenwart des Rechtspraktikanten Mag. Zechner als Schriftführer in der Strafsache gegen Manfred Mudder und einen weiteren Angeklagten wegen des Vergehens des Betrugs nach § 146 StGB und anderer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Linz als Schöffengericht vom 28. Jänner 2015, GZ 34 Hv 118/14b-50, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Dr. Danek` — partial — pred is substring of gold: `Prof. Dr. Danek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Danek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Lendl`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Fürnkranz`(person)
- `Dr. Mann`(person)
- `Mag. Zechner`(person)
- `Manfred Mudder`(person)
- `Landesgerichts Linz`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/17Os3_14s`) (sent_id: `deanon_260716_TRAIN/17Os3_14s_3`)


Kopf Der Oberste Gerichtshof hat am 12. Mai 2014 durch den Präsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Ratz als Vorsitzenden, die Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek und Hon.-Prof. Dr. Kirchbacher sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Kotanko als Schriftführerin in der Strafsache gegen Arno Enste wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Feldkirch als Schöffengericht vom 24. September 2013, GZ 50 Hv 37/13t-48, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Danek` — partial — pred is substring of gold: `Prof. Dr. Danek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Ratz`(person)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Danek`(person)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Dr. Oshidari`(person)
- `Mag. Kotanko`(person)
- `Arno Enste`(person)
- `Landesgerichts Feldkirch`(organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/1Ob78_22k`) (sent_id: `deanon_260716_TRAIN/1Ob78_22k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. HR Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Familienrechtssache des Antragstellers Dr. Erhard Hörl, vertreten durch den Erwachsenenvertreter Dr. Carla Hoffner, Rechtsanwalt in Wien, gegen die Antragsgegnerin Juliana Inderwiedenstraße, vertreten durch Dr. Karl Newole, Rechtsanwalt in Wien, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. Dezember 2021, GZ 44 R 449/21m-15, mit dem der Beschluss des Bezirksgerichts Josefstadt vom 29. November 2021, GZ 25 Fam 3/21k-10, bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

**False Positives:**

- `Dr. Bydlinski` — partial — pred is substring of gold: `Univ.-Prof. HR Dr. Bydlinski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. HR Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Mag. Wessely-Kristöfel`(person)
- `Dr. Parzmayr`(person)
- `Dr. Erhard Hörl`(person)
- `Dr. Carla Hoffner`(person)
- `Juliana Inderwiedenstraße`(person)
- `Dr. Karl Newole`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Josefstadt`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/23Os1_15t`) (sent_id: `deanon_260716_TRAIN/23Os1_15t_3`)


Kopf Der Oberste Gerichtshof als Disziplinargericht für Rechtsanwälte und Rechtsanwaltsanwärter hat am 9. November 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Anwaltsrichter Dr. Konzett und Mag. Brunar sowie den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Sailer in Gegenwart des Richteramtsanwärters Mag. Wüstner als Schriftführer in der Disziplinarsache gegen Dr. Amanda Monaco, Rechtsanwalt in Schwanngasse 23, 3240 Gries, Österreich, wegen der Disziplinarvergehen der Berufspflichtenverletzung und der Beeinträchtigung von Ehre oder Ansehen des Standes über die Berufung des Disziplinarbeschuldigten wegen Nichtigkeit, Schuld und Strafe gegen das Erkenntnis des Disziplinarrats der Vorarlberger Rechtsanwaltskammer vom 12. November 2014, GZ D 15/13 (DV 18/13)-10, nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Knibbe, des Kammeranwalts Dr. Hirsch, des Disziplinarbeschuldigten und seines Verteidigers Prof. Dr. Wennig zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Wennig` — partial — pred is substring of gold: `Prof. Dr. Wennig`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Philipp`(person)
- `Dr. Konzett`(person)
- `Mag. Brunar`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Mag. Wüstner`(person)
- `Dr. Amanda Monaco`(person)
- `Schwanngasse 23, 3240 Gries, Österreich`(address)
- `Mag. Knibbe`(person)
- `Dr. Hirsch`(person)
- `Prof. Dr. Wennig`(person)

**Example 20** (doc_id: `deanon_260716_TRAIN/3Ob72_20i`) (sent_id: `deanon_260716_TRAIN/3Ob72_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Marktgemeinde James Weyand, MA, vertreten durch Dr. Nader Karl Mahdi, Rechtsanwalt in Wattens, gegen die beklagte Partei Lützeler Garten AG, Esteplatz 2, 9064 Schöpfendorf, Österreich, vertreten durch Altenweisl Wallnöfer Watschinger Zimmermann Rechtsanwälte GmbH in Innsbruck, und die auf Seiten der beklagten Partei beigetretene Nebenintervenientin Demeyer u. Köktas Analyse GmbH, Zinkendorferstraße 100, 9321 Schöttlhof, Österreich, vertreten durch Dr. Christian Girardi, LL.M., Ing. Dr. Stefan Schwärzler, Mag. Daniel Pichler, Rechtsanwälte in Innsbruck, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. März 2020, GZ 1 R 5/20z-27, womit das Urteil des Landesgerichts Innsbruck vom 14. November 2019, GZ 12 Cg 33/19m-18, teilweise bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Dr. Stefan Schwärzler` — partial — pred is substring of gold: `Ing. Dr. Stefan Schwärzler`

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

**Example 21** (doc_id: `deanon_260716_TRAIN/8Ob101_14g`) (sent_id: `deanon_260716_TRAIN/8Ob101_14g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Prof. Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner und die Hofräte Mag. Ziegelbauer und Dr. Brenn als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Obere Ortsstraße 29, 2565 Holzschlag, Österreich, vertreten durch Mag. Hubertus Weben, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Gemeinde VetR Yelec Mente, wegen Feststellung, über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Innsbruck als Rekursgericht vom 2. September 2014, GZ 3 R 62/14p-5, mit dem der Beschluss des Landesgerichts Innsbruck vom 30. Juni 2014, GZ 17 Cg 68/14p-2, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen (§§ 528a, 510 Abs 3 ZPO).

**False Positives:**

- `Dr. Spenling` — partial — pred is substring of gold: `Prof. Dr. Spenling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Prof. Dr. Spenling`(person)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Tarmann-Prentner`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Brenn`(person)
- `Obere Ortsstraße 29, 2565 Holzschlag, Österreich`(address)
- `Mag. Hubertus Weben`(person)
- `VetR Yelec Mente`(person)
- `Oberlandesgerichts Innsbruck`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/8Ob132_16v`) (sent_id: `deanon_260716_TRAIN/8Ob132_16v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsrekursgericht durch den Vizepräsidenten des Obersten Gerichtshofs Prof. Dr. Spenling als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner, den Hofrat Dr. Brenn und die Hofrätinnen Mag. Korn und Dr. Weixelbraun-Mohr als weitere Richter in der Insolvenzsache des früheren Schuldners Dr. Mona Maiser, zuletzt wohnhaft in Uferstöcklstraße 12, 9462 Raning, Österreich, Insolvenzverwalter Dr. Kurt Freyler, Rechtsanwalt in Wien, über die Revisionsrekurse des Gläubigers Dr. Helmut Oberlies, vertreten durch Dr. Marlene Klein, Rechtsanwältin in Wien, gegen die Beschlüsse des Oberlandesgerichts Wien als Rekursgericht vom 18. November 2016, AZ 28 R 280/16a, 28 R 281/16y und GZ 28 R 282/16w-206, den Beschluss gefasst:  Spruch Die Revisionsrekurse werden zurückgewiesen.

**False Positives:**

- `Dr. Spenling` — partial — pred is substring of gold: `Prof. Dr. Spenling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Spenling`(person)
- `Dr. Tarmann-Prentner`(person)
- `Dr. Brenn`(person)
- `Mag. Korn`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Mona Maiser`(person)
- `Uferstöcklstraße 12, 9462 Raning, Österreich`(address)
- `Dr. Kurt Freyler`(person)
- `Dr. Helmut Oberlies`(person)
- `Dr. Marlene Klein`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/8Ob70_16a`) (sent_id: `deanon_260716_TRAIN/8Ob70_16a_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten des Obersten Gerichtshofs Prof. Dr. Spenling als Vorsitzenden sowie die Hofrätin Dr. Tarmann-Prentner, den Hofrat Dr. Brenn und die Hofrätinnen Mag. Korn und Dr. Weixelbraun-Mohr als weitere Richter in der Rechtssache der klagenden Partei Justin Bonaventura, vertreten durch Mag. Michael Stuxer, Rechtsanwalt in Wien, gegen die beklagte Partei Svenja Markowic, vertreten durch MMag. Johannes Pfeifer, Rechtsanwalt in Liezen, wegen 9.500 EUR sA und Räumung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Leoben vom 9. Mai 2016, GZ 1 R 48/16z-22, den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht aufgrund der von den Parteien angezeigten Vereinbarung des Ruhens des Verfahrens zurückgestellt. Begründung:  Rechtliche Beurteilung Die Streitteile zeigten die von ihnen getroffene Vereinbarung des („ewigen“) Ruhens des Verfahrens an.

**False Positives:**

- `Dr. Spenling` — partial — pred is substring of gold: `Prof. Dr. Spenling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Spenling`(person)
- `Dr. Tarmann-Prentner`(person)
- `Dr. Brenn`(person)
- `Mag. Korn`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Justin Bonaventura`(person)
- `Mag. Michael Stuxer`(person)
- `Svenja Markowic`(person)
- `MMag. Johannes Pfeifer`(person)
- `Landesgerichts Leoben`(organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/8Ob75_13g`) (sent_id: `deanon_260716_TRAIN/8Ob75_13g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Spenling als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner und die Hofräte Mag. Ziegelbauer und Dr. Brenn als weitere Richter in der Rechtssache der klagenden Partei Dr. Mikolaj Gedrim, vertreten durch Mag. Klaus P. Pichler, Rechtsanwalt in Dornbirn, und die Nebenintervenientin auf Seiten der klagenden Partei Kelver Maschinenbau Vertrieb GmbH, Jacobsgasse 5, 4742 Feldegg, Österreich, vertreten durch Mayrhofer, Plankel & Partner, Rechtsanwälte in Dornbirn, gegen die beklagte Partei Dr.in Hildegard Stanislaus, vertreten durch Rechtsanwälte Mandl GmbH in Feldkirch, und den Nebenintervenienten auf Seiten der beklagten Partei Ophelia Michelzöblein, vertreten durch Mag. Jürgen Nagel, Rechtsanwalt in Bregenz, wegen 64.718,68 EUR sA, und Feststellung (Streitwert: 4.000 EUR), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Entscheidungsbegründung im Beschluss des Obersten Gerichtshofs vom 26. Juni 2014, 8 Ob 75/13g, wird dahin berichtigt, dass der erste Satz im dritten Absatz des Punkts 4.4 zu lauten hat: „Zu ersetzen hat der Beklagte hingegen die Kosten der Wiedererrichtung der vertragsmäßig geschuldeten Straße.“

**False Positives:**

- `Dr. Spenling` — partial — pred is substring of gold: `Prof. Dr. Spenling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Spenling`(person)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Tarmann-Prentner`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Brenn`(person)
- `Dr. Mikolaj Gedrim`(person)
- `Mag. Klaus P. Pichler`(person)
- `Kelver Maschinenbau Vertrieb GmbH`(organisation)
- `Jacobsgasse 5, 4742 Feldegg, Österreich`(address)
- `Dr.in Hildegard Stanislaus`(person)
- `Ophelia Michelzöblein`(person)
- `Mag. Jürgen Nagel`(person)
- `Obersten Gerichtshofs`(organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/8Ob90_15s`) (sent_id: `deanon_260716_TRAIN/8Ob90_15s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten des Obersten Gerichtshofs Prof. Dr. Spenling als Vorsitzenden sowie die Hofrätin Dr. Tarmann-Prentner, die Hofräte Mag. Ziegelbauer und Dr. Brenn und die Hofrätin Dr. Weixelbraun-Mohr als weitere Richter in der Rechtssache der klagenden Partei mj HR Judith Jadamus, vertreten durch den Vater Bruno Magg, vertreten durch Dr. Michael Kowarz, Rechtsanwalt in Wals, gegen die beklagte Partei Ferdinand Tebbe, vertreten durch Dr. Herbert Gschöpf, Dr. Marwin Gschöpf, Rechtsanwälte in Velden, wegen 8.328,43 EUR sA und Feststellung (2.000 EUR), über die Revision der klagenden Partei (Revisionsinteresse 5.164,21 EUR sA) gegen das Urteil des Landesgerichts Salzburg vom 24. Juni 2015, GZ 22 R 161/15b-51, mit dem das Urteil des Bezirksgerichts St. Johann im Pongau vom 25. März 2015, GZ 2 C 128/13d-47, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Spenling` — partial — pred is substring of gold: `Prof. Dr. Spenling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Spenling`(person)
- `Dr. Tarmann-Prentner`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Brenn`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `HR Judith Jadamus`(person)
- `Bruno Magg`(person)
- `Dr. Michael Kowarz`(person)
- `Ferdinand Tebbe`(person)
- `Dr. Herbert Gschöpf`(person)
- `Dr. Marwin Gschöpf`(person)
- `Landesgerichts Salzburg`(organisation)
- `Bezirksgerichts St. Johann im Pongau`(organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/8Ob94_14b`) (sent_id: `deanon_260716_TRAIN/8Ob94_14b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Prof. Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner und die Hofräte Mag. Ziegelbauer und Dr. Brenn als weitere Richter in der Rechtssache der klagenden Parteien 1.

**False Positives:**

- `Dr. Spenling` — partial — pred is substring of gold: `Prof. Dr. Spenling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Prof. Dr. Spenling`(person)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Tarmann-Prentner`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Brenn`(person)

**Example 27** (doc_id: `deanon_260716_TRAIN/8Ob96_17a`) (sent_id: `deanon_260716_TRAIN/8Ob96_17a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsrekursgericht durch den Vizepräsidenten des Obersten Gerichtshofs Prof. Dr. Spenling als Vorsitzenden sowie die Hofrätin Dr. Tarmann-Prentner, den Hofrat Dr. Brenn und die Hofrätinnen Mag. Korn und Dr. Weixelbraun-Mohr als weitere Richter in der Rechtssache der Antragsteller 1.

**False Positives:**

- `Dr. Spenling` — partial — pred is substring of gold: `Prof. Dr. Spenling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Spenling`(person)
- `Dr. Tarmann-Prentner`(person)
- `Dr. Brenn`(person)
- `Mag. Korn`(person)
- `Dr. Weixelbraun-Mohr`(person)

**Example 28** (doc_id: `deanon_260716_TRAIN/8ObA13_15t`) (sent_id: `deanon_260716_TRAIN/8ObA13_15t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten des Obersten Gerichtshofs Prof. Dr. Spenling als Vorsitzenden und durch die Hofrätin des Obersten Gerichtshofs Dr. Tarmann-Prentner und den Hofrat des Obersten Gerichtshofs Dr. Brenn sowie die fachkundigen Laienrichter Dr. Christoph Kainz und Mag. Johann Schneller als weitere Richter in der Arbeitsrechtssache der klagenden Partei Louisa Niklei, Bakk. art., vertreten durch Orgler + Pfurtscheller, Rechtsanwälte in Innsbruck, gegen die beklagte Partei Gierhard Pharma GmbH, Batthyanystraße 10, 2812 Untereck, Österreich, vertreten durch Dr. Paul Delazer, Rechtsanwalt in Innsbruck, wegen Feststellung des aufrechten Bestands eines Dienstverhältnisses, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 17. Dezember 2014, GZ 13 Ra 46/14h-76, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO iVm § 2 Abs 1 ASGG).

**False Positives:**

- `Dr. Spenling` — partial — pred is substring of gold: `Prof. Dr. Spenling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Spenling`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Tarmann-Prentner`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Brenn`(person)
- `Dr. Christoph Kainz`(person)
- `Mag. Johann Schneller`(person)
- `Louisa Niklei, Bakk. art.`(person)
- `Orgler + Pfurtscheller, Rechtsanwälte`(organisation)
- `Gierhard Pharma GmbH`(organisation)
- `Batthyanystraße 10, 2812 Untereck, Österreich`(address)
- `Dr. Paul Delazer`(person)
- `Oberlandesgerichts Innsbruck`(organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/8ObA18_17f`) (sent_id: `deanon_260716_TRAIN/8ObA18_17f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Brenn als weitere Richter sowie die fachkundigen Laienrichter Mag. Dr. Bernhard Gruber und Harald Kohlruss in der Arbeitsrechtssache der klagenden Partei MedR Clemens Schepper, vertreten durch Freimüller/Obereder/Pilz Rechtsanwält_innen GmbH in Wien, gegen die beklagte Partei Muehleis & Klaese Technik AG, Rosentaler Weg 2k, 9811 St. Peter in Holz, Österreich, vertreten durch DLA Piper Weiss-Tessbach Rechtsanwälte GmbH in Wien, wegen Feststellung (Streitwert 282,56 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. November 2016, GZ 7 Ra 90/16f-19, mit dem das Urteil des Arbeits- und Sozialgerichts Wien vom 20. Juli 2016, GZ 33 Cga 50/16p-15, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Spenling` — partial — pred is substring of gold: `Prof. Dr. Spenling`

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

**Example 30** (doc_id: `deanon_260716_TRAIN/8ObA27_16b`) (sent_id: `deanon_260716_TRAIN/8ObA27_16b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten des Obersten Gerichtshofs Prof. Dr. Spenling als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Brenn sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner und Wolfgang Cadilek als weitere Richter in der Arbeitsrechtssache der klagenden Partei ICZK Lebensmittel GesmbH, Zur Wasserkaserne 11, 4743 Böcklarn, Österreich, vertreten durch Dr. Alexander Milavec, Rechtsanwalt in Wien, gegen die beklagte Partei Dworzak + Lüdeker Garten Gesellschaft mbH, Seeweingärten I 4, 5574 Göriach, Österreich, vertreten durch die Jirovec & Partner Rechtsanwalts GmbH in Wien, wegen 1.450 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 18. Februar 2016, GZ 8 Ra 69/15y-24, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO iVm § 2 Abs 1 ASGG).

**False Positives:**

- `Dr. Spenling` — partial — pred is substring of gold: `Prof. Dr. Spenling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Spenling`(person)
- `Dr. Tarmann-Prentner`(person)
- `Dr. Brenn`(person)
- `Mag. Dr. Rolf Gleißner`(person)
- `Wolfgang Cadilek`(person)
- `ICZK Lebensmittel GesmbH`(organisation)
- `Zur Wasserkaserne 11, 4743 Böcklarn, Österreich`(address)
- `Dr. Alexander Milavec`(person)
- `Dworzak + Lüdeker Garten Gesellschaft mbH`(organisation)
- `Seeweingärten I 4, 5574 Göriach, Österreich`(address)
- `Jirovec & Partner Rechtsanwalts GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/8ObA71_14w`) (sent_id: `deanon_260716_TRAIN/8ObA71_14w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden und durch die Hofrätin Dr. Tarmann-Prentner, den Hofrat Mag. Ziegelbauer, sowie die fachkundigen Laienrichter Mag. Andreas Mörk und Mag. Matthias Schachner als weitere Richter in der Arbeitsrechtssache der klagenden Partei Cynthia Schamel, vertreten durch Forcher-Mayr & Kantner Rechtsanwälte Partnerschaft in Innsbruck, gegen die beklagte Partei Werkglanz-Verlag AG, Blattbühel 46, 9073 Klagenfurt, Österreich, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Feststellung (Streitwert: 21.800 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 30. September 2014, GZ 15 Ra 92/14p-40, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Dr. Spenling` — partial — pred is substring of gold: `Prof. Dr. Spenling`

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

**Example 32** (doc_id: `deanon_260716_TRAIN/8ObA72_16w`) (sent_id: `deanon_260716_TRAIN/8ObA72_16w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten des Obersten Gerichtshofs Prof. Dr. Spenling als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Brenn sowie die fachkundigen Laienrichter Dr. Josef Schleinzer und ADir.

**False Positives:**

- `Dr. Spenling` — partial — pred is substring of gold: `Prof. Dr. Spenling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Prof. Dr. Spenling`(person)
- `Dr. Tarmann-Prentner`(person)
- `Dr. Brenn`(person)
- `Dr. Josef Schleinzer`(person)

</details>

---

## `Role Title Name Full` 💣

**F1:** 0.000 | **Precision:** 0.071 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1d87b1c4`  
**Description:**
Matches legal roles followed by titles (Dr., Mag., etc.) and full names, capturing the entire name string including hyphenated parts.

**Content:**
```
(?:Senatspr\u00e4sident(?:in)?|Vizepr\u00e4sident(?:in)?|Hofrat(?:in)?|Hofr\u00e4te(?:in)?|Oberlandesgerichtsrat(?:in)?|Landesgerichtsrat(?:in)?|Bezirksgerichtsrat(?:in)?|Kanzler(?:in)?|Prokurator(?:in)?|Staatsanwalt(?:in)?|Richter(?:in)?|Vorsitzender(?:in)?|Mitglied(?:in)?|Privatbeteiligter(?:in)?|Zeuge(?:in)?|Gesch\u00e4digter(?:in)?|Angeklagter(?:in)?|Opfer|Betroffener(?:in)?|Vertreter(?:in)?|Anwalt(?:in)?|Rechtsanwalt(?:in)?|Notar|Pr\u00e4sident(?:in)?)\s+(?:(?:Hon\.-Prof\.|Univ\.-Prof\.|Priv\.-Doz\.|Prof\.|MMag\.|DI\.|Ing\.|PhD\.|Dipl\.-Ing\.|Bakk\.\s+iur\.|MBA|BSc|LL\.M\.|RgR|\u00d6kR|StR|OStR|KR|AR|VetR|PD|Mag\.a|Mag\.in|MMag\.in|Dr\.|Mag\.)\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.071 | 0.000 | 0.000 | 14 | 1 | 13 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 13 | 3435 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_30`)


Die erst am 3. Oktober 2014 erfolgte Beschlusszustellung an die seinerzeitige gesetzliche Vertreterin Karin Burnat bewirkte keine Sanierung des Versäumnisses, weil infolge mittlerweile eingetretener Volljährigkeit des Beschuldigten Johannes Blaschtschak zu diesem Zeitpunkt die Mitwirkungsrechte des gesetzlichen Vertreters bereits erloschen waren (vglSchrollin WK2JGG § 38 Rz 22;

| Predicted | Gold |
|---|---|
| `Karin Burnat` | `Karin Burnat` |

**Missed by this rule (FN):**

- `Johannes Blaschtschak` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/2Ob162_23x`) (sent_id: `deanon_260716_TRAIN/2Ob162_23x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte Hon.-Prof. PD Dr. Rassi, MMag. Sloboda und Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Prof.in Romana Janaseck, vertreten durch Lirk Spielbüchler Hirtzberger Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Simone Gintautas, wegen Feststellung, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 18. Juli 2023, GZ 21 R 75/23k-7, mit dem der Beschluss des Bezirksgerichts St. Johann im Pongau vom 28. Februar 2023, GZ 305 C 9/23x-3, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof. PD Dr. Rassi`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Grohmann`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `MMag. Sloboda und Dr. Kikinger`(person)
- `Mag. Fitz`(person)
- `Prof.in Romana Janaseck`(person)
- `Lirk Spielbüchler Hirtzberger Rechtsanwälte OG`(organisation)
- `Simone Gintautas`(person)
- `Landesgerichts Salzburg`(organisation)
- `Bezirksgerichts St. Johann im Pongau`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/2Ob193_23f`) (sent_id: `deanon_260716_TRAIN/2Ob193_23f_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte Hon.-Prof. PD Dr. Rassi, MMag. Sloboda, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Denise Markstaler, vertreten durch Weber Rechtsanwälte GmbH & Co KG in Wien 1, gegen die beklagte Partei Rut Adamheit, vertreten durch BEURLE Rechtsanwälte GmbH & Co KG in Linz, wegen Herausgabe (Streitwert 1.525.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2023, GZ 2 R 87/23m-32, mit dem das Urteil des Landesgerichts Salzburg vom 5. April 2023, GZ 8 Cg 9/23a-22, aufgehoben wurde zu Recht erkannt:  Spruch

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof. PD Dr. Rassi`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 2** (doc_id: `deanon_260716_TRAIN/3Nc11_13t`) (sent_id: `deanon_260716_TRAIN/3Nc11_13t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie die Hofräte Univ.-Prof Dr. Neumayr und Dr. Jensik als weitere Richter in der Ordinationssache der Antragstellerin Mikulska Textil GmbH, Kohleck 4, 6794 Partenen, Österreich, vertreten durch Dr. Clemens Thiele, Rechtsanwalt in Salzburg, gegen die Antragsgegnerin TraunWind GmbH, Ferdinand Schaller-Weg 1, 4131 Stieberberg, Österreich, wegen Exekutionsführung nach § 355 EO, infolge Antrags gemäß § 28 JN den Beschluss gefasst:  Spruch Für die Bewilligung und die Vollziehung der beabsichtigten Unterlassungsexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Univ` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 3** (doc_id: `deanon_260716_TRAIN/3Ob139_20t`) (sent_id: `deanon_260716_TRAIN/3Ob139_20t_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der gefährdeten Partei Dr. Günter Geusau, Rechtsanwalt in Wels, als Masseverwalter über das Vermögen der Kelwald GmbH, Friedelstraße 1, 8350 Pertlstein, Österreich, gegen die Gegnerin der gefährdeten Partei Füsslin Telekom GmbH, Kaltbach 4, 8733 Hof, Österreich, vertreten durch Stock Rechtsanwälte PartnerschaftsgesellschaftmbB in Siegen, Deutschland, im Einvernehmen mit Mag. Martin Schönmair, Rechtsanwalt in Wels, wegen einstweiliger Verfügung nach § 381 Z 1 EO (265.239,60 EUR), aus Anlass des außerordentlichen Revisionsrekurses der gefährdeten Partei gegen den Beschluss des Landesgerichts Wels als Rekursgericht vom 1. Juli 2020, GZ 22 R 129/20g-12, mit dem der Beschluss des Bezirksgerichts Wels vom 3. April 2020, GZ 8 C 302/20g-2, abgeändert wurde, den Beschluss gefasst:  Spruch Aus Anlass des Revisionsrekurses der gefährdeten Partei wird der Beschluss des Rekursgerichts, mit dem über den Rekurs der Gegnerin der gefährdeten Partei meritorisch entschieden wurde, als nichtig aufgehoben, und dem Erstgericht aufgetragen, den Schriftsatz der Gegnerin der gefährdeten Partei vom 29. April 2020 (nur) als Widerspruch gegen die Einstweilige Verfügung des Erstgerichts vom 3. April 2020, GZ 8 C 302/20g-2, zu behandeln und darüber das gesetzmäßige Verfahren einzuleiten.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof. PD Dr. Rassi`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Roch`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Dr. Stefula`(person)
- `Dr. Günter Geusau`(person)
- `Kelwald GmbH`(organisation)
- `Friedelstraße 1, 8350 Pertlstein, Österreich`(address)
- `Füsslin Telekom GmbH`(organisation)
- `Kaltbach 4, 8733 Hof, Österreich`(address)
- `Stock Rechtsanwälte PartnerschaftsgesellschaftmbB`(organisation)
- `Mag. Martin Schönmair`(person)
- `Landesgerichts Wels`(organisation)
- `Bezirksgerichts Wels`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/3Ob147_20v`) (sent_id: `deanon_260716_TRAIN/3Ob147_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Glanzval Dienstleistungen GmbH, Otto-Hittmair-Platz 29, 9423 Steinberg-Hart, Österreich, vertreten durch Mag. Andreas Kleiber, Rechtsanwalt in Wien, gegen die beklagte Partei Gisela Filippovic, MBA verein Arthur Hoelle, vertreten durch Pflaum Karlberger Wiener Opetnik, Rechtsanwälte in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 22. Juli 2020, GZ 40 R 37/20t-27, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof. PD Dr. Rassi`

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

**Example 5** (doc_id: `deanon_260716_TRAIN/3Ob170_20a`) (sent_id: `deanon_260716_TRAIN/3Ob170_20a_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Familienrechtssache des Antragstellers Christina Ach, vertreten durch GKP Gabl Kogler Leitner Stöglehner Bodingbauer Rechtsanwälte OG in Linz, gegen den Antragsgegner Raul Cattarius, Bakk. rer. nat. Bakk. phil., vertreten durch Dr. Thomas Marschall, Rechtsanwalt in Wien, wegen Unterhalts, über den Revisionsrekurs des Antragsgegners gegen den Beschluss des Landesgerichts Linz als Rekursgericht vom 7. August 2020, GZ 15 R 162/20d-329, mit dem der Beschluss des Bezirksgerichts Linz vom 27. April 2020, GZ 1 Pu 20/13m-323, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Hon` — similar text (different position): `Hon.-Prof. Dr. Lovrek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Dr. Stefula`(person)
- `Christina Ach`(person)
- `Bodingbauer Rechtsanwälte OG`(organisation)
- `Raul Cattarius, Bakk. rer. nat. Bakk. phil.`(person)
- `Dr. Thomas Marschall`(person)
- `Landesgerichts Linz`(organisation)
- `Bezirksgerichts Linz`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/3Ob72_20i`) (sent_id: `deanon_260716_TRAIN/3Ob72_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Marktgemeinde James Weyand, MA, vertreten durch Dr. Nader Karl Mahdi, Rechtsanwalt in Wattens, gegen die beklagte Partei Lützeler Garten AG, Esteplatz 2, 9064 Schöpfendorf, Österreich, vertreten durch Altenweisl Wallnöfer Watschinger Zimmermann Rechtsanwälte GmbH in Innsbruck, und die auf Seiten der beklagten Partei beigetretene Nebenintervenientin Demeyer u. Köktas Analyse GmbH, Zinkendorferstraße 100, 9321 Schöttlhof, Österreich, vertreten durch Dr. Christian Girardi, LL.M., Ing. Dr. Stefan Schwärzler, Mag. Daniel Pichler, Rechtsanwälte in Innsbruck, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. März 2020, GZ 1 R 5/20z-27, womit das Urteil des Landesgerichts Innsbruck vom 14. November 2019, GZ 12 Cg 33/19m-18, teilweise bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof. PD Dr. Rassi`

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

**Example 7** (doc_id: `deanon_260716_TRAIN/4Ob142_21t`) (sent_id: `deanon_260716_TRAIN/4Ob142_21t_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Hon.-Prof. PD Dr. Rassi als Vorsitzenden und die Hofräte und Hofrätinnen Dr. Schwarzenbacher, Dr. Kodek, MMag. Matzka sowie Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei Laurence Perger, vertreten durch Viehböck Breiter Schenk & Nau Rechtsanwälte OG in Mödling, gegen die beklagte Partei EIPD Chemie ges.m.b.H., Insel 21, 4840 Diesenbach, Österreich, vertreten durch Celar Senoner Weber-Wilfert Rechtsanwälte GmbH in Wien, wegen Herausgabe eines Buchauszugs (Streitwert 4.000 EUR) und 41.049,64 EUR sA, über die außerordentliche Revision der klagenden Partei, gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Mai 2021, GZ 5 R 162/20k-66, mit dem das Urteil des Handelsgerichts Wien vom 30. September 2020, GZ 48 Cg 28/19f-59, bestätigt wurde, beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof. PD Dr. Rassi`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Dr. Schwarzenbacher`(person)
- `Dr. Kodek`(person)
- `MMag. Matzka`(person)
- `Mag. Istjan, LL.M.`(person)
- `Laurence Perger`(person)
- `Viehböck Breiter Schenk & Nau Rechtsanwälte OG`(organisation)
- `EIPD Chemie ges.m.b.H.`(organisation)
- `Insel 21, 4840 Diesenbach, Österreich`(address)
- `Weber-Wilfert Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/6Ob47_25t`) (sent_id: `deanon_260716_TRAIN/6Ob47_25t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Hofer-Zeni-Rennhofer als Vorsitzende sowie die Hofrätinnen und Hofräte Dr. Faber, Mag. Pertmayr, Dr. Weber und Mag. Nigl LL.M. als weitere Richter in der Rechtssache der klagenden Partei Kimberly Schnellhardt, vertreten durch Dr. Alexander Amann LL.M., Rechtsanwalt in Gamprin-Bendern, Liechtenstein, wider die beklagte Partei Digital Trasudwerk AG, Galles 5, 8453 Kitzelsdorf, Österreich, Deutschland, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 71.888,75 EUR sA Zug um Zug gegen die Rückstellung eines Fahrzeugs, in eventu wegen 17.972,19 EUR sA und Feststellung, im Verfahren über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Jänner 2025, GZ 11 R 7/25t-63, den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Faber` — partial — pred is substring of gold: `Dr. Faber`

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

**Example 9** (doc_id: `deanon_260716_TRAIN/7Nc6_13m`) (sent_id: `deanon_260716_TRAIN/7Nc6_13m_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Huber als Vorsitzende und die Hofrätinnen und Hofräte Dr. Hoch, Dr. Kalivoda, Mag. Dr. Wurdinger und Mag. Malesich als weitere Richter in der Arbeitsrechtssache der klagenden Partei Dr. Sabrina Dijkman, vertreten durch Dr. Clemens Gärner, Rechtsanwalt in Wien, gegen die beklagte Partei FPZE Metall AG, Jeitnerweg 110, 8773 Seiz, Österreich, vertreten durch Dr. Helmut Engelbrecht und andere Rechtsanwälte in Wien, wegen 4.868,07 EUR sA und Feststellung, über die Befangenheitsanzeige des Hofrats des Obersten Gerichtshofs Dr. Richard Hargassner im Verfahren 9 ObA 29/13z den Beschluss gefasst:  Spruch Der Hofrat des Obersten Gerichtshofs Dr. Richard Hargassner ist ausgeschlossen.

**False Positives:**

- `Hoch` — partial — pred is substring of gold: `Dr. Hoch`

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

**Example 10** (doc_id: `deanon_260716_TRAIN/7Ob110_13x`) (sent_id: `deanon_260716_TRAIN/7Ob110_13x_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Huber als Vorsitzende und die Hofrätinnen und Hofräte Dr. Hoch, Dr. Kalivoda, Mag. Dr. Wurdinger und Mag. Malesich als weitere Richter in der Rechtssache der klagenden Partei Gerdelbracht Telekom AG, KLG Gartengemeinde Adolfstor 4, 4352 Oberkalmberg, Österreich, vertreten durch Kunz Schima Wallentin Rechtsanwälte OG in Wien, gegen die beklagte Partei Mag. (FH) Franz Burgschmidt, vertreten durch Binder Grösswang Rechtsanwälte OG in Wien, wegen Erteilung von Auskünften, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. April 2013, GZ 11 R 75/13z-12, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Hoch` — partial — pred is substring of gold: `Dr. Hoch`

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

**Example 11** (doc_id: `deanon_260716_TRAIN/7Ob201_12b`) (sent_id: `deanon_260716_TRAIN/7Ob201_12b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Dr. Huber als Vorsitzende und die Hofrätinnen und Hofräte Dr. Hoch, Dr. Kalivoda, Mag. Dr. Wurdinger und Mag. Malesich als weitere Richter in der Rechtssache der klagenden Partei Bundeskammer für Arbeiter und Angestellte, 1041 Wien, Prinz-Eugen-Straße 20-22, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Sudlex Heizung AG, Weißenbachstraße 12, 9376 Lichtegg, Österreich, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Unterlassung und Urteilsveröffentlichung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 9. November 2011, GZ 2 R 203/11d-11, womit das Urteil des Handelsgerichts Wien vom 26. Juni 2011, GZ 19 Cg 49/11v-5, teilweise abgeändert wurde, beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Hoch` — partial — pred is substring of gold: `Dr. Hoch`

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

**Example 12** (doc_id: `deanon_260716_TRAIN/7Ob229_13x`) (sent_id: `deanon_260716_TRAIN/7Ob229_13x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Dr. Huber als Vorsitzende und die Hofrätinnen und Hofräte Dr. Hoch, Dr. Kalivoda, Mag. Dr. Wurdinger und Mag. Malesich als weitere Richter in der Rechtssache der klagenden Partei Kimberly Rempp, vertreten durch Dr. Peter Krassnig, Rechtsanwalt in Klagenfurt, gegen die beklagte Partei Dr. Tanja Sassenscheidt, vertreten durch Mag. Alexander Todor-Kostic, Mag. Silke Todor-Kostic, Rechtsanwälte in Velden, wegen Feststellung (in eventu Vertragsaufhebung), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 27. September 2013, GZ 5 R 79/13x-266, den Beschluss gefasst:  Spruch Der in der außerordentlichen Revision enthaltene Rekurs gegen die Verwerfung der Berufung wegen Nichtigkeit und die außerordentliche Revision werden zurückgewiesen.

**False Positives:**

- `Hoch` — partial — pred is substring of gold: `Dr. Hoch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Huber`(person)
- `Dr. Hoch`(person)
- `Dr. Kalivoda`(person)
- `Mag. Dr. Wurdinger`(person)
- `Mag. Malesich`(person)
- `Kimberly Rempp`(person)
- `Dr. Peter`(person)
- `Dr. Tanja Sassenscheidt`(person)
- `Mag. Alexander Todor-Kostic`(person)
- `Mag. Silke Todor-Kostic`(person)
- `Oberlandesgerichts Graz`(organisation)

</details>

---

## `Role Name Context` 🏆

**F1:** 0.009 | **Precision:** 0.012 | **Recall:** 0.007  

**Format:** `regex`  
**Rule ID:** `b03227e4`  
**Description:**
Matches names following specific legal roles (Zeuge, Kläger, etc.) or prepositions (von, mit, durch) that indicate a person, capturing only the name. Requires a title or specific role context to avoid false positives on nouns.

**Content:**
```
(?:(?:Zeuge|Zeugin|Kläger|Klägerin|Verteidiger|Verteidigerin|Geschädigter|Geschädigte|Opfer|Betroffener|Betroffene|Vater|Mutter|Sohn|Tochter|Ehegatte|Ehegattin|Entscheidungsträger|von|mit|durch|als|und|sowie)\s+)(?:(?:Dr\.|Mag\.|Prof\.|MMag\.|Ing\.|DI\.|PhD\.|Dipl\.-Ing\.|Bakk\.\s+iur\.|MBA|BSc|LL\.M\.)\s+)?([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+-[A-Z][a-zäöüß]+)*)\b(?=,|\.|\s+(?:und|sowie|als|von|mit|durch|in|auf|an|bei|für|nach|über|unter|ohne|neben|zwischen|gegen|um|bis|seit|während|trotz|wegen|statt|außer|neben|zwischen|gegen|um))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.012 | 0.007 | 0.009 | 2434 | 30 | 2404 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 30 | 2404 | 4145 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und die Hofräte Dr. Fellinger und Dr. Schramm als weitere Richter in der Pflegschaftssache der Minderjährigen Gerhard Lohrmann, geboren am 10. August 1983, und Veit Künneken, geboren am 31. Mai 1967, AZ 2 PS 117/09t des Bezirksgerichts Feldkirchen, infolge Vorlage zur Genehmigung der Übertragung gemäß § 111 JN an das Bezirksgericht Neunkirchen, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Übertragung der Zuständigkeit zur Besorgung dieser Pflegschaftssache an das Bezirksgericht Neunkirchen wird genehmigt.

| Predicted | Gold |
|---|---|
| `Veit Künneken` | `Veit Künneken` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Gerhard Lohrmann` (person)
- `10. August 1983` (date)
- `31. Mai 1967` (date)
- `Bezirksgerichts Feldkirchen` (organisation)
- `Bezirksgericht Neunkirchen` (organisation)
- `Bezirksgericht Neunkirchen` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Jason Langeloh, vertreten durch die Mag. Martin Rützler, Rechtsanwalt in Dornbirn, gegen die beklagte Partei, Selma Einoeder, vertreten durch Mag. Alexander Gerngross und Mag. Klaus Köck, Rechtsanwälte in Premstätten bei Graz, wegen 6.795,66 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 223 C 1313/24w des Bezirksgerichts Graz-Ost den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an das Bezirksgericht Dornbirn wird abgewiesen.

**False Positives:**

- `Vorsitzenden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Mag. Schober`(person)
- `Dr. Vollmaier`(person)
- `Jason Langeloh`(person)
- `Mag. Martin Rützler`(person)
- `Selma Einoeder`(person)
- `Mag. Alexander Gerngross`(person)
- `Mag. Klaus Köck`(person)
- `Bezirksgerichts Graz-Ost`(organisation)
- `Bezirksgericht Dornbirn`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_7`)


[2] Die Beklagte erhob Einspruch gegen den Zahlungsbefehl, bestritt das Vorliegen von Mängeln und wandte im Übrigen ein, ihr sei nie die Möglichkeit zur Verbesserung eingeräumt worden.

**False Positives:**

- `Mängeln` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_35`)


Ihr Schriftsatz mit der Stellungnahme zum Delegationsantrag enthält auch Vorbringen zur Sache und Beweisanträge und ist damit im Hauptverfahren verwertbar (RS0036025 [T5, T8, T10]).

**False Positives:**

- `Beweisanträge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Kordelia Meelis, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Fatima Tengel, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Vorsitzenden` — no gold match — likely missing annotation
- `Neumayer` — partial — pred is substring of gold: `Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Kordelia Meelis`(person)
- `Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft`(organisation)
- `Fatima Tengel`(person)
- `Mag. Ernst Michael Lang`(person)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_6`)


Die Aktiengesellschaft habe damit geworben, mit den eingezahlten Beträgen Edelmetalle zu marktüblichen Preisen zu erwerben, zu lagern und zu verwalten und habe dem Beklagten in dessen Funktion als Rechtsanwalt und öffentlicher Notar den Auftrag erteilt, jährliche Prüfberichte über den vollständigen Bestand zu erstellen.

**False Positives:**

- `Rechtsanwalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der beim Landesgericht Linz zu AZ 3 Cg 46/21a anhängigen Rechtssache der klagenden Partei Hollengk Planung GmbH, Am Steindl 3, 9873 Döbriach, Österreich, vertreten durch Huber Berchtold Rechtsanwälte OG in Wien, gegen die beklagte Partei Wind Nexheimval GmbH, Wiesbergsiedlung 4, 8341 Pöllau, Österreich, vertreten durch ScherbaumSeebacher Rechtsanwälte GmbH in Graz, wegen 188.117,55 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN folgenden Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, zur Verhandlung und Entscheidung der Rechtssache anstelle des Landesgerichts Linz das Landesgericht Korneuburg zu bestimmen, wird abgewiesen.

**False Positives:**

- `Vorsitzenden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_18`)


Mag es auch richtig sein, dass das Bauvorhaben in Klosterneuburg zu befunden sein werde, so stünden dieser einmaligen Befundaufnahme mehrere Verhandlungstermine und Zeugeneinvernahmen gegenüber.

**False Positives:**

- `Zeugeneinvernahmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Schramm als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Florens Drehkopf, LLB, geboren am 16. Dezember 1952, AZ 7 P 203/15g des Bezirksgerichts Mödling, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Mödling zurückgestellt.  Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

**False Positives:**

- `Vorsitzenden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schramm`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Fichtenau`(person)
- `Florens Drehkopf, LLB`(person)
- `16. Dezember 1952`(date)
- `Bezirksgerichts Mödling`(organisation)
- `Bezirksgericht Mödling`(organisation)
- `Bezirksgericht Mödling`(organisation)
- `Bezirksgericht Judenburg`(organisation)
- `Bezirksgerichts Judenburg`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Marlene Friss, Russische Föderation, gegen die verpflichtete Partei WestTelekom GmbH, Rehwald 11, 4723 Fronberg, Österreich, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

**False Positives:**

- `Vorsitzenden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_9`)


Die örtliche Zuständigkeit knüpft alternativ an den Wohnsitz des Verpflichteten bzw an den Sitz von Gesellschaften oder sonstigen juristischen Personen, die als Verpflichtete in Anspruch genommen werden einerseits oder an die Zuständigkeit zum Vollzug der Exekution, die aufgrund des ausländischen Exekutionstitels, dessen Vollstreckbarerklärung angestrebt wird, eingeleitet werden könnte, andererseits an.

**False Positives:**

- `Verpflichtete` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und die Hofräte Dr. Fellinger und Dr. Schramm als weitere Richter in der Pflegschaftssache der Minderjährigen Gerhard Lohrmann, geboren am 10. August 1983, und Veit Künneken, geboren am 31. Mai 1967, AZ 2 PS 117/09t des Bezirksgerichts Feldkirchen, infolge Vorlage zur Genehmigung der Übertragung gemäß § 111 JN an das Bezirksgericht Neunkirchen, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Übertragung der Zuständigkeit zur Besorgung dieser Pflegschaftssache an das Bezirksgericht Neunkirchen wird genehmigt.

**False Positives:**

- `Vorsitzenden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schinko`(person)
- `Dr. Fellinger`(person)
- `Dr. Schramm`(person)
- `Gerhard Lohrmann`(person)
- `10. August 1983`(date)
- `Veit Künneken`(person)
- `31. Mai 1967`(date)
- `Bezirksgerichts Feldkirchen`(organisation)
- `Bezirksgericht Neunkirchen`(organisation)
- `Bezirksgericht Neunkirchen`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_17`)


Sie sprechen nur dann dagegen, wenn das bisher zuständige Gericht wegen seiner bisherigen Ermittlungen und Tatsachenkenntnisse, seiner eingehenderen Vertrautheit oder seiner besonderen Sachkenntnis, aufgrund unmittelbarer Einvernahme der maßgeblichen Personen oder sonstiger trifftiger Gründe besser geeignet ist (RIS-Justiz RS0047032).

**False Positives:**

- `Tatsachenkenntnisse` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen Selma Eichler, LLM, geboren 13. September 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt. Begründung:  Rechtliche Beurteilung [1] Mit Beschluss vom 12.

**False Positives:**

- `Vorsitzenden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Nowotny`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Selma Eichler, LLM`(person)
- `13. September`(date)
- `Bezirksgerichts Graz-West`(organisation)
- `Bezirksgericht Graz-West`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Ober-Automotive GmbH, Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei Katharina Rothschadl, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Vorsitzenden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Ober-Automotive GmbH`(organisation)
- `Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich`(address)
- `Mag. Alexander Rimser`(person)
- `Katharina Rothschadl`(person)

**Example 14** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_4`)


Text Begründung: Das klagende Unternehmen mit Sitz in Österreich begehrt gegenüber der in Hongkong ansässigen beklagten Partei die Feststellung, dass zwischen den Parteien weder ein Data Transfer Agreement noch ein Collaboration Agreement abgeschlossen worden sei oder diese wirksam zustande gekommen seien.

**False Positives:**

- `Sitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_5`)


In eventu begehrte die klagende Partei die Feststellung, dass zwischen den Parteien kein Vertrag über die Weitergabe und Nutzung von Rechten, Lizenzen, Daten, Know-How, technischen Informationen und Unterlagen betreffend mikroverkapseltem Clomazone sowie über eine Zusammenarbeit hinsichtlich der Entwicklung und Produktion von mikroverkapseltem Clomazone mit belastenden Bestimmungen, wie insbesondere der Untersagung der Weitergabe der bekannten Informationen an Dritte, wirksam abgeschlossen worden sei oder bestehe, sodass der Beklagten keine wie auch immer gearteten Rechte gegenüber der Klägerin zustünden.

**False Positives:**

- `Nutzung` — no gold match — likely missing annotation
- `Rechten` — no gold match — likely missing annotation
- `Produktion` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 16** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_10`)


Die Klägerin stützte die Zuständigkeit des von ihr angerufenen Landesgerichts Wr. Neustadt als Handelsgericht auf § 88 Abs 1 und 2 JN.

**False Positives:**

- `Handelsgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_11`)


Für den Fall der örtlichen Unzuständigkeit des angerufenen Gerichts beantragte die Klägerin gemäß § 28 JN die Bestimmung des Landesgerichts Wr. Neustadt als Handelsgericht als für den gegenständlichen Rechtsstreit örtlich zuständiges Gericht.

**False Positives:**

- `Handelsgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_23`)


3.1 Auch wenn die früher vorgenommene Ausdehnung des Vertrags zwischen dem Vereinigten Königreich von Großbritannien und Nordirland und der Republik Österreich über die gegenseitige Anerkennung und Vollstreckung gerichtlicher Entscheidungen in Zivil- und Handelssachen (BGBl 1962/224) auf Hongkong (BGBl 1978/90) - seit Beendigung des Britischen Hoheitsrechts - keine Geltung mehr für Hongkong hat (BGBl III 1999/51) und zwischen Österreich und China die Gegenseitigkeit im Verhältnis beider Staaten, was die Anerkennung und Vollstreckbarkeit gerichtlicher Exekutionstitel in jeweils anderen Staaten anlangt, fehlt (vgl 3 Nc 15/14g), kann die mangelnde Vollstreckbarkeit ausländischer Entscheidungen ein besonderes Rechtsschutzbedürfnis für die Inanspruchnahme inländischer Gerichte nur dann begründen, wenn die Entscheidungen des an sich berufenen Staats in Österreich vollstreckt werden müssten (4 Nd 507/96;

**False Positives:**

- `Großbritannien` — no gold match — likely missing annotation
- `Nordirland` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 19** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin mj Dietlind Schiewick, geboren 23. Oktober 2017, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Vöcklabruck, 4840 Vöcklabruck, Sportplatzstraße 1–3), deren Mutter Gisela Akcakaya, MSc, und des Antragsgegners Ernst Hartjens, Russische Föderation, wegen Feststellung der Abstammung, aufgrund der vom Bezirksgericht Josefstadt verfügten Vorlage des Akts AZ 23 Fam 2/21y zur Entscheidung gemäß § 111 Abs 2 JN den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Villach zurückgestellt.  Text Begründung: [1] Gegenstand des Verfahrens ist der Antrag auf Feststellung der Abstammung der zum Zeitpunkt der Antragstellung am 24.

**False Positives:**

- `Vorsitzenden` — no gold match — likely missing annotation
- `Jugendhilfeträger` — no gold match — likely missing annotation
- `Gisela Akcakaya` — partial — pred is substring of gold: `Gisela Akcakaya, MSc`

> overlaps gold: 1  |  likely missing annotation: 2

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Fichtenau`(person)
- `Mag. Ziegelbauer`(person)
- `Dietlind Schiewick`(person)
- `23. Oktober`(date)
- `Bezirkshauptmannschaft Vöcklabruck`(organisation)
- `Gisela Akcakaya, MSc`(person)
- `Ernst Hartjens`(person)
- `Bezirksgericht Josefstadt`(organisation)
- `Bezirksgericht Villach`(organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie durch die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Hon.-Prof.in KzlR Iris Makowska, vertreten durch Skribe Rechtsanwaelte GmbH in Wien, gegen die beklagte Partei Dieter Apfelbacher Ltd, Am Fundbach 31w, 9170 Tratten, Österreich, wegen 400 EUR sA, über den Ordinationsantrag nach § 28 JN in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Vorsitzenden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 21** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_4`)


Text Begründung: Die Klägerin macht gegen die beklagte Partei, eine ägyptische Fluglinie, Ansprüche nach der Verordnung (EG) 261/2004 des Europäischen Parlaments und des Rates vom 11. Februar 2004 über eine gemeinsame Regelung für Ausgleichs- und Unterstützungsleistungen für Fluggäste im Fall der Nichtbeförderung und bei Annullierung oder großer Verspätung von Flügen (EU-Fluggastrechte-VO) geltend.

**False Positives:**

- `Unterstützungsleistungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_10`)


Es ist dabei auf die Kriterien der Sach- und Parteinähe sowie der Zweckmäßigkeit Bedacht zu nehmen (RS0106680 [T13]).

**False Positives:**

- `Parteinähe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Paulina Nüsken, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Oliver Eylart, Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Vorsitzenden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Paulina Nüsken`(person)
- `Skribe Rechtsanwälte GmbH`(organisation)
- `Oliver Eylart`(person)
- `Bezirksgericht Schwechat`(organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_5`)


Der in Österreich wohnhafte Kläger erhob gegen das beklagte Luftfahrtunternehmen mit Sitz im Vereinigten Königreich Klage auf Zahlung von 82,39 EUR sA aufgrund der Verordnung (EG) Nr 261/2004 des Europäischen Parlaments und des Rates vom 11. Februar 2004 über eine gemeinsame Regelung für Ausgleichs- und Unterstützungsleistungen für Fluggäste im Fall der Nichtbeförderung und bei Annullierung oder großer Verspätung von Flügen (EU-FluggastVO).

**False Positives:**

- `Unterstützungsleistungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_6`)


Sein Flug von Wien nach Bristol sei annulliert worden, weshalb er von der Beklagten die Rückerstattung der Flugscheinkosten nach Art 8 Abs 1 lit a EU-FluggastVO fordere.

**False Positives:**

- `Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_21`)


[7] 4.1 Der Oberste Gerichtshof hat Ordinationsanträgen bereits in einer Vielzahl von Entscheidungen stattgegeben, wenn der Kläger Ansprüche nach der EU-FluggastVO sonst in einem Drittstaat einklagen müsste und zwischen diesem Drittstaat und Österreich kein Vollstreckungsübereinkommen besteht (zB 6 Nc 1/19b ZVR 2019/114, 259 [Mayr];

**False Positives:**

- `Entscheidungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_24`)


[8] 4.2 Auch im Verhältnis zu dem seit 1. 1. 2021 als Drittstaat anzusehenden Vereinigten Königreich Großbritannien und Nordirland (vgl Art 126 des Abkommens über den Austritt des Vereinigten Königreichs Großbritannien und Nordirland aus der Europäischen Union und der Europäischen Atomgemeinschaft, ABl C 384 1/1 [idF: Austrittsabkommen]) liegt eine vergleichbare Situation vor: [9] 4.3 Entscheidungen eines britischen Gerichts, die in einem nach dem Ablauf des 31.

**False Positives:**

- `Drittstaat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_30`)


[10] 4.4 Nach dem Vertrag zwischen der Republik Österreich und dem Vereinigten Königreich von Großbritannien und Nordirland über die gegenseitige Anerkennung und Vollstreckung gerichtlicher Entscheidungen in Zivil- und Handelssachen, BGBl 1962/224, werden grundsätzlich nur Entscheidungen in Zivil- und Handelssachen eines „oberen Gerichts“ (Art II Abs 1 iVm Art I Z 2) nach einem (auch Fragen der Zuständigkeit umfassenden) Exequaturverfahren (Art III) anerkannt und vollstreckt.

**False Positives:**

- `Großbritannien` — no gold match — likely missing annotation
- `Nordirland` — no gold match — likely missing annotation
- `Handelssachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 29** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_37`)


Bei der Auswahl des zu bestimmenden Gerichts ist auf die Kriterien der Sach- und Parteinähe sowie der Zweckmäßigkeit Bedacht zu nehmen (RS0106680 [T13]).

**False Positives:**

- `Parteinähe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger und Hon.-Prof. Dr. Neumayr als weitere Richter in der Verlassenschaftssache nach dem am 9. September 2009 verstorbenen, zuletzt in Zum Wetterkreuz 15, 5121 Hofstadt, Österreich, wohnhaft gewesenen Manfred Johann Puff, AZ 1 A 349/09w des Bezirksgerichts Kitzbühel, über den Delegierungsantrag der Karin Ciliberto, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, den B e s c h l u s s gefasst:  Spruch Dem Delegierungsantrag wird stattgegeben.

**False Positives:**

- `Vorsitzenden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schinko`(person)
- `Dr. Fellinger`(person)
- `Hon.-Prof. Dr. Neumayr`(person)
- `Zum Wetterkreuz 15, 5121 Hofstadt, Österreich`(address)
- `Manfred Johann Puff`(person)
- `Bezirksgerichts Kitzbühel`(organisation)
- `Karin Ciliberto`(person)
- `Mag. Maximilian Kocher`(person)

**Example 31** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_8`)


Die - durch einen Notar mit Kanzleisitz in Wien vertretene - Witwe und die beiden minderjährigen Kinder des Verstorbenen, für die ein Rechtsanwalt mit Kanzleisitz in Wien als Kollisionskurator bestellt wurde, halten sich nach dem von ihnen bestätigten Antragsvorbringen ebenfalls im Sprengel des Bezirksgerichts Mödling auf.

**False Positives:**

- `Kanzleisitz` — no gold match — likely missing annotation
- `Kanzleisitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Bezirksgerichts Mödling`(organisation)

**Example 32** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Steidlen+Ysner Daten GmbH, Kaminweg 34, 8200 Laßnitzthal, Österreich, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Verlag Waldlemder GmbH, Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

**False Positives:**

- `Vorsitzenden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 33** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_6`)


Die Leistungen der beklagten Partei seien in Bezug auf Trittschallschutz-Decke und Bodenaufbau Nassräume und Technikräume mangelhaft, wodurch der klagenden Partei (in Form von Sanierungskosten und Mietzinsentgang) ein Schaden in Höhe des Klagsbetrags entstanden sei.

**False Positives:**

- `Sanierungskosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_10`)


Von zwei Ausnahmen abgesehen seien sämtliche einzuvernehmende Personen in Wien oder in der Nähe von Wien aufhältig.

**False Positives:**

- `Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_19`)


Die Parteien hätten die Einvernahme von zehn Personen beantragt, von denen lediglich zwei (der Geschäftsführer und ein Mitarbeiter der beklagten Partei) in Linz ansässig seien, die übrigen in Wien und in der Umgebung von Wien.

**False Positives:**

- `Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_47`)


Das Objekt, auf das sich der Rechtsstreit bezieht, ist in Wien gelegen, sodass auch ein Ortsaugenschein sowie die Befundaufnahme durch Sachverständige in Wien durchzuführen sind.

**False Positives:**

- `Sachverständige` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Rechtssache der klagenden Partei Mur Dorftalnex Technologien -GmbH, Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich, vertreten durch Dr. Peter Lechner und Dr. Hermann Pfurtscheller, Rechtsanwälte in Innsbruck, und ihrer Nebenintervenientin Ober Dertri GmbH, Hintereggweg 93, 2070 Kleinhöflein, Österreich, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Rudolf Ketelhut GmbH, Fiebrichgasse 17, 5120 Seeleiten, Österreich, vertreten durch Rechtsanwaltskanzlei Dr. Bernhard Hämmerle GmbH in Innsbruck, und ihrer Nebenintervenientin Völkertz Energie GmbH, Brunnbachweg 19, 4653 Mayersdorf, Österreich, vertreten durch Dr. Franz Pechmann, Rechtsanwalt in Wien, wegen 696.238,34 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck vom 2. Oktober 2009, GZ 4 R 108/09b-167, mit dem das Urteil des Landesgerichts Innsbruck vom 23. Februar 2009, GZ 41 Cg 228/01z-152, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

**False Positives:**

- `Revisionsgericht` — no gold match — likely missing annotation
- `Vorsitzenden` — no gold match — likely missing annotation
- `Rechtsanwaltskanzlei Dr` — positional overlap with gold: `Dr. Bernhard Hämmerle GmbH`

> overlaps gold: 1  |  likely missing annotation: 2

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

**Example 38** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_9`)


4. 2000 einen Architektur- und Ingenieurvertrag, in dem sich die Klägerin zu Architektur- und Ingenieurleistungen - auch zur örtlichen Bauaufsicht - im vertraglich festgelegten Umfang für das Bauvorhaben verpflichtete.

**False Positives:**

- `Ingenieurvertrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_83`)


Eine Vereinbarung, wonach die Beklagte Zahlungen wegen Gewährleistungsansprüchen nicht zurückhalten dürfe (s RIS-Justiz RS0016592), wurde nämlich weder behauptet noch festgestellt. Dass die Beklagte Vorleistungspflichtige der Vorschüsse ist, führt nicht dazu, dass sie insoweit das Preisminderungsrecht nicht mit Einrede, sondern mit Klage geltend machen müsste, macht doch das Gesetz die Geltendmachung von Gewährleistungsrechten nicht von der Erfüllung der eigenen Verbindlichkeit abhängig.

**False Positives:**

- `Einrede` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_85`)


Da das Berufungsgericht zu Unrecht die Entscheidungsreife eines Teils des Klagebegehrens bejahte, war in Stattgebung der Revision das Teilurteil aufzuheben und mit Zurückverweisung an das Erstgericht vorzugehen.

**False Positives:**

- `Zurückverweisung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Schneidergruberweg 37, 5132 Reith, Österreich, vertreten durch Dr. Alois Schneider, Rechtsanwalt in Rattenberg, wider die beklagte Partei Dario von Ebers, vertreten durch Dr. Walter Hausberger, Dr. Katharina Moritz und Dr. Alfred Schmidt, Rechtsanwälte in Wörgl, wegen Entfernung und Unterlassung (Revisionsinteresse 10.000 EUR), infolge Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 3. November 2017, GZ 3 R 172/17s-22, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Rattenberg vom 17. Mai 2017, GZ 3 C 401/15k-18, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Revisionsgericht` — no gold match — likely missing annotation
- `Vorsitzenden` — no gold match — likely missing annotation
- `Ebers` — partial — pred is substring of gold: `Dario von Ebers`

> overlaps gold: 1  |  likely missing annotation: 2

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Stefula`(person)
- `Schneidergruberweg 37, 5132 Reith, Österreich`(address)
- `Dr. Alois Schneider`(person)
- `Dario von Ebers`(person)
- `Dr. Walter Hausberger`(person)
- `Dr. Katharina Moritz`(person)
- `Dr. Alfred Schmidt`(person)
- `Landesgerichts Innsbruck`(organisation)
- `Bezirksgerichts Rattenberg`(organisation)

**Example 42** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_10`)


Die Klägerin begehrt, der Beklagte möge zwei Obstbäume (des Altbestands) entfernen sowie Eigentumseingriffe durch Anpflanzen von Obstbäumen auf ihren (näher bezeichneten) Grundstücken unterlassen und die von ihm im Jahr 2015 dort neu gepflanzten Bäume entfernen.

**False Positives:**

- `Eigentumseingriffe` — no gold match — likely missing annotation
- `Anpflanzen` — no gold match — likely missing annotation
- `Obstbäumen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 43** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_24`)


Im Zuge mehrfacher Grundstücksteilungen bzw Ab- und Zuschreibungen in den Jahren 1958 und 2010 wurde diese Eintragung nicht deckungsgleich auf die abgeschriebenen Grundstücke ausgedehnt.

**False Positives:**

- `Zuschreibungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_65`)


1.2 Als reichsrechtliches Begleitgesetz zur Grundbuchseinführung in Tirol wurde daher das „Gesetz vom 17. März 1897, womit für den Fall der Einführung der Grundbücher in Tirol einige grundbuchsrechtliche Sonderbestimmungen und erleichternde Gebürenvorschriften erlassen und Beschränkungen der Theilung von Gebäuden nach materiellen Antheilen eingeführt werden (Wirksam für die gefürstete Grafschaft Tirol)“ erlassen und unter RGBl 1897/77 kundgemacht („Tiroler Grundbuchsanlegungsreichsgesetz“ [TirGARG] in Abgrenzung zum parallel beschlossenen landesrechtlichen „Tiroler Grundbuchsanlegungsgesetz“, GVBlTirVbg 1897/9).

**False Positives:**

- `Gebäuden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_66`)


1.3 Das Baumeigentum ist in den (seither unveränderten) Artikeln III bis V TirGARG geregelt:  Artikel III. Rechtsverhältnisse, die vor dem Beginne der Wirksamkeit dieses Gesetzes in Ansehung von Bäumen derart begründet wurden, daß letztere abgesondert vom Grund und Boden als selbständige Vermögensobjecte sich darstellen, werden durch dieses Gesetz nicht berührt.

**False Positives:**

- `Boden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_68`)


Hingegen können nach dem Inkrafttreten des gegenwärtigen Gesetzes Rechtsverhältnisse dieser Art in Ansehung von Bäumen, welche unter die vorstehenden Bestimmungen nicht fallen, nicht neu begründet werden.

**False Positives:**

- `Bäumen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_85`)


Zur Vermeidung von Zweifeln über die Erwerbungsart „hinsichtlich der vom Grundbuche ausgeschlossenen Bäume“ wurde eine Bestimmung über die künftige Erwerbungsart getroffen (Artikel IV Abs. 2).

**False Positives:**

- `Zweifeln` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_90`)


2. Im Schrifttum wird zu § 295 ABGB (Unbeweglichkeit von Pflanzen) und zu § 420 ABGB (Eigentumserwerb durch Pflanzen und Säen) ohne weitere Ausführungen oder Fundstellen auf die Sonderrechte an Bäumen in Tirol hingewiesen (HolznerinRummel/Lukas, ABGB4§ 295 Rz 1;KarnerinRummel/Lukas, ABGB4§ 420 Rz 2;HelmichinKletečka/Schauer, ABGB-ON1.03§ 295 Rz 6;MaderinKletečka/Schauer, ABGB-ON1.03§ 420 Rz 1;HofmanninSchwimann/Kodek, ABGB Praxiskommentar4§ 295 Rz 2;Klicka/ReidingerinSchwimann/Kodek, ABGB-Praxiskommentar4§ 420 Rz 2;KodekinSchwimann/Neumayr, ABGB-Taschenkommentar4§ 295 Rz 1;KisslingerinFenyves/Kerschner/Vonkilch,Klang3§ 295 Rz 6;KlanginKlang, Kommentar zum ABGB² § 295 Rz 1;KlanginKlang, Kommentar zum ABGB² § 420 Rz 2).

**False Positives:**

- `Pflanzen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_92`)


3. Zur grundbuchsrechtlichen Behandlung ist auf § 20 lit b GBG zu verweisen, wonach„zur Begründung bestimmter, nach den Vorschriften dieses oder eines anderen Gesetzes damit verbundener Rechtswirkungen, wie zum Beispiel die Anmerkung der Rangordnung, der Abschreibung von Grundstücken, der Simultanhaftung, der Aufkündigung einer Hypothekarforderung, der Streitanhängigkeit, der Zwangsverwaltung, der Erteilung des Zuschlages“ grundbücherliche Anmerkungen erfolgen können.

**False Positives:**

- `Grundstücken` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_104`)


Im Fall einer irrtümlichen Nichtübertragung der Anmerkung wäre allenfalls ein gutgläubiger Erwerb von Eigentum an den Bäumen durch den Erwerber einer Liegenschaft denkbar, worauf es aber keine Hinweise in den Feststellungen gibt.

**False Positives:**

- `Eigentum` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_117`)


Bereits das Berufungsgericht hat darauf hingewiesen, dass – selbst wenn man nicht von einer Verjährung der Rechte aus der Vereinbarung 1977 ausgehen wollte – lediglich ein Anspruch auf Ablöse der Bäume bestünde, somit ein Anspruch auf Eigentumsverschaffung, nicht aber auf die in Punkt 1 des Klagebegehrens geforderte „Entfernung“ von Bäumen.

**False Positives:**

- `Bäumen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Bartholomäus Junghahn, geboren am 8. Mai 1999, und der minderjährigen HR Sophie Elefteriadis, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Vorsitzenden` — no gold match — likely missing annotation
- `Familie Rechtsvertretung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Bartholomäus Junghahn`(person)
- `HR Sophie Elefteriadis`(person)
- `Magistrat der Stadt Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Favoriten`(organisation)

**Example 53** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_12`)


Am 26. 2. 2010 beantragten die beiden Minderjährigen, vertreten durch den Jugendwohlfahrtsträger, (neuerlich) die Gewährung von Unterhaltsvorschüssen in Titelhöhe gemäß den §§ 3, 4 Z 1 UVG.

**False Positives:**

- `Unterhaltsvorschüssen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Eva Abdelrahman, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei Hochenadel Immobilien GmbH, Ritterhof 11, 2661 Graben, Österreich, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Revisionsgericht` — no gold match — likely missing annotation
- `Vorsitzenden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

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

**Example 55** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Juri Gerstl GmbH, Mutten 18, 3251 Schauboden, Österreich, vertreten durch Dr. Ralph Trischler, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, sowie die Nebenintervenientin auf Seiten der beklagten Partei Bundesbeschaffung GmbH, 1020 Wien, Lassallestraße 9b, vertreten durch die Olischar Rechtsanwaltsgesellschaft mbH in Wien, wegen 15.535 EUR sA, über den Revisionsrekurs der klagenden Partei (Revisionsinteresse: 7.460 EUR), gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 23. Februar 2023, GZ 16 R 168/22a-20, mit welchem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 5. September 2022, GZ 11 Cg 48/22t-12, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Vorsitzende` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 56** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_8`)


Die von der Nebenintervenientin vertretene Beklagte führte zu GZ 4805.03467 ein Vergabeverfahren zum Ankauf von Hygienepapier durch, das am 16.

**False Positives:**

- `Hygienepapier` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_40`)


Darüber hinaus werden dadurch potentielle Widersprüchlichkeiten vermieden, die sich aus divergierenden Rechtsansichten von Vergabekontrollbehörden und Zivilgerichten ergeben können (KurzinHeid/Reisner/Deutschmann/Hofbauer, BVergG 2018 [2019] § 373 Rz 5;Pesendorfer/Rief, Schadenersatz bei rechtmäßigem Widerruf?

**False Positives:**

- `Vergabekontrollbehörden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Leander Lindlahr, geboren am 1. August 2011, und des mj Yussuf Prussog, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Vorsitzenden` — no gold match — likely missing annotation
- `Familie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Leander Lindlahr`(person)
- `Yussuf Prussog`(person)
- `Magistrat der Stadt Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Bezirksgerichts Donaustadt`(organisation)

**Example 59** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_20`)


Das Rekursgericht sprach aus, dass der ordentliche Revisionsrekurs gegen seine Entscheidung zulässig sei, weil noch keine Rechtsprechung des Obersten Gerichtshofs zum Wegfall der Exportverpflichtung bei Gewährung von Unterhaltsvorschüssen nach § 4 Z 3 UVG vorliege.

**False Positives:**

- `Unterhaltsvorschüssen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)

**Example 60** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_48`)


Außerdem bezweckt der in Art 7 der VO (EWG) 1612/68 verankerte Gleichbehandlungsgrundsatz nach ständiger Rechtsprechung, die Diskriminierung von Kindern, denen der Arbeitnehmer Unterhalt gewährt, zu verhindern (M. Windisch-Graetz, Neuerungen im Europäischen koordinierten Sozialrecht, DRdA 2011, 219 ff [221];Felten/Neumayr, Die neue Wanderarbeitnehmerverordnung und Unterhaltsvorschuss, iFamZ 2010, 164 ff [167] mit Nachweisen aus der Rechtsprechung).

**False Positives:**

- `Kindern` — no gold match — likely missing annotation
- `Unterhaltsvorschuss` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 61** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_54`)


Für eine Mutter mit Wohnsitz in einem anderen Mitgliedstaat, die in Österreich einer unselbständigen Erwerbstätigkeit nachgeht und somit in den persönlichen Anwendungsbereich der VO (EWG) 1612/68 bzw nunmehr der VO (EU) 492/2011 fällt, stellt nämlich der Empfang von Unterhaltsvorschüssen zweifelsfrei eine soziale Vergünstigung dar, da auf diese Weise ihr Beitrag am Aufkommen für den Unterhalt des Kindes verringert wird (Felten/NeumayraaO iFamZ 2010, 169 mwN).

**False Positives:**

- `Wohnsitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_69`)


Dennoch ist in diesem Zusammenhang festzuhalten, dass der EuGH der Verwirklichung von Allgemeininteressen durch ausschließliche Anknüpfung an einen Wohnsitz im Inland sehr kritisch gegenübersteht.

**False Positives:**

- `Allgemeininteressen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_71`)


Der EuGH hat daher einen Exportanspruch von Familienleistungen über die VO (EU) 492/2011 verneint, wenn zu dem zuständigen Staat keine hinreichend enge Bindung besteht, zB weil die betreffende Person dort lediglich eine geringfügige Beschäftigung ausübt (vglFelten/NeumayraaO iFamZ 2010, 169 mwN).

**False Positives:**

- `Familienleistungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des minderjährigen Cedric Annamüller, geboren am 8. März 2007, 16. Mai 1964, vertreten durch das Land Kärnten als Kinder- und Jugendhilfeträger (Magistrat der Landeshauptstadt Klagenfurt, Abteilung für Jugend und Familie, Bahnhofstraße 35, 9010 Klagenfurt am Wörthersee), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Graz, gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 8. Jänner 2016, GZ 4 R 283/15g-16, womit der Beschluss des Bezirksgerichts Klagenfurt vom 17. November 2015, GZ 1 Pu 69/10x-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Vorsitzenden` — no gold match — likely missing annotation
- `Familie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Mag. Ziegelbauer`(person)
- `Cedric Annamüller`(person)
- `8. März`(date)
- `16. Mai 1964`(date)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts Klagenfurt`(organisation)
- `Bezirksgerichts Klagenfurt`(organisation)

**Example 65** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_9`)


Der Minderjährige sei georgischer Staatsbürger und Konventionsflüchtling.

**False Positives:**

- `Konventionsflüchtling` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_13`)


Mit dem angefochtenen Beschluss gab das Rekursgericht dem Rekurs des Bundes nicht Folge und sprach aus, dass der ordentliche Revisionsrekurs zulässig sei, weil Rechtsprechung des Obersten Gerichtshofs zur Frage fehle, inwiefern das Erstgericht bei der Weitergewährung von Unterhaltsvorschüssen von Amts wegen zu prüfen habe, ob dem Minderjährigen nach wie vor die Flüchtlingseigenschaft zukomme.

**False Positives:**

- `Unterhaltsvorschüssen` — no gold match — likely missing annotation
- `Amts` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)

**Example 67** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_25`)


Der Rechtsansicht des Rekursgerichts sei entgegenzuhalten, dass im Fall eines Weitergewährungsantrags nach § 4 Z 2 UVG die vorhergehende Unterlassung zumutbarer (und nicht von vornherein aussichtsloser) Versuche zur Schaffung eines Unterhaltstitels ebenfalls einen von Amts wegen wahrzunehmenden Grund für die Nichtweitergewährung des Vorschusses darstelle.

**False Positives:**

- `Amts` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludmilla von Amelunxen, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, gegen die beklagte Partei Svetlana Leinhäuser, vertreten durch Dr. Thomas Brückl, Mag. Christian Breit, Rechtsanwälte in Ried im Innkreis, wegen 1.778,52 EUR und Unterlassung (Streitwert 2.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Wels als Berufungsgericht vom 25. Jänner 2023, GZ 21 R 2/23b-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Grieskirchen vom 27. Oktober 2022, GZ 3 C 642/20h-27, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Rekursgericht` — no gold match — likely missing annotation
- `Vorsitzende` — no gold match — likely missing annotation
- `Amelunxen` — partial — pred is substring of gold: `Ludmilla von Amelunxen`

> overlaps gold: 1  |  likely missing annotation: 2

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Mag. Schober`(person)
- `Dr. Annerl`(person)
- `Ludmilla von Amelunxen`(person)
- `Dr. Bernhard Birek`(person)
- `Svetlana Leinhäuser`(person)
- `Dr. Thomas Brückl`(person)
- `Mag. Christian Breit`(person)
- `Landesgerichts Wels`(organisation)
- `Bezirksgerichts Grieskirchen`(organisation)

**Example 69** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_10`)


[3] Durch das Versagen von Bäumen auf der Liegenschaft des Beklagten wurden 45 Jungbäume der Klägerin beschädigt.

**False Positives:**

- `Bäumen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_12`)


[4] DieKlägerinbegehrte vom Beklagten Ersatz für die beschädigten Jungbäume und für die geleisteten Arbeitsstunden von insgesamt (zuletzt) 1.778,52 EUR sowie die Unterlassung von Störungen der Nutzung ihrer Liegenschaft durch umstürzende und auf ihre Liegenschaft fallende Bäume, die durch Wurzelfäule und Krankheit ihre Standfestigkeit verloren hätten.

**False Positives:**

- `Wurzelfäule` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_13`)


Bereits seit 2014 würden immer wieder Bäume vom Grundstück des Beklagten wegen mangelnder Pflege und Fürsorge auf das Grundstück der Klägerin stürzen.

**False Positives:**

- `Fürsorge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_22`)


Ein allfälliges Stürzen der Bäume sei auf ein Eschensterben zurückzuführen, nicht jedoch auf seine mangelnde Pflege und Fürsorge.

**False Positives:**

- `Fürsorge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_35`)


[7] DasBerufungsgerichtgab der gegen die Abweisung der Klagebegehren erhobenen Berufung der Klägerin Folge, hob das Ersturteil auf und verwies die Rechtssache in diesem Umfang zur neuerlichen Entscheidung nach allfälliger Verfahrensergänzung an das Erstgericht zurück.

**False Positives:**

- `Folge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_37`)


Als Haftungsgrundlage komme auch § 1319 ABGB nicht in Betracht, weil im Anwendungsbereich des Forstgesetzes die Haftungsbeschränkung nach § 176 ForstG der Anwendung des § 1319 ABGB vorgehe und den Halter von Bäumen in einem Wald iSd § 1a ForstG entlaste.

**False Positives:**

- `Bäumen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_80`)


Anderes gilt, wenn Treu und Glauben mit Rücksicht auf die Verkehrssitte eine Tätigkeit fordern (RS0037753).

**False Positives:**

- `Glauben` — no gold match — likely missing annotation
- `Rücksicht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 76** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_95`)


In einem solchen Fall kann der Oberste Gerichtshof durch Urteil in der Sache selbst erkennen (§ 519 Abs 2 Satz 3 ZPO), sodass der Beschluss des Berufungsgerichts aufzuheben und die klageabweisende Entscheidung des Erstgerichts wiederherzustellen war.

**False Positives:**

- `Urteil` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)

**Example 77** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Mag. Kevin Maassen, vertreten durch Dr. Clemens Lintschinger, Rechtsanwalt in Wien, gegen die beklagte Partei Hon.-Prof. Friedhelm Adde, vertreten durch Mag. Dr. Georg Backhausen, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 27. Jänner 2016, GZ 38 R 265/15z-45, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Revisionsgericht` — no gold match — likely missing annotation
- `Vorsitzenden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Fellinger`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Mag. Ziegelbauer`(person)
- `Mag. Kevin Maassen`(person)
- `Dr. Clemens Lintschinger`(person)
- `Hon.-Prof. Friedhelm Adde`(person)
- `Mag. Dr. Georg Backhausen`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 78** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_20`)


Dieser Fall liegt hier aber nach den den Obersten Gerichtshof bindenden Feststellungen nicht vor, weil der Beklagte - entgegen den Ausführungen des Revisionswerbers - die aufgekündigte Wohnungnichtregelmäßig zu Wohnzwecken verwendet, sondern lediglich sporadisch, als Absteigequartier.

**False Positives:**

- `Absteigequartier` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Obersten Gerichtshof`(organisation)

**Example 79** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden, die Hofräte Mag. Schober, Dr. Annerl und Dr. Vollmaier sowie die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Ing. Mag. Pamela Gotterbauer, vertreten durch Mag. Helwig Schuster, Rechtsanwalt in Melk, gegen die beklagten Parteien 1.

**False Positives:**

- `Revisionsgericht` — no gold match — likely missing annotation
- `Vorsitzenden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Mag. Schober`(person)
- `Dr. Annerl`(person)
- `Dr. Vollmaier`(person)
- `Dr. Wallner-Friedl`(person)
- `Ing. Mag. Pamela Gotterbauer`(person)
- `Mag. Helwig Schuster`(person)

**Example 80** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_27`)


Vereinbart wurde die Prüfung des Bodens durch Experten.

**False Positives:**

- `Experten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_30`)


[4] Nach Beiziehung eines vom Kläger organisierten Reitplatzexperten sanierten die Beklagten den Hallenboden durch Beifügung von Holzfasern.

**False Positives:**

- `Beifügung` — no gold match — likely missing annotation
- `Holzfasern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 82** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_41`)


[7] Am 13. 2. 2022 endete die Einstellung von Liso und Fio, den letzten beiden im Reitstall der Beklagten verbliebenen Pferde des Klägers und seiner Lebensgefährtin.

**False Positives:**

- `Liso` — no gold match — likely missing annotation
- `Fio` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 83** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_42`)


[8] Mit Aufforderungsschreiben vom 10. 3. 2022 begehrten der Kläger und seine Lebensgefährtin wegen massiver Missstände (nicht fachgerecht erneuerter Hallenboden, keine regelmäßige Planierung und Bewässerung der Böden, im Ergebnis nicht reitbarer Bodenbelag, unzureichende[s] bis schadhafte[s] Einstreu und Futter, nicht fachgerechte Einzäunung, schadhafte Schrittmaschine, zu kleine Boxengrößen) von den Beklagten einen Minderungsbetrag von gesamt 12.750 EUR.

**False Positives:**

- `Futter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_99`)


Der Kläger wendet sich in seinem Rechtsmittelvortrag im Kern gegen die berufungsgerichtliche Qualifikation des Pferdeeinstellungsvertrags als gemischter Vertrag mit Elementen eines Bestand- und Verwahrungsvertrags sowie die daraus abgeleitete Konsequenz, wonach – entsprechend der zum Mietzinsminderungsrecht des Bestandnehmers nach § 1096 ABGB entwickelten Judikatur – in der vorbehaltlosen Entgeltzahlung über den gesamten Vertragszeitraum hinweg ein konkludenter Verzicht auf Entgeltminderungsansprüche wegen Schlechtleistung liege.

**False Positives:**

- `Verwahrungsvertrags` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_260716_TRAIN/10Ob18_13i`) (sent_id: `deanon_260716_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei SüdSanitär Gruppe GmbH, Rinzendorf 28, 4501 Lindach, Österreich, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Revisionsgericht` — no gold match — likely missing annotation
- `Vorsitzenden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

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

**Example 86** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Ralph Prusseit, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Akbayrak Metall GmbH, Schroateck 57, 4710 Niederweng, Österreich, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Vorsitzenden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 87** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_30`)


PDOR Analyse hat den Netzkunden schriftlich und zeitnah über den Einbau eines intelligenten Messgerätes und die damit verbundenen Rahmenbedingungen, insbesondere im Hinblick auf Datenschutz sowie Bereitstellung und Übermittlung der Informationen gemäß §§ 81a bis 84a ElWOG 2010 zu informieren.[…] Mantze Forschung hat den Wunsch eines Netzkunden, kein intelligentes Messgerät zu erhalten, zu berücksichtigen.[…] 5. Will der Netzkunde Messeinrichtungen selbst beistellen, hat er diesen Wunsch Nord Bercon Holding zeitgerecht mitzuteilen.

**False Positives:**

- `Bereitstellung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `PDOR Analyse`(organisation)
- `Mantze Forschung`(organisation)
- `Nord Bercon Holding`(organisation)

**Example 88** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_50`)


Eine Nacheichung oder Installation von Messgeräten, die keine Smart Meter seien, wäre eine Zuwiderhandlung gegen § 83 Abs 1 ElWOG iVm der IME-VO und gemäß § 99 Abs 2 Z 14 ElWOG mit einer Geldstrafe von bis zu 75.000 EUR bedroht.

**False Positives:**

- `Messgeräten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_69`)


[14]2.§ 381 Z 2 EO ermöglicht die Erlassung einstweiliger Verfügungen zur Sicherung anderer Ansprüche als Geldansprüche, wenn solche Verfügungen zur Verhütung drohender Gewalt oder zur Abwendung eines drohenden unwiederbringlichen Schadens nötig erscheinen.

**False Positives:**

- `Geldansprüche` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 90** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_89`)


§ 18 Z 2 lit b MEG ermächtigt die Bundesministerin oder den Bundesminister für Arbeit und Wirtschaft, durch Verordnung die gemäß § 15 MEG bestehende Nacheichfrist hinsichtlich bestimmter Messgeräte um jeweils höchstens fünf Jahre zu verlängern, wenn durch Prüfungen von Teilmengen der in einem bestimmten Jahr geeichten Messgeräte nach festzulegenden allgemein anerkannten statistischen Verfahren zu erwarten ist, dass die Richtigkeit und Zuverlässigkeit dieser Messgeräte für diesen Zeitraum gewährleistet ist.

**False Positives:**

- `Wirtschaft` — no gold match — likely missing annotation
- `Prüfungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 91** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_90`)


§ 1 der aufgrund dieser Ermächtigung ergangenen Verordnung der Bundesministerin für Digitalisierung und Wirtschaftsstandort über die Verlängerung der Nacheichfrist für Elektrizitätszähler und elektrische Tarifgeräte regelt eine solche Verlängerung der Nacheichfrist um jeweils fünf Jahre für die in § 15 Z 7 lit b und c sowie Z 10 MEG angeführten Elektrizitätszähler, wenn deren Richtigkeit vor Ablauf der Gültigkeit der Eichung durch eine Stichprobenprüfung nachgewiesen worden ist.

**False Positives:**

- `Wirtschaftsstandort` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 92** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_107`)


[26]7.2.Im Ergebnis trifft der Antragsteller mit seinem Verhalten daher (bloß) die Entscheidung, welche Art von Messeinrichtung bei ihm zum Einsatz kommen soll.

**False Positives:**

- `Messeinrichtung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_110`)


Selbst wenn man mit der Antragsgegnerin davon ausginge, dass diese vom Antragsteller erhobenen Bedenken gegen den Einbau eines Smart Meters nicht zutreffen und der Antragsteller den Einbau somit zu dulden hätte, läge nämlich eine Vertragsverletzung vor, der durch die Inanspruchnahme gerichtlicher Hilfe begegnet werden könnte und es wäre auch dann nicht ersichtlich, warum der Antragsgegnerin eine Verbrauchsmessung und Abrechnung in einer vom Antragsteller gewünschten Form nicht zumindest vorübergehend – bis zur Klärung, ob den Antragsteller die von ihr behauptete Duldungspflicht trifft – zumutbar (oder warum ihr dies weniger zumutbar als dem Antragsteller die Stromabschaltung und Auflösung des Netzzugangsvertrags) sein sollte.

**False Positives:**

- `Abrechnung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 94** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Heimcon Software GmbH, H - Am Hang 3, 4912 Rettenbrunn, Österreich, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, gegen die beklagte Partei Gunter Landwirtschaft GmbH, Schlossfeld 38, 9300 Graßdorf, Österreich, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, wegen 7.731,06 EUR und Feststellung (Streitwert 20.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse insgesamt 11.597,42 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 216/14h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Revisionsgericht` — no gold match — likely missing annotation
- `Vorsitzenden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

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

**Example 95** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_4`)


Text Begründung: Die Klägerin betreibt ein Säge- und Hobelwerk und stellt Bauholz her.

**False Positives:**

- `Hobelwerk` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 96** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_12`)


2011 wurden in einem der Hochseilparks erstmals Mängel an der Verleimung der Lärchenhölzer festgestellt. Schließlich begannen bei sämtlichen Bauprojekten sich die Verleimungskanten voneinander zu lösen.

**False Positives:**

- `Mängel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 97** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_26`)


Weiters habe sie der Klägerin Zinsen und Prozesskosten, zu deren Zahlung sie im Verfahren vor dem Bezirksgericht Bezirksgericht Hall (in Tirol) verurteilt worden war, sowie die Kosten deren eigener Vertretung in diesem Verfahren zu ersetzen.

**False Positives:**

- `Prozesskosten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Hall (in Tirol)`(organisation)

**Example 98** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_34`)


1.1 Der Werkunternehmer ist regelmäßig als Sachverständiger anzusehen (§ 1299 ABGB), sodass er einem objektiven Sorgfaltsmaßstab unterliegt und die üblichen Branchenkenntnisse zu vertreten hat.

**False Positives:**

- `Sachverständiger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 99** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_46`)


Während nämlich die Beklagte Leimbinder aller Art und Formate produziert, betreibt die Klägerin ein Säge- und Hobelwerk und stellt im Rahmen ihres Geschäftsbetriebs Bauholz für verschiedene Verwendungsmöglichkeiten her.

**False Positives:**

- `Hobelwerk` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Complaint Case Context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2a43aa87`  
**Description:**
Matches persons mentioned immediately after 'in der Beschwerdesache' (in the complaint case).

**Content:**
```
in\s+der\s+Beschwerdesache\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Deceased Person Context` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9b46a3d5`  
**Description:**
Matches persons identified as deceased (verstorbenen) in inheritance contexts.

**Content:**
```
verstorbenen\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 2 | 3922 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_15`)


Eine neuerliche Begutachtung durch den zwischenzeitlich verstorbenen Sachverständigen sei unmöglich.

**False Positives:**

- `Sachverst` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/2Ob162_23x`) (sent_id: `deanon_260716_TRAIN/2Ob162_23x_7`)


Text Begründung: [1] Beim Bezirksgericht St. Johann im Pongau ist zu AZ 455 A 78/22f das Verlassenschaftsverfahren nach dem 2022 verstorbenen Erblasser anhängig.

**False Positives:**

- `Erblasser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht St. Johann im Pongau`(organisation)

</details>

---

## `Dr Name List` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a6c1e32e`  
**Description:**
Matches Dr. Name patterns in lists or after roles, ensuring full names including hyphenated parts are captured.

**Content:**
```
(?:(?:Senatspräsident(?:in)?|Vizepräsident(?:in)?|Hofrat(?:in)?|Hofräte(?:in)?|Oberlandesgerichtsrat(?:in)?|Landesgerichtsrat(?:in)?|Bezirksgerichtsrat(?:in)?|Kanzler(?:in)?|Prokurator(?:in)?|Staatsanwalt(?:in)?|Richter(?:in)?|Vorsitzender(?:in)?|Mitglied(?:in)?|Privatbeteiligter(?:in)?|Zeuge(?:in)?|Geschädigter(?:in)?|Angeklagter(?:in)?|Verurteilter(?:in)?|Opfer|Betroffener(?:in)?|Vertreter(?:in)?|Anwalt(?:in)?|Rechtsanwalt(?:in)?|Notar|OStR|StR|KR|AR|OMedR|HR|VetR|Ing\.|DI\.|PhD\.|Dipl\.-Ing\.|Bakk\. iur\.|MBA|BSc|LL\.M\.)\s+)?(?:,\s*|\s+und\s+|(?<=\s))(Dr\.[\s]+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+-[A-Z][a-zäöüß]+)*))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 24 | 0 | 24 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 24 | 3663 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_3`)


Kopf Der Oberste Gerichtshof hat am 18. März 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski im Verfahren zur Unterbringung des Mag. Herwig Bäseke in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB, AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz gemäß § 62 Abs 1 zweiter Satz OGH-Geo 2019 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger sowie Mag. Fürnkranz sind von der Entscheidung über die Anträge des Mag. Herwig Berto auf Erneuerung des Strafverfahrens AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, ausgeschlossen.

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Oshidari`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Herwig Bäseke`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Fürnkranz`(person)
- `OGH`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Fürnkranz`(person)
- `Mag. Herwig Berto`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_4`)


An ihre Stelle treten Senatspräsident des Obersten Gerichtshofs Dr. Solé sowie Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Setz-Hummel.

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Dr. Setz-Hummel`(person)

**Example 2** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_12`)


Senatspräsident des Obersten Gerichtshofs Dr. Solé sowie Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Setz-Hummel treten aufgrund der laufenden Vertretungsregelung der Geschäftsverteilung des Obersten Gerichtshofs an deren Stelle (§ 45 Abs 2 StPO).

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Dr. Setz-Hummel`(person)
- `Obersten Gerichtshofs`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_3`)


Kopf Der Oberste Gerichtshof hat am 9. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Brenner und Dr. Setz-Hummel in der Strafsache gegen Ahmed Koehnen wegen des Verbrechens des Mordes nach § 75 StGB, AZ 606 Hv 1/11m des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit der Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Brenner`(person)
- `Dr. Setz-Hummel`(person)
- `Ahmed Koehnen`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `OGH`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_3`)


Kopf Der Oberste Gerichtshof hat am 12. September 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart der Richteramtsanwärterin Mag. Ruckendorfer als Schriftführerin in der Strafsache gegen Thomas Leutz wegen des Verbrechens des gewerbsmäßigen schweren Betrugs nach §§ 146, 147 Abs 1 Z 1, Abs 3, 148 zweiter Fall, 15 StGB und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 13. September 2018, GZ 35 Hv 46/18m-130, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Oshidari`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Dr. Brenner`(person)
- `Dr. Setz-Hummel`(person)
- `Mag. Ruckendorfer`(person)
- `Thomas Leutz`(person)
- `Landesgerichts Innsbruck`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2020 durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé und durch die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Viktor Marschmeyer und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 3 zweiter Fall StGB, AZ 352 HR 214/11x des Landesgerichts für Strafsachen Wien, über den Antrag des Dr. Stefan Toepfl auf Erneuerung des Strafverfahrens gemäß § 363a StPO in Ansehung des Beschlusses des Oberlandesgerichts Wien vom 28. August 2018, AZ 20 Bs 199/18p, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Oshidari`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Dr. Brenner`(person)
- `Dr. Setz-Hummel`(person)
- `Mag. Hauer`(person)
- `Viktor Marschmeyer`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Dr. Stefan Toepfl`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/2Ob175_21f`) (sent_id: `deanon_260716_TRAIN/2Ob175_21f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätin Dr. Solé und die Hofräte Dr. Nowotny und MMag. Sloboda als weitere Richter in der Rechtssache der klagenden Partei Roxana Eisenhoefer, vertreten durch Mag. Axel Bauer, Rechtsanwalt in Wien, gegen die beklagte Partei Magdalena Wosniak, vertreten durch Dr. Manfred Sommerbauer ua, Rechtsanwälte in Wiener Neustadt, wegen 44.903,84 EUR sA, über die Revision der beklagten Partei gegen das Zwischenurteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. Juni 2021, GZ 11 R 79/21z-66, womit das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. März 2021, GZ 5 Cg 105/19a-50 in der Fassung des Berichtigungsbeschlusses vom 16. März 2021, GZ 5 Cg 105/19a-51, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision der beklagten Partei wird zurückgewiesen.

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Grohmann`(person)
- `Dr. Musger`(person)
- `Dr. Solé`(person)
- `Dr. Nowotny`(person)
- `MMag. Sloboda`(person)
- `Roxana Eisenhoefer`(person)
- `Mag. Axel Bauer`(person)
- `Magdalena Wosniak`(person)
- `Dr. Manfred Sommerbauer`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/2Ob180_21s`) (sent_id: `deanon_260716_TRAIN/2Ob180_21s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden sowie den Hofrat Dr. Musger, die Hofrätin Dr. Solé und die Hofräte Dr. Nowotny und MMag. Sloboda als weitere Richter in der Rechtssache der klagenden Partei Ing. Serge Keilacker, vertreten durch Dr. Alexander Bosio, Rechtsanwalt in Zell am See, gegen die beklagten Parteien 1. KzlR Gerhard Baltronat, Bakk. art., und 2. Gerald Povilaitis, MSc, beide vertreten durch Kinberger-Schuberth-Fischer Rechtsanwälte-GmbH in Zell am See, wegen 21.376,95 EUR sA und Feststellung (Streitwert: 10.000 EUR), über die Revisionen der klagenden und der zweitbeklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 6. August 2021, GZ 53 R 110/21i-23, womit das Teil- und Teilzwischenurteil des Bezirksgerichts Zell am See vom 6. April 2021, GZ 18 C 892/20z-17, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revisionen der klagenden und der zweitbeklagten Partei werden zurückgewiesen.

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Veith`(person)
- `Dr. Musger`(person)
- `Dr. Solé`(person)
- `Dr. Nowotny`(person)
- `MMag. Sloboda`(person)
- `Ing. Serge Keilacker`(person)
- `Dr. Alexander Bosio`(person)
- `KzlR Gerhard Baltronat, Bakk. art.`(person)
- `Gerald Povilaitis, MSc`(person)
- `Kinberger-Schuberth-Fischer Rechtsanwälte-GmbH`(organisation)
- `Landesgerichts Salzburg`(organisation)
- `Bezirksgerichts Zell am See`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/2Ob194_19x`) (sent_id: `deanon_260716_TRAIN/2Ob194_19x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden und den Hofrat Dr. Musger, die Hofrätin Dr. Solé und die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Haßtenteufel Umwelt GmbH & Co KG, Peter Zauner Weg 324, 5273 Wesen, Österreich, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Klagenfurt, gegen die beklagte Partei Isaak Tomzak, vertreten durch Dr. Maximilian Motschiunig, Rechtsanwalt in Klagenfurt, wegen Vertragsaufhebung und Abgabe einer Willenserklärung (Streitwert 35.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 1. Oktober 2019, GZ 2 R 141/19a, 2 R 142/19y-95, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`

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

**Example 9** (doc_id: `deanon_260716_TRAIN/2Ob57_20a`) (sent_id: `deanon_260716_TRAIN/2Ob57_20a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden und den Hofrat Dr. Musger, die Hofrätin Dr. Solé und die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Elina Faber, vertreten durch Dr. Gernot Lehner, Rechtsanwalt in Neumarkt im Hausruckkreis, gegen die beklagten Parteien 1. Chiara Prukop, 2.

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Veith`(person)
- `Dr. Musger`(person)
- `Dr. Solé`(person)
- `Dr. Nowotny`(person)
- `Mag. Pertmayr`(person)
- `Elina Faber`(person)
- `Dr. Gernot Lehner`(person)
- `Chiara Prukop`(person)

**Example 10** (doc_id: `deanon_260716_TRAIN/6Ob83_16y`) (sent_id: `deanon_260716_TRAIN/6Ob83_16y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden und durch die Hofräte Dr. Schramm, Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny als weitere Richter in der Pflegschaftssache der Minderjährigen 1. Miroslav Arfs, geboren am 8. Juli 2001, 2. Philipp Adomszent, geboren am 9. Juli 2002, 3. Roxana Costantin, geboren am 11. März 2005, 4. Mario Klingensteiner, geboren am 18. März 2010, über den außerordentlichen Revisionsrekurs der Mutter OSR Magdalena Aquila, vertreten durch Dr. Michèle Grogger-Endlicher, Rechtsanwältin in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 3. Februar 2016, GZ 48 R 369/15t-98, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen (§ 71 Abs 3 AußStrG).

**False Positives:**

- `Dr. Mich` — partial — pred is substring of gold: `Dr. Michèle Grogger-Endlicher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Schramm`(person)
- `Dr. Gitschthaler`(person)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. Nowotny`(person)
- `Miroslav Arfs`(person)
- `8. Juli`(date)
- `Philipp Adomszent`(person)
- `9. Juli`(date)
- `Roxana Costantin`(person)
- `11. März`(date)
- `Mario Klingensteiner`(person)
- `18. März`(date)
- `OSR Magdalena Aquila`(person)
- `Dr. Michèle Grogger-Endlicher`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/7Ob116_22t`) (sent_id: `deanon_260716_TRAIN/7Ob116_22t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Dr. Wurdinger, Mag. Malesich, Dr. Weber und Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Hedwig Konnertz, MSc, vertreten durch Dr. Christof Joham und Mag. Andreas Voggenberger, Rechtsanwälte in Eugendorf, gegen die beklagte Partei Noruniwald KI -AG, Teichterberg 14y, 3394 Wolfstein, Österreich, vertreten durch Dr. Haymo Modelhart und andere, Rechtsanwälte in Linz, wegen 9.132,90 EUR sA und Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 5. Mai 2022, GZ 53 R 51/22i-41, womit das Urteil des Bezirksgerichts Salzburg vom 26. Jänner 2022, GZ 12 C 675/20w-37, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`

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

**Example 12** (doc_id: `deanon_260716_TRAIN/7Ob157_19t`) (sent_id: `deanon_260716_TRAIN/7Ob157_19t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Wolf Makrigiannis, LLB LTD, Marienstraße 101, 4091 Wenzelberg, Österreich, vertreten durch Hasch & Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei MittelGarten Werke GmbH, Trappelgasse 16, 3361 Mauer bei Amstetten, Österreich, vertreten durch Dr. Dominik Schärmer, Rechtsanwalt in Wien, wegen 30.000 EUR, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 12. Juni 2019, GZ 6 R 46/19f-22, mit dem das Zwischenurteil des Landesgerichts Linz vom 26. Februar 2019, GZ 63 Cg 37/18i-18, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Dr. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Wolf Makrigiannis, LLB`(person)
- `Marienstraße 101, 4091 Wenzelberg, Österreich`(address)
- `Hasch & Partner Anwaltsgesellschaft mbH`(organisation)
- `MittelGarten Werke GmbH`(organisation)
- `Trappelgasse 16, 3361 Mauer bei Amstetten, Österreich`(address)
- `Dr. Dominik Schärmer`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Linz`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/7Ob162_20d`) (sent_id: `deanon_260716_TRAIN/7Ob162_20d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Dorothea Waeger, Bakk. techn. BEd, vertreten durch Mag. Marco und Mag. Amelie Kunczicky, Rechtsanwälte in Mayrhofen, gegen die beklagte Partei OberVerlag AG, Thomas Alva Edison-Straße 158, 4843 Wörmansedt, Österreich, vertreten durch Mag. Thomas Anker und DI Mag. Nikolaus Gratl, Rechtsanwäte in Innsbruck, wegen Urkundeneinsicht, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. Juni 2020, GZ 4 R 55/20z-18, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`

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

**Example 14** (doc_id: `deanon_260716_TRAIN/7Ob203_24i`) (sent_id: `deanon_260716_TRAIN/7Ob203_24i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Dr. Wurdinger, Mag. Malesich, Dr. Weber und Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Christina Steenfath, vertreten durch Mag. Martin Wabra, Rechtsanwalt in Gmünd, gegen die beklagte Partei SüdSanitär AG, Rechenweg 4O, 3261 Ernegg, Österreich, vertreten durch die MUSEY rechtsanwalt gmbH in Salzburg, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. Oktober 2024, GZ 5 R 144/24v-49, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`

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

**Example 15** (doc_id: `deanon_260716_TRAIN/7Ob21_20v`) (sent_id: `deanon_260716_TRAIN/7Ob21_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Bernhard Freyberg, vertreten durch die Niedermayr Rechtsanwalt GmbH in Steyr, gegen die beklagte Partei Dr. Flora Precht, vertreten durch Dr. Heinz Stöger, Rechtsanwalt in Wien, wegen 585.800 EUR sA und Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. November 2019, GZ 1 R 150/19i-18, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Dr. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Bernhard Freyberg`(person)
- `Niedermayr Rechtsanwalt GmbH`(organisation)
- `Dr. Flora Precht`(person)
- `Dr. Heinz Stöger`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/7Ob22_24x`) (sent_id: `deanon_260716_TRAIN/7Ob22_24x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Dr. Wurdinger, Mag. Malesich, Dr. Weber und Mag. Fitz als weitere Richter in der Rechtssache der gefährdeten Partei DI Hartwig Jullien, vertreten durch Dr. Kristina Venturini, Rechtsanwältin in Wien, gegen den Gegner der gefährdeten Partei DDr.in Juri Thias, vertreten durch Dr. Waltraud Künstl, Rechtsanwältin in Wien, wegen einstweiliger Verfügung gemäß § 382b und § 382c EO, über den außerordentlichen Revisionsrekurs des Gegners der gefährdeten Partei gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 29. Dezember 2023, GZ 16 R 312/23f-4, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO, § 78 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Solé`(person)
- `Mag. Dr. Wurdinger`(person)
- `Mag. Malesich`(person)
- `Dr. Weber`(person)
- `Mag. Fitz`(person)
- `DI Hartwig Jullien`(person)
- `Dr. Kristina Venturini`(person)
- `DDr.in Juri Thias`(person)
- `Dr. Waltraud Künstl`(person)
- `Landesgerichts Wiener Neustadt`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/7Ob36_25g`) (sent_id: `deanon_260716_TRAIN/7Ob36_25g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Malesich, Dr. Weber, Mag. Fitz und Mag. Jelinek als weitere Richter in der Rechtssache der klagenden Partei Gundula Aichmann, vertreten durch Poduschka Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Plönnigs Technik AG, Wieden 35, 3390 Spielberg, Österreich, vertreten durch Themmer, Toth & Partner Rechtsanwälte GmbH in Wien, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 28. November 2024, GZ 1 R 124/24t-14, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 27. Juni 2024, GZ 21 C 604/23m-10, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`

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

**Example 18** (doc_id: `deanon_260716_TRAIN/7Ob38_20v`) (sent_id: `deanon_260716_TRAIN/7Ob38_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in den verbundenen Rechtssachen der klagenden und widerbeklagten Partei Angelika Barankewitz, geboren am 11. Januar 2022, vertreten durch Mag. Sabine Schuster, Rechtsanwältin in Lenzing, gegen die beklagte und widerklagende Partei Frank Johannhson, geboren am 1. Juli 2017, vertreten durch Dr. Monika Morscher-Spießberger, Rechtsanwältin in Vöcklabruck, wegen Ehescheidung über die außerordentliche Revision der klagenden und widerbeklagten Partei gegen das Urteil des Landesgerichts Wels als Berufungsgericht vom 4. Dezember 2019, GZ 21 R 260/19p-48, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Dr. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Angelika Barankewitz`(person)
- `11. Januar 2022`(date)
- `Mag. Sabine Schuster`(person)
- `Frank Johannhson`(person)
- `1. Juli 2017`(date)
- `Dr. Monika Morscher-Spießberger`(person)
- `Landesgerichts Wels`(organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/7Ob45_19x`) (sent_id: `deanon_260716_TRAIN/7Ob45_19x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Dr. Arabella Venczel, vertreten durch Dr. Stefan Gloyer, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Berkenheger Analyse AG, Ebendorfer Hauptstraße 3, 8054 Graz, Österreich, vertreten durch Dr. Herbert Salficky, Rechtsanwalt in Wien, wegen 53.526,48 EUR sA und Feststellung, den Beschluss gefasst:  Spruch Das Urteil des Obersten Gerichtshofs vom 26. Juni 2019, zu 7 Ob 45/19x wird in seinen Entscheidungsgründen dahin berichtigt, dass es auf Seite 8 in Absatz 4 anstelle „Die Revision ist zulässig, sie ist im Sinn des Aufhebungsantrags auch berechtigt“ richtig „Die Revision ist zulässig, sie ist aber nicht berechtigt“ zu lauten hat.

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`

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

**Example 20** (doc_id: `deanon_260716_TRAIN/7Ob54_20x`) (sent_id: `deanon_260716_TRAIN/7Ob54_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende sowie die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Techn R Ramona Rössler, vertreten durch Mag. Astrid Roblyek, Rechtsanwältin in Klagenfurt am Wörthersee, gegen die beklagte Partei ZED Planung AG Haberditzlgasse 29, 9341 Kreuth, Österreich, vertreten durch Jarolim Partner Rechtsanwälte GmbH in Wien, wegen 7.339,70 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 31. Oktober 2019, GZ 4 R 325/19i-15, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 15. Juli 2019, GZ 15 C 998/18y-11, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`

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

**Example 21** (doc_id: `deanon_260716_TRAIN/7Ob6_20p`) (sent_id: `deanon_260716_TRAIN/7Ob6_20p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Ing. Roderich Florczyk, vertreten durch Dr. Norbert Nowak, Rechtsanwalt in Wien, gegen die beklagte Partei Mittel-Energie AG, Gaunitzhof 8, 4632 Breitwies, Österreich, vertreten durch die Schönherr Rechtsanwälte GmbH in Wien, wegen 6.342,73 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 8. November 2018, GZ 60 R 98/18v-12, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 15. Juni 2018, GZ 18 C 109/18p-8, abgeändert wurde, beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`

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

**Example 22** (doc_id: `deanon_260716_TRAIN/7Ob92_19h`) (sent_id: `deanon_260716_TRAIN/7Ob92_19h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Karen Jansonius, vertreten durch Dr. Herwig Ernst, Rechtsanwalt in Korneuburg, gegen die beklagte Partei Schopf Automotive AG Grebien-Gasse 50, 4675 Dirisam, Österreich, vertreten durch Dr. Herbert Laimböck, Rechtsanwalt in Wien, wegen 521.151,28 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. April 2019, GZ 5 R 32/19s-29, womit das Urteil des Handelsgerichts Wien vom 14. Jänner 2019, GZ 10 Cg 70/17z-25, bestätigt wurde, beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`

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

**Example 23** (doc_id: `deanon_260716_TRAIN/7Ob94_20d`) (sent_id: `deanon_260716_TRAIN/7Ob94_20d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Mag. Juliana Mündelein, vertreten durch Brand Rechtsanwälte GmbH in Wien, gegen die beklagte Partei ACBK Elektro Solutions AG, Schwarzenseer Straße 25, 9560 Steuerberg, Österreich, vertreten durch Dorda Rechtsanwälte GmbH in Wien, wegen 16.354,47 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 31. Jänner 2020, GZ 1 R 120/19b-21, womit das Urteil des Handelsgerichts Wien vom 22. Juli 2019, GZ 16 Cg 50/18d-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`

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

</details>

---

## `Prof Dr Name List` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `47aea583`  
**Description:**
Matches Prof. Dr. Name patterns in lists.

**Content:**
```
(?:,\s*|\s+und\s+)(Prof\.\s+Dr\.[\s]+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Ing Name List` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fab7906f`  
**Description:**
Matches Ing. Name patterns in lists or after roles.

**Content:**
```
(?:,\s*|\s+und\s+|des\s+|der\s+|den\s+)(Ing\.[\s]+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Mag Dr Name List` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2424034d`  
**Description:**
Matches Mag. Dr. Name patterns in lists.

**Content:**
```
(?:,\s*|\s+und\s+)(Mag\.\s+Dr\.[\s]+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Dr Name Standalone` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e91d29f0`  
**Description:**
Matches Dr. Name patterns where the previous token is a comma or 'und', ensuring the title is captured.

**Content:**
```
(?:,\s*|\s+und\s+)(Dr\.[\s]+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Role Name Full` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `42f7eeb9`  
**Description:**
Matches legal roles followed by titles and full names, capturing only the name part, with stricter negative lookahead.

**Content:**
```
(?:Senatspr\u00e4sident(?:in)?|Vizepr\u00e4sident(?:in)?|Hofrat(?:in)?|Hofr\u00e4te(?:in)?|Oberlandesgerichtsrat(?:in)?|Landesgerichtsrat(?:in)?|Bezirksgerichtsrat(?:in)?|Kanzler(?:in)?|Prokurator(?:in)?|Staatsanwalt(?:in)?|Richter(?:in)?|Vorsitzender(?:in)?|Mitglied(?:in)?|Privatbeteiligter(?:in)?|Zeuge(?:in)?|Gesch\u00e4digter(?:in)?|Angeklagter(?:in)?|Verurteilter(?:in)?|Opfer|Betroffener(?:in)?|Vertreter(?:in)?|Anwalt(?:in)?|Rechtsanwalt(?:in)?|Notar)\s+(?:(?:Dr\.|Mag\.|Hon\.-Prof\.|Univ\.-Prof\.|Priv\.-Doz\.|Prof\.|MMag\.|KR\.|OStR\.|StR\.|AR\.|Ing\.|DI\.|PhD\.|Dipl\.-Ing\.|Bakk\. iur\.|MBA|BSc|LL\.M\.|RgR|\u00d6kR|StR|OStR|KR|AR|VetR|PD|Mag\.a|Mag\.in|MMag\.in)\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 9 | 0 | 9 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 9 | 4074 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Eva Abdelrahman, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei Hochenadel Immobilien GmbH, Ritterhof 11, 2661 Graben, Österreich, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Gmb` — similar text (different position): `Hochenadel Immobilien GmbH`

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

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Cassandra Wespi, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Bilek Lebensmittel GmbH in Liqu, Dreijochgasse 11, 4722 Stefansdorf, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Gmb` — partial — pred is substring of gold: `Vogl Rechtsanwalt GmbH`

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

**Example 2** (doc_id: `deanon_260716_TRAIN/17Ob10_20z`) (sent_id: `deanon_260716_TRAIN/17Ob10_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätinnen Mag. Malesich und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Pascal Alsweh, vertreten durch Stephan Briem Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Dr. Simone Pittruff als Treuhänder der Insolvenzgläubiger der Unter-Analyse Aktiengesellschaft, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH in Linz, wegen Feststellung (Streitwert 18.335,66 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. März 2020, GZ 1 R 31/20i-13, womit das Urteil des Landesgerichts Linz vom 9. Dezember 2019, GZ 4 Cg 73/18z-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Gmb` — partial — pred is substring of gold: `Stephan Briem Rechtsanwalt GmbH`

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

**Example 3** (doc_id: `deanon_260716_TRAIN/2Ob194_24d`) (sent_id: `deanon_260716_TRAIN/2Ob194_24d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte MMag. Sloboda, Dr. Thunhart, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Dagobert Drügemöller, vertreten durch Gottgeisl Leinsmer Weber Rechtsanwälte GmbH in Wien, wider die beklagte Partei Rosalinde Nölker, Malta, vertreten durch Mag. Simon Wallner Rechtsanwalt GmbH in Wien, wegen 30.895 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 1. Oktober 2024, GZ 12 R 72/24g-21, den Beschluss gefasst:  Spruch I. Der Antrag auf Unterbrechung des Revisionsverfahrens bis zur Entscheidung des Europäischen Gerichtshofs zu C-683/24 wird abgewiesen.

**False Positives:**

- `Gmb` — similar text (different position): `Gottgeisl Leinsmer Weber Rechtsanwälte GmbH`

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

**Example 4** (doc_id: `deanon_260716_TRAIN/5Ob184_21a`) (sent_id: `deanon_260716_TRAIN/5Ob184_21a_4`)


Christian den Drijver, 2. Techn R Adalbert Amirzadeh, ebenda, beide vertreten durch Schlösser & Partner Rechtsanwälte OG in Wien, gegen die Antragsgegnerin Marion Döhnert, vertreten durch Mag. Michael Operschal Rechtsanwalt GmbH in Wien, wegen § 37 Abs 1 Z 8 iVm § 16 MRG, über den Revisionsrekurs der Antragsteller gegen den Sachbeschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 19. Mai 2021, GZ 40 R 2/21x-15, mit dem der Sachbeschluss des Bezirksgerichts Floridsdorf vom 30. Oktober 2020, GZ 28 Msch 9/19g-11, abgeändert wurde, den Sachbeschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Gmb` — partial — pred is substring of gold: `Mag. Michael Operschal Rechtsanwalt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Christian den Drijver`(person)
- `Techn R Adalbert Amirzadeh`(person)
- `Partner Rechtsanwälte OG`(organisation)
- `Marion Döhnert`(person)
- `Mag. Michael Operschal Rechtsanwalt GmbH`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Floridsdorf`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/6Ob10_22x`) (sent_id: `deanon_260716_TRAIN/6Ob10_22x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Nowotny, Dr. Hofer-Zeni-Rennhofer, Dr. Faber und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Tralog-KI Versicherungs AG, Adolf Schwayer-Gasse 22, 3371 Hofa, Österreich, vertreten durch Musey Rechtsanwalt GmbH in Salzburg, gegen die beklagte Partei WaldRecycling GmbH, Georg-Rendl-Weg 28, 9065 Ebenthal, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 7.246.839 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 1. Dezember 2021, GZ 2 R 165/21d-49, womit das Teil- und Zwischenurteil des Landesgerichts Salzburg vom 6. September 2021, GZ 6 Cg 16/20m-45, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Gmb` — partial — pred is substring of gold: `Musey Rechtsanwalt GmbH`

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

**Example 6** (doc_id: `deanon_260716_TRAIN/6Ob118_16w`) (sent_id: `deanon_260716_TRAIN/6Ob118_16w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden und durch die Hofräte Dr. Schramm, Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Ing. Laurence Joester, vertreten durch Dr. Wolfgang Leitner, Priv.-Doz. Dr. Max Leitner, Dr. Mara-Sophie Häusler, Rechtsanwälte in Wien, gegen die beklagte Partei Jasper Ratloff, vertreten durch Lederer Rechtsanwalt GmbH in Wien, und der Nebenintervenienten auf Seite der beklagten Partei 1.

**False Positives:**

- `Gmb` — partial — pred is substring of gold: `Lederer Rechtsanwalt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Schramm`(person)
- `Dr. Gitschthaler`(person)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. Nowotny`(person)
- `Ing. Laurence Joester`(person)
- `Dr. Wolfgang Leitner`(person)
- `Priv.-Doz. Dr. Max Leitner`(person)
- `Dr. Mara-Sophie Häusler`(person)
- `Jasper Ratloff`(person)
- `Lederer Rechtsanwalt GmbH`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/7Ob137_17y`) (sent_id: `deanon_260716_TRAIN/7Ob137_17y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Dr. Höllwerth, Dr. E. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Dr. Elias Hemerle, vertreten durch die Breiteneder Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Mooshuber Planung AG, Schustergasse 57, 4682 Brunau, Österreich, vertreten durch die Binder Grösswang Rechtsanwälte GmbH in Wien, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 31. Mai 2017, GZ 4 R 19/17v-16, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Gmb` — partial — pred is substring of gold: `Breiteneder Rechtsanwalt GmbH`

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

**Example 8** (doc_id: `deanon_260716_TRAIN/7Ob21_20v`) (sent_id: `deanon_260716_TRAIN/7Ob21_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Bernhard Freyberg, vertreten durch die Niedermayr Rechtsanwalt GmbH in Steyr, gegen die beklagte Partei Dr. Flora Precht, vertreten durch Dr. Heinz Stöger, Rechtsanwalt in Wien, wegen 585.800 EUR sA und Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. November 2019, GZ 1 R 150/19i-18, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Gmb` — partial — pred is substring of gold: `Niedermayr Rechtsanwalt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Dr. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Bernhard Freyberg`(person)
- `Niedermayr Rechtsanwalt GmbH`(organisation)
- `Dr. Flora Precht`(person)
- `Dr. Heinz Stöger`(person)
- `Oberlandesgerichts Wien`(organisation)

</details>

---

## `Name with Degree` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `650daf7c`  
**Description:**
Matches names followed by degrees like MSc, M.A., LL.M. in standalone or list contexts.

**Content:**
```
([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s+(?:MSc|M\.A\.|M\.Sc\.|LL\.M\.|LLB)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Mag Name Full` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7607e33a`  
**Description:**
Matches Mag. followed by full names, explicitly allowing hyphenated surnames.

**Content:**
```
Mag\.\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 6 | 0 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 6 | 4025 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden, die Hofräte Mag. Schober, Dr. Annerl und Dr. Vollmaier sowie die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Ing. Mag. Pamela Gotterbauer, vertreten durch Mag. Helwig Schuster, Rechtsanwalt in Melk, gegen die beklagten Parteien 1.

**False Positives:**

- `Mag. Pamela Gotterbauer` — partial — pred is substring of gold: `Ing. Mag. Pamela Gotterbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Mag. Schober`(person)
- `Dr. Annerl`(person)
- `Dr. Vollmaier`(person)
- `Dr. Wallner-Friedl`(person)
- `Ing. Mag. Pamela Gotterbauer`(person)
- `Mag. Helwig Schuster`(person)

**Example 1** (doc_id: `deanon_260716_TRAIN/8Ob123_18y`) (sent_id: `deanon_260716_TRAIN/8Ob123_18y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn, den Hofrat Dr. Stefula und die Hofrätin Mag. Wessely-Kristöfel als weitere Richter in der Pflegschaftssache der 1. mj Techn R VetR Erhard Januscheidt, geboren am 8. Februar 2002, 2. mj Kurt Altiparmak, geboren am 12. September 2004, beide wohnhaft beim Vater Eberhard Jendges, BA, dieser vertreten durch Ing. Mag. Andreas Gartner, Rechtsanwalt in St. Valentin, und 3. mj Agnes Jirasek, geboren am 6. Februar 2013, wohnhaft bei der Mutter Elina Wientzeck, diese vertreten durch Gloß, Pucher, Leitner, Schweinzer, Gloß, Rechtsanwälte in St. Pölten, wegen Ersetzung der Zustimmung zur Namensänderung, über den Revisionsrekurs der Mutter gegen den Beschluss des Landesgerichts St. Pölten als Rekursgericht vom 3. Juli 2018, GZ 23 R 226/18k-58, mit dem der Beschluss des Bezirksgerichts St. Pölten vom 3. April 2018, GZ 2 Ps 270/16s-47, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Mag. Andreas Gartner` — partial — pred is substring of gold: `Ing. Mag. Andreas Gartner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Tarmann-Prentner`(person)
- `Mag. Korn`(person)
- `Dr. Stefula`(person)
- `Mag. Wessely-Kristöfel`(person)
- `Techn R VetR Erhard Januscheidt`(person)
- `Kurt Altiparmak`(person)
- `Eberhard Jendges, BA`(person)
- `Ing. Mag. Andreas Gartner`(person)
- `Agnes Jirasek`(person)
- `Elina Wientzeck`(person)
- `Landesgerichts St. Pölten`(organisation)
- `Bezirksgerichts St. Pölten`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/9ObA11_12a`) (sent_id: `deanon_260716_TRAIN/9ObA11_12a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Hofrat des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras, die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter KR Mag. Paul Kunsky und Dr. Klaus Mayr als weitere Richter in der Arbeitsrechtssache der klagenden Partei DI Pablo Göppele, vertreten durch Dr. Andreas Löw, Rechtsanwalt in 1070 Wien, wider die beklagte Partei Druck Lemverlex GmbH, Mühlbauerweg 44, 4841 Brunau, Österreich, vertreten durch Dr. Peter Rudeck, Dr. Gerhard Schlager, Rechtsanwälte in 1080 Wien, wegen Ausstellung eines Dienstzeugnisses, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 21. Oktober 2011, GZ 9 Ra 102/11b-10, mit dem der Berufung des Klägers gegen das Urteil des Arbeits- und Sozialgerichts Wien vom 30. Mai 2011, GZ 1 Cga 40/11z-6, keine Folge gegeben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Mag. Paul Kunsky` — partial — pred is substring of gold: `KR Mag. Paul Kunsky`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hopf`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Dehn`(person)
- `KR Mag. Paul Kunsky`(person)
- `Dr. Klaus Mayr`(person)
- `DI Pablo Göppele`(person)
- `Dr. Andreas Löw`(person)
- `Druck Lemverlex GmbH`(organisation)
- `Mühlbauerweg 44, 4841 Brunau, Österreich`(address)
- `Dr. Peter`(person)
- `Dr. Gerhard Schlager`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/9ObA120_19s`) (sent_id: `deanon_260716_TRAIN/9ObA120_19s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau und den Hofrat des Obersten Gerichtshofs Dr. Hargassner sowie die fachkundigen Laienrichter KR Mag. Paul Kunsky und Harald Kohlruss als weitere Richter in der Arbeitsrechtssache der klagenden Partei Mike Scheinpflug, vertreten durch Mag. Martin Wakolbinger, Rechtsanwalt in Enns, gegen die beklagte Partei EnnsValkelKI GmbH, Eckldorf 4z, 8755 Möschitzgraben, Österreich, vertreten durch Mag. Martin Singer, Rechtsanwalt in Schwaz, wegen 7.434,83 EUR sA, über die Revision der beklagten Partei (Revisionsstreitwert: 2.400 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 12. August 2019, GZ 11 Ra 45/19w-33, mit dem den Berufungen beider Parteien gegen das Urteil des Landesgerichts Linz als Arbeits- und Sozialgericht vom 19. Februar 2019, GZ 9 Cga 79/18i-26, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Mag. Paul Kunsky` — partial — pred is substring of gold: `KR Mag. Paul Kunsky`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hopf`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Fichtenau`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hargassner`(person)
- `KR Mag. Paul Kunsky`(person)
- `Harald Kohlruss`(person)
- `Mike Scheinpflug`(person)
- `Mag. Martin Wakolbinger`(person)
- `EnnsValkelKI GmbH`(organisation)
- `Eckldorf 4z, 8755 Möschitzgraben, Österreich`(address)
- `Mag. Martin Singer`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Linz`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/9ObA144_14p`) (sent_id: `deanon_260716_TRAIN/9ObA144_14p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden und die Hofräte des Obersten Gerichtshofs Mag. Ziegelbauer und Dr. Hargassner sowie die fachkundigen Laienrichter KR Mag. Paul Kunsky und Harald Kohlruss als weitere Richter in der Arbeitsrechtssache der klagenden Partei Franziska Schönmeier, vertreten durch Held Berdnik Astner & Partner Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Heizung Bachkraftlog GmbH & Co KG, Schlangglfeld 48, 4980 Viehausen, Österreich, vertreten durch die Klein, Wuntschek & Partner Rechtsanwälte GmbH in Graz, wegen Kündigungsanfechtung, über die außerordentliche Revision und den „Kostenrekurs“ der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 26. September 2014, GZ 7 Ra 66/14a-25, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mag. Paul Kunsky` — partial — pred is substring of gold: `KR Mag. Paul Kunsky`

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

**Example 5** (doc_id: `deanon_260716_TRAIN/9ObA4_10v`) (sent_id: `deanon_260716_TRAIN/9ObA4_10v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten des Obersten Gerichtshofs Dr. Rohrer als Vorsitzenden und die Hofräte des Obersten Gerichtshofs Dr. Hradil und Hon.-Prof. Dr. Kuras sowie die fachkundigen Laienrichter Mag. Eva Pernt und KR Mag. Michaela Haydter als weitere Richter in der Arbeitsrechtssache der klagenden Partei Bruno Milona, vertreten durch Mag. Stefan Weiskopf, Dr. Rainer Kappacher, Rechtsanwälte in Landeck, wider die beklagte Partei Mathilda Bödiker, vertreten durch Greiter, Pegger, Kofler & Partner, Rechtsanwälte in Innsbruck, sowie den Nebenintervenienten auf Seiten der beklagten Partei Hubert Wegmüller, wegen 65.800 EUR sA und Rechnungslegung (Streitwert 6.000 EUR), über die Revision der beklagten Partei (Revisionsinteresse 1.500 EUR) gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 10. November 2009, GZ 15 Ra 96/09v-40, mit dem infolge Berufung beider Parteien das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 29. April 2009, GZ 44 Cga 33/07z-35, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Mag. Michaela Haydter` — partial — pred is substring of gold: `KR Mag. Michaela Haydter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Rohrer`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hradil`(person)
- `Hon.-Prof. Dr. Kuras`(person)
- `Mag. Eva Pernt`(person)
- `KR Mag. Michaela Haydter`(person)
- `Bruno Milona`(person)
- `Mag. Stefan Weiskopf`(person)
- `Dr. Rainer Kappacher`(person)
- `Mathilda Bödiker`(person)
- `Greiter, Pegger, Kofler & Partner, Rechtsanwälte`(organisation)
- `Hubert Wegmüller`(person)
- `Oberlandesgerichts Innsbruck`(organisation)
- `Landesgerichts Innsbruck`(organisation)

</details>

---

## `Legal Role Context` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b5811980`  
**Description:**
Matches person names following specific legal context words (als, durch, und, sowie) that indicate a person, excluding the role itself.

**Content:**
```
(?:als|durch|und|sowie|von|mit|gegen|in\s+der|im|des|der|den|eines|einer)\s+(?:Hon\.-Prof\.|Univ\.-Prof\.|Priv\.-Doz\.|Prof\.|Dr\.|Mag\.|MMag\.|DI\.|Ing\.|Dipl\.-Ing\.|Bakk\. iur\.|MBA|BSc|LL\.M\.|RgR|\u00d6kR|StR|OStR|KR|AR|VetR|PD|Prof\.in|Univ\.-Prof\.in|MMag\.in|DDr\.|DDr\.in|Hon\.-Prof\.in|Univ\.-Prof\.in)?\s+(?:Dr\.)?\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+-[A-Z][a-zäöüß]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 2 | 3857 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Karim Mielewczik, gegen die beklagte Partei Dr. Sandro Gädecken, vertreten durch Ing. Dr. Stefan Krall und Dr. Oliver Kühnl, Rechtsanwälte in Innsbruck, wegen 9.456 EUR sA (Revisionsinteresse 9.268,50 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 25. Februar 2025, GZ 21 R 434/24f-29, mit dem das Urteil des Bezirksgerichts Seekirchen am Wallersee vom 5. September 2024, GZ 2 C 1107/23d-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `durch Ing. Dr. Stefan Krall` — partial — gold is substring of pred: `Ing. Dr. Stefan Krall`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Dr. Annerl`(person)
- `Dr. Vollmaier`(person)
- `Dr. Wallner-Friedl`(person)
- `Karim Mielewczik`(person)
- `Dr. Sandro Gädecken`(person)
- `Ing. Dr. Stefan Krall`(person)
- `Dr. Oliver Kühnl`(person)
- `Landesgerichts Salzburg`(organisation)
- `Bezirksgerichts Seekirchen`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofrätin Dr. Grohmann und den Hofrat Dr. Steger als weitere Richter in der Pflegschaftssache des mj Aron Margwarth, geboren am 29. März 1957, Vater Klaus Rufer, vertreten durch Prof. Dr. Georg Zanger, Rechtsanwalt in Wien, wegen Obsorge, über den Delegierungsantrag der Mutter Rafaela Erreth, vertreten durch Mag. Britta Schönhart-Loinig, Rechtsanwältin in Wien, den Beschluss gefasst:  Spruch Der Antrag auf Delegierung der Pflegschaftssache vom Bezirksgericht Gänserndorf an das Bezirksgericht Villach wird abgewiesen.

**False Positives:**

- `durch Prof. Dr. Georg Zanger` — partial — gold is substring of pred: `Prof. Dr. Georg Zanger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Jensik`(person)
- `Dr. Grohmann`(person)
- `Dr. Steger`(person)
- `Aron Margwarth`(person)
- `29. März 1957`(date)
- `Klaus Rufer`(person)
- `Prof. Dr. Georg Zanger`(person)
- `Rafaela Erreth`(person)
- `Mag. Britta Schönhart-Loinig`(person)
- `Bezirksgericht Gänserndorf`(organisation)
- `Bezirksgericht Villach`(organisation)

</details>

---

## `Genitive Person Name` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `08a727f7`  
**Description:**
Specifically targets names appearing in genitive constructions common in criminal judgments (e.g., 'des Verbrechens ... [Name]'), ensuring the name is preceded by a genitive article or preposition.

**Content:**
```
(?:des|der|die|eines|einer)\s+([A-Z][a-zäöüß]+\s+[A-Z][a-zäöüß]+)\b(?=\s+(?:des|der|die|von|mit|durch|als|und|sowie|im|am|bei|nach|vor|über|unter|ohne|neben|zwischen|trotz|wegen|statt|außer|seit|während|bis|um|für|an|auf|in|,|\.|\(|\))|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 9 | 0 | 9 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 9 | 4167 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_24`)


Zwar können der Wohnort der Parteien und der zu vernehmenden Zeugen oder auch die Lage eines Augenscheinsgegenstands Zweckmäßigkeitsgründe für die Beurteilung des Delegierungsantrags sein (vgl RS0046333 [T8]).

**False Positives:**

- `Augenscheinsgegenstands Zweckmäßigkeitsgründe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_115`)


7 Ob 167/24w Rz 17) – nicht bezweifelt. Soweit die Antragsgegnerin geltend macht, dass der Antragsteller den Einbau eines Smart Meters (mit einer „Opt-Out-Konfiguration“) zu dulden (und sie dafür Zugang zum Objekt zu erhalten) habe, ist dies nicht Gegenstand des Provisorialverfahrens, in dem es vielmehr um die Berechtigung der Antragsgegnerin geht, einen solchen Anspruch durch (Drohung mit) Stromabschaltung oder Auflösung des Netzzugangsvertrags durchzusetzen (9 Ob 95/24x Rz 26;

**False Positives:**

- `Smart Meters` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_10`)


DerKlägermacht mit seiner Klage Ansprüche (Leistung und Feststellung) aufgrund eines gegenüber der Beklagten erklärten Rücktritts aus der Veranlagung in die Kommanditbeteiligung geltend.

**False Positives:**

- `Klage Ansprüche` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_260716_TRAIN/1Ob152_24w`) (sent_id: `deanon_260716_TRAIN/1Ob152_24w_18`)


Das ist aber nur der Fall, wenn das Berufungsgericht seiner Entscheidung Tatsachenannahmen ohne Beweisergänzung oder Beweiswiederholung zugrunde legt, die über jene des Erstgerichts hinausgehen oder von diesen abweichen (1 Ob 2/21g).

**False Positives:**

- `Entscheidung Tatsachenannahmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_260716_TRAIN/2Ob114_24i`) (sent_id: `deanon_260716_TRAIN/2Ob114_24i_36`)


Dass die Veräußerung einer Vermächtnisforderung Zessionsrecht und nicht den Regeln über den Erbschaftskauf zu unterstellen ist, ist schon aus dem klaren Wortlaut der §§ 1392 und 1278 ABGB abzuleiten und entspricht auch der bisherigen Rechtsprechung (6 Ob 136/07d Pkt 9.3.4.; so auch die herrschende Lehre:Bayer/NowotnyinKletečka/Schauer, ABGB-ON1.05§ 1278 Rz 5;Stefulain Klang³ § 1278 ABGB Rz 44;Karner/Steiningerin KBB7§ 1278 ABGB Rz 2 aA [aber nur in Bezug auf die Einhaltung der Formpflicht]:Ch.

**False Positives:**

- `Vermächtnisforderung Zessionsrecht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_260716_TRAIN/4Ob226_21w`) (sent_id: `deanon_260716_TRAIN/4Ob226_21w_17`)


Es steht nämlich nicht nur fest, dass die Medikamenteneinnahme der Klägerin für die Schlaganfälle ihres Sohnes weder kausal noch risikoerhöhend war, sondern auch, dass der Beklagten weder in Ansehung der (Wieder-)Verordnung des Medikaments noch im Zusammenhang mit einer in erster Instanz noch behaupteten, in der Revision aber nicht mehr konkret angesprochenen Fehlbehandlung durch Unterbleiben einer Notsectio Behandlungsfehler unterlaufen sind.

**False Positives:**

- `Notsectio Behandlungsfehler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_260716_TRAIN/6Ob118_16w`) (sent_id: `deanon_260716_TRAIN/6Ob118_16w_7`)


Er zeichnete auf Empfehlung und Vermittlung des Beklagten, der sich nach seiner Tätigkeit als Bankmitarbeiter selbständig gemacht und zu dem der Kläger als Vermögensberater gewechselt hatte, von September 2002 bis April 2007 unter Zwischenschaltung eines Treuhänders Kommanditbeteiligungen an sechs Kommanditgesellschaften deutschen Rechts („Reefer-Flotten-Fonds I und II“, „Holland-Fonds“, „Merkur Sky“) über eine Summe von insgesamt 105.000 EUR, ab den fünf seit 2004 eingegangenen Beteiligungen jeweils zuzüglich eines Agios von 750 EUR.

**False Positives:**

- `Treuhänders Kommanditbeteiligungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_260716_TRAIN/7Ob92_19h`) (sent_id: `deanon_260716_TRAIN/7Ob92_19h_13`)


[...]“ 11T-Allgemeine Feuerversicherungs-Bedingungen (AFB) „Allgemeiner Teil Auf dieVersicherung finden die Bestimmungen der Allgemeinen Bedingungen für die Sachversicherung (ABS) Anwendung.

**False Positives:**

- `Teil Auf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_260716_TRAIN/7Ob92_19h`) (sent_id: `deanon_260716_TRAIN/7Ob92_19h_30`)


[...] HH1-Allgemeine Bedingungen für Haushaltsversicherungen-ABH „Allgemeiner Teil Auf die Sachversicherung finden dieallgemeinen Bedingungen für die Sachversicherung (ABS) Anwendung, […].

**False Positives:**

- `Teil Auf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Mimi Jueterbock Pattern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2ab1136c`  
**Description:**
Specific pattern for 'Mimi Jueterbock' which appears without a title in the training data.

**Content:**
```
Mimi\s+Jueterbock
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Istvan Krautkrämer Pattern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `69988dfa`  
**Description:**
Specific pattern for 'Istvan Krautkrämer' which appears without a title.

**Content:**
```
Istvan\s+Krautkrämer
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

