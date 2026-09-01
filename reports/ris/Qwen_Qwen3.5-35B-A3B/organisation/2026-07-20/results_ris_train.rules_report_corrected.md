# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-08-31T08:21:59.936691

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | 1000 |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 800 |
| Validation documents | 200 |
| Test documents | 477 |
| Train sentences | 3245 |
| Validation sentences | 812 |
| Test sentences | 22727 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 30 |
| Max samples in prompt | 200 |
| Refinement iterations | 1 |
| Seed | 42 |
| Agentic | False |
| Enable Critic | True |
| Enable Prune | False |
| Critic Interval | 2 |
| Audit Interval | 0 |
| Use GREX | True |
| Format | regex |
| Synthesis strategy | bulk |
| Sampling strategy | balanced |
| Batch size | 50 |
| Refine per batch | 0 |
| Manually annotated examples | 0 |
| First batch with manual data | None |

</details>

---

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 98.0% |
| True Positives | 3375 |
| False Positives | 91 |
| False Negatives | 639 |
| Total Gold Entities | 4014 |
| Micro Precision | 97.4% |
| Micro Recall | 84.1% |
| Micro F1 | 90.2% |
| Macro F1 | 90.2% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Oberste_Gerichtshof` | 55.5% | 100.0% | 38.4% | 1543 | 1543 | 0 |
| `Oberlandesgericht_City` | 17.0% | 100.0% | 9.3% | 373 | 373 | 0 |
| `OGH_Abbreviation` | 21.9% | 100.0% | 12.3% | 493 | 493 | 0 |
| `Bezirksgericht_Handelsgericht` | 0.2% | 100.0% | 0.1% | 5 | 5 | 0 |
| `Verfassungsgerichtshof` | 1.1% | 100.0% | 0.6% | 23 | 23 | 0 |
| `Landesgericht_City_Extended` | 19.6% | 100.0% | 10.9% | 436 | 436 | 0 |
| `Magistrat_Wien` | 0.4% | 100.0% | 0.2% | 8 | 8 | 0 |
| `Verein_Organisation` | 0.1% | 100.0% | 0.0% | 2 | 2 | 0 |
| `Landesgericht_Strafsachen` | 4.8% | 100.0% | 2.5% | 99 | 99 | 0 |
| `VwGH_Abbreviation` | 0.4% | 100.0% | 0.2% | 9 | 9 | 0 |
| `Bezirksgericht_Spittal_Güssing_Schärding` | 0.1% | 100.0% | 0.0% | 2 | 2 | 0 |
| `Bezirksgerichts_Leopoldstadt` | 0.3% | 100.0% | 0.2% | 7 | 7 | 0 |
| `Bezirksgericht_City_Extended` | 10.8% | 98.7% | 5.7% | 232 | 229 | 3 |
| `Hyphenated_Ampersand_Corporate_Name` | 1.4% | 93.5% | 0.7% | 31 | 29 | 2 |
| `Law_Firm_Rechtsanwaelte_OG` | 1.8% | 72.0% | 0.9% | 50 | 36 | 14 |
| `Law_Firm_OG_KG_GmbH` | 3.5% | 66.7% | 1.8% | 108 | 72 | 36 |
| `Gesellschaft_mbh_Specific` | 0.1% | 50.0% | 0.1% | 6 | 3 | 3 |
| `Domain_Organisation` | 0.2% | 30.8% | 0.1% | 13 | 4 | 9 |
| `Generic_KG_Entity` | 0.1% | 7.7% | 0.0% | 26 | 2 | 24 |
| `Bezirksgericht_Grieskirchen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `PVA_Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SAK_Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schweizer_Ausgleichskasse_SAK` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wien_Telekom_Betriebe_GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `OGK_Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Vorarlberger_Gebietskrankenkasse` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Landesgericht_Krems` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Hyphenated_Gesellschaft_mbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Slash_Separated_Corporate_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Oberste_Gerichtshof` 🏆

**F1:** 0.555 | **Precision:** 1.000 | **Recall:** 0.384  

**Format:** `regex`  
**Rule ID:** `69f4d34d`  
**Description:**
Matches the Supreme Court of Austria in nominative or genitive case.

**Content:**
```
\bOberste(?:n)?\s+Gerichtshof(?:s)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.384 | 0.555 | 1543 | 1543 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1543 | 0 | 2470 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Jason Langeloh, vertreten durch die Mag. Martin Rützler, Rechtsanwalt in Dornbirn, gegen die beklagte Partei, Selma Einoeder, vertreten durch Mag. Alexander Gerngross und Mag. Klaus Köck, Rechtsanwälte in Premstätten bei Graz, wegen 6.795,66 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 223 C 1313/24w des Bezirksgerichts Graz-Ost den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an das Bezirksgericht Dornbirn wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Hon.-Prof. Dr. Nowotny` (person)
- `Mag. Schober` (person)
- `Dr. Vollmaier` (person)
- `Jason Langeloh` (person)
- `Mag. Martin Rützler` (person)
- `Selma Einoeder` (person)
- `Mag. Alexander Gerngross` (person)
- `Mag. Klaus Köck` (person)
- `Bezirksgerichts Graz-Ost` (organisation)
- `Bezirksgericht Dornbirn` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_14`)


Das Erstgericht legte den Akt dem Obersten Gerichtshof unter Hinweis auf den Verfahrensstand, aber entgegen § 31 Abs 3 JN ohne eigene Stellungnahme zur Zweckmäßigkeit, zur Entscheidung über den Delegierungsantrag vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Kordelia Meelis, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Fatima Tengel, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Kordelia Meelis` (person)
- `Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft` (organisation)
- `Fatima Tengel` (person)
- `Mag. Ernst Michael Lang` (person)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_13`)


In ihrem gegen diesen Beschluss erhobenenRekursbeantragte die Klägerin hilfsweise (für den Fall, dass ihrem Rekurs nicht stattgegeben werden sollte) die Ordination gemäß § 28 JN an ein vom Obersten Gerichtshof zu benennendes Bezirksgericht (ON 34).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_19`)


Ist über die internationale Zuständigkeit bereits eine rechtskräftige Entscheidung ergangen, ist der Oberste Gerichtshof an diese Entscheidung gebunden (Garberin Fasching/Konecny3§ 28 JN Rz 25;

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_23`)


2.1 Als Grundlage für eine Ordination kommt daher nur der Fall des § 28 Abs 1 Z 2 JN in Betracht, wonach die Bestimmung eines örtlich zuständigen Gerichts durch den Obersten Gerichtshof dann zulässig ist, wenn der Antragsteller seinen Wohnsitz im Inland hat und im Einzelfall die Rechtsverfolgung im Ausland nicht möglich oder unzumutbar wäre (RIS-Justiz RS0112108).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der beim Landesgericht Linz zu AZ 3 Cg 46/21a anhängigen Rechtssache der klagenden Partei Hollengk Planung GmbH, Am Steindl 3, 9873 Döbriach, Österreich, vertreten durch Huber Berchtold Rechtsanwälte OG in Wien, gegen die beklagte Partei Wind Nexheimval GmbH, Wiesbergsiedlung 4, 8341 Pöllau, Österreich, vertreten durch ScherbaumSeebacher Rechtsanwälte GmbH in Graz, wegen 188.117,55 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN folgenden Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, zur Verhandlung und Entscheidung der Rechtssache anstelle des Landesgerichts Linz das Landesgericht Korneuburg zu bestimmen, wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

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
- `Landesgerichts Linz` (organisation)
- `Landesgericht Korneuburg` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Schramm als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Florens Drehkopf, LLB, geboren am 16. Dezember 1952, AZ 7 P 203/15g des Bezirksgerichts Mödling, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Mödling zurückgestellt.  Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Schramm` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Florens Drehkopf, LLB` (person)
- `16. Dezember 1952` (date)
- `Bezirksgerichts Mödling` (organisation)
- `Bezirksgericht Mödling` (organisation)
- `Bezirksgericht Mödling` (organisation)
- `Bezirksgericht Judenburg` (organisation)
- `Bezirksgerichts Judenburg` (organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_4`)


Das Bezirksgericht Mödling legte den Akt zur Entscheidung gemäß § 111 Abs 2 JN dem Obersten Gerichtshof vor (ON 8), ohne den Übertragungsbeschluss an die Parteien zuzustellen.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Missed by this rule (FN):**

- `Bezirksgericht Mödling` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_8`)


Andernfalls könnte eine Verschiebung der funktionellen Zuständigkeit eintreten, weil mangels Bestätigung des Übertragungsbeschlusses durch das Rekursgericht gar keine Grundlage für die Genehmigung einer Zuständigkeitsübertragung durch den Obersten Gerichtshof bestünde (9 Nc 15/14a;

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Marlene Friss, Russische Föderation, gegen die verpflichtete Partei WestTelekom GmbH, Rehwald 11, 4723 Fronberg, Österreich, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Marlene Friss` (person)
- `WestTelekom GmbH` (organisation)
- `Rehwald 11, 4723 Fronberg, Österreich` (address)
- `Bezirksgericht Innere Stadt Wien` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_4`)


Text Begründung: Mit ihrer erkennbar an den Obersten Gerichtshof gerichteten Eingabe vom 6.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 12** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und die Hofräte Dr. Fellinger und Dr. Schramm als weitere Richter in der Pflegschaftssache der Minderjährigen Gerhard Lohrmann, geboren am 10. August 1983, und Veit Künneken, geboren am 31. Mai 1967, AZ 2 PS 117/09t des Bezirksgerichts Feldkirchen, infolge Vorlage zur Genehmigung der Übertragung gemäß § 111 JN an das Bezirksgericht Neunkirchen, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Übertragung der Zuständigkeit zur Besorgung dieser Pflegschaftssache an das Bezirksgericht Neunkirchen wird genehmigt.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Schramm` (person)
- `Gerhard Lohrmann` (person)
- `10. August 1983` (date)
- `Veit Künneken` (person)
- `31. Mai 1967` (date)
- `Bezirksgerichts Feldkirchen` (organisation)
- `Bezirksgericht Neunkirchen` (organisation)
- `Bezirksgericht Neunkirchen` (organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_9`)


Das übertragende Gericht legte aufgrund dieser Weigerung den Akt dem Obersten Gerichtshof als gemeinsam übergeordnetem Gericht zur Entscheidung gemäß § 111 Abs 2 JN vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 14** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen Selma Eichler, LLM, geboren 13. September 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt. Begründung:  Rechtliche Beurteilung [1] Mit Beschluss vom 12.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Nowotny` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Selma Eichler, LLM` (person)
- `13. September` (date)
- `Bezirksgerichts Graz-West` (organisation)
- `Bezirksgericht Graz-West` (organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_5`)


[2] Das Bezirksgericht Graz-West legte den Akt daraufhin dem Obersten Gerichtshof zur Entscheidung gemäß § 111 Abs 2 JN vor, ohne den Übertragungsbeschluss den Parteien zuzustellen.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Missed by this rule (FN):**

- `Bezirksgericht Graz-West` (organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Ober-Automotive GmbH, Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei Katharina Rothschadl, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Ober-Automotive GmbH` (organisation)
- `Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich` (address)
- `Mag. Alexander Rimser` (person)
- `Katharina Rothschadl` (person)

**Example 17** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_15`)


Das Erstgericht wies die Klage wegen Fehlens eines inländischen Gerichtsstands und somit der österreichischen internationalen Zuständigkeit rechtskräftig zurück und legte daraufhin den Akt dem Obersten Gerichtshof zur Entscheidung über den hilfsweise gestellten Ordinationsantrag vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 18** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin mj Dietlind Schiewick, geboren 23. Oktober 2017, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Vöcklabruck, 4840 Vöcklabruck, Sportplatzstraße 1–3), deren Mutter Gisela Akcakaya, MSc, und des Antragsgegners Ernst Hartjens, Russische Föderation, wegen Feststellung der Abstammung, aufgrund der vom Bezirksgericht Josefstadt verfügten Vorlage des Akts AZ 23 Fam 2/21y zur Entscheidung gemäß § 111 Abs 2 JN den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Villach zurückgestellt.  Text Begründung: [1] Gegenstand des Verfahrens ist der Antrag auf Feststellung der Abstammung der zum Zeitpunkt der Antragstellung am 24.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Mag. Ziegelbauer` (person)
- `Dietlind Schiewick` (person)
- `23. Oktober` (date)
- `Bezirkshauptmannschaft Vöcklabruck` (organisation)
- `Gisela Akcakaya, MSc` (person)
- `Ernst Hartjens` (person)
- `Bezirksgericht Josefstadt` (organisation)
- `Bezirksgericht Villach` (organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_21`)


[7] Letztlich legte das Bezirksgericht Josefstadt die Akten dem Obersten Gerichtshof zur Entscheidung des Zuständigkeitsstreits vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Missed by this rule (FN):**

- `Bezirksgericht Josefstadt` (organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_22`)


[8] Die vom Bezirksgericht Villach veranlasste Vorlage der Akten an den Obersten Gerichtshof ist verfrüht:  Rechtliche Beurteilung [9] Übertragungsbeschlüsse nach § 111 JN sind durch die Parteien anfechtbar (RIS-Justiz RS0046981 [insb T5]).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Missed by this rule (FN):**

- `Bezirksgericht Villach` (organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_23`)


Ohne rechtskräftigen Übertragungsbeschluss nach § 111 Abs 1 JN kommt eine Entscheidung des Obersten Gerichtshofs nach § 111 Abs 2 JN nicht in Betracht (RS0047067).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 22** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_24`)


Dies gilt jedenfalls dann, wenn das für die Entscheidung über einen Rekurs gegen den Übertragungsbeschluss zuständige Gericht mit dem zur Genehmigung nach § 111 Abs 2 JN berufenen Gericht (hier der Oberste Gerichtshof) nicht ident ist (RS0047067 [T14]).

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 23** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie durch die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Hon.-Prof.in KzlR Iris Makowska, vertreten durch Skribe Rechtsanwaelte GmbH in Wien, gegen die beklagte Partei Dieter Apfelbacher Ltd, Am Fundbach 31w, 9170 Tratten, Österreich, wegen 400 EUR sA, über den Ordinationsantrag nach § 28 JN in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Hon.-Prof.in KzlR Iris Makowska` (person)
- `Skribe Rechtsanwaelte GmbH` (organisation)
- `Dieter Apfelbacher` (person)
- `Am Fundbach 31w, 9170 Tratten, Österreich` (address)
- `Bezirksgericht Schwechat` (organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_6`)


Rechtliche Beurteilung Nach § 28 Abs 1 Z 2 JN hat der Oberste Gerichtshof, wenn für eine bürgerliche Rechtssache die Voraussetzungen für die örtliche Zuständigkeit eines inländischen Gerichts im Sinne dieses Gesetzes oder einer anderen Rechtsvorschrift nicht gegeben oder nicht zu ermitteln sind, aus den sachlich zuständigen Gerichten eines zu bestimmen, welches für die fragliche Rechtssache als örtlich zuständig zu gelten hat, wenn unter anderem der Kläger österreichischer Staatsbürger ist oder seinen Wohnsitz, gewöhnlichen Aufenthalt oder Sitz im Inland hat und im Einzelfall die Rechtsverfolgung im Ausland nicht möglich oder unzumutbar wäre.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 25** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_7`)


Der Oberste Gerichtshof hat in gleich gelagerten Fällen (4 Nc 11/19h, 6 Nc 1/19b, 7 Nc 23/19w) die Ordination bewilligt.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 26** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Paulina Nüsken, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Oliver Eylart, Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Univ.-Prof. Dr. Neumayr` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Paulina Nüsken` (person)
- `Skribe Rechtsanwälte GmbH` (organisation)
- `Oliver Eylart` (person)
- `Bezirksgericht Schwechat` (organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_14`)


An die rechtskräftige Verneinung der internationalen Zuständigkeit des vom Kläger angerufenen Bezirksgerichts Schwechat ist der Oberste Gerichtshof gebunden (RIS-Justiz RS0046568).

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Bezirksgerichts Schwechat` (organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_16`)


Für den Fall, dass für eine bürgerliche Rechtssache die Voraussetzungen für die örtliche Zuständigkeit eines inländischen Gerichts nicht gegeben oder nicht zu ermitteln sind, bestimmt § 28 Abs 1 Z 2 JN, dass der Oberste Gerichtshof aus den sachlich zuständigen Gerichten eines zu bestimmen hat, welches für die fragliche Rechtssache als örtlich zuständig zu gelten hat, wenn der Kläger österreichischer Staatsbürger ist oder seinen Wohnsitz, gewöhnlichen Aufenthalt oder Sitz im Inland hat und im Einzelfall die Rechtsverfolgung im Ausland nicht möglich oder unzumutbar wäre.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 29** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_21`)


[7] 4.1 Der Oberste Gerichtshof hat Ordinationsanträgen bereits in einer Vielzahl von Entscheidungen stattgegeben, wenn der Kläger Ansprüche nach der EU-FluggastVO sonst in einem Drittstaat einklagen müsste und zwischen diesem Drittstaat und Österreich kein Vollstreckungsübereinkommen besteht (zB 6 Nc 1/19b ZVR 2019/114, 259 [Mayr];

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 30** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger und Hon.-Prof. Dr. Neumayr als weitere Richter in der Verlassenschaftssache nach dem am 9. September 2009 verstorbenen, zuletzt in Zum Wetterkreuz 15, 5121 Hofstadt, Österreich, wohnhaft gewesenen Manfred Johann Puff, AZ 1 A 349/09w des Bezirksgerichts Kitzbühel, über den Delegierungsantrag der Karin Ciliberto, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, den B e s c h l u s s gefasst:  Spruch Dem Delegierungsantrag wird stattgegeben.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Zum Wetterkreuz 15, 5121 Hofstadt, Österreich` (address)
- `Manfred Johann Puff` (person)
- `Bezirksgerichts Kitzbühel` (organisation)
- `Karin Ciliberto` (person)
- `Mag. Maximilian Kocher` (person)

**Example 31** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Steidlen+Ysner Daten GmbH, Kaminweg 34, 8200 Laßnitzthal, Österreich, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Verlag Waldlemder GmbH, Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

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
- `Landesgerichts Linz` (organisation)
- `Handelsgericht Wien` (organisation)

**Example 32** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_40`)


2.2. Die Ansicht vonMayr(Die Delegation im zivilgerichtlichen Verfahren, JBl 1983, 293 [299]; in diesem Sinn auchSchneiderinFasching/Konecny3§ 31 JN Rz 18), der Vereinbarung des Gerichtsstands oder des Erfüllungsorts sei kein größeres Gewicht beizumessen als der gesetzlichen Zuständigkeit, hat der Oberste Gerichtshof bereits abgelehnt (RIS-Justiz RS0046198 [T10]).

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 33** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Rechtssache der klagenden Partei Mur Dorftalnex Technologien -GmbH, Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich, vertreten durch Dr. Peter Lechner und Dr. Hermann Pfurtscheller, Rechtsanwälte in Innsbruck, und ihrer Nebenintervenientin Ober Dertri GmbH, Hintereggweg 93, 2070 Kleinhöflein, Österreich, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Rudolf Ketelhut GmbH, Fiebrichgasse 17, 5120 Seeleiten, Österreich, vertreten durch Rechtsanwaltskanzlei Dr. Bernhard Hämmerle GmbH in Innsbruck, und ihrer Nebenintervenientin Völkertz Energie GmbH, Brunnbachweg 19, 4653 Mayersdorf, Österreich, vertreten durch Dr. Franz Pechmann, Rechtsanwalt in Wien, wegen 696.238,34 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck vom 2. Oktober 2009, GZ 4 R 108/09b-167, mit dem das Urteil des Landesgerichts Innsbruck vom 23. Februar 2009, GZ 41 Cg 228/01z-152, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

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
- `Landesgerichts Innsbruck` (organisation)

**Example 34** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_54`)


1. Auf die Ausführungen der Revision, die sich gegen die dem Aufhebungsbeschluss zugrundeliegende rechtliche Beurteilung des Berufungsgerichts wenden, ist vom Obersten Gerichtshof mangels Bekämpfbarkeit des Aufhebungsbeschlusses derzeit nicht einzugehen.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 35** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Schneidergruberweg 37, 5132 Reith, Österreich, vertreten durch Dr. Alois Schneider, Rechtsanwalt in Rattenberg, wider die beklagte Partei Dario von Ebers, vertreten durch Dr. Walter Hausberger, Dr. Katharina Moritz und Dr. Alfred Schmidt, Rechtsanwälte in Wörgl, wegen Entfernung und Unterlassung (Revisionsinteresse 10.000 EUR), infolge Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 3. November 2017, GZ 3 R 172/17s-22, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Rattenberg vom 17. Mai 2017, GZ 3 C 401/15k-18, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

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
- `Landesgerichts Innsbruck` (organisation)
- `Bezirksgerichts Rattenberg` (organisation)

**Example 36** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_57`)


Das Berufungsgericht ließ die Revision mit der Begründung zu, dass keine Rechtsprechung des Obersten Gerichtshofs zu den Folgen der unterbliebenen Mitübertragung der Anmerkung des selbständigen Eigentums an Bäumen bestehe.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 37** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Bartholomäus Junghahn, geboren am 8. Mai 1999, und der minderjährigen HR Sophie Elefteriadis, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Bartholomäus Junghahn` (person)
- `HR Sophie Elefteriadis` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 38** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_22`)


Das Rekursgericht sprach aus, dass der ordentliche Revisionsrekurs zulässig sei, weil noch keine Rechtsprechung des Obersten Gerichtshofs zu der Bestimmung des § 3 Z 2 UVG idF FamRÄG 2009 vorliege.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 39** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Eva Abdelrahman, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei Hochenadel Immobilien GmbH, Ritterhof 11, 2661 Graben, Österreich, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
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

**Example 40** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_65`)


Die Klage wurde daher lange vor Ablauf der Verjährungsfrist eingebracht und der Fortsetzungsantrag rund sechs Monate nach dem Ablauf der ursprünglichen Verjährungsfrist gestellt. In der Entscheidung 6 Ob 822/81 (RIS-Justiz RS0034674) ist der Oberste Gerichtshof in einem Fall, in dem Ruhen des Verfahrens eingetreten war und beinahe ein Jahr nach Ablauf der dreijährigen Verjährungsfrist andauerte, von einer Verjährung mangels gehöriger Fortsetzung ausgegangen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 41** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Juri Gerstl GmbH, Mutten 18, 3251 Schauboden, Österreich, vertreten durch Dr. Ralph Trischler, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, sowie die Nebenintervenientin auf Seiten der beklagten Partei Bundesbeschaffung GmbH, 1020 Wien, Lassallestraße 9b, vertreten durch die Olischar Rechtsanwaltsgesellschaft mbH in Wien, wegen 15.535 EUR sA, über den Revisionsrekurs der klagenden Partei (Revisionsinteresse: 7.460 EUR), gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 23. Februar 2023, GZ 16 R 168/22a-20, mit welchem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 5. September 2022, GZ 11 Cg 48/22t-12, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Hon.-Prof. Dr. Lovrek` (person)
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

**Example 42** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_32`)


Nach ständiger Rechtsprechung des Obersten Gerichtshofs umfasst dieser Schadenersatzanspruch auch die Vertretungskosten im Zusammenhang mit einem auf Nichtigerklärung einer vergaberechtswidrigen Ausschreibung gerichteten Verfahren (RIS-Justiz RS0121198;

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 43** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Leander Lindlahr, geboren am 1. August 2011, und des mj Yussuf Prussog, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Leander Lindlahr` (person)
- `Yussuf Prussog` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)

**Example 44** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_20`)


Das Rekursgericht sprach aus, dass der ordentliche Revisionsrekurs gegen seine Entscheidung zulässig sei, weil noch keine Rechtsprechung des Obersten Gerichtshofs zum Wegfall der Exportverpflichtung bei Gewährung von Unterhaltsvorschüssen nach § 4 Z 3 UVG vorliege.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 45** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_23`)


Rechtliche Beurteilung Der Revisionsrekurs ist zulässig, weil noch keine Rechtsprechung des Obersten Gerichtshofs zu der über den Einzelfall hinaus bedeutsamen Rechtsfrage, ob die in einem anderen EU-Mitgliedstaat wohnhaften Kinder einen Anspruch auf österreichische Unterhaltsvorschüsse aufgrund der Bestimmungen der VO (EWG) 1612/68 bzw der neuen VO (EU) 492/2011 haben, vorliegt.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 46** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des minderjährigen Cedric Annamüller, geboren am 8. März 2007, 16. Mai 1964, vertreten durch das Land Kärnten als Kinder- und Jugendhilfeträger (Magistrat der Landeshauptstadt Klagenfurt, Abteilung für Jugend und Familie, Bahnhofstraße 35, 9010 Klagenfurt am Wörthersee), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Graz, gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 8. Jänner 2016, GZ 4 R 283/15g-16, womit der Beschluss des Bezirksgerichts Klagenfurt vom 17. November 2015, GZ 1 Pu 69/10x-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Ziegelbauer` (person)
- `Cedric Annamüller` (person)
- `8. März` (date)
- `16. Mai 1964` (date)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts Klagenfurt` (organisation)
- `Bezirksgerichts Klagenfurt` (organisation)

**Example 47** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_13`)


Mit dem angefochtenen Beschluss gab das Rekursgericht dem Rekurs des Bundes nicht Folge und sprach aus, dass der ordentliche Revisionsrekurs zulässig sei, weil Rechtsprechung des Obersten Gerichtshofs zur Frage fehle, inwiefern das Erstgericht bei der Weitergewährung von Unterhaltsvorschüssen von Amts wegen zu prüfen habe, ob dem Minderjährigen nach wie vor die Flüchtlingseigenschaft zukomme.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 48** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_23`)


Rechtliche Beurteilung Der Revisionsrekurs des Bundes ist entgegen dem den Obersten Gerichtshof nicht bindenden Ausspruch des Rekursgerichts (§ 71 Abs 1 AußStrG) mangels einer Rechtsfrage im Sinn des § 62 Abs 1 AußStrG nicht zulässig.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 49** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_30`)


Nach der Rechtsprechung des Obersten Gerichtshofs liegt ein Grund für die amtswegige Versagung der Weitergewährung auch darin, dass bei einer Vorschussgewährung nach § 4 Z 2 UVG vom Kind nicht alles Zumutbare zur Schaffung eines Unterhaltstitels unternommen worden ist (RIS-Justiz RS0076105: 10 Ob 48/10x;

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 50** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludmilla von Amelunxen, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, gegen die beklagte Partei Svetlana Leinhäuser, vertreten durch Dr. Thomas Brückl, Mag. Christian Breit, Rechtsanwälte in Ried im Innkreis, wegen 1.778,52 EUR und Unterlassung (Streitwert 2.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Wels als Berufungsgericht vom 25. Jänner 2023, GZ 21 R 2/23b-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Grieskirchen vom 27. Oktober 2022, GZ 3 C 642/20h-27, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

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
- `Landesgerichts Wels` (organisation)
- `Bezirksgerichts Grieskirchen` (organisation)

**Example 51** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_95`)


In einem solchen Fall kann der Oberste Gerichtshof durch Urteil in der Sache selbst erkennen (§ 519 Abs 2 Satz 3 ZPO), sodass der Beschluss des Berufungsgerichts aufzuheben und die klageabweisende Entscheidung des Erstgerichts wiederherzustellen war.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 52** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Mag. Kevin Maassen, vertreten durch Dr. Clemens Lintschinger, Rechtsanwalt in Wien, gegen die beklagte Partei Hon.-Prof. Friedhelm Adde, vertreten durch Mag. Dr. Georg Backhausen, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 27. Jänner 2016, GZ 38 R 265/15z-45, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Ziegelbauer` (person)
- `Mag. Kevin Maassen` (person)
- `Dr. Clemens Lintschinger` (person)
- `Hon.-Prof. Friedhelm Adde` (person)
- `Mag. Dr. Georg Backhausen` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 53** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_20`)


Dieser Fall liegt hier aber nach den den Obersten Gerichtshof bindenden Feststellungen nicht vor, weil der Beklagte - entgegen den Ausführungen des Revisionswerbers - die aufgekündigte Wohnungnichtregelmäßig zu Wohnzwecken verwendet, sondern lediglich sporadisch, als Absteigequartier.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 54** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_27`)


Ein Kostenersatz für die ohne Freistellung durch den Obersten Gerichtshof eingebrachte Revisionsbeantwortung steht der Klägerin nach § 508a Abs 2 Satz 2 ZPO nicht zu (RIS-Justiz RS0043690 [T6, T7]).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 55** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden, die Hofräte Mag. Schober, Dr. Annerl und Dr. Vollmaier sowie die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Ing. Mag. Pamela Gotterbauer, vertreten durch Mag. Helwig Schuster, Rechtsanwalt in Melk, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Hon.-Prof. Dr. Nowotny` (person)
- `Mag. Schober` (person)
- `Dr. Annerl` (person)
- `Dr. Vollmaier` (person)
- `Dr. Wallner-Friedl` (person)
- `Ing. Mag. Pamela Gotterbauer` (person)
- `Mag. Helwig Schuster` (person)

**Example 56** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_82`)


Es entspricht der ständigen Rechtsprechung des Obersten Gerichtshofs, dass Ansprüche aus verschiedenen Verträgen betreffend verschiedene Rechtsgüter auch bei Gleichartigkeit nicht in einem sachlichen oder rechtlichen Zusammenhang stehen (RS0037926 [T26]).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 57** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_100`)


Nach der Rechtsprechung des Obersten Gerichtshofs sei der Pferdeeinstellungsvertrag als entgeltlicher Verwahrungsvertrag zu werten, der nach seinem überwiegenden Charakter nicht als Bestandvertrag zu qualifizieren sei.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 58** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_144`)


Das Berufungsgericht hat – ausgehend von seiner vom Obersten Gerichtshof nicht geteilten Rechtsansicht – sowohl die Mängelrüge (Nichteinholung eines Gutachtens für den Bereich Pferdehaltung und Pferdesport) als auch die (auch) die Feststellungen zu den behaupteten Mängeln betreffende Beweisrüge der Berufung nicht erledigt, weshalb sein Verfahren mangelhaft geblieben ist.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 59** (doc_id: `deanon_260716_TRAIN/10Ob18_13i`) (sent_id: `deanon_260716_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei SüdSanitär Gruppe GmbH, Rinzendorf 28, 4501 Lindach, Österreich, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Verein für Konsumenteninformation` (organisation)
- `Dr. Walter Reichholf` (person)
- `SüdSanitär Gruppe GmbH` (organisation)
- `Rinzendorf 28, 4501 Lindach, Österreich` (address)
- `Kraft & Winternitz Rechtsanwälte GmbH` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 60** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Ralph Prusseit, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Akbayrak Metall GmbH, Schroateck 57, 4710 Niederweng, Österreich, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Hon.-Prof. Dr. Nowotny` (person)
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

**Example 61** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_56`)


Der Oberste Gerichtshof habe festgehalten, dass die Weigerung des Netzbenutzers, dem Netzbetreiber für einen geplanten Zählertausch Zutritt zu einem Objekt zu gewähren, es nicht rechtfertige, anstelle der Inanspruchnahme gerichtlicher Hilfe faktisch zur Selbsthilfe im Wege der (Androhung der) Stromabschaltung zu greifen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 62** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_75`)


[17]5.Der Oberste Gerichtshof hat zu 9 Ob 95/24x, 7 Ob 167/24w und 3 Ob 191/24w (betreffend vergleichbare AB-VN einer anderen Netzbetreiberin) dargelegt, dass die Weigerung des Netzbenutzers, der Netzbetreiberin Zugang zu seinem Objekt zu gewähren, damit sie einen (grundsätzlich funktionsfähigen) Stromzähler austauschen kann, qualitativ nicht den Fällen des Zahlungsverzugs und der Verweigerung einer Vorauszahlung oder Sicherheitsleistung gleichzuhalten sei.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 63** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Heimcon Software GmbH, H - Am Hang 3, 4912 Rettenbrunn, Österreich, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, gegen die beklagte Partei Gunter Landwirtschaft GmbH, Schlossfeld 38, 9300 Graßdorf, Österreich, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, wegen 7.731,06 EUR und Feststellung (Streitwert 20.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse insgesamt 11.597,42 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 216/14h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
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

**Example 64** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_50`)


4. 2011 enthaltenen Hinweise weitere Aufträge erteilt habe, werden keine Umstände aufgezeigt, die einen vom Obersten Gerichtshof aufzugreifenden Fehler in der Beurteilung des Berufungsgerichts, der nicht fachkundigen Klägerin könne kein Mitverschulden am Entstehen des Schadens angelastet werden, begründen könnten.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 65** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der minderjährigen Annabelle Thurnher, geboren am 24. Juni 2001, vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung, Bezirk 10, 1100 Wien, Van der Nüll-Gasse 20), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 17. September 2009, GZ 44 R 454/09d-38, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Favoriten vom 16. Juni 2009, GZ 40 P 36/08f-U-26, teilweise abgeändert wurde, den B e s c h l u s s gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Annabelle Thurnher` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 66** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei DDr.in Cornelia Rinaldo, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Conmon-Verlag Limited, Kroisegg 20, 4052 Fleckendorf, Österreich Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Univ.-Prof. Dr. Neumayr` (person)
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

**Example 67** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_9`)


Die Revision der Beklagten ist entgegen dem – den Obersten Gerichtshof nicht bindenden – Zulassungsausspruch mangels Vorliegens einer Rechtsfrage von erheblicher Bedeutung im Sinn des § 502 Abs 1 ZPO nicht zulässig.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 68** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_11`)


Das Vorliegen einer Rechtsfrage von erheblicher Bedeutung ist nach dem Zeitpunkt der Entscheidung über das Rechtsmittel durch den Obersten Gerichtshof zu beurteilen.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 69** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_12`)


Eine im Zeitpunkt der Einbringung des Rechtsmittels tatsächlich aufgeworfene erhebliche Rechtsfrage fällt somit weg, wenn sie vor der Erledigung des Rechtsmittels bereits durch eine andere Entscheidung des Obersten Gerichtshofs geklärt wurde (RS0112921 [T5]).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 70** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_15`)


2010 geltenden Fassung des GSpG hat der Oberste Gerichtshof bereits in der – einen nahezu identen Sachverhalt betreffenden – Entscheidung 6 Ob 229/21a klargestellt, dass zwar das in § 21 Abs 2 Z 1 GSpG (bzw § 14 Abs 2 Z 1 GSpG) idF vor dem Budgetbegleitgesetz 2011 normierte Sitzerfordernis unionsrechtswidrig war und nach der Rechtsprechung des EuGH ein Mitgliedstaat keine (verwaltungs-)strafrechtlichen Sanktionen wegen einer nicht erfüllten Verwaltungsformalität verhängen darf, wenn er die Erfüllung dieser Formalität unter Verstoß gegen das Unionsrecht abgelehnt oder vereitelt hat, dass aber dieser Grundsatz schon deshalb nicht auf die vorliegende Konstellation übertragbar ist, weil die „Nichtigkeitssanktion“ im Sinn des § 879 Abs 1 ABGB keine vergleichbare staatliche Sanktion repressiver Natur darstellt. Weiters führte der Oberste Gerichtshof in der zitierten Entscheidung 6 Ob 229/21a aus, dass die zivilrechtliche Unerlaubtheit des Spiels eine Strafbarkeit im Sinn des § 168 StGB nicht voraussetzt (4 Ob 70/22f mwH; RS0102178 [T10]).

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 71** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_20`)


Der Oberste Gerichtshof hat mittlerweile auch die Passivlegitimation der Beklagten für den vom Kläger mit Leistungskondiktion begehrten Ersatz seiner Spielverluste aus Online-Pokerspielen in vergleichbaren Verfahren bereits mehrfach bejaht (6 Ob 229/21a;

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 72** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der Kinder 1.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)

**Example 73** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_59`)


2.2 In der – bereits von den Vorinstanzen zitierten und verwerteten – Entscheidung 1 Ob 158/15i hat der Oberste Gerichtshof das folgende, in der Entscheidung 8 Ob 89/17x fortgeschriebene Modell für die Festsetzung des Differenzunterhalts entwickelt: Zunächst ist der fiktive Geldunterhaltsanspruch des Kindes gegen jeden Elternteil nach der Prozentmethode – bei weit überdurchschnittlichem Einkommen des besser verdienenden Elternteils unter Bedachtnahme auf die sogenannte Luxusgrenze – zu ermitteln.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 74** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_78`)


NeuhausersErgebnis beträgt 261 EUR, jenes des Obersten Gerichtshofs 252 EUR, wobei der Unterhaltsbetrag gerundet mit 260 EUR festgesetzt wurde.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 75** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_84`)


Senats des Obersten Gerichtshofs zufolge § 231 Abs 2 Satz 2 ABGB in Fällen als problematisch, in denen ein Elternteil nichts oder unterhalb des Existenzminimums verdient.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 76** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr.Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei AXA Software Institut Gesellschaft mbH, Fuchsgrabengasse 27K, 8330 Untergiem, Österreich, vertreten durch Mag. Oliver Simoncic, Rechtsanwalt in St. Pölten, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr.Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Korn` (person)
- `AXA Software Institut Gesellschaft mbH` (organisation)
- `Fuchsgrabengasse 27K, 8330 Untergiem, Österreich` (address)
- `Mag. Oliver Simoncic` (person)

**Example 77** (doc_id: `deanon_260716_TRAIN/10Ob26_10m`) (sent_id: `deanon_260716_TRAIN/10Ob26_10m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der mj 1.)

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)

**Example 78** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei James Jooß, vertreten durch Dr. Klaus Schiller, Rechtsanwalt in Schwanenstadt, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `James Jooß` (person)
- `Dr. Klaus Schiller` (person)

**Example 79** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_79`)


Rechtliche Beurteilung DieRevisionist entgegen dem - den Obersten Gerichtshof nicht bindenden (§ 508 Abs 1 ZPO) - Ausspruch des Berufungsgerichts zulässig, weil das Berufungsgericht von der ständigen Rechtsprechung des Obersten Gerichtshofs zur Beurteilung von Kündigungserklärungen abweicht;

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 80** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_108`)


Dabei wird übersehen, dass im Rechtsmittelverfahren vor dem Obersten Gerichtshof Verweise in der Revision bzw Revisionsbeantwortung auf Ausführungen in anderen Schriftsätzen (zB der Berufung) nach ständiger Rechtsprechung unzulässig und unbeachtlich sind (RIS-Justiz RS0043579 und RS0043616; vgl auch RS0007029).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 81** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Brigitte Martz, geboren am 16. November 1978, wegen Kontaktrechts des Vaters Dr. Gustav Thöning, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Madeleine Musialik, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Missed by this rule (FN):**

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
- `Landesgerichts Wiener Neustadt` (organisation)
- `Bezirksgerichts Wiener Neustadt` (organisation)

**Example 82** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_4`)


Begründung:  Rechtliche Beurteilung Der Oberste Gerichtshof befasste sich in seinem Aufhebungsbeschluss vom 13.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 83** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_39`)


2.1 Der gegen den abändernden Teil der Rekursentscheidung gerichtete – nach Freistellung durch den Obersten Gerichtshof vomVater beantwortete– Revisionsrekurs ist hingegen zulässig und im Sinne einer Aufhebung berechtigt.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 84** (doc_id: `deanon_260716_TRAIN/10Ob28_19v`) (sent_id: `deanon_260716_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Bau Zorostfurt GmbH, Isbarystraße 47, 4152 Schölling, Österreich, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Buitenkamp und Rothauge Landwirtschaft GmbH, Gewerbegebiet Mathon 17, 3672 Reitern, Österreich, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Univ.-Prof. Dr. Neumayr` (person)
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

**Example 85** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der zur AZ 38 Nc 13/08i beim Landesgericht für Zivilrechtssachen Wien anhängigen Ablehnungssache des Ablehnungswerbers Mag. Herwig Bortzlaff, über den Rekurs des Ablehnungswerbers gegen den Beschluss des Oberlandesgerichts Wien vom 10. November 2009, GZ 13 Nc 14/09x-2, womit ein Ablehnungsantrag zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Landesgericht für Zivilrechtssachen Wien` (organisation)
- `Mag. Herwig Bortzlaff` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 86** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_16`)


Die Verhängung der Ordnungsstrafe hingegen sei grundsätzlich durch Rekurs an den Obersten Gerichtshof bekämpfbar.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 87** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_19`)


Mit dem dagegen erhobenen Rekurs an den Obersten Gerichtshof verband der Rechtsmittelwerber einen Ablehnungsantrag gegen die Vorsitzende und die beiden weiteren Mitglieder des 13.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 88** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_25`)


Der Beschluss ist daher, da dem Ablehnungsantrag nicht stattgegeben wurde, gemäß § 24 Abs 2 JN uneingeschränkt an den Obersten Gerichtshof anfechtbar.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 89** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_27`)


Vor Eingehen auf das Rechtsmittel selbst ist vorerst die Frage zu prüfen, ob die Rekursschrift von einem Rechtsanwalt zu fertigen und daher durch den Obersten Gerichtshof das Verbesserungsverfahren einzuleiten wäre.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 90** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_31`)


Das Oberlandesgericht Wien hat funktionell als Erstgericht entschieden, der Oberste Gerichtshof entscheidet daher im vorliegenden Fall als Rekursgericht.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)

**Example 91** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_34`)


Soweit der Rechtsmittelwerber in seinem Rekurs ohne nähere Substantiierung „alle als befangen angezeigten Richter des Obersten Gerichtshofs" ablehnt, sieht sich der erkennende Senat nicht veranlasst, die pauschale Ablehnung derjenigen seiner Mitglieder, die bereits früher in Rechtssachen des Rechtsmittelwerbers entschieden haben, zum Gegenstand einer Entscheidung des für Ablehnungen zuständigen Senats des Obersten Gerichtshofs zu machen (vgl RIS-Justiz RS0111658).

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |
| `Obersten Gerichtshofs` | `Obersten Gerichtshofs` |

**Example 92** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Jaden Meyerjohann, geboren am 3. Juli 2020, Leroy Jungschmidt, geboren am 28. Mai 1965 und Clemens Theocharakis, geboren am 25. März 1999, in Pflege und Erziehung der Mutter Emanuela Janischefsky, vertreten durch das Land Vorarlberg als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Feldkirch, Schlossgraben 1, 6800 Feldkirch), wegen Gewährung von Unterhaltsvorschuss, über den Revisionsrekurs des Vaters Ashley Biesert, vertreten durch Mag. Hans-Christian Obernberger, Rechtsanwalt in Feldkirch, gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 12. Juli 2011, GZ 3 R 198/11g, 3 R 199/11d, 3 R 200/11a-18, womit die Beschlüsse des Bezirksgerichts Feldkirch vom 18. Mai 2011, GZ 12 Pu 141/11f-4 bis 6, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

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
- `Landesgerichts Feldkirch` (organisation)
- `Bezirksgerichts Feldkirch` (organisation)

**Example 93** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_19`)


Nach Vorlage des Revisionsrekurses stellte der Oberste Gerichtshof mit Beschluss vom 25.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 94** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_26`)


Mit Beschluss des Erstgerichts vom 29. 11. 2013 (zugestellt am 9. 12. 2013) wurde dem Vertreter des Vaters in der Folge auch der ordentliche Revisionsrekurs „vom31. 1. 2013(ON 82)“ zur Verbesserung binnen 14 Tagen (gemäß dem Beschluss 10 Ob 29/13g [ON 93]) zurückgestellt. Den am 10. 12. 2013 im ERV eingebrachten verbesserten Revisionsrekurs legt das Erstgericht neuerlich dem Obersten Gerichtshof zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 95** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_35`)


das ordentliche Rechtsmittel ist jedoch entgegen dem - gemäß § 71 Abs 1 AußStrG den Obersten Gerichtshof nicht bindenden - Ausspruch des Rekursgerichts wegen Fehlens einer erheblichen Rechtsfrage nicht zulässig.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 96** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_54`)


3. Entgegen den Ausführungen zur Zulässigkeit des Revisionsrekurses hat sich der Oberste Gerichtshof bereits ausdrücklich mit der Frage befasst, ob die (wenn auch nur mögliche) Anwendung europäischen Primär- und Sekundärrechtes oder völkerrechtlicher Abkommen der EU mit anderen Staaten (unabhängig davon, ob eine „schwierige Rechtsfrage“ zu lösen ist) dem Begriff „ausländisches Recht“ im Sinn des § 16 Abs 2 Z 6 RpflG zuzurechnen ist und demgemäß auch dem Richtervorbehalt unterliegt.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Example 97** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch und Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der minderjährigen Karsten Alberter, geboren am 2. April 2010, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Wien-Umgebung, Fachgebiet Jugendwohlfahrt), 3400 Klosterneuburg, Leopoldstraße 21, über das als „Berufung“ bezeichnete Rechtsmittel des Vaters Helmut Dreilich, gegen den Beschluss des Landesgerichts Korneuburg als Rekursgericht vom 25. März 2013, GZ 23 R 30/13v-53, womit der Beschluss des Bezirksgerichts Schwechat vom 27. August 2012, GZ 8 Pu 190/11i-39, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.  Text Begründung: Verfahrensgegenstand ist die Festsetzung des gesetzlichen Unterhalts für die mj Lena Amini.

| Predicted | Gold |
|---|---|
| `Oberste Gerichtshof` | `Oberste Gerichtshof` |

**Missed by this rule (FN):**

- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Karsten Alberter` (person)
- `2. April 2010` (date)
- `Helmut Dreilich` (person)
- `Landesgerichts Korneuburg` (organisation)
- `Bezirksgerichts Schwechat` (organisation)
- `Lena Amini` (person)

**Example 98** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_10`)


Das Erstgericht wertete dieses Rechtsmittel als außerordentlichen Revisionsrekurs und ging davon aus, dass dieser sogleich dem Obersten Gerichtshof vorzulegen sei.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

**Example 99** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_15`)


Daraufhin legte das Erstgericht das Rechtsmittel dem Obersten Gerichtshof zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Obersten Gerichtshof` | `Obersten Gerichtshof` |

</details>

---

## `Oberlandesgericht_City` 🏆

**F1:** 0.170 | **Precision:** 1.000 | **Recall:** 0.093  

**Format:** `regex`  
**Rule ID:** `7d387332`  
**Description:**
Matches Regional High Courts with city names, ensuring 'Graz' is included.

**Content:**
```
\bOberlandesgerichts?\s+(?:Wien|Linz|Innsbruck|Salzburg|Graz|Klagenfurt|Eisenstadt|St.\s+Pölten|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|Linz)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.093 | 0.170 | 373 | 373 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 373 | 0 | 3507 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Rechtssache der klagenden Partei Mur Dorftalnex Technologien -GmbH, Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich, vertreten durch Dr. Peter Lechner und Dr. Hermann Pfurtscheller, Rechtsanwälte in Innsbruck, und ihrer Nebenintervenientin Ober Dertri GmbH, Hintereggweg 93, 2070 Kleinhöflein, Österreich, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Rudolf Ketelhut GmbH, Fiebrichgasse 17, 5120 Seeleiten, Österreich, vertreten durch Rechtsanwaltskanzlei Dr. Bernhard Hämmerle GmbH in Innsbruck, und ihrer Nebenintervenientin Völkertz Energie GmbH, Brunnbachweg 19, 4653 Mayersdorf, Österreich, vertreten durch Dr. Franz Pechmann, Rechtsanwalt in Wien, wegen 696.238,34 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck vom 2. Oktober 2009, GZ 4 R 108/09b-167, mit dem das Urteil des Landesgerichts Innsbruck vom 23. Februar 2009, GZ 41 Cg 228/01z-152, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Innsbruck` | `Oberlandesgerichts Innsbruck` |

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
- `Landesgerichts Innsbruck` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Bartholomäus Junghahn, geboren am 8. Mai 1999, und der minderjährigen HR Sophie Elefteriadis, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Bartholomäus Junghahn` (person)
- `HR Sophie Elefteriadis` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_23`)


Gegen die Entscheidung des Rekursgerichts richtet sich der Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, mit dem Antrag, den angefochtenen Beschluss im Sinne einer Wiederherstellung der Beschlüsse des Erstgerichts abzuändern.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 3** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Eva Abdelrahman, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei Hochenadel Immobilien GmbH, Ritterhof 11, 2661 Graben, Österreich, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

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
- `Lederer Rechtsanwalt GmbH` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Juri Gerstl GmbH, Mutten 18, 3251 Schauboden, Österreich, vertreten durch Dr. Ralph Trischler, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, sowie die Nebenintervenientin auf Seiten der beklagten Partei Bundesbeschaffung GmbH, 1020 Wien, Lassallestraße 9b, vertreten durch die Olischar Rechtsanwaltsgesellschaft mbH in Wien, wegen 15.535 EUR sA, über den Revisionsrekurs der klagenden Partei (Revisionsinteresse: 7.460 EUR), gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 23. Februar 2023, GZ 16 R 168/22a-20, mit welchem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 5. September 2022, GZ 11 Cg 48/22t-12, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Mag. Schober` (person)
- `Dr. Thunhart` (person)
- `Juri Gerstl` (person)
- `Mutten 18, 3251 Schauboden, Österreich` (address)
- `Dr. Ralph Trischler` (person)
- `Bundesbeschaffung GmbH` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Leander Lindlahr, geboren am 1. August 2011, und des mj Yussuf Prussog, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Leander Lindlahr` (person)
- `Yussuf Prussog` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_17`)


DasRekursgerichtgab dem Rekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, Folge und wies den Unterhaltsvorschussantrag der beiden Kinder ab.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 7** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_22`)


Der Bund, vertreten durch den Präsidenten des Oberlandesgerichts Wien, beantragt in seiner Revisionsrekursbeantwortung, den Revisionsrekurs zurückzuweisen bzw ihm keine Folge zu geben.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 8** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des minderjährigen Cedric Annamüller, geboren am 8. März 2007, 16. Mai 1964, vertreten durch das Land Kärnten als Kinder- und Jugendhilfeträger (Magistrat der Landeshauptstadt Klagenfurt, Abteilung für Jugend und Familie, Bahnhofstraße 35, 9010 Klagenfurt am Wörthersee), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Graz, gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 8. Jänner 2016, GZ 4 R 283/15g-16, womit der Beschluss des Bezirksgerichts Klagenfurt vom 17. November 2015, GZ 1 Pu 69/10x-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Graz` | `Oberlandesgerichts Graz` |

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
- `Landesgerichts Klagenfurt` (organisation)
- `Bezirksgerichts Klagenfurt` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Heimcon Software GmbH, H - Am Hang 3, 4912 Rettenbrunn, Österreich, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, gegen die beklagte Partei Gunter Landwirtschaft GmbH, Schlossfeld 38, 9300 Graßdorf, Österreich, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, wegen 7.731,06 EUR und Feststellung (Streitwert 20.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse insgesamt 11.597,42 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 216/14h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Linz` | `Oberlandesgerichts Linz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Korn` (person)
- `Heimcon Software GmbH` (organisation)
- `H - Am Hang 3, 4912 Rettenbrunn, Österreich` (address)
- `Vavrovsky Heine Marth Rechtsanwälte GmbH` (organisation)
- `Gunter Landwirtschaft GmbH` (organisation)
- `Schlossfeld 38, 9300 Graßdorf, Österreich` (address)
- `Stolz & Schartner Rechtsanwälte GmbH` (organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei DDr.in Cornelia Rinaldo, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Conmon-Verlag Limited, Kroisegg 20, 4052 Fleckendorf, Österreich Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

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
- `Brandl Talos Rechtsanwälte GmbH` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_4`)


Enns-Umwelt Consulting Limited, Alpineweg 221, 5730 Jochbergthurn, Österreich, 2. Ing. Lara Markart, letztere vertreten durch Radel Stampf Supper Rechtsanwälte OG in Mattersburg, wegen 160.422,79 EUR sA, infolge Revision der klagenden Partei (Revisionsinteresse 107.422,79 EUR sA) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Jänner 2015, GZ 4 R 119/14w-32, womit das Urteil des Landesgerichts St. Pölten vom 25. April 2014, GZ 37 Cg 96/13f-28, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Enns-Umwelt` (organisation)
- `Alpineweg 221, 5730 Jochbergthurn, Österreich` (address)
- `Ing. Lara Markart` (person)
- `Radel Stampf Supper Rechtsanwälte OG` (organisation)
- `Landesgerichts St. Pölten` (organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_5`)


Unter Alver GmbH, beide Granglitzweg 11, 3251 Kroißenberg, Österreich, beide vertreten durch Dr. Michael Schneditz-Bolfras und andere Rechtsanwälte in Gmunden, wegen Bucheinsicht (in eventu Rechnungslegung) und Zahlung (Streitwert: 70.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Teilurteil des Oberlandesgerichts Linz als Berufungsgericht vom 17. Februar 2014, GZ 3 R 13/14y-90, womit das Urteil des Landesgerichts Wels vom 27. November 2013 (in der mit Beschluss vom 12. Dezember 2013 berichtigten Fassung), GZ 2 Cg 78/10p-82 und -84, abgeändert wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Linz` | `Oberlandesgerichts Linz` |

**Missed by this rule (FN):**

- `Unter Alver GmbH` (organisation)
- `Granglitzweg 11, 3251 Kroißenberg, Österreich` (address)
- `Dr. Michael Schneditz-Bolfras` (person)
- `Landesgerichts Wels` (organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/10Ob28_19v`) (sent_id: `deanon_260716_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Bau Zorostfurt GmbH, Isbarystraße 47, 4152 Schölling, Österreich, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Buitenkamp und Rothauge Landwirtschaft GmbH, Gewerbegebiet Mathon 17, 3672 Reitern, Österreich, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Linz` | `Oberlandesgerichts Linz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
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

**Example 14** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der zur AZ 38 Nc 13/08i beim Landesgericht für Zivilrechtssachen Wien anhängigen Ablehnungssache des Ablehnungswerbers Mag. Herwig Bortzlaff, über den Rekurs des Ablehnungswerbers gegen den Beschluss des Oberlandesgerichts Wien vom 10. November 2009, GZ 13 Nc 14/09x-2, womit ein Ablehnungsantrag zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Landesgericht für Zivilrechtssachen Wien` (organisation)
- `Mag. Herwig Bortzlaff` (person)

**Example 15** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_8`)


Dem gegen diesen Beschluss vom Ablehnungswerber erhobenen Rekurs gab das Oberlandesgericht Wien durch seinen 11.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Example 16** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_11`)


Senats des Oberlandesgerichts Wien wegen Befangenheit ab.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_13`)


Senat des Oberlandesgerichts Wien in der Besetzung Senatspräsidentin Dr. Paolo Barley sowie Mag. Klarissa Hausteiner und Mag. Viola Brauch als weitere Richter den Ablehnungsantrag des Ablehnungswerbers vom 24. 8. 2009 zurück.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Dr. Paolo Barley` (person)
- `Mag. Klarissa Hausteiner` (person)
- `Mag. Viola Brauch` (person)

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_14`)


Es wurde darauf hingewiesen, dass die Entscheidung des Oberlandesgerichts Wien vom 3. 8. 2009, AZ 11 R 105/09f, im Umfang der Bestätigung der Zurückweisung des Ablehnungsantrags bereits in Rechtskraft erwachsen sei.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 19** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_17`)


Eine Ablehnung der Richter des die Ordnungsstrafe verhängenden Rekurssenats des Oberlandesgerichts Wien sei daher grundsätzlich möglich.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 20** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_20`)


Senats des Oberlandesgerichts Wien, die über seine Ablehnungserklärung entschieden haben.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 21** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_22`)


Senat des Oberlandesgerichts Wien (AZ 12 Nc 44/09a) entschieden, dass dieser offenbar rechtsmissbräuchlich erhobene Ablehnungsantrag nicht zum Gegenstand einer gerichtlichen Entscheidung gemacht werden müsse.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 22** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_24`)


Vorauszuschicken ist, dass das Oberlandesgerichts Wien nicht einen Beschluss im Rechtsmittelverfahren gefasst hat, sondern als Erstgericht entschieden hat.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 23** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_31`)


Das Oberlandesgericht Wien hat funktionell als Erstgericht entschieden, der Oberste Gerichtshof entscheidet daher im vorliegenden Fall als Rekursgericht.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_36`)


Senats des Oberlandesgerichts Wien aufzuzeigen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 25** (doc_id: `deanon_260716_TRAIN/10Ob30_19p`) (sent_id: `deanon_260716_TRAIN/10Ob30_19p_22`)


DasRekursgerichtgab dem Rekurs des Präsidenten des Oberlandesgerichts Wien teilweise Folge und reduzierte die gewährten Unterhaltsvorschüsse auf 150 EUR monatlich.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 26** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende, den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber sowie die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Leander Andermann, vertreten durch Dr. Martin Leitner, Rechtsanwalt in Wien, gegen die beklagte Partei Ing. Ferdinand Abramova, vertreten durch Mag. Wilhelm Deutschmann MBA und Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M., Rechtsanwälte in Linz, wegen 500.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 11. Mai 2022, GZ 2 R 64/22b-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Linz` | `Oberlandesgerichts Linz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Mag. Schober` (person)
- `Dr. Annerl` (person)
- `Leander Andermann` (person)
- `Dr. Martin Leitner` (person)
- `Ing. Ferdinand Abramova` (person)
- `Mag. Wilhelm Deutschmann MBA` (person)
- `Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M.` (person)

**Example 27** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

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
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Ziegelbauer als Vorsitzenden sowie die Hofrätin Dr. Faber und die Hofräte Mag. Schober, Dr. Thunhart und Dr. Annerl als weitere Richter in der Pflegschaftssache der minderjährigen Meinrad Bruhnsen, geboren 30. Januar 2006, vertreten durch das Land Wien als Träger der Kinder- und Jugendhilfe (Magistrat der Stadt Wien, Rechtsvertretung Bezirke 1, 4 bis 9, 1060 Wien, Amerlingstraße 11), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch die Präsidentin des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 31. Oktober 2022, GZ 43 R 323/22a-17, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 9. Juni 2022, GZ 4 Pu 58/22a-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Mag. Schober` (person)
- `Dr. Thunhart` (person)
- `Dr. Annerl` (person)
- `Meinrad Bruhnsen` (person)
- `30. Januar` (date)
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Innere Stadt Wien` (organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_5`)


Dr. Felix Cornils, Niederlande, beide vertreten durch Tramposch & Partner, Rechtsanwälte KG in Innsbruck, gegen die beklagte Partei Mag.a Constanze Rizzo, vertreten durch König Ermacora Klotz & Partner, Rechtsanwälte in Innsbruck, wegen je 15.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 1. Juli 2020, GZ 10 R 16/20h-49, mit dem das Urteil des Landesgerichts Innsbruck vom 6. Februar 2020, GZ 41 Cg 11/19i-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Innsbruck` | `Oberlandesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Dr. Felix Cornils` (person)
- `Tramposch & Partner, Rechtsanwälte KG` (organisation)
- `Mag.a Constanze Rizzo` (person)
- `Landesgerichts Innsbruck` (organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Pflegschaftssache 1. der mj Emma Mittelstaedt, geboren am 21. Mai 2025 und 2. des mj Milena Roesche, geboren am 25. Juni 1957, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung Bezirk 22, 1220 Wien, Hirschstettner Straße 19-21/Stiege N), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 10. Dezember 2014, GZ 42 R 343/13x, 42 R 344/13v und 42 R 345/13s-106, womit den Rekursen der Minderjährigen gegen den Beschluss des Bezirksgerichts Donaustadt vom 14. März 2013, GZ 3 Pu 61/12x-40, teilweise Folge gegeben wurde (Pkt 1 des Spruchs), dem Rekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen die Beschlüsse des Bezirksgerichts Donaustadt (jeweils) vom 6. Juni 2013, GZ 3 Pu 61/12x-49 und 3 Pu 61/12x-50, Folge gegeben (Pkt 2a des Spruchs), und aus Anlass des Rekurses die Anträge der Minderjährigen auf Gewährung von Unterhaltsvorschüssen zur Gänze abgewiesen wurden (Pkt 2b des Spruchs), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

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
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_14`)


Das Erstgericht legte dem Rekursgericht die gegen den abweislichen Teil des Titelbeschlusses erhobenen Rekurse der Minderjährigen sowie den vom Präsidenten des Oberlandesgerichts Wien erhobenen Rekurs gegen die Bewilligung von Unterhaltsvorschüssen für den Monat April 2013 zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 32** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_26`)


Unter einem gab das Rekursgericht dem Rekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, Folge und wies die Anträge der beiden Minderjährigen auf Gewährung von Unterhaltsvorschüssen für den Monat April 2013 ab (Punkt 2a des Spruchs).

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 33** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_38`)


Im Hinblick darauf, dass im vorliegenden Fall erst nachträglich bekannt geworden sei, dass ein Zustellmangel vorliege und der Wegfall der Rechtskraft des Unterhaltstitels den im § 7 UVG genannten Umständen zumindest vergleichbar sei, erscheine aus Anlass des Rekurses des Präsidenten des Oberlandesgerichts Wien eine bis zum Beginn der Vorschussbewilligung rückwirkende Wahrnehmung zulässig.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 34** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_69`)


Mangels Anfechtung durch den Präsidenten des Oberlandesgerichts Wien sind die erstinstanzlichen Gewährungsbeschlüsse betreffend den Zeitraum ab 1. 5. 2013 in (Teil-)Rechtskraft erwachsen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 35** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_71`)


Wenn das Rekursgericht dennoch aus Anlass des vom Präsidenten des Oberlandesgerichts Wien hinsichtlich des Monats April 2013 erhobenen Rekurses die (rechtskräftigen) erstgerichtlichen Gewährungsbeschlüsse zum Nachteil der beiden Minderjährigen (also zu Ungunsten der den Beschlussnichtanfechtenden Parteien) dahingehend abgeändert hat, dass deren Anträge auf Gewährung von Unterhaltsvorschüssen zur Gänze abgewiesen wurden, hat es seine Kognitionsbefugnis überschritten.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 36** (doc_id: `deanon_260716_TRAIN/10Ob43_19z`) (sent_id: `deanon_260716_TRAIN/10Ob43_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Othmar Mertl, vertreten durch Nitsch Pajor Zöllner Rechtsanwälte OG in Mödling, gegen die beklagte Partei Stadtgemeinde Malik Fridt, vertreten durch Krist Bubits Rechtsanwälte OG in Mödling, wegen 1.) 21.216,92 EUR sA und 2.) Feststellung (Streitwert: 2.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Februar 2019, GZ 12 R 96/18b-36, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Wiener Neustadt vom 31. August 2018, GZ 20 Cg 86/17h-31, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

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
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 37** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und den Hofrat Dr. Schramm, die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin Scarlett Achatzi, gegen den Antragsgegner Mag. Ewald Aszmutat, wegen Unterhalt, infolge Rekurses des Antragsgegners gegen den Beschluss des Oberlandesgerichts Wien vom 4. Jänner 2017, GZ 12 Nc 28/16h-3, womit der Ablehnungsantrag des Antragsgegners zurückgewiesen wurde, sowie über den Ablehnungsantrag gegen alle Richter des Oberlandesgerichts Wien, folgenden Beschluss gefasst:  Spruch 1.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Scarlett Achatzi` (person)
- `Mag. Ewald Aszmutat` (person)

**Example 38** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_4`)


Der Ablehnungsantrag gegen alle Richter des Oberlandesgerichts Wien wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 39** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_16`)


Gegen diesen Beschluss richtet sich der Rekurs des Antragsgegners, verbunden mit einem Ablehnungsantrag wegen Befangenheit aller Richterinnen und Richter des Oberlandesgerichts Wien.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 40** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_17`)


Rechtliche Beurteilung 1.Zur Ablehnung sämtlicher Richterinnen und Richter des Oberlandesgerichts Wien: Auch als Begründung für den Ablehnungsantrag wegen Befangenheit aller Richterinnen und Richter des Oberlandesgerichts Wien führt der Ablehnungswerber aus, es sei im (seine Tochter betreffenden) Pflegschaftsverfahren zu kriminellen Handlungen, insbesondere zu Hochverrat nach § 242 StGB gekommen, wodurch sowohl ihm als auch seiner Tochter unwiederbringlicher Schaden an Lebensqualität und persönlicher Identität verursacht worden sei.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 41** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_18`)


Nicht nur die Mitglieder des an der Entscheidung beteiligten Senats des Oberlandesgerichts Wien, sondern alle Richter dieses Gerichts seien am Hochverrat an der Republik Österreich, an ihm selbst sowie seiner Tochter beteiligt.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 42** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_21`)


Da der Ablehnungswerber alle Richterinnen und Richter des Oberlandesgerichts Wien ablehnt, ist der Oberste Gerichtshof zur Entscheidung berufen (RIS-Justiz RS0045997).

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_26`)


Inwiefern die Mitglieder des an der Entscheidung beteiligten Senats des Oberlandesgerichts Wien, aber auch alle anderen Richter und Richterinnen dieses Gerichtshofs den Tatbestand des Hochverrats nach § 242 StGB erfüllt haben sollten – indem sie es unternommen hätten, mit Gewalt oder durch Drohung mit Gewalt die Verfassung der Republik Österreich oder eines ihrer Bundesländer zu ändern oder ein zur Republik Österreich gehörendes Gebiet abzutrennen –, wird im Ablehnungsantrag nicht näher begründet und ausgeführt.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 44** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_28`)


2. DerRekursgegen den Beschluss des Oberlandesgerichts Wien vom 4. Jänner 2017 ist zulässig (§ 24 Abs 2 JN; RIS-Justiz RS0043830);

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 45** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_32`)


2.2 Von diesen Grundsätzen der Rechtsprechung ist das Oberlandesgericht Wien bei seiner Entscheidung nicht abgewichen, wenn es den Ablehnungsantrag gegen alle Richter und Richterinnen des Landesgerichts für Zivilrechtssachen Wien und des Bezirksgerichts Josefstadt als nicht dem Gesetz gemäß ausgeführt zurückgewiesen hat.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Missed by this rule (FN):**

- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Josefstadt` (organisation)

**Example 46** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Cassandra Wespi, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Bilek Lebensmittel GmbH in Liqu, Dreijochgasse 11, 4722 Stefansdorf, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `DI Cassandra Wespi` (person)
- `Vogl Rechtsanwalt GmbH` (organisation)
- `Bilek Lebensmittel GmbH` (organisation)
- `Dreijochgasse 11, 4722 Stefansdorf, Österreich` (address)
- `Wess Kux Kispert & Eckert Rechtsanwalts GmbH` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 47** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Ing. Christian Stangl-Brachnik, MA BA und Mag. Claudia Gründel (beide aus dem Kreis der Arbeitgeber) als weitere Richter in der Sozialrechtssache der klagenden Partei Mathias Jendl, vertreten durch Dr. Thomas Stampfer und Dr. Christoph Orgler, Rechtsanwälte in Graz, gegen die beklagte Partei Sozialversicherungsanstalt der Bauern, 1031 Wien, Ghegastraße 1, vertreten durch Dr. Michael Stögerer, Rechtsanwalt in Wien, wegen Ausgleichszulage, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2017, GZ 7 Rs 37/17s-11, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. April 2017, GZ 43 Cgs 113/17p-7, teils bestätigt und teils abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Graz` | `Oberlandesgerichts Graz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Ing. Christian Stangl-Brachnik, MA BA` (person)
- `Mag. Claudia Gründel` (person)
- `Mathias Jendl` (person)
- `Dr. Thomas Stampfer` (person)
- `Dr. Christoph Orgler` (person)
- `Dr. Michael Stögerer` (person)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)

**Example 48** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, den Hofrat Dr. Fellinger und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter KR Hermann Furtner (aus dem Kreis der Arbeitgeber) und AR Angelika Neuhauser (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Birgit Jaros, vertreten durch Dr. Herbert Pochieser, Rechtsanwalt in Wien, gegen die beklagte Partei Wiener Gebietskrankenkasse, 1100 Wien, Wienerbergstraße 15-19, vertreten durch Dr. Heinz Edelmann, Rechtsanwalt in Wien, wegen Kostenerstattung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 11. September 2012, GZ 8 Rs 49/12b-28, womit das Urteil des Arbeits- und Sozialgerichts Wien vom 21. November 2011, GZ 17 Cgs 120/10a-24, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Fichtenau` (person)
- `KR Hermann Furtner` (person)
- `AR Angelika Neuhauser` (person)
- `Birgit Jaros` (person)
- `Dr. Herbert Pochieser` (person)
- `Wiener Gebietskrankenkasse` (organisation)
- `Dr. Heinz Edelmann` (person)

**Example 49** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Roland Soukup, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Linz` | `Oberlandesgerichts Linz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Dr. Gabriele Griehsel` (person)
- `Dr. Wolfgang Kozak` (person)
- `Roland Soukup` (person)
- `Mahringer Steinwender Bestebner Rechtsanwälte OG` (organisation)
- `Landesgerichts Salzburg` (organisation)

**Example 50** (doc_id: `deanon_260716_TRAIN/10ObS99_15d`) (sent_id: `deanon_260716_TRAIN/10ObS99_15d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die fachkundigen Laienrichter Mag. Dr. Wolfgang Höfle (aus dem Kreis der Arbeitgeber) und Ing. Thomas Bauer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Willibald Kollowrat, BEd, vertreten durch Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH in Graz, gegen die beklagte Partei Versicherungsanstalt für Eisenbahnen und Bergbau, Linke Wienzeile 48-52, 1060 Wien, vertreten durch Dr. Marie-Luise Safranek, Rechtsanwältin in Graz, wegen Wochengeld, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Juni 2015, GZ 7 Rs 28/15i-9, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 25. Februar 2015, GZ 36 Cgs 216/14d-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Graz` | `Oberlandesgerichts Graz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Mag. Dr. Wolfgang Höfle` (person)
- `Ing. Thomas Bauer` (person)
- `Willibald Kollowrat, BEd` (person)
- `Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH` (organisation)
- `Versicherungsanstalt für Eisenbahnen und Bergbau` (organisation)
- `Dr. Marie-Luise Safranek` (person)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)

**Example 51** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_5`)


Dagegen richtet sich die als Rekurs bezeichnete, prozessordnungswidrig an das Oberlandesgericht Linz gerichtete Beschwerde des Richard Laumeyer.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Linz` | `Oberlandesgericht Linz` |

**Missed by this rule (FN):**

- `Richard Laumeyer` (person)

**Example 52** (doc_id: `deanon_260716_TRAIN/11Os59_13f`) (sent_id: `deanon_260716_TRAIN/11Os59_13f_4`)


Zur Entscheidung über die Berufung werden die Akten dem Oberlandesgericht Wien zugeleitet.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Example 53** (doc_id: `deanon_260716_TRAIN/11Os67_16m`) (sent_id: `deanon_260716_TRAIN/11Os67_16m_4`)


Zur Entscheidung über die Berufungen werden die Akten dem Oberlandesgericht Innsbruck zugeleitet.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Innsbruck` | `Oberlandesgericht Innsbruck` |

**Example 54** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_4`)


Augst 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Vizepräsidentin des Obersten Gerichtshofs Mag. Marek, die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Wieser als Schriftführerin in der Maßnahmenvollzugssache des Gerald Winand wegen bedingter Nachsicht einer mit Freiheitsentziehung verbundenen vorbeugenden Maßnahme (§ 21 Abs 1 StGB) über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien vom 16. Mai 2018, AZ 22 Bs 119/18p (AZ 606 Hv 1/17k des Landesgerichts Korneuburg), nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

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
- `Landesgerichts Korneuburg` (organisation)

**Example 55** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_5`)


Gründe:  Rechtliche Beurteilung Der gegen den Beschluss des Oberlandesgerichts Wien, mit dem eine Beschwerde des Gerald Wandscheer gegen den Beschluss des Landesgerichts Korneuburg vom 21. Februar 2018, GZ 606 Hv 1/17k-94, als verspätet zurückgewiesen worden war, gerichtete „Einspruch“ war ebenso zurückzuweisen, weil gegen derartige Entscheidungen eines Beschwerdegerichts kein weiterer Rechtszug vorgesehen ist (§ 89 Abs 6 StPO).

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Gerald Wandscheer` (person)
- `Landesgerichts Korneuburg` (organisation)

**Example 56** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_8`)


Der vorliegende Antrag des Mag. Herwig Bleuler bezieht sich auf das Urteil des Oberlandesgerichts Wien vom 21. August 2019, AZ 17 Bs 168/19h, mit dem der Berufung des Betroffenen gegen das Urteil des Landesgerichts für Strafsachen Wien vom 14. November 2018, GZ 22 Hv 7/18k-350, nicht Folge gegeben wurde.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Mag. Herwig Bleuler` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 57** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_4`)


2005 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab ist von der Entscheidung über die Beschwerde des Oliver Paukstat gegen den Beschluss des Oberlandesgerichts Wien vom 8. Februar 2016, AZ 32 Bs 12/16y, ausgeschlossen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Oliver Paukstat` (person)

**Example 58** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_9`)


An der angefochtenen Entscheidung des Oberlandesgerichts Wien hat die mit ihm in einem Angehörigenverhältnis im Sinne des § 72 StGB stehende Senatspräsidentin des Oberlandesgerichts Dr. Christine Schwab als Richterin mitgewirkt.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Dr. Christine Schwab` (person)

**Example 59** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_9`)


1. Senatspräsident des Obersten Gerichtshofs Dr. Schwab zeigt seine Ausgeschlossenheit unter Hinweis auf die (Vor-)Entscheidung des Obersten Gerichtshofs vom 8. August 2013, GZ 12 Ns 48/13z-3, sowie den Umstand an, dass er mit Senatspräsidentin des Oberlandesgerichts Wien Dr. Christine Schwab, die an mehreren (vom Anzeiger im einzelnen bezeichneten) früheren Entscheidungen dieses Gerichts in dieser Sache mit Bezug auf die Prüfung des Tatverdachts teilgenommen hat, im Angehörigenverhältnis des § 72 StGB stehe.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Christine Schwab` (person)

**Example 60** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_14`)


Senat des Obersten Gerichtshofs - unter dem Aspekt der §§ 281 Abs 1 Z 5a, 362 StPO - auch der Tatverdacht hinsichtlich eines Tatzeitraums („August 2008 bis längstens 14. Dezember 2008“ - vgl Urteil des Landesgerichts für Strafsachen Wien vom 14. Oktober 2014, GZ 16 Hv 20/14x-3462, US 2) zu prüfen, auf den sich auch das Oberlandesgericht Wien in Entscheidungen bezog, die unter Mitwirkung der Angehörigen des Anzeigers getroffen wurden (vgl insb BS 32 f in AZ 19 Bs 465/12i).

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 61** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_4`)


2005 den Beschluss gefasst:  Spruch Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski ist von der Entscheidung über die Beschwerde des Ahmed Kleinmayer gegen den Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 25. November 2019, AZ 23 Bs 343/19p, ausgeschlossen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Ahmed Kleinmayer` (person)

**Example 62** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_7`)


Mit dem erwähnten Beschluss vom 25. November 2019 hatte das Oberlandesgericht Wien einer Beschwerde des Ahmed Kocks gegen einen Beschluss des Landesgerichts für Strafsachen Wien auf Ablehnung eines Antrags des Genannten auf Wiederaufnahme des Verfahrens AZ 606 Hv 1/11m jenes Gerichts nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Missed by this rule (FN):**

- `Ahmed Kocks` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 63** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Thomas Michenfelder wegen des Verbrechens des schweren gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 2 und Z 5, 129 Abs 1 Z 1, Z 2 und Z 3, 130 Abs 2 zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 38 Hv 40/18z des Landesgerichts Krems an der Donau, über die von der Generalprokuratur gegen den Beschluss des Präsidenten des Oberlandesgerichts Wien vom 17. Oktober 2018, AZ 130 Ns 31/18w, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Mag. Gföller und der Verteidigerin Dr. Zeh-Gindl zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Dr. Mann` (person)
- `Dr. Brenner` (person)
- `Mag. Rögner` (person)
- `Thomas Michenfelder` (person)
- `Landesgerichts Krems an der Donau` (organisation)
- `Mag. Gföller` (person)
- `Dr. Zeh-Gindl` (person)

**Example 64** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_4`)


Der Beschluss des Präsidenten des Oberlandesgerichts Wien vom 17. Oktober 2018, AZ 130 Ns 31/18w, verletzt § 43 Abs 1 Z 3 StPO.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 65** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_5`)


Dieser Beschluss wird aufgehoben und es wird in der Sache selbst erkannt, dass der Senatspräsident des Oberlandesgerichts Wien Dr. Krenn sowie die Richterinnen des Oberlandesgerichts Wien Mag. Edwards und Mag. Sanda von der Entscheidung über die Berufung des Angeklagten gegen das Urteil des Landesgerichts Krems an der Donau vom 8. August 2018, GZ 38 Hv 40/18z-100, nicht ausgeschlossen sind.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Dr. Krenn` (person)
- `Mag. Edwards` (person)
- `Mag. Sanda` (person)
- `Landesgerichts Krems an der Donau` (organisation)

**Example 66** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_7`)


Senat des Oberlandesgerichts Wien, dem der Senatspräsident Dr. Krenn sowie die Richterinnen Mag. Edwards und Mag. Sanda angehörten, dieses Urteil „in amtswegiger Wahrnehmung des Nichtigkeitsgrunds des § 281 Abs 1 Z 9 lit a iVm § 489 Abs 1 StPO“ wegen des Vorliegens von Rechtsfehlern mangels Feststellungen (vgl zu diesem BegriffRatz, WK-StPO § 281 Rz 605 ff) in den Schuldsprüchen I./ und III./, demgemäß im Strafausspruch und im Ausspruch über den Privatbeteiligtenanspruch auf und verwies die Sache in diesem Umfang zu neuerlicher Verhandlung und Entscheidung an das Erstgericht.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Dr. Krenn` (person)
- `Mag. Edwards` (person)
- `Mag. Sanda` (person)

**Example 67** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_11`)


Dagegen ergriff der Genannte Berufung wegen Nichtigkeit und Strafe (ON 107), die dem Oberlandesgericht Wien mit Bericht vom 8. Oktober 2018 (ON 108) vorgelegt und über die bislang noch nicht entschieden wurde.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Example 68** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_12`)


Mit Beschluss vom 17. Oktober 2018, AZ 130 Ns 31/18w, stellte der Präsident des Oberlandesgerichts Wien fest, dass Senatspräsident Dr. Krenn sowie die Richterinnen Mag. Edwards und Mag. Sanda „im Berufungsverfahren über die vom Erstangeklagten Thomas Mecit erhobene Berufung (ON 107) ausgeschlossen“ seien.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Dr. Krenn` (person)
- `Mag. Edwards` (person)
- `Mag. Sanda` (person)
- `Thomas Mecit` (person)

**Example 69** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_16`)


Rechtliche Beurteilung Wie die Generalprokuratur in ihrer Nichtigkeitsbeschwerde zur Wahrung des Gesetzes zutreffend ausführt, steht dieser Beschluss des Präsidenten des Oberlandesgerichts Wien mit dem Gesetz nicht in Einklang: Schon aufgrund ihres Ausnahmecharakters, insbesondere aber mit Blick auf das Spannungsverhältnis zum verfassungsrechtlich gewährleisteten Recht auf den gesetzlichen Richter (Art 83 Abs 2 B-VG) und zum Prinzip der festen Geschäftsverteilung (Art 87 Abs 3 B-VG) erfordert die Wahrnehmung von Ausschließungsgründen (§ 43 StPO) eine strikte Auslegung dieser Norm, um die – neben der Unabsetzbarkeit und Unversetzbarkeit (Art 88 Abs 2 B-VG) – wesentlichsten Säulen der richterlichen Unabhängigkeit (Art 87 Abs 1 B-VG) nicht auszuhöhlen (vglLässig, WK-StPO Vor §§ 43–47 Rz 3).

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Example 70** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_19`)


Gegenständlich aber hatte das Oberlandesgericht Wien im ersten Rechtsgang die Tatfrage im Rahmen der Strafberufung des Angeklagten Thomas Marczynkowski entgegen der Ausführungen im angefochtenen Beschluss weder „in voller Kognitionsbefugnis“ zu beurteilen, noch bezog es in den Entscheidungsgründen hiezu beweiswürdigend Stellung.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Missed by this rule (FN):**

- `Thomas Marczynkowski` (person)

**Example 71** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_21`)


Gründe, die geeignet wären, im Sinn des § 43 Abs 1 Z 3 StPO die volle Unvoreingenommenheit und Unparteilichkeit des Senatspräsidenten des Oberlandesgerichts Wien Dr. Krenn sowie der Richterinnen Mag. Edwards und Mag. Sanda im zweiten Rechtsgang in Zweifel zu ziehen, liegen daher entgegen der im angefochtenen Beschluss vertretenen Auffassung nicht vor.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Dr. Krenn` (person)
- `Mag. Edwards` (person)
- `Mag. Sanda` (person)

**Example 72** (doc_id: `deanon_260716_TRAIN/12Os152_12p`) (sent_id: `deanon_260716_TRAIN/12Os152_12p_3`)


Kopf Der Oberste Gerichtshof hat am 13. Dezember 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Fruhmann als Schriftführerin in der Strafsache gegen unbekannte Täter wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB, AZ 130 Bl 65/12s des Landesgerichts für Strafsachen Wien, über die Beschwerde des Gebhard Sayin gegen den Beschluss des Oberlandesgerichts Wien vom 23. Oktober 2012, AZ 17 Bs 410/12m, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Michel` (person)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Fruhmann` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Gebhard Sayin` (person)

**Example 73** (doc_id: `deanon_260716_TRAIN/12Os152_12p`) (sent_id: `deanon_260716_TRAIN/12Os152_12p_4`)


Text Gründe: Mit der angefochtenen Entscheidung wies das Oberlandesgericht Wien die Beschwerde des Gebhard Senkfeil gegen den Beschluss des Landesgerichts für Strafsachen Wien vom 25. September 2012, GZ 130 Bl 65/12s-10, mit welchem der Antrag des Beschwerdeführers auf Fortführung des Verfahrens AZ 20 UT 91/12p der Staatsanwaltschaft Wien gegen unbekannte Täter wegen § 302 Abs 1 StGB zurückgewiesen worden war, als unzulässig zurück (§ 196 Abs 1 StPO).

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Missed by this rule (FN):**

- `Gebhard Senkfeil` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 74** (doc_id: `deanon_260716_TRAIN/12Os17_18v`) (sent_id: `deanon_260716_TRAIN/12Os17_18v_3`)


Kopf Der Oberste Gerichtshof hat am 15. März 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. T. Solé, Dr. Oshidari, Dr. Michel-Kwapinski und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Ettel als Schriftführerin in der Maßnahmenvollzugssache des Andreas Wegele, AZ 181 BE 143/17y des Landesgerichts für Strafsachen Wien, über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien vom 9. Jänner 2018, AZ 131 Bs 370/17z, und seinen Antrag auf Bewilligung der Verfahrenshilfe nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Dr. Oshidari` (person)
- `Dr. Michel-Kwapinski` (person)
- `Dr. Brenner` (person)
- `Mag. Ettel` (person)
- `Andreas Wegele` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 75** (doc_id: `deanon_260716_TRAIN/12Os17_18v`) (sent_id: `deanon_260716_TRAIN/12Os17_18v_5`)


Text Gründe: Mit dem angefochtenen Beschluss vom 9. Jänner 2018, AZ 131 Bs 370/17z, gab das Oberlandesgericht Wien als Rechtsmittelgericht der Beschwerde des Andreas Wackerow gegen den Beschluss des Landesgerichts für Strafsachen Wien vom 20. November 2017, GZ 181 BE 143/17y-16, mit dem die bedingte Entlassung aus einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 2 StGB abgelehnt worden war, nicht Folge.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Missed by this rule (FN):**

- `Andreas Wackerow` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 76** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_6`)


Zur Entscheidung über die Berufung wegen des Strafausspruchs werden die Akten vorerst dem Oberlandesgericht Innsbruck zugeleitet.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Innsbruck` | `Oberlandesgericht Innsbruck` |

**Example 77** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_3`)


Kopf Der Oberste Gerichtshof hat am 8. April 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Holzweber als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll, Dr. Schwab, Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger in Gegenwart der Richteramtsanwärterin Mag. Bayer als Schriftführerin in der Strafsache gegen Dr. Ernst-Peter Nepomuk Lieschke wegen des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB über die Beschwerde des Verurteilten gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 19. Jänner 2010, AZ 20 Bs 461/09d (GZ 20 Hv 73/09p-19 des Landesgerichts St. Pölten), nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Holzweber` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Dr. Schwab` (person)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Hetlinger` (person)
- `Mag. Bayer` (person)
- `Dr. Ernst` (person)
- `Nepomuk Lieschke` (person)
- `Landesgerichts St. Pölten` (organisation)

**Example 78** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_4`)


Text G r ü n d e : Mit Urteil des Einzelrichters des Landesgerichts St. Pölten vom 18. September 2009, GZ 20 Hv 73/09p-13, wurde Dr. Ernst-Peter Paula Langehanke des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB schuldig erkannt und zu einer für eine Probezeit von drei Jahren bedingt nachgesehenen Freiheitsstrafe von vier Wochen verurteilt. Der vom Angeklagten dagegen erhobenen Berufung wegen Nichtigkeit, Schuld und Strafe gab das Oberlandesgericht Wien mit der nunmehr angefochtenen Entscheidung keine Folge (ON 19).

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Missed by this rule (FN):**

- `Landesgerichts St. Pölten` (organisation)
- `Dr. Ernst` (person)
- `Paula Langehanke` (person)

**Example 79** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2020 durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé und durch die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Viktor Marschmeyer und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 3 zweiter Fall StGB, AZ 352 HR 214/11x des Landesgerichts für Strafsachen Wien, über den Antrag des Dr. Stefan Toepfl auf Erneuerung des Strafverfahrens gemäß § 363a StPO in Ansehung des Beschlusses des Oberlandesgerichts Wien vom 28. August 2018, AZ 20 Bs 199/18p, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Dr. Brenner` (person)
- `Dr. Setz-Hummel` (person)
- `Mag. Hauer` (person)
- `Viktor Marschmeyer` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Dr. Stefan Toepfl` (person)

**Example 80** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_5`)


Das Oberlandesgericht Wien als Rechtsmittelgericht gab der dagegen erhobenen Beschwerde des Beschuldigten (ON 661) mit Beschluss vom 28. August 2018, AZ 20 Bs 199/18p, nicht Folge (ON 683).

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Example 81** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_6`)


Rechtliche Beurteilung Gegen diesen Beschluss des Oberlandesgerichts Wien richtet sich der – nicht auf ein Erkenntnis des Europäischen Gerichtshofs für Menschenrechte (EGMR) gestützte – (rechtzeitige) Antrag des Beschuldigten Dr. Stefan Tilge auf Erneuerung des Strafverfahrens gemäß § 363a StPO per analogiam, mit welchem dieser einen „Verstoß gegen Art 6 und 8 EMRK, Art 1 1.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Wien` | `Oberlandesgerichts Wien` |

**Missed by this rule (FN):**

- `Dr. Stefan Tilge` (person)

**Example 82** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_4`)


Zur Entscheidung über die Berufung werden die Akten dem Oberlandesgericht Graz zugeleitet.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Graz` | `Oberlandesgericht Graz` |

**Example 83** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_20`)


Mit Beschluss des Oberlandesgerichts Innsbruck als Beschwerdegericht vom 25. November 2014, AZ 11 Bs 326/14z, 349/14g (ON 47 im Akt AZ 51 Hv 32/13i des Landesgerichts Feldkirch bzw ON 52 im Akt AZ 39 Hv 64/14h dieses Landesgerichts), wurde die Beschwerde als unzulässig (verspätet) zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Innsbruck` | `Oberlandesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Landesgerichts Feldkirch` (organisation)

**Example 84** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_34`)


Durch die Aufhebung des Beschlusses auf Wiederaufnahme des Strafverfahrens wird die von diesem rechtslogisch abhängige Beschwerdeentscheidung des Oberlandesgerichts Innsbruck hinfällig (RIS-Justiz RS0100444).

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Innsbruck` | `Oberlandesgerichts Innsbruck` |

**Example 85** (doc_id: `deanon_260716_TRAIN/13Os105_19v`) (sent_id: `deanon_260716_TRAIN/13Os105_19v_5`)


Mit Urteil vom 21. Mai 2019 gab das Oberlandesgericht Innsbruck der Berufung des Genannten Folge.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Innsbruck` | `Oberlandesgericht Innsbruck` |

**Example 86** (doc_id: `deanon_260716_TRAIN/13Os108_19k`) (sent_id: `deanon_260716_TRAIN/13Os108_19k_5`)


Die dagegen gerichtete Beschwerde des Sebastian Naegeler wies das Oberlandesgericht Graz mit Beschluss vom 1. August 2019, AZ 10 Bs 202/19k, unter Hinweis auf § 196 Abs 1 zweiter Halbsatz StPO als unzulässig zurück.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Graz` | `Oberlandesgericht Graz` |

**Missed by this rule (FN):**

- `Sebastian Naegeler` (person)

**Example 87** (doc_id: `deanon_260716_TRAIN/13Os117_19h`) (sent_id: `deanon_260716_TRAIN/13Os117_19h_4`)


Zur Entscheidung über die Berufung werden die Akten dem Oberlandesgericht Wien zugeleitet.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Example 88** (doc_id: `deanon_260716_TRAIN/13Os126_17d`) (sent_id: `deanon_260716_TRAIN/13Os126_17d_4`)


Zur Entscheidung über die Berufung und die Beschwerde werden die Akten dem Oberlandesgericht Linz zugeleitet.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Linz` | `Oberlandesgericht Linz` |

**Example 89** (doc_id: `deanon_260716_TRAIN/13Os155_15s`) (sent_id: `deanon_260716_TRAIN/13Os155_15s_4`)


Zur Entscheidung über die Berufung gegen die Aussprüche über die Strafe und die privatrechtlichen Ansprüche werden die Akten dem Oberlandesgericht Wien zugeleitet.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Example 90** (doc_id: `deanon_260716_TRAIN/13Os16_15z`) (sent_id: `deanon_260716_TRAIN/13Os16_15z_3`)


Kopf Der Oberste Gerichtshof hat am 25. Februar 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Bachl als Schriftführerin in der Strafsache gegen Mag. Johanna Fletcher wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB, AZ 3 St 166/14k der Staatsanwaltschaft Wels, über die Beschwerde des Herbert Onesseit gegen den Beschluss des Oberlandesgerichts Linz vom 9. Jänner 2015, AZ 7 Bs 218/14d (ON 12), nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Linz` | `Oberlandesgerichts Linz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Mag. Bachl` (person)
- `Mag. Johanna Fletcher` (person)
- `Herbert Onesseit` (person)

**Example 91** (doc_id: `deanon_260716_TRAIN/13Os16_15z`) (sent_id: `deanon_260716_TRAIN/13Os16_15z_4`)


Gründe:  Rechtliche Beurteilung Mit dem angefochtenen Beschluss wies das Oberlandesgericht Linz die Beschwerde des Herbert Oehlschlager gegen den Beschluss des Landesgerichts Wels vom 19. November 2014, AZ 24 Bl 81/14h (ON 9 der Ermittlungsakten), mit dem der Antrag des Genannten auf Fortführung des Verfahrens zurückgewiesen worden war, gemäß § 196 Abs 1 erster Satz StPO zurück (ON 12 der Ermittlungsakten).

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Linz` | `Oberlandesgericht Linz` |

**Missed by this rule (FN):**

- `Herbert Oehlschlager` (person)
- `Landesgerichts Wels` (organisation)

**Example 92** (doc_id: `deanon_260716_TRAIN/13Os23_15d`) (sent_id: `deanon_260716_TRAIN/13Os23_15d_4`)


Zur Entscheidung über die Berufung und die Beschwerde werden die Akten dem Oberlandesgericht Wien zugeleitet.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Example 93** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_5`)


Zur Entscheidung über die Berufung werden die Akten dem Oberlandesgericht Wien zugeleitet.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Wien` | `Oberlandesgericht Wien` |

**Example 94** (doc_id: `deanon_260716_TRAIN/13Os68_18a`) (sent_id: `deanon_260716_TRAIN/13Os68_18a_4`)


Text Gründe: Mihai von Crailsheim wurde mit Urteil des Landesgerichts für Strafsachen Graz als Schöffengericht vom 19. April 2017, GZ 222 Hv 15/17v-207, des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 2 erster Fall StGB sowie weiterer strafbarer Handlungen schuldig erkannt und zu einer Freiheitsstrafe verurteilt, die das Oberlandesgericht Graz – in Stattgebung einer dagegen erhobenen Berufung des Angeklagten – mit Urteil vom 25. Oktober 2017, AZ 8 Bs 311/17x, herabsetzte.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Graz` | `Oberlandesgericht Graz` |

**Missed by this rule (FN):**

- `Mihai von Crailsheim` (person)
- `Landesgerichts für Strafsachen Graz` (organisation)

**Example 95** (doc_id: `deanon_260716_TRAIN/13Os74_17g`) (sent_id: `deanon_260716_TRAIN/13Os74_17g_4`)


Zur Entscheidung über die Berufung und die Beschwerde werden die Akten dem Oberlandesgericht Linz zugeleitet.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Linz` | `Oberlandesgericht Linz` |

**Example 96** (doc_id: `deanon_260716_TRAIN/13Os78_12p`) (sent_id: `deanon_260716_TRAIN/13Os78_12p_3`)


Kopf Der Oberste Gerichtshof hat am 30. August 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin Mag. Temper als Schriftführerin in der Strafsache gegen Michael Lengjel und andere Beschuldigte wegen des Vergehens des schweren Betrugs nach §§ 146, 147 Abs 2 StGB sowie weiterer strafbarer Handlungen, AZ 21 Bl 5/11k des Landesgerichts Innsbruck, über die Beschwerden der Anna Wynand und des DI Georg Lu Brian Waltemate gegen den Beschluss des Oberlandesgerichts Innsbruck vom 29. Mai 2012, AZ 6 Bs 220/12x, 221/12v, 222/12s, 223/12p und 224/12k, nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerden werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Innsbruck` | `Oberlandesgerichts Innsbruck` |

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
- `Landesgerichts Innsbruck` (organisation)
- `Anna Wynand` (person)
- `Brian Waltemate` (person)

**Example 97** (doc_id: `deanon_260716_TRAIN/13Os78_12p`) (sent_id: `deanon_260716_TRAIN/13Os78_12p_4`)


Gründe:  Rechtliche Beurteilung Mit dem angefochtenen Beschluss wies das Oberlandesgericht Innsbruck die Beschwerden der Anna Waniek und des DI Georg Lu Carla Hanel gegen mehrere Verfügungen des Vorsitzenden eines Drei-Richter-Senats des Landesgerichts Innsbruck als unzulässig zurück.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Innsbruck` | `Oberlandesgericht Innsbruck` |

**Missed by this rule (FN):**

- `Anna Waniek` (person)
- `Carla Hanel` (person)
- `Landesgerichts Innsbruck` (organisation)

**Example 98** (doc_id: `deanon_260716_TRAIN/13Os97_11f`) (sent_id: `deanon_260716_TRAIN/13Os97_11f_4`)


Zur Entscheidung über die Berufung wegen des Ausspruchs über die Strafe werden die Akten dem Oberlandesgericht Linz zugeleitet.

| Predicted | Gold |
|---|---|
| `Oberlandesgericht Linz` | `Oberlandesgericht Linz` |

**Example 99** (doc_id: `deanon_260716_TRAIN/13Os99_19m`) (sent_id: `deanon_260716_TRAIN/13Os99_19m_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Christoph Holthuijsen wegen des Verbrechens der schweren Körperverletzung nach § 84 Abs 4 StGB, AZ 18 Hv 37/19b des Landesgerichts Klagenfurt, über die von der Generalprokuratur gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 21. August 2019, AZ 10 Bs 221/19d, ergriffene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Verteidigerin Mag. Sternad und des Privatbeteiligtenvertreters Mag. Höllwerth zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Oberlandesgerichts Graz` | `Oberlandesgerichts Graz` |

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
- `Landesgerichts Klagenfurt` (organisation)
- `Mag. Höpler` (person)
- `Mag. Sternad` (person)
- `Mag. Höllwerth` (person)

</details>

---

## `OGH_Abbreviation` 🏆

**F1:** 0.219 | **Precision:** 1.000 | **Recall:** 0.123  

**Format:** `regex`  
**Rule ID:** `ad43d7bd`  
**Description:**
Matches the abbreviation OGH (Oberster Gerichtshof).

**Content:**
```
\bOGH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.123 | 0.219 | 493 | 493 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 493 | 0 | 3521 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc25_09x`) (sent_id: `deanon_260716_TRAIN/10Nc25_09x_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 11** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 12** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 13** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 14** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 15** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 16** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 19** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 20** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 21** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 22** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 23** (doc_id: `deanon_260716_TRAIN/10Ob18_13i`) (sent_id: `deanon_260716_TRAIN/10Ob18_13i_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 24** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 25** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 26** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 27** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 28** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 29** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 30** (doc_id: `deanon_260716_TRAIN/10Ob26_10m`) (sent_id: `deanon_260716_TRAIN/10Ob26_10m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 31** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 32** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 33** (doc_id: `deanon_260716_TRAIN/10Ob28_19v`) (sent_id: `deanon_260716_TRAIN/10Ob28_19v_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 34** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 35** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 36** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 37** (doc_id: `deanon_260716_TRAIN/10Ob30_19p`) (sent_id: `deanon_260716_TRAIN/10Ob30_19p_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 38** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 39** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 40** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 41** (doc_id: `deanon_260716_TRAIN/10Ob3_12g`) (sent_id: `deanon_260716_TRAIN/10Ob3_12g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 42** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 43** (doc_id: `deanon_260716_TRAIN/10Ob41_14y`) (sent_id: `deanon_260716_TRAIN/10Ob41_14y_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 44** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 45** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 46** (doc_id: `deanon_260716_TRAIN/10Ob43_19z`) (sent_id: `deanon_260716_TRAIN/10Ob43_19z_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 47** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 48** (doc_id: `deanon_260716_TRAIN/10Ob57_13z`) (sent_id: `deanon_260716_TRAIN/10Ob57_13z_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 49** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 50** (doc_id: `deanon_260716_TRAIN/10Ob6_24s`) (sent_id: `deanon_260716_TRAIN/10Ob6_24s_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 51** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 52** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 53** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 54** (doc_id: `deanon_260716_TRAIN/10ObS99_15d`) (sent_id: `deanon_260716_TRAIN/10ObS99_15d_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 55** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 56** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 57** (doc_id: `deanon_260716_TRAIN/11Os59_13f`) (sent_id: `deanon_260716_TRAIN/11Os59_13f_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 58** (doc_id: `deanon_260716_TRAIN/11Os67_16m`) (sent_id: `deanon_260716_TRAIN/11Os67_16m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 59** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 60** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 61** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_3`)


Kopf Der Oberste Gerichtshof hat am 18. März 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski im Verfahren zur Unterbringung des Mag. Herwig Bäseke in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB, AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz gemäß § 62 Abs 1 zweiter Satz OGH-Geo 2019 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger sowie Mag. Fürnkranz sind von der Entscheidung über die Anträge des Mag. Herwig Berto auf Erneuerung des Strafverfahrens AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, ausgeschlossen.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Herwig Bäseke` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Fürnkranz` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Fürnkranz` (person)
- `Mag. Herwig Berto` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 62** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 63** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_3`)


Kopf Der Oberste Gerichtshof hat am 16. März 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Brenner in der Strafvollzugssache des Oliver Pekarek, AZ 39 Ns 43/15i des Landesgerichts Krems an der Donau, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Brenner` (person)
- `Oliver Pekarek` (person)
- `Landesgerichts Krems an der Donau` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)

**Example 64** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 65** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_3`)


Kopf Der Oberste Gerichtshof hat am 11. März 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Dr. Oshidari als weitere Richter in der Strafsache gegen Gerhard Bukowska wegen des Verbrechens des schweren gewerbsmäßigen Betrugs nach §§ 146, 147 Abs 3, 148 erster Fall, 15 Abs 1 StGB und weiterer strafbarer Handlungen, AZ 16 Hv 20/14x des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätin des Obersten Gerichtshofs Mag. Michel gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Dr. Oshidari` (person)
- `Gerhard Bukowska` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Michel` (person)

**Example 66** (doc_id: `deanon_260716_TRAIN/12Ns94_11m`) (sent_id: `deanon_260716_TRAIN/12Ns94_11m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 67** (doc_id: `deanon_260716_TRAIN/12Ns94_11m`) (sent_id: `deanon_260716_TRAIN/12Ns94_11m_3`)


Kopf Der Oberste Gerichtshof hat am 28. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in der Strafsache gegen Mag. Herwig Bernts wegen des Vergehens des Widerstands gegen die Staatsgewalt nach § 269 Abs 1 erster Fall StGB und anderer strafbarer Handlungen, AZ 20 Hv 38/11f des Landesgerichts Linz, über den Antrag des Angeklagten auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Herwig Bernts` (person)
- `Landesgerichts Linz` (organisation)

**Example 68** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 69** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_3`)


Kopf Der Oberste Gerichtshof hat am 9. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Brenner und Dr. Setz-Hummel in der Strafsache gegen Ahmed Koehnen wegen des Verbrechens des Mordes nach § 75 StGB, AZ 606 Hv 1/11m des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit der Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Brenner` (person)
- `Dr. Setz-Hummel` (person)
- `Ahmed Koehnen` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)

**Example 70** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 71** (doc_id: `deanon_260716_TRAIN/12Os152_12p`) (sent_id: `deanon_260716_TRAIN/12Os152_12p_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 72** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 73** (doc_id: `deanon_260716_TRAIN/12Os17_18v`) (sent_id: `deanon_260716_TRAIN/12Os17_18v_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 74** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 75** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 76** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 77** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 78** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 79** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 80** (doc_id: `deanon_260716_TRAIN/13Fss3_19y`) (sent_id: `deanon_260716_TRAIN/13Fss3_19y_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 81** (doc_id: `deanon_260716_TRAIN/13Fss3_19y`) (sent_id: `deanon_260716_TRAIN/13Fss3_19y_3`)


Kopf Der Oberste Gerichtshof hat am 21. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und die Hofrätin des Obersten Gerichtshofs Dr. Brenner über den von Ing. Sebastian Novko im Verfahren AZ 5 Bl 6/19v des Landesgerichts für Strafsachen Graz gestellten Fristsetzungsantrag nach Einsichtnahme der Generalprokuratur in die Akten und Abstimmung gemäß § 62 Abs 1 zweiter Satz OGH-Geo 2019 den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Brenner` (person)
- `Ing. Sebastian Novko` (person)
- `Landesgerichts für Strafsachen Graz` (organisation)

**Example 82** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 83** (doc_id: `deanon_260716_TRAIN/13Os105_19v`) (sent_id: `deanon_260716_TRAIN/13Os105_19v_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 84** (doc_id: `deanon_260716_TRAIN/13Os108_19k`) (sent_id: `deanon_260716_TRAIN/13Os108_19k_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 85** (doc_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a__0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 86** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 87** (doc_id: `deanon_260716_TRAIN/13Os117_19h`) (sent_id: `deanon_260716_TRAIN/13Os117_19h_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 88** (doc_id: `deanon_260716_TRAIN/13Os126_17d`) (sent_id: `deanon_260716_TRAIN/13Os126_17d_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 89** (doc_id: `deanon_260716_TRAIN/13Os155_15s`) (sent_id: `deanon_260716_TRAIN/13Os155_15s_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 90** (doc_id: `deanon_260716_TRAIN/13Os16_15z`) (sent_id: `deanon_260716_TRAIN/13Os16_15z_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 91** (doc_id: `deanon_260716_TRAIN/13Os22_12b_13Ns16_12z_`) (sent_id: `deanon_260716_TRAIN/13Os22_12b_13Ns16_12z__0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 92** (doc_id: `deanon_260716_TRAIN/13Os23_15d`) (sent_id: `deanon_260716_TRAIN/13Os23_15d_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 93** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 94** (doc_id: `deanon_260716_TRAIN/13Os34_19b`) (sent_id: `deanon_260716_TRAIN/13Os34_19b_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 95** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 96** (doc_id: `deanon_260716_TRAIN/13Os68_18a`) (sent_id: `deanon_260716_TRAIN/13Os68_18a_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 97** (doc_id: `deanon_260716_TRAIN/13Os74_17g`) (sent_id: `deanon_260716_TRAIN/13Os74_17g_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 98** (doc_id: `deanon_260716_TRAIN/13Os78_12p`) (sent_id: `deanon_260716_TRAIN/13Os78_12p_0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

**Example 99** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__0`)


Gericht OGH

| Predicted | Gold |
|---|---|
| `OGH` | `OGH` |

</details>

---

## `Bezirksgericht_Handelsgericht` 

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `abcf145d`  
**Description:**
Matches District Courts for Commercial Matters (Handelssachen).

**Content:**
```
\bBezirksgerichts?\s+für\s+Handelssachen\s+(?:Wien|Linz|Salzburg|Innsbruck|Graz|Klagenfurt|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|St.\s+Pölten)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 5 | 5 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 0 | 3761 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_16`)


Mit Urteil des Bezirksgerichts Bezirksgericht für Handelssachen Wien vom 21.

| Predicted | Gold |
|---|---|
| `Bezirksgericht für Handelssachen Wien` | `Bezirksgericht für Handelssachen Wien` |

**Example 1** (doc_id: `deanon_260716_TRAIN/7Ob36_25g`) (sent_id: `deanon_260716_TRAIN/7Ob36_25g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Malesich, Dr. Weber, Mag. Fitz und Mag. Jelinek als weitere Richter in der Rechtssache der klagenden Partei Gundula Aichmann, vertreten durch Poduschka Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Plönnigs Technik AG, Wieden 35, 3390 Spielberg, Österreich, vertreten durch Themmer, Toth & Partner Rechtsanwälte GmbH in Wien, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 28. November 2024, GZ 1 R 124/24t-14, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 27. Juni 2024, GZ 21 C 604/23m-10, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts für Handelssachen Wien` | `Bezirksgerichts für Handelssachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Solé` (person)
- `Mag. Malesich` (person)
- `Dr. Weber` (person)
- `Mag. Fitz` (person)
- `Mag. Jelinek` (person)
- `Gundula Aichmann` (person)
- `Poduschka Partner Anwaltsgesellschaft mbH` (organisation)
- `Plönnigs Technik AG` (organisation)
- `Wieden 35, 3390 Spielberg, Österreich` (address)
- `Themmer, Toth & Partner Rechtsanwälte GmbH` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/7Ob6_20p`) (sent_id: `deanon_260716_TRAIN/7Ob6_20p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Ing. Roderich Florczyk, vertreten durch Dr. Norbert Nowak, Rechtsanwalt in Wien, gegen die beklagte Partei Mittel-Energie AG, Gaunitzhof 8, 4632 Breitwies, Österreich, vertreten durch die Schönherr Rechtsanwälte GmbH in Wien, wegen 6.342,73 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 8. November 2018, GZ 60 R 98/18v-12, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 15. Juni 2018, GZ 18 C 109/18p-8, abgeändert wurde, beschlossen und zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Bezirksgerichts für Handelssachen Wien` | `Bezirksgerichts für Handelssachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Hon.-Prof. Dr. Höllwerth` (person)
- `Dr. Solé` (person)
- `Mag. Malesich` (person)
- `MMag. Matzka` (person)
- `Ing. Roderich Florczyk` (person)
- `Dr. Norbert Nowak` (person)
- `Mittel-Energie AG` (organisation)
- `Gaunitzhof 8, 4632 Breitwies, Österreich` (address)
- `Schönherr Rechtsanwälte GmbH` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/7Ob6_20p`) (sent_id: `deanon_260716_TRAIN/7Ob6_20p_19`)


Rechtliche Beurteilung Zu I.: 1.1.Der Senat hat aus Anlass der Revision mit Beschluss vom 27. Februar 2019, AZ 7 Ob 26/19b, das Revisionsverfahren bis zur Entscheidung des Gerichtshofs der Europäischen Union (EuGH) über das Vorabentscheidungsersuchen vom 12. Juli 2018 des Bezirksgerichts für Handelssachen Wien (GZ 13 C 738/17z-12 [13 C 8/18y, 13 C 21/18k und 13 C 2/18s]), Rechtssache C-479/18,UNIQA Österreich Versicherungen ua, unterbrochen.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts für Handelssachen Wien` | `Bezirksgerichts für Handelssachen Wien` |

**Example 4** (doc_id: `deanon_260716_TRAIN/7Ob85_15y`) (sent_id: `deanon_260716_TRAIN/7Ob85_15y_6`)


Renzlhausen 24, 6553 See, Österreich, vertreten durch Dorda Brugger Jordis Rechtsanwälte GmbH in Wien, wegen 7.523,16 EUR sA, über den Rekurs der erstbeklagten Partei gegen den Beschluss des Handelsgerichts Wien als Berufungsgericht vom 19. Februar 2015, GZ 1 R 6/15a-49, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 29. September 2014, GZ 13 C 134/10s-45, hinsichtlich der erstbeklagten Partei aufgehoben wurde, den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts für Handelssachen Wien` | `Bezirksgerichts für Handelssachen Wien` |

**Missed by this rule (FN):**

- `Dorda Brugger Jordis Rechtsanwälte GmbH` (organisation)
- `Handelsgerichts Wien` (organisation)

</details>

---

## `Verfassungsgerichtshof` 🏆

**F1:** 0.011 | **Precision:** 1.000 | **Recall:** 0.006  

**Format:** `regex`  
**Rule ID:** `4f019849`  
**Description:**
Matches the Constitutional Court (Verfassungsgerichtshof) in nominative or genitive case.

**Content:**
```
\bVerfassungsgerichtshof(?:s)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.006 | 0.011 | 23 | 23 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 23 | 0 | 3713 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_93`)


Die nach den Vorgaben des Verfassungsgerichtshofs gebotene steuerliche Entlastung des Geldunterhaltspflichtigen basiert auf dem Modell der getrennten Haushaltsführung (vgl RIS-Justiz RS0117015), in dem ein Elternteil seine Unterhaltspflicht durch Betreuungsleistungen und der andere durch Geldleistungen (allenfalls kombiniert mit anzurechnenden Naturalleistungen) erfüllt. Bei getrennter Haushaltsführung hat die Familienbeihilfe die Funktion, Betreuungsleistungen abzugelten und die steuerliche Entlastung des Geldunterhaltspflichtigen zu bewirken (RIS-Justiz RS0117015 [T20]).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |

**Example 1** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_91`)


Das Berufungsgericht sehe sich daher nicht zu einer Antragstellung an den Verfassungsgerichtshof veranlasst.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 2** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_147`)


2. Seine Anregung, ein Gesetzesprüfungsver-fahren beim Verfassungsgerichtshof bezüglich der „von der beklagten Partei ins Treffen geführten gesetzlichen Bestimmungen“ einzuleiten, begründet der Kläger mit einer Verletzung des Gleichheitssatzes.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 3** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_158`)


Mangelhaft soll das Berufungsverfahren deshalb geblieben sein, weil das Berufungsgericht keinen Antrag an den Verfassungsgerichtshof gestellt hat: Hat der Oberste Gerichtshof oder ein zur Entscheidung in zweiter Instanz zuständiges Gericht gegen die Anwendung eines (Bundes- oder Landes-)Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken, so ist nach Art 89 Abs 2 B-VG von Amts wegen der Antrag auf Aufhebung dieses Gesetzes beim Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_159`)


Nach einhelliger Rechtsprechung steht den Parteien eines Gerichtsverfahrens kein Recht auf Antragstellung hinsichtlich einer Befassung des Verfassungsgerichtshofs zu. Die Parteien können eine solche Antragstellung nur anregen (RIS-Justiz RS0056514;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |

**Example 5** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_162`)


Unterlässt ein Gericht die Anfechtung einer Norm beim Verfassungsgerichtshof, steht dagegen nach ständiger Rechtsprechung keiner Partei ein Rechtsmittel zu (RIS-Justiz RS0056514 [T10]).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 6** (doc_id: `deanon_260716_TRAIN/3Ob229_14v`) (sent_id: `deanon_260716_TRAIN/3Ob229_14v_44`)


Auch der Verfassungsgerichtshof hat in der vom Kläger zitierten Entscheidung B 97/91, B 284/91-303/91 (= VfSlg 13.006) zu einer - nicht dem § 38 Abs 6 OÖ ROG entsprechenden - Norm des früheren OÖ ROG 1972 eingeräumt, dass unter dem auch dort verwendeten Begriff „Grundstück“ nicht unbedingt nur ein einzelnes Grundstück verstanden werden kann, sondern gegebenenfalls auch mehrere Grundstücke, die miteinander eine „Einheit“ bilden.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 7** (doc_id: `deanon_260716_TRAIN/3Ob26_23d`) (sent_id: `deanon_260716_TRAIN/3Ob26_23d_47`)


Die Klägerin führt dagegen ins Treffen, dass die beschlussmäßige Umwidmung eines Grundstücks nach der Rechtsprechung des Verfassungsgerichtshofs erst dann erfolgen könne, wenn die Gemeinde bereits Eigentümerin des betroffenen Grundstücks sei; nur wenn es sich beim Grundstück um eine Privatstraße gehandelt hätte, die über Antrag des Eigentümers umgewidmet werden sollte, wäre eine Beschlussfassung nach § 27 Abs 2 Sbg LStG 1966 durch die Gemeinde vor Eigentumserwerb möglich gewesen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |

**Example 8** (doc_id: `deanon_260716_TRAIN/3Ob26_23d`) (sent_id: `deanon_260716_TRAIN/3Ob26_23d_50`)


Der von der Klägerin in diesem Zusammenhang zitierten Entscheidung des Verfassungsgerichtshofs vom 27. September 2003, V 108/01, lag nämlich der Sachverhalt zugrunde, dass der dort streitgegenständliche (Verbindungs-)Weg im Zeitpunkt der (vor der Enteignung des Grundstücks erfolgten) Widmung als Gemeindestraße schon seit Jahren als Privatstraße diente.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |

**Example 9** (doc_id: `deanon_260716_TRAIN/3Ob26_23d`) (sent_id: `deanon_260716_TRAIN/3Ob26_23d_51`)


Vor diesem Hintergrund sprach der Verfassungsgerichtshof aus, dass durch die Öffentlicherklärung einesin der Natur schon bestehendenWeges durch Verordnung mangels Eigentumserwerbs in gesetzwidriger Weise Gemeingebrauch begründet werde.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 10** (doc_id: `deanon_260716_TRAIN/5Ob171_22s`) (sent_id: `deanon_260716_TRAIN/5Ob171_22s_66`)


In den vonRohregger(aaO) zitierten Entscheidungen bejahen auch der Verfassungsgerichtshof (B 1050/09) und der Verwaltungsgerichtshof (AW 2012/01/0032) die Bedeutung des § 10 RAO und der Vorgängerbestimmung des § 10 RL-BA 2015 für das öffentliche Interesse an dem Verbot der Doppelvertretung, weil es dem Schutz der durch einen Rechtsanwalt vertretenen Parteien diene, seine Einhaltung für das zwischen Rechtsanwalt und Klient bestehende Treueverhältnis für wesentlich erachtet werde und für das allgemeine Bild der Anwaltschaft in der Öffentlichkeit von Bedeutung sei.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 11** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_147`)


3.2.6.Auch der Verfassungsgerichtshof hat sich bereits mehrfach (G 164/2014;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 12** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_152`)


Der Verfassungsgerichtshof führte allerdings aus, dass die Bestimmungen des Fern- und Auswärtsgeschäfte-Gesetzes den Vorschriften der Verbraucherrechte-RL entsprächen, welche den Mitgliedstaaten keinen Spielraum bei der Umsetzung einräumten;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 13** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_154`)


Auch von einem Vorabentscheidungsersuchen an den EuGH sah der Verfassungsgerichtshof ab (ErwG 74).

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 14** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_155`)


Darüber hinaus setzte sich der Verfassungsgerichtshof in diesem Erkenntnis mit Art 14 Abs 2 der Verbraucherrechte-RL, der durch § 15 Abs 4 FAGG umgesetzt wurde, auseinander und äußerte keine Zweifel an der Gültigkeit des Art 14 Abs 2 letzter Satz (entspricht § 15 Abs 4 letzter Satz FAGG): Der Verfassungsgerichtshof hat keine Zweifel an der Gültigkeit des Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 15** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_159`)


Der Verfassungsgerichtshof kann nun nicht erkennen, dass die Regelung des Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL diesen von der Rechtsprechung des Gerichtshofes der Europäischen Union aufgestellten Kriterien im Rahmen der Verhältnismäßigkeitsprüfung eines Unionsrechtsakts widerspricht: Die Bestimmungen der Verbraucherrechte-RL verfolgen das Ziel eines umfassenden Verbraucherschutzes bei Fernabsatzverträgen und außerhalb von Geschäftsräumen geschlossenen Verträgen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 16** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_161`)


Der Verfassungsgerichtshof hat keine Zweifel, dass die in Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL normierte Rechtsfolge für den Unternehmer bei mangelnder Belehrung über das Widerrufsrecht geeignet ist, das Ziel des umfassenden Verbraucherschutzes bei Fernabsatzverträgen und bei außerhalb von Geschäftsräumen geschlossenen Verträgen zu erreichen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 17** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_162`)


Der Verfassungsgerichtshof kann auch nicht erkennen, dass die Regelung des Art 14 Abs 2 letzter Satz der Verbraucherrechte-RL über das hinausgeht, was zur Verfolgung des mit der Regelung verfolgten Ziels des umfassenden Verbraucherschutzes erforderlich ist.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 18** (doc_id: `deanon_260716_TRAIN/6Ob36_20t`) (sent_id: `deanon_260716_TRAIN/6Ob36_20t_165`)


Der Verfassungsgerichtshof hat sohin keine Zweifel an deren Gültigkeit.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 19** (doc_id: `deanon_260716_TRAIN/8ObA72_19z`) (sent_id: `deanon_260716_TRAIN/8ObA72_19z_12`)


2. Dabei konnte sich der Oberste Gerichtshof auf einschlägige Judikatur sowohl des Verfassungsgerichtshofs als auch des EuGH stützen: 2.1 Der Verfassungsgerichtshof hat in seinem Erkenntnis G 450/2015 ua Parteianträge von ÖBB-Bediensteten (unter anderem auch des Klägers) abgewiesen, die § 53a und § 56 Abs 18 bis 24 BundesbahnG je idF BGBl I Nr 64/2015 als verfassungswidrig aufzuheben.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofs` | `Verfassungsgerichtshofs` |
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `ÖBB` (organisation)

</details>

---

## `Landesgericht_City_Extended` 🏆

**F1:** 0.196 | **Precision:** 1.000 | **Recall:** 0.109  

**Format:** `regex`  
**Rule ID:** `d93c350a`  
**Description:**
Matches Regional Courts with city names, ensuring 'St. Pölten', 'Hermagor', 'Leoben', 'Salzburg', 'Graz', 'Wien', 'Linz', 'Innsbruck', 'Klagenfurt', 'Bregenz', 'Feldkirch', 'Leoben', 'Lienz', 'Villach', 'Wels', 'Schwechat', 'Liesing', 'Gmunden', 'Bad Ischl', 'Telfs', 'Neusiedl am See', 'Favoriten', 'Fünfthau', 'Josefstadt', 'Hietzing', 'Ried im Innkreis', 'Krems an der Donau', 'Eisenstadt', 'Korneuburg', 'Laa an der Thaya', 'Wiener Neustadt', 'Steyr' are included.

**Content:**
```
\bLandesgerichts?\s+(?:für\s+Zivilrechtssachen\s+(?:Graz|Wien|Linz|Salzburg|Innsbruck|Eisenstadt|Klagenfurt|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|St\.\s+Pölten|Schwechat|Liesing|Gmunden|Bad\s+Ischl|Wels|Telfs|Neusiedl\s+am\s+See|Favoriten|Fünfthau|Josefstadt|Hietzing|Graz|Wien|Linz|Salzburg|Innsbruck|Eisenstadt|Klagenfurt|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|St\.\s+Pölten)|Eisenstadt|Salzburg|Innsbruck|Korneuburg|Laa\s+an\s+der\s+Thaya|Wels|Linz|Salzburg|Innsbruck|Eisenstadt|Klagenfurt|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|St\.\s+Pölten|Schwechat|Liesing|Gmunden|Bad\s+Ischl|Wels|Telfs|Neusiedl\s+am\s+See|Favoriten|Fünfthau|Josefstadt|Hietzing|Graz|Wien|Linz|Salzburg|Innsbruck|Eisenstadt|Klagenfurt|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|St\.\s+Pölten|Steyr|Wiener\s+Neustadt|Graz|Wien|Linz|Salzburg|Innsbruck|Eisenstadt|Klagenfurt|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|St\.\s+Pölten|Ried\s+im\s+Innkreis|Krems\s+an\s+der\s+Donau|Feldkirch|Graz|Wien|Linz|Salzburg|Innsbruck|Eisenstadt|Klagenfurt|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|St\.\s+Pölten|Schwechat|Liesing|Gmunden|Bad\s+Ischl|Wels|Telfs|Neusiedl\s+am\s+See|Favoriten|Fünfthau|Josefstadt|Hietzing|Graz|Wien|Linz|Salzburg|Innsbruck|Eisenstadt|Klagenfurt|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|St\.\s+Pölten|Hermagor)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.109 | 0.196 | 436 | 436 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 436 | 0 | 3559 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_3`)


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

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_6`)


Die in Wien ansässige klagende Gesellschaft nimmt die in Linz ansässige beklagte Gesellschaft beim Landesgericht Linz auf restliche Honorare für Planungsleistungen für ein Bauvorhaben in Klosterneuburg bei Wien in Anspruch.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_12`)


[3] Bereits in der Klage beantragt dieKlägerindie Delegierung der Rechtssache an das Landesgericht Korneuburg.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_15`)


Die Verhandlung der Rechtssache im Gerichtssprengel des Bauvorhabens – dem Landesgericht Korneuburg – sei daher verfahrensökonomisch und zweckmäßig.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_19`)


Sowohl die Beklagte als auch ihre Geschäftsführer sowie fünf namhaft gemachte Zeugen hätten ihren Arbeitsplatz bzw Wohnsitz im Sprengel des Landesgerichts Linz.

| Predicted | Gold |
|---|---|
| `Landesgerichts Linz` | `Landesgerichts Linz` |

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_21`)


Die Delegierung an das Landesgericht Korneuburg wäre daher mit einer erheblichen Verteuerung des Verfahrens und einer Erschwerung des Gerichtszugangs verbunden.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_29`)


Die Rechtssache weist keinen eindeutigen Schwerpunkt zum Landesgericht Korneuburg auf.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_30`)


Zwar ist das Bauvorhaben im Sprengel des Landesgerichts Korneuburg situiert.

| Predicted | Gold |
|---|---|
| `Landesgerichts Korneuburg` | `Landesgerichts Korneuburg` |

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_31`)


Mehrere von der Beklagten namhaft gemachte Zeugen sind aber im Sprengel des angerufenen Landesgerichts Linz bzw in Oberösterreich wohnhaft.

| Predicted | Gold |
|---|---|
| `Landesgerichts Linz` | `Landesgerichts Linz` |

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_32`)


Damit kann nicht gesagt werden, dass die Gründe für eine Übertragung der Rechtssache vom Landesgericht Linz an das Landesgericht Korneuburg überwiegen.

| Predicted | Gold |
|---|---|
| `Landesgericht Linz` | `Landesgericht Linz` |
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_33`)


Dass die Rechtssache vom Landesgericht Korneuburg aller Voraussicht nach rasch und mit geringerem Kostenaufwand zu Ende geführt werden kann, ist nach dem bisherigen Vorbringen nicht zu erkennen.

| Predicted | Gold |
|---|---|
| `Landesgericht Korneuburg` | `Landesgericht Korneuburg` |

**Example 11** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_3`)


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

**Example 12** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_3`)


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

**Example 13** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_3`)


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

**Example 14** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Bartholomäus Junghahn, geboren am 8. Mai 1999, und der minderjährigen HR Sophie Elefteriadis, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Bartholomäus Junghahn` (person)
- `HR Sophie Elefteriadis` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Juri Gerstl GmbH, Mutten 18, 3251 Schauboden, Österreich, vertreten durch Dr. Ralph Trischler, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, sowie die Nebenintervenientin auf Seiten der beklagten Partei Bundesbeschaffung GmbH, 1020 Wien, Lassallestraße 9b, vertreten durch die Olischar Rechtsanwaltsgesellschaft mbH in Wien, wegen 15.535 EUR sA, über den Revisionsrekurs der klagenden Partei (Revisionsinteresse: 7.460 EUR), gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 23. Februar 2023, GZ 16 R 168/22a-20, mit welchem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 5. September 2022, GZ 11 Cg 48/22t-12, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Mag. Schober` (person)
- `Dr. Thunhart` (person)
- `Juri Gerstl` (person)
- `Mutten 18, 3251 Schauboden, Österreich` (address)
- `Dr. Ralph Trischler` (person)
- `Bundesbeschaffung GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Leander Lindlahr, geboren am 1. August 2011, und des mj Yussuf Prussog, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Leander Lindlahr` (person)
- `Yussuf Prussog` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


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

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_3`)


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

**Example 19** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Mag. Kevin Maassen, vertreten durch Dr. Clemens Lintschinger, Rechtsanwalt in Wien, gegen die beklagte Partei Hon.-Prof. Friedhelm Adde, vertreten durch Mag. Dr. Georg Backhausen, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 27. Jänner 2016, GZ 38 R 265/15z-45, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

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
- `Mag. Dr. Georg Backhausen` (person)

**Example 20** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_5`)


Anita Schetzel, vertreten durch die Summereder Pichler Wächter Rechtsanwälte GmbH in Leonding, wegen 12.750 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Wels als Berufungsgericht vom 13. Dezember 2023, GZ 21 R 277/23v-53, mit dem das Urteil des Bezirksgerichts Wels vom 23. August 2023, GZ 9 C 430/22s-47, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Die Revision wird in Ansehung der Klageforderungen von 2.700 EUR sA, 4.575 EUR sA und 450 EUR sA zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Wels` | `Landesgerichts Wels` |

**Missed by this rule (FN):**

- `Anita Schetzel` (person)
- `Bezirksgerichts Wels` (organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Ralph Prusseit, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Akbayrak Metall GmbH, Schroateck 57, 4710 Niederweng, Österreich, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgerichts Krems an der Donau` | `Landesgerichts Krems an der Donau` |

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
- `Skribe Rechtsanwälte GmbH` (organisation)
- `Bezirksgerichts Zwettl` (organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der minderjährigen Annabelle Thurnher, geboren am 24. Juni 2001, vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung, Bezirk 10, 1100 Wien, Van der Nüll-Gasse 20), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 17. September 2009, GZ 44 R 454/09d-38, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Favoriten vom 16. Juni 2009, GZ 40 P 36/08f-U-26, teilweise abgeändert wurde, den B e s c h l u s s gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Annabelle Thurnher` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei DDr.in Cornelia Rinaldo, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Conmon-Verlag Limited, Kroisegg 20, 4052 Fleckendorf, Österreich Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

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
- `Brandl Talos Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_4`)


Malik Schoch, geboren 7. November 2002, 2. 7. Juli 2025, geboren 10. Juli 2004, und 3. Alan Schindlmair, geboren 7. August 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Timon Schönswetter, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Malik Schoch` (person)
- `7. November` (date)
- `7. Juli 2025` (date)
- `10. Juli` (date)
- `Alan Schindlmair` (person)
- `7. August` (date)
- `Mag. Florian Kucera` (person)
- `Mag. Timon Schönswetter` (person)
- `Doschek Rechtsanwalts GmbH` (organisation)
- `Bezirksgerichts Döbling` (organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_4`)


Enns-Umwelt Consulting Limited, Alpineweg 221, 5730 Jochbergthurn, Österreich, 2. Ing. Lara Markart, letztere vertreten durch Radel Stampf Supper Rechtsanwälte OG in Mattersburg, wegen 160.422,79 EUR sA, infolge Revision der klagenden Partei (Revisionsinteresse 107.422,79 EUR sA) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Jänner 2015, GZ 4 R 119/14w-32, womit das Urteil des Landesgerichts St. Pölten vom 25. April 2014, GZ 37 Cg 96/13f-28, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts St. Pölten` | `Landesgerichts St. Pölten` |

**Missed by this rule (FN):**

- `Enns-Umwelt` (organisation)
- `Alpineweg 221, 5730 Jochbergthurn, Österreich` (address)
- `Ing. Lara Markart` (person)
- `Radel Stampf Supper Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_10`)


2008 erfolgte die Eintragung beim Firmenbuch des Landesgerichts Eisenstadt mit einer Niederlassung in Angyalföldstraße 52, 4193 Hayrl, Österreich.

| Predicted | Gold |
|---|---|
| `Landesgerichts Eisenstadt` | `Landesgerichts Eisenstadt` |

**Missed by this rule (FN):**

- `Angyalföldstraße 52, 4193 Hayrl, Österreich` (address)

**Example 27** (doc_id: `deanon_260716_TRAIN/10Ob26_10m`) (sent_id: `deanon_260716_TRAIN/10Ob26_10m_5`)


Lars Ballogh, geboren am 3. Juli 2003, alle vertreten durch das Land Wien als Jugendwohlfahrtsträger (Amt für Jugend und Familie - Rechtsfürsorge Bezirke 17., 18. und 19., 1190 Wien, Gatterburggasse 12-14), wegen Unterhaltsvorschuss, über den „außerordentlichen Revisionsrekurs“ des Vaters Mag. Anton Bohmert, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. April 2009, GZ 44 R 193/08w-U140, womit der als Zulassungsvorstellung zu wertende „außerordentliche Revisionsrekurs“ des Vaters zurückgewiesen wurde, den Beschluss gefasst:  Spruch Der „außerordentliche Revisionsrekurs“ wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Lars Ballogh` (person)
- `Mag. Anton Bohmert` (person)

**Example 28** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_5`)


Unter Alver GmbH, beide Granglitzweg 11, 3251 Kroißenberg, Österreich, beide vertreten durch Dr. Michael Schneditz-Bolfras und andere Rechtsanwälte in Gmunden, wegen Bucheinsicht (in eventu Rechnungslegung) und Zahlung (Streitwert: 70.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Teilurteil des Oberlandesgerichts Linz als Berufungsgericht vom 17. Februar 2014, GZ 3 R 13/14y-90, womit das Urteil des Landesgerichts Wels vom 27. November 2013 (in der mit Beschluss vom 12. Dezember 2013 berichtigten Fassung), GZ 2 Cg 78/10p-82 und -84, abgeändert wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts Wels` | `Landesgerichts Wels` |

**Missed by this rule (FN):**

- `Unter Alver GmbH` (organisation)
- `Granglitzweg 11, 3251 Kroißenberg, Österreich` (address)
- `Dr. Michael Schneditz-Bolfras` (person)
- `Oberlandesgerichts Linz` (organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


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

**Example 30** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der zur AZ 38 Nc 13/08i beim Landesgericht für Zivilrechtssachen Wien anhängigen Ablehnungssache des Ablehnungswerbers Mag. Herwig Bortzlaff, über den Rekurs des Ablehnungswerbers gegen den Beschluss des Oberlandesgerichts Wien vom 10. November 2009, GZ 13 Nc 14/09x-2, womit ein Ablehnungsantrag zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgericht für Zivilrechtssachen Wien` | `Landesgericht für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Mag. Herwig Bortzlaff` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_5`)


Im Zusammenhang mit diesem Verfahren wies das Landesgericht für Zivilrechtssachen Wien mit Beschluss vom 26.

| Predicted | Gold |
|---|---|
| `Landesgericht für Zivilrechtssachen Wien` | `Landesgericht für Zivilrechtssachen Wien` |

**Example 32** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_6`)


11. 2008, GZ 38 Nc 13/08i-2, den Ablehnungsantrag des Mag. Herwig Berkenbrink in dessen Rekurs gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 13.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Mag. Herwig Berkenbrink` (person)

**Example 33** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_3`)


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

**Example 34** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_3`)


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

**Example 35** (doc_id: `deanon_260716_TRAIN/10Ob30_19p`) (sent_id: `deanon_260716_TRAIN/10Ob30_19p_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der minderjährigen Maja Dolleschell, geboren 14. August 2009, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Melk, 3390 Melk, Abt Karl-Straße 25a) wegen Unterhaltsvorschüssen, über den Revisionsrekurs des Kindes gegen den Beschluss des Landesgerichts St. Pölten als Rekursgericht vom 23. Jänner 2019, GZ 23 R 6/19h-52, mit dem der Beschluss des Bezirksgerichts Melk vom 21. November 2018, GZ 22 Pu 194/16m-42, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgerichts St. Pölten` | `Landesgerichts St. Pölten` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Maja Dolleschell` (person)
- `14. August` (date)
- `Bezirkshauptmannschaft Melk` (organisation)
- `Bezirksgerichts Melk` (organisation)

**Example 36** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


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

**Example 37** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_3`)


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

**Example 38** (doc_id: `deanon_260716_TRAIN/10Ob3_12g`) (sent_id: `deanon_260716_TRAIN/10Ob3_12g_3`)


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

**Example 39** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Ziegelbauer als Vorsitzenden sowie die Hofrätin Dr. Faber und die Hofräte Mag. Schober, Dr. Thunhart und Dr. Annerl als weitere Richter in der Pflegschaftssache der minderjährigen Meinrad Bruhnsen, geboren 30. Januar 2006, vertreten durch das Land Wien als Träger der Kinder- und Jugendhilfe (Magistrat der Stadt Wien, Rechtsvertretung Bezirke 1, 4 bis 9, 1060 Wien, Amerlingstraße 11), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch die Präsidentin des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 31. Oktober 2022, GZ 43 R 323/22a-17, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 9. Juni 2022, GZ 4 Pu 58/22a-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Mag. Schober` (person)
- `Dr. Thunhart` (person)
- `Dr. Annerl` (person)
- `Meinrad Bruhnsen` (person)
- `30. Januar` (date)
- `Magistrat der Stadt Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Bezirksgerichts Innere Stadt Wien` (organisation)

**Example 40** (doc_id: `deanon_260716_TRAIN/10Ob41_14y`) (sent_id: `deanon_260716_TRAIN/10Ob41_14y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in den verbundenen Familienrechtssachen des Antragstellers DI Dr. Bodo Kaczynski, geboren am 25. Juli 1975, vertreten durch Mag. Werner Thurner, Rechtsanwalt in Graz, gegen die Antragsgegnerinnen 1. Wolfgang Lombardini, geboren am 4. Dezember 2022, 2. Livia Löblein, geboren am 11. Januar 1966, vertreten durch Mörth Ecker Filzmaier, Rechtsanwalts-Partnerschaft in Graz, wegen Unterhalt, über den Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 24. September 2013, GZ 2 R 11/13x-76, womit der Beschluss des Bezirksgerichts Graz-Ost vom 26. November 2012, GZ 231 Fam 14/11a, 231 Fam 17/11t, 231 Fam 18/11i-60, teilweise bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.  Text Begründung: DasErstgerichtsetzte den monatlichen Unterhalt für die Erstantragsgegnerin ab 1. 2. 2011 von 390 EUR um 30 EUR auf 360 EUR herab (Punkt 1);

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Graz` | `Landesgerichts für Zivilrechtssachen Graz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `DI Dr. Bodo Kaczynski` (person)
- `25. Juli 1975` (date)
- `Mag. Werner Thurner` (person)
- `Wolfgang Lombardini` (person)
- `4. Dezember 2022` (date)
- `Livia Löblein` (person)
- `11. Januar 1966` (date)
- `Mörth Ecker Filzmaier, Rechtsanwalts-Partnerschaft` (organisation)
- `Bezirksgerichts Graz-Ost` (organisation)

**Example 41** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_5`)


Dr. Felix Cornils, Niederlande, beide vertreten durch Tramposch & Partner, Rechtsanwälte KG in Innsbruck, gegen die beklagte Partei Mag.a Constanze Rizzo, vertreten durch König Ermacora Klotz & Partner, Rechtsanwälte in Innsbruck, wegen je 15.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 1. Juli 2020, GZ 10 R 16/20h-49, mit dem das Urteil des Landesgerichts Innsbruck vom 6. Februar 2020, GZ 41 Cg 11/19i-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Dr. Felix Cornils` (person)
- `Tramposch & Partner, Rechtsanwälte KG` (organisation)
- `Mag.a Constanze Rizzo` (person)
- `Oberlandesgerichts Innsbruck` (organisation)

**Example 42** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Pflegschaftssache 1. der mj Emma Mittelstaedt, geboren am 21. Mai 2025 und 2. des mj Milena Roesche, geboren am 25. Juni 1957, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung Bezirk 22, 1220 Wien, Hirschstettner Straße 19-21/Stiege N), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 10. Dezember 2014, GZ 42 R 343/13x, 42 R 344/13v und 42 R 345/13s-106, womit den Rekursen der Minderjährigen gegen den Beschluss des Bezirksgerichts Donaustadt vom 14. März 2013, GZ 3 Pu 61/12x-40, teilweise Folge gegeben wurde (Pkt 1 des Spruchs), dem Rekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen die Beschlüsse des Bezirksgerichts Donaustadt (jeweils) vom 6. Juni 2013, GZ 3 Pu 61/12x-49 und 3 Pu 61/12x-50, Folge gegeben (Pkt 2a des Spruchs), und aus Anlass des Rekurses die Anträge der Minderjährigen auf Gewährung von Unterhaltsvorschüssen zur Gänze abgewiesen wurden (Pkt 2b des Spruchs), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

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
- `Magistrat der Stadt Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Bezirksgerichts Donaustadt` (organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/10Ob43_19z`) (sent_id: `deanon_260716_TRAIN/10Ob43_19z_3`)


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

**Example 44** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_9`)


Im Rahmen seiner Äußerung zu diesem Unterhaltserhöhungsantrag lehnte der Antragsgegner jeweils alle Richter des Bezirksgerichts Josefstadt und des diesem übergeordneten Landesgerichts für Zivilrechtssachen Wien ab.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Bezirksgerichts Josefstadt` (organisation)

**Example 45** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_12`)


Da mehrere Senate des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht an dem genannten Verhalten beteiligt gewesen seien, sei auch das gesamte Landesgericht für Zivilrechtssachen Wien als befangen anzusehen, über den nunmehr geltend gemachten Unterhaltsanspruch zu entscheiden.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |
| `Landesgericht für Zivilrechtssachen Wien` | `Landesgericht für Zivilrechtssachen Wien` |

**Example 46** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_32`)


2.2 Von diesen Grundsätzen der Rechtsprechung ist das Oberlandesgericht Wien bei seiner Entscheidung nicht abgewichen, wenn es den Ablehnungsantrag gegen alle Richter und Richterinnen des Landesgerichts für Zivilrechtssachen Wien und des Bezirksgerichts Josefstadt als nicht dem Gesetz gemäß ausgeführt zurückgewiesen hat.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)
- `Bezirksgerichts Josefstadt` (organisation)

**Example 47** (doc_id: `deanon_260716_TRAIN/10Ob57_13z`) (sent_id: `deanon_260716_TRAIN/10Ob57_13z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der Kinder Mikolaj Eleftheriadou, geboren am 9. August 1991, Helge Schuchmann, geboren am 30. September 1992, mj Isabel Rahnfeld, geboren am 22. Dezember 1998 und mj PhD Daniel Coutand, geboren am 18. Jänner 2001, wegen Unterhaltsvorschuss, infolge Revisionsrekurses des Vaters Mag. Dirk Hükelheim, vertreten durch Mag. Roland Marko, Rechtsanwalt in Wien, dieser vertreten durch Dr. Francisco Rumpf, Rechtsanwalt in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 7. Juni 2013, GZ 43 R 391/08f ua -U-458, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 12. November 2007, GZ 2 P 88/07t-U-238, abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Wien` | `Landesgerichts für Zivilrechtssachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mikolaj Eleftheriadou` (person)
- `Helge Schuchmann` (person)
- `Isabel Rahnfeld` (person)
- `PhD Daniel Coutand` (person)
- `Mag. Dirk Hükelheim` (person)
- `Mag. Roland Marko` (person)
- `Dr. Francisco Rumpf` (person)
- `Bezirksgerichts Innere Stadt Wien` (organisation)

**Example 48** (doc_id: `deanon_260716_TRAIN/10Ob6_24s`) (sent_id: `deanon_260716_TRAIN/10Ob6_24s_3`)


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

**Example 49** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Ing. Christian Stangl-Brachnik, MA BA und Mag. Claudia Gründel (beide aus dem Kreis der Arbeitgeber) als weitere Richter in der Sozialrechtssache der klagenden Partei Mathias Jendl, vertreten durch Dr. Thomas Stampfer und Dr. Christoph Orgler, Rechtsanwälte in Graz, gegen die beklagte Partei Sozialversicherungsanstalt der Bauern, 1031 Wien, Ghegastraße 1, vertreten durch Dr. Michael Stögerer, Rechtsanwalt in Wien, wegen Ausgleichszulage, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2017, GZ 7 Rs 37/17s-11, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. April 2017, GZ 43 Cgs 113/17p-7, teils bestätigt und teils abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Graz` | `Landesgerichts für Zivilrechtssachen Graz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Ing. Christian Stangl-Brachnik, MA BA` (person)
- `Mag. Claudia Gründel` (person)
- `Mathias Jendl` (person)
- `Dr. Thomas Stampfer` (person)
- `Dr. Christoph Orgler` (person)
- `Dr. Michael Stögerer` (person)
- `Oberlandesgerichts Graz` (organisation)

**Example 50** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_3`)


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

**Example 51** (doc_id: `deanon_260716_TRAIN/10ObS99_15d`) (sent_id: `deanon_260716_TRAIN/10ObS99_15d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die fachkundigen Laienrichter Mag. Dr. Wolfgang Höfle (aus dem Kreis der Arbeitgeber) und Ing. Thomas Bauer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Willibald Kollowrat, BEd, vertreten durch Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH in Graz, gegen die beklagte Partei Versicherungsanstalt für Eisenbahnen und Bergbau, Linke Wienzeile 48-52, 1060 Wien, vertreten durch Dr. Marie-Luise Safranek, Rechtsanwältin in Graz, wegen Wochengeld, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Juni 2015, GZ 7 Rs 28/15i-9, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 25. Februar 2015, GZ 36 Cgs 216/14d-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts für Zivilrechtssachen Graz` | `Landesgerichts für Zivilrechtssachen Graz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Mag. Dr. Wolfgang Höfle` (person)
- `Ing. Thomas Bauer` (person)
- `Willibald Kollowrat, BEd` (person)
- `Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH` (organisation)
- `Versicherungsanstalt für Eisenbahnen und Bergbau` (organisation)
- `Dr. Marie-Luise Safranek` (person)
- `Oberlandesgerichts Graz` (organisation)

**Example 52** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_3`)


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

**Example 53** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_4`)


In Stattgebung der Nichtigkeitsbeschwerde wird das angefochtene Urteil aufgehoben, eine neue Hauptverhandlung angeordnet und die Sache an das Landesgericht Salzburg verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Example 54** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_3`)


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

**Example 55** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_4`)


Gründe:  Rechtliche Beurteilung Mit dem angefochtenen Beschluss wurde die von Richard Lilienfein erhobene Nichtigkeitsbeschwerde gegen das Urteil des Landesgerichts Salzburg vom 17. Juni 2011, GZ 40 Hv 147/10g-538, als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Richard Lilienfein` (person)

**Example 56** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_8`)


Die von Richard Leissner gegen das ihn freisprechende Urteil des Einzelrichters des Landesgerichts Salzburg vom 17. Juni 2011 ausdrücklich an den Obersten Gerichtshof gerichtete Nichtigkeitsbeschwerde wurde vom Erstgericht zutreffend gemäß § 285a Z 1 StPO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Richard Leissner` (person)
- `Obersten Gerichtshof` (organisation)

**Example 57** (doc_id: `deanon_260716_TRAIN/11Os59_13f`) (sent_id: `deanon_260716_TRAIN/11Os59_13f_3`)


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

**Example 58** (doc_id: `deanon_260716_TRAIN/11Os67_16m`) (sent_id: `deanon_260716_TRAIN/11Os67_16m_3`)


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

**Example 59** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_4`)


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

**Example 60** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_5`)


Gründe:  Rechtliche Beurteilung Der gegen den Beschluss des Oberlandesgerichts Wien, mit dem eine Beschwerde des Gerald Wandscheer gegen den Beschluss des Landesgerichts Korneuburg vom 21. Februar 2018, GZ 606 Hv 1/17k-94, als verspätet zurückgewiesen worden war, gerichtete „Einspruch“ war ebenso zurückzuweisen, weil gegen derartige Entscheidungen eines Beschwerdegerichts kein weiterer Rechtszug vorgesehen ist (§ 89 Abs 6 StPO).

| Predicted | Gold |
|---|---|
| `Landesgerichts Korneuburg` | `Landesgerichts Korneuburg` |

**Missed by this rule (FN):**

- `Oberlandesgerichts Wien` (organisation)
- `Gerald Wandscheer` (person)

**Example 61** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_3`)


Kopf Der Oberste Gerichtshof hat am 16. März 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Brenner in der Strafvollzugssache des Oliver Pekarek, AZ 39 Ns 43/15i des Landesgerichts Krems an der Donau, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `Landesgerichts Krems an der Donau` | `Landesgerichts Krems an der Donau` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Brenner` (person)
- `Oliver Pekarek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `OGH` (organisation)

**Example 62** (doc_id: `deanon_260716_TRAIN/12Ns94_11m`) (sent_id: `deanon_260716_TRAIN/12Ns94_11m_3`)


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

**Example 63** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Thomas Michenfelder wegen des Verbrechens des schweren gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 2 und Z 5, 129 Abs 1 Z 1, Z 2 und Z 3, 130 Abs 2 zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 38 Hv 40/18z des Landesgerichts Krems an der Donau, über die von der Generalprokuratur gegen den Beschluss des Präsidenten des Oberlandesgerichts Wien vom 17. Oktober 2018, AZ 130 Ns 31/18w, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Mag. Gföller und der Verteidigerin Dr. Zeh-Gindl zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts Krems an der Donau` | `Landesgerichts Krems an der Donau` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Dr. Mann` (person)
- `Dr. Brenner` (person)
- `Mag. Rögner` (person)
- `Thomas Michenfelder` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Mag. Gföller` (person)
- `Dr. Zeh-Gindl` (person)

**Example 64** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_5`)


Dieser Beschluss wird aufgehoben und es wird in der Sache selbst erkannt, dass der Senatspräsident des Oberlandesgerichts Wien Dr. Krenn sowie die Richterinnen des Oberlandesgerichts Wien Mag. Edwards und Mag. Sanda von der Entscheidung über die Berufung des Angeklagten gegen das Urteil des Landesgerichts Krems an der Donau vom 8. August 2018, GZ 38 Hv 40/18z-100, nicht ausgeschlossen sind.

| Predicted | Gold |
|---|---|
| `Landesgerichts Krems an der Donau` | `Landesgerichts Krems an der Donau` |

**Missed by this rule (FN):**

- `Oberlandesgerichts Wien` (organisation)
- `Dr. Krenn` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Mag. Edwards` (person)
- `Mag. Sanda` (person)

**Example 65** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_6`)


Text Gründe: Soweit für die Behandlung der Nichtigkeitsbeschwerde zur Wahrung des Gesetzes von Bedeutung wurde Thomas Maksym mit Urteil des Landesgerichts Krems an der Donau vom 13. März 2018 (ON 72) des Verbrechens des schweren gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 2 und Z 5, 129 Abs 1 Z 1, Z 2 und Z 3, 130 Abs 2 zweiter Fall und 15 StGB (I./) sowie der Vergehen der Urkundenunterdrückung nach § 229 Abs 1 StGB (II./) und des Betrugs nach § 146 StGB (III./) schuldig erkannt und zu einer Freiheitsstrafe verurteilt. Aus Anlass der (allein aufrechterhaltenen) Berufung des Angeklagten wegen des Ausspruchs über die Strafe (ON 86) hob der zuständige 21.

| Predicted | Gold |
|---|---|
| `Landesgerichts Krems an der Donau` | `Landesgerichts Krems an der Donau` |

**Missed by this rule (FN):**

- `Thomas Maksym` (person)

**Example 66** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_10`)


Im zweiten Rechtsgang sprach die Einzelrichterin des Landesgerichts Krems an der Donau Thomas Muthardt mit Urteil vom 8. August 2018 (ON 100) neuerlich anklagekonform schuldig und verurteilte ihn zu einer Freiheitsstrafe.

| Predicted | Gold |
|---|---|
| `Landesgerichts Krems an der Donau` | `Landesgerichts Krems an der Donau` |

**Missed by this rule (FN):**

- `Thomas Muthardt` (person)

**Example 67** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_13`)


Dazu führte er aus, dass die genannten Richter das Urteil des Landesgerichts Krems an der Donau vom 13. März 2018 (ON 72) in amtswegiger Wahrnehmung des Nichtigkeitsgrundes des § 281 Abs 1 Z 9 lit a [der Sache nach Z 10] StPO „großteils aufgehoben“ und „dabei“ „die Tatfrage mit Hinweis auf die Strafbarkeit des angelasteten Verhaltens indizierende Verfahrensergebnisse mit voller Kognitionsbefugnis [beurteilt] und […] beweiswürdigend Stellung bezogen“ hätten.

| Predicted | Gold |
|---|---|
| `Landesgerichts Krems an der Donau` | `Landesgerichts Krems an der Donau` |

**Example 68** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__9`)


Unter einem erging der Beschluss, gemäß § 494a Abs 1 Z 2 StPO vom Widerruf der zum AZ 36 Hv 118/05p des Landesgerichts Innsbruck und zum AZ 3 U 350/06d des Bezirksgerichts Kufstein jeweils gewährten bedingten Strafnachsicht abzusehen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Bezirksgerichts Kufstein` (organisation)

**Example 69** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_3`)


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

**Example 70** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_4`)


In Stattgebung der Nichtigkeitsbeschwerde wird das angefochtene Urteil, das im Übrigen unberührt bleibt, im Ausspruch über den Verfall aufgehoben, soweit er sich auf einen 35.353,95 Euro übersteigenden Betrag bezieht, und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an den Einzelrichter des Landesgerichts Innsbruck verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Example 71** (doc_id: `deanon_260716_TRAIN/12Os31_19d`) (sent_id: `deanon_260716_TRAIN/12Os31_19d_26`)


In Stattgebung der Nichtigkeitsbeschwerde des Angeklagten war daher das angefochtene Urteil wie im Spruch ersichtlich aufzuheben und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an den Einzelrichter des Landesgerichts Innsbruck (§ 445 Abs 2 StPO;

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Example 72** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_3`)


Kopf Der Oberste Gerichtshof hat am 8. April 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Holzweber als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll, Dr. Schwab, Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger in Gegenwart der Richteramtsanwärterin Mag. Bayer als Schriftführerin in der Strafsache gegen Dr. Ernst-Peter Nepomuk Lieschke wegen des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB über die Beschwerde des Verurteilten gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 19. Jänner 2010, AZ 20 Bs 461/09d (GZ 20 Hv 73/09p-19 des Landesgerichts St. Pölten), nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts St. Pölten` | `Landesgerichts St. Pölten` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Holzweber` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Dr. Schwab` (person)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Hetlinger` (person)
- `Mag. Bayer` (person)
- `Dr. Ernst` (person)
- `Nepomuk Lieschke` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 73** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_4`)


Text G r ü n d e : Mit Urteil des Einzelrichters des Landesgerichts St. Pölten vom 18. September 2009, GZ 20 Hv 73/09p-13, wurde Dr. Ernst-Peter Paula Langehanke des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB schuldig erkannt und zu einer für eine Probezeit von drei Jahren bedingt nachgesehenen Freiheitsstrafe von vier Wochen verurteilt. Der vom Angeklagten dagegen erhobenen Berufung wegen Nichtigkeit, Schuld und Strafe gab das Oberlandesgericht Wien mit der nunmehr angefochtenen Entscheidung keine Folge (ON 19).

| Predicted | Gold |
|---|---|
| `Landesgerichts St. Pölten` | `Landesgerichts St. Pölten` |

**Missed by this rule (FN):**

- `Dr. Ernst` (person)
- `Paula Langehanke` (person)
- `Oberlandesgericht Wien` (organisation)

**Example 74** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_3`)


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

**Example 75** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_4`)


Im Verfahren AZ 51 Hv 32/13i des Landesgerichts Feldkirch, verletzt die Unterlassung der nachstehend angeführten Zustellungen an den gesetzlichen Vertreter des jugendlichen Beschuldigten Johannes Büffel das Gesetz, und zwar 1./ des Antrags der Staatsanwaltschaft vom 12. März 2014 auf Wiederaufnahme des Strafverfahrens (ON 29) zur Gegenäußerung binnen 14 Tagen in § 38 Abs 1 JGG iVm § 357 Abs 2 erster Satz StPO; 2./ des Beschlusses vom 4. Mai 2014 auf Wiederaufnahme des Strafverfahrens (ON 35) in § 38 Abs 3 erster Satz JGG iVm § 86 Abs 2 StPO iVm § 87 Abs 1 StPO.

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Johannes Büffel` (person)

**Example 76** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_5`)


Der zuletzt bezeichnete Beschluss wird aufgehoben und die Sache zu neuer Entscheidung über den Antrag der Staatsanwaltschaft vom 12. März 2014 auf Wiederaufnahme des Strafverfahrens (ON 29) an das Landesgericht Feldkirch verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgericht Feldkirch` | `Landesgericht Feldkirch` |

**Example 77** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_6`)


Text Gründe: In der Jugendstrafsache AZ 51 Hv 32/13i des Landesgerichts Feldkirch legte die Staatsanwaltschaft Feldkirch mit Strafantrag vom 18. April 2013, AZ 9 St 82/13f, dem am 23. August 1996 geborenen Angeklagten Johannes Bednorz als Vergehen der fortgesetzten Gewaltausübung nach § 107b Abs 1 und Abs 2 StGB (I./) sowie der Nötigung nach den §§ 15 Abs 1, 105 Abs 1 StGB (II./, III./1./), der gefährlichen Drohung nach § 107 Abs 1 StGB (III./2./) und der Sachbeschädigung nach § 125 StGB (III./3./) qualifiziertes Verhalten zum Nachteil der Sabrina Hemmersdorfer zur Last (ON 3).

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Johannes Bednorz` (person)
- `Sabrina Hemmersdorfer` (person)

**Example 78** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_7`)


Mit gekürzt ausgefertigtem Urteil der Einzelrichterin in Jugendstrafsachen des Landesgerichts Feldkirch vom 5. Juni 2013 wurde der jugendliche Angeklagte mehrerer Vergehen schuldig erkannt, jedoch von der Anklage (I./), er habe in Heinrich-Prosl-Gasse 6, 2034 Großharras, Österreich im Zeitraum von März 2012 bis Ende Februar 2013 gegen Sabrina Höllerl eine längere Zeit hindurch fortgesetzt Gewalt ausgeübt, indem er sie mehr als zehnmal mit Fäusten gegen den Bauch und gegen das Gesicht geschlagen habe, wodurch diese teilweise Prellungen und Schürfwunden erlitten habe, mangels Schuldbeweises gemäß § 259 Z 3 StPO freigesprochen (ON 14).

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Heinrich-Prosl-Gasse 6, 2034 Großharras, Österreich` (address)
- `Sabrina Höllerl` (person)

**Example 79** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_8`)


Aus Anlass des ihre polizeilichen Angaben abschwächenden und zum oben angeführten Freispruch führenden Aussageverhaltens der Zeugin Sabrina Härtel in der Hauptverhandlung vom 5. Juni 2013 (ON 13 S 5 ff) erhob die Staatsanwaltschaft Feldkirch am 20. Juni 2013 zu AZ 9 St 131/13m in der Jugendstrafsache AZ 20 Hv 68/13f des Landesgerichts Feldkirch Strafantrag (ON 4 des zuletzt bezeichneten Aktes) gegen die Genannte wegen des Verdachts der am 8. März 2013 und am 15. März 2013 in Franz Schuster-Straße 8, 8212 Kleinpesendorf, Österreich im Ermittlungsverfahren gegen Johannes Breenkötter begangenen Vergehen der falschen Beweisaussage nach § 288 Abs 1 und Abs 4 StGB (I./) sowie der Verleumdung nach § 297 Abs 1 zweiter Fall StGB (II./).

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Sabrina Härtel` (person)
- `Franz Schuster-Straße 8, 8212 Kleinpesendorf, Österreich` (address)
- `Johannes Breenkötter` (person)

**Example 80** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_9`)


Nachdem die Angeklagte Sabrina Heckel in der Hauptverhandlung am 24. Juli 2013 angegeben hatte, als Zeugin nicht vor der Polizei, sondern in der Hauptverhandlung am 5. Juni 2013 gegen Johannes Butze falsch ausgesagt zu haben, gab die Staatsanwaltschaft noch in dieser Hauptverhandlung eine Alternativanklage zu Protokoll, der zufolge sie als Zeugin in der Hauptverhandlung am 5. Juni 2013 gegen Johannes Bulthaup vor dem Landesgericht Feldkirch die Vergehen der falschen Beweisaussage nach § 288 Abs 1 StGB (III./) und der Begünstigung nach § 299 Abs 1 StGB (IV./) begangen habe (ON 10 S 3 f des Aktes AZ 51 Hv 46/13y des Landesgerichts Feldkirch).

| Predicted | Gold |
|---|---|
| `Landesgericht Feldkirch` | `Landesgericht Feldkirch` |
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Sabrina Heckel` (person)
- `Johannes Butze` (person)
- `Johannes Bulthaup` (person)

**Example 81** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_10`)


Mit gekürzt ausgefertigtem Urteil des Landesgerichts Feldkirch vom 2. September 2013, GZ 20 Hv 68/13f-13, wurde Sabrina Harrazin im Sinne dieser Alternativanklage schuldig erkannt.

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Sabrina Harrazin` (person)

**Example 82** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_11`)


Hierauf beantragte die Staatsanwaltschaft Feldkirch in dem Johannes Bergknecht betreffenden Verfahren AZ 51 Hv 32/13i des Landesgerichts Feldkirch am 12. März 2014 gemäß § 355 StPO iVm § 352 Abs 1 Z 1 StPO die Wiederaufnahme des Strafverfahrens im Umfang des am 5. Juni 2013 ergangenen Freispruchs des Angeklagten Johannes Bertrang, weil dieser durch die falsche Beweisaussage der Zeugin Sabrina Holzschuher herbeigeführt worden sei (ON 29).

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Johannes Bergknecht` (person)
- `Johannes Bertrang` (person)
- `Sabrina Holzschuher` (person)

**Example 83** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_13`)


Mit Beschluss des Einzelrichters des Landesgerichts Feldkirch vom 4. Mai 2014, GZ 51 Hv 32/13i-35, wurde in Stattgebung des Antrags der Staatsanwaltschaft das Strafverfahren gegen Johannes Braentel wegen § 107b Abs 1 und Abs 2 StGB gemäß § 355 StPO im Umfang des rechtskräftigen Freispruchs wiederaufgenommen und das Urteil des Landesgerichts Feldkirch vom 5. Juni 2013 (ON 14) umfänglich des Freispruchs aufgehoben.

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Johannes Braentel` (person)

**Example 84** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_15`)


Die Staatsanwaltschaft Feldkirch erhob am 14. August 2014 zu AZ 9 St 82/13f hinsichtlich des dem seinerzeitigen Freispruch zu Grunde liegenden Vorwurfs Strafantrag gegen Johannes Brookhoff (ON 36 in dem das wiederaufgenommene Verfahren betreffenden Akt AZ 39 Hv 64/14h des Landesgerichts Feldkirch).

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Johannes Brookhoff` (person)

**Example 85** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_16`)


Anlässlich der Ausschreibung der Hauptverhandlung im wiederaufgenommenen Verfahren für den 24. September 2014 wurde dem Angeklagten ein Verfahrenshilfeverteidiger beigegeben (ON 38 im Akt AZ 39 Hv 64/14h des Landesgerichts Feldkirch).

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Example 86** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_18`)


Am 1. Oktober 2014 verfügte das Landesgericht Feldkirch die Zustellung der „ON 35“ (gemeint sichtlich: des Beschlusses auf Wiederaufnahme des Strafverfahrens ON 35 im Akt AZ 51 Hv 32/13i und ON 47 im Akt AZ 39 Hv 64/14h jeweils des Landesgerichts Feldkirch) an „die Erziehungsberechtigte des Johannes Bauckloh “, worauf der seinerzeitigen gesetzlichen Vertreterin (der Mutter) des nunmehr volljährigen Angeklagten der Beschluss am 3. Oktober 2014 eigenhändig zugestellt wurde (ON 42 S 3).

| Predicted | Gold |
|---|---|
| `Landesgericht Feldkirch` | `Landesgericht Feldkirch` |
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Johannes Bauckloh` (person)

**Example 87** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_19`)


Am 17. Oktober 2014 langte beim Landesgericht Feldkirch zu AZ 51 Hv 32/13i eine vom Verfahrenshilfeverteidiger im Verfahren AZ 39 Hv 64/14h dieses Landesgerichts verfasste Beschwerde des Angeklagten Johannes Bartlmäß (ON 42 im Akt AZ 51 Hv 32/13i des Landesgerichts Feldkirch) gegen den Beschluss des Landesgerichts Feldkirch vom 4. Mai 2014 auf Wiederaufnahme des Strafverfahrens ein.

| Predicted | Gold |
|---|---|
| `Landesgericht Feldkirch` | `Landesgericht Feldkirch` |
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Johannes Bartlmäß` (person)

**Example 88** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_20`)


Mit Beschluss des Oberlandesgerichts Innsbruck als Beschwerdegericht vom 25. November 2014, AZ 11 Bs 326/14z, 349/14g (ON 47 im Akt AZ 51 Hv 32/13i des Landesgerichts Feldkirch bzw ON 52 im Akt AZ 39 Hv 64/14h dieses Landesgerichts), wurde die Beschwerde als unzulässig (verspätet) zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Feldkirch` | `Landesgerichts Feldkirch` |

**Missed by this rule (FN):**

- `Oberlandesgerichts Innsbruck` (organisation)

**Example 89** (doc_id: `deanon_260716_TRAIN/13Os105_19v`) (sent_id: `deanon_260716_TRAIN/13Os105_19v_3`)


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

**Example 90** (doc_id: `deanon_260716_TRAIN/13Os105_19v`) (sent_id: `deanon_260716_TRAIN/13Os105_19v_4`)


Text Gründe: Mit Urteil des Landesgerichts Innsbruck als Schöffengericht vom 19. November 2018, GZ 37 Hv 122/18b-17, wurde – soweit hier von Bedeutung – Roman Ungetühm mehrerer strafbarer Handlungen schuldig erkannt und zu einer Freiheitsstrafe verurteilt. Mit Beschluss vom 2. April 2019, GZ 11 Os 22/19y-4, wies der Oberste Gerichtshof die von Roman Ulucan dagegen aus Z 11 des § 281 Abs 1 StPO erhobene Nichtigkeitsbeschwerde gemäß § 285d Abs 1 StPO bei nichtöffentlicher Beratung sofort zurück.

| Predicted | Gold |
|---|---|
| `Landesgerichts Innsbruck` | `Landesgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Roman Ungetühm` (person)
- `Oberste Gerichtshof` (organisation)
- `Roman Ulucan` (person)

**Example 91** (doc_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a__3`)


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

**Example 92** (doc_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a__4`)


In der Strafsache AZ 25 Hv 30/17m des Landesgerichts Eisenstadt verletzt die Unterlassung der Verlesung des Europäischen Haftbefehls vom 27. Juli 2015 (ON 44) und der Mitteilung des ungarischen Justizministeriums vom 26. November 2015 (ON 125) in der Hauptverhandlung (ON 154) § 252 Abs 2 StPO.

| Predicted | Gold |
|---|---|
| `Landesgerichts Eisenstadt` | `Landesgerichts Eisenstadt` |

**Example 93** (doc_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a_`) (sent_id: `deanon_260716_TRAIN/13Os110_19d_13Os111_19a__5`)


Das Urteil des Landesgerichts Eisenstadt vom 6. Juni 2017 (ON 155) wird aufgehoben, eine neue Hauptverhandlung angeordnet und die Sache an das Landesgericht Eisenstadt verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Eisenstadt` | `Landesgerichts Eisenstadt` |
| `Landesgericht Eisenstadt` | `Landesgericht Eisenstadt` |

**Example 94** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__3`)


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

**Example 95** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__4`)


Es verletzen (1) das Urteil des Landesgerichts Salzburg als Schöffengericht vom 28. Oktober 2015, GZ 41 Hv 49/15k-33, § 31 Abs 1 erster Satz StGB und (2) der unter einem verkündete Beschluss auf Absehen vom Widerruf der Nikola Mehlhose mit Urteil des Landesgerichts Salzburg vom 10. September 2014, GZ 47 Hv 86/14v-7, gewährten bedingten Strafnachsicht § 494a Abs 1 Z 2 StPO.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Nikola Mehlhose` (person)

**Example 96** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__5`)


Das Urteil des Landesgerichts Salzburg als Schöffengericht vom 28. Oktober 2015, GZ 41 Hv 49/15k-33, das im Übrigen unberührt bleibt, wird im Nikola Meine betreffenden Strafausspruch aufgehoben und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an das Landesgericht Salzburg verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |
| `Landesgericht Salzburg` | `Landesgericht Salzburg` |

**Missed by this rule (FN):**

- `Nikola Meine` (person)

**Example 97** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__6`)


Gründe:  Rechtliche Beurteilung Mit in Rechtskraft erwachsenem Urteil des Landesgerichts Salzburg vom 10. September 2014, GZ 47 Hv 86/14v-7, wurde Nikola Miscenko wegen des Vergehens des Betrugs nach § 146 StGB zu einer unter Bestimmung einer dreijährigen Probezeit bedingt nachgesehenen Freiheitsstrafe von vier Monaten verurteilt. Mit Urteil des Landesgerichts Salzburg vom 28. Oktober 2015, GZ 41 Hv 49/15k-33, das auch einen Schuldspruch eines anderen Angeklagten enthält, wurde der Genannte wegen eines am 27. Mai 2012 begangenen Vergehens schuldig erkannt und hierfür eine weitere Sanktion verhängt.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Nikola Miscenko` (person)

**Example 98** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__7`)


Unter einem fasste das Gericht neben anderen Aussprüchen auch den Beschluss, vom Widerruf der Nikola Mikeska mit Urteil des Landesgerichts Salzburg vom 10. September 2014, GZ 47 Hv 86/14v-7, gewährten bedingten Strafnachsicht abzusehen.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

**Missed by this rule (FN):**

- `Nikola Mikeska` (person)

**Example 99** (doc_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i_`) (sent_id: `deanon_260716_TRAIN/13Os113_17t_13Os114_17i__10`)


Da das Urteil des Landesgerichts Salzburg als Schöffengericht vom 28. Oktober 2015 auf das Erkenntnis vom 10. September 2014 nicht Bedacht nimmt, verstößt es gegen die genannte Bestimmung.

| Predicted | Gold |
|---|---|
| `Landesgerichts Salzburg` | `Landesgerichts Salzburg` |

</details>

---

## `Magistrat_Wien` 

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `b3f6167e`  
**Description:**
Matches the Magistrat der Stadt Wien.

**Content:**
```
\bMagistrat\s+der\s+Stadt\s+Wien\b
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

## `Verein_Organisation` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d6aad400`  
**Description:**
Matches organizations starting with 'Verein' (Association) capturing the full name.

**Content:**
```
\bVerein\s+für\s+[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.001 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 3806 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob18_13i`) (sent_id: `deanon_260716_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei SüdSanitär Gruppe GmbH, Rinzendorf 28, 4501 Lindach, Österreich, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Verein für Konsumenteninformation` | `Verein für Konsumenteninformation` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Dr. Walter Reichholf` (person)
- `SüdSanitär Gruppe GmbH` (organisation)
- `Rinzendorf 28, 4501 Lindach, Österreich` (address)
- `Kraft & Winternitz Rechtsanwälte GmbH` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/6Ob56_19g`) (sent_id: `deanon_260716_TRAIN/6Ob56_19g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1060 Wien, Linke Wienzeile 18, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei QUMV Pflege GmbH, Nordring 89q, 2770 Gutenstein, Österreich, vertreten durch Dr. Peter Lindinger Dr. Andreas Pramer GesbR, Rechtsanwälte in Linz, wegen Unterlassung und Urteilsveröffentlichung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2019, GZ 3 R 141/18b-17, mit dem über Berufungen der klagenden und der beklagten Partei das Urteil des Landesgerichts Linz vom 2. September 2018, GZ 31 Cg 4/18a-9, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Verein für Konsumenteninformation` | `Verein für Konsumenteninformation` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schramm` (person)
- `Dr. Gitschthaler` (person)
- `Univ.-Prof. Dr. Kodek` (person)
- `Dr. Nowotny` (person)
- `Dr. Faber` (person)
- `Kosesnik-Wehrle & Langer Rechtsanwälte KG` (organisation)
- `QUMV Pflege GmbH` (organisation)
- `Nordring 89q, 2770 Gutenstein, Österreich` (address)
- `Dr. Peter Lindinger` (person)
- `Dr. Andreas Pramer` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Linz` (organisation)

</details>

---

## `Landesgericht_Strafsachen` 🏆

**F1:** 0.048 | **Precision:** 1.000 | **Recall:** 0.025  

**Format:** `regex`  
**Rule ID:** `29819c24`  
**Description:**
Matches Regional Courts for Criminal Matters (Landesgericht für Strafsachen).

**Content:**
```
\bLandesgerichts?\s+für\s+Strafsachen\s+(?:Wien|Linz|Salzburg|Innsbruck|Graz|Klagenfurt|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|St.\s+Pölten|Eisenstadt)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.025 | 0.048 | 99 | 99 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 99 | 0 | 3421 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_12`)


Mit Beschluss des Landesgerichts für Strafsachen Graz vom 18.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Example 1** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_14`)


Mit Urteil des Landesgerichts für Strafsachen Graz vom 14. 12. 2016, 222 Hv 68/16m, wurde er gemäß § 21 Abs 1 StGB in eine Anstalt für geistig abnorme Rechtsbrecher eingewiesen, wo er seit 20.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Example 2** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_3`)


Kopf Der Oberste Gerichtshof hat am 18. März 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski im Verfahren zur Unterbringung des Mag. Herwig Bäseke in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB, AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz gemäß § 62 Abs 1 zweiter Satz OGH-Geo 2019 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger sowie Mag. Fürnkranz sind von der Entscheidung über die Anträge des Mag. Herwig Berto auf Erneuerung des Strafverfahrens AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, ausgeschlossen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Herwig Bäseke` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Fürnkranz` (person)
- `OGH` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Fürnkranz` (person)
- `Mag. Herwig Berto` (person)

**Example 3** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_8`)


Der vorliegende Antrag des Mag. Herwig Bleuler bezieht sich auf das Urteil des Oberlandesgerichts Wien vom 21. August 2019, AZ 17 Bs 168/19h, mit dem der Berufung des Betroffenen gegen das Urteil des Landesgerichts für Strafsachen Wien vom 14. November 2018, GZ 22 Hv 7/18k-350, nicht Folge gegeben wurde.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Mag. Herwig Bleuler` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_9`)


Dieses Verfahren hat unter anderem auch als mit Strafe bedrohte Handlungen iSd § 107 Abs 1 und 2 erster Fall StGB subsumierte Anlasstaten zum Nachteil der genannten Richter des Obersten Gerichtshofs zum Gegenstand (US 7, 10 des erwähnten Urteils des Landesgerichts für Strafsachen Wien).

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_3`)


Kopf Der Oberste Gerichtshof hat am 11. März 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Dr. Oshidari als weitere Richter in der Strafsache gegen Gerhard Bukowska wegen des Verbrechens des schweren gewerbsmäßigen Betrugs nach §§ 146, 147 Abs 3, 148 erster Fall, 15 Abs 1 StGB und weiterer strafbarer Handlungen, AZ 16 Hv 20/14x des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätin des Obersten Gerichtshofs Mag. Michel gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Dr. Oshidari` (person)
- `Gerhard Bukowska` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Michel` (person)
- `OGH` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_4`)


2005 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab und Hofrätin des Obersten Gerichtshofs Mag. Michel sind von der Entscheidung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Gerhard Boesl betreffend das Verfahren AZ 16 Hv20/14x des Landesgerichts für Strafsachen Wien ausgeschlossen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Michel` (person)
- `Gerhard Boesl` (person)

**Example 7** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_6`)


Gründe:  Rechtliche Beurteilung Der Oberste Gerichtshof hat zu AZ 11 Os 5/15t über die gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 14. Oktober 2014, GZ 16 Hv 20/14x-3462, ergriffene Nichtigkeitsbeschwerde und Berufung des Angeklagten Gerhard Bugnenings zu entscheiden.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Gerhard Bugnenings` (person)

**Example 8** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_14`)


Senat des Obersten Gerichtshofs - unter dem Aspekt der §§ 281 Abs 1 Z 5a, 362 StPO - auch der Tatverdacht hinsichtlich eines Tatzeitraums („August 2008 bis längstens 14. Dezember 2008“ - vgl Urteil des Landesgerichts für Strafsachen Wien vom 14. Oktober 2014, GZ 16 Hv 20/14x-3462, US 2) zu prüfen, auf den sich auch das Oberlandesgericht Wien in Entscheidungen bezog, die unter Mitwirkung der Angehörigen des Anzeigers getroffen wurden (vgl insb BS 32 f in AZ 19 Bs 465/12i).

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Oberlandesgericht Wien` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_3`)


Kopf Der Oberste Gerichtshof hat am 9. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Brenner und Dr. Setz-Hummel in der Strafsache gegen Ahmed Koehnen wegen des Verbrechens des Mordes nach § 75 StGB, AZ 606 Hv 1/11m des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit der Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Brenner` (person)
- `Dr. Setz-Hummel` (person)
- `Ahmed Koehnen` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `OGH` (organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_7`)


Mit dem erwähnten Beschluss vom 25. November 2019 hatte das Oberlandesgericht Wien einer Beschwerde des Ahmed Kocks gegen einen Beschluss des Landesgerichts für Strafsachen Wien auf Ablehnung eines Antrags des Genannten auf Wiederaufnahme des Verfahrens AZ 606 Hv 1/11m jenes Gerichts nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)
- `Ahmed Kocks` (person)

**Example 11** (doc_id: `deanon_260716_TRAIN/12Os152_12p`) (sent_id: `deanon_260716_TRAIN/12Os152_12p_3`)


Kopf Der Oberste Gerichtshof hat am 13. Dezember 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Fruhmann als Schriftführerin in der Strafsache gegen unbekannte Täter wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB, AZ 130 Bl 65/12s des Landesgerichts für Strafsachen Wien, über die Beschwerde des Gebhard Sayin gegen den Beschluss des Oberlandesgerichts Wien vom 23. Oktober 2012, AZ 17 Bs 410/12m, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Michel` (person)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Fruhmann` (person)
- `Gebhard Sayin` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/12Os152_12p`) (sent_id: `deanon_260716_TRAIN/12Os152_12p_4`)


Text Gründe: Mit der angefochtenen Entscheidung wies das Oberlandesgericht Wien die Beschwerde des Gebhard Senkfeil gegen den Beschluss des Landesgerichts für Strafsachen Wien vom 25. September 2012, GZ 130 Bl 65/12s-10, mit welchem der Antrag des Beschwerdeführers auf Fortführung des Verfahrens AZ 20 UT 91/12p der Staatsanwaltschaft Wien gegen unbekannte Täter wegen § 302 Abs 1 StGB zurückgewiesen worden war, als unzulässig zurück (§ 196 Abs 1 StPO).

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)
- `Gebhard Senkfeil` (person)

**Example 13** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__4`)


Im Verfahren AZ 28 U 165/17y des Bezirksgerichts Leopoldstadt verletzen 1./ die Durchführung der Hauptverhandlung und Urteilsfällung am 26. September 2018 in Abwesenheit des Angeklagten § 427 Abs 1 StPO, 2./ die Verlesung des die Vernehmung des Zeugen Alexander Struttmann beinhaltenden Teils des Hauptverhandlungsprotokolls vom 28. Februar 2018 (ON 9) in der Hauptverhandlung am 26. September 2018 § 252 Abs 1 StPO iVm § 447 StPO, 3./ der unter einem mit dem Urteil vom 26. September 2018 (ON 25) gefasste Beschluss auf Widerruf der Nenad Pohlmann mit Urteil des Landesgerichts für Strafsachen Wien vom 28. Jänner 2015, AZ 162 Hv 117/14k, gewährten bedingten Strafnachsicht § 494a Abs 3 StPO und 4./ das Urteil vom 26. September 2018 (ON 25) § 31 Abs 1 StGB.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Bezirksgerichts Leopoldstadt` (organisation)
- `Alexander Struttmann` (person)
- `Nenad Pohlmann` (person)

**Example 14** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__7`)


Ferner beantragte die Staatsanwaltschaft, die Nenad Pleßing mit Urteil des Landesgerichts für Strafsachen Wien vom 28. Jänner 2015, AZ 162 Hv 117/14k, gewährte bedingte Strafnachsicht (vgl ON 2 S 32) zu widerrufen, und wies darauf hin, dass der Widerruf der mit Urteil des genannten Gerichts vom 19. September 2017, AZ 44 Hv 88/17g, gewährten bedingten Strafnachsicht dem zuständigen Gerichtshof vorzubehalten sei.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Nenad Pleßing` (person)

**Example 15** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__14`)


Eine Bedachtnahme auf das Urteil des Landesgerichts für Strafsachen Wien vom 19. September 2017, AZ 44 Hv 88/17g, (unjournalisiert im Akt einliegend nach ON 27; vgl ON 22 Punkt 2./) gemäß § 31 StGB, erfolgte nicht.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Example 16** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__15`)


Zugleich fasste es den Beschluss auf Widerruf (§ 494a Abs 1 Z 4 StPO) der Nenad Plettener mit Urteil des Landesgerichts für Strafsachen Wien vom 28. Jänner 2015, AZ 162 Hv 117/14k, gewährten bedingten Strafnachsicht einer Freiheitsstrafe, ohne zuvor diesen Akt oder zumindest eine Abschrift des Urteils beigeschafft zu haben.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Nenad Plettener` (person)

**Example 17** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__16`)


In Ansehung der dem Angeklagten mit Urteil des Landesgerichts für Strafsachen Wien vom 19. September 2017, AZ 44 Hv 88/17g, gewährten bedingten Strafnachsicht erging ein auf § 494a Abs 2 letzter Satz StPO gestützter Vorbehaltsbeschluss.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Example 18** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__18`)


Über die rechtzeitige Beschwerde der Staatsanwaltschaft gegen den Beschluss auf Widerruf bedingter Strafnachsicht (ON 28) wurde noch nicht entschieden (AZ 131 Bl 94/18x des Landesgerichts für Strafsachen Wien).

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Example 19** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__28`)


Der Strafantrag vom 28. November 2017, aus dem der Antrag der Staatsanwaltschaft auf Widerruf der bedingten Strafnachsicht zu AZ 162 Hv 117/14k des Landesgerichts für Strafsachen Wien ersichtlich ist (ON 4), wurde dem Angeklagten durch Zustellung zur Kenntnis gebracht.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Example 20** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__32`)


Die unterbliebene Bedachtnahme auf das aktenkundige Urteil des Landesgerichts für Strafsachen Wien vom 19. September 2017, AZ 44 Hv 88/17g, verletzt daher mit Blick auf den Zeitpunkt der dem Abwesenheitsurteil zugrunde liegenden Tat (3. Februar 2017) § 31 Abs 1 StGB.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Example 21** (doc_id: `deanon_260716_TRAIN/12Os17_18v`) (sent_id: `deanon_260716_TRAIN/12Os17_18v_3`)


Kopf Der Oberste Gerichtshof hat am 15. März 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. T. Solé, Dr. Oshidari, Dr. Michel-Kwapinski und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Ettel als Schriftführerin in der Maßnahmenvollzugssache des Andreas Wegele, AZ 181 BE 143/17y des Landesgerichts für Strafsachen Wien, über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien vom 9. Jänner 2018, AZ 131 Bs 370/17z, und seinen Antrag auf Bewilligung der Verfahrenshilfe nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Dr. Oshidari` (person)
- `Dr. Michel-Kwapinski` (person)
- `Dr. Brenner` (person)
- `Mag. Ettel` (person)
- `Andreas Wegele` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/12Os17_18v`) (sent_id: `deanon_260716_TRAIN/12Os17_18v_5`)


Text Gründe: Mit dem angefochtenen Beschluss vom 9. Jänner 2018, AZ 131 Bs 370/17z, gab das Oberlandesgericht Wien als Rechtsmittelgericht der Beschwerde des Andreas Wackerow gegen den Beschluss des Landesgerichts für Strafsachen Wien vom 20. November 2017, GZ 181 BE 143/17y-16, mit dem die bedingte Entlassung aus einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 2 StGB abgelehnt worden war, nicht Folge.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)
- `Andreas Wackerow` (person)

**Example 23** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2020 durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé und durch die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Viktor Marschmeyer und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 3 zweiter Fall StGB, AZ 352 HR 214/11x des Landesgerichts für Strafsachen Wien, über den Antrag des Dr. Stefan Toepfl auf Erneuerung des Strafverfahrens gemäß § 363a StPO in Ansehung des Beschlusses des Oberlandesgerichts Wien vom 28. August 2018, AZ 20 Bs 199/18p, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Dr. Brenner` (person)
- `Dr. Setz-Hummel` (person)
- `Mag. Hauer` (person)
- `Viktor Marschmeyer` (person)
- `Dr. Stefan Toepfl` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_4`)


Text Gründe: Im Ermittlungsverfahren gegen Viktor Meisterernst und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und 3 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 703 St 3/11t (nunmehr AZ 713 St 24/18i) der Staatsanwaltschaft Wien, stellte der Beschuldigte Dr. Stefan Tydeck mit Schriftsatz vom 29. November 2017 – soweit im Folgenden von Relevanz – den Antrag auf Einstellung des Ermittlungsverfahrens „gemäß § 108 StPO“ (ON 558), welchen das Landesgericht für Strafsachen Wien mit Beschluss vom 22. Juni 2018, AZ 352 HR 214/11x, abwies (ON 644).

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Wien` | `Landesgericht für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Viktor Meisterernst` (person)
- `Dr. Stefan Tydeck` (person)

**Example 25** (doc_id: `deanon_260716_TRAIN/12Os45_13d`) (sent_id: `deanon_260716_TRAIN/12Os45_13d_3`)


Kopf Der Oberste Gerichtshof hat am 20. Juni 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Müller als Schriftführerin in der Strafsache gegen Maximilian Gompertz wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB und anderer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Graz als Jugendschöffengericht vom 10. Dezember 2012, GZ 14 Hv 110/12b-39, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Michel` (person)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Müller` (person)
- `Maximilian Gompertz` (person)

**Example 26** (doc_id: `deanon_260716_TRAIN/13Fss3_19y`) (sent_id: `deanon_260716_TRAIN/13Fss3_19y_3`)


Kopf Der Oberste Gerichtshof hat am 21. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und die Hofrätin des Obersten Gerichtshofs Dr. Brenner über den von Ing. Sebastian Novko im Verfahren AZ 5 Bl 6/19v des Landesgerichts für Strafsachen Graz gestellten Fristsetzungsantrag nach Einsichtnahme der Generalprokuratur in die Akten und Abstimmung gemäß § 62 Abs 1 zweiter Satz OGH-Geo 2019 den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Brenner` (person)
- `Ing. Sebastian Novko` (person)
- `OGH` (organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/13Fss3_19y`) (sent_id: `deanon_260716_TRAIN/13Fss3_19y_4`)


Gründe:  Rechtliche Beurteilung Mit seinem Fristsetzungsantrag vom 23. Dezember 2019 behauptet Ing. Sebastian Neuwirth Säumnis des Obersten Gerichtshofs mit „der Vornahme einer Verfahrenshandlung und Ausfertigung einer Entscheidung“ in Ansehung seines am 20. August 2019 beim Obersten Gerichtshof eingebrachten, gegen den Beschluss des Landesgerichts für Strafsachen Graz vom 1. Juli 2019, AZ 5 Bl 6/19v gerichteten Antrags auf Erneuerung des Strafverfahrens.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Missed by this rule (FN):**

- `Ing. Sebastian Neuwirth` (person)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshof` (organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/13Os108_19k`) (sent_id: `deanon_260716_TRAIN/13Os108_19k_3`)


Kopf Der Oberste Gerichtshof hat am 29. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Schriftführerin Dr. Ondreasova in der Strafsache gegen Alois Petraschek und andere Beschuldigte wegen des Vergehens der Untreue nach § 153 Abs 1 und 2 StGB aF und weiterer strafbarer Handlungen, AZ 5 Bl 6/19v des Landesgerichts für Strafsachen Graz, über die Anträge des Sebastian Neuhäußer auf Erneuerung des Strafverfahrens und auf Verlängerung der Frist zur Einbringung eines solchen Antrags nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Anträge werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

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
- `Alois Petraschek` (person)
- `Sebastian Neuhäußer` (person)

**Example 29** (doc_id: `deanon_260716_TRAIN/13Os108_19k`) (sent_id: `deanon_260716_TRAIN/13Os108_19k_4`)


Text Gründe: Mit Beschluss des Landesgerichts für Strafsachen Graz vom 1. Juli 2019, AZ 5 Bl 6/19v, wurde der von Sebastian Niemz am 24. Mai 2019 gestellte Antrag auf Fortführung des aufgrund seiner Anzeige von der Staatsanwaltschaft Graz zu AZ 22 St 47/14v gegen Alois Paasch und andere Beschuldigte wegen des Vergehens der Untreue nach § 153 Abs 1 und 2 StGB aF und weiterer strafbarer Handlungen geführten und gegen sämtliche Beschuldigte gemäß § 190 Z 2 StPO eingestellten Ermittlungsverfahrens als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Missed by this rule (FN):**

- `Sebastian Niemz` (person)
- `Alois Paasch` (person)

**Example 30** (doc_id: `deanon_260716_TRAIN/13Os117_19h`) (sent_id: `deanon_260716_TRAIN/13Os117_19h_3`)


Kopf Der Oberste Gerichtshof hat am 26. Februar 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Schriftführers Dr. Schöll in der Strafsache gegen Martin Pfaffenberg wegen des Verbrechens der absichtlichen schweren Körperverletzung nach § 87 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 5. September 2019, GZ 43 Hv 73/19x-48, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Dr. Schöll` (person)
- `Martin Pfaffenberg` (person)

**Example 31** (doc_id: `deanon_260716_TRAIN/13Os22_12b_13Ns16_12z_`) (sent_id: `deanon_260716_TRAIN/13Os22_12b_13Ns16_12z__3`)


Kopf Der Oberste Gerichtshof hat am 5. April 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. Lässig und die Hofrätin des Obersten Gerichtshofs Mag. Marek in Gegenwart der Richteramtsanwärterin MMag. Linzner als Schriftführerin im Verfahren zur Unterbringung der Mag. Türkan Maja Besold in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB, AZ 33 Hv 24/12g des Landesgerichts für Strafsachen Wien, über die Grundrechtsbeschwerde der Betroffenen nach Einsichtnahme durch die Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Grundrechtsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Marek` (person)
- `MMag. Linzner` (person)
- `Maja Besold` (person)

**Example 32** (doc_id: `deanon_260716_TRAIN/13Os22_12b_13Ns16_12z_`) (sent_id: `deanon_260716_TRAIN/13Os22_12b_13Ns16_12z__4`)


Text Gründe: Das Landesgericht für Strafsachen Wien verhängte mit Beschluss vom 9. Dezember 2011 über Mag. Türkan Kirstin Bierwolf die Untersuchungshaft aus den Gründen der Tatbegehungsgefahr nach § 173 Abs 2 Z 3 lit b und lit d StPO (ON 12).

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Wien` | `Landesgericht für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Kirstin Bierwolf` (person)

**Example 33** (doc_id: `deanon_260716_TRAIN/13Os23_15d`) (sent_id: `deanon_260716_TRAIN/13Os23_15d_3`)


Kopf Der Oberste Gerichtshof hat am 15. April 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Ableidinger als Schriftführerin in der Strafsache gegen Karl Wolniak wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 26. November 2014, GZ 31 Hv 87/14k-77, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Mag. Ableidinger` (person)
- `Karl Wolniak` (person)

**Example 34** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__4`)


Abs 1 fünfter Fall, Abs 2 Z 1 SMG und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Graz als Schöffengericht vom 20. Jänner 2012, GZ 8 Hv 83/11m-49, sowie die von der Generalprokuratur gegen den Vorgang der schriftlichen Ausfertigung dieses Urteils erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Dr. Brenner, sowie des Angeklagten und seines Verteidigers Mag. Heinz Russold nach Anhörung der Generalprokuratur zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Missed by this rule (FN):**

- `Dr. Brenner` (person)
- `Mag. Heinz Russold` (person)

**Example 35** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__5`)


In der Strafsache gegen Erik Jamrozy, AZ 8 Hv 83/11m des Landesgerichts für Strafsachen Graz, verletzt der Vorgang der schriftlichen Ausfertigung des am 20. Jänner 2012 mündlich verkündeten Urteils durch einen anderen Richter als den daran dauernd verhinderten Vorsitzenden des Schöffengerichts §§ 14 Abs 1 und 15 Abs 1 der Kaiserlichen Verordnung vom 14. Dezember 1915 über die Abfassung und Unterfertigung von gerichtlichen Entscheidungen in Zivil- und Strafsachen und von Protokollen bei dauernder Verhinderung des Richters oder des Schriftführers RGBl 1915/372.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Missed by this rule (FN):**

- `Erik Jamrozy` (person)

**Example 36** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__6`)


Dem Landesgericht für Strafsachen Graz wird ein Vorgehen gemäß §§ 14 und 15 dieser Verordnung aufgetragen.

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Graz` | `Landesgericht für Strafsachen Graz` |

**Example 37** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__10`)


Rechtliche Beurteilung Zufolge Suspendierung des Vorsitzenden des Schöffengerichts fasste der Personalsenat des Landesgerichts für Strafsachen Graz am 20. Februar 2012 den Beschluss, die Ausfertigung dieses mündlich verkündeten Urteils einer anderen Richterin dieses Gerichts zu übertragen (ON 1 S 19 ff).

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Example 38** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__28`)


8. Das Landesgericht für Strafsachen Graz hätte demnach die Staatsanwaltschaft und den Angeklagten von der dauernden Verhinderung des Vorsitzenden des Schöffengerichts in Kenntnis setzen und vor Betrauung eines anderen Richters mit der Urteilsausfertigung nach ihrem Einverständnis fragen müssen.

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Graz` | `Landesgericht für Strafsachen Graz` |

**Example 39** (doc_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_260716_TRAIN/13Os33_12w_13Os58_12x__30`)


Mit Blick auf § 292 letzter Satz StPO sah sich der Oberste Gerichtshof veranlasst, dem Landesgericht für Strafsachen Graz aufzutragen, gemäß §§ 14 und 15 der Kaiserlichen Verordnung vorzugehen.

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Graz` | `Landesgericht für Strafsachen Graz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)

**Example 40** (doc_id: `deanon_260716_TRAIN/13Os34_19b`) (sent_id: `deanon_260716_TRAIN/13Os34_19b_5`)


Dieser Beschluss wird aufgehoben und es wird dem Landesgericht für Strafsachen Graz aufgetragen, im Verfahren AZ 16 Hv 32/15a über den Widerruf zu entscheiden.

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Graz` | `Landesgericht für Strafsachen Graz` |

**Example 41** (doc_id: `deanon_260716_TRAIN/13Os34_19b`) (sent_id: `deanon_260716_TRAIN/13Os34_19b_6`)


Text Gründe: Mit in Rechtskraft erwachsenem Urteil des Landesgerichts für Strafsachen Graz vom 23. April 2015, AZ 16 Hv 32/15a, wurde Wolfgang Woerz zu einer Freiheitsstrafe von fünfzehn Monaten verurteilt, wovon ein Strafteil von zehn Monaten gemäß § 43a

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Missed by this rule (FN):**

- `Wolfgang Woerz` (person)

**Example 42** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_4`)


Abs 1 fünfter Fall, Abs 2 Z 3 SMG sowie einer weiteren strafbaren Handlung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 28. Februar 2017, GZ 44 Hv 144/16s-121, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Example 43** (doc_id: `deanon_260716_TRAIN/13Os45_17t`) (sent_id: `deanon_260716_TRAIN/13Os45_17t_14`)


Die Sanktionsrüge (Z 11 zweiter Fall) wendet sich gegen die als nach § 33 Abs 1 Z 2 StGB strafschärfend gewertete Verurteilung des Angeklagten durch das Landesgericht für Strafsachen Wien vom 16. Februar 2012, AZ 62 Hv 10/12m, (ua) wegen Vergehen des unerlaubten Umgangs mit Suchtmitteln (US 4, 9; ON 97).

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Wien` | `Landesgericht für Strafsachen Wien` |

**Example 44** (doc_id: `deanon_260716_TRAIN/13Os68_18a`) (sent_id: `deanon_260716_TRAIN/13Os68_18a_3`)


Kopf Der Oberste Gerichtshof hat am 27. Juni 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Sinek als Schriftführerin in der Strafsache gegen Mihai Clößner wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 2 erster Fall StGB und weiterer strafbarer Handlungen, AZ 222 Hv 15/17v des Landesgerichts für Strafsachen Graz, über den Antrag des Angeklagten auf Erneuerung des Strafverfahrens nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Mag. Sinek` (person)
- `Mihai Clößner` (person)

**Example 45** (doc_id: `deanon_260716_TRAIN/13Os68_18a`) (sent_id: `deanon_260716_TRAIN/13Os68_18a_4`)


Text Gründe: Mihai von Crailsheim wurde mit Urteil des Landesgerichts für Strafsachen Graz als Schöffengericht vom 19. April 2017, GZ 222 Hv 15/17v-207, des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 2 erster Fall StGB sowie weiterer strafbarer Handlungen schuldig erkannt und zu einer Freiheitsstrafe verurteilt, die das Oberlandesgericht Graz – in Stattgebung einer dagegen erhobenen Berufung des Angeklagten – mit Urteil vom 25. Oktober 2017, AZ 8 Bs 311/17x, herabsetzte.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Missed by this rule (FN):**

- `Mihai von Crailsheim` (person)
- `Oberlandesgericht Graz` (organisation)

**Example 46** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__3`)


Kopf Der Oberste Gerichtshof hat am 26. Februar 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Schriftführers Dr. Schöll in der Strafsache gegen Robert Ultsch wegen des Vergehens der Urkundenfälschung nach § 223 Abs 1 StGB und einer weiteren strafbaren Handlung, AZ 13 U 351/18d des Bezirksgerichts Innere Stadt Wien, über den auf den Beschluss des Landesgerichts für Strafsachen Wien als Berufungsgericht vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), bezogenen Antrag der Generalprokuratur auf außerordentliche Wiederaufnahme des Verfahrens und über ihre gegen den Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30 der U-Akten) zur Wahrung des Gesetzes erhobene Nichtigkeitsbeschwerde nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Schneider, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Dr. Schöll` (person)
- `Robert Ultsch` (person)
- `Bezirksgerichts Innere Stadt Wien` (organisation)
- `Bezirksgerichts Innere Stadt Wien` (organisation)
- `Mag. Schneider` (person)

**Example 47** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__5`)


In Stattgebung des Antrags der Generalprokuratur wird im außerordentlichen Weg die Wiederaufnahme des Berufungsverfahrens verfügt, der Beschluss des Landesgerichts für Strafsachen Wien vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), aufgehoben und die Sache zur neuerlichen Entscheidung über die Berufung des Angeklagten gegen das Urteil des Bezirksgerichts Innere Stadt Wien vom 27. November 2018 (ON 19 der U-Akten) an das Landesgericht für Strafsachen Wien verwiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |
| `Landesgericht für Strafsachen Wien` | `Landesgericht für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Bezirksgerichts Innere Stadt Wien` (organisation)

**Example 48** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__9`)


Die am 22. Februar 2019 – innerhalb der Frist des § 467 Abs 1 StPO (vgl Zustellnachweis an ON 19) – ausgeführte Berufung des Robert Unterdörfer (ON 21) wies das Landesgericht für Strafsachen Wien als Berufungsgericht mit Beschluss vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23), gemäß § 470 Z 1 StPO als unzulässig zurück, weil die am 27. November 2018 zur Post gegebene Rechtsmittelanmeldung gegen das am 23. November 2018 verkündete Urteil verspätet gewesen sei.

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Wien` | `Landesgericht für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Robert Unterdörfer` (person)

**Example 49** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__14`)


Rechtliche Beurteilung Wie die Generalprokuratur in ihrem Antrag auf außerordentliche Wiederaufnahme des Verfahrens zutreffend darlegt, bestehen gegen die Richtigkeit der dem Beschluss des Landesgerichts für Strafsachen Wien als Berufungsgericht vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23), zugrunde gelegten Tatsache, das erstinstanzliche Urteil sei am 23. November 2018 verkündet worden, erhebliche Bedenken: Die Verfügung des Bezirksgerichts Innere Stadt Wien vom 1. November 2018 auf Ladung des Angeklagten zur Hauptverhandlung am 27. November 2018 (ON 1 [unjournalisiert] S 6), das auf der letzten Seite der Urteilsurschrift angeführte Urteilsdatum „27. November 2018“ (ON 19 S 5), die im Verfahrensakt enthaltene (unjournalisierte) Äußerung der Staatsanwaltschaft Wien vom 15. November 2019, AZ 126 BAZ 822/11s, sowie der Berichtigungsbeschluss vom 4. Dezember 2019 (ON 30) legen qualifiziert nahe, dass das Urteil am27. November 2018verkündet wurde.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Bezirksgerichts Innere Stadt Wien` (organisation)

**Example 50** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__15`)


Der Senat von drei Richtern (§ 31 Abs 6 Z 1 StPO) des Landesgerichts für Strafsachen Wien jedoch ging – angesichts des Akteninhalts (vgl ON 18 S 1, ON 19 S 1) nicht vorwerfbar – von einer Verkündung des erstinstanzlichen Urteils am 23. November 2018 aus und legte diese Annahme seinem (auf Basis dessen rechtsrichtigen) Beschluss zugrunde, die Berufung wegen verspäteter Anmeldung zurückzuweisen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Example 51** (doc_id: `deanon_260716_TRAIN/14Ns5_20a`) (sent_id: `deanon_260716_TRAIN/14Ns5_20a_3`)


Kopf Der Oberste Gerichtshof hat am 24. Februar 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden sowie die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in der Straf- und Medienrechtssache der Privatanklägerin und Antragstellerin Petra Schwegle gegen den Angeklagten und Antragsgegner Holger Voelke wegen des Vergehens der üblen Nachrede nach § 111 StGB und einer weiteren strafbaren Handlung sowie § 6 Abs 1 und § 34 Abs 1 MedienG, AZ 92 Hv 58/19a des Landesgerichts für Strafsachen Wien, über den Antrag des Angeklagten und Antragsgegners auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Danek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Hetlinger` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Petra Schwegle` (person)
- `Holger Voelke` (person)
- `OGH` (organisation)

**Example 52** (doc_id: `deanon_260716_TRAIN/14Ns5_20a`) (sent_id: `deanon_260716_TRAIN/14Ns5_20a_5`)


Die Akten werden dem Oberlandesgericht Wien zurückgestellt. Gründe:  Rechtliche Beurteilung Der Wohnsitz des Angeklagten und Antragsgegners im Sprengel eines anderen Gerichts (ON 16 iVm ON 15 und ON 1 S 4 und 6) ist ebensowenig ein wichtiger Grund im Sinn des § 39 Abs 1 StPO wie der Umstand, dass sich der – von der Mindestsicherung lebende – Angeklagte die Kosten für die Anreise zum Landesgericht für Strafsachen Wien ersparen würde (RIS-Justiz RS0129146;

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Wien` | `Landesgericht für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)

**Example 53** (doc_id: `deanon_260716_TRAIN/14Os132_10h`) (sent_id: `deanon_260716_TRAIN/14Os132_10h_3`)


Kopf Der Oberste Gerichtshof hat am 28. September 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden sowie durch die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in Gegenwart der Richteramtsanwärterin Mag. Reichly als Schriftführerin in der Strafsache gegen Tomislav Ahlwarth wegen des Verbrechens des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und einer weiteren strafbaren Handlung, AZ 063 Hv 117/10a des Landesgerichts für Strafsachen Wien, über die Grundrechtsbeschwerde des Angeklagten vom 23. August 2010 nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Grundrechtsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Philipp` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Hetlinger` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Mag. Reichly` (person)
- `Tomislav Ahlwarth` (person)

**Example 54** (doc_id: `deanon_260716_TRAIN/14Os132_10h`) (sent_id: `deanon_260716_TRAIN/14Os132_10h_4`)


Text Gründe: Gegen Tomsilav Ayik ist beim Landesgericht für Strafsachen Wien ein - im Stadium der Hauptverhandlung befindliches - Verfahren wegen der Verbrechen des Suchtgifthandels nach § 28a Abs 1 zweiter und dritter Fall, Abs 4 Z 3 SMG und nach § 28a Abs 1 fünfter Fall, Abs 4 Z 3 SMG anhängig, in dem sich der Angeklagte seit 5. April 2010 in Untersuchungshaft befindet (ON 20).

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Wien` | `Landesgericht für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Ayik` (person)

**Example 55** (doc_id: `deanon_260716_TRAIN/14Os133_19v`) (sent_id: `deanon_260716_TRAIN/14Os133_19v_3`)


Kopf Der Oberste Gerichtshof hat am 14. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Mann und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Finanzstrafsache gegen Dr. Peter Johanni wegen des Finanzvergehens der Abgabenhinterziehung nach §§ 33 Abs 1, 13 FinStrG, AZ 14 Hv 3/10a des Landesgerichts für Strafsachen Wien, über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 23. Oktober 2019, AZ 23 Bs 323/19x, nach Einsichtnahme der Generalprokuratur in die Akten den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Danek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Hetlinger` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Mann` (person)
- `Dr. Setz-Hummel` (person)
- `Mag. Hauer` (person)
- `Dr. Peter Johanni` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 56** (doc_id: `deanon_260716_TRAIN/14Os133_19v`) (sent_id: `deanon_260716_TRAIN/14Os133_19v_4`)


Text Gründe: Mit dem angefochtenen Beschluss gab das Oberlandesgericht Wien einer – die ersatzlose Streichung „irrelevanter Begründungsteile“ begehrenden – Beschwerde des Dr. Peter Jovanovic gegen den Beschluss des Landesgerichts für Strafsachen Wien vom 25. September 2019, GZ 14 Hv 3/10a-500, mit welchem ausgesprochen worden war, dass dem Gericht die Ahndung der dem Angeklagten zur Last gelegten Taten als Finanzvergehen nicht zustehe (§ 53 Abs 1, § 212 FinStrG), nicht Folge.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)
- `Dr. Peter Jovanovic` (person)

**Example 57** (doc_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h_`) (sent_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h__3`)


Kopf Der Oberste Gerichtshof hat am 24. Jänner 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätinnen des Obersten Gerichtshofs Mag. Hetlinger und Mag. Marek sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari in Gegenwart der Richteramtsanwärterin MMag. Linzner als Schriftführerin in der Strafsache gegen Bernd Karacabey wegen des Verbrechens der absichtlichen schweren Körperverletzung nach § 87 Abs 1 und Abs 2 erster Fall StGB und einer anderen strafbaren Handlung über die von der Generalprokuratur gegen die Beschlüsse des Landesgerichts für Strafsachen Graz vom 20. Juni 2011, GZ 15 Hv 126/10k-44, und des Oberlandesgerichts Graz vom 11. August 2011, AZ 9 Bs 259/11y, sowie einen Vorgang erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Knibbe, des Angeklagten und seines Verteidigers Dr. Vacarescu zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Philipp` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Hetlinger` (person)
- `Mag. Marek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Dr. Oshidari` (person)
- `MMag. Linzner` (person)
- `Bernd Karacabey` (person)
- `Oberlandesgerichts Graz` (organisation)
- `Mag. Knibbe` (person)
- `Dr. Vacarescu` (person)

**Example 58** (doc_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h_`) (sent_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h__4`)


Im Verfahren AZ 15 Hv 126/10k des Landesgerichts für Strafsachen Graz verletzen das Gesetz 1.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Example 59** (doc_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h_`) (sent_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h__5`)


die nach Anhörung der Staatsanwaltschaft, nicht aber des Angeklagten erfolgte Beschlussfassung vom 20. Juni 2011 (ON 44) auf Berichtigung des Hauptverhandlungsprotokolls (ON 37) und Angleichung des schriftlichen an das mündlich verkündete Urteil vom 2. Dezember 2010 (ON 38) § 271 Abs 7 vierter Satz und § 270 Abs 3 erster Satz StPO; 2. der Beschluss des Landesgerichts für Strafsachen Graz vom 20. Juni 2011 (ON 44) § 86 Abs 1 vierter und letzter Satz StPO; 3. der Beschluss des Oberlandesgerichts Graz vom 11. August 2011, AZ 9 Bs 259/11y (ON 47), § 271 iVm § 270 Abs 3 dritter Satz StPO.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Missed by this rule (FN):**

- `Oberlandesgerichts Graz` (organisation)

**Example 60** (doc_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h_`) (sent_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h__7`)


Text Gründe: Mit Urteil des Landesgerichts für Strafsachen Graz als Schöffengericht vom 2. Dezember 2010, GZ 15 Hv 126/10k-38, wurde Bernd Kalverkamp der Verbrechen der absichtlichen schweren Körperverletzung nach § 87 Abs 1 und Abs 2 erster Fall StGB (I/1) und der schweren Nötigung nach §§ 15, 105 Abs 1, 106 Abs 1 Z 1 und 2 StGB (I/2) schuldig erkannt und hiefür unter Anwendung des § 28 StGB nach § 87 Abs 2 erster Halbsatz StGB zu einer Freiheitsstrafe von 18 (achtzehn) Monaten verurteilt, wovon gemäß § 43a Abs 3 StGB ein Teil von 15 (fünfzehn) Monaten bedingt nachgesehen wurde.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Missed by this rule (FN):**

- `Bernd Kalverkamp` (person)

**Example 61** (doc_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h_`) (sent_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h__15`)


Rechtliche Beurteilung Wie die Generalprokuratur in ihrer zur Wahrung des Gesetzes erhobenen Nichtigkeitsbeschwerde zutreffend ausführt, wurde durch die angesprochenen Beschlüsse und den Vorgang unterbliebener Anhörung des Angeklagten vor Berichtigung des Hauptverhandlungsprotokolls und Urteilsangleichung das Gesetz verletzt: (1)Zum Beschluss des Landesgerichts für Strafsachen Graz vom 20. Juni 2011, GZ 15 Hv 126/10k-44: a)

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Example 62** (doc_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h_`) (sent_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h__23`)


Indem der Vorsitzende des Schöffengerichts des Landesgerichts für Strafsachen Graz vor der unter einem erfolgten Beschlussfassung auf „Ergänzung und Berichtigung“ (gemeint: Berichtigung des Protokolls nach § 271 Abs 7 zweiter Satz StPO und Angleichung des schriftlichen an das mündlich verkündete Urteil) nur den - aus dem aktenkundigen schriftlichen Verhandlungsbericht ersichtlichen - Standpunkt der Staatsanwaltschaft berücksichtigte, dem Angeklagten jedoch keine Gelegenheit zur Stellungnahme zur beabsichtigten Berichtigung und Angleichung oder zu dem eben angesprochenen Schriftstück einräumte, hat er gegen § 271 Abs 7 vierter Satz und § 270 Abs 3 erster Satz StPO verstoßen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Example 63** (doc_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h_`) (sent_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h__27`)


Diesen Anforderungen wird der Beschluss des Landesgerichts für Strafsachen Graz vom 20. Juni 2011, GZ 15 Hv 126/10k-44, der weder die den Spruch tragenden gesetzlichen Bestimmungen anführt noch eine Rechtsmittelbelehrung enthält und aus dessen kursorischer Begründung zudem in keiner Weise hervorgeht, auf welchen Beweismitteln (etwa der Überzeugung des Vorsitzenden des Schöffensenats oder dem schriftlichen Verhandlungsbericht des Sitzungsvertreters der Staatsanwaltschaft) die Annahme irrtümlicher Nichterwähnung des „ordentlich verkündeten“ Ausspruchs über die Bestimmung einer dreijährigen Probezeit im Hauptverhandlungsprotokoll und der schriftlichen Urteilsausfertigung gründet (zu den Begründungserfordernissen von Beschlüssen vglTipold, WK-StPO § 86 Rz 8 mwN;Nimmervoll, Beschluss und Beschwerde 40 f), nicht gerecht.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Example 64** (doc_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h_`) (sent_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h__31`)


Da nicht auszuschließen ist, dass die aufgezeigten Gesetzesverletzungen zum Nachteil des Verurteilten wirken, sah sich der Oberste Gerichtshof veranlasst, deren Feststellung mit konkreter Wirkung zu verknüpfen (§ 292 letzter Satz StPO) und den Beschluss des Landesgerichts für Strafsachen Graz vom 20. Juni 2011, GZ 15 Hv 126/10k-44 sowie - zur Klarstellung - die Beschwerdeentscheidung des Oberlandesgerichts Graz vom 11. August 2011, AZ 9 Bs 259/11y (ON 47) aufzuheben.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Oberlandesgerichts Graz` (organisation)

**Example 65** (doc_id: `deanon_260716_TRAIN/15Os110_17s`) (sent_id: `deanon_260716_TRAIN/15Os110_17s_3`)


Kopf Der Oberste Gerichtshof hat am 19. September 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden und den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Shafiqullah Kira Nesselrodt und andere Angeklagte wegen des Verbrechens der absichtlichen schweren Körperverletzung nach §§ 15, 87 Abs 1 StGB, AZ 24 Hv 4/16v des Landesgerichts für Strafsachen Graz, über die Grundrechtsbeschwerde des Shafiqullah Erwin Nungässer gegen den Beschluss des Oberlandesgerichts Graz als Beschwerdegericht vom 8. März 2017, AZ 10 Bs 65/17k (ON 107 der Hv-Akten), nach Anhörung der Generalprokuratur zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Danek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Lendl` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Mann` (person)
- `Mag. Wetter` (person)
- `Kira Nesselrodt` (person)
- `Erwin Nungässer` (person)
- `Oberlandesgerichts Graz` (organisation)

**Example 66** (doc_id: `deanon_260716_TRAIN/15Os110_17s`) (sent_id: `deanon_260716_TRAIN/15Os110_17s_6`)


Text Gründe: Mit auch unbekämpfte Schuldsprüche anderer Angeklagter enthaltendem Urteil des Landesgerichts für Strafsachen Graz als Schöffengericht vom 14. Februar 2017, GZ 24 Hv 4/16v-90, wurde Shafiqullah Gudrun Noeltner des Verbrechens der absichtlichen schweren Körperverletzung nach §§ 15, 87 Abs 1 StGB schuldig erkannt und – unter Anrechnung von Vorhaftzeiten vom 5. September 2016 bis zum Urteilszeitpunkt – zu einer Freiheitsstrafe von vierundzwanzig Monaten verurteilt, wobei gemäß § 43a

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Graz` | `Landesgerichts für Strafsachen Graz` |

**Missed by this rule (FN):**

- `Gudrun Noeltner` (person)

**Example 67** (doc_id: `deanon_260716_TRAIN/15Os110_17s`) (sent_id: `deanon_260716_TRAIN/15Os110_17s_10`)


Aus Anlass eines vom Angeklagten am 17. Februar 2017 eingebrachten Antrags auf Aufhebung der Untersuchungshaft (ON 95) setzte das Landesgericht für Strafsachen Graz mit Beschluss vom 23. Februar 2017 die am 7. September 2016 verhängte (ON 11) – und danach wiederholt prolongierte (ON 32, 71) – Untersuchungshaft aus den Haftgründen der Flucht- und der Tatbegehungsgefahr nach § 173 Abs 2 Z 1 und Z 3 lit a StPO fort (ON 100).

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Graz` | `Landesgericht für Strafsachen Graz` |

**Example 68** (doc_id: `deanon_260716_TRAIN/15Os162_11d`) (sent_id: `deanon_260716_TRAIN/15Os162_11d_3`)


Kopf Der Oberste Gerichtshof hat am 25. Jänner 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Danek als Vorsitzenden, die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Dr. Michel-Kwapinski als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Brandstetter als Schriftführer in der Strafvollzugssache der Radmila Mayrhöfer, AZ 188 BE 302/10x des Landesgerichts für Strafsachen Wien, über den von der Generalprokuratur gegen den Vorgang, dass vor Beschlussfassung über die bedingte Entlassung die Einsichtnahme in den Urteilsakt AZ 75 Hv 151/06h des Landesgerichts für Strafsachen Wien unterblieb, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Eisenmenger, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Danek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Mag. Lendl` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Brandstetter` (person)
- `Radmila Mayrhöfer` (person)
- `Dr. Eisenmenger` (person)

**Example 69** (doc_id: `deanon_260716_TRAIN/15Os162_11d`) (sent_id: `deanon_260716_TRAIN/15Os162_11d_4`)


In der Strafvollzugssache der Radmila Muend, AZ 188 BE 302/10x des Landesgerichts für Strafsachen Wien (vormals AZ 44 BE 397/10a des Landesgerichts Wiener Neustadt), verletzt der ohne vorangehende Einsichtnahme in den Akt AZ 75 Hv 151/06h des Landesgerichts für Strafsachen Wien gefasste Beschluss des Landesgerichts Wiener Neustadt als Vollzugsgericht vom 24. August 2010, GZ 44 BE 397/10a- 5, über die bedingte Entlassung der Verurteilten § 152 Abs 2 erster Satz StVG.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Radmila Muend` (person)
- `Landesgerichts Wiener Neustadt` (organisation)
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 70** (doc_id: `deanon_260716_TRAIN/15Os162_11d`) (sent_id: `deanon_260716_TRAIN/15Os162_11d_5`)


Text Gründe: Radmila Michalske, wurde durch Urteil des Landesgerichts für Strafsachen Wien vom 8. November 2006, GZ 75 Hv 151/06h-72, zu einer Freiheitsstrafe von 18 Monaten verurteilt, wobei ein Teil von zwölf Monaten unter Bestimmung einer dreijährigen Probezeit bedingt nachgesehen wurde.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Radmila Michalske` (person)

**Example 71** (doc_id: `deanon_260716_TRAIN/15Os162_11d`) (sent_id: `deanon_260716_TRAIN/15Os162_11d_7`)


Aufgrund neuerlicher Delinquenz wurde sie in der Folge durch Urteil des Landesgerichts für Strafsachen Wien vom 12. August 2009, GZ 81 Hv 85/09a-104, zu einer Freiheitsstrafe von 27 Monaten verurteilt. Unter einem wurde die bedingte Nachsicht hinsichtlich des zur erstgenannten Verurteilung ausgesprochenen zwölfmonatigen Strafteils gemäß §§ 53 Abs 1 StGB, 494a Abs 1 Z 4 StPO beschlussmäßig widerrufen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Example 72** (doc_id: `deanon_260716_TRAIN/15Os162_11d`) (sent_id: `deanon_260716_TRAIN/15Os162_11d_9`)


Am 10. Februar 2010 erging im Verfahren AZ 75 Hv 151/06h des Landesgerichts für Strafsachen Wien (ON 91) ein Beschluss auf nachträgliche Milderung der Strafe gemäß § 31a StGB in der Form, dass „die ursprünglich verhängte Freiheitsstrafe in der Höhe von 18 Monaten, wobei ein Strafteil von zwölf Monaten bedingt nachgesehen wurde, auf eine Freiheitsstrafe in der Höhe von 15 Monaten“ reduziert werde, wovon „ein Strafteil von zehn Monaten unter Setzung einer Probezeit von drei Jahren bedingt nachgesehen“ sei.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Example 73** (doc_id: `deanon_260716_TRAIN/15Os162_11d`) (sent_id: `deanon_260716_TRAIN/15Os162_11d_10`)


Mit Beschluss des Landesgerichts Wiener Neustadt als Vollzugsgericht vom 24. August 2010, GZ 44 BE 397/10a-5, wurde Radmila Maseizik am 5. November 2010 aus dem Vollzug der mit Urteil des Landesgerichts für Strafsachen Wien vom 12. August 2009, AZ 81 Hv 85/09a, verhängten unbedingten Freiheitsstrafe von 27 Monaten und der mit Urteil des Landesgerichts für Strafsachen Wien vom 8. November 2006, AZ 75 Hv 151/06h, ausgesprochenen zehnmonatigen Freiheitsstrafe nach Verbüßung eines Teils von 25 Monaten gemäß § 46 StGB bedingt entlassen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Landesgerichts Wiener Neustadt` (organisation)
- `Radmila Maseizik` (person)

**Example 74** (doc_id: `deanon_260716_TRAIN/15Os162_11d`) (sent_id: `deanon_260716_TRAIN/15Os162_11d_12`)


Nach der Aktenlage nahm der Vollzugsrichter vor seiner Entscheidung lediglich in das zu AZ 81 Hv 85/09a des Landesgerichts für Strafsachen Wien ergangene Urteil und eine aktuelle Strafregisterauskunft Einsicht, verabsäumte aber die Beischaffung und Einsichtnahme in den Akt oder das Urteil zu AZ 75 Hv 151/06h des Landesgerichts für Strafsachen Wien.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Example 75** (doc_id: `deanon_260716_TRAIN/15Os162_11d`) (sent_id: `deanon_260716_TRAIN/15Os162_11d_17`)


Im vorliegenden Fall wurde hinsichtlich der zu AZ 81 Hv 85/09a des Landesgerichts für Strafsachen Wien verhängten Strafe die (bloße) Einsicht in das Urteil den genannten Kriterien gerecht.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Example 76** (doc_id: `deanon_260716_TRAIN/15Os162_11d`) (sent_id: `deanon_260716_TRAIN/15Os162_11d_18`)


Bezüglich der zu AZ 75 Hv 151/06h des Landesgerichts für Strafsachen Wien ausgesprochenen Sanktion fehlte jedoch jedenfalls eine taugliche Entscheidungsgrundlage, zumal weder in den Akt noch in das Urteil eingesehen wurde, sodass die dennoch erfolgte Beschlussfassung gegen § 152 Abs 1 StVG verstieß.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Example 77** (doc_id: `deanon_260716_TRAIN/15Os162_11d`) (sent_id: `deanon_260716_TRAIN/15Os162_11d_19`)


Die Generalprokuratur beantragte, der Gesetzesverletzung konkrete Wirkung zuzuerkennen, dies mit folgenderBegründung: „Im Verfahren AZ 75 Hv 151/06h des Landesgerichts für Strafsachen Wien wurde die ursprünglich verhängte Strafe von 18 Monaten (davon ein Strafteil von zwölf Monaten bedingt) mit rechtskräftigem Beschluss vom 10. Februar 2010 (ON 91) gemäß § 31a

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Example 78** (doc_id: `deanon_260716_TRAIN/15Os162_11d`) (sent_id: `deanon_260716_TRAIN/15Os162_11d_21`)


Dem Vollzugsrichter blieb die - bereits in der eingeholten Strafregisterauskunft vermerkte (ON 4 in AZ 188 BE 302/10x des Landesgerichts für Strafsachen Wien) - nachträgliche Strafmilderung nur deshalb verborgen, weil er die nach § 152 Abs 2 erster Satz StVG zwingend gebotene Einsichtnahme in den in Rede stehenden Vorstrafakt unterließ.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Example 79** (doc_id: `deanon_260716_TRAIN/15Os162_11d`) (sent_id: `deanon_260716_TRAIN/15Os162_11d_31`)


Dafür spricht auch ihre Verfügung S 242 in AZ 75 Hv 151/06h des Landesgerichts für Strafsachen Wien, nach der sie von einem nach wie vor zu vollziehenden widerrufenen Strafteil ausging.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Example 80** (doc_id: `deanon_260716_TRAIN/15Os162_11d`) (sent_id: `deanon_260716_TRAIN/15Os162_11d_32`)


Die bedingte Entlassung erfolgte daher zu Recht auch aus dem zu AZ 75 Hv 151/06h des Landesgerichts für Strafsachen Wien ausgesprochenen zehnmonatigen Strafteil, sodass ein - zu einem Vorgehen nach § 292 letzter Satz StPO veranlassender - Nachteil der Verurteilten durch die konstatierte Gesetzesverletzung nicht gegeben ist.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Example 81** (doc_id: `deanon_260716_TRAIN/15Os178_15p`) (sent_id: `deanon_260716_TRAIN/15Os178_15p_3`)


Kopf Der Oberste Gerichtshof hat am 1. Juli 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden in der Strafsache des Privatanklägers Mag. Ralph Kreickenbaum gegen Martin Rick wegen des Vergehens der üblen Nachrede nach § 111 Abs 1 und Abs 2 StGB, AZ 91 Hv 75/09d des Landesgerichts für Strafsachen Wien über den Antrag des Privatanklägers auf Verlängerung der Frist zur Äußerung zur Stellungnahme der Generalprokuratur den Beschluss gefasst:  Spruch Der Antrag des Privatanklägers Mag. Ralph Klosterkötter vom 27. Juni 2016 auf Verlängerung der Frist zur Äußerung zur Stellungnahme der Generalprokuratur wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Danek` (person)
- `Mag. Ralph Kreickenbaum` (person)
- `Martin Rick` (person)
- `Mag. Ralph Klosterkötter` (person)

**Example 82** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__3`)


Kopf Der Oberste Gerichtshof hat am 11. September 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Setz-Hummel in Gegenwart der Richteramtsanwärterin Mag. Leitner als Schriftführerin in der Medienrechtssache des Antragstellers Georgia Bruckmeir gegen die Antragsgegnerin MittelForschung GmbH und eine weitere Antragsgegnerin wegen § 6 Abs 1 und § 8a Abs 6 MedienG, AZ 91 Hv 49/17t des Landesgerichts für Strafsachen Wien, über die von der Generalprokuratur gegen die Urteile des Landesgerichts für Strafsachen Wien vom 26. März 2018 (ON 65 der Hv-Akten) und des Oberlandesgerichts Wien als Berufungsgericht vom 28. November 2018, AZ 17 Bs 153/18a (ON 74 der Hv-Akten), erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Holzleithner, des Vertreters des Antragstellers, Dr. Bauer, und des Vertreters der Antragsgegnerin Analyse Fenheim GmbH, Mag. Bauer, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Lendl` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Fürnkranz` (person)
- `Dr. Setz-Hummel` (person)
- `Mag. Leitner` (person)
- `Georgia Bruckmeir` (person)
- `MittelForschung GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Mag. Holzleithner` (person)
- `Dr. Bauer` (person)
- `Analyse Fenheim GmbH` (organisation)
- `Mag. Bauer` (person)

**Example 83** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__4`)


In der Medienrechtssache des Antragstellers Univ.-Prof.in Laurin Schramm gegen die Antragsgegnerin CDL Luftfahrt GmbH wegen § 6 Abs 1 und § 8a Abs 6 MedienG, AZ 91 Hv 49/17t des Landesgerichts für Strafsachen Wien, verletzen die Urteile 1./ dieses Gerichts vom 26. März 2018 (ON 65) in seinem Punkt III./, womit der Antrag des Antragstellers, der Antragsgegnerin Drau-IT GmbH auch für die am 4. Juni 2017 auf dem Facebook-Account von www.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Laurin Schramm` (person)
- `CDL Luftfahrt GmbH` (organisation)
- `Drau-IT GmbH` (organisation)

**Example 84** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__8`)


Wien Dorftratri Technologien.at und www.facebook.com/ RheinMöbel.at) und eine weitere Antragsgegnerin (nunmehr Mediengruppe „ Stadt Logderder “ GmbH) wegen § 6 Abs 1 und § 8a Abs 6 MedienG, AZ 91 Hv 49/17t des Landesgerichts für Strafsachen Wien, erkannte der Einzelrichter dieses Gerichts mit Urteil vom 26. März 2018 (ON 65) – soweit im Folgenden für die Nichtigkeitsbeschwerde zur Wahrung des Gesetzes von Relevanz – ua dahin, dass durch die am 4. Juni 2017 auf der Website www.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Wien Dorftratri Technologien.at` (organisation)
- `RheinMöbel.at` (organisation)
- `Stadt Logderder` (organisation)

**Example 85** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__20`)


Den gegen das (hier nur auszugsweise dargestellte) Urteil des Landesgerichts für Strafsachen Wien vom 26. März 2018 gerichteten Berufungen des Antragstellers und der beiden Antragsgegnerinnen gab das Oberlandesgericht Wien als Berufungsgericht mit Urteilvom 28. November 2018, AZ 17 Bs 153/18a (ON 74 der Hv-Akten), nicht Folge.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)

**Example 86** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__29`)


Wie die Generalprokuratur in ihrer zur Wahrung des Gesetzes erhobenen Nichtigkeitsbeschwerde zutreffend ausführt, stehen die Urteile des Landesgerichts für Strafsachen Wien vom 26. März 2018, GZ 91 Hv 49/17t-65, und des Oberlandesgerichts Wien als Berufungsgericht vom 28. November 2018, AZ 17 Bs 153/18a (ON 74 der Hv-Akten), mit dem Gesetz nicht im Einklang: Dem Berufungsgericht ist zunächst zuzustimmen, dass der in § 17 ECG normierte Ausschluss der Verantwortlichkeit mangels Fremdheit der verlinkten Informationen nicht in Betracht kommt (vgl ErläutRV 817 BlgNR 21.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberlandesgerichts Wien` (organisation)

**Example 87** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__57`)


Das Landesgericht für Strafsachen Wien und das Oberlandesgericht Wien als Berufungsgericht haben somit die (grundsätzliche) Verwirklichung des Entschädigungsanspruchs nach § 6 Abs 1 MedienG in Bezug auf die am 4. Juni 2017 auf dem Facebook-Account von www.

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Wien` | `Landesgericht für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)

**Example 88** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_3`)


Kopf Der Oberste Gerichtshof hat am 11. Dezember 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in Gegenwart des Schriftführers Dr. Koller in der Medienrechtssache der Antragsteller Dr. Ludger Schäpan und Moses Rüßbült gegen die Antragsgegnerin Synzortal-Medien GmbH & Co KG wegen §§ 7 f MedienG, AZ 93 Hv 56/18p des Landesgerichts für Strafsachen Wien, über die von der Generalprokuratur gegen den Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 9. März 2020, AZ 18 Bs 340/19k (ON 27), erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Erste Generalanwältin Mag. Wachberger, der Vertreterin der Antragsteller Dr. Windhager und des Vertreters der Antragsgegnerin Mag. Hermetter, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

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
- `Dr. Koller` (person)
- `Dr. Ludger Schäpan` (person)
- `Moses Rüßbült` (person)
- `Synzortal-Medien GmbH & Co KG` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Mag. Wachberger` (person)
- `Dr. Windhager` (person)
- `Mag. Hermetter` (person)

**Example 89** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_5`)


Text Gründe: In der Medienrechtssache der Antragsteller Dr. Wieland Skocdopole und Priv.-Doz.in Heidrun Aguera, BA MSc gegen die Antragsgegnerin Wald Fenkraftal GmbH & Co KG wegen §§ 7 f MedienG brachten die Antragsteller beim Landesgericht für Strafsachen Wien gesondert, jeweils in einem eigenen Schriftsatz aber vertreten durch dieselbe Rechtsanwältin selbständige Entschädigungsanträge gegen die Antragsgegnerin ein.

| Predicted | Gold |
|---|---|
| `Landesgericht für Strafsachen Wien` | `Landesgericht für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Dr. Wieland Skocdopole` (person)
- `Priv.-Doz.in Heidrun Aguera, BA MSc` (person)
- `Wald Fenkraftal GmbH & Co KG` (organisation)

**Example 90** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_6`)


Mit Beschluss vom 5. Juni 2018 wurde das von Herta Täumer angestrengte Verfahren (AZ 91 Hv 44/18h des Landegerichts für Strafsachen Wien) „gemäß § 37 Abs 1 StPO“ in das Verfahren des Antragstellers Dr. Ramona Jöstingmeyer gegen dieselbe Antragsgegnerin (AZ 93 Hv 56/18p des Landesgerichts für Strafsachen Wien), einbezogen (ON 1 S 1).

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

**Missed by this rule (FN):**

- `Herta Täumer` (person)
- `Dr. Ramona Jöstingmeyer` (person)

**Example 91** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_7`)


Im zweiten Rechtsgang wurde die Antragsgegnerin mit (in Rechtskraft erwachsenem) Urteil des Landesgerichts für Strafsachen Wien vom 4. Juli 2019, GZ 93 Hv 56/18p-18, nach §§ 7 und 7a MedienG jeweils zur Zahlung einer Entschädigung an die Antragsteller sowie gemäß § 389 Abs 1 StPO (iVm § 41 Abs 1 MedienG) zum Ersatz der Verfahrenskosten verpflichtet.

| Predicted | Gold |
|---|---|
| `Landesgerichts für Strafsachen Wien` | `Landesgerichts für Strafsachen Wien` |

</details>

---

## `VwGH_Abbreviation` 

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `d619a589`  
**Description:**
Matches the abbreviation VwGH (Verwaltungsgerichtshof).

**Content:**
```
\bVwGH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 9 | 9 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 9 | 0 | 3838 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_29`)


Hingegen sind die Kosten einer rechtsfreundlichen Vertretung vom Bundesverwaltungsgericht nicht zuzusprechen (VwGH 2005/04/0257;ReisnerinHeid/Preslmayr, Vergaberecht4[2015] Rz 2034).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_44`)


Ein Antrag auf Feststellung des in einem Nachprüfungsverfahren geltend gemachten Vergaberechtsverstoßes ist nämlich nach dem Widerruf dieses Vergabeverfahrens nicht mehr möglich (VwGH 2012/04/0133).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 2** (doc_id: `deanon_260716_TRAIN/1Ob224_19a`) (sent_id: `deanon_260716_TRAIN/1Ob224_19a_17`)


Da von mehreren vom Gesetz alternativ zur Verfügung gestellten Möglichkeiten der Verständigung des Empfängers von der Hinterlegung jene zu wählen ist, von der angenommen werden kann, dass sie die größere Gewähr dafür bietet, dass der Empfänger die Verständigung tatsächlich erhält (vglWalter/Mayer, Das Österreichische Zustellrecht [1983] § 17 ZustG Anm 21;WesselyinFrauenberger-Pfeiler/ Raschauer/Sander/Wessely, Österreichisches Zustellrecht² [2011] § 17 ZustG Rz 6 unter Hinweis auf 9 ObA 64/93; siehe auch VwGH Ra 2017/20/0290;

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 3** (doc_id: `deanon_260716_TRAIN/1Ob224_19a`) (sent_id: `deanon_260716_TRAIN/1Ob224_19a_22`)


Da die Vorschriften über die Zustellung (und daher auch über die Art der Zurücklassung der Hinterlegungsanzeige) durch eine Vereinbarung zwischen dem Postzusteller und dem Empfänger nicht geändert werden können (VwGH 87/05/0063), kommt es entgegen der Ansicht der Revisionsrekurswerberin nicht darauf an, ob die „Zeitungsröhre“ bisher „anstandslos“ für sämtliche Postzustellungen genutzt wurde.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 4** (doc_id: `deanon_260716_TRAIN/7Ob193_21i`) (sent_id: `deanon_260716_TRAIN/7Ob193_21i_23`)


[6] 4.1 Der hier interessierende Art 9.2.3.1.1 des Rahmenvertrags entspricht § 117 Abs 4 GewO 1994 (vgl VwGH 2007/04/0198 mwN).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 5** (doc_id: `deanon_260716_TRAIN/8Ob101_14g`) (sent_id: `deanon_260716_TRAIN/8Ob101_14g_12`)


Hinsichtlich der vom Klagebegehren betroffenen Liegenschaften hat nicht nur die Agrarbehörde über diese Frage bereits entschieden, sondern liegt auch ein letztinstanzliches Erkenntnis des Verwaltungsgerichtshofs vor (VwGH 15.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 6** (doc_id: `deanon_260716_TRAIN/9ObA92_15t`) (sent_id: `deanon_260716_TRAIN/9ObA92_15t_34`)


2.2.Demgegenüber erachtetMüller(Judikaturdivergenzen zwischen VwGH und OGH? - Eine Entwarnung, ZAS 2003/22;ders, Nochmals: Kollektivvertraglicher Mindestlohn und Sachbezug in der Sozialversicherung, ASoK 2002, 220), die kollektivvertraglichen Entlohnungsbestimmungen im Ergebnis als zweiseitig zwingende Anordnung eines Barzahlungsgebots, sodass es auf einen Günstigkeitsvergleich nicht mehr ankomme.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Missed by this rule (FN):**

- `OGH` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/9ObA92_15t`) (sent_id: `deanon_260716_TRAIN/9ObA92_15t_35`)


Diese Ansicht teilen auchLöschnigg(Entscheidungsanmerkung zu VwGH 95/08/0037, DRdA 2003, 340 f),Spitzl/Huber(inKuras[Hrsg], Handbuch Arbeitsrecht [1997] Pkt. 3.2.3.),Preiss(in ZellKomm2§ 78 GewO Rz 7),Kozak(inReissner, AngG2§ 42 Rz 34) undKarner(inMazal/Risak, Arbeitsrecht, System und Praxiskommentar [2014] Kap.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 8** (doc_id: `deanon_260716_TRAIN/9ObA92_15t`) (sent_id: `deanon_260716_TRAIN/9ObA92_15t_41`)


Ob der Marktwert der vom Arbeitgeber tatsächlich gewährten Naturalbezüge im Ergebnis höher sei als der „vereinbarte Wert“, dh höher als jener Teil des Barentgelts, an dessen Stelle die Sachbezüge geleistet werden sollten, sei daher unentscheidend (VwGH vom 22. 3. 1994, 92/08/0150;

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

</details>

---

## `Bezirksgericht_Spittal_Güssing_Schärding` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ec998e7c`  
**Description:**
Matches District Courts for specific missing cities: Spittal an der Drau, Güssing, Schärding.

**Content:**
```
\bBezirksgerichts?\s+(?:Spittal\s+an\s+der\s+Drau|Güssing|Schärding)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.000 | 0.001 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 2378 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/1Ob51_14b`) (sent_id: `deanon_260716_TRAIN/1Ob51_14b_4`)


Janet Zapel, vertreten durch Dr. Johannes Dörner und Dr. Alexander Singer, Rechtsanwälte in Graz und 2. Nikolaus Terzopoulou, wegen Streitanmerkung, über den Revisionsrekurs der erstbeklagten Partei gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 12. Februar 2014, GZ 3 R 12/14w-8, mit dem der Rekurs der erstbeklagten Partei gegen den Beschluss des Bezirksgerichts Spittal an der Drau vom 11. Dezember 2013, GZ 6 C 233/13a-2, teilweise zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Spittal an der Drau` | `Bezirksgerichts Spittal an der Drau` |

**Missed by this rule (FN):**

- `Janet Zapel` (person)
- `Dr. Johannes Dörner` (person)
- `Dr. Alexander Singer` (person)
- `Nikolaus Terzopoulou` (person)
- `Landesgerichts Klagenfurt` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/5Ob102_24x`) (sent_id: `deanon_260716_TRAIN/5Ob102_24x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei ÖkR KzlR Sonja Doganoglu, wider die beklagte Partei Stoeberl Bau AG, Bernhard-Paumgartner-Weg 41, 3233 Hohenbrand, Österreich, Deutschland vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 13.607,40 EUR sA und Feststellung über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Ried im Innkreis als Berufungsgericht vom 13. März 2024, GZ 18 R 2/24k-29, mit dem das Urteil des Bezirksgerichts Schärding vom 6. November 2023, GZ 2 C 478/20g-24, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Schärding` | `Bezirksgerichts Schärding` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Jensik` (person)
- `Mag. Wurzer` (person)
- `Mag. Painsi` (person)
- `Dr. Weixelbraun-Mohr` (person)
- `Dr. Steger` (person)
- `ÖkR KzlR Sonja Doganoglu` (person)
- `Stoeberl Bau AG` (organisation)
- `Bernhard-Paumgartner-Weg 41, 3233 Hohenbrand, Österreich` (address)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Ried im Innkreis` (organisation)

</details>

---

## `Bezirksgerichts_Leopoldstadt` 

**F1:** 0.003 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `a858714a`  
**Description:**
Matches 'Bezirksgerichts Leopoldstadt' specifically to handle the missing case in the extended city list.

**Content:**
```
\bBezirksgerichts?\s+Leopoldstadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.003 | 7 | 7 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 0 | 3311 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Nenad Pschor wegen des Vergehens der Veruntreuung nach § 133 Abs 1 StGB, AZ 28 U 165/17y des Bezirksgerichts Leopoldstadt, über die von der Generalprokuratur gegen das Urteil des genannten Gerichts vom 26. September 2018 (ON 25) sowie weitere Vorgänge in diesem Verfahren erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Oberstaatsanwalt Mag. Schneider, LL.M., zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Leopoldstadt` | `Bezirksgerichts Leopoldstadt` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Oshidari` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Dr. Mann` (person)
- `Dr. Brenner` (person)
- `Mag. Rögner` (person)
- `Nenad Pschor` (person)
- `Mag. Schneider, LL.M.` (person)

**Example 1** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__4`)


Im Verfahren AZ 28 U 165/17y des Bezirksgerichts Leopoldstadt verletzen 1./ die Durchführung der Hauptverhandlung und Urteilsfällung am 26. September 2018 in Abwesenheit des Angeklagten § 427 Abs 1 StPO, 2./ die Verlesung des die Vernehmung des Zeugen Alexander Struttmann beinhaltenden Teils des Hauptverhandlungsprotokolls vom 28. Februar 2018 (ON 9) in der Hauptverhandlung am 26. September 2018 § 252 Abs 1 StPO iVm § 447 StPO, 3./ der unter einem mit dem Urteil vom 26. September 2018 (ON 25) gefasste Beschluss auf Widerruf der Nenad Pohlmann mit Urteil des Landesgerichts für Strafsachen Wien vom 28. Jänner 2015, AZ 162 Hv 117/14k, gewährten bedingten Strafnachsicht § 494a Abs 3 StPO und 4./ das Urteil vom 26. September 2018 (ON 25) § 31 Abs 1 StGB.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Leopoldstadt` | `Bezirksgerichts Leopoldstadt` |

**Missed by this rule (FN):**

- `Alexander Struttmann` (person)
- `Nenad Pohlmann` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__5`)


Das Abwesenheitsurteil vom 26. September 2018 sowie der unter einem gefasste Beschluss (ON 25) werden aufgehoben und die Sache zu neuer Verhandlung und Entscheidung an das Bezirksgericht Leopoldstadt verwiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Leopoldstadt` | `Bezirksgericht Leopoldstadt` |

**Example 3** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__6`)


Text Gründe: Im Verfahren AZ 28 U 165/17y des Bezirksgerichts Leopoldstadt legte die Staatsanwaltschaft Wien Nenad Pielstick mit Strafantrag vom 28. November 2017 (ON 4) ein am 3. Februar 2017 in Langauweg 3, 3203 Röhrenbach, Österreich gesetztes und als Vergehen der Veruntreuung nach § 133 Abs 1 StGB beurteiltes Verhalten zur Last.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Leopoldstadt` | `Bezirksgerichts Leopoldstadt` |

**Missed by this rule (FN):**

- `Nenad Pielstick` (person)
- `Langauweg 3, 3203 Röhrenbach, Österreich` (address)

**Example 4** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__11`)


Nach zwei negativen Versuchen der Vorführung zur Hauptverhandlung am 2. Mai 2018 (ON 10a, 11) und am 27. Juni 2018 (ON 17, 18) führte das Bezirksgericht Leopoldstadt die – wiederholte (§ 276a zweiter Satz StPO) – Hauptverhandlung am 26. September 2018 in Abwesenheit des Angeklagten durch (ON 24), weil auch zu diesem Termin ein Vorführungsversuch erfolglos geblieben war (ON 23).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Leopoldstadt` | `Bezirksgericht Leopoldstadt` |

**Example 5** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__13`)


Mit Abwesenheitsurteil vom 26. September 2018 (ON 25) sprach das Bezirksgericht Leopoldstadt Nenad Panagiotakopoulou des Vergehens der Veruntreuung nach § 133 Abs 1 StGB schuldig und verurteilte ihn zu einer Freiheitsstrafe.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Leopoldstadt` | `Bezirksgericht Leopoldstadt` |

**Missed by this rule (FN):**

- `Nenad Panagiotakopoulou` (person)

**Example 6** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__19`)


Rechtliche Beurteilung Wie die Generalprokuratur in ihrer gemäß § 23 StPO ergriffenen Nichtigkeitsbeschwerde zur Wahrung des Gesetzes zutreffend aufzeigt, wurde im Verfahren AZ 28 U 165/17y des Bezirksgerichts Leopoldstadt das Gesetz mehrfach verletzt: 1./

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Leopoldstadt` | `Bezirksgerichts Leopoldstadt` |

</details>

---

## `Bezirksgericht_City_Extended` 🏆

**F1:** 0.108 | **Precision:** 0.987 | **Recall:** 0.057  

**Format:** `regex`  
**Rule ID:** `bb537474`  
**Description:**
Matches District Courts with city names, including specific missing cities like Ried im Innkreis, Mödling, Floridsdorf, and districts.

**Content:**
```
\bBezirksgerichts?\s+(?:Melk|Steyr|Feldbach|Rohrbach|Enns|Donaustadt|Fünfthau|Innere\s+Stadt\s+Wien|Schwechat|Liesing|Gmunden|Bad\s+Ischl|Wels|Telfs|Neusiedl\s+am\s+See|Favoriten|Josefstadt|Hietzing|Graz-West|Graz-Ost|Kirchdorf\s+an\s+der\s+Krems|Amstetten|Vöcklabruck|Döbling|St\.\s+Pöltten|Kufstein|Laa\s+an\s+der\s+Thaya|Schwaz|Hall|Dornbirn|Bludenz|Lustenau|Hohenems|Rankweil|Schaan|Vaduz|Balzers|Triesen|Triesenberg|Eschen|Mauren|Gamprin|Planken|Schellenberg|Au|Ruggell|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|Salzburg|Innsbruck|Eisenstadt|Klagenfurt|Graz|Wien|Linz|Bregenz|Feldkirch|Leoben|Lienz|Villach|Wels|St\.\s+Pöltten|Schwaz|Hall|Innsbruck|Dornbirn|Bludenz|Feldkirch|Bregenz|Lustenau|Dornbirn|Hohenems|Rankweil|Schaan|Vaduz|Balzers|Triesen|Triesenberg|Eschen|Mauren|Gamprin|Planken|Schellenberg|Au|Ruggell|Ried\s+im\s+Innkreis|Mödling|Floridsdorf|Fürstenfeld|Grieskirchen|Neulengbach|Deutschlandsberg|Hermagor|Freistadt)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.987 | 0.057 | 0.108 | 232 | 229 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 229 | 3 | 3784 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Jason Langeloh, vertreten durch die Mag. Martin Rützler, Rechtsanwalt in Dornbirn, gegen die beklagte Partei, Selma Einoeder, vertreten durch Mag. Alexander Gerngross und Mag. Klaus Köck, Rechtsanwälte in Premstätten bei Graz, wegen 6.795,66 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 223 C 1313/24w des Bezirksgerichts Graz-Ost den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an das Bezirksgericht Dornbirn wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Graz-Ost` | `Bezirksgerichts Graz-Ost` |
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

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_8`)


[3] Mit Antrag vom 21. 2. 2025 beantragte der Kläger – noch vor der vorbereitenden Tagsatzung – die Delegierung der Rechtssache an das Bezirksgericht Dornbirn, weil nicht nur er sowie das Unternehmen, in dessen Kfz-Werkstatt das Fahrzeug repariert worden sei, und dem er im Verfahren den Streit verkündet habe, sondern auch die von ihm in großer Zahl namhaft gemachten Zeugen ihren (Wohn-)Sitz in Vorarlberg hätten.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Dornbirn` | `Bezirksgericht Dornbirn` |

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_9`)


Zudem befinde sich das in Rede stehende Fahrzeug im Sprengel des Bezirksgerichts Dornbirn.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Dornbirn` | `Bezirksgerichts Dornbirn` |

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_10`)


Die Weiterführung des Verfahrens vor dem Bezirksgericht Graz-Ost wäre daher mit einem erheblichen Mehraufwand verbunden bzw müsste allenfalls praktisch das gesamte Beweisverfahren im Wege der Videokonferenz durchgeführt werden.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz-Ost` | `Bezirksgericht Graz-Ost` |

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_27`)


dieser könnte auch aus dem Sprengel des Bezirksgerichts Dornbirn oder dessen näherer Umgebung gewählt werden, was die Anreisekosten für eine Befundaufnahme jedenfalls reduzieren würde.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Dornbirn` | `Bezirksgerichts Dornbirn` |

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_4`)


Text Begründung: Die Klägerin begehrt mit der am 4. 8. 2017 beim Bezirksgericht Steyr eingebrachten Klage von dem in der Schweiz ansässigen Beklagten 4.660 EUR sA.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Steyr` | `Bezirksgericht Steyr` |

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_11`)


2018 erklärte sich dasBezirksgericht Steyrfür örtlich unzuständig und überwies (antragsgemäß) die Rechtssache an das nicht offenbar unzuständige Bezirksgericht Salzburg.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_22`)


Da das Bezirksgericht Salzburg die internationale Zuständigkeit Österreichs zur Erledigung der Klage rechtskräftig verneint hat, kann eine Ordination nicht mehr erfolgreich auf § 28 Abs 1 Z 1 JN gestützt werden.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Salzburg` | `Bezirksgericht Salzburg` |

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Schramm als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Florens Drehkopf, LLB, geboren am 16. Dezember 1952, AZ 7 P 203/15g des Bezirksgerichts Mödling, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Mödling zurückgestellt.  Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Mödling` | `Bezirksgerichts Mödling` |
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schramm` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Florens Drehkopf, LLB` (person)
- `16. Dezember 1952` (date)
- `Bezirksgericht Judenburg` (organisation)
- `Bezirksgerichts Judenburg` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_4`)


Das Bezirksgericht Mödling legte den Akt zur Entscheidung gemäß § 111 Abs 2 JN dem Obersten Gerichtshof vor (ON 8), ohne den Übertragungsbeschluss an die Parteien zuzustellen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Missed by this rule (FN):**

- `Obersten Gerichtshof` (organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_3`)


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

**Example 11** (doc_id: `deanon_260716_TRAIN/10Nc22_13m`) (sent_id: `deanon_260716_TRAIN/10Nc22_13m_11`)


Der Antrag war daher dem Bezirksgericht Innere Stadt Wien, in dessen Sprengel die verpflichtete Partei nach dem Antragsvorbringen ihren Sitz hat, gemäß § 44 JN zu überweisen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innere Stadt Wien` | `Bezirksgericht Innere Stadt Wien` |

**Example 12** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen Selma Eichler, LLM, geboren 13. September 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt. Begründung:  Rechtliche Beurteilung [1] Mit Beschluss vom 12.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Graz-West` | `Bezirksgerichts Graz-West` |
| `Bezirksgericht Graz-West` | `Bezirksgericht Graz-West` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Nowotny` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Selma Eichler, LLM` (person)
- `13. September` (date)

**Example 13** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_4`)


9. 2023 übertrug das Bezirksgericht Graz-West die Zuständigkeit zur Führung der Pflegschaftssache dem Bezirksgericht Braunau am Inn, das die Übernahme jedoch ablehnte.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz-West` | `Bezirksgericht Graz-West` |

**Missed by this rule (FN):**

- `Bezirksgericht Braunau am Inn` (organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/10Nc27_23m`) (sent_id: `deanon_260716_TRAIN/10Nc27_23m_5`)


[2] Das Bezirksgericht Graz-West legte den Akt daraufhin dem Obersten Gerichtshof zur Entscheidung gemäß § 111 Abs 2 JN vor, ohne den Übertragungsbeschluss den Parteien zuzustellen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Graz-West` | `Bezirksgericht Graz-West` |

**Missed by this rule (FN):**

- `Obersten Gerichtshof` (organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_3`)


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

**Example 16** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_7`)


[2] Mit Beschluss vom 10. 8. 2020 übertrug das zunächst in dieser Rechtssache angerufene Bezirksgericht Vöcklabruck die Zuständigkeit gemäß § 111 Abs 1 JN an das Bezirksgericht Villach, weil sich die Minderjährige nunmehr in einem Containerdorf in Kreutzerstraße 7, 4851 Haunolding, Österreich aufhalte (ON 7).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Vöcklabruck` | `Bezirksgericht Vöcklabruck` |
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Missed by this rule (FN):**

- `Kreutzerstraße 7, 4851 Haunolding, Österreich` (address)

**Example 17** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_9`)


Das Bezirksgericht Villach übernahm die Zuständigkeit mit Beschluss vom 19. 8. 2020 (ON 8), schrieb eine Tagsatzung für den 28.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Example 18** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_13`)


Daraufhin beraumte das Bezirksgericht Villach die Tagsatzung ab, widerrief das Zustellersuchen (ON 20a) und übertrug mitBeschluss vom 10.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Example 19** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_15`)


2021die Zuständigkeit zur Besorgung dieser Rechtssache nach § 111 Abs 1 JN an das Bezirksgericht Josefstadt (ON 22).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Example 20** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_17`)


Das Bezirksgericht Josefstadt lehnte die Übernahme der Zuständigkeit unter Rückmittlung des Akts am 18.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Example 21** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_18`)


1. 2021 bzw mit Beschluss vom 29. 1. 2021 ab, weil § 111 JN auf Verfahren in Abstammungssachen keine Anwendung finde und die Minderjährige im Zeitpunkt der Antragstellung ihren gewöhnlichen Aufenthalt nicht im Sprengel des Bezirksgerichts Josefstadt gehabt habe (ON 28).

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Josefstadt` | `Bezirksgerichts Josefstadt` |

**Example 22** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_20`)


Das Bezirksgericht Villach retournierte den Akt daraufhin an das Bezirksgericht Josefstadt mit dem Hinweis, dass der Akt vom Bezirksgericht Josefstadt dem gemeinsam übergeordneten Gericht vorzulegen sei (ON 30).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Example 23** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_21`)


[7] Letztlich legte das Bezirksgericht Josefstadt die Akten dem Obersten Gerichtshof zur Entscheidung des Zuständigkeitsstreits vor.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Missed by this rule (FN):**

- `Obersten Gerichtshof` (organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_22`)


[8] Die vom Bezirksgericht Villach veranlasste Vorlage der Akten an den Obersten Gerichtshof ist verfrüht:  Rechtliche Beurteilung [9] Übertragungsbeschlüsse nach § 111 JN sind durch die Parteien anfechtbar (RIS-Justiz RS0046981 [insb T5]).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Villach` | `Bezirksgericht Villach` |

**Missed by this rule (FN):**

- `Obersten Gerichtshof` (organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_3`)


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

**Example 26** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_5`)


Das von der Klägerin mit ihrer Klage angerufene Bezirksgericht Schwechat hat die internationale und örtliche Zuständigkeit rechtskräftig verneint (RIS-Justiz RS0046450).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 27** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_11`)


Unter Berücksichtigung dieser Vorgaben erscheint eine Zuweisung der Sache an das Bezirksgericht Schwechat als zweckmäßig.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 28** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_3`)


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

**Example 29** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_7`)


Das vom Kläger angerufene Bezirksgericht Schwechat sprach rechtskräftig seine (internationale) Unzuständigkeit aus.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 30** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_14`)


An die rechtskräftige Verneinung der internationalen Zuständigkeit des vom Kläger angerufenen Bezirksgerichts Schwechat ist der Oberste Gerichtshof gebunden (RIS-Justiz RS0046568).

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Schwechat` | `Bezirksgerichts Schwechat` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_38`)


Unter Berücksichtigung dieser Vorgaben hat eine Zuweisung an das Bezirksgericht Schwechat zu erfolgen, lag doch zum einen der Abflugort in dessen Sprengel und wurde zum anderen die Klage bereits bei diesem Gericht behandelt (6 Nc 31/20s mwN ua).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Schwechat` | `Bezirksgericht Schwechat` |

**Example 32** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_4`)


Anstelle des Bezirksgerichts Kitzbühel wird das Bezirksgericht Mödling als zur Führung des Verlassenschaftsverfahrens zuständiges Gericht bestimmt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Missed by this rule (FN):**

- `Bezirksgerichts Kitzbühel` (organisation)

**Example 33** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_6`)


Die nachlasszugehörigen Liegenschaften sind überwiegend im Sprengel des Bezirksgerichts Mödling situiert.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Mödling` | `Bezirksgerichts Mödling` |

**Example 34** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_8`)


Die - durch einen Notar mit Kanzleisitz in Wien vertretene - Witwe und die beiden minderjährigen Kinder des Verstorbenen, für die ein Rechtsanwalt mit Kanzleisitz in Wien als Kollisionskurator bestellt wurde, halten sich nach dem von ihnen bestätigten Antragsvorbringen ebenfalls im Sprengel des Bezirksgerichts Mödling auf.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Mödling` | `Bezirksgerichts Mödling` |

**Example 35** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_10`)


Im Hinblick auf die angeführten Umstände erscheint die Übertragung der Zuständigkeit an das Bezirksgericht Mödling im Sinne des § 31 Abs 1 JN zweckmäßig und geeignet, eine Verkürzung und Verbilligung des Verfahrens zu bewirken.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Mödling` | `Bezirksgericht Mödling` |

**Example 36** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Bartholomäus Junghahn, geboren am 8. Mai 1999, und der minderjährigen HR Sophie Elefteriadis, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Favoriten` | `Bezirksgerichts Favoriten` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Bartholomäus Junghahn` (person)
- `HR Sophie Elefteriadis` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 37** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Leander Lindlahr, geboren am 1. August 2011, und des mj Yussuf Prussog, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Donaustadt` | `Bezirksgerichts Donaustadt` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Leander Lindlahr` (person)
- `Yussuf Prussog` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 38** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des minderjährigen Cedric Annamüller, geboren am 8. März 2007, 16. Mai 1964, vertreten durch das Land Kärnten als Kinder- und Jugendhilfeträger (Magistrat der Landeshauptstadt Klagenfurt, Abteilung für Jugend und Familie, Bahnhofstraße 35, 9010 Klagenfurt am Wörthersee), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Graz, gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 8. Jänner 2016, GZ 4 R 283/15g-16, womit der Beschluss des Bezirksgerichts Klagenfurt vom 17. November 2015, GZ 1 Pu 69/10x-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Klagenfurt` | `Bezirksgerichts Klagenfurt` |

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
- `Landesgerichts Klagenfurt` (organisation)

**Example 39** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludmilla von Amelunxen, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, gegen die beklagte Partei Svetlana Leinhäuser, vertreten durch Dr. Thomas Brückl, Mag. Christian Breit, Rechtsanwälte in Ried im Innkreis, wegen 1.778,52 EUR und Unterlassung (Streitwert 2.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Wels als Berufungsgericht vom 25. Jänner 2023, GZ 21 R 2/23b-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Grieskirchen vom 27. Oktober 2022, GZ 3 C 642/20h-27, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Grieskirchen` | `Bezirksgerichts Grieskirchen` |

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
- `Landesgerichts Wels` (organisation)

**Example 40** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_5`)


Anita Schetzel, vertreten durch die Summereder Pichler Wächter Rechtsanwälte GmbH in Leonding, wegen 12.750 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Wels als Berufungsgericht vom 13. Dezember 2023, GZ 21 R 277/23v-53, mit dem das Urteil des Bezirksgerichts Wels vom 23. August 2023, GZ 9 C 430/22s-47, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Die Revision wird in Ansehung der Klageforderungen von 2.700 EUR sA, 4.575 EUR sA und 450 EUR sA zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Wels` | `Bezirksgerichts Wels` |

**Missed by this rule (FN):**

- `Anita Schetzel` (person)
- `Landesgerichts Wels` (organisation)

**Example 41** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der minderjährigen Annabelle Thurnher, geboren am 24. Juni 2001, vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung, Bezirk 10, 1100 Wien, Van der Nüll-Gasse 20), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 17. September 2009, GZ 44 R 454/09d-38, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Favoriten vom 16. Juni 2009, GZ 40 P 36/08f-U-26, teilweise abgeändert wurde, den B e s c h l u s s gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Favoriten` | `Bezirksgerichts Favoriten` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schinko` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Annabelle Thurnher` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 42** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_4`)


Malik Schoch, geboren 7. November 2002, 2. 7. Juli 2025, geboren 10. Juli 2004, und 3. Alan Schindlmair, geboren 7. August 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Timon Schönswetter, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Döbling` | `Bezirksgerichts Döbling` |

**Missed by this rule (FN):**

- `Malik Schoch` (person)
- `7. November` (date)
- `7. Juli 2025` (date)
- `10. Juli` (date)
- `Alan Schindlmair` (person)
- `7. August` (date)
- `Mag. Florian Kucera` (person)
- `Mag. Timon Schönswetter` (person)
- `Doschek Rechtsanwalts GmbH` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_4`)


Text Begründung: Beim Bezirksgericht Innere Stadt Wien ist zur AZ 2 P 88/07t ein Pflegschaftsverfahren betreffend die mj Kinder Basil Biewer anhängig.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innere Stadt Wien` | `Bezirksgericht Innere Stadt Wien` |

**Missed by this rule (FN):**

- `Basil Biewer` (person)

**Example 44** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Jaden Meyerjohann, geboren am 3. Juli 2020, Leroy Jungschmidt, geboren am 28. Mai 1965 und Clemens Theocharakis, geboren am 25. März 1999, in Pflege und Erziehung der Mutter Emanuela Janischefsky, vertreten durch das Land Vorarlberg als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Feldkirch, Schlossgraben 1, 6800 Feldkirch), wegen Gewährung von Unterhaltsvorschuss, über den Revisionsrekurs des Vaters Ashley Biesert, vertreten durch Mag. Hans-Christian Obernberger, Rechtsanwalt in Feldkirch, gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 12. Juli 2011, GZ 3 R 198/11g, 3 R 199/11d, 3 R 200/11a-18, womit die Beschlüsse des Bezirksgerichts Feldkirch vom 18. Mai 2011, GZ 12 Pu 141/11f-4 bis 6, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Feldkirch` | `Bezirksgerichts Feldkirch` |

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
- `Landesgerichts Feldkirch` (organisation)

**Example 45** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch und Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der minderjährigen Karsten Alberter, geboren am 2. April 2010, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Wien-Umgebung, Fachgebiet Jugendwohlfahrt), 3400 Klosterneuburg, Leopoldstraße 21, über das als „Berufung“ bezeichnete Rechtsmittel des Vaters Helmut Dreilich, gegen den Beschluss des Landesgerichts Korneuburg als Rekursgericht vom 25. März 2013, GZ 23 R 30/13v-53, womit der Beschluss des Bezirksgerichts Schwechat vom 27. August 2012, GZ 8 Pu 190/11i-39, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.  Text Begründung: Verfahrensgegenstand ist die Festsetzung des gesetzlichen Unterhalts für die mj Lena Amini.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Schwechat` | `Bezirksgerichts Schwechat` |

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
- `Landesgerichts Korneuburg` (organisation)
- `Lena Amini` (person)

**Example 46** (doc_id: `deanon_260716_TRAIN/10Ob30_19p`) (sent_id: `deanon_260716_TRAIN/10Ob30_19p_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der minderjährigen Maja Dolleschell, geboren 14. August 2009, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Melk, 3390 Melk, Abt Karl-Straße 25a) wegen Unterhaltsvorschüssen, über den Revisionsrekurs des Kindes gegen den Beschluss des Landesgerichts St. Pölten als Rekursgericht vom 23. Jänner 2019, GZ 23 R 6/19h-52, mit dem der Beschluss des Bezirksgerichts Melk vom 21. November 2018, GZ 22 Pu 194/16m-42, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Melk` | `Bezirksgerichts Melk` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Maja Dolleschell` (person)
- `14. August` (date)
- `Bezirkshauptmannschaft Melk` (organisation)
- `Landesgerichts St. Pölten` (organisation)

**Example 47** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Ziegelbauer als Vorsitzenden sowie die Hofrätin Dr. Faber und die Hofräte Mag. Schober, Dr. Thunhart und Dr. Annerl als weitere Richter in der Pflegschaftssache der minderjährigen Meinrad Bruhnsen, geboren 30. Januar 2006, vertreten durch das Land Wien als Träger der Kinder- und Jugendhilfe (Magistrat der Stadt Wien, Rechtsvertretung Bezirke 1, 4 bis 9, 1060 Wien, Amerlingstraße 11), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch die Präsidentin des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 31. Oktober 2022, GZ 43 R 323/22a-17, mit dem der Beschluss des Bezirksgerichts Innere Stadt Wien vom 9. Juni 2022, GZ 4 Pu 58/22a-7, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Innere Stadt Wien` | `Bezirksgerichts Innere Stadt Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Ziegelbauer` (person)
- `Dr. Faber` (person)
- `Mag. Schober` (person)
- `Dr. Thunhart` (person)
- `Dr. Annerl` (person)
- `Meinrad Bruhnsen` (person)
- `30. Januar` (date)
- `Magistrat der Stadt Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 48** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_6`)


Mit einstweiliger Verfügung des Bezirksgerichts Innere Stadt Wien vom 28. April 2022 wurde der Vater verpflichtet, dem Kind einen vorläufigen monatlichen Unterhaltsbeitrag in Höhe von 38 EUR zu leisten (ON 2).

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Innere Stadt Wien` | `Bezirksgerichts Innere Stadt Wien` |

**Example 49** (doc_id: `deanon_260716_TRAIN/10Ob41_14y`) (sent_id: `deanon_260716_TRAIN/10Ob41_14y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in den verbundenen Familienrechtssachen des Antragstellers DI Dr. Bodo Kaczynski, geboren am 25. Juli 1975, vertreten durch Mag. Werner Thurner, Rechtsanwalt in Graz, gegen die Antragsgegnerinnen 1. Wolfgang Lombardini, geboren am 4. Dezember 2022, 2. Livia Löblein, geboren am 11. Januar 1966, vertreten durch Mörth Ecker Filzmaier, Rechtsanwalts-Partnerschaft in Graz, wegen Unterhalt, über den Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 24. September 2013, GZ 2 R 11/13x-76, womit der Beschluss des Bezirksgerichts Graz-Ost vom 26. November 2012, GZ 231 Fam 14/11a, 231 Fam 17/11t, 231 Fam 18/11i-60, teilweise bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.  Text Begründung: DasErstgerichtsetzte den monatlichen Unterhalt für die Erstantragsgegnerin ab 1. 2. 2011 von 390 EUR um 30 EUR auf 360 EUR herab (Punkt 1);

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Graz-Ost` | `Bezirksgerichts Graz-Ost` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `DI Dr. Bodo Kaczynski` (person)
- `25. Juli 1975` (date)
- `Mag. Werner Thurner` (person)
- `Wolfgang Lombardini` (person)
- `4. Dezember 2022` (date)
- `Livia Löblein` (person)
- `11. Januar 1966` (date)
- `Mörth Ecker Filzmaier, Rechtsanwalts-Partnerschaft` (organisation)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)

**Example 50** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Pflegschaftssache 1. der mj Emma Mittelstaedt, geboren am 21. Mai 2025 und 2. des mj Milena Roesche, geboren am 25. Juni 1957, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung Bezirk 22, 1220 Wien, Hirschstettner Straße 19-21/Stiege N), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 10. Dezember 2014, GZ 42 R 343/13x, 42 R 344/13v und 42 R 345/13s-106, womit den Rekursen der Minderjährigen gegen den Beschluss des Bezirksgerichts Donaustadt vom 14. März 2013, GZ 3 Pu 61/12x-40, teilweise Folge gegeben wurde (Pkt 1 des Spruchs), dem Rekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen die Beschlüsse des Bezirksgerichts Donaustadt (jeweils) vom 6. Juni 2013, GZ 3 Pu 61/12x-49 und 3 Pu 61/12x-50, Folge gegeben (Pkt 2a des Spruchs), und aus Anlass des Rekurses die Anträge der Minderjährigen auf Gewährung von Unterhaltsvorschüssen zur Gänze abgewiesen wurden (Pkt 2b des Spruchs), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Donaustadt` | `Bezirksgerichts Donaustadt` |
| `Bezirksgerichts Donaustadt` | `Bezirksgerichts Donaustadt` |

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
- `Magistrat der Stadt Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 51** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_7`)


Mit Beschluss des Bezirksgerichts Josefstadt vom 28. 4. 2004, GZ 16 P 99/00g-363, war der Antragsgegner zur Zahlung eines Unterhalts ab 1. 8. 2004 bis auf weiteres, längstens jedoch bis zur Selbsterhaltungsfähigkeit der Antragstellerin in Höhe von monatlich 250 EUR verpflichtet worden.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Josefstadt` | `Bezirksgerichts Josefstadt` |

**Example 52** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_8`)


Am 20. 9. 2016 beantragte die Antragstellerin beim Bezirksgericht Josefstadt die Erhöhung der monatlichen Unterhaltszahlung auf 440 EUR ab 1. 9. 2016.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Josefstadt` | `Bezirksgericht Josefstadt` |

**Example 53** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_9`)


Im Rahmen seiner Äußerung zu diesem Unterhaltserhöhungsantrag lehnte der Antragsgegner jeweils alle Richter des Bezirksgerichts Josefstadt und des diesem übergeordneten Landesgerichts für Zivilrechtssachen Wien ab.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Josefstadt` | `Bezirksgerichts Josefstadt` |

**Missed by this rule (FN):**

- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 54** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_32`)


2.2 Von diesen Grundsätzen der Rechtsprechung ist das Oberlandesgericht Wien bei seiner Entscheidung nicht abgewichen, wenn es den Ablehnungsantrag gegen alle Richter und Richterinnen des Landesgerichts für Zivilrechtssachen Wien und des Bezirksgerichts Josefstadt als nicht dem Gesetz gemäß ausgeführt zurückgewiesen hat.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Josefstadt` | `Bezirksgerichts Josefstadt` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 55** (doc_id: `deanon_260716_TRAIN/10Ob57_13z`) (sent_id: `deanon_260716_TRAIN/10Ob57_13z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der Kinder Mikolaj Eleftheriadou, geboren am 9. August 1991, Helge Schuchmann, geboren am 30. September 1992, mj Isabel Rahnfeld, geboren am 22. Dezember 1998 und mj PhD Daniel Coutand, geboren am 18. Jänner 2001, wegen Unterhaltsvorschuss, infolge Revisionsrekurses des Vaters Mag. Dirk Hükelheim, vertreten durch Mag. Roland Marko, Rechtsanwalt in Wien, dieser vertreten durch Dr. Francisco Rumpf, Rechtsanwalt in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 7. Juni 2013, GZ 43 R 391/08f ua -U-458, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 12. November 2007, GZ 2 P 88/07t-U-238, abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Innere Stadt Wien` | `Bezirksgerichts Innere Stadt Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mikolaj Eleftheriadou` (person)
- `Helge Schuchmann` (person)
- `Isabel Rahnfeld` (person)
- `PhD Daniel Coutand` (person)
- `Mag. Dirk Hükelheim` (person)
- `Mag. Roland Marko` (person)
- `Dr. Francisco Rumpf` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 56** (doc_id: `deanon_260716_TRAIN/10Ob6_24s`) (sent_id: `deanon_260716_TRAIN/10Ob6_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Dr. Weber, Mag. Schober, Dr. Annerl und Dr. Vollmaier als weitere Richter in der Rechtssache des (ehemaligen) Klägers und Gegners der gefährdeten Parteien Agatha von der Heide, vertreten durch MMag. Dr. Sebastian Pribas, Rechtsanwalt in Dornbirn, als Verfahrenshelfer, dieser vertreten durch Mag. Benedikt Walch, Rechtsanwalt in Lech am Arlberg, gegen die (ehemals) Beklagte und erstgefährdete Partei Alva Sengül, sowie die zweitgefährdete Partei mj Selina Birkmeir, und die drittgefährdete Partei mj Harald Ladwig, LLM, alle wohnhaft in In der Klaus 72, 4785 Bach, Österreich, und vertreten durch Mag. German Bertsch, Rechtsanwalt in Feldkirch, wegen Ehescheidung sowie einstweiligem Ehegatten- und Kindesunterhalt, über den außerordentlichen Revisionsrekurs des Gegners der gefährdeten Parteien gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 22. September 2022, GZ 3 R 187/22f-323, womit der Beschluss des Bezirksgerichts Feldkirch vom 29. April 2022, GZ 2 C 23/17g-306, bestätigt wurde, den Beschluss gefasst:  Spruch In Ansehung der auf Zahlung von einstweiligem Ehegattenunterhalt gerichteten Begehren wird der außerordentliche Revisionsrekurs gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Feldkirch` | `Bezirksgerichts Feldkirch` |

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
- `Landesgerichts Feldkirch` (organisation)

**Example 57** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_10`)


Für ihn ist ein Sachwalter bestellt, der seit 2011 alle Angelegenheiten (§ 268 Abs 3 Z 3 ABGB) zu besorgen hat (siehe den Beschluss des Bezirksgericht Bezirksgericht Freistadt vom 15.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Freistadt` | `Bezirksgericht Freistadt` |

**Example 58** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__3`)


Kopf Der Oberste Gerichtshof hat am 10. Juni 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Holzweber als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll, Dr. Schwab, Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Gotsmy als Schriftführer in der Strafsache gegen Jennifer Janauscheck wegen des Vergehens des Raufhandels nach § 91 Abs 2 zweiter Fall StGB über die von der Generalprokuratur gegen das Urteil des Bezirksgerichts Kufstein vom 30. Jänner 2008, GZ 3 U 166/07x-49, und den unter einem gefassten Beschluss gemäß § 494a Abs 1 Z 2 StPO erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Eisenmenger, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Kufstein` | `Bezirksgerichts Kufstein` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Holzweber` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Dr. Schwab` (person)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Hetlinger` (person)
- `Mag. Gotsmy` (person)
- `Jennifer Janauscheck` (person)
- `Dr. Eisenmenger` (person)

**Example 59** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__4`)


Im Verfahren AZ 3 U 166/07x des Bezirksgerichts Kufstein verletzen das Gesetz 1. das Urteil vom 30. Jänner 2008 in seinem Strafausspruch in § 5 Z 5 JGG und § 31 Abs 1 zweiter Satz StGB;

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Kufstein` | `Bezirksgerichts Kufstein` |

**Example 60** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__5`)


2. der unter einem gefasste Beschluss gemäß § 494a Abs 1 Z 2 StPO auf Absehen vom Widerruf der zum AZ 3 U 350/06d des Bezirksgerichts Kufstein gewährten bedingten Strafnachsicht in §§ 494a Abs 1 und 495 Abs 2 StPO sowie § 55 Abs 1 StGB.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Kufstein` | `Bezirksgerichts Kufstein` |

**Example 61** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__6`)


Das Urteil, das im Übrigen unberührt bleibt, wird in seinem Strafausspruch aufgehoben und dem Bezirksgericht Kufstein im Umfang der Aufhebung die neuerliche Verhandlung und Entscheidung aufgetragen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Kufstein` | `Bezirksgericht Kufstein` |

**Example 62** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__7`)


Text Gründe: Die am 26. Jänner 1991 geborene Jennifer Johannwerner wurde mit rechtskräftigem Urteil des Bezirksgerichts Kufstein vom 16. April 2007, GZ 3 U 350/06d-20, mehrerer Vergehen der Körperverletzung nach § 83 Abs 1 StGB und des Vergehens der Sachbeschädigung nach § 125 StGB schuldig erkannt und hiefür unter Anwendung des § 5 Z 4 JGG zu einer unter Bestimmung einer dreijährigen Probezeit bedingt nachgesehenen Freiheitsstrafe von zwei Monaten verurteilt (Blg ./2 zum Bezugsakt AZ 3 U 166/07x des Bezirksgerichts Kufstein).

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Kufstein` | `Bezirksgerichts Kufstein` |
| `Bezirksgerichts Kufstein` | `Bezirksgerichts Kufstein` |

**Missed by this rule (FN):**

- `Jennifer Johannwerner` (person)

**Example 63** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__8`)


Mit rechtskräftigem Urteil des Bezirksgerichts Kufstein vom 30. Jänner 2008, GZ 3 U 166/07x-49, wurde die auch damals noch Jugendliche des am 28. Oktober 2006 begangenen Vergehens des Raufhandels nach § 91 Abs 2 zweiter Fall StGB schuldig erkannt und hiefür unter Bedachtnahme gemäß „§§ 31 Abs 1 und 40“ StGB auf das Urteil des Bezirksgerichts Kufstein vom 16. April 2007, GZ 3 U 350/06d-20, nach dem zweiten Strafsatz des § 91 Abs 2 StGB zu einer Zusatzgeldstrafe von 200 Tagessätzen, für den Fall der Uneinbringlichkeit zu 100 Tagen Ersatzfreiheitsstrafe verurteilt (das mit Beschluss ON 64 richtig gestellte Urteilsdatum wurde entgegen richterlicher Anordnung [S 306] am Rande der Urteilsurschrift ON 49 nicht beigesetzt).

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Kufstein` | `Bezirksgerichts Kufstein` |
| `Bezirksgerichts Kufstein` | `Bezirksgerichts Kufstein` |

**Example 64** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__9`)


Unter einem erging der Beschluss, gemäß § 494a Abs 1 Z 2 StPO vom Widerruf der zum AZ 36 Hv 118/05p des Landesgerichts Innsbruck und zum AZ 3 U 350/06d des Bezirksgerichts Kufstein jeweils gewährten bedingten Strafnachsicht abzusehen.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Kufstein` | `Bezirksgerichts Kufstein` |

**Missed by this rule (FN):**

- `Landesgerichts Innsbruck` (organisation)

**Example 65** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__12`)


Rechtliche Beurteilung Wie die Generalprokuratur in ihrer zur Wahrung des Gesetzes erhobenen Nichtigkeitsbeschwerde zutreffend ausführt, stehen das Urteil des Bezirksgerichts Kufstein vom 30. Jänner 2008 in seinem Strafausspruch sowie der unter einem gefasste Beschluss gemäß § 494a Abs 1 Z 2 StPO mit dem Gesetz nicht im Einklang: Die Beschuldigte stand zum Tatzeitpunkt im 16.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Kufstein` | `Bezirksgerichts Kufstein` |

**Example 66** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__19`)


Die vorliegende Jugendstraftat vom 28. Oktober 2006 hätte bereits in dem früheren Verfahren AZ 3 U 350/06d des Bezirksgerichts Kufstein abgeurteilt werden können.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Kufstein` | `Bezirksgerichts Kufstein` |

**Example 67** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__22`)


Durch die Verhängung einer (Zusatz-)Geldstrafe von 200 Tagessätzen in Missachtung des durch § 5 Z 5 JGG geänderten Strafrahmens bei ersichtlicher Nichtanwendung des § 37 Abs 1 StGB und demzufolge auch der bei Zusatzstrafen anzuwendenden Strafbemessungsvorschrift des § 31 Abs 1 zweiter Satz StGB hat das Bezirksgericht Kufstein das Gesetz in den genannten Bestimmungen zum Nachteil der Verurteilten verletzt.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Kufstein` | `Bezirksgericht Kufstein` |

**Example 68** (doc_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y_`) (sent_id: `deanon_260716_TRAIN/12Os197_09a_12Os198_09y__23`)


Der Oberste Gerichtshof sah sich daher gemäß § 292 letzter Satz StPO veranlasst, das Urteil im Strafausspruch aufzuheben und dem Bezirksgericht Kufstein in diesem Umfang die Verfahrenserneuerung aufzutragen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Kufstein` | `Bezirksgericht Kufstein` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)

**Example 69** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_3`)


Kopf Der Oberste Gerichtshof hat am 14. August 2014 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, die Hofräte des Obersten Gerichtshofs Dr. Lässig, Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Anscheringer als Schriftführer in der Strafsache gegen Natascha von Bohr wegen Vergehen des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 erster und zweiter Fall, Abs 2 SMG in dem zu AZ 18 U 198/14k des Bezirksgerichts Innere Stadt Wien und AZ 18 U 266/14m des Bezirksgerichts Linz zwischen diesen Gerichten geführten Zuständigkeitsstreit den Beschluss gefasst:  Spruch Das Hauptverfahren ist vom Bezirksgericht Linz zu führen.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Innere Stadt Wien` | `Bezirksgerichts Innere Stadt Wien` |
| `Bezirksgerichts Linz` | `Bezirksgerichts Linz` |
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

**Example 70** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_5`)


Das Bezirksgericht Linz überwies die Sache dem Bezirksgericht Innere Stadt Wien mit der Begründung örtlicher Unzuständigkeit (vgl ON 1 S 3: „erste Taten in Wien“).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Linz` | `Bezirksgericht Linz` |
| `Bezirksgericht Innere Stadt Wien` | `Bezirksgericht Innere Stadt Wien` |

**Example 71** (doc_id: `deanon_260716_TRAIN/13Ns45_14t`) (sent_id: `deanon_260716_TRAIN/13Ns45_14t_13`)


Aus dem hier zur Anwendung kommenden Anknüpfungstatbestand des § 36 Abs 3 erster Satz (iVm § 37 Abs 2 zweiter Satz) StPO folgt demnach die Zuständigkeit des Bezirksgerichts Linz.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Linz` | `Bezirksgerichts Linz` |

**Example 72** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__3`)


Kopf Der Oberste Gerichtshof hat am 26. Februar 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Nordmeyer, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Schriftführers Dr. Schöll in der Strafsache gegen Robert Ultsch wegen des Vergehens der Urkundenfälschung nach § 223 Abs 1 StGB und einer weiteren strafbaren Handlung, AZ 13 U 351/18d des Bezirksgerichts Innere Stadt Wien, über den auf den Beschluss des Landesgerichts für Strafsachen Wien als Berufungsgericht vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), bezogenen Antrag der Generalprokuratur auf außerordentliche Wiederaufnahme des Verfahrens und über ihre gegen den Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30 der U-Akten) zur Wahrung des Gesetzes erhobene Nichtigkeitsbeschwerde nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Schneider, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Innere Stadt Wien` | `Bezirksgerichts Innere Stadt Wien` |
| `Bezirksgerichts Innere Stadt Wien` | `Bezirksgerichts Innere Stadt Wien` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Mag. Michel` (person)
- `Dr. Oberressl` (person)
- `Dr. Brenner` (person)
- `Dr. Schöll` (person)
- `Robert Ultsch` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Mag. Schneider` (person)

**Example 73** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__5`)


In Stattgebung des Antrags der Generalprokuratur wird im außerordentlichen Weg die Wiederaufnahme des Berufungsverfahrens verfügt, der Beschluss des Landesgerichts für Strafsachen Wien vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23 der U-Akten), aufgehoben und die Sache zur neuerlichen Entscheidung über die Berufung des Angeklagten gegen das Urteil des Bezirksgerichts Innere Stadt Wien vom 27. November 2018 (ON 19 der U-Akten) an das Landesgericht für Strafsachen Wien verwiesen.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Innere Stadt Wien` | `Bezirksgerichts Innere Stadt Wien` |

**Missed by this rule (FN):**

- `Landesgerichts für Strafsachen Wien` (organisation)
- `Landesgericht für Strafsachen Wien` (organisation)

**Example 74** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__6`)


2. Der Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30 der U-Akten) verletzt §§ 270 Abs 3, 271 Abs 7 StPO iVm §§ 447, 458 zweiter Satz StPO.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Innere Stadt Wien` | `Bezirksgerichts Innere Stadt Wien` |

**Example 75** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__7`)


Text Gründe: Mit Urteil des Bezirksgerichts Innere Stadt Wien (ON 19) wurde Robert Ulrici jeweils eines Vergehens der Urkundenfälschung nach § 223 Abs 1 StGB und der Verletzung der Unterhaltspflicht nach § 198 Abs 1 StGB schuldig erkannt und hiefür zu einer bedingt nachgesehenen Freiheitsstrafe verurteilt. Nach Verkündung des Urteils und erteilter Rechtsmittelbelehrung erklärte der – nicht durch einen Verteidiger vertretene (vgl § 57 Abs 2 dritter Satz StPO;Fabrizy, StPO13§ 57 Rz 10) – Angeklagte zunächst, auf Rechtsmittel zu verzichten (ON 18 S 5).

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Innere Stadt Wien` | `Bezirksgerichts Innere Stadt Wien` |

**Missed by this rule (FN):**

- `Robert Ulrici` (person)

**Example 76** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__10`)


Im Protokoll über die Hauptverhandlung vor dem Bezirksgericht Innere Stadt Wien ist als Tag der Hauptverhandlung „23. 11. 2018“ angeführt (ON 18 S 1).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innere Stadt Wien` | `Bezirksgericht Innere Stadt Wien` |

**Example 77** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__13`)


Mit Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30) wurden sowohl das Protokoll über die Hauptverhandlung (ON 18) als auch die Urteilsurschrift (ON 19) in Ansehung des „Verhandlungsdatum[s]“ von „23. 11. 2018“ auf „27. 11. 2018“ berichtigt.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Innere Stadt Wien` | `Bezirksgerichts Innere Stadt Wien` |

**Example 78** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__14`)


Rechtliche Beurteilung Wie die Generalprokuratur in ihrem Antrag auf außerordentliche Wiederaufnahme des Verfahrens zutreffend darlegt, bestehen gegen die Richtigkeit der dem Beschluss des Landesgerichts für Strafsachen Wien als Berufungsgericht vom 2. Mai 2019, AZ 132 Bl 18/19d (ON 23), zugrunde gelegten Tatsache, das erstinstanzliche Urteil sei am 23. November 2018 verkündet worden, erhebliche Bedenken: Die Verfügung des Bezirksgerichts Innere Stadt Wien vom 1. November 2018 auf Ladung des Angeklagten zur Hauptverhandlung am 27. November 2018 (ON 1 [unjournalisiert] S 6), das auf der letzten Seite der Urteilsurschrift angeführte Urteilsdatum „27. November 2018“ (ON 19 S 5), die im Verfahrensakt enthaltene (unjournalisierte) Äußerung der Staatsanwaltschaft Wien vom 15. November 2019, AZ 126 BAZ 822/11s, sowie der Berichtigungsbeschluss vom 4. Dezember 2019 (ON 30) legen qualifiziert nahe, dass das Urteil am27. November 2018verkündet wurde.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Innere Stadt Wien` | `Bezirksgerichts Innere Stadt Wien` |

**Missed by this rule (FN):**

- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 79** (doc_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f_`) (sent_id: `deanon_260716_TRAIN/13Os7_20h_13Os8_20f__18`)


Ebenso zutreffend führt die Generalprokuratur in ihrer zur Wahrung des Gesetzes erhobenen Nichtigkeitsbeschwerde aus, dass der Beschluss des Bezirksgerichts Innere Stadt Wien vom 4. Dezember 2019 (ON 30) in zweierlei Hinsicht das Gesetz verletzt: Die Ausfertigung der Urteilsurschrift mit unrichtigem Datum bewirkt ein – nicht die im § 260 Abs 1 Z 1 bis Z 3 und Abs 2 StPO erwähnten Punkte betreffendes – Formgebrechen, das (hier) der Richter des Bezirksgerichts allenfalls nach Anhörung der Beteiligten zu berichtigen hat (§ 270 Abs 3 erster Satz StPO iVm §§ 447, 458 zweiter Satz StPO;

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Innere Stadt Wien` | `Bezirksgerichts Innere Stadt Wien` |

**Example 80** (doc_id: `deanon_260716_TRAIN/14Ns52_18k`) (sent_id: `deanon_260716_TRAIN/14Ns52_18k_3`)


Kopf Der Oberste Gerichtshof hat am 13. November 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in der Strafsache gegen Daniel Bruchmüller wegen der Vergehen des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 erster und zweiter Fall, Abs 2 SMG in dem zu AZ 4 U 118/18k des Bezirksgerichts St. Pölten und zu AZ 18 U 242/18p des Bezirksgerichts Linz zwischen diesen Gerichten geführten Zuständigkeitsstreit nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung gemäß § 60 Abs 1 Satz 2 OGH-Geo.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Linz` | `Bezirksgerichts Linz` |

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
- `Daniel Bruchmüller` (person)
- `Bezirksgerichts St. Pölten` (organisation)
- `OGH` (organisation)

**Example 81** (doc_id: `deanon_260716_TRAIN/14Ns52_18k`) (sent_id: `deanon_260716_TRAIN/14Ns52_18k_4`)


2005 den Beschluss gefasst:  Spruch Für die Durchführung des Strafverfahrens ist das Bezirksgericht Linz zuständig.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Linz` | `Bezirksgericht Linz` |

**Example 82** (doc_id: `deanon_260716_TRAIN/14Ns52_18k`) (sent_id: `deanon_260716_TRAIN/14Ns52_18k_5`)


Gründe:  Rechtliche Beurteilung Mit beim Bezirksgericht Linz eingebrachtem Strafantrag vom 28. Juni 2018 (ON 12) legte die Staatsanwaltschaft Linz Daniel Berlage ein „ab ca Mitte Mai 2016 bis … 18. Jänner 2018“ (1) und am 18. Jänner 2018 „in Linz“ (2) gesetztes, als die Vergehen des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 erster und zweiter Fall, Abs 2 SMG beurteiltes Verhalten zur Last.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Linz` | `Bezirksgericht Linz` |

**Missed by this rule (FN):**

- `Daniel Berlage` (person)

**Example 83** (doc_id: `deanon_260716_TRAIN/14Ns52_18k`) (sent_id: `deanon_260716_TRAIN/14Ns52_18k_12`)


Das Bezirksgericht Linz überwies die Sache „gemäß § 37 Abs 2 StPO“ unter Hinweis auf eine im letztgenannten Verfahren durchgeführte Abfrage aus dem Zentralen Melderegister, aus der sich ergab, dass der Angeklagte von 20. März 2014 bis 5. Mai 2017, sohin zu Beginn des von der Anklage umfassten Tatzeitraums, im Bezirk Amstetten polizeilich gemeldet war (ON 14), wegen örtlicher Unzuständigkeit dem Bezirksgericht St. Pölten (ON 1 S 3 verso).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Linz` | `Bezirksgericht Linz` |

**Missed by this rule (FN):**

- `Bezirksgericht St. Pölten` (organisation)

**Example 84** (doc_id: `deanon_260716_TRAIN/14Ns52_18k`) (sent_id: `deanon_260716_TRAIN/14Ns52_18k_17`)


Die vom Bezirksgericht Linz vertretene Ansicht, die früheste vom Anklagevorwurf erfasste Tat sei an jenem Ort verübt worden, an dem der Angeklagte zur Zeit ihrer Begehung polizeilich gemeldet gewesen sei, findet im Gesetz keine Stütze;

| Predicted | Gold |
|---|---|
| `Bezirksgericht Linz` | `Bezirksgericht Linz` |

**Example 85** (doc_id: `deanon_260716_TRAIN/14Ns52_18k`) (sent_id: `deanon_260716_TRAIN/14Ns52_18k_20`)


Aus § 37 Abs 2 zweiter Satz StPO ergibt sich daher die Kompetenz des Bezirksgerichts Linz (vgl auch 11 Ns 66/14s).

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Linz` | `Bezirksgerichts Linz` |

**Example 86** (doc_id: `deanon_260716_TRAIN/14Ns62_15a`) (sent_id: `deanon_260716_TRAIN/14Ns62_15a_3`)


Kopf Der Oberste Gerichtshof hat am 20. Juli 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden sowie die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger und den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer in der Strafsache gegen Ferenc Florin und Gabor Schwiecker wegen des Vergehens des Diebstahls nach §§ 15, 127 StGB, AZ 9 U 170/15k des Bezirksgerichts Innsbruck über den Antrag der Angeklagten auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Innsbruck` | `Bezirksgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Philipp` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Hetlinger` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Ferenc Florin` (person)
- `Gabor Schwiecker` (person)
- `OGH` (organisation)

**Example 87** (doc_id: `deanon_260716_TRAIN/14Ns62_15a`) (sent_id: `deanon_260716_TRAIN/14Ns62_15a_5`)


Die Akten werden dem Oberlandesgericht Innsbruck zurückgestellt. Gründe:  Rechtliche Beurteilung Abgesehen davon, dass es sich bei der angegebenen Anschrift des Angeklagten nach der Aktenlage um eine „Briefkastenadresse“ handelt (ON 2 S 5 in ON 4) werden zur Frage allfälliger Täterschaftsform im Sprengel des Bezirksgerichts Innsbruck aufhältige Zeugen (ON 2 S 33 in ON 4) zu vernehmen sein.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Innsbruck` | `Bezirksgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Oberlandesgericht Innsbruck` (organisation)

**Example 88** (doc_id: `deanon_260716_TRAIN/15Ns104_16m`) (sent_id: `deanon_260716_TRAIN/15Ns104_16m_3`)


Kopf Der Oberste Gerichtshof hat am 28. Dezember 2016 durch den Senatspräsident des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Mag. Lendl und Dr. Mann in der Strafsache gegen Markus Herdemertens wegen des Vergehens des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 erster und zweiter Fall und Abs 2 SMG, AZ 2 U 63/16z des Bezirksgerichts Bad Ischl, über den Antrag der Staatsanwaltschaft Wels auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Bad Ischl` | `Bezirksgerichts Bad Ischl` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Prof. Dr. Danek` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Lendl` (person)
- `Dr. Mann` (person)
- `Markus Herdemertens` (person)
- `OGH` (organisation)

**Example 89** (doc_id: `deanon_260716_TRAIN/15Os107_16y`) (sent_id: `deanon_260716_TRAIN/15Os107_16y_3`)


Kopf Der Oberste Gerichtshof hat am 16. November 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Mag. Lendl und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in Gegenwart des Richteramtsanwärters Mag. Beran als Schriftführer in der Strafsache gegen Peter Eckehardt wegen des Vergehens der üblen Nachrede nach § 111 Abs 1 StGB und einer weiteren strafbaren Handlung, über die von der Generalprokuratur gegen den Beschluss des Bezirksgerichts Steyr vom 7. Mai 2013, GZ 5 U 44/12h-39, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Dr. Janda, sowie des Angeklagten zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Steyr` | `Bezirksgerichts Steyr` |

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
- `Mag. Beran` (person)
- `Peter Eckehardt` (person)
- `Dr. Janda` (person)

**Example 90** (doc_id: `deanon_260716_TRAIN/15Os107_16y`) (sent_id: `deanon_260716_TRAIN/15Os107_16y_4`)


Der Beschluss des Bezirksgerichts Steyr vom 7. Mai 2013, GZ 5 U 44/12h-39, verletzt I. in seinem Punkt 1./ § 393 Abs 2 erster Satz iVm Abs 4 StPO und II. in seinem Punkt 2./ § 390 Abs 1 zweiter Satz iVm § 381 Abs 1 StPO.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Steyr` | `Bezirksgerichts Steyr` |

**Example 91** (doc_id: `deanon_260716_TRAIN/15Os107_16y`) (sent_id: `deanon_260716_TRAIN/15Os107_16y_5`)


Text Gründe: In der Strafsache gegen Peter Ellsäßer wegen des Vergehens der üblen Nachrede nach § 111 Abs 1 StGB und einer weiteren strafbaren Handlung, AZ 5 U 44/12h des Bezirksgerichts Steyr, stellte der Einzelrichter des Bezirksgerichts das aufgrund einer von Martin Bartelme erhobenen Privatanklage geführte Verfahren mit – am 30. April 2013 in Rechtskraft erwachsenem (ON 38) – Beschluss vom 27. März 2013 (ON 32) gemäß § 71 Abs 6 StPO ein und verpflichtete den Privatankläger gemäß § 390 Abs 1 zweiter Satz StPO zum Ersatz der Kosten des Verfahrens.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Steyr` | `Bezirksgerichts Steyr` |

**Missed by this rule (FN):**

- `Peter Ellsäßer` (person)
- `Martin Bartelme` (person)

**Example 92** (doc_id: `deanon_260716_TRAIN/15Os107_16y`) (sent_id: `deanon_260716_TRAIN/15Os107_16y_7`)


Mit unangefochten in Rechtskraft erwachsenem Beschluss vom 7. Mai 2013 (ON 39) bestimmte das Bezirksgericht Steyr die vom Privatankläger zu ersetzenden „Kosten der Vertretung des Privatangeklagten“ – nämlich für eine Intervention beim Bezirksgericht Steyr, für die Teilnahme an der Hauptverhandlung und für den Kostenbestimmungsantrag unter gleichzeitiger Abweisung des Mehrbegehrens – (aufgrund eines Rechenfehlers statt mit 544,44 Euro) mit 342,08 Euro (1./) sowie vom Angeklagten für sein Erscheinen vor Gericht geltend gemachte (Fahrt-)Kosten (ON 32a S 2) mit 15,40 Euro (2./).

| Predicted | Gold |
|---|---|
| `Bezirksgericht Steyr` | `Bezirksgericht Steyr` |
| `Bezirksgericht Steyr` | `Bezirksgericht Steyr` |

**Example 93** (doc_id: `deanon_260716_TRAIN/15Os107_16y`) (sent_id: `deanon_260716_TRAIN/15Os107_16y_8`)


Über Antrag des Verfahrenshilfeverteidigers berichtigte das Bezirksgericht Steyr mit Beschluss vom 4. November 2015 (ON 44) den „Rechnungsendbetrag“ zu 1./ (als offenkundigen Rechenfehler) auf 544,44 Euro.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Steyr` | `Bezirksgericht Steyr` |

**Example 94** (doc_id: `deanon_260716_TRAIN/15Os107_16y`) (sent_id: `deanon_260716_TRAIN/15Os107_16y_10`)


Rechtliche Beurteilung Der Beschluss des Bezirksgerichts Steyr vom 7. Mai 2013 (ON 39) steht – wie die Generalprokuratur in ihrer Nichtigkeitsbeschwerde zur Wahrung des Gesetzes zutreffend aufzeigt – mit dem Gesetz nicht in Einklang: Gemäß § 390 Abs 1 zweiter Satz StPO ist – soweit hier von Relevanz – der Privatankläger im Fall eines Einstellungsbeschlusses nach § 71 Abs 6 StPO zum Ersatz aller infolge seines Einschreitens aufgelaufenen Kosten – worunter (nur) alle in § 381 Abs 1 StPO aufgelisteten Kosten des Strafverfahrens zu verstehen sind – zu verpflichten.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Steyr` | `Bezirksgerichts Steyr` |

**Example 95** (doc_id: `deanon_260716_TRAIN/15Os97_10v`) (sent_id: `deanon_260716_TRAIN/15Os97_10v_3`)


Kopf Der Oberste Gerichtshof hat am 11. August 2010 durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Schmucker als Vorsitzende sowie durch die Hofräte des Obersten Gerichtshofs Dr. Danek, Dr. T. Solé und Mag. Lendl sowie durch die Hofrätin des Obersten Gerichtshofs Dr. Bachner-Foregger in Gegenwart des Richteramtsanwärters Mag. Mechtler als Schriftführer in der Strafsache gegen Andreas Gudszenties wegen des Vergehens der Körperverletzung nach § 83 Abs 1 StGB, AZ 7 U 49/08s des Bezirksgerichts Innsbruck, über die von der Generalprokuratur erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes gegen die Unterlassung der Verständigung des Vollzugsgerichts von der Verlängerung der Probezeit nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Holzleithner, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Innsbruck` | `Bezirksgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schmucker` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Danek` (person)
- `Dr. T. Solé` (person)
- `Mag. Lendl` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Mechtler` (person)
- `Andreas Gudszenties` (person)
- `Mag. Holzleithner` (person)

**Example 96** (doc_id: `deanon_260716_TRAIN/15Os97_10v`) (sent_id: `deanon_260716_TRAIN/15Os97_10v_4`)


Im Verfahren AZ 7 U 49/08s des Bezirksgerichts Innsbruck verletzt der Vorgang, dass es das Gericht unterließ, von seinem gemeinsam mit dem Urteil vom 4. August 2009 (unter Absehen vom Widerruf der Andreas Garthoff im Verfahren AZ 23 BE 29/06a des Landesgerichts Innsbruck gemäß § 46 Abs 2 StGB gewährten bedingten Entlassung) gefassten Beschluss auf Verlängerung der Probezeit unverzüglich dieses Landesgericht als Vollzugsgericht zu verständigen, § 494a Abs 7 StPO.

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Innsbruck` | `Bezirksgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Andreas Garthoff` (person)
- `Landesgerichts Innsbruck` (organisation)

**Example 97** (doc_id: `deanon_260716_TRAIN/15Os97_10v`) (sent_id: `deanon_260716_TRAIN/15Os97_10v_6`)


Mit - auch Freisprüche enthaltendem - Urteil des Bezirksgerichts Innsbruck vom 4. August 2009, GZ 7 U 49/08s-20, wurde Andreas Großjann des (während der Probezeit begangenen) Vergehens der Körperverletzung nach § 83 Abs 1 StGB schuldig erkannt und zu einer Freiheitsstrafe von sechs Wochen verurteilt. Zugleich fasste die Bezirksrichterin den Beschluss, vom Widerruf der im Verfahren AZ 23 BE 29/06a des Landesgerichts Innsbruck gewährten bedingten Entlassung abzusehen und die Probezeit auf fünf Jahre zu verlängern (§ 494a Abs 1 Z 2, Abs 6 StPO; s S 4 in ON 18 bzw US 4).

| Predicted | Gold |
|---|---|
| `Bezirksgerichts Innsbruck` | `Bezirksgerichts Innsbruck` |

**Missed by this rule (FN):**

- `Andreas Großjann` (person)
- `Landesgerichts Innsbruck` (organisation)

**Example 98** (doc_id: `deanon_260716_TRAIN/15Os97_10v`) (sent_id: `deanon_260716_TRAIN/15Os97_10v_13`)


Rechtliche Beurteilung Wie die Generalprokuratur in ihrer zur Wahrung des Gesetzes erhobenen Nichtigkeitsbeschwerde zutreffend ausführt, verletzt der Vorgang, dass es das Bezirksgericht Innsbruck unterließ, von seinem gemeinsam mit dem Urteil vom 4. August 2009 (unter Absehen vom Widerruf der Andreas Gaisert im Verfahren AZ 23 BE29/06a des Landesgerichts Innsbruck gewährten bedingten Entlassung) gefassten Beschluss auf Verlängerung der Probezeit unverzüglich das Vollzugsgericht in Kenntnis zu setzen, § 494a Abs 7 StPO, wonach das erkennende Gericht all jene Gerichte unverzüglich zu verständigen hat, deren Vorentscheidungen von einer Entscheidung nach § 494a Abs 1 und 6 StPO betroffen sind.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Innsbruck` | `Bezirksgericht Innsbruck` |

**Missed by this rule (FN):**

- `Andreas Gaisert` (person)
- `Landesgerichts Innsbruck` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_26`)


Weiters habe sie der Klägerin Zinsen und Prozesskosten, zu deren Zahlung sie im Verfahren vor dem Bezirksgericht Bezirksgericht Hall (in Tirol) verurteilt worden war, sowie die Kosten deren eigener Vertretung in diesem Verfahren zu ersetzen.

**False Positives:**

- `Bezirksgericht Hall` — partial — pred is substring of gold: `Bezirksgericht Hall (in Tirol)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Hall (in Tirol)`(organisation)

</details>

---

## `Hyphenated_Ampersand_Corporate_Name` 🏆

**F1:** 0.014 | **Precision:** 0.935 | **Recall:** 0.007  

**Format:** `regex`  
**Rule ID:** `5952d33c`  
**Description:**
Matches corporate names where the name and suffix are connected by hyphens, plus signs, or ampersands without spaces (e.g., 'Kallenbach+Knackmuss Elektro GmbH', 'Höllerling&Voegtlin Logistik GmbH', 'See-Telekom Gruppe GmbH').

**Content:**
```
(?<![\w])([A-Z][a-zA-Z]+(?:-[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\+[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s*&\s*[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s+&\s*[A-Z][a-zA-Z]+)+)\s+(?:GmbH|AG|Aktiengesellschaft|Gesellschaft\s+mbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.935 | 0.007 | 0.014 | 31 | 29 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 29 | 2 | 3912 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc28_14w`) (sent_id: `deanon_260716_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Ober-Automotive GmbH, Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei Katharina Rothschadl, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Ober-Automotive GmbH` | `Ober-Automotive GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Fellinger` (person)
- `Dr. Hoch` (person)
- `Gasteiner Alpenstraße 18, 9133 Blasnitzenberg, Österreich` (address)
- `Mag. Alexander Rimser` (person)
- `Katharina Rothschadl` (person)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_9`)


Er trat deswegen im Mai 2018 an die Klägerin heran, um eine Regelung seiner „persönlichen Haftungen“ über „rund 500.000 EUR“ aus der „Bürgschaft Norallex-Heizung GmbH“ zu erreichen.

| Predicted | Gold |
|---|---|
| `Norallex-Heizung GmbH` | `Norallex-Heizung GmbH` |

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Drau-Pharma GmbH` | `Drau-Pharma GmbH` |

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
- `Strazzegasse 12, 8762 Oberzeiring, Österreich` (address)
- `Mag. Johannes Bügler` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_6`)


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

**Example 4** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__4`)


In der Medienrechtssache des Antragstellers Univ.-Prof.in Laurin Schramm gegen die Antragsgegnerin CDL Luftfahrt GmbH wegen § 6 Abs 1 und § 8a Abs 6 MedienG, AZ 91 Hv 49/17t des Landesgerichts für Strafsachen Wien, verletzen die Urteile 1./ dieses Gerichts vom 26. März 2018 (ON 65) in seinem Punkt III./, womit der Antrag des Antragstellers, der Antragsgegnerin Drau-IT GmbH auch für die am 4. Juni 2017 auf dem Facebook-Account von www.

| Predicted | Gold |
|---|---|
| `Drau-IT GmbH` | `Drau-IT GmbH` |

**Missed by this rule (FN):**

- `Univ.-Prof.in Laurin Schramm` (person)
- `CDL Luftfahrt GmbH` (organisation)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/17Ob10_19y`) (sent_id: `deanon_260716_TRAIN/17Ob10_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende und die Hofräte Dr. Musger und Priv.-Doz. Dr. Rassi, die Hofrätin Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Dr. Joshua Reupold, als Masseverwalter über das Vermögen der Wald-Versand Gesellschaft mbH, Kugelmannplatz 4, 5121 Döstling, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, gegen die beklagten Parteien 1. Johanna Baldczus, und 2. MedR Nadja Grela, beide vertreten durch Schöpf & Maurer, Rechtsanwalt in Salzburg, wegen 59.028,60 EUR sA, aus Anlass der außerordentlichen Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. April 2019, GZ 1 R 161/18d-52, mit dem das Urteil des Landesgerichts Salzburg vom 30. August 2018, GZ 57 Cg 10/17z-43, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das angefochtene Urteil wird, soweit es die Abweisung des Teilbegehens, die beklagten Parteien seien zur ungeteilten Hand schuldig, der klagenden Partei 18.168,21 EUR samt 4 % Zinsen seit 15.

| Predicted | Gold |
|---|---|
| `Wald-Versand Gesellschaft mbH` | `Wald-Versand Gesellschaft mbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Dr. Musger` (person)
- `Priv.-Doz. Dr. Rassi` (person)
- `Dr. Kodek` (person)
- `Dr. Stefula` (person)
- `Dr. Joshua Reupold` (person)
- `Kugelmannplatz 4, 5121 Döstling, Österreich` (address)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` (organisation)
- `Johanna Baldczus` (person)
- `MedR Nadja Grela` (person)
- `Maurer` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Salzburg` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/17Ob10_20z`) (sent_id: `deanon_260716_TRAIN/17Ob10_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätinnen Mag. Malesich und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Pascal Alsweh, vertreten durch Stephan Briem Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Dr. Simone Pittruff als Treuhänder der Insolvenzgläubiger der Unter-Analyse Aktiengesellschaft, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH in Linz, wegen Feststellung (Streitwert 18.335,66 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. März 2020, GZ 1 R 31/20i-13, womit das Urteil des Landesgerichts Linz vom 9. Dezember 2019, GZ 4 Cg 73/18z-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Unter-Analyse Aktiengesellschaft` | `Unter-Analyse Aktiengesellschaft` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Dr. Musger` (person)
- `Mag. Malesich` (person)
- `Dr. Kodek` (person)
- `Dr. Stefula` (person)
- `Pascal Alsweh` (person)
- `Stephan Briem Rechtsanwalt GmbH` (organisation)
- `Dr. Simone Pittruff` (person)
- `Shamiyeh & Reiser Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Linz` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/17Ob10_20z`) (sent_id: `deanon_260716_TRAIN/17Ob10_20z_5`)


Text Begründung: Die Nortal-Energie Aktiengesellschaft (im Folgenden: Schuldnerin) betrieb einen Ferienclub.

| Predicted | Gold |
|---|---|
| `Nortal-Energie Aktiengesellschaft` | `Nortal-Energie Aktiengesellschaft` |

**Example 8** (doc_id: `deanon_260716_TRAIN/2Ob115_10s`) (sent_id: `deanon_260716_TRAIN/2Ob115_10s_4`)


Uniber-Verlag AG, Jedretsberg 24, 4190 Brunnwald, Österreich, und 2. Fenuni AG, Wildschönauerstraße, Oberau 3, 8444 Reith, Österreich, beide vertreten durch die Liebenwein Rechtsanwälte GmbH in Wien, gegen die beklagten und widerklagenden Parteien 1.

| Predicted | Gold |
|---|---|
| `Uniber-Verlag AG` | `Uniber-Verlag AG` |

**Missed by this rule (FN):**

- `Jedretsberg 24, 4190 Brunnwald, Österreich` (address)
- `Fenuni AG` (organisation)
- `Wildschönauerstraße, Oberau 3, 8444 Reith, Österreich` (address)
- `Liebenwein Rechtsanwälte GmbH` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/3Ob209_21p`) (sent_id: `deanon_260716_TRAIN/3Ob209_21p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei APHU Solar GmbH & Co KG, Hochkreuth 39, 8144 Bischofegg, Österreich, vertreten durch DDr. Heinz Dietmar Schimanko, Rechtsanwalt in Wien, gegen die beklagte Partei Traun-Transport GmbH, Stauderstraße 30, 8200 Pircha, Österreich, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH & Co KG in Wien, wegen 7.906,82 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 7. Juni 2021, GZ 38 R 66/21v-16, mit dem das Urteil des Bezirksgerichts Favoriten vom 19. Jänner 2021, GZ 3 C 503/20f-12, abgeändert wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Traun-Transport GmbH` | `Traun-Transport GmbH` |

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
- `Stauderstraße 30, 8200 Pircha, Österreich` (address)
- `Bichler Zrzavy Rechtsanwälte GmbH & Co KG` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/3Ob99_10w`) (sent_id: `deanon_260716_TRAIN/3Ob99_10w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Senatspräsidenten Hon.-Prof. Dr. Sailer, den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und den Hofrat Dr. Jensik als weitere Richter in der Rechtssache der klagenden Partei Dr. Johannes Müller, Rechtsanwalt, Wien 3, Ditscheinergasse 2, als Masseverwalter im Konkurs der Wald-Event GmbH, gegen die beklagte Partei Wiener Gebietskrankenkasse, Wien 10, Wienerbergstraße 15-19, vertreten durch Preslmayr Rechtsanwälte OG in Wien, und der Nebenintervenienten auf der Seite der beklagten Partei 1.)

| Predicted | Gold |
|---|---|
| `Wald-Event GmbH` | `Wald-Event GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Prückner` (person)
- `Hon.-Prof. Dr. Sailer` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Lovrek` (person)
- `Dr. Jensik` (person)
- `Dr. Johannes Müller` (person)
- `Wiener Gebietskrankenkasse` (organisation)
- `Preslmayr Rechtsanwälte OG` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/4Nc3_12x`) (sent_id: `deanon_260716_TRAIN/4Nc3_12x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel und Dr. Jensik als weitere Richter in der beim Landesgericht Innsbruck zu AZ 59 Cg 92/11x anhängigen Rechtssache der klagenden Partei Kelkel-Versicherung GmbH, Walkersdorf 16, 9761 Tröbelsberg, Österreich, vertreten durch Mag. Heinz Heher, Rechtsanwalt in Wien, gegen die beklagte Partei Zorzorzor GmbH, Großenbergstraße 43, 8561 Neudorf bei Sankt Johann ob Hohenburg, Österreich, vertreten durch Dr. Adrian Hollaender, Rechtsanwalt in Innsbruck, wegen Unterlassung, Urteilsveröffentlichung und 67.606 EUR sA, über die Delegierungsanträge der beklagten Partei gemäß § 31 Abs 2 JN, folgenden Beschluss gefasst:  Spruch Die Anträge der beklagten Partei, die Rechtssache an das „Landesgericht Wien“ bzw Handelsgericht Wien zu delegieren, werden abgewiesen.

| Predicted | Gold |
|---|---|
| `Kelkel-Versicherung GmbH` | `Kelkel-Versicherung GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schenk` (person)
- `Dr. Vogel` (person)
- `Dr. Jensik` (person)
- `Landesgericht Innsbruck` (organisation)
- `Walkersdorf 16, 9761 Tröbelsberg, Österreich` (address)
- `Mag. Heinz Heher` (person)
- `Zorzorzor GmbH` (organisation)
- `Großenbergstraße 43, 8561 Neudorf bei Sankt Johann ob Hohenburg, Österreich` (address)
- `Dr. Adrian Hollaender` (person)
- `Landesgericht Wien` (organisation)
- `Handelsgericht Wien` (organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/4Ob26_20g`) (sent_id: `deanon_260716_TRAIN/4Ob26_20g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Vogel als Vorsitzenden und die Hofräte Dr. Schwarzenbacher, Hon.-Prof. Dr. Brenn, Priv.-Doz. Dr. Rassi und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Xenia Pintar GmbH, Alfred Leiner-Straße 15, 8674 Grubbauer, Österreich, vertreten durch Rechtsanwaltskanzlei Dr. Wendling GmbH in Kitzbühel, gegen die beklagte Partei Sudwil-Umwelt GmbH, Pleschberg 7, 9872 Gössering, Österreich, Deutschland, vertreten durch Dr. Dan Katzlinger, Rechtsanwalt in Innsbruck, wegen 70.000 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. Dezember 2019, GZ 10 R 49/19k-32, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Sudwil-Umwelt GmbH` | `Sudwil-Umwelt GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Vogel` (person)
- `Dr. Schwarzenbacher` (person)
- `Hon.-Prof. Dr. Brenn` (person)
- `Priv.-Doz. Dr. Rassi` (person)
- `MMag. Matzka` (person)
- `Xenia Pintar` (person)
- `Alfred Leiner-Straße 15, 8674 Grubbauer, Österreich` (address)
- `Dr. Wendling GmbH` (organisation)
- `Pleschberg 7, 9872 Gössering, Österreich` (address)
- `Dr. Dan Katzlinger` (person)
- `Oberlandesgerichts Innsbruck` (organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/6Ob169_12i`) (sent_id: `deanon_260716_TRAIN/6Ob169_12i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Pimmer als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Dr. Schramm, Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Seesteincon-Transport GmbH, Wildbacher Straße 174, 3623 Bernhards, Österreich, vertreten durch List Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Heimnor GmbH, Am Johannisgraben 44, 8200 Albersdorf, Österreich, vertreten durch Dr. Christoph Brenner - Mag. Severin Perschl Rechtsanwälte OG in Krems, wegen 7.641,30 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Korneuburg als Berufungsgericht vom 16. Februar 2012, GZ 21 R 262/11v-50, womit das Urteil des Bezirksgerichts Gänserndorf vom 2. August 2011, GZ 12 C 1036/10h-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Seesteincon-Transport GmbH` | `Seesteincon-Transport GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Pimmer` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schramm` (person)
- `Dr. Gitschthaler` (person)
- `Univ.-Prof. Dr. Kodek` (person)
- `Dr. Nowotny` (person)
- `Wildbacher Straße 174, 3623 Bernhards, Österreich` (address)
- `List Rechtsanwälte GmbH` (organisation)
- `Heimnor GmbH` (organisation)
- `Am Johannisgraben 44, 8200 Albersdorf, Österreich` (address)
- `Dr. Christoph Brenner` (person)
- `Mag. Severin Perschl Rechtsanwälte OG` (organisation)
- `Landesgerichts Korneuburg` (organisation)
- `Bezirksgerichts Gänserndorf` (organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/6Ob231_24z`) (sent_id: `deanon_260716_TRAIN/6Ob231_24z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Hofer-Zeni-Rennhofer als Vorsitzende sowie die Hofrätinnen und Hofräte Hon.-Prof. Dr. Faber, Mag. Pertmayr, Dr. Weber und Mag. Nigl LL.M. als weitere Richter in der Rechtssache der klagenden Partei Ing. Tiffany Jähncke, vertreten durch Poduschka Partner Anwaltsgesellschaft mbH in Linz, wider die beklagte Partei Sudconbach-Bau AG, Hart, Akazienstraße 15v, 4064 Oftering, Österreich, Deutschland, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 9.600 EUR sA, im Verfahren über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Linz als Berufungsgericht vom 7. Oktober 2024, GZ 6 R 57/24b-31, womit das Urteil des Bezirksgerichts Traun vom 16. Februar 2024, GZ 2 C 198/23z-22, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei vom 9. Dezember 2025 auf Fortsetzung des Verfahrens wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Sudconbach-Bau AG` | `Sudconbach-Bau AG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Hon.-Prof. Dr. Faber` (person)
- `Mag. Pertmayr` (person)
- `Dr. Weber` (person)
- `Mag. Nigl` (person)
- `Ing. Tiffany Jähncke` (person)
- `Poduschka Partner Anwaltsgesellschaft mbH` (organisation)
- `Hart, Akazienstraße 15v, 4064 Oftering, Österreich` (address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Linz` (organisation)
- `Bezirksgerichts Traun` (organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_7`)


9. 2003 ist im Firmenbuch des Handelsgerichts Wien zu FN FN230079f die Werksteinfurt-Immobilien GmbH (im Folgenden: „Gesellschaft“) eingetragen.

| Predicted | Gold |
|---|---|
| `Werksteinfurt-Immobilien GmbH` | `Werksteinfurt-Immobilien GmbH` |

**Missed by this rule (FN):**

- `Handelsgerichts Wien` (organisation)
- `FN230079f` (business_register_number)

**Example 16** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_25`)


[7] Am 3. 3. 2020 beantragte derÖsterreichische Verband Gemeinnütziger Bauvereinigungen – Revisionsverband(in der Folge „Revisionsverband“) im Firmenbuch des Erstgerichts bei der Gesellschaft die Löschung der derzeit eingetragenen Gesellschafter und die Wiedereintragung der ursprünglichen Gesellschafter Dr. Natalie Taubmann mit einer voll eingezahlten Stammeinlage von 22.400 EUR und Gartwald-Handel GmbH mit einer voll eingezahlten Stammeinlage von 12.600 EUR.

| Predicted | Gold |
|---|---|
| `Gartwald-Handel GmbH` | `Gartwald-Handel GmbH` |

**Missed by this rule (FN):**

- `Dr. Natalie Taubmann` (person)

**Example 17** (doc_id: `deanon_260716_TRAIN/6Ob240_20t`) (sent_id: `deanon_260716_TRAIN/6Ob240_20t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie durch die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Firmenbuchsache der zu FN FN103376a beim Landesgericht Landesgericht Krems an der Donau eingetragenen Taltalgart-Gastronomie GmbH mit Sitz in der politischen Gemeinde Landesgericht Salzburg, über den Revisionsrekurs der Telekom Mongart gesellschaft mbH, Franz-Martin-Straße 1, 9161 Ehrensdorf, Österreich, vertreten durch Dr. Robert Mogy, Rechtsanwalt in Klagenfurt, gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. Oktober 2020, GZ 4 R 153/20g-8, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen (§ 71 Abs 3 AußStrG iVm § 15 Abs 2 FBG).

| Predicted | Gold |
|---|---|
| `Taltalgart-Gastronomie GmbH` | `Taltalgart-Gastronomie GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schramm` (person)
- `Hon.-Prof. Dr. Gitschthaler` (person)
- `Univ.-Prof. Dr. Kodek` (person)
- `Dr. Nowotny` (person)
- `Dr. Faber` (person)
- `FN103376a` (business_register_number)
- `Landesgericht Krems an der Donau` (organisation)
- `Landesgericht Salzburg` (organisation)
- `Telekom Mongart gesellschaft mbH` (organisation)
- `Franz-Martin-Straße 1, 9161 Ehrensdorf, Österreich` (address)
- `Dr. Robert Mogy` (person)
- `Oberlandesgerichts Graz` (organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/6Ob56_19g`) (sent_id: `deanon_260716_TRAIN/6Ob56_19g_16`)


Diese Partner sind: AGN Automotive Holding GmbH, Stadt Monmon gmbh, Fenwerk-Automotive GmbH oder die Verwendung sinngleicher Klauseln zuunterlassen;

| Predicted | Gold |
|---|---|
| `Fenwerk-Automotive GmbH` | `Fenwerk-Automotive GmbH` |

**Missed by this rule (FN):**

- `AGN Automotive Holding GmbH` (organisation)
- `Stadt Monmon gmbh` (organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/6Ob56_19g`) (sent_id: `deanon_260716_TRAIN/6Ob56_19g_350`)


Diese Partner sind: Wilheim-Pflege GmbH, Leubert+Krennbauer Bau gmbh, Nexglanz GmbH.

| Predicted | Gold |
|---|---|
| `Wilheim-Pflege GmbH` | `Wilheim-Pflege GmbH` |

**Missed by this rule (FN):**

- `Leubert+Krennbauer Bau gmbh` (organisation)
- `Nexglanz GmbH.` (organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/7Ob172_21a`) (sent_id: `deanon_260716_TRAIN/7Ob172_21a_6`)


Text Entscheidungsgründe: [1] Zwischen der Sudwil-Lebensmittel GmbH (in Hinkunft: Versicherungsnehmerin) und der Beklagten besteht ein Rechtsschutzversicherungsvertrag, der auch den Rechtsschutz für den Privatbereich des Betriebsinhabers umfasst.

| Predicted | Gold |
|---|---|
| `Sudwil-Lebensmittel GmbH` | `Sudwil-Lebensmittel GmbH` |

**Example 21** (doc_id: `deanon_260716_TRAIN/7Ob48_17k`) (sent_id: `deanon_260716_TRAIN/7Ob48_17k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und durch die Hofrätinnen und Hofräte Dr. Höllwerth, Dr. E. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Seetal Consulting GmbH, Diakoniestraße 19, 3251 Ameishaufen, Österreich, vertreten durch Aigner Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Rhein-Landwirtschaft AG, Starfach-Hohe Wand Weg 97, 3386 Würmling, Österreich, vertreten durch Dr. Josef Milchram, Dr. Anton Ehm und Mag. Thomas Mödlagl, Rechtsanwälte in Wien, wegen 1.373.171,48 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 20. Jänner 2017, GZ 1 R 160/16d-52, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Rhein-Landwirtschaft AG` | `Rhein-Landwirtschaft AG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Dr. Höllwerth` (person)
- `Dr. E. Solé` (person)
- `Mag. Malesich` (person)
- `MMag. Matzka` (person)
- `Seetal Consulting GmbH` (organisation)
- `Diakoniestraße 19, 3251 Ameishaufen, Österreich` (address)
- `Aigner Rechtsanwalts GmbH` (organisation)
- `Starfach-Hohe Wand Weg 97, 3386 Würmling, Österreich` (address)
- `Dr. Josef Milchram` (person)
- `Dr. Anton Ehm` (person)
- `Mag. Thomas Mödlagl` (person)
- `Oberlandesgerichts Linz` (organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/7Ob6_20p`) (sent_id: `deanon_260716_TRAIN/7Ob6_20p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Ing. Roderich Florczyk, vertreten durch Dr. Norbert Nowak, Rechtsanwalt in Wien, gegen die beklagte Partei Mittel-Energie AG, Gaunitzhof 8, 4632 Breitwies, Österreich, vertreten durch die Schönherr Rechtsanwälte GmbH in Wien, wegen 6.342,73 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 8. November 2018, GZ 60 R 98/18v-12, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 15. Juni 2018, GZ 18 C 109/18p-8, abgeändert wurde, beschlossen und zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Mittel-Energie AG` | `Mittel-Energie AG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Hon.-Prof. Dr. Höllwerth` (person)
- `Dr. Solé` (person)
- `Mag. Malesich` (person)
- `MMag. Matzka` (person)
- `Ing. Roderich Florczyk` (person)
- `Dr. Norbert Nowak` (person)
- `Gaunitzhof 8, 4632 Breitwies, Österreich` (address)
- `Schönherr Rechtsanwälte GmbH` (organisation)
- `Handelsgerichts Wien` (organisation)
- `Bezirksgerichts für Handelssachen Wien` (organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/8ObA71_14w`) (sent_id: `deanon_260716_TRAIN/8ObA71_14w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden und durch die Hofrätin Dr. Tarmann-Prentner, den Hofrat Mag. Ziegelbauer, sowie die fachkundigen Laienrichter Mag. Andreas Mörk und Mag. Matthias Schachner als weitere Richter in der Arbeitsrechtssache der klagenden Partei Cynthia Schamel, vertreten durch Forcher-Mayr & Kantner Rechtsanwälte Partnerschaft in Innsbruck, gegen die beklagte Partei Werkglanz-Verlag AG, Blattbühel 46, 9073 Klagenfurt, Österreich, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Feststellung (Streitwert: 21.800 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 30. September 2014, GZ 15 Ra 92/14p-40, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Werkglanz-Verlag AG` | `Werkglanz-Verlag AG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Prof. Dr. Spenling` (person)
- `Dr. Tarmann-Prentner` (person)
- `Mag. Ziegelbauer` (person)
- `Mag. Andreas Mörk` (person)
- `Mag. Matthias Schachner` (person)
- `Cynthia Schamel` (person)
- `Forcher-Mayr & Kantner Rechtsanwälte Partnerschaft` (organisation)
- `Blattbühel 46, 9073 Klagenfurt, Österreich` (address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Innsbruck` (organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/8ObA82_11h`) (sent_id: `deanon_260716_TRAIN/8ObA82_11h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner sowie die fachkundigen Laienrichter Dr. Günter Steinlechner und Harald Kohlruss als weitere Richter in der Arbeitsrechtssache der klagenden Partei Dr. Xenia Hegedusic, vertreten durch Mag. Priska Seeber, Rechtsanwältin in Innsbruck, gegen die beklagte Partei Sudtralem-Event GmbH, Mayrwiesstraße 6, 5400 Bad Dürrnberg, Österreich, vertreten durch Dr. Harald Vill Dr. Helfried Penz und Mag. Christoph Rupp, Rechtsanwälte in Innsbruck, wegen 20.871,93 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2011, GZ 15 Ra 75/11h-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Sudtralem-Event GmbH` | `Sudtralem-Event GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Spenling` (person)
- `Hon.-Prof. Dr. Kuras` (person)
- `Dr. Tarmann-Prentner` (person)
- `Dr. Günter Steinlechner` (person)
- `Harald Kohlruss` (person)
- `Dr. Xenia Hegedusic` (person)
- `Mag. Priska Seeber` (person)
- `Mayrwiesstraße 6, 5400 Bad Dürrnberg, Österreich` (address)
- `Dr. Harald Vill` (person)
- `Dr. Helfried Penz` (person)
- `Mag. Christoph Rupp` (person)
- `Oberlandesgerichts Innsbruck` (organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/8ObS12_19a`) (sent_id: `deanon_260716_TRAIN/8ObS12_19a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Wessely-Kristöfel als weitere Richter sowie die fachkundigen Laienrichter Mag. Thomas Stegmüller (aus dem Kreis der Arbeitgeber) und Gerald Fida (aus dem Kreis der Arbeitnehmer) in der Sozialrechtssache der klagenden Partei Miranda Tönnesmann, vertreten durch Dr. Christoph Orgler, Rechtsanwalt in Graz, gegen die beklagte Partei IEF-Service GmbH, Geschäftsstelle Graz, 8020 Graz, Europaplatz 12, vertreten durch die Finanzprokuratur, 1010 Wien, Singerstraße 17–19, wegen 3.159 EUR sA (Insolvenz-Entgelt), über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 12. September 2019, GZ 6 Rs 33/19y-9, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 6. Mai 2019, GZ 36 Cgs 47/19h-5, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `IEF-Service GmbH` | `IEF-Service GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Kuras` (person)
- `Dr. Tarmann-Prentner` (person)
- `Mag. Wessely-Kristöfel` (person)
- `Mag. Thomas Stegmüller` (person)
- `Gerald Fida` (person)
- `Miranda Tönnesmann` (person)
- `Dr. Christoph Orgler` (person)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/8ObS8_22t`) (sent_id: `deanon_260716_TRAIN/8ObS8_22t_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Stefula als weitere Richter (Senat gemäß § 11a Abs 3 Z 2 ASGG) in der Sozialrechtssache der klagenden Partei Dipl. Kff. Saskia Claussner, vertreten durch Dr. Herbert Marschitz und andere Rechtsanwälte in Kufstein, gegen die beklagte Partei IEF-Service GmbH, 6020 Innsbruck, Meraner Straße 1, vertreten durch die Finanzprokuratur in Wien, wegen 34.726 EUR sA (Insolvenzentgelt), über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 18. Oktober 2022, GZ 25 Rs 56/22d-34, mit dem das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 9. Juni 2022, GZ 44 Cgs 43/21m-27, samt dem ihm vorangegangenen Verfahren für nichtig erklärt und die Klage zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `IEF-Service GmbH` | `IEF-Service GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Kuras` (person)
- `Dr. Tarmann-Prentner` (person)
- `Dr. Stefula` (person)
- `Dipl. Kff. Saskia Claussner` (person)
- `Dr. Herbert Marschitz` (person)
- `Oberlandesgerichts Innsbruck` (organisation)
- `Landesgerichts Innsbruck` (organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/9Ob10_19i`) (sent_id: `deanon_260716_TRAIN/9Ob10_19i_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Dehn, Dr. Hargassner, Mag. Korn und Dr. Stefula in der Rechtssache der klagenden Partei Oneseit Garten GmbH, Stephanieweg 12, 4901 Hub, Österreich, vertreten durch Partnerschaft Schuppich Sporn & Winischhofer, Rechtsanwälte in Wien, gegen die beklagte Partei Brucknor-Planung GmbH, Tadtner Weg 4, 5133 Dick, Österreich, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, wegen 6.265 EUR sA, über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Salzburg als Berufungsgericht vom 29. November 2018, GZ 53 R 212/18k-19, mit dem der Berufung der klagenden Partei gegen das Urteil des Bezirksgerichts Salzburg vom 25. Juni 2018, GZ 17 C 965/17a-15, Folge gegeben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Brucknor-Planung GmbH` | `Brucknor-Planung GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Dehn` (person)
- `Dr. Hargassner` (person)
- `Mag. Korn` (person)
- `Dr. Stefula` (person)
- `Oneseit Garten GmbH` (organisation)
- `Stephanieweg 12, 4901 Hub, Österreich` (address)
- `Partnerschaft Schuppich Sporn & Winischhofer, Rechtsanwälte` (organisation)
- `Tadtner Weg 4, 5133 Dick, Österreich` (address)
- `Vavrovsky Heine Marth Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Salzburg` (organisation)
- `Bezirksgerichts Salzburg` (organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/9ObA118_18w`) (sent_id: `deanon_260716_TRAIN/9ObA118_18w_4`)


Gabriele Svirak in der Arbeitsrechtssache der klagenden Partei Gertrude Kovacik, vertreten durch Dr. Gerhard Hiebler, Dr. Gerd Grebenjak, Rechtsanwälte in Leoben, gegen die beklagte Partei Hoch-Handel GmbH, Sollach 7, 6671 Gaicht, Österreich, vertreten durch Dr. Helmut Fetz, Dr. Birgit Fetz ua, Rechtsanwälte in Leoben, wegen 500 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. August 2018, GZ 7 Ra 23/18h-12, mit dem der Berufung der klagenden Partei gegen das Urteil des Landesgerichts Leoben als Arbeits- und Sozialgericht vom 14. Dezember 2017, GZ 23 Cga 75/17x-7, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision der klagenden Partei wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hoch-Handel GmbH` | `Hoch-Handel GmbH` |

**Missed by this rule (FN):**

- `Gabriele Svirak` (person)
- `Gertrude Kovacik` (person)
- `Dr. Gerhard Hiebler` (person)
- `Dr. Gerd Grebenjak` (person)
- `Sollach 7, 6671 Gaicht, Österreich` (address)
- `Dr. Helmut Fetz` (person)
- `Dr. Birgit Fetz` (person)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts Leoben` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_3`)


Kopf Der Oberste Gerichtshof hat am 11. Dezember 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Mag. Fürnkranz und Dr. Mann in Gegenwart des Schriftführers Dr. Koller in der Medienrechtssache der Antragsteller Dr. Ludger Schäpan und Moses Rüßbült gegen die Antragsgegnerin Synzortal-Medien GmbH & Co KG wegen §§ 7 f MedienG, AZ 93 Hv 56/18p des Landesgerichts für Strafsachen Wien, über die von der Generalprokuratur gegen den Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 9. März 2020, AZ 18 Bs 340/19k (ON 27), erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Erste Generalanwältin Mag. Wachberger, der Vertreterin der Antragsteller Dr. Windhager und des Vertreters der Antragsgegnerin Mag. Hermetter, zu Recht erkannt:  Spruch

**False Positives:**

- `Synzortal-Medien GmbH` — partial — pred is substring of gold: `Synzortal-Medien GmbH & Co KG`

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

**Example 1** (doc_id: `deanon_260716_TRAIN/9ObA76_13m`) (sent_id: `deanon_260716_TRAIN/9ObA76_13m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras, die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner und Mag. Ernst Bassler als weitere Richter in der Arbeitsrechtssache der klagenden Partei Adrian Leiße, BSc, vertreten durch Dr. H. Burmann ua, Rechtsanwälte in Innsbruck, gegen die beklagten Parteien 1. Logkraft-Verlag GmbH & Co KG, 2.

**False Positives:**

- `Logkraft-Verlag GmbH` — partial — pred is substring of gold: `Logkraft-Verlag GmbH & Co KG`

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
- `Mag. Ernst`(person)
- `Adrian Leiße, BSc`(person)
- `Logkraft-Verlag GmbH & Co KG`(organisation)

</details>

---

## `Law_Firm_Rechtsanwaelte_OG` 🏆

**F1:** 0.018 | **Precision:** 0.720 | **Recall:** 0.009  

**Format:** `regex`  
**Rule ID:** `a5f09bd3`  
**Description:**
Matches law firms ending in 'Rechtsanwälte OG' with flexible name structures including hyphens and '&' or 'und'.

**Content:**
```
\b([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*|[A-Z][a-zA-Z]+(?:-[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\+[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s+und\s+[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s*&\s*[A-Z][a-zA-Z]+)+)\s+Rechtsanwälte\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.720 | 0.009 | 0.018 | 50 | 36 | 14 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 36 | 14 | 3959 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der beim Landesgericht Linz zu AZ 3 Cg 46/21a anhängigen Rechtssache der klagenden Partei Hollengk Planung GmbH, Am Steindl 3, 9873 Döbriach, Österreich, vertreten durch Huber Berchtold Rechtsanwälte OG in Wien, gegen die beklagte Partei Wind Nexheimval GmbH, Wiesbergsiedlung 4, 8341 Pöllau, Österreich, vertreten durch ScherbaumSeebacher Rechtsanwälte GmbH in Graz, wegen 188.117,55 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN folgenden Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, zur Verhandlung und Entscheidung der Rechtssache anstelle des Landesgerichts Linz das Landesgericht Korneuburg zu bestimmen, wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Huber Berchtold Rechtsanwälte OG` | `Huber Berchtold Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Fichtenau` (person)
- `Dr. Grohmann` (person)
- `Landesgericht Linz` (organisation)
- `Hollengk Planung GmbH` (organisation)
- `Am Steindl 3, 9873 Döbriach, Österreich` (address)
- `Wind Nexheimval GmbH` (organisation)
- `Wiesbergsiedlung 4, 8341 Pöllau, Österreich` (address)
- `ScherbaumSeebacher Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Linz` (organisation)
- `Landesgericht Korneuburg` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_4`)


Enns-Umwelt Consulting Limited, Alpineweg 221, 5730 Jochbergthurn, Österreich, 2. Ing. Lara Markart, letztere vertreten durch Radel Stampf Supper Rechtsanwälte OG in Mattersburg, wegen 160.422,79 EUR sA, infolge Revision der klagenden Partei (Revisionsinteresse 107.422,79 EUR sA) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Jänner 2015, GZ 4 R 119/14w-32, womit das Urteil des Landesgerichts St. Pölten vom 25. April 2014, GZ 37 Cg 96/13f-28, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Radel Stampf Supper Rechtsanwälte OG` | `Radel Stampf Supper Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Enns-Umwelt` (organisation)
- `Alpineweg 221, 5730 Jochbergthurn, Österreich` (address)
- `Ing. Lara Markart` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts St. Pölten` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Poinstingl & Partner Rechtsanwälte OG` | `Poinstingl & Partner Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Fellinger` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Mag. Korn` (person)
- `Langhansl+Antonewitz Chemie AG` (organisation)
- `Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich` (address)
- `Drau-Pharma GmbH` (organisation)
- `Strazzegasse 12, 8762 Oberzeiring, Österreich` (address)
- `Mag. Johannes Bügler` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/10Ob43_19z`) (sent_id: `deanon_260716_TRAIN/10Ob43_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Othmar Mertl, vertreten durch Nitsch Pajor Zöllner Rechtsanwälte OG in Mödling, gegen die beklagte Partei Stadtgemeinde Malik Fridt, vertreten durch Krist Bubits Rechtsanwälte OG in Mödling, wegen 1.) 21.216,92 EUR sA und 2.) Feststellung (Streitwert: 2.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Februar 2019, GZ 12 R 96/18b-36, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Wiener Neustadt vom 31. August 2018, GZ 20 Cg 86/17h-31, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Krist Bubits Rechtsanwälte OG` | `Krist Bubits Rechtsanwälte OG` |

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
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Roland Soukup, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mahringer Steinwender Bestebner Rechtsanwälte OG` | `Mahringer Steinwender Bestebner Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Schramm` (person)
- `Dr. Fichtenau` (person)
- `Dr. Gabriele Griehsel` (person)
- `Dr. Wolfgang Kozak` (person)
- `Roland Soukup` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Salzburg` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Dr. Florenzia Münsterer, vertreten durch Rechtsanwälte Dr. Amhof & Dr. Damian GmbH in Wien, gegen die beklagte Partei MittelEnergie Werke Bank AG, Altlassing 110, 4183 Ahorn, Österreich, vertreten durch Urbanek Lind Schmied Reisch Rechtsanwälte OG in Wien, wegen 600.090 EUR sA, über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 25. Mai 2011, GZ 15 R 64/11h-54, mit dem das Urteil des Handelsgerichts Wien vom 14. Jänner 2011, GZ 16 Cg 20/10f-50, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Urbanek Lind Schmied Reisch Rechtsanwälte OG` | `Urbanek Lind Schmied Reisch Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Dr. Grohmann` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Florenzia Münsterer` (person)
- `Rechtsanwälte Dr. Amhof & Dr. Damian GmbH` (organisation)
- `MittelEnergie Werke Bank` (organisation)
- `Altlassing 110, 4183 Ahorn, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/1Ob174_19y`) (sent_id: `deanon_260716_TRAIN/1Ob174_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Theophil Mielewzyk, vertreten durch Dr. Hannes Paulweber, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Liu Jantschar, vertreten durch die Heiss & Heiss Rechtsanwälte OG, Innsbruck, wegen 137.664,28 EUR sA sowie Feststellung (Streitwert 15.000 EUR), über die außerordentliche Revision der beklagten Partei gegen das (richtig) Teilzwischenurteil des Oberlandesgerichts Innsbruck vom 18. Juli 2019, GZ 1 R 76/19i-74, mit dem das Urteil des Landesgerichts Innsbruck vom 21. Februar 2019, GZ 8 Cg 119/16z-68, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Heiss & Heiss Rechtsanwälte OG` | `Heiss & Heiss Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Theophil Mielewzyk` (person)
- `Dr. Hannes Paulweber` (person)
- `Liu Jantschar` (person)
- `Oberlandesgerichts Innsbruck` (organisation)
- `Landesgerichts Innsbruck` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/1Ob186_12b`) (sent_id: `deanon_260716_TRAIN/1Ob186_12b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Thomas Plüm, vertreten durch Kammler & Koll Rechtsanwälte OG in Freistadt, gegen die beklagte Partei Patrick Dimpfel, vertreten durch Mag. Klaus Burgholzer, Rechtsanwalt in Linz, wegen 100.000 EUR sA und Feststellung (Streitwert: 5.000 EUR), über die außerordentliche Revision der klagenden Partei (Revisionsinteresse: 70.000 EUR sA) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. Juli 2012, GZ 2 R 79/12v-22, mit dem das Urteil des Landesgerichts Linz vom 27. Februar 2012, GZ 5 Cg 61/11d-18, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Kammler & Koll Rechtsanwälte OG` | `Kammler & Koll Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Dr. Grohmann` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Thomas Plüm` (person)
- `Patrick Dimpfel` (person)
- `Mag. Klaus Burgholzer` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Linz` (organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/1Ob192_11h`) (sent_id: `deanon_260716_TRAIN/1Ob192_11h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Hierle Sanitär Limited, London, Zirkinger Straße 3, 8082 Glatzau, Österreich, vertreten durch Thum Weinreich Schwarz Fuchsbauer Rechtsanwälte OG in St. Pölten, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 1,8 Mio EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Juni 2011, GZ 14 R 214/10h-39, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 3. September 2010, GZ 33 Cg 3/09t-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Thum Weinreich Schwarz Fuchsbauer Rechtsanwälte OG` | `Thum Weinreich Schwarz Fuchsbauer Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Dr. Grohmann` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Hierle Sanitär Limited` (organisation)
- `Zirkinger Straße 3, 8082 Glatzau, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/1Ob216_15v`) (sent_id: `deanon_260716_TRAIN/1Ob216_15v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Suleika Kranigk, vertreten durch Hon.-Prof. Dr. Michel Walter, Rechtsanwalt in Wien, gegen die beklagte Partei Kelfen Transport Solutions GmbH, Geßlgasse 35, 9911 Thal-Wilfern, Österreich, vertreten durch die Schlösser & Partner Rechtsanwälte OG, Graz, wegen 33.930 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 19. August 2015, GZ 13 R 74/15w-55, mit dem das Endurteil des Landesgerichts Korneuburg vom 26. Februar 2015, GZ 3 Cg 15/13h-50, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Partner Rechtsanwälte OG` | `Partner Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Suleika Kranigk` (person)
- `Hon.-Prof. Dr. Michel Walter` (person)
- `Kelfen Transport Solutions GmbH` (organisation)
- `Geßlgasse 35, 9911 Thal-Wilfern, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts Korneuburg` (organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/1Ob224_20b`) (sent_id: `deanon_260716_TRAIN/1Ob224_20b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache klagenden Partei Rainer Baetzel, vertreten durch Dr. Harald Hauer, Rechtsanwalt in Wien, gegen die beklagte Partei Rimscha Versand GmbH in Liquidation, Götzau 193, 5452 Grub, Österreich, vertreten durch die Petsch Frosch Klein Arturo Rechtsanwälte OG, Wien, wegen 38.236,58 EUR sA und Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Oktober 2020, GZ 3 R 51/20x-50, mit dem das Urteil des Handelsgerichts Wien vom 24. Juli 2020, GZ 34 Cg 51/18h-45, bestätigt wurde, in nicht öffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Petsch Frosch Klein Arturo Rechtsanwälte OG` | `Petsch Frosch Klein Arturo Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Rainer Baetzel` (person)
- `Dr. Harald Hauer` (person)
- `Rimscha Versand GmbH` (organisation)
- `Götzau 193, 5452 Grub, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/1Ob7_18p`) (sent_id: `deanon_260716_TRAIN/1Ob7_18p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Familienrechtssache des Antragstellers Hon.-Prof.in Linda Helmers, vertreten durch die GKP Gabl Kogler Leitner Stöglehner Bodingbauer Rechtsanwälte OG, Linz, gegen die Antragsgegnerin Ramona Borkert, vertreten durch die ANWALTGMBH Rinner Teuchtmann, Linz, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse nach den §§ 81 ff EheG, über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts Linz als Rekursgericht vom 15. November 2017, GZ 15 R 484/17b-10, mit dem der Beschluss des Bezirksgerichts Urfahr vom 28. September 2017, GZ 13 Fam 22/17v-5, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Bodingbauer Rechtsanwälte OG` | `Bodingbauer Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Sailer` (person)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Hon.-Prof.in Linda Helmers` (person)
- `Ramona Borkert` (person)
- `ANWALTGMBH Rinner Teuchtmann` (organisation)
- `Landesgerichts Linz` (organisation)
- `Bezirksgerichts Urfahr` (organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/1Ob95_21h`) (sent_id: `deanon_260716_TRAIN/1Ob95_21h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Gawelzyk Pflege GmbH, Am See IX 247, 6320 Achleit, Österreich, vertreten durch die Zumtobel Kronberger Rechtsanwälte OG, Salzburg, gegen die beklagte Partei Loos und Woiciech Analyse GmbH, Rasenweg 21, 3441 Baumgarten am Tullnerfeld, Österreich, vertreten durch die Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH, Salzburg, wegen 135.656,39 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. April 2021, GZ 2 R 39/21z-27, mit dem das Urteil des Landesgerichts Ried im Innkreis vom 27. Jänner 2021, GZ 2 Cg 24/20i-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Zumtobel Kronberger Rechtsanwälte OG` | `Zumtobel Kronberger Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Gawelzyk Pflege GmbH` (organisation)
- `Am See IX 247, 6320 Achleit, Österreich` (address)
- `Loos und Woiciech Analyse GmbH` (organisation)
- `Rasenweg 21, 3441 Baumgarten am Tullnerfeld, Österreich` (address)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Ried im Innkreis` (organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/2Ob115_10s`) (sent_id: `deanon_260716_TRAIN/2Ob115_10s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in den verbundenen Rechtssachen der klagenden und widerbeklagten Partei Schwarzig Medien Aktiengesellschaft, Balthasar-Waltl-Weg 227, 3921 Kehrbach, Österreich, vertreten durch die Kunz Schima Wallentin Rechtsanwälte OG in Wien, und der Nebenintervenientinnen auf Seiten der klagenden Partei 1.

| Predicted | Gold |
|---|---|
| `Kunz Schima Wallentin Rechtsanwälte OG` | `Kunz Schima Wallentin Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Baumann` (person)
- `Dr. Veith` (person)
- `Dr. E. Solé` (person)
- `Dr. Schwarzenbacher` (person)
- `Dr. Nowotny` (person)
- `Schwarzig Medien Aktiengesellschaft` (organisation)
- `Balthasar-Waltl-Weg 227, 3921 Kehrbach, Österreich` (address)

**Example 14** (doc_id: `deanon_260716_TRAIN/2Ob86_12d`) (sent_id: `deanon_260716_TRAIN/2Ob86_12d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Erika Huwold, vertreten durch Gruböck & Lentschig Rechtsanwälte OG in Baden, wider die beklagte Partei „ MedR Dr.in Sara Stehlig “ Arnold Schleicherdt, vertreten durch Themmer, Toth & Partner Rechtsanwälte OG in Wien, wegen 144.329,55 EUR sA (Revisionsinteresse 54.717 EUR sA), infolge der außerordentlichen Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Februar 2012, GZ 4 R 598/11g-25, den Beschluss gefasst:  Spruch Das Revisionsverfahren wird bis zur rechtskräftigen Erledigung des Verfahrens über den Ablehnungsantrag der beklagten Partei gegen die Erstrichterin unterbrochen.

| Predicted | Gold |
|---|---|
| `Toth & Partner Rechtsanwälte OG` | `Toth & Partner Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Baumann` (person)
- `Dr. Veith` (person)
- `Dr. E. Solé` (person)
- `Dr. Schwarzenbacher` (person)
- `Dr. Nowotny` (person)
- `Erika Huwold` (person)
- `Gruböck & Lentschig Rechtsanwälte OG` (organisation)
- `MedR Dr.in Sara Stehlig` (person)
- `Arnold Schleicherdt` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/3Ob12_11b`) (sent_id: `deanon_260716_TRAIN/3Ob12_11b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Dagobert Schoeler, vertreten durch Hopmeier & Wagner Rechtsanwälte OG in Wien, gegen die beklagte Partei Peter Cuypers, vertreten durch Kaufmann & Thurnher Rechtsanwälte GmbH in Dornbirn, wegen Einwendungen gegen den Anspruch (§ 35 EO), über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts Feldkirch als Berufungsgericht vom 9. November 2010, GZ 3 R 354/10x-15, womit über Berufung der klagenden Partei das Urteil des Bezirksgerichts Bludenz vom 9. August 2010, GZ 4 C 516/10z-11, abgeändert wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hopmeier & Wagner Rechtsanwälte OG` | `Hopmeier & Wagner Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Prückner` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Lovrek` (person)
- `Dr. Jensik` (person)
- `Dr. Roch` (person)
- `Dagobert Schoeler` (person)
- `Peter Cuypers` (person)
- `Kaufmann & Thurnher Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Feldkirch` (organisation)
- `Bezirksgerichts Bludenz` (organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/3Ob137_17v`) (sent_id: `deanon_260716_TRAIN/3Ob137_17v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Jensik und Dr. Roch und die Hofrätin Dr. Kodek als weitere Richter in der Pflegschaftssache der Minderjährigen 1. StR Corvin Lengenfelder, geboren am 16. September 2007, 2. Alva Dielschneider, geboren am 28. April 2009, beide wohnhaft beim Vater Mag. Gottfried Clef, dieser vertreten durch Dr. Johann Etienne Korab, Rechtsanwalt in Wien, über den außerordentlichen Revisionsrekurs der Mutter Mag. Alma Plohn, vertreten durch Hornek Hubacek Lichtenstrasser Rechtsanwälte OG in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 15. Mai 2017, GZ 48 R 101/17b-137, womit Punkt 1. und 2. des Beschlusses des Bezirksgerichts Döbling vom 9. Jänner 2017, GZ 1 Ps 119/13b-90, bestätigt wurde, den Beschluss gefasst:  Spruch 1.

| Predicted | Gold |
|---|---|
| `Hornek Hubacek Lichtenstrasser Rechtsanwälte OG` | `Hornek Hubacek Lichtenstrasser Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hoch` (person)
- `Dr. Lovrek` (person)
- `Dr. Jensik` (person)
- `Dr. Roch` (person)
- `Dr. Kodek` (person)
- `StR Corvin Lengenfelder` (person)
- `16. September` (date)
- `Alva Dielschneider` (person)
- `28. April` (date)
- `Mag. Gottfried Clef` (person)
- `Dr. Johann Etienne Korab` (person)
- `Mag. Alma Plohn` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Döbling` (organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/3Ob166_25w`) (sent_id: `deanon_260716_TRAIN/3Ob166_25w_4`)


Eduard Mauderer, vertreten durch Mag. Sarah Abel, Rechtsanwältin in Salzburg, und 2. Schmiede Digital GmbH, Pöllmühle 139H, 2095 Drosendorf Stadt, Österreich, vertreten durch die Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, wegen 7.164,36 EUR sA und Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 10. Juli 2025, GZ 53 R 145/25t-18, mit dem das Teilurteil des Bezirksgerichts Salzburg vom 12. März 2025, GZ 31 C 1179/24h-12, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mahringer Steinwender Bestebner Rechtsanwälte OG` | `Mahringer Steinwender Bestebner Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Eduard Mauderer` (person)
- `Mag. Sarah Abel` (person)
- `Schmiede Digital GmbH` (organisation)
- `Pöllmühle 139H, 2095 Drosendorf Stadt, Österreich` (address)
- `Landesgerichts Salzburg` (organisation)
- `Bezirksgerichts Salzburg` (organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/3Ob170_20a`) (sent_id: `deanon_260716_TRAIN/3Ob170_20a_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Familienrechtssache des Antragstellers Christina Ach, vertreten durch GKP Gabl Kogler Leitner Stöglehner Bodingbauer Rechtsanwälte OG in Linz, gegen den Antragsgegner Raul Cattarius, Bakk. rer. nat. Bakk. phil., vertreten durch Dr. Thomas Marschall, Rechtsanwalt in Wien, wegen Unterhalts, über den Revisionsrekurs des Antragsgegners gegen den Beschluss des Landesgerichts Linz als Rekursgericht vom 7. August 2020, GZ 15 R 162/20d-329, mit dem der Beschluss des Bezirksgerichts Linz vom 27. April 2020, GZ 1 Pu 20/13m-323, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Bodingbauer Rechtsanwälte OG` | `Bodingbauer Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Hon.-Prof. PD Dr. Rassi` (person)
- `Dr. Weixelbraun-Mohr` (person)
- `Dr. Kodek` (person)
- `Dr. Stefula` (person)
- `Christina Ach` (person)
- `Raul Cattarius, Bakk. rer. nat. Bakk. phil.` (person)
- `Dr. Thomas Marschall` (person)
- `Landesgerichts Linz` (organisation)
- `Bezirksgerichts Linz` (organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/3Ob236_17b`) (sent_id: `deanon_260716_TRAIN/3Ob236_17b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Roch und Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Babette Ermentraut, vertreten durch Harb & Postl Rechtsanwälte OG in Graz, gegen die beklagte Partei OSR Dipl. Kfm. OMedR Raimund Stolarik, vertreten durch Dr. Paul Bauer, Dr. Anton Triendl, Rechtsanwälte in Innsbruck, wegen 32.173,22 EUR sA und Feststellung, über die außerordentliche Revision der beklagten Partei (Revisionsinteresse 23.653,60 EUR sA und Feststellung) gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 29. November 2017, GZ 10 R 59/17b-27, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Harb & Postl Rechtsanwälte OG` | `Harb & Postl Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hoch` (person)
- `Dr. Roch` (person)
- `Dr. Rassi` (person)
- `Dr. Weixelbraun-Mohr` (person)
- `Dr. Kodek` (person)
- `Babette Ermentraut` (person)
- `OSR Dipl. Kfm. OMedR Raimund Stolarik` (person)
- `Dr. Paul` (person)
- `Dr. Anton Triendl` (person)
- `Oberlandesgerichts Innsbruck` (organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/3Ob99_10w`) (sent_id: `deanon_260716_TRAIN/3Ob99_10w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Senatspräsidenten Hon.-Prof. Dr. Sailer, den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und den Hofrat Dr. Jensik als weitere Richter in der Rechtssache der klagenden Partei Dr. Johannes Müller, Rechtsanwalt, Wien 3, Ditscheinergasse 2, als Masseverwalter im Konkurs der Wald-Event GmbH, gegen die beklagte Partei Wiener Gebietskrankenkasse, Wien 10, Wienerbergstraße 15-19, vertreten durch Preslmayr Rechtsanwälte OG in Wien, und der Nebenintervenienten auf der Seite der beklagten Partei 1.)

| Predicted | Gold |
|---|---|
| `Preslmayr Rechtsanwälte OG` | `Preslmayr Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Prückner` (person)
- `Hon.-Prof. Dr. Sailer` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Lovrek` (person)
- `Dr. Jensik` (person)
- `Dr. Johannes Müller` (person)
- `Wald-Event GmbH` (organisation)
- `Wiener Gebietskrankenkasse` (organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/4Ob174_24b`) (sent_id: `deanon_260716_TRAIN/4Ob174_24b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Mag. Istjan, LL.M., und Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Greule Recycling GmbH, Staudenweg, Oberau 49, 3571 Stallegg, Österreich, vertreten durch Mag. Dieter Koch, Rechtsanwalt in Bruck an der Mur, gegen die beklagte Partei HEWQ IT Institut AG, Enengl-Florianiweg 15, 4892 Grubleiten, Österreich, vertreten durch die AHP Rechtsanwälte OG in Klagenfurt am Wörthersee, wegen 171.573,05 CHF sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 11. Juli 2024, GZ 4 R 62/24f-26, mit dem das Urteil des Landesgerichts Klagenfurt vom 31. Jänner 2024, GZ 20 Cg 40/23v-20, abgeändert wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `AHP Rechtsanwälte OG` | `AHP Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schwarzenbacher` (person)
- `Hon.-Prof. PD Dr. Rassi` (person)
- `Mag. Istjan, LL.M.` (person)
- `Mag. Waldstätten` (person)
- `Dr. Stiefsohn` (person)
- `Greule Recycling GmbH` (organisation)
- `Staudenweg, Oberau 49, 3571 Stallegg, Österreich` (address)
- `Mag. Dieter Koch` (person)
- `HEWQ IT Institut AG` (organisation)
- `Enengl-Florianiweg 15, 4892 Grubleiten, Österreich` (address)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts Klagenfurt` (organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/4Ob47_14m`) (sent_id: `deanon_260716_TRAIN/4Ob47_14m_4`)


Ulrich Schlaifer, vertreten durch die Galla & Herget Rechtsanwälte OG in Wien, 2.

| Predicted | Gold |
|---|---|
| `Galla & Herget Rechtsanwälte OG` | `Galla & Herget Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Ulrich Schlaifer` (person)

**Example 23** (doc_id: `deanon_260716_TRAIN/5Ob184_21a`) (sent_id: `deanon_260716_TRAIN/5Ob184_21a_4`)


Christian den Drijver, 2. Techn R Adalbert Amirzadeh, ebenda, beide vertreten durch Schlösser & Partner Rechtsanwälte OG in Wien, gegen die Antragsgegnerin Marion Döhnert, vertreten durch Mag. Michael Operschal Rechtsanwalt GmbH in Wien, wegen § 37 Abs 1 Z 8 iVm § 16 MRG, über den Revisionsrekurs der Antragsteller gegen den Sachbeschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 19. Mai 2021, GZ 40 R 2/21x-15, mit dem der Sachbeschluss des Bezirksgerichts Floridsdorf vom 30. Oktober 2020, GZ 28 Msch 9/19g-11, abgeändert wurde, den Sachbeschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Partner Rechtsanwälte OG` | `Partner Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Christian den Drijver` (person)
- `Techn R Adalbert Amirzadeh` (person)
- `Marion Döhnert` (person)
- `Mag. Michael Operschal Rechtsanwalt GmbH` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Floridsdorf` (organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/5Ob30_11i`) (sent_id: `deanon_260716_TRAIN/5Ob30_11i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und die Hofrätinnen Dr. Hurch und Dr. Lovrek sowie die Hofräte Dr. Höllwerth und Mag. Wurzer als weitere Richter in der wohnrechtlichen Außerstreitsache der Antragstellerin Edith Ilse Semyonov, vertreten durch Maraszto Milisits Rechtsanwälte OG in Wien, gegen den Antragsgegner DDr. Ernest Bayraktar, vertreten durch Dr. Erich Kafka und Dr. Manfred Palkovits, Rechtsanwälte in Wien, wegen §§ 6 Abs 2, 37 Abs 1 Z 2 MRG, über den Revisionsrekurs des Antragsgegners gegen den Sachbeschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 27. Oktober 2010, GZ 39 R 248/10z-60, mit dem infolge Rekurses des Antragsgegners der Sachbeschluss des Bezirksgerichts Döbling vom 27. April 2010, GZ 15 Msch 10/07p-51, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Maraszto Milisits Rechtsanwälte OG` | `Maraszto Milisits Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Danzl` (person)
- `Dr. Hurch` (person)
- `Dr. Lovrek` (person)
- `Dr. Höllwerth` (person)
- `Mag. Wurzer` (person)
- `Edith Ilse Semyonov` (person)
- `DDr. Ernest Bayraktar` (person)
- `Dr. Erich Kafka` (person)
- `Dr. Manfred Palkovits` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Döbling` (organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/7Ob110_13x`) (sent_id: `deanon_260716_TRAIN/7Ob110_13x_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Huber als Vorsitzende und die Hofrätinnen und Hofräte Dr. Hoch, Dr. Kalivoda, Mag. Dr. Wurdinger und Mag. Malesich als weitere Richter in der Rechtssache der klagenden Partei Gerdelbracht Telekom AG, KLG Gartengemeinde Adolfstor 4, 4352 Oberkalmberg, Österreich, vertreten durch Kunz Schima Wallentin Rechtsanwälte OG in Wien, gegen die beklagte Partei Mag. (FH) Franz Burgschmidt, vertreten durch Binder Grösswang Rechtsanwälte OG in Wien, wegen Erteilung von Auskünften, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. April 2013, GZ 11 R 75/13z-12, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Kunz Schima Wallentin Rechtsanwälte OG` | `Kunz Schima Wallentin Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Huber` (person)
- `Dr. Hoch` (person)
- `Dr. Kalivoda` (person)
- `Mag. Dr. Wurdinger` (person)
- `Mag. Malesich` (person)
- `Gerdelbracht Telekom AG` (organisation)
- `KLG Gartengemeinde Adolfstor 4, 4352 Oberkalmberg, Österreich` (address)
- `Mag. (FH) Franz Burgschmidt` (person)
- `Binder Grösswang Rechtsanwälte OG` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/7Ob165_18t`) (sent_id: `deanon_260716_TRAIN/7Ob165_18t_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. E. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Pflegschaftssache der mj Jean Mak, geboren am 6. August 2012, vertreten durch ihre Mutter Liliana Oberlach, diese vertreten durch Maus Riedherr Rechtsanwälte OG in Salzburg, wegen Unterhalts, über den Revisionsrekurs des Vaters Mag. Ing. Bodo Caspersen, vertreten durch Sattlegger, Dorninger, Steiner & Partner, Rechtsanwälte in Linz, gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 11. Juli 2018, GZ 21 R 134/18d-77, mit dem der Beschluss des Bezirksgerichts Salzburg vom 20. April 2016, GZ 4 Pu 110/15x-43, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Maus Riedherr Rechtsanwälte OG` | `Maus Riedherr Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Hon.-Prof. Dr. Höllwerth` (person)
- `Dr. E. Solé` (person)
- `Mag. Malesich` (person)
- `MMag. Matzka` (person)
- `Jean Mak` (person)
- `6. August` (date)
- `Liliana Oberlach` (person)
- `Mag. Ing. Bodo Caspersen` (person)
- `Landesgerichts Salzburg` (organisation)
- `Bezirksgerichts Salzburg` (organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/7Ob259_10d`) (sent_id: `deanon_260716_TRAIN/7Ob259_10d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Huber als Vorsitzende und durch die Hofräte Dr. Hoch, Dr. Kalivoda, Dr. Roch und Mag. Dr. Wurdinger als weitere Richter in den verbundenen Rechtssachen der klagenden und widerbeklagten Partei Maule Digital Rechtsanwälte GmbH, Zur Fischwasserung 33, 4090 Stadl, Österreich, gegen die beklagte und widerklagende Partei Mag. Wolfgang Kojima, vertreten durch GKP Gabl Kogler Papesch Leitner Rechtsanwälte OG in Linz, wegen 63.833,25 EUR sA (Klage) und 15.000 EUR sA (Widerklage), über die außerordentliche Revision der beklagten und widerklagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 9. November 2010, GZ 15 R 64/10g-89, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `GKP Gabl Kogler Papesch Leitner Rechtsanwälte OG` | `GKP Gabl Kogler Papesch Leitner Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Huber` (person)
- `Dr. Hoch` (person)
- `Dr. Kalivoda` (person)
- `Dr. Roch` (person)
- `Mag. Dr. Wurdinger` (person)
- `Maule Digital Rechtsanwälte GmbH` (organisation)
- `Zur Fischwasserung 33, 4090 Stadl, Österreich` (address)
- `Mag. Wolfgang Kojima` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/7Ob85_15y`) (sent_id: `deanon_260716_TRAIN/7Ob85_15y_4`)


Isabel Nestle AG, Reinsbach 186, 9131 Dolina, Österreich, vertreten durch Jank Weiler Operenyi Rechtsanwälte OG in Wien, 2.

| Predicted | Gold |
|---|---|
| `Jank Weiler Operenyi Rechtsanwälte OG` | `Jank Weiler Operenyi Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Isabel Nestle` (person)
- `Reinsbach 186, 9131 Dolina, Österreich` (address)

**Example 29** (doc_id: `deanon_260716_TRAIN/8ObA74_22y`) (sent_id: `deanon_260716_TRAIN/8ObA74_22y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Stefula als weitere Richter und die fachkundigen Laienrichter Dr. Ingomar Stupar (aus dem Kreis der Arbeitgeber) und Mag. Robert Brunner (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Sibylle Singl, vertreten durch Mag. Christian Marchhart, Rechtsanwalt in St. Pölten, dieser vertreten durch die Urbanek Lind Schmied Reisch Rechtsanwälte OG in St. Pölten, gegen die beklagten Parteien 1. Yussuf Waszek, und 2. Nikolai Terlinden, beide vertreten durch Mag. Agnes Lepschy, Rechtsanwältin in Altlengbach, wegen 86.509,66 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. Juli 2022, GZ 7 Ra 66/22k-63, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Urbanek Lind Schmied Reisch Rechtsanwälte OG` | `Urbanek Lind Schmied Reisch Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Kuras` (person)
- `Dr. Tarmann-Prentner` (person)
- `Dr. Stefula` (person)
- `Dr. Ingomar Stupar` (person)
- `Mag. Robert Brunner` (person)
- `Sibylle Singl` (person)
- `Mag. Christian Marchhart` (person)
- `Yussuf Waszek` (person)
- `Nikolai Terlinden` (person)
- `Mag. Agnes Lepschy` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/9Ob27_18p`) (sent_id: `deanon_260716_TRAIN/9Ob27_18p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsrekursgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Dehn, Dr. Hargassner, Mag. Korn und Dr. Stefula in der Rechtssache der klagenden Partei Thilo Aust, vertreten durch Mag. Dr. Surena Ettefagh, Rechtsanwalt in Frastanz, gegen die beklagte Partei Milan Turnherr, vertreten durch Achammer & Mennel Rechtsanwälte OG in Feldkirch, wegen Feststellung, Löschung von Grundbuchseintragungen und Räumung (Streitwert: 19.440 EUR sA), über den Revisionsrekurs der beklagten Partei gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 18. Jänner 2018, GZ 1 R 8/18m-150, mit dem der Rekurs der beklagten Partei gegen den Beschluss des Bezirksgerichts Bezau vom 30. Oktober 2015, GZ 5 C 39/14w-86, zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Achammer & Mennel Rechtsanwälte OG` | `Achammer & Mennel Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Dehn` (person)
- `Dr. Hargassner` (person)
- `Mag. Korn` (person)
- `Dr. Stefula` (person)
- `Thilo Aust` (person)
- `Dr. Surena Ettefagh` (person)
- `Milan Turnherr` (person)
- `Landesgerichts Feldkirch` (organisation)
- `Bezirksgerichts Bezau` (organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/9Ob3_20m`) (sent_id: `deanon_260716_TRAIN/9Ob3_20m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Dr. Fichtenau, Dr. Hargassner, Mag. Korn und Dr. Stefula in der Rechtssache der klagenden Partei Larissa Kleinicke, vertreten durch Dr. Harald Schwendinger und Dr. Brigitte Piber, Rechtsanwälte in Salzburg, gegen die beklagte Partei Ralph Heimersheim, vertreten durch Fahrner Unterrainer Rechtsanwälte OG in Zell am See, wegen Wiederaufnahme des Verfahrens AZ 17 C 29/13w des Bezirksgerichts Zell am See (wegen 11.658,48 EUR sA und Feststellung), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 25. April 2019, GZ 53 R 71/19a-9, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Fahrner Unterrainer Rechtsanwälte OG` | `Fahrner Unterrainer Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Fichtenau` (person)
- `Dr. Hargassner` (person)
- `Mag. Korn` (person)
- `Dr. Stefula` (person)
- `Larissa Kleinicke` (person)
- `Dr. Harald Schwendinger` (person)
- `Dr. Brigitte Piber` (person)
- `Ralph Heimersheim` (person)
- `Bezirksgerichts Zell am See` (organisation)
- `Landesgerichts Salzburg` (organisation)

**Example 32** (doc_id: `deanon_260716_TRAIN/9Ob49_19z`) (sent_id: `deanon_260716_TRAIN/9Ob49_19z_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Dehn, Dr. Hargassner, Mag. Korn und Dr. Stefula in der Rechtssache der klagenden Partei Traude Fahner, vertreten durch Dr. Harald Schwendinger und Dr. Brigitte Piber, Rechtsanwälte in Salzburg, gegen die beklagte Partei Stella Vaßmers, vertreten durch Fahrner Unterrainer Rechtsanwälte OG in Zell am See, wegen Wiederaufnahme des Verfahrens AZ 17 C 29/13w des Bezirksgerichts Zell am See (wegen 11.658,48 EUR sA und Feststellung), über den Rekurs der klagenden Partei gegen den Beschluss des Landesgerichts Salzburg als Berufungsgericht vom 13. Juni 2019, GZ 53 R 71/19a-12, mit dem der Antrag auf Abänderung des Unzulässigkeitsausspruchs gemäß § 508 Abs 1 ZPO zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Fahrner Unterrainer Rechtsanwälte OG` | `Fahrner Unterrainer Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Dehn` (person)
- `Dr. Hargassner` (person)
- `Mag. Korn` (person)
- `Dr. Stefula` (person)
- `Traude Fahner` (person)
- `Dr. Harald Schwendinger` (person)
- `Dr. Brigitte Piber` (person)
- `Stella Vaßmers` (person)
- `Bezirksgerichts Zell am See` (organisation)
- `Landesgerichts Salzburg` (organisation)

**Example 33** (doc_id: `deanon_260716_TRAIN/9Ob72_18f`) (sent_id: `deanon_260716_TRAIN/9Ob72_18f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Dehn, Dr. Hargassner, Mag. Korn und Dr. Stefula in der Rechtssache der klagenden Partei UnterTransport GmbH, Arnold-Rosé-Gasse 16, 8345 Krusdorf, Österreich, vertreten durch Knirsch Gschaider & Cerha Rechtsanwälte OG in Wien, sowie des Nebenintervenienten auf Seiten der klagenden Partei Dr. Scarlett Grimmecke, gegen die beklagte Partei Siebentritt Transport GesmbH, Pungartweg 25, 5232 Moosdorf, Österreich, vertreten durch Partnerschaft Schuppich Sporn & Winischhofer, Rechtsanwälte in Wien, wegen 159.824,87 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Juli 2018, GZ 129 R 55/18h-40, mit dem der Berufung der klagenden Partei gegen das Urteil des Handelsgerichts Wien vom 6. April 2018, GZ 21 Cg 23/15s-36, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt und beschlossen:  Spruch

| Predicted | Gold |
|---|---|
| `Gschaider & Cerha Rechtsanwälte OG` | `Gschaider & Cerha Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Dehn` (person)
- `Dr. Hargassner` (person)
- `Mag. Korn` (person)
- `Dr. Stefula` (person)
- `UnterTransport GmbH` (organisation)
- `Arnold-Rosé-Gasse 16, 8345 Krusdorf, Österreich` (address)
- `Dr. Scarlett Grimmecke` (person)
- `Siebentritt Transport GesmbH` (organisation)
- `Pungartweg 25, 5232 Moosdorf, Österreich` (address)
- `Partnerschaft Schuppich Sporn & Winischhofer, Rechtsanwälte` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 34** (doc_id: `deanon_260716_TRAIN/9ObA120_22w`) (sent_id: `deanon_260716_TRAIN/9ObA120_22w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende, den Hofrat Dr. Hargassner und die Hofrätin Mag. Korn sowie die fachkundigen Laienrichter Dr. Martina Michor (aus dem Kreis der Arbeitgeber) und Dr. Andrea Eisler (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Roswitha Prokscha, vertreten durch AHP Rechtsanwälte OG in Klagenfurt am Wörthersee, gegen die beklagte Partei Martin Mainardt, vertreten durch Moser Mutz, Rechtsanwälte GesbR in Klagenfurt am Wörthersee, wegen Einwilligung in die Auflösung eines Dienstverhältnisses, in eventu Feststellung (Streitwert 94.891,52 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. September 2022, GZ 7 Ra 23/22i-24, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `AHP Rechtsanwälte OG` | `AHP Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Fichtenau` (person)
- `Dr. Hargassner` (person)
- `Mag. Korn` (person)
- `Dr. Martina Michor` (person)
- `Dr. Andrea Eisler` (person)
- `Roswitha Prokscha` (person)
- `Martin Mainardt` (person)
- `Moser Mutz, Rechtsanwälte GesbR` (organisation)
- `Oberlandesgerichts Graz` (organisation)

**Example 35** (doc_id: `deanon_260716_TRAIN/9ObA41_14s`) (sent_id: `deanon_260716_TRAIN/9ObA41_14s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras, die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Mag. Gerald Fuchs und Peter Schönhofer als weitere Richter in der Arbeitsrechtssache der klagenden Partei Clarissa Bannwarth, vertreten durch Dr. Remo Sacherer, Rechtsanwalt in Wien, gegen die beklagte Partei Garten Bernexdorf AG, Sittestraße 49, 4203 Katzgraben, Österreich, vertreten durch Korn Rechtsanwälte OG in Wien, wegen Kündigungsanfechtung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Februar 2014, GZ 7 Ra 4/14f-29, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Korn Rechtsanwälte OG` | `Korn Rechtsanwälte OG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kuras` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Dehn` (person)
- `Mag. Gerald Fuchs` (person)
- `Peter Schönhofer` (person)
- `Clarissa Bannwarth` (person)
- `Dr. Remo Sacherer` (person)
- `Garten Bernexdorf AG` (organisation)
- `Sittestraße 49, 4203 Katzgraben, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/1Ob128_17f`) (sent_id: `deanon_260716_TRAIN/1Ob128_17f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Familienrechtssache des Antragstellers Mag. Josefine Rehn, vertreten durch die Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG, Wien, gegen die Antragsgegnerin Susanne Lürkens, vertreten durch Mag. Anna-Maria Freiberger, Rechtsanwältin in Wien, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 24. April 2017, GZ 45 R 66/17i, 67/17m-19, mit dem die Beschlüsse des Bezirksgerichts Liesing vom 4. Jänner 2017, GZ 7 Fam 30/16m-12, und vom 17. Jänner 2017, GZ 7 Fam 30/16m-14, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Norbert Marschall Rechtsanwälte OG` — partial — pred is substring of gold: `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Mag. Josefine Rehn`(person)
- `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG`(organisation)
- `Susanne Lürkens`(person)
- `Mag. Anna-Maria Freiberger`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Liesing`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/1Ob182_17x`) (sent_id: `deanon_260716_TRAIN/1Ob182_17x_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Dr. Wurdinger, und die Hofrätinnen Dr. Hofer-Zeni-Rennhofer und Dr. Kodek in der Rechtssache der gefährdeten Partei Aloisa Moosleitner, vertreten durch die Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG, Wien, gegen die gefährdete Partei Catharina Uppenbrink, vertreten durch Dr. Alexander Haas, Rechtsanwalt in Seiersberg-Pirka, wegen Erlassung einer einstweiligen Verfügung nach § 382 Z 8 lit c zweiter Fall EO, über den außerordentlichen Revisionsrekurs der gefährdeten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 11. September 2017, GZ 1 R 213/17a-221, mit dem der Beschluss des Bezirksgerichts Fürstenfeld vom 25. Juli 2017, GZ 23 Fam 27/15p-207, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Norbert Marschall Rechtsanwälte OG` — partial — pred is substring of gold: `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Mag. Wurzer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Kodek`(person)
- `Aloisa Moosleitner`(person)
- `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG`(organisation)
- `Catharina Uppenbrink`(person)
- `Dr. Alexander Haas`(person)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)
- `Bezirksgerichts Fürstenfeld`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/2Ob162_23x`) (sent_id: `deanon_260716_TRAIN/2Ob162_23x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte Hon.-Prof. PD Dr. Rassi, MMag. Sloboda und Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Prof.in Romana Janaseck, vertreten durch Lirk Spielbüchler Hirtzberger Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Simone Gintautas, wegen Feststellung, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 18. Juli 2023, GZ 21 R 75/23k-7, mit dem der Beschluss des Bezirksgerichts St. Johann im Pongau vom 28. Februar 2023, GZ 305 C 9/23x-3, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Hirtzberger Rechtsanwälte OG` — partial — pred is substring of gold: `Lirk Spielbüchler Hirtzberger Rechtsanwälte OG`

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

**Example 3** (doc_id: `deanon_260716_TRAIN/2Ob194_19x`) (sent_id: `deanon_260716_TRAIN/2Ob194_19x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden und den Hofrat Dr. Musger, die Hofrätin Dr. Solé und die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Haßtenteufel Umwelt GmbH & Co KG, Peter Zauner Weg 324, 5273 Wesen, Österreich, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Klagenfurt, gegen die beklagte Partei Isaak Tomzak, vertreten durch Dr. Maximilian Motschiunig, Rechtsanwalt in Klagenfurt, wegen Vertragsaufhebung und Abgabe einer Willenserklärung (Streitwert 35.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 1. Oktober 2019, GZ 2 R 141/19a, 2 R 142/19y-95, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Sommer Rechtsanwälte OG` — partial — pred is substring of gold: `Gheneff - Rami - Sommer Rechtsanwälte OG`

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

**Example 4** (doc_id: `deanon_260716_TRAIN/2Ob86_12d`) (sent_id: `deanon_260716_TRAIN/2Ob86_12d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Erika Huwold, vertreten durch Gruböck & Lentschig Rechtsanwälte OG in Baden, wider die beklagte Partei „ MedR Dr.in Sara Stehlig “ Arnold Schleicherdt, vertreten durch Themmer, Toth & Partner Rechtsanwälte OG in Wien, wegen 144.329,55 EUR sA (Revisionsinteresse 54.717 EUR sA), infolge der außerordentlichen Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Februar 2012, GZ 4 R 598/11g-25, den Beschluss gefasst:  Spruch Das Revisionsverfahren wird bis zur rechtskräftigen Erledigung des Verfahrens über den Ablehnungsantrag der beklagten Partei gegen die Erstrichterin unterbrochen.

**False Positives:**

- `Lentschig Rechtsanwälte OG` — partial — pred is substring of gold: `Gruböck & Lentschig Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Baumann`(person)
- `Dr. Veith`(person)
- `Dr. E. Solé`(person)
- `Dr. Schwarzenbacher`(person)
- `Dr. Nowotny`(person)
- `Erika Huwold`(person)
- `Gruböck & Lentschig Rechtsanwälte OG`(organisation)
- `MedR Dr.in Sara Stehlig`(person)
- `Arnold Schleicherdt`(person)
- `Toth & Partner Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/3Ob222_17v`) (sent_id: `deanon_260716_TRAIN/3Ob222_17v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Jensik und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Familienrechtssache des Antragstellers Janosch von Reichel, vertreten durch Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG in Wien, gegen den Antragsgegner Vincent Niederführ, vertreten durch Dr. Heinz-Peter Wachter, Rechtsanwalt in Wien, wegen Unterhaltsherabsetzung, über den Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2017, GZ 45 R 267/17y-81, womit der Beschluss des Bezirksgerichts Fünfhaus vom 12. April 2017, GZ 3 Fam 9/15b-72, abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Norbert Marschall Rechtsanwälte OG` — partial — pred is substring of gold: `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hoch`(person)
- `Dr. Jensik`(person)
- `Mag. Painsi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Janosch von Reichel`(person)
- `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG`(organisation)
- `Vincent Niederführ`(person)
- `Dr. Heinz-Peter Wachter`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Fünfhaus`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/3Ob245_19d`) (sent_id: `deanon_260716_TRAIN/3Ob245_19d_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie den Hofrat Priv.-Doz. Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Axel Capkin, vertreten durch Dr. Gerda Schildberger, Rechtsanwältin in Bruck an der Mur, gegen die beklagte Partei Milena Kurthen, vertreten durch Dr. Zsizsik & Dr. Prattes Rechtsanwälte OG in Bruck an der Mur, wegen Unterhalt, über die „außerordentliche Revision“ der klagenden Partei gegen das Urteil des Landesgerichts Leoben als Berufungsgericht vom 4. November 2019, GZ 2 R 204/19b-48, den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.  Text Begründung: Die Klägerin begehrte vom Beklagten Ehegattenunterhalt in unterschiedlicher (mehrfach ausgedehnter und eingeschränkter) Höhe für vergangene Zeiträume sowie laufenden Unterhalt ab Jänner 2019 von je 358 EUR monatlich.

**False Positives:**

- `Prattes Rechtsanwälte OG` — partial — pred is substring of gold: `Dr. Zsizsik & Dr. Prattes Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Roch`(person)
- `Priv.-Doz. Dr. Rassi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Mag. Pertmayr`(person)
- `Axel Capkin`(person)
- `Dr. Gerda Schildberger`(person)
- `Milena Kurthen`(person)
- `Dr. Zsizsik & Dr. Prattes Rechtsanwälte OG`(organisation)
- `Landesgerichts Leoben`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/4Ob142_21t`) (sent_id: `deanon_260716_TRAIN/4Ob142_21t_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Hon.-Prof. PD Dr. Rassi als Vorsitzenden und die Hofräte und Hofrätinnen Dr. Schwarzenbacher, Dr. Kodek, MMag. Matzka sowie Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei Laurence Perger, vertreten durch Viehböck Breiter Schenk & Nau Rechtsanwälte OG in Mödling, gegen die beklagte Partei EIPD Chemie ges.m.b.H., Insel 21, 4840 Diesenbach, Österreich, vertreten durch Celar Senoner Weber-Wilfert Rechtsanwälte GmbH in Wien, wegen Herausgabe eines Buchauszugs (Streitwert 4.000 EUR) und 41.049,64 EUR sA, über die außerordentliche Revision der klagenden Partei, gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Mai 2021, GZ 5 R 162/20k-66, mit dem das Urteil des Handelsgerichts Wien vom 30. September 2020, GZ 48 Cg 28/19f-59, bestätigt wurde, beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Schenk & Nau Rechtsanwälte OG` — partial — pred is substring of gold: `Viehböck Breiter Schenk & Nau Rechtsanwälte OG`

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

**Example 8** (doc_id: `deanon_260716_TRAIN/5Ob180_19k`) (sent_id: `deanon_260716_TRAIN/5Ob180_19k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer, Mag. Painsi und Dr. Steger als weitere Richter in der Rechtssache der klagenden und gefährdeten Partei Marianne Haspolat, BEd GmbH, Feldgraben 4, 4081 Haizing, Österreich, vertreten durch Dr. Bernd Roßkothen, Rechtsanwalt in Salzburg, gegen die beklagte Partei und Gegnerin der gefährdeten Partei Christina Leiteritz GmbH, Rachlgasse 10, 3834 Arnolz, Österreich, vertreten durch die König & Kliemstein Rechtsanwälte OG in Salzburg, wegen Erlassung einer einstweiligen Verfügung (Streitwert 35.000 EUR), über den Revisionsrekurs der klagenden und gefährdeten Partei gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 29. August 2019, GZ 6 R 94/19i-15, mit dem der Beschluss des Landesgerichts Salzburg vom 22. Juli 2019, GZ 57 Cg 101/19k-3, über Rekurs der beklagten Partei und Gegnerin der gefährdeten Partei abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Kliemstein Rechtsanwälte OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Jensik`(person)
- `Dr. Grohmann`(person)
- `Mag. Wurzer`(person)
- `Mag. Painsi`(person)
- `Dr. Steger`(person)
- `Marianne Haspolat, BEd`(person)
- `Feldgraben 4, 4081 Haizing, Österreich`(address)
- `Dr. Bernd Roßkothen`(person)
- `Christina Leiteritz`(person)
- `Rachlgasse 10, 3834 Arnolz, Österreich`(address)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Salzburg`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/6Ob169_12i`) (sent_id: `deanon_260716_TRAIN/6Ob169_12i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Pimmer als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Dr. Schramm, Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Seesteincon-Transport GmbH, Wildbacher Straße 174, 3623 Bernhards, Österreich, vertreten durch List Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Heimnor GmbH, Am Johannisgraben 44, 8200 Albersdorf, Österreich, vertreten durch Dr. Christoph Brenner - Mag. Severin Perschl Rechtsanwälte OG in Krems, wegen 7.641,30 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Korneuburg als Berufungsgericht vom 16. Februar 2012, GZ 21 R 262/11v-50, womit das Urteil des Bezirksgerichts Gänserndorf vom 2. August 2011, GZ 12 C 1036/10h-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Severin Perschl Rechtsanwälte OG` — partial — pred is substring of gold: `Mag. Severin Perschl Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Pimmer`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schramm`(person)
- `Dr. Gitschthaler`(person)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. Nowotny`(person)
- `Seesteincon-Transport GmbH`(organisation)
- `Wildbacher Straße 174, 3623 Bernhards, Österreich`(address)
- `List Rechtsanwälte GmbH`(organisation)
- `Heimnor GmbH`(organisation)
- `Am Johannisgraben 44, 8200 Albersdorf, Österreich`(address)
- `Dr. Christoph Brenner`(person)
- `Mag. Severin Perschl Rechtsanwälte OG`(organisation)
- `Landesgerichts Korneuburg`(organisation)
- `Bezirksgerichts Gänserndorf`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/7Ob180_16w`) (sent_id: `deanon_260716_TRAIN/7Ob180_16w_4`)


Dr. Anabel Heimboeckel, vertreten durch Rechtsanwälte Dr. Amhof & Dr. Damian GmbH in Wien, gegen die beklagte Partei Dominik Westerberger, vertreten durch Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG in Wien, wegen Ehescheidung, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 22. Juni 2016, GZ 42 R 130/16b-33, womit das Urteil des Bezirksgerichts Innere Stadt Wien vom 30. Dezember 2015, GZ 3 C 9/14w-27, bestätigt wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Norbert Marschall Rechtsanwälte OG` — partial — pred is substring of gold: `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Anabel Heimboeckel`(person)
- `Rechtsanwälte Dr. Amhof & Dr. Damian GmbH`(organisation)
- `Dominik Westerberger`(person)
- `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Innere Stadt Wien`(organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/7Ob80_18t`) (sent_id: `deanon_260716_TRAIN/7Ob80_18t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Dr. Höllwerth, Dr. E. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden und widerbeklagten Partei Martha Masius, vertreten durch die Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG in Wien, gegen die beklagte und widerklagende Partei Evelyn Möckel, vertreten durch Mag. Petra Laback, Rechtsanwältin in Wien, wegen Ehescheidung, über die außerordentlichen Revisionen beider Parteien gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 14. Februar 2018, GZ 42 R 417/17k-57, den Beschluss gefasst:  Spruch Die außerordentlichen Revisionen beider Parteien werden gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Norbert Marschall Rechtsanwälte OG` — partial — pred is substring of gold: `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Dr. Höllwerth`(person)
- `Dr. E. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Martha Masius`(person)
- `Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG`(organisation)
- `Evelyn Möckel`(person)
- `Mag. Petra Laback`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/8ObA14_21y`) (sent_id: `deanon_260716_TRAIN/8ObA14_21y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn als weitere Richter sowie die fachkundigen Laienrichter Johannes Püller (aus dem Kreis der Arbeitgeber) und Mag. Thomas Kallab (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Ing. Annalena Wirtl, vertreten durch Stögerer Preisinger Rechtsanwälte OG in Wien, gegen die beklagte Partei Justin von Rücker, vertreten durch die Finanzprokuratur, 1010 Wien, Singerstraße 17–19, wegen Feststellung (Interesse 7.089,60 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 18. Dezember 2020, GZ 7 Ra 46/20s-14, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Preisinger Rechtsanwälte OG` — partial — pred is substring of gold: `Stögerer Preisinger Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Tarmann-Prentner`(person)
- `Mag. Korn`(person)
- `Johannes Püller`(person)
- `Mag. Thomas Kallab`(person)
- `Ing. Annalena Wirtl`(person)
- `Stögerer Preisinger Rechtsanwälte OG`(organisation)
- `Justin von Rücker`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/9Ob2_19p`) (sent_id: `deanon_260716_TRAIN/9Ob2_19p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsrekursgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätinnen und Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Dehn, Dr. Hargassner, Mag. Korn und Dr. Stefula in der Pflegschaftssache der mj OSR Noah Glaesser, geboren am 8. März 2015, wohnhaft bei der Mutter Mag. Bettina Ewerting, vertreten durch Dr. Karin Prutsch ua, Rechtsanwälte in Graz, Vater Prof. Dr. Oleg Bohl, vertreten durch BHF Briefer Hülle Frohner Rechtsanwälte OG in Wien, wegen Unterhalt, über den „außerordentlichen Revisionsrekurs“ der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 6. November 2018, GZ 1 R 240/18y-24, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt. Begründung:  Rechtliche Beurteilung Gemäß § 62 Abs 3 AußStrG ist der Revisionsrekurs – außer im Fall des § 63 Abs 3 AußStrG – jedenfalls unzulässig, wenn der Entscheidungsgegenstand an Geld oder Geldeswert insgesamt 30.000 EUR nicht übersteigt und das Rekursgericht nach § 59 Abs 1 Z 2 AußStrG den ordentlichen Revisionsrekurs für nicht zulässig erklärt hat.

**False Positives:**

- `Frohner Rechtsanwälte OG` — partial — pred is substring of gold: `BHF Briefer Hülle Frohner Rechtsanwälte OG`

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
- `OSR Noah Glaesser`(person)
- `8. März`(date)
- `Mag. Bettina Ewerting`(person)
- `Dr. Karin Prutsch`(person)
- `Dr. Oleg Bohl`(person)
- `BHF Briefer Hülle Frohner Rechtsanwälte OG`(organisation)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)

</details>

---

## `Law_Firm_OG_KG_GmbH` 🏆

**F1:** 0.035 | **Precision:** 0.667 | **Recall:** 0.018  

**Format:** `regex`  
**Rule ID:** `ac276403`  
**Description:**
Matches law firms identified by suffixes OG, KG, or GmbH, allowing for slashes, hyphens, and 'und'/'&' in names, ensuring full name capture including 'GmbH & Co KG'.

**Content:**
```
(?<![\w])([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*|[A-Z][a-zA-Z]+(?:-[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\+[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s+und\s+[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s*&\s*[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s+&\s*[A-Z][a-zA-Z]+)+|[A-Za-z]+(?:/[A-Za-z]+)+)\s+(?:Rechtsanwälte|Anwälte|Anwaltsgesellschaft)\s+(?:OG|KG|GmbH|mbH|GmbH\s+&\s+Co\s+KG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.667 | 0.018 | 0.035 | 108 | 72 | 36 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 72 | 36 | 3923 |

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

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_3`)


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

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob18_13i`) (sent_id: `deanon_260716_TRAIN/10Ob18_13i_3`)


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

**Example 3** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_3`)


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

**Example 4** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_3`)


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

**Example 5** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_3`)


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

**Example 6** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


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

**Example 7** (doc_id: `deanon_260716_TRAIN/17Ob10_19y`) (sent_id: `deanon_260716_TRAIN/17Ob10_19y_3`)


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

**Example 8** (doc_id: `deanon_260716_TRAIN/17Ob10_20z`) (sent_id: `deanon_260716_TRAIN/17Ob10_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätinnen Mag. Malesich und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Pascal Alsweh, vertreten durch Stephan Briem Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Dr. Simone Pittruff als Treuhänder der Insolvenzgläubiger der Unter-Analyse Aktiengesellschaft, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH in Linz, wegen Feststellung (Streitwert 18.335,66 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. März 2020, GZ 1 R 31/20i-13, womit das Urteil des Landesgerichts Linz vom 9. Dezember 2019, GZ 4 Cg 73/18z-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Shamiyeh & Reiser Rechtsanwälte GmbH` | `Shamiyeh & Reiser Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Dr. Musger` (person)
- `Mag. Malesich` (person)
- `Dr. Kodek` (person)
- `Dr. Stefula` (person)
- `Pascal Alsweh` (person)
- `Stephan Briem Rechtsanwalt GmbH` (organisation)
- `Dr. Simone Pittruff` (person)
- `Unter-Analyse Aktiengesellschaft` (organisation)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Linz` (organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/18OCg12_19t`) (sent_id: `deanon_260716_TRAIN/18OCg12_19t_3`)


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

**Example 10** (doc_id: `deanon_260716_TRAIN/1Ob105_18z`) (sent_id: `deanon_260716_TRAIN/1Ob105_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Familienrechtssache des Antragstellers Ludmilla Bonauer, vertreten durch die Korp Rechtsanwalts GmbH, Andorf, gegen die Antragsgegnerin Henriette Geißendorf, vertreten durch die Puttinger Vogl Rechtsanwälte GmbH, Ried im Innkreis, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts Wels als Rekursgericht vom 2. Mai 2018, GZ 21 R 50/18d-32, mit dem der Rekurs des Antragstellers gegen den Beschluss des Bezirksgerichts Grieskirchen vom 8. Jänner 2018, GZ 8 Fam 37/16i-26, zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Puttinger Vogl Rechtsanwälte GmbH` | `Puttinger Vogl Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Ludmilla Bonauer` (person)
- `Korp Rechtsanwalts GmbH` (organisation)
- `Henriette Geißendorf` (person)
- `Landesgerichts Wels` (organisation)
- `Bezirksgerichts Grieskirchen` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/1Ob109_18p`) (sent_id: `deanon_260716_TRAIN/1Ob109_18p_3`)


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

**Example 12** (doc_id: `deanon_260716_TRAIN/1Ob12_21b`) (sent_id: `deanon_260716_TRAIN/1Ob12_21b_3`)


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

**Example 13** (doc_id: `deanon_260716_TRAIN/1Ob152_24w`) (sent_id: `deanon_260716_TRAIN/1Ob152_24w_3`)


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

**Example 14** (doc_id: `deanon_260716_TRAIN/1Ob178_19m`) (sent_id: `deanon_260716_TRAIN/1Ob178_19m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Hilde Dammrow, vertreten durch die Korn und Gärtner Rechtsanwälte OG, Salzburg, gegen die beklagte Partei Evelyn Allmutter, vertreten durch die Ferner Hornung & Partner Rechtsanwälte GmbH, Salzburg, wegen Wiederaufnahme des Verfahrens AZ 17 C 1538/16p des Bezirksgerichts Salzburg, über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 12. Juni 2019, GZ 22 R 163/19b-7, mit dem der Beschluss des Bezirksgerichts Salzburg vom 25. Jänner 2019, GZ 17 C 80/19f-2, mit einer Maßgabe bestätigt wurde, den Beschluss gefasst:  Spruch Dem außerordentlichen Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hornung & Partner Rechtsanwälte GmbH` | `Hornung & Partner Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Hilde Dammrow` (person)
- `Evelyn Allmutter` (person)
- `Bezirksgerichts Salzburg` (organisation)
- `Landesgerichts Salzburg` (organisation)
- `Bezirksgerichts Salzburg` (organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/1Ob226_20x`) (sent_id: `deanon_260716_TRAIN/1Ob226_20x_3`)


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

**Example 16** (doc_id: `deanon_260716_TRAIN/1Ob53_25p`) (sent_id: `deanon_260716_TRAIN/1Ob53_25p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Dr. Wurdinger als Vorsitzenden sowie die Hofrätin und die Hofräte Dr. Steger, Mag. Wessely-Kristöfel, Dr. Parzmayr und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Gottfried Lügenbiehl, vertreten durch die ANWALTGMBH Rinner Teuchtmann in Linz, gegen die beklagte Partei Ing. Marlene Fahlandt, vertreten durch die Wintersberger Rechtsanwälte GmbH in Ried im Innkreis, wegen 200.500 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 30. Jänner 2025, GZ 1 R 2/25g-86, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Wintersberger Rechtsanwälte GmbH` | `Wintersberger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Steger` (person)
- `Mag. Wessely-Kristöfel` (person)
- `Dr. Parzmayr` (person)
- `Dr. Vollmaier` (person)
- `Gottfried Lügenbiehl` (person)
- `ANWALTGMBH Rinner Teuchtmann` (organisation)
- `Ing. Marlene Fahlandt` (person)
- `Oberlandesgerichts Linz` (organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/1Ob56_17t`) (sent_id: `deanon_260716_TRAIN/1Ob56_17t_4`)


Gloria Hackenbuchner GmbH, Untere Kanalstraße 187, 2471 Hollern, Österreich, vertreten durch Mag. Manfred Sommerbauer und MMag. Dr. Michael Dohr LL.M., Rechtsanwälte in Wiener Neustadt, und 2. Nelleßen + Stümpfel Automotive AG, Villengasse 31, 8670 Krieglach, Österreich, vertreten durch die Kosch & Partner Rechtsanwälte GmbH, Wiener Neustadt, wegen 76.444,01 EUR sA über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Jänner 2017, GZ 1 R 164/16v-174, mit dem das Urteil des Handelsgerichts Wien vom 12. August 2016, GZ 65 Cg 12/15x-169, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Kosch & Partner Rechtsanwälte GmbH` | `Kosch & Partner Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Gloria Hackenbuchner` (person)
- `Untere Kanalstraße 187, 2471 Hollern, Österreich` (address)
- `Mag. Manfred Sommerbauer` (person)
- `MMag. Dr. Michael Dohr LL.M.` (person)
- `Nelleßen + Stümpfel Automotive AG` (organisation)
- `Villengasse 31, 8670 Krieglach, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/1Ob95_21h`) (sent_id: `deanon_260716_TRAIN/1Ob95_21h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Gawelzyk Pflege GmbH, Am See IX 247, 6320 Achleit, Österreich, vertreten durch die Zumtobel Kronberger Rechtsanwälte OG, Salzburg, gegen die beklagte Partei Loos und Woiciech Analyse GmbH, Rasenweg 21, 3441 Baumgarten am Tullnerfeld, Österreich, vertreten durch die Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH, Salzburg, wegen 135.656,39 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. April 2021, GZ 2 R 39/21z-27, mit dem das Urteil des Landesgerichts Ried im Innkreis vom 27. Jänner 2021, GZ 2 Cg 24/20i-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` | `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Bydlinski` (person)
- `Mag. Wurzer` (person)
- `Mag. Dr. Wurdinger` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Parzmayr` (person)
- `Gawelzyk Pflege GmbH` (organisation)
- `Am See IX 247, 6320 Achleit, Österreich` (address)
- `Zumtobel Kronberger Rechtsanwälte OG` (organisation)
- `Loos und Woiciech Analyse GmbH` (organisation)
- `Rasenweg 21, 3441 Baumgarten am Tullnerfeld, Österreich` (address)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Ried im Innkreis` (organisation)

**Example 19** (doc_id: `deanon_260716_TRAIN/2Ob114_24i`) (sent_id: `deanon_260716_TRAIN/2Ob114_24i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte MMag. Sloboda, Dr. Thunhart, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Dorothea Woltzen, vertreten durch Metzler & Partner Rechtsanwälte GmbH in Linz, gegen die beklagte Partei Edeltraud Eickemeyer, vertreten durch Nenning & Tockner, Rechtsanwälte in Steyr, wegen Herstellung, Ausfolgung und Unterlassung über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Steyr als Berufungsgericht vom 21. Dezember 2023, GZ 1 R 116/23m-12, mit dem einer Berufung der beklagten Partei gegen das Urteil des Bezirksgerichts Kirchdorf an der Krems vom 26. Juli 2023, GZ 1 C 132/23y-7, Folge gegeben wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Metzler & Partner Rechtsanwälte GmbH` | `Metzler & Partner Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Grohmann` (person)
- `MMag. Sloboda` (person)
- `Dr. Thunhart` (person)
- `Dr. Kikinger` (person)
- `Mag. Fitz` (person)
- `Dorothea Woltzen` (person)
- `Edeltraud Eickemeyer` (person)
- `Nenning & Tockner, Rechtsanwälte` (organisation)
- `Landesgerichts Steyr` (organisation)
- `Bezirksgerichts Kirchdorf an der Krems` (organisation)

**Example 20** (doc_id: `deanon_260716_TRAIN/2Ob115_10s`) (sent_id: `deanon_260716_TRAIN/2Ob115_10s_4`)


Uniber-Verlag AG, Jedretsberg 24, 4190 Brunnwald, Österreich, und 2. Fenuni AG, Wildschönauerstraße, Oberau 3, 8444 Reith, Österreich, beide vertreten durch die Liebenwein Rechtsanwälte GmbH in Wien, gegen die beklagten und widerklagenden Parteien 1.

| Predicted | Gold |
|---|---|
| `Liebenwein Rechtsanwälte GmbH` | `Liebenwein Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Uniber-Verlag AG` (organisation)
- `Jedretsberg 24, 4190 Brunnwald, Österreich` (address)
- `Fenuni AG` (organisation)
- `Wildschönauerstraße, Oberau 3, 8444 Reith, Österreich` (address)

**Example 21** (doc_id: `deanon_260716_TRAIN/2Ob115_10s`) (sent_id: `deanon_260716_TRAIN/2Ob115_10s_5`)


Seecon Verlag GmbH, Krengasse 31, 3911 Marbach am Walde, Österreich, und 2. Mag. Lena Zikorski, beide vertreten durch die Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH in Wien, wegen jeweils 50.000,50 EUR sA (Klagen) und 483.000 EUR sA (Widerklagen), über die außerordentliche Revision der klagenden und widerbeklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. April 2010, GZ 15 R 257/09p-58, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH` | `Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Seecon Verlag GmbH` (organisation)
- `Krengasse 31, 3911 Marbach am Walde, Österreich` (address)
- `Mag. Lena Zikorski` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/2Ob194_24d`) (sent_id: `deanon_260716_TRAIN/2Ob194_24d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte MMag. Sloboda, Dr. Thunhart, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Dagobert Drügemöller, vertreten durch Gottgeisl Leinsmer Weber Rechtsanwälte GmbH in Wien, wider die beklagte Partei Rosalinde Nölker, Malta, vertreten durch Mag. Simon Wallner Rechtsanwalt GmbH in Wien, wegen 30.895 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 1. Oktober 2024, GZ 12 R 72/24g-21, den Beschluss gefasst:  Spruch I. Der Antrag auf Unterbrechung des Revisionsverfahrens bis zur Entscheidung des Europäischen Gerichtshofs zu C-683/24 wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Gottgeisl Leinsmer Weber Rechtsanwälte GmbH` | `Gottgeisl Leinsmer Weber Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Grohmann` (person)
- `MMag. Sloboda` (person)
- `Dr. Thunhart` (person)
- `Dr. Kikinger` (person)
- `Mag. Fitz` (person)
- `Dagobert Drügemöller` (person)
- `Rosalinde Nölker` (person)
- `Mag. Simon Wallner Rechtsanwalt GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/2Ob79_11y`) (sent_id: `deanon_260716_TRAIN/2Ob79_11y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Angelika Erdönmez, vertreten durch Hengstschläger Lindner und Partner Rechtsanwälte GmbH in Linz, gegen die beklagte Partei Sabine Lance, vertreten durch Mag. Gerlach Bachinger, Rechtsanwalt in Traun, wegen 14.957,31 EUR sA und Feststellung (Streitinteresse: 7.500 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 15. März 2011, GZ 3 R 34/11g-24, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts Linz vom 22. Dezember 2010, GZ 1 Cg 210/09m-20, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Lindner und Partner Rechtsanwälte GmbH` | `Lindner und Partner Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Baumann` (person)
- `Dr. Veith` (person)
- `Dr. E. Solé` (person)
- `Dr. Schwarzenbacher` (person)
- `Dr. Nowotny` (person)
- `Angelika Erdönmez` (person)
- `Sabine Lance` (person)
- `Mag. Gerlach Bachinger` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Linz` (organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/3Ob108_18f`) (sent_id: `deanon_260716_TRAIN/3Ob108_18f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Roch und Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Dr. Denis Aichmüller, vertreten durch Scherbaum Seebacher Rechtsanwälte GmbH in Graz, wider die beklagte Partei Hemma Fenski, vertreten durch Dr. Destaller ua, Rechtsanwälte in Graz, wegen (eingeschränkt) Räumung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 23. Februar 2018, GZ 7 R 137/17v-19, mit dem das Urteil des Bezirksgerichts Graz-Ost vom 29. September 2017, GZ 213 C 131/16m-15, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Scherbaum Seebacher Rechtsanwälte GmbH` | `Scherbaum Seebacher Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hoch` (person)
- `Dr. Roch` (person)
- `Dr. Rassi` (person)
- `Dr. Weixelbraun-Mohr` (person)
- `Dr. Kodek` (person)
- `Dr. Denis Aichmüller` (person)
- `Hemma Fenski` (person)
- `Dr. Destaller` (person)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)
- `Bezirksgerichts Graz-Ost` (organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/3Ob12_11b`) (sent_id: `deanon_260716_TRAIN/3Ob12_11b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Dagobert Schoeler, vertreten durch Hopmeier & Wagner Rechtsanwälte OG in Wien, gegen die beklagte Partei Peter Cuypers, vertreten durch Kaufmann & Thurnher Rechtsanwälte GmbH in Dornbirn, wegen Einwendungen gegen den Anspruch (§ 35 EO), über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts Feldkirch als Berufungsgericht vom 9. November 2010, GZ 3 R 354/10x-15, womit über Berufung der klagenden Partei das Urteil des Bezirksgerichts Bludenz vom 9. August 2010, GZ 4 C 516/10z-11, abgeändert wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Kaufmann & Thurnher Rechtsanwälte GmbH` | `Kaufmann & Thurnher Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Prückner` (person)
- `Hon.-Prof. Dr. Neumayr` (person)
- `Dr. Lovrek` (person)
- `Dr. Jensik` (person)
- `Dr. Roch` (person)
- `Dagobert Schoeler` (person)
- `Hopmeier & Wagner Rechtsanwälte OG` (organisation)
- `Peter Cuypers` (person)
- `Landesgerichts Feldkirch` (organisation)
- `Bezirksgerichts Bludenz` (organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/3Ob185_22k`) (sent_id: `deanon_260716_TRAIN/3Ob185_22k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn und die Hofrätinnen Dr. Weixelbraun-Mohr, Dr. Kodek und Mag. Wessely-Kristöfel als weitere Richter in der Exekutionssache der betreibenden Partei Dr. Moritz Absmeier, vertreten durch Dr. Martin Neuwirth, Dr. Alexander Neurauter, Rechtsanwälte in Wien, gegen die verpflichtete Partei DENU Immobilien GmbH, Gürtel 12, 5145 Schmalzhofen, Österreich, vertreten durch Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH in Wien, wegen zwangsweiser Räumung, über den Revisionsrekurs der betreibenden Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 12. August 2022, GZ 40 R 104/22y-20, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 8. April 2022, GZ 49 E 11/22w-3, abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH` | `Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Höllwerth` (person)
- `Hon.-Prof. Dr. Brenn` (person)
- `Dr. Weixelbraun-Mohr` (person)
- `Dr. Kodek` (person)
- `Mag. Wessely-Kristöfel` (person)
- `Dr. Moritz Absmeier` (person)
- `Dr. Martin Neuwirth` (person)
- `Dr. Alexander Neurauter` (person)
- `DENU Immobilien GmbH` (organisation)
- `Gürtel 12, 5145 Schmalzhofen, Österreich` (address)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Innere Stadt Wien` (organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/3Ob229_14v`) (sent_id: `deanon_260716_TRAIN/3Ob229_14v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Vizepräsidentin Dr. Lovrek und die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Mag. Helga Nusskern, vertreten durch Hochleitner Rechtsanwälte GmbH in Linz, gegen die beklagte Partei Stadtgemeine Nicoletta Schusterius, vertreten durch Dr. Günther Klepp und andere Rechtsanwälte in Linz, wegen Aufhebung eines Kaufvertrags, infolge außerordentlicher Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 8. Oktober 2014, GZ 6 R 163/14d-32, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Linz vom 25. Juli 2014, GZ 2 Cg 65/13a-27, mit einer Maßgabe bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hochleitner Rechtsanwälte GmbH` | `Hochleitner Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hoch` (person)
- `Dr. Lovrek` (person)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Dr. Jensik` (person)
- `Dr. Roch` (person)
- `Mag. Helga Nusskern` (person)
- `Nicoletta Schusterius` (person)
- `Dr. Günther Klepp` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Linz` (organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/3Ob26_23d`) (sent_id: `deanon_260716_TRAIN/3Ob26_23d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Anton Reuschel, vertreten durch Mag. Christopher Schmied, Rechtsanwalt in Salzburg, gegen die beklagte Partei Marktgemeinde KommR Frieda Goetzens, vertreten durch Ebner Aichinger Guggenberger Rechtsanwälte GmbH in Salzburg, wegen Feststellung einer Dienstbarkeit und Beseitigung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 7. Dezember 2022, GZ 3 R 142/22f-17, womit das Urteil des Landesgerichts Salzburg vom 29. September 2022, GZ 9 Cg 47/22w-12, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Ebner Aichinger Guggenberger Rechtsanwälte GmbH` | `Ebner Aichinger Guggenberger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Höllwerth` (person)
- `Hon.-Prof. Dr. Brenn` (person)
- `Dr. Weixelbraun-Mohr` (person)
- `Dr. Kodek` (person)
- `Dr. Stefula` (person)
- `Anton Reuschel` (person)
- `Mag. Christopher Schmied` (person)
- `KommR Frieda Goetzens` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Salzburg` (organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/3Ob32_17b`) (sent_id: `deanon_260716_TRAIN/3Ob32_17b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Jensik und Dr. Roch und die Hofrätin Dr. Kodek als weitere Richter in der Exekutionssache der betreibenden Partei Balthasar Düppen, Italien, vertreten durch Oberhammer Rechtsanwälte GmbH in Wien, wider die verpflichtete Partei Ober Talnor gesellschaft mbH, Pesenbachtal 28, 5121 Eckldorf, Österreich, vertreten durch Dr. Daniel Charim und Mag. Jakob Charim, Rechtsanwälte in Wien, wegen (restlich) 347.093,53 EUR sA über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 7. Dezember 2016, GZ 46 R 323/16i-61, womit der Beschluss des Bezirksgerichts Josefstadt vom 24. Juni 2016, GZ 11 E 2966/11p-56, bestätigt wurde, den Beschluss gefasst:  Spruch I.Der Revisionsrekurs der verpflichteten Partei wird, soweit er die Bestätigung der Exekutionsbewilligung bekämpft, als jedenfalls unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Oberhammer Rechtsanwälte GmbH` | `Oberhammer Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hoch` (person)
- `Dr. Lovrek` (person)
- `Dr. Jensik` (person)
- `Dr. Roch` (person)
- `Dr. Kodek` (person)
- `Balthasar Düppen` (person)
- `Ober Talnor gesellschaft mbH` (organisation)
- `Pesenbachtal 28, 5121 Eckldorf, Österreich` (address)
- `Dr. Daniel Charim` (person)
- `Mag. Jakob Charim` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Josefstadt` (organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/4Nc30_22g`) (sent_id: `deanon_260716_TRAIN/4Nc30_22g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Kodek als Vorsitzenden sowie die Hofräte Dr. Schwarzenbacher und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Iris Gscheider, vertreten durch Dr. Sabine C.M. Deutsch, Rechtsanwältin in Riegersburg, gegen die beklagte Partei Mag. Annette Salzbauer, als Masseverwalter im Konkursverfahren über das Vermögen von Lynn Galleitner (AZ 26 S 10/21x des Landesgerichts für Zivilrechtssachen Graz), vertreten durch die GRAF ISOLA Rechtsanwälte GmbH in Graz, wegen Unterlassung, über den Delegierungsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der unmittelbar beim Obersten Gerichtshof eingebrachte Delegierungsantrag samt Beilagen wird dem Landesgericht für Zivilrechtssachen Graz als Erstgericht zu AZ 10 Cg 83/22z zur geschäftsordnungsgemäßen Behandlung übermittelt. Begründung:  Rechtliche Beurteilung [1]

| Predicted | Gold |
|---|---|
| `GRAF ISOLA Rechtsanwälte GmbH` | `GRAF ISOLA Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Kodek` (person)
- `Dr. Schwarzenbacher` (person)
- `MMag. Matzka` (person)
- `Iris Gscheider` (person)
- `Dr. Sabine C.M. Deutsch` (person)
- `Mag. Annette Salzbauer` (person)
- `Lynn Galleitner` (person)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)
- `Obersten Gerichtshof` (organisation)
- `Landesgericht für Zivilrechtssachen Graz` (organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/4Nc4_17a`) (sent_id: `deanon_260716_TRAIN/4Nc4_17a_4`)


HFJY Getränke Consulting, Dänemark, 2. SeeTouristik Dienstleistungen GmbH, Poysbrunner Straße 102, 4112 Rottenegg, Österreich, beide vertreten durch Graf & Pitkowitz Rechtsanwälte GmbH in Wien, gegen die Beklagten 1. Cizmeci + Janda Chemie GmbH, Lahntalweg 53, 9413 Kamp, Österreich, 2.

| Predicted | Gold |
|---|---|
| `Graf & Pitkowitz Rechtsanwälte GmbH` | `Graf & Pitkowitz Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `HFJY Getränke Consulting` (organisation)
- `SeeTouristik Dienstleistungen GmbH` (organisation)
- `Poysbrunner Straße 102, 4112 Rottenegg, Österreich` (address)
- `Cizmeci + Janda Chemie GmbH` (organisation)
- `Lahntalweg 53, 9413 Kamp, Österreich` (address)

**Example 32** (doc_id: `deanon_260716_TRAIN/4Ob100_13d`) (sent_id: `deanon_260716_TRAIN/4Ob100_13d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Verein Karen Böckel, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei Düwall + Rief Daten -Aktiengesellschaft, Gassing/Burgweg 63, 4613 Mistelbach bei Wels, Österreich, vertreten durch Raits Bleiziffer Rechtsanwälte GmbH in Salzburg, und die Nebenintervenientin auf Seiten der beklagten Partei „ Eberhard Besemer ” Linda Hukauf, vertreten durch Dr. Peter Zöchbauer und andere Rechtsanwälte in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert 36.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz vom 19. April 2013, GZ 1 R 192/12d-14, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Raits Bleiziffer Rechtsanwälte GmbH` | `Raits Bleiziffer Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schenk` (person)
- `Dr. Vogel` (person)
- `Dr. Jensik` (person)
- `Dr. Musger` (person)
- `Dr. Schwarzenbacher` (person)
- `Karen Böckel` (person)
- `Kosesnik-Wehrle & Langer Rechtsanwälte KG` (organisation)
- `Düwall + Rief Daten -Aktiengesellschaft` (organisation)
- `Gassing/Burgweg 63, 4613 Mistelbach bei Wels, Österreich` (address)
- `Eberhard Besemer` (person)
- `Linda Hukauf` (person)
- `Dr. Peter Zöchbauer` (person)
- `Oberlandesgerichts Linz` (organisation)

**Example 33** (doc_id: `deanon_260716_TRAIN/4Ob119_22m`) (sent_id: `deanon_260716_TRAIN/4Ob119_22m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Kodek sowie die Hofräte Dr. Schwarzenbacher, Dr. Nowotny und Hon.-Prof. PD Dr. Rassi und die Hofrätin Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei Silvester Schusterius KG, Brunnsteinweg 3, 9602 Draschitz, Österreich, vertreten durch Dr. Franz Krainer, Rechtsanwalt in Graz, gegen die beklagte Partei TalVerlag Manufaktur GmbH, Dr. Leopold Bauer-Gasse 105, 4843 Hinterschlagen, Österreich, vertreten durch die Hohenberg Rechtsanwälte GmbH in Graz, wegen 84.521,61 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz vom 12. Mai 2022, GZ 5 R 170/21s-33, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hohenberg Rechtsanwälte GmbH` | `Hohenberg Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Kodek` (person)
- `Dr. Schwarzenbacher` (person)
- `Dr. Nowotny` (person)
- `Hon.-Prof. PD Dr. Rassi` (person)
- `Mag. Istjan, LL.M.` (person)
- `Silvester Schusterius` (person)
- `Brunnsteinweg 3, 9602 Draschitz, Österreich` (address)
- `Dr. Franz Krainer` (person)
- `TalVerlag Manufaktur GmbH` (organisation)
- `Dr. Leopold Bauer-Gasse 105, 4843 Hinterschlagen, Österreich` (address)
- `Oberlandesgerichts Graz` (organisation)

**Example 34** (doc_id: `deanon_260716_TRAIN/4Ob142_21t`) (sent_id: `deanon_260716_TRAIN/4Ob142_21t_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Hon.-Prof. PD Dr. Rassi als Vorsitzenden und die Hofräte und Hofrätinnen Dr. Schwarzenbacher, Dr. Kodek, MMag. Matzka sowie Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei Laurence Perger, vertreten durch Viehböck Breiter Schenk & Nau Rechtsanwälte OG in Mödling, gegen die beklagte Partei EIPD Chemie ges.m.b.H., Insel 21, 4840 Diesenbach, Österreich, vertreten durch Celar Senoner Weber-Wilfert Rechtsanwälte GmbH in Wien, wegen Herausgabe eines Buchauszugs (Streitwert 4.000 EUR) und 41.049,64 EUR sA, über die außerordentliche Revision der klagenden Partei, gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Mai 2021, GZ 5 R 162/20k-66, mit dem das Urteil des Handelsgerichts Wien vom 30. September 2020, GZ 48 Cg 28/19f-59, bestätigt wurde, beschlossen und zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Weber-Wilfert Rechtsanwälte GmbH` | `Weber-Wilfert Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. PD Dr. Rassi` (person)
- `Dr. Schwarzenbacher` (person)
- `Dr. Kodek` (person)
- `MMag. Matzka` (person)
- `Mag. Istjan, LL.M.` (person)
- `Laurence Perger` (person)
- `Viehböck Breiter Schenk & Nau Rechtsanwälte OG` (organisation)
- `EIPD Chemie ges.m.b.H.` (organisation)
- `Insel 21, 4840 Diesenbach, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 35** (doc_id: `deanon_260716_TRAIN/4Ob201_10b`) (sent_id: `deanon_260716_TRAIN/4Ob201_10b_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Kevin Woelfel OEG, Rudolf Radinger-Straße 110o, 4623 Moostal, Österreich, vertreten durch Dr. Martin Leitner und Dr. Ralph Trischler, Rechtsanwälte in Wien, gegen die beklagte Partei Rätz Handel GmbH, Schögglstraße 25, 4085 Dankmairing, Österreich, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung, Rechnungslegung, Schadenersatz und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 36.000 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 27. September 2010, GZ 1 R 192/10b-13, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß Der Antrag auf Zuspruch der Kosten der Revisionsrekursbeantwortung wird gemäß § 508a Abs 2 Satz 2 und § 521a Abs 2 ZPO abgewiesen.

| Predicted | Gold |
|---|---|
| `Bichler Zrzavy Rechtsanwälte GmbH` | `Bichler Zrzavy Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schenk` (person)
- `Dr. Vogel` (person)
- `Dr. Jensik` (person)
- `Dr. Musger` (person)
- `Dr. Schwarzenbacher` (person)
- `Kevin Woelfel` (person)
- `Rudolf Radinger-Straße 110o, 4623 Moostal, Österreich` (address)
- `Dr. Martin Leitner` (person)
- `Dr. Ralph Trischler` (person)
- `Rätz Handel GmbH` (organisation)
- `Schögglstraße 25, 4085 Dankmairing, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)

**Example 36** (doc_id: `deanon_260716_TRAIN/4Ob64_18t`) (sent_id: `deanon_260716_TRAIN/4Ob64_18t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Vogel als Vorsitzenden sowie die Hofräte Dr. Schwarzenbacher, Hon.-Prof. Dr. Brenn, Dr. Rassi und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Mag. Florentin Jakobautzki, vertreten durch die Konrad Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Lischke&Rohleff Solar AG, Volkshausplatz 46, 3830 Pyhra, Österreich, vertreten durch die Binder Grösswang Rechtsanwälte GmbH in Wien, wegen 106.196,74 EUR sA und Feststellung (Streitwert 156.303,26 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 13. Oktober 2017, GZ 129 R 24/17y-24, womit das Urteil des Handelsgerichts Wien vom 2. August 2017, GZ 10 Cg 1/16a-19, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Konrad Rechtsanwälte GmbH` | `Konrad Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Vogel` (person)
- `Dr. Schwarzenbacher` (person)
- `Hon.-Prof. Dr. Brenn` (person)
- `Dr. Rassi` (person)
- `MMag. Matzka` (person)
- `Mag. Florentin Jakobautzki` (person)
- `Lischke&Rohleff Solar AG` (organisation)
- `Volkshausplatz 46, 3830 Pyhra, Österreich` (address)
- `Binder Grösswang Rechtsanwälte GmbH` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 37** (doc_id: `deanon_260716_TRAIN/4Ob9_20g`) (sent_id: `deanon_260716_TRAIN/4Ob9_20g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Vogel als Vorsitzenden und die Hofräte Dr. Schwarzenbacher, Hon.-Prof. Dr. Brenn, Priv.-Doz. Dr. Rassi und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Ingrid Marke, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1) ZTYW Solar Vertrieb GmbH, Hans-Woerle-Weg 13, 4852 Gahberg, Österreich, und 2) Hoch Fenfurtmon Systeme AG, Raxer Straße 24, 8952 Kienach, Österreich, beide vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 11.091,23 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 6. November 2019, GZ 2 R 158/19x-27, mit dem das Urteil des Landesgerichts Linz vom 29. August 2019, GZ 36 Cg 14/18h-22, bestätigt wurde, den Beschluss gefasst:  Spruch I. Das Revisionsverfahren zu 4 Ob 9/20g wird bis zur Vorabentscheidung des Gerichtshofs der Europäischen Union über das Vorabentscheidungsersuchen des Obersten Gerichtshofs vom 17.

| Predicted | Gold |
|---|---|
| `Poduschka Anwaltsgesellschaft mbH` | `Poduschka Anwaltsgesellschaft mbH` |
| `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` | `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Vogel` (person)
- `Dr. Schwarzenbacher` (person)
- `Hon.-Prof. Dr. Brenn` (person)
- `Priv.-Doz. Dr. Rassi` (person)
- `MMag. Matzka` (person)
- `Ingrid Marke` (person)
- `ZTYW Solar Vertrieb GmbH` (organisation)
- `Hans-Woerle-Weg 13, 4852 Gahberg, Österreich` (address)
- `Hoch Fenfurtmon Systeme AG` (organisation)
- `Raxer Straße 24, 8952 Kienach, Österreich` (address)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Linz` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 38** (doc_id: `deanon_260716_TRAIN/5Ob102_24x`) (sent_id: `deanon_260716_TRAIN/5Ob102_24x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei ÖkR KzlR Sonja Doganoglu, wider die beklagte Partei Stoeberl Bau AG, Bernhard-Paumgartner-Weg 41, 3233 Hohenbrand, Österreich, Deutschland vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 13.607,40 EUR sA und Feststellung über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Ried im Innkreis als Berufungsgericht vom 13. März 2024, GZ 18 R 2/24k-29, mit dem das Urteil des Bezirksgerichts Schärding vom 6. November 2023, GZ 2 C 478/20g-24, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` | `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Jensik` (person)
- `Mag. Wurzer` (person)
- `Mag. Painsi` (person)
- `Dr. Weixelbraun-Mohr` (person)
- `Dr. Steger` (person)
- `ÖkR KzlR Sonja Doganoglu` (person)
- `Stoeberl Bau AG` (organisation)
- `Bernhard-Paumgartner-Weg 41, 3233 Hohenbrand, Österreich` (address)
- `Landesgerichts Ried im Innkreis` (organisation)
- `Bezirksgerichts Schärding` (organisation)

**Example 39** (doc_id: `deanon_260716_TRAIN/5Ob141_23f`) (sent_id: `deanon_260716_TRAIN/5Ob141_23f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Svenja Brochtrup, vertreten durch Poduschka Partner AnwaltsGmbH in Linz, gegen die beklagte Partei EnnsFinanzen AG, Bartlstraße 9, 8490 Zelting, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 19.600 EUR sA über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 22. Mai 2023, GZ 12 R 6/23y-34, mit dem das Urteil des Landesgerichts Wels vom 11. Jänner 2023, GZ 8 Cg 29/20s-29, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` | `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Jensik` (person)
- `Mag. Wurzer` (person)
- `Mag. Painsi` (person)
- `Dr. Weixelbraun-Mohr` (person)
- `Dr. Steger` (person)
- `Svenja Brochtrup` (person)
- `EnnsFinanzen AG` (organisation)
- `Bartlstraße 9, 8490 Zelting, Österreich` (address)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Wels` (organisation)

**Example 40** (doc_id: `deanon_260716_TRAIN/5Ob177_20w`) (sent_id: `deanon_260716_TRAIN/5Ob177_20w_5`)


MedR Heinz Tahir, vertreten durch die Schmid & Horn Rechtsanwälte GmbH, Graz, gegen die Antragsgegner 1. Arch.

| Predicted | Gold |
|---|---|
| `Schmid & Horn Rechtsanwälte GmbH` | `Schmid & Horn Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `MedR Heinz Tahir` (person)

**Example 41** (doc_id: `deanon_260716_TRAIN/5Ob259_15x`) (sent_id: `deanon_260716_TRAIN/5Ob259_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers Shoshana Dimpfel, vertreten durch Hofbauer & Wagner Rechtsanwälte KG in St. Pölten, gegen den Antragsgegner Adolf Beehr, vertreten durch Dr. Franz Gütlbauer, Dr. Siegfried Sieghartsleitner, Dr. Michael Pichlmair, Rechtsanwälte in Wels, wegen § 8 Abs 2 MRG (hier: wegen Abänderung des Sachbeschlusses des Bezirksgerichts Traun vom 18. März 2014, GZ 17 Msch 6/13m-8) über den „Rekurs“ des Antragsgegners gegen den Beschluss des Landesgerichts Linz als Rekursgericht vom 8. Oktober 2015, GZ 14 R 56/15a-22, mit dem der Beschluss des Bezirksgerichts Traun vom 25. Februar 2015, GZ 17 Msch 6/13m-18, bestätigt wurde, den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hofbauer & Wagner Rechtsanwälte KG` | `Hofbauer & Wagner Rechtsanwälte KG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hradil` (person)
- `Dr. Höllwerth` (person)
- `Dr. Grohmann` (person)
- `Mag. Wurzer` (person)
- `Mag. Painsi` (person)
- `Shoshana Dimpfel` (person)
- `Adolf Beehr` (person)
- `Dr. Franz Gütlbauer` (person)
- `Dr. Siegfried Sieghartsleitner` (person)
- `Dr. Michael Pichlmair` (person)
- `Bezirksgerichts Traun` (organisation)
- `Landesgerichts Linz` (organisation)
- `Bezirksgerichts Traun` (organisation)

**Example 42** (doc_id: `deanon_260716_TRAIN/5Ob71_24p`) (sent_id: `deanon_260716_TRAIN/5Ob71_24p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Mag. Wurzer als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Painsi, Dr. Weixelbraun-Mohr, Dr. Steger und Dr. Pfurtscheller als weitere Richter in der Rechtssache der klagenden Partei Josefine Fretschner, vertreten durch die Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei AlpenDerlogverEvent GmbH, Am Kröpflmühlerberg 93, 3925 Kleinpertenschlag, Österreich, vertreten durch die Wolf Theiss Rechtsanwälte GmbH & Co KG in Wien, wegen 7.140 EUR und Feststellung (Streitwert 2.000 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Steyr als Berufungsgericht vom 8. Februar 2024, GZ 1 R 120/23z-43, mit dem das Urteil des Bezirksgerichts Steyr vom 28. September 2023, GZ 2 C 288/21x-39, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das Verfahren über die Revision der beklagten Partei wird bis zur Entscheidung des Gerichtshofs der Europäischen Union (EuGH) über die Vorabentscheidungsersuchen des Landgerichts Ravensburg (Deutschland) vom 9. November 2023, Rechtssache C-666/23, vom 9. November 2023, Rechtssache C-667/23, und vom 15. November 2023, Rechtssache C-668/23, unterbrochen.

| Predicted | Gold |
|---|---|
| `Poduschka Anwaltsgesellschaft mbH` | `Poduschka Anwaltsgesellschaft mbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mag. Wurzer` (person)
- `Mag. Painsi` (person)
- `Dr. Weixelbraun-Mohr` (person)
- `Dr. Steger` (person)
- `Dr. Pfurtscheller` (person)
- `Josefine Fretschner` (person)
- `AlpenDerlogverEvent GmbH` (organisation)
- `Am Kröpflmühlerberg 93, 3925 Kleinpertenschlag, Österreich` (address)
- `Wolf Theiss Rechtsanwälte GmbH & Co KG` (organisation)
- `Landesgerichts Steyr` (organisation)
- `Bezirksgerichts Steyr` (organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/6Ob105_20i`) (sent_id: `deanon_260716_TRAIN/6Ob105_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden, die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Jaden Ince, vertreten durch Mag. Erwin Falkner, Rechtsanwalt in Wien, gegen die beklagte Partei R. Enns Verfurt GmbH, Greifenberg 38, 4972 Windhag, Österreich, vertreten durch Hoffmann & Sykora Rechtsanwälte KG in Tulln, wegen 6.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts St. Pölten als Berufungsgericht vom 13. November 2019, GZ 21 R 208/19z-53, womit über Berufung der klagenden Partei das Urteil des Bezirksgerichts Tulln vom 23. Juni 2019, GZ 11 C 276/18p-49, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Hoffmann & Sykora Rechtsanwälte KG` | `Hoffmann & Sykora Rechtsanwälte KG` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schramm` (person)
- `Hon.-Prof. Dr. Gitschthaler` (person)
- `Univ.-Prof. Dr. Kodek` (person)
- `Dr. Nowotny` (person)
- `Dr. Faber` (person)
- `Jaden Ince` (person)
- `Mag. Erwin Falkner` (person)
- `Enns Verfurt GmbH` (organisation)
- `Greifenberg 38, 4972 Windhag, Österreich` (address)
- `Landesgerichts St. Pölten` (organisation)
- `Bezirksgerichts Tulln` (organisation)

**Example 44** (doc_id: `deanon_260716_TRAIN/6Ob10_22x`) (sent_id: `deanon_260716_TRAIN/6Ob10_22x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Nowotny, Dr. Hofer-Zeni-Rennhofer, Dr. Faber und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Tralog-KI Versicherungs AG, Adolf Schwayer-Gasse 22, 3371 Hofa, Österreich, vertreten durch Musey Rechtsanwalt GmbH in Salzburg, gegen die beklagte Partei WaldRecycling GmbH, Georg-Rendl-Weg 28, 9065 Ebenthal, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 7.246.839 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 1. Dezember 2021, GZ 2 R 165/21d-49, womit das Teil- und Zwischenurteil des Landesgerichts Salzburg vom 6. September 2021, GZ 6 Cg 16/20m-45, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` | `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Gitschthaler` (person)
- `Dr. Nowotny` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Faber` (person)
- `Mag. Pertmayr` (person)
- `Tralog-KI Versicherungs AG` (organisation)
- `Adolf Schwayer-Gasse 22, 3371 Hofa, Österreich` (address)
- `Musey Rechtsanwalt GmbH` (organisation)
- `WaldRecycling GmbH` (organisation)
- `Georg-Rendl-Weg 28, 9065 Ebenthal, Österreich` (address)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Salzburg` (organisation)

**Example 45** (doc_id: `deanon_260716_TRAIN/6Ob169_12i`) (sent_id: `deanon_260716_TRAIN/6Ob169_12i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Pimmer als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Dr. Schramm, Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Seesteincon-Transport GmbH, Wildbacher Straße 174, 3623 Bernhards, Österreich, vertreten durch List Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Heimnor GmbH, Am Johannisgraben 44, 8200 Albersdorf, Österreich, vertreten durch Dr. Christoph Brenner - Mag. Severin Perschl Rechtsanwälte OG in Krems, wegen 7.641,30 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Korneuburg als Berufungsgericht vom 16. Februar 2012, GZ 21 R 262/11v-50, womit das Urteil des Bezirksgerichts Gänserndorf vom 2. August 2011, GZ 12 C 1036/10h-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `List Rechtsanwälte GmbH` | `List Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Pimmer` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Schramm` (person)
- `Dr. Gitschthaler` (person)
- `Univ.-Prof. Dr. Kodek` (person)
- `Dr. Nowotny` (person)
- `Seesteincon-Transport GmbH` (organisation)
- `Wildbacher Straße 174, 3623 Bernhards, Österreich` (address)
- `Heimnor GmbH` (organisation)
- `Am Johannisgraben 44, 8200 Albersdorf, Österreich` (address)
- `Dr. Christoph Brenner` (person)
- `Mag. Severin Perschl Rechtsanwälte OG` (organisation)
- `Landesgerichts Korneuburg` (organisation)
- `Bezirksgerichts Gänserndorf` (organisation)

**Example 46** (doc_id: `deanon_260716_TRAIN/6Ob18_20w`) (sent_id: `deanon_260716_TRAIN/6Ob18_20w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden, durch die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny sowie durch die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Iris Blumstock, vertreten durch Dorda Rechtsanwälte GmbH in Wien, wider die beklagte Partei Dr. Peter Temir, vertreten durch Dr. Thomas Weber, Rechtsanwalt in Baden, und den Nebenintervenienten auf Seiten der beklagten Partei Dr. Emanuela Brinkhuis, vertreten durch Prettenhofer Raimann Pérez Rechtsanwaltspartnerschaft in Wien, wegen Löschung und Unterlassung, über die außerordentlichen Revisionen der beklagten Partei und des Nebenintervenienten gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 19. November 2019, GZ 58 R 58/19f-36, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentlichen Revisionen werden gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dorda Rechtsanwälte GmbH` | `Dorda Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schramm` (person)
- `Dr. Gitschthaler` (person)
- `Univ.-Prof. Dr. Kodek` (person)
- `Dr. Nowotny` (person)
- `Dr. Faber` (person)
- `Iris Blumstock` (person)
- `Dr. Peter Temir` (person)
- `Dr. Thomas Weber` (person)
- `Dr. Emanuela Brinkhuis` (person)
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 47** (doc_id: `deanon_260716_TRAIN/6Ob231_24z`) (sent_id: `deanon_260716_TRAIN/6Ob231_24z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Hofer-Zeni-Rennhofer als Vorsitzende sowie die Hofrätinnen und Hofräte Hon.-Prof. Dr. Faber, Mag. Pertmayr, Dr. Weber und Mag. Nigl LL.M. als weitere Richter in der Rechtssache der klagenden Partei Ing. Tiffany Jähncke, vertreten durch Poduschka Partner Anwaltsgesellschaft mbH in Linz, wider die beklagte Partei Sudconbach-Bau AG, Hart, Akazienstraße 15v, 4064 Oftering, Österreich, Deutschland, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 9.600 EUR sA, im Verfahren über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Linz als Berufungsgericht vom 7. Oktober 2024, GZ 6 R 57/24b-31, womit das Urteil des Bezirksgerichts Traun vom 16. Februar 2024, GZ 2 C 198/23z-22, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei vom 9. Dezember 2025 auf Fortsetzung des Verfahrens wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Poduschka Partner Anwaltsgesellschaft mbH` | `Poduschka Partner Anwaltsgesellschaft mbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Hon.-Prof. Dr. Faber` (person)
- `Mag. Pertmayr` (person)
- `Dr. Weber` (person)
- `Mag. Nigl` (person)
- `Ing. Tiffany Jähncke` (person)
- `Sudconbach-Bau AG` (organisation)
- `Hart, Akazienstraße 15v, 4064 Oftering, Österreich` (address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Linz` (organisation)
- `Bezirksgerichts Traun` (organisation)

**Example 48** (doc_id: `deanon_260716_TRAIN/6Ob233_20p`) (sent_id: `deanon_260716_TRAIN/6Ob233_20p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden, die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Firmenbuchsache der RheinLebensmittel Systeme GmbH, FN FN982022c, wegen § 10 Abs 2 FBG, über den Revisionsrekurs des Österreichischen Verbandes Gemeinnütziger Bauvereinigungen Revisionsverband, 1010 Wien, Bösendorferstraße 7, vertreten durch KWR Karasek Wietrzyk Rechtsanwälte GmbH in Wien, gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 3. September 2020, GZ 6 R 158/20d-6, womit der Rekurs gegen den Beschluss des Handelsgerichts Wien vom 20. Juli 2020, GZ 72 Fr 3266/20f-3, zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `KWR Karasek Wietrzyk Rechtsanwälte GmbH` | `KWR Karasek Wietrzyk Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schramm` (person)
- `Hon.-Prof. Dr. Gitschthaler` (person)
- `Univ.-Prof. Dr. Kodek` (person)
- `Dr. Nowotny` (person)
- `Dr. Faber` (person)
- `RheinLebensmittel Systeme GmbH` (organisation)
- `FN982022c` (business_register_number)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 49** (doc_id: `deanon_260716_TRAIN/7Ob138_16v`) (sent_id: `deanon_260716_TRAIN/7Ob138_16v_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Höllwerth als Vorsitzenden und durch die Hofräte Mag. Wurzer, Mag. Malesich, Dr. Hofer-Zeni-Rennhofer und Dr. Singer als weitere Richter in der Rechtssache der gefährdeten Partei Theobald Schomäker, vertreten durch Suppan & Spiegl Rechtsanwälte GmbH in Wien, gegen den Gegner der gefährdeten Partei Berthold Hömann, vertreten durch Dr. Paul Luiki, Rechtsanwalt in Wien, dieser vertreten durch Dr. Romana Zeh-Gindl, Rechtsanwältin in Wien, wegen Erlassung einer einstweiligen Verfügung, infolge des außerordentlichen Revisionsrekurses des Gegners der gefährdeten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 30. Mai 2016, GZ 46 R 177/16v-26, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 19. Jänner 2016, GZ 26 C 1563/15w-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Akten werden dem Rekursgericht zur Ergänzung seiner Entscheidung durch den Ausspruch über den Wert seines Entscheidungsgegenstands übermittelt.  Text Begründung: Das Erstgericht erließ die nach § 382g EO beantragte einstweilige Verfügung zur Sicherung der auf §§ 16, 1328a ABGB und § 1330 ABGB gestützten Unterlassungsansprüche.

| Predicted | Gold |
|---|---|
| `Suppan & Spiegl Rechtsanwälte GmbH` | `Suppan & Spiegl Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Höllwerth` (person)
- `Mag. Wurzer` (person)
- `Mag. Malesich` (person)
- `Dr. Hofer-Zeni-Rennhofer` (person)
- `Dr. Singer` (person)
- `Theobald Schomäker` (person)
- `Berthold Hömann` (person)
- `Dr. Paul Luiki` (person)
- `Dr. Romana Zeh-Gindl` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Innere Stadt Wien` (organisation)

**Example 50** (doc_id: `deanon_260716_TRAIN/7Ob157_19t`) (sent_id: `deanon_260716_TRAIN/7Ob157_19t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Wolf Makrigiannis, LLB LTD, Marienstraße 101, 4091 Wenzelberg, Österreich, vertreten durch Hasch & Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei MittelGarten Werke GmbH, Trappelgasse 16, 3361 Mauer bei Amstetten, Österreich, vertreten durch Dr. Dominik Schärmer, Rechtsanwalt in Wien, wegen 30.000 EUR, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 12. Juni 2019, GZ 6 R 46/19f-22, mit dem das Zwischenurteil des Landesgerichts Linz vom 26. Februar 2019, GZ 63 Cg 37/18i-18, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hasch & Partner Anwaltsgesellschaft mbH` | `Hasch & Partner Anwaltsgesellschaft mbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Hon.-Prof. Dr. Höllwerth` (person)
- `Dr. Solé` (person)
- `Mag. Malesich` (person)
- `MMag. Matzka` (person)
- `Wolf Makrigiannis, LLB` (person)
- `Marienstraße 101, 4091 Wenzelberg, Österreich` (address)
- `MittelGarten Werke GmbH` (organisation)
- `Trappelgasse 16, 3361 Mauer bei Amstetten, Österreich` (address)
- `Dr. Dominik Schärmer` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Linz` (organisation)

**Example 51** (doc_id: `deanon_260716_TRAIN/7Ob193_21i`) (sent_id: `deanon_260716_TRAIN/7Ob193_21i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätin und Hofräte Mag. Dr. Wurdinger, Mag. Malesich, MMag. Matzka und Dr. Weber als weitere Richter in der Rechtssache der klagenden Partei Zerweckh & Braunmöller Touristik GmbH, Albert-Böhler-Gasse 8, 9832 Stieflberg, Österreich, vertreten durch Schmid & Horn Rechtsanwälte GmbH in Graz, gegen die beklagte Partei VJHV Event Werke -AG, Oberpfälzer Weg 3, 4733 Eitzenberg, Österreich, vertreten durch Dr. Wolfgang Muchitsch, Rechtsanwalt in Graz, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 7. Oktober 2021, GZ 2 R 175/21d-15, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Schmid & Horn Rechtsanwälte GmbH` | `Schmid & Horn Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Mag. Dr. Wurdinger` (person)
- `Mag. Malesich` (person)
- `MMag. Matzka` (person)
- `Dr. Weber` (person)
- `Zerweckh & Braunmöller Touristik GmbH` (organisation)
- `Albert-Böhler-Gasse 8, 9832 Stieflberg, Österreich` (address)
- `VJHV Event Werke -AG` (organisation)
- `Oberpfälzer Weg 3, 4733 Eitzenberg, Österreich` (address)
- `Dr. Wolfgang Muchitsch` (person)
- `Oberlandesgerichts Graz` (organisation)

**Example 52** (doc_id: `deanon_260716_TRAIN/7Ob36_25g`) (sent_id: `deanon_260716_TRAIN/7Ob36_25g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Malesich, Dr. Weber, Mag. Fitz und Mag. Jelinek als weitere Richter in der Rechtssache der klagenden Partei Gundula Aichmann, vertreten durch Poduschka Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Plönnigs Technik AG, Wieden 35, 3390 Spielberg, Österreich, vertreten durch Themmer, Toth & Partner Rechtsanwälte GmbH in Wien, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 28. November 2024, GZ 1 R 124/24t-14, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 27. Juni 2024, GZ 21 C 604/23m-10, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Poduschka Partner Anwaltsgesellschaft mbH` | `Poduschka Partner Anwaltsgesellschaft mbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Solé` (person)
- `Mag. Malesich` (person)
- `Dr. Weber` (person)
- `Mag. Fitz` (person)
- `Mag. Jelinek` (person)
- `Gundula Aichmann` (person)
- `Plönnigs Technik AG` (organisation)
- `Wieden 35, 3390 Spielberg, Österreich` (address)
- `Themmer, Toth & Partner Rechtsanwälte GmbH` (organisation)
- `Handelsgerichts Wien` (organisation)
- `Bezirksgerichts für Handelssachen Wien` (organisation)

**Example 53** (doc_id: `deanon_260716_TRAIN/7Ob54_20x`) (sent_id: `deanon_260716_TRAIN/7Ob54_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende sowie die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Techn R Ramona Rössler, vertreten durch Mag. Astrid Roblyek, Rechtsanwältin in Klagenfurt am Wörthersee, gegen die beklagte Partei ZED Planung AG Haberditzlgasse 29, 9341 Kreuth, Österreich, vertreten durch Jarolim Partner Rechtsanwälte GmbH in Wien, wegen 7.339,70 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 31. Oktober 2019, GZ 4 R 325/19i-15, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 15. Juli 2019, GZ 15 C 998/18y-11, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Jarolim Partner Rechtsanwälte GmbH` | `Jarolim Partner Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Hon.-Prof. Dr. Höllwerth` (person)
- `Dr. Solé` (person)
- `Mag. Malesich` (person)
- `MMag. Matzka` (person)
- `Techn R Ramona Rössler` (person)
- `Mag. Astrid Roblyek` (person)
- `ZED Planung AG` (organisation)
- `Haberditzlgasse 29, 9341 Kreuth, Österreich` (address)
- `Landesgerichts Klagenfurt` (organisation)
- `Bezirksgerichts Klagenfurt` (organisation)

**Example 54** (doc_id: `deanon_260716_TRAIN/7Ob85_15y`) (sent_id: `deanon_260716_TRAIN/7Ob85_15y_6`)


Renzlhausen 24, 6553 See, Österreich, vertreten durch Dorda Brugger Jordis Rechtsanwälte GmbH in Wien, wegen 7.523,16 EUR sA, über den Rekurs der erstbeklagten Partei gegen den Beschluss des Handelsgerichts Wien als Berufungsgericht vom 19. Februar 2015, GZ 1 R 6/15a-49, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 29. September 2014, GZ 13 C 134/10s-45, hinsichtlich der erstbeklagten Partei aufgehoben wurde, den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dorda Brugger Jordis Rechtsanwälte GmbH` | `Dorda Brugger Jordis Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Handelsgerichts Wien` (organisation)
- `Bezirksgerichts für Handelssachen Wien` (organisation)

**Example 55** (doc_id: `deanon_260716_TRAIN/7Ob94_20d`) (sent_id: `deanon_260716_TRAIN/7Ob94_20d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Hon.-Prof. Dr. Höllwerth, Dr. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Mag. Juliana Mündelein, vertreten durch Brand Rechtsanwälte GmbH in Wien, gegen die beklagte Partei ACBK Elektro Solutions AG, Schwarzenseer Straße 25, 9560 Steuerberg, Österreich, vertreten durch Dorda Rechtsanwälte GmbH in Wien, wegen 16.354,47 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 31. Jänner 2020, GZ 1 R 120/19b-21, womit das Urteil des Handelsgerichts Wien vom 22. Juli 2019, GZ 16 Cg 50/18d-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Brand Rechtsanwälte GmbH` | `Brand Rechtsanwälte GmbH` |
| `Dorda Rechtsanwälte GmbH` | `Dorda Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Kalivoda` (person)
- `Hon.-Prof. Dr. Höllwerth` (person)
- `Dr. Solé` (person)
- `Mag. Malesich` (person)
- `MMag. Matzka` (person)
- `Mag. Juliana Mündelein` (person)
- `ACBK Elektro Solutions AG` (organisation)
- `Schwarzenseer Straße 25, 9560 Steuerberg, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)
- `Handelsgerichts Wien` (organisation)

**Example 56** (doc_id: `deanon_260716_TRAIN/8Ob39_24d`) (sent_id: `deanon_260716_TRAIN/8Ob39_24d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Tarmann-Prentner als Vorsitzende sowie die Hofräte MMag. Matzka, Dr. Stefula, Dr. Thunhart und Mag. Dr. Sengstschmid als weitere Richter in der Rechtssache der klagenden Partei Helena Seuboth, vertreten durch Mag. Dieter Koch, Rechtsanwalt in Bruck an der Mur, gegen die beklagte Partei Springl Technik GmbH Josef-Weber-Straße 87h, 2565 Schwechatbach, Österreich, vertreten durch die DORDA Rechtsanwälte GmbH in Wien, wegen 112.655,74 EUR sA, über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. Februar 2024, GZ 2 R 8/24z-20.2, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `DORDA Rechtsanwälte GmbH` | `DORDA Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Tarmann-Prentner` (person)
- `MMag. Matzka` (person)
- `Dr. Stefula` (person)
- `Dr. Thunhart` (person)
- `Mag. Dr. Sengstschmid` (person)
- `Helena Seuboth` (person)
- `Mag. Dieter Koch` (person)
- `Springl Technik GmbH` (organisation)
- `Josef-Weber-Straße 87h, 2565 Schwechatbach, Österreich` (address)
- `Oberlandesgerichts Graz` (organisation)

**Example 57** (doc_id: `deanon_260716_TRAIN/8ObA10_12x`) (sent_id: `deanon_260716_TRAIN/8ObA10_12x_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Spenling als Vorsitzenden, die Hofräte Hon.-Prof. Dr. Kuras und Mag. Ziegelbauer sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner und Mag. Manuela Majeranowski als weitere Richter in der Arbeitsrechtssache der klagenden Partei Techn R Laurin Tommke, vertreten durch Hasch & Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Zorlex Verlag Gesellschaft mbH, Poeschlstraße 16, 4904 Hippelsberg, Österreich, vertreten durch Mag. Klaus F. Lughofer LLM, Rechtsanwalt in Linz, wegen Feststellung (Streitwert: 30.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. November 2011, GZ 11 Ra 92/11w-10, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Linz als Arbeits- und Sozialgericht vom 31. August 2011, GZ 11 Cga 101/11d-5, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Hasch & Partner Anwaltsgesellschaft mbH` | `Hasch & Partner Anwaltsgesellschaft mbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Spenling` (person)
- `Hon.-Prof. Dr. Kuras` (person)
- `Mag. Ziegelbauer` (person)
- `Mag. Dr. Rolf Gleißner` (person)
- `Mag. Manuela Majeranowski` (person)
- `Techn R Laurin Tommke` (person)
- `Zorlex Verlag Gesellschaft mbH` (organisation)
- `Poeschlstraße 16, 4904 Hippelsberg, Österreich` (address)
- `Mag. Klaus F. Lughofer LLM` (person)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Linz` (organisation)

**Example 58** (doc_id: `deanon_260716_TRAIN/9Ob10_19i`) (sent_id: `deanon_260716_TRAIN/9Ob10_19i_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Dehn, Dr. Hargassner, Mag. Korn und Dr. Stefula in der Rechtssache der klagenden Partei Oneseit Garten GmbH, Stephanieweg 12, 4901 Hub, Österreich, vertreten durch Partnerschaft Schuppich Sporn & Winischhofer, Rechtsanwälte in Wien, gegen die beklagte Partei Brucknor-Planung GmbH, Tadtner Weg 4, 5133 Dick, Österreich, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, wegen 6.265 EUR sA, über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Salzburg als Berufungsgericht vom 29. November 2018, GZ 53 R 212/18k-19, mit dem der Berufung der klagenden Partei gegen das Urteil des Bezirksgerichts Salzburg vom 25. Juni 2018, GZ 17 C 965/17a-15, Folge gegeben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Vavrovsky Heine Marth Rechtsanwälte GmbH` | `Vavrovsky Heine Marth Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Dehn` (person)
- `Dr. Hargassner` (person)
- `Mag. Korn` (person)
- `Dr. Stefula` (person)
- `Oneseit Garten GmbH` (organisation)
- `Stephanieweg 12, 4901 Hub, Österreich` (address)
- `Partnerschaft Schuppich Sporn & Winischhofer, Rechtsanwälte` (organisation)
- `Brucknor-Planung GmbH` (organisation)
- `Tadtner Weg 4, 5133 Dick, Österreich` (address)
- `Landesgerichts Salzburg` (organisation)
- `Bezirksgerichts Salzburg` (organisation)

**Example 59** (doc_id: `deanon_260716_TRAIN/9Ob41_14s`) (sent_id: `deanon_260716_TRAIN/9Ob41_14s_4`)


OStR OMedR Gabriel Mittermiller, vertreten durch Mag. Petra Trauntschnig, Rechtsanwältin in Wien, gegen die beklagte Partei Allar Recycling GmbH, Eduardgasse 9, 5360 Rußbach, Österreich, vertreten durch Köhler Draskovits Unger Rechtsanwälte GmbH in Wien, wegen Wiederherstellung (Streitwert: 35.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. April 2014, GZ 15 R 35/14y-22, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Draskovits Unger Rechtsanwälte GmbH` | `Draskovits Unger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `OStR OMedR Gabriel Mittermiller` (person)
- `Mag. Petra Trauntschnig` (person)
- `Allar Recycling GmbH` (organisation)
- `Eduardgasse 9, 5360 Rußbach, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)

**Example 60** (doc_id: `deanon_260716_TRAIN/9Ob65_22g`) (sent_id: `deanon_260716_TRAIN/9Ob65_22g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende, die Hofrätinnen und Hofräte des Obersten Gerichtshofs Dr. Hargassner, Mag. Korn, Dr. Thunhart und MMag. Sloboda als weitere Richter in der Rechtssache der klagenden Partei Lieselotte Mebesius, vertreten durch die Poduschka Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Ahrenhold Druck AG, Brunnbichlweg 19, 3261 Figelsberg, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 22.140,32 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 19. Juni 2019, GZ 2 R 92/19s-21, mit dem der Berufung der klagenden Partei gegen das Urteil des Landesgerichts Linz vom 12. April 2019, GZ 45 Cg 33/18v-17, nicht Folge gegeben wurde, den Beschluss gefasst:  Spruch I. Das mit Beschluss vom 15. April 2020, AZ 9 Ob 61/19i, bis zur Entscheidung des Gerichtshofs der Europäischen Union über den vom Obersten Gerichtshof am 17.

| Predicted | Gold |
|---|---|
| `Poduschka Partner Anwaltsgesellschaft mbH` | `Poduschka Partner Anwaltsgesellschaft mbH` |
| `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` | `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Fichtenau` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hargassner` (person)
- `Mag. Korn` (person)
- `Dr. Thunhart` (person)
- `MMag. Sloboda` (person)
- `Lieselotte Mebesius` (person)
- `Ahrenhold Druck AG` (organisation)
- `Brunnbichlweg 19, 3261 Figelsberg, Österreich` (address)
- `Oberlandesgerichts Linz` (organisation)
- `Landesgerichts Linz` (organisation)
- `Obersten Gerichtshof` (organisation)

**Example 61** (doc_id: `deanon_260716_TRAIN/9Ob68_22y`) (sent_id: `deanon_260716_TRAIN/9Ob68_22y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Dr. Hargassner, Mag. Korn, MMag. Sloboda und Dr. Annerl in der Rechtssache der klagenden Partei Niels Doerfel, vertreten durch Neubauer Fähnrich Rechtsanwälte GmbH & Co KG in Graz, gegen die beklagte Partei Gudrun Kovalschuk Gesellschaft m.b.H. (FN FN119735f ), FN297530m, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung und 19.490 EUR sA (Gesamtstreitwert: 19.490 EUR), über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 10. September 2019, GZ 4 R 89/19v-59, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 27. März 2019, GZ 20 Cg 15/18t-54, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Revisionsverfahren wird fortgesetzt.

| Predicted | Gold |
|---|---|
| `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` | `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` |

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
- `Neubauer Fähnrich Rechtsanwälte GmbH & Co KG` (organisation)
- `Gudrun Kovalschuk` (person)
- `FN119735f` (business_register_number)
- `FN297530m` (business_register_number)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)

**Example 62** (doc_id: `deanon_260716_TRAIN/9Ob6_24h`) (sent_id: `deanon_260716_TRAIN/9Ob6_24h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende, die Hofrätinnen und Hofräte des Obersten Gerichtshofs Mag. Ziegelbauer, Dr. Hargassner, Mag. Korn und Dr. Stiefsohn in der Rechtssache der klagenden Partei Jennifer Franckh, vertreten durch Dr. Alexander Amann LL.M., Rechtsanwalt in Gamprin-Bendern, Fürstentum Liechtenstein, gegen die beklagte Partei DrauGarten AG, Wamprechtsham 54, 4926 Untereselbach, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 2.375 EUR und Feststellung (Streitwert: 4.000 EUR), über die Revision der beklagten Partei gegen das Zwischenurteil des Landesgerichts Wels als Berufungsgericht vom 25. Oktober 2023, GZ 22 R 198/23h-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Vöcklabruck vom 15. Juni 2023, GZ 13 C 630/22f-26, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I.Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` | `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Fichtenau` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Ziegelbauer` (person)
- `Dr. Hargassner` (person)
- `Mag. Korn` (person)
- `Dr. Stiefsohn` (person)
- `Jennifer Franckh` (person)
- `Dr. Alexander Amann LL.M.` (person)
- `DrauGarten AG` (organisation)
- `Wamprechtsham 54, 4926 Untereselbach, Österreich` (address)
- `Landesgerichts Wels` (organisation)
- `Bezirksgerichts Vöcklabruck` (organisation)

**Example 63** (doc_id: `deanon_260716_TRAIN/9ObA109_13i`) (sent_id: `deanon_260716_TRAIN/9ObA109_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras, die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner und Mag. Thomas Kallab als weitere Richter in der Arbeitsrechtssache der klagenden Partei PhD Mag.a Traude Eyssner, gegen die beklagte Partei Mag. Siegmund Liepinsky, vertreten durch Hochleitner Rechtsanwälte GmbH in Linz, wegen 3.674,41 EUR brutto abzüglich 181,96 EUR netto sA (Revisionsinteresse 1.572,49 EUR brutto sA), über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 23. Mai 2013, GZ 8 Ra 36/13t-44, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Hochleitner Rechtsanwälte GmbH` | `Hochleitner Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kuras` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Dehn` (person)
- `Mag. Dr. Rolf Gleißner` (person)
- `Mag. Thomas Kallab` (person)
- `PhD Mag.a Traude Eyssner` (person)
- `Mag. Siegmund Liepinsky` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 64** (doc_id: `deanon_260716_TRAIN/9ObA124_19d`) (sent_id: `deanon_260716_TRAIN/9ObA124_19d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Hopf als Vorsitzenden, die Hofrätin Dr. Fichtenau und den Hofrat Dr. Hargassner sowie die fachkundigen Laienrichter Dr. Peter Zeitler (aus dem Kreis der Arbeitnehmer) und Angela Taschek (aus dem Kreis der Arbeitgeber) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Bartscherer und Wagenknecht Holz GmbH & Co KG, Gotthelfgasse 57 - 74, 9361 Leimersberg, Österreich, vertreten durch Burgstaller & Preyer Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Richard Armgart, vertreten durch Mag. Franjo Schruiff, LL.M. Rechtsanwalt in Wien, wegen 14.927,23 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. August 2019, GZ 10 Ra 33/19z-30, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Burgstaller & Preyer Rechtsanwälte GmbH` | `Burgstaller & Preyer Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Hopf` (person)
- `Dr. Fichtenau` (person)
- `Dr. Hargassner` (person)
- `Dr. Peter Zeitler` (person)
- `Bartscherer und Wagenknecht Holz GmbH & Co KG` (organisation)
- `Gotthelfgasse 57 - 74, 9361 Leimersberg, Österreich` (address)
- `Richard Armgart` (person)
- `Mag. Franjo Schruiff, LL.M.` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 65** (doc_id: `deanon_260716_TRAIN/9ObA150_21f`) (sent_id: `deanon_260716_TRAIN/9ObA150_21f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende, den Hofrat Mag. Ziegelbauer und die Hofrätin Mag. Korn als weitere Richter (Senat gemäß § 11a ASGG) in der Arbeitsrechtssache der klagenden Partei Priv.-Doz. Peter Dannheisser, vertreten durch Mag. German Storch, Mag. Rainer Storch, Rechtsanwälte in Linz, gegen die beklagte Partei QZTV Versand gmbh in Liquidation, St. Sebastiani-Straße 35, 9972 Virgen, Österreich, vertreten durch Herbst Kinsky Rechtsanwälte GmbH in Wien, wegen 322,06 EUR brutto sA, über die Kostenbestimmungsanträge der klagenden und der beklagten Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Kostenbestimmungsantrag wird dem Erstgericht zur Entscheidung übermittelt.  Text Begründung: [1]

| Predicted | Gold |
|---|---|
| `Herbst Kinsky Rechtsanwälte GmbH` | `Herbst Kinsky Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Fichtenau` (person)
- `Mag. Ziegelbauer` (person)
- `Mag. Korn` (person)
- `Priv.-Doz. Peter Dannheisser` (person)
- `Mag. German Storch` (person)
- `Mag. Rainer Storch` (person)
- `QZTV Versand gmbh` (organisation)
- `St. Sebastiani-Straße 35, 9972 Virgen, Österreich` (address)

**Example 66** (doc_id: `deanon_260716_TRAIN/9ObA30_23m`) (sent_id: `deanon_260716_TRAIN/9ObA30_23m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende, die Hofräte des Obersten Gerichtshofs Mag. Ziegelbauer und Dr. Hargassner sowie die fachkundigen Laienrichter Mag. Thomas Stegmüller (aus dem Kreis der Arbeitgeber) und Robert Hauser (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Immanuel Möllerke, vertreten durch bfp Brandstetter Feigl Pfleger Rechtsanwälte GmbH in Amstetten, gegen die beklagte Partei Land Mathilda Coulais, vertreten durch Mag. Thomas Reisch, Rechtsanwalt in Wien, wegen 13.868,98 EUR sA und Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. Februar 2023, GZ 7 Ra 69/22a-25, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Brandstetter Feigl Pfleger Rechtsanwälte GmbH` | `Brandstetter Feigl Pfleger Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Fichtenau` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Ziegelbauer` (person)
- `Dr. Hargassner` (person)
- `Mag. Thomas Stegmüller` (person)
- `Immanuel Möllerke` (person)
- `Mathilda Coulais` (person)
- `Mag. Thomas Reisch` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 67** (doc_id: `deanon_260716_TRAIN/9ObA82_20d`) (sent_id: `deanon_260716_TRAIN/9ObA82_20d_3`)


Kopf Der Oberste Gerichtshof hat als Revisions- und Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau und den Hofrat des Obersten Gerichtshofs Dr. Hargassner sowie die fachkundigen Laienrichter Mag. Dr. Bernhard Gruber (aus dem Kreis der Arbeitgeber) und Angela Taschek (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Marktgemeinde KommR KommR Piedro Leyendecker, vertreten durch Ehrenhöfer & Häusler Rechtsanwälte GmbH in Wiener Neustadt, gegen die beklagte Partei Milena Leinhaas, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, wegen 28.428,01 EUR sA, über den Rekurs und die außerordentliche Revision der klagenden Partei gegen den Beschluss (I.) und das Urteil (II.) des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 22. Juli 2020, GZ 9 Ra 111/19p-25, mit dem das Urteil des Landesgerichts Wiener Neustadt als Arbeits- und Sozialgericht vom 17. September 2019, GZ 9 Cga 126/18g-21, aus Anlass der Berufung der beklagten Partei hinsichtlich der Rückforderung einer Zahlung als nichtig aufgehoben und die Klage zurückgewiesen wurde und über Berufung der beklagen Partei hinsichtlich des Anspruchs nach dem OrgHG abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird teilweise Folge gegeben und der angefochtene Beschluss des Berufungsgerichts ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Kosch & Partner Rechtsanwälte GmbH` | `Kosch & Partner Rechtsanwälte GmbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hopf` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Fichtenau` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Hargassner` (person)
- `Mag. Dr. Bernhard Gruber` (person)
- `KommR KommR Piedro Leyendecker` (person)
- `Ehrenhöfer & Häusler Rechtsanwälte GmbH` (organisation)
- `Milena Leinhaas` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts Wiener Neustadt` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/1Ob12_21b`) (sent_id: `deanon_260716_TRAIN/1Ob12_21b_5`)


Zlatan Schempf, alle vertreten durch die Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte GmbH, Wien, wegen Feststellung und Räumung, über die außerordentliche Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. November 2020, GZ 2 R 122/20d-54, mit dem das Urteil des Landesgerichts Wels vom 27. Juli 2020, GZ 2 Cg 84/18g-47, in der Hauptsache bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

**False Positives:**

- `Proksch Manak Kraft Rechtsanwälte GmbH` — partial — pred is substring of gold: `Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zlatan Schempf`(person)
- `Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Wels`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/1Ob139_18z`) (sent_id: `deanon_260716_TRAIN/1Ob139_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Verena Tappendorff Inc., Sankt Andrä im Sausal 24, 8552 Aichberg, Österreich, vertreten durch Mag. Ralph Kilches, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Sabine Martinsson, als Insolvenzverwalter im Insolvenzverfahren über das Vermögen der Touristik Synberbruck GmbH, Fridau 56l, 7433 Bergwerk, Österreich, vertreten durch die Haslinger/Nagele & Partner Rechtsanwälte GmbH, Linz, wegen Feststellung einer Insolvenzforderung (Streitwert 447.352,05 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 28. Juni 2018, GZ 1 R 83/18h-8, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Nagele & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Haslinger/Nagele & Partner Rechtsanwälte GmbH`

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

**Example 2** (doc_id: `deanon_260716_TRAIN/2Ob193_23f`) (sent_id: `deanon_260716_TRAIN/2Ob193_23f_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte Hon.-Prof. PD Dr. Rassi, MMag. Sloboda, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Denise Markstaler, vertreten durch Weber Rechtsanwälte GmbH & Co KG in Wien 1, gegen die beklagte Partei Rut Adamheit, vertreten durch BEURLE Rechtsanwälte GmbH & Co KG in Linz, wegen Herausgabe (Streitwert 1.525.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2023, GZ 2 R 87/23m-32, mit dem das Urteil des Landesgerichts Salzburg vom 5. April 2023, GZ 8 Cg 9/23a-22, aufgehoben wurde zu Recht erkannt:  Spruch

**False Positives:**

- `Weber Rechtsanwälte GmbH` — partial — pred is substring of gold: `Weber Rechtsanwälte GmbH & Co KG`
- `BEURLE Rechtsanwälte GmbH` — partial — pred is substring of gold: `BEURLE Rechtsanwälte GmbH & Co KG`

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

**Example 3** (doc_id: `deanon_260716_TRAIN/2Ob89_17b`) (sent_id: `deanon_260716_TRAIN/2Ob89_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende, die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé sowie den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Dipl.-Ing. Eleonore Wagenbret, vertreten durch Posch, Schausberger & Lutz Rechtsanwälte GmbH in Wels, gegen die beklagten Parteien 1. Rudolfa Schoenmaekers, 2. Lorena Sieckkötter, und 3. TraunSanitär Dienstleistungen Versicherungs-AG, Georg Pfligersdorffer-Gasse 71, 3610 Maigen, Österreich, alle vertreten durch Mag. Dr. A. Michael Dallinger, Rechtsanwalt in Wels, wegen 187.040,19 EUR sA und Feststellung (Streitinteresse: 5.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 1. März 2017, GZ 6 R 30/17z-42, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Schausberger & Lutz Rechtsanwälte GmbH` — partial — pred is substring of gold: `Posch, Schausberger & Lutz Rechtsanwälte GmbH`

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

**Example 4** (doc_id: `deanon_260716_TRAIN/3Ob1_18w`) (sent_id: `deanon_260716_TRAIN/3Ob1_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Roch und Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Druck Steinnex GmbH, Josef-Wessely-Straße 15, 4171 Unterriedl, Österreich, vertreten durch Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG in Wien, gegen die beklagten Parteien 1.

**False Positives:**

- `Maur & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG`

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

**Example 5** (doc_id: `deanon_260716_TRAIN/3Ob209_21p`) (sent_id: `deanon_260716_TRAIN/3Ob209_21p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei APHU Solar GmbH & Co KG, Hochkreuth 39, 8144 Bischofegg, Österreich, vertreten durch DDr. Heinz Dietmar Schimanko, Rechtsanwalt in Wien, gegen die beklagte Partei Traun-Transport GmbH, Stauderstraße 30, 8200 Pircha, Österreich, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH & Co KG in Wien, wegen 7.906,82 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 7. Juni 2021, GZ 38 R 66/21v-16, mit dem das Urteil des Bezirksgerichts Favoriten vom 19. Jänner 2021, GZ 3 C 503/20f-12, abgeändert wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Bichler Zrzavy Rechtsanwälte GmbH` — partial — pred is substring of gold: `Bichler Zrzavy Rechtsanwälte GmbH & Co KG`

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

**Example 6** (doc_id: `deanon_260716_TRAIN/3Ob223_19v`) (sent_id: `deanon_260716_TRAIN/3Ob223_19v_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Priv.-Doz. Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr, Dr. Kodek und Mag. Wessely-Kristöfel als weitere Richter in der Exekutionssache der betreibenden Partei WestLebensmittel Betriebe GesmbH, Adalbert-Stifter-Platz 4, 3143 Gattring-Raking, Österreich, vertreten durch Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG in Wien, gegen die verpflichtete Partei Dkfm.

**False Positives:**

- `Maur & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG`

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

**Example 7** (doc_id: `deanon_260716_TRAIN/3Ob72_20i`) (sent_id: `deanon_260716_TRAIN/3Ob72_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Marktgemeinde James Weyand, MA, vertreten durch Dr. Nader Karl Mahdi, Rechtsanwalt in Wattens, gegen die beklagte Partei Lützeler Garten AG, Esteplatz 2, 9064 Schöpfendorf, Österreich, vertreten durch Altenweisl Wallnöfer Watschinger Zimmermann Rechtsanwälte GmbH in Innsbruck, und die auf Seiten der beklagten Partei beigetretene Nebenintervenientin Demeyer u. Köktas Analyse GmbH, Zinkendorferstraße 100, 9321 Schöttlhof, Österreich, vertreten durch Dr. Christian Girardi, LL.M., Ing. Dr. Stefan Schwärzler, Mag. Daniel Pichler, Rechtsanwälte in Innsbruck, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. März 2020, GZ 1 R 5/20z-27, womit das Urteil des Landesgerichts Innsbruck vom 14. November 2019, GZ 12 Cg 33/19m-18, teilweise bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Watschinger Zimmermann Rechtsanwälte GmbH` — partial — pred is substring of gold: `Altenweisl Wallnöfer Watschinger Zimmermann Rechtsanwälte GmbH`

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

**Example 8** (doc_id: `deanon_260716_TRAIN/4Nc4_17a`) (sent_id: `deanon_260716_TRAIN/4Nc4_17a_5`)


Sanitär Norfurtwerk AG, Piburger Straße 20, 4204 Hadersdorf, Österreich, Deutschland, beide vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Gesamtstreitwert 69.500 EUR), über den Ordinationsantrag der Klägerinnen den Beschluss gefasst:  Spruch Dem Ordinationsantrag wird stattgegeben.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Sanitär Norfurtwerk AG`(organisation)
- `Piburger Straße 20, 4204 Hadersdorf, Österreich`(address)
- `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/4Ob100_13d`) (sent_id: `deanon_260716_TRAIN/4Ob100_13d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Verein Karen Böckel, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei Düwall + Rief Daten -Aktiengesellschaft, Gassing/Burgweg 63, 4613 Mistelbach bei Wels, Österreich, vertreten durch Raits Bleiziffer Rechtsanwälte GmbH in Salzburg, und die Nebenintervenientin auf Seiten der beklagten Partei „ Eberhard Besemer ” Linda Hukauf, vertreten durch Dr. Peter Zöchbauer und andere Rechtsanwälte in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert 36.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz vom 19. April 2013, GZ 1 R 192/12d-14, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Wehrle & Langer Rechtsanwälte KG` — partial — pred is substring of gold: `Kosesnik-Wehrle & Langer Rechtsanwälte KG`

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

**Example 10** (doc_id: `deanon_260716_TRAIN/4Ob180_10i`) (sent_id: `deanon_260716_TRAIN/4Ob180_10i_3`)


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

**Example 11** (doc_id: `deanon_260716_TRAIN/4Ob53_24h`) (sent_id: `deanon_260716_TRAIN/4Ob53_24h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Mag. Istjan, LL.M., und Mag. Waldstätten sowie den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Talheimder GmbH, Eisenbahnerstraße 406, 6100 Reith bei Seefeld, Österreich, vertreten durch die Eckert . Nittmann Rechtsanwälte GmbH in Wien, gegen die beklagten Parteien 1.

**False Positives:**

- `Nittmann Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schwarzenbacher`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Mag. Istjan, LL.M.`(person)
- `Mag. Waldstätten`(person)
- `Dr. Stiefsohn`(person)
- `Talheimder GmbH`(organisation)
- `Eisenbahnerstraße 406, 6100 Reith bei Seefeld, Österreich`(address)

**Example 12** (doc_id: `deanon_260716_TRAIN/4Ob8_25t`) (sent_id: `deanon_260716_TRAIN/4Ob8_25t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Istjan, LL.M., Mag. Waldstätten, Dr. Stiefsohn und Mag. Böhm in der Rechtssache der klagenden Partei Flörcke Textil -GmbH, Im Weg 42, 8271 Wagerberg, Österreich, vertreten durch die Schneider & Schneider Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Gastronomie Furtaltra GmbH, Wiesfleck 42, 4844 Schacha, Österreich, vertreten durch die Blum, Hagen & Partner Rechtsanwälte GmbH in Feldkirch, wegen 511.571,82 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 21. November 2024, GZ 2 R 151/24h-121, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Hagen & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Blum, Hagen & Partner Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schwarzenbacher`(person)
- `Mag. Istjan, LL.M.`(person)
- `Mag. Waldstätten`(person)
- `Dr. Stiefsohn`(person)
- `Mag. Böhm`(person)
- `Flörcke Textil -GmbH`(organisation)
- `Im Weg 42, 8271 Wagerberg, Österreich`(address)
- `Schneider & Schneider Rechtsanwalts GmbH`(organisation)
- `Gastronomie Furtaltra GmbH`(organisation)
- `Wiesfleck 42, 4844 Schacha, Österreich`(address)
- `Blum, Hagen & Partner Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Innsbruck`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/5Ob171_22s`) (sent_id: `deanon_260716_TRAIN/5Ob171_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Savitski&Flashar Möbel GmbH, Kada-Gasse 107, 9170 Zell-Oberwinkel, Österreich, vertreten durch Dr. Manfred Sommerbauer, DDr. Michael Dohr, LL.M., LL.M., Rechtsanwälte in Wiener Neustadt, gegen die beklagte Partei Fryc+Brotzler Energie Rechtsanwälte GmbH, Lange Gasse 15, 4891 Plain, Österreich, wegen Unterlassung (Streitwert 36.000 EUR) und Feststellung (Streitwert 3.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien vom 30. Mai 2022, GZ 5 R 6/22x-46, mit dem das Urteil des Handelsgerichts Wien vom 3. November 2021, GZ 21 Cg 21/21f-39, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Brotzler Energie Rechtsanwälte GmbH` — partial — pred is substring of gold: `Fryc+Brotzler Energie Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Jensik`(person)
- `Mag. Wurzer`(person)
- `Mag. Painsi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Steger`(person)
- `Savitski&Flashar Möbel GmbH`(organisation)
- `Kada-Gasse 107, 9170 Zell-Oberwinkel, Österreich`(address)
- `Dr. Manfred Sommerbauer`(person)
- `DDr. Michael Dohr, LL.M.`(person)
- `Fryc+Brotzler Energie Rechtsanwälte GmbH`(organisation)
- `Lange Gasse 15, 4891 Plain, Österreich`(address)
- `Oberlandesgerichts Wien`(organisation)
- `Handelsgerichts Wien`(organisation)

**Example 14** (doc_id: `deanon_260716_TRAIN/5Ob177_20w`) (sent_id: `deanon_260716_TRAIN/5Ob177_20w_7`)


Imre Leitersbach, beide vertreten durch die Held Berdnik Astner & Partner Rechtsanwälte GmbH, Graz, wegen § 37 Abs 1 Z 8, Z 8b, Z 9, Z 12 MRG, über den Revisionsrekurs der Antragsgegner gegen den Sachbeschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 14. Mai 2020, GZ 5 R 15/20t-34, mit dem der „Teilsachbeschluss“ des Bezirksgerichts Leibnitz vom 8. November 2019, GZ 17 MSch 8/18x-30, aufgehoben wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Astner & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Held Berdnik Astner & Partner Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Imre Leitersbach`(person)
- `Held Berdnik Astner & Partner Rechtsanwälte GmbH`(organisation)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)
- `Bezirksgerichts Leibnitz`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/5Ob63_21g`) (sent_id: `deanon_260716_TRAIN/5Ob63_21g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer, Mag. Painsi und Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Alexander Imberg, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Antonia Diemar, vertreten durch Lansky, Ganzger & Partner Rechtsanwälte GmbH in Wien, wegen 405.188,80 EUR sA und Feststellung (Streitwert 35.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 18. Februar 2021, GZ 11 R 8/21h-28, mit dem die Berufung der beklagten Partei gegen das Versäumungsurteil des Landesgerichts für Zivilrechtssachen Wien vom 11. August 2020, GZ 17 Cg 55/20p-4, zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Ganzger & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Lansky, Ganzger & Partner Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Jensik`(person)
- `Dr. Grohmann`(person)
- `Mag. Wurzer`(person)
- `Mag. Painsi`(person)
- `Dr. Steger`(person)
- `Alexander Imberg`(person)
- `Mag. Franz Podovsovnik`(person)
- `Antonia Diemar`(person)
- `Lansky, Ganzger & Partner Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/5Ob71_24p`) (sent_id: `deanon_260716_TRAIN/5Ob71_24p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Mag. Wurzer als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Painsi, Dr. Weixelbraun-Mohr, Dr. Steger und Dr. Pfurtscheller als weitere Richter in der Rechtssache der klagenden Partei Josefine Fretschner, vertreten durch die Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei AlpenDerlogverEvent GmbH, Am Kröpflmühlerberg 93, 3925 Kleinpertenschlag, Österreich, vertreten durch die Wolf Theiss Rechtsanwälte GmbH & Co KG in Wien, wegen 7.140 EUR und Feststellung (Streitwert 2.000 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Steyr als Berufungsgericht vom 8. Februar 2024, GZ 1 R 120/23z-43, mit dem das Urteil des Bezirksgerichts Steyr vom 28. September 2023, GZ 2 C 288/21x-39, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das Verfahren über die Revision der beklagten Partei wird bis zur Entscheidung des Gerichtshofs der Europäischen Union (EuGH) über die Vorabentscheidungsersuchen des Landgerichts Ravensburg (Deutschland) vom 9. November 2023, Rechtssache C-666/23, vom 9. November 2023, Rechtssache C-667/23, und vom 15. November 2023, Rechtssache C-668/23, unterbrochen.

**False Positives:**

- `Wolf Theiss Rechtsanwälte GmbH` — partial — pred is substring of gold: `Wolf Theiss Rechtsanwälte GmbH & Co KG`

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

- `Maur & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG`

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

- `PHH Prochaska Havranek Rechtsanwälte GmbH` — partial — pred is substring of gold: `PHH Prochaska Havranek Rechtsanwälte GmbH & Co KG`

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

**Example 19** (doc_id: `deanon_260716_TRAIN/6Ob231_24z`) (sent_id: `deanon_260716_TRAIN/6Ob231_24z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Hofer-Zeni-Rennhofer als Vorsitzende sowie die Hofrätinnen und Hofräte Hon.-Prof. Dr. Faber, Mag. Pertmayr, Dr. Weber und Mag. Nigl LL.M. als weitere Richter in der Rechtssache der klagenden Partei Ing. Tiffany Jähncke, vertreten durch Poduschka Partner Anwaltsgesellschaft mbH in Linz, wider die beklagte Partei Sudconbach-Bau AG, Hart, Akazienstraße 15v, 4064 Oftering, Österreich, Deutschland, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 9.600 EUR sA, im Verfahren über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Linz als Berufungsgericht vom 7. Oktober 2024, GZ 6 R 57/24b-31, womit das Urteil des Bezirksgerichts Traun vom 16. Februar 2024, GZ 2 C 198/23z-22, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei vom 9. Dezember 2025 auf Fortsetzung des Verfahrens wird abgewiesen.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

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

**Example 20** (doc_id: `deanon_260716_TRAIN/6Ob47_25t`) (sent_id: `deanon_260716_TRAIN/6Ob47_25t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Hofer-Zeni-Rennhofer als Vorsitzende sowie die Hofrätinnen und Hofräte Dr. Faber, Mag. Pertmayr, Dr. Weber und Mag. Nigl LL.M. als weitere Richter in der Rechtssache der klagenden Partei Kimberly Schnellhardt, vertreten durch Dr. Alexander Amann LL.M., Rechtsanwalt in Gamprin-Bendern, Liechtenstein, wider die beklagte Partei Digital Trasudwerk AG, Galles 5, 8453 Kitzelsdorf, Österreich, Deutschland, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 71.888,75 EUR sA Zug um Zug gegen die Rückstellung eines Fahrzeugs, in eventu wegen 17.972,19 EUR sA und Feststellung, im Verfahren über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Jänner 2025, GZ 11 R 7/25t-63, den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

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

**Example 21** (doc_id: `deanon_260716_TRAIN/6Ob56_19g`) (sent_id: `deanon_260716_TRAIN/6Ob56_19g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1060 Wien, Linke Wienzeile 18, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei QUMV Pflege GmbH, Nordring 89q, 2770 Gutenstein, Österreich, vertreten durch Dr. Peter Lindinger Dr. Andreas Pramer GesbR, Rechtsanwälte in Linz, wegen Unterlassung und Urteilsveröffentlichung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2019, GZ 3 R 141/18b-17, mit dem über Berufungen der klagenden und der beklagten Partei das Urteil des Landesgerichts Linz vom 2. September 2018, GZ 31 Cg 4/18a-9, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Wehrle & Langer Rechtsanwälte KG` — partial — pred is substring of gold: `Kosesnik-Wehrle & Langer Rechtsanwälte KG`

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

**Example 22** (doc_id: `deanon_260716_TRAIN/7Ob259_10d`) (sent_id: `deanon_260716_TRAIN/7Ob259_10d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Huber als Vorsitzende und durch die Hofräte Dr. Hoch, Dr. Kalivoda, Dr. Roch und Mag. Dr. Wurdinger als weitere Richter in den verbundenen Rechtssachen der klagenden und widerbeklagten Partei Maule Digital Rechtsanwälte GmbH, Zur Fischwasserung 33, 4090 Stadl, Österreich, gegen die beklagte und widerklagende Partei Mag. Wolfgang Kojima, vertreten durch GKP Gabl Kogler Papesch Leitner Rechtsanwälte OG in Linz, wegen 63.833,25 EUR sA (Klage) und 15.000 EUR sA (Widerklage), über die außerordentliche Revision der beklagten und widerklagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 9. November 2010, GZ 15 R 64/10g-89, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Maule Digital Rechtsanwälte GmbH` — partial — gold is substring of pred: `Maule Digital Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Huber`(person)
- `Dr. Hoch`(person)
- `Dr. Kalivoda`(person)
- `Dr. Roch`(person)
- `Mag. Dr. Wurdinger`(person)
- `Maule Digital Rechtsanwälte GmbH`(organisation)
- `Zur Fischwasserung 33, 4090 Stadl, Österreich`(address)
- `Mag. Wolfgang Kojima`(person)
- `GKP Gabl Kogler Papesch Leitner Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/7Ob25_17b`) (sent_id: `deanon_260716_TRAIN/7Ob25_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofrätinnen und Hofräte Dr. Höllwerth, Dr. E. Solé, Mag. Malesich und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Dr. Luna Kowalczuk, vertreten durch Mag. Willibald Berger, Rechtsanwalt in Marchtrenk, gegen die beklagte Partei Dr. Eleonore Fulbrecht, vertreten durch Posch, Schausberger & Lutz Rechtsanwälte GmbH in Wels, wegen 13.632,65 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Wels als Berufungsgericht vom 16. November 2016, GZ 21 R 273/16w (21 R 274/16t, 21 R 275/16i)-178, mit dem das Urteil des Bezirksgerichts Grieskirchen vom 3. Juni 2016, GZ 8 C 22/05x-148, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Schausberger & Lutz Rechtsanwälte GmbH` — partial — pred is substring of gold: `Posch, Schausberger & Lutz Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Kalivoda`(person)
- `Dr. Höllwerth`(person)
- `Dr. E. Solé`(person)
- `Mag. Malesich`(person)
- `MMag. Matzka`(person)
- `Dr. Luna Kowalczuk`(person)
- `Mag. Willibald Berger`(person)
- `Dr. Eleonore Fulbrecht`(person)
- `Posch, Schausberger & Lutz Rechtsanwälte GmbH`(organisation)
- `Landesgerichts Wels`(organisation)
- `Bezirksgerichts Grieskirchen`(organisation)

**Example 24** (doc_id: `deanon_260716_TRAIN/7Ob36_25g`) (sent_id: `deanon_260716_TRAIN/7Ob36_25g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Malesich, Dr. Weber, Mag. Fitz und Mag. Jelinek als weitere Richter in der Rechtssache der klagenden Partei Gundula Aichmann, vertreten durch Poduschka Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Plönnigs Technik AG, Wieden 35, 3390 Spielberg, Österreich, vertreten durch Themmer, Toth & Partner Rechtsanwälte GmbH in Wien, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 28. November 2024, GZ 1 R 124/24t-14, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 27. Juni 2024, GZ 21 C 604/23m-10, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Toth & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Themmer, Toth & Partner Rechtsanwälte GmbH`

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

**Example 25** (doc_id: `deanon_260716_TRAIN/8ObA18_17f`) (sent_id: `deanon_260716_TRAIN/8ObA18_17f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Brenn als weitere Richter sowie die fachkundigen Laienrichter Mag. Dr. Bernhard Gruber und Harald Kohlruss in der Arbeitsrechtssache der klagenden Partei MedR Clemens Schepper, vertreten durch Freimüller/Obereder/Pilz Rechtsanwält_innen GmbH in Wien, gegen die beklagte Partei Muehleis & Klaese Technik AG, Rosentaler Weg 2k, 9811 St. Peter in Holz, Österreich, vertreten durch DLA Piper Weiss-Tessbach Rechtsanwälte GmbH in Wien, wegen Feststellung (Streitwert 282,56 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. November 2016, GZ 7 Ra 90/16f-19, mit dem das Urteil des Arbeits- und Sozialgerichts Wien vom 20. Juli 2016, GZ 33 Cga 50/16p-15, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Weiss-Tessbach Rechtsanwälte GmbH` — partial — pred is substring of gold: `DLA Piper Weiss-Tessbach Rechtsanwälte GmbH`

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

**Example 26** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden und die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn sowie die fachkundigen Laienrichter Mag. Dr. Monika Lanz und Wolfgang Cadilek als weitere Richter in der Arbeitsrechtssache der klagenden Partei Hon.-Prof. Dieter Kovacs, vertreten durch Pfurtscheller Orgler Huber, Rechtsanwälte in Innsbruck, gegen die beklagte Partei ÖBB-Personenverkehr AG, Monsbergergasse 12, 6210 Astenberg, Österreich, vertreten durch die CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 3.963,75 EUR brutto sA, aus Anlass der (außerordentlichen) Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. Februar 2013, GZ 13 Ra 1/13i-16, mit dem das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 16. Oktober 2012, GZ 42 Cga 87/12h-12, abgeändert wurde, den Beschluss gefasst:  Spruch A.Dem Gerichtshof der Europäischen Union werden folgende Fragen zur Vorabentscheidung vorgelegt: 1.Ist Art 21 der Grundrechtecharta in Verbindung mit Art 7 Abs 1, Art 16 und Art 17 der Richtlinie 2000/78/EG dahin auszulegen, dass a)ein Arbeitnehmer, für den vom Arbeitgeber aufgrund einer gesetzlich normierten altersdiskriminierenden Anrechnung von Vordienstzeiten zunächst ein unrichtiger Vorrückungsstichtag festgesetzt wurde, in jedem Fall Anspruch auf Zahlung der Gehaltsdifferenz unter Zugrundelegung des diskriminierungsfreien Vorrückungsstichtags hat, b)oder aber dahin, dass der Mitgliedstaat die Möglichkeit hat, durch eine diskriminierungsfreie Anrechnung der Vordienstzeiten die Altersdiskriminierung auch ohne finanziellen Ausgleich (durch Neufestsetzung des Vorrückungsstichtags bei gleichzeitiger Verlängerung des Vorrückungszeitraums) zu beseitigen, insbesondere wenn diese entgeltneutrale Lösung die Liquidität des Arbeitgebers aufrechterhalten sowie einen übermäßigen Neuberechnungsaufwand vermeiden soll?

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

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

**Example 27** (doc_id: `deanon_260716_TRAIN/8ObA71_14w`) (sent_id: `deanon_260716_TRAIN/8ObA71_14w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden und durch die Hofrätin Dr. Tarmann-Prentner, den Hofrat Mag. Ziegelbauer, sowie die fachkundigen Laienrichter Mag. Andreas Mörk und Mag. Matthias Schachner als weitere Richter in der Arbeitsrechtssache der klagenden Partei Cynthia Schamel, vertreten durch Forcher-Mayr & Kantner Rechtsanwälte Partnerschaft in Innsbruck, gegen die beklagte Partei Werkglanz-Verlag AG, Blattbühel 46, 9073 Klagenfurt, Österreich, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Feststellung (Streitwert: 21.800 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 30. September 2014, GZ 15 Ra 92/14p-40, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

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

**Example 28** (doc_id: `deanon_260716_TRAIN/8ObA72_19z`) (sent_id: `deanon_260716_TRAIN/8ObA72_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Wessely-Kristöfel als weitere Richter sowie die fachkundigen Laienrichter Johannes Püller (aus dem Kreis der Arbeitgeber) und Mag. Michael Puhm (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Petra Tschurtschenthaler, vertreten durch Dr. Markus Orgler, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Uthe Getränke AG, Triester Bundesstraße 146, 3452 Trasdorf, Österreich, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 4.200,83 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 17. Oktober 2019, GZ 13 Ra 41/15z-30, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — partial — pred is substring of gold: `CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH`

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

**Example 29** (doc_id: `deanon_260716_TRAIN/8ObA74_19v`) (sent_id: `deanon_260716_TRAIN/8ObA74_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Wessely-Kristöfel als weitere Richter sowie die fachkundigen Laienrichter Mag. Thomas Stegmüller (aus dem Kreis der Arbeitgeber) und Gerald Fida (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Mag. OStR Dipl. Kfm. Albert Jellinek, vertreten durch Mag. Dr. Johannes Winkler, Rechtsanwalt in Linz, gegen die beklagte Partei Rhein Trazor GmbH, Erste Straße 10, 5151 Gastein, Österreich, vertreten durch MM Metzler & Musel Rechtsanwälte GmbH in Linz, wegen 18.229,17 EUR brutto sA und Ausstellung eines Dienstzeugnisses, über die außerordentliche Revision der klagenden Partei (Revisionsinteresse 18.229,17 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 28. Oktober 2019, GZ 11 Ra 63/19t-15, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Metzler & Musel Rechtsanwälte GmbH` — partial — pred is substring of gold: `MM Metzler & Musel Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Kuras`(person)
- `Dr. Tarmann-Prentner`(person)
- `Mag. Wessely-Kristöfel`(person)
- `Mag. Thomas Stegmüller`(person)
- `Gerald Fida`(person)
- `Mag. OStR Dipl. Kfm. Albert Jellinek`(person)
- `Mag. Dr. Johannes Winkler`(person)
- `Rhein Trazor GmbH`(organisation)
- `Erste Straße 10, 5151 Gastein, Österreich`(address)
- `MM Metzler & Musel Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Linz`(organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/9ObA144_14p`) (sent_id: `deanon_260716_TRAIN/9ObA144_14p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden und die Hofräte des Obersten Gerichtshofs Mag. Ziegelbauer und Dr. Hargassner sowie die fachkundigen Laienrichter KR Mag. Paul Kunsky und Harald Kohlruss als weitere Richter in der Arbeitsrechtssache der klagenden Partei Franziska Schönmeier, vertreten durch Held Berdnik Astner & Partner Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Heizung Bachkraftlog GmbH & Co KG, Schlangglfeld 48, 4980 Viehausen, Österreich, vertreten durch die Klein, Wuntschek & Partner Rechtsanwälte GmbH in Graz, wegen Kündigungsanfechtung, über die außerordentliche Revision und den „Kostenrekurs“ der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 26. September 2014, GZ 7 Ra 66/14a-25, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Astner & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Held Berdnik Astner & Partner Rechtsanwälte GmbH`
- `Wuntschek & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Klein, Wuntschek & Partner Rechtsanwälte GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 31** (doc_id: `deanon_260716_TRAIN/9ObA18_19s`) (sent_id: `deanon_260716_TRAIN/9ObA18_19s_4`)


Gabriele Svirak als weitere Richter in der Arbeitsrechtssache der klagenden Partei Bruno Milke, vertreten durch Dr. Herbert Holzinger, Rechtsanwalt in Wien, gegen die beklagte Partei Enne Logistik GmbH, Obere Klaus 24, 8301 Präbach, Österreich, vertreten durch Haslinger/Nagele & Partner Rechtsanwälte GmbH in Linz, wegen 2.672,09 EUR brutto sA und 608 EUR netto sA, Ausstellung eines Dienstzeugnisses und Vorlage eines Buchauszugs, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. Dezember 2018, GZ 10 Ra 83/18a-11, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Nagele & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Haslinger/Nagele & Partner Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gabriele Svirak`(person)
- `Bruno Milke`(person)
- `Dr. Herbert Holzinger`(person)
- `Enne Logistik GmbH`(organisation)
- `Obere Klaus 24, 8301 Präbach, Österreich`(address)
- `Haslinger/Nagele & Partner Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 32** (doc_id: `deanon_260716_TRAIN/9ObA4_13y`) (sent_id: `deanon_260716_TRAIN/9ObA4_13y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Werner Rodlauer und Mag. Robert Brunner als weitere Richter in der Arbeitsrechtssache der klagenden Partei OSR Mag.a Amber Mittelhäußer, vertreten durch Dr. Susanne Kuen, Rechtsanwältin in Wien, gegen die beklagte Partei Klaussen Metall GmbH, Urlakenstraße 5W, 3912 Kleingöttfritz, Österreich, vertreten durch Fellner Wratzfeld & Partner Rechtsanwälte GmbH in Wien, wegen 125.731,44 EUR sA, über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 30. Oktober 2012, GZ 11 Ra 82/12a-74, mit dem das Urteil des Landesgerichts Steyr als Arbeits- und Sozialgericht vom 31. Juli 2012, GZ 9 Cga 245/08g-70, aufgehoben und die Rechtssache an das Erstgericht zurückverwiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Wratzfeld & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Fellner Wratzfeld & Partner Rechtsanwälte GmbH`

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

**Example 33** (doc_id: `deanon_260716_TRAIN/9ObA8_20x`) (sent_id: `deanon_260716_TRAIN/9ObA8_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau und den Hofrat des Obersten Gerichtshofs Dr. Hargassner sowie die fachkundigen Laienrichter Dr. Ingomar Stupar (aus dem Kreis der Arbeitgeber) und Mag. Werner Pletzenauer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Mag. Dr. Hartmut Sperber, vertreten durch Moser Mutz Rechtsanwälte GesbR in Klagenfurt am Wörthersee, gegen die beklagte Partei HASK Software Betriebe AG, Alter Garten 34, 8490 Hummersdorf, Österreich, vertreten durch Wiedenbauer Mutz Winkler & Partner Rechtsanwälte GmbH in Klagenfurt am Wörthersee, wegen Kündigungsanfechtung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 18. Dezember 2019, GZ 7 Ra 70/19x-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Winkler & Partner Rechtsanwälte GmbH` — partial — pred is substring of gold: `Wiedenbauer Mutz Winkler & Partner Rechtsanwälte GmbH`

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

## `Gesellschaft_mbh_Specific` 

**F1:** 0.001 | **Precision:** 0.500 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `19ebbf47`  
**Description:**
Specifically matches 'Gesellschaft mbH' (lowercase g) which the generic rule might miss if the name structure is complex, e.g., 'Kress Möbel gesellschaft mbH'.

**Content:**
```
(?<![\w])([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*|[A-Z][a-zA-Z]+(?:-[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\+[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s+und\s+[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s*&\s*[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s+&\s*[A-Z][a-zA-Z]+)+)\s+gesellschaft\s+mbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.001 | 0.001 | 6 | 3 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 3 | 1936 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/3Ob1_18w`) (sent_id: `deanon_260716_TRAIN/3Ob1_18w_4`)


MJIL Holz Consulting gesellschaft mbH, Feldbaumstraße 8c, 4892 Walligen, Österreich, 2.

| Predicted | Gold |
|---|---|
| `MJIL Holz Consulting gesellschaft mbH` | `MJIL Holz Consulting gesellschaft mbH` |

**Missed by this rule (FN):**

- `Feldbaumstraße 8c, 4892 Walligen, Österreich` (address)

**Example 1** (doc_id: `deanon_260716_TRAIN/3Ob1_18w`) (sent_id: `deanon_260716_TRAIN/3Ob1_18w_6`)


Inn-Logistik gesellschaft mbH, Sanatoriumstraße 22, 4084 Ensfeld, Österreich, alle vertreten durch Dr. Nikolaus Kraft, Rechtsanwalt in Wien, wegen Unzulässigkeitserklärung einer Exekution (§ 36 EO), über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 19. September 2017, GZ 47 R 281/17x-41, womit das Urteil des Bezirksgerichts Meidling vom 20. Juni 2016, GZ 5 C 1/15w-37, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Inn-Logistik gesellschaft mbH` | `Inn-Logistik gesellschaft mbH` |

**Missed by this rule (FN):**

- `Sanatoriumstraße 22, 4084 Ensfeld, Österreich` (address)
- `Dr. Nikolaus Kraft` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Meidling` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/6Ob240_20t`) (sent_id: `deanon_260716_TRAIN/6Ob240_20t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie durch die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Firmenbuchsache der zu FN FN103376a beim Landesgericht Landesgericht Krems an der Donau eingetragenen Taltalgart-Gastronomie GmbH mit Sitz in der politischen Gemeinde Landesgericht Salzburg, über den Revisionsrekurs der Telekom Mongart gesellschaft mbH, Franz-Martin-Straße 1, 9161 Ehrensdorf, Österreich, vertreten durch Dr. Robert Mogy, Rechtsanwalt in Klagenfurt, gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. Oktober 2020, GZ 4 R 153/20g-8, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen (§ 71 Abs 3 AußStrG iVm § 15 Abs 2 FBG).

| Predicted | Gold |
|---|---|
| `Telekom Mongart gesellschaft mbH` | `Telekom Mongart gesellschaft mbH` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Dr. Schramm` (person)
- `Hon.-Prof. Dr. Gitschthaler` (person)
- `Univ.-Prof. Dr. Kodek` (person)
- `Dr. Nowotny` (person)
- `Dr. Faber` (person)
- `FN103376a` (business_register_number)
- `Landesgericht Krems an der Donau` (organisation)
- `Taltalgart-Gastronomie GmbH` (organisation)
- `Landesgericht Salzburg` (organisation)
- `Franz-Martin-Straße 1, 9161 Ehrensdorf, Österreich` (address)
- `Dr. Robert Mogy` (person)
- `Oberlandesgerichts Graz` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/3Ob182_11b`) (sent_id: `deanon_260716_TRAIN/3Ob182_11b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Traun Logtri gesellschaft mbH, Friedhofplatz 9, 5274 Weikerding, Österreich, vertreten durch Dr. Maximilian Gumpoldsberger, Rechtsanwalt in Wels, und der Nebenintervenientin auf Seiten der klagenden Partei Ruddies + Kasperrek Umwelt Gesellschaft mbH, Hohenkogl 4, 8255 Steinhöf, Österreich, vertreten durch Dr. Lydia Friedle, Rechtsanwältin in Mannersdorf am Leithagebirge, gegen die beklagte Partei Büchner Holz GmbH, Schedifkaplatz 3, 3134 Fräuleinmühle, Österreich, vertreten durch Dr. Franz Gütlbauer, Dr. Siegfried Sieghartsleitner und Dr. Michael Pichlmair, Rechtsanwälte in Wels, sowie der Nebenintervenientin auf Seiten der beklagten Partei Feigle + Hinzelin Cloud Gesellschaft mbH, Josef-Wolf-Platz 10, 4063 Rudelsdorf, Österreich, vertreten durch Mag. Thomas Braun, Rechtsanwalt in Wien, wegen restlich 52.596,75 EUR sA, infolge Revision der klagenden Partei gegen das Endurteil des Oberlandesgerichts Linz als Berufungsgericht vom 4. Juli 2011, GZ 4 R 108/11x-47, womit infolge Berufung der klagenden Partei das Endurteil des Landesgerichts Wels vom 14. März 2011, GZ 6 Cg 17/09w-42, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Traun Logtri gesellschaft mbH` — partial — gold is substring of pred: `Traun Logtri gesellschaft mbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Prückner`(person)
- `Hon.-Prof. Dr. Neumayr`(person)
- `Dr. Lovrek`(person)
- `Dr. Jensik`(person)
- `Dr. Roch`(person)
- `Traun Logtri gesellschaft mbH`(organisation)
- `Friedhofplatz 9, 5274 Weikerding, Österreich`(address)
- `Dr. Maximilian Gumpoldsberger`(person)
- `Ruddies + Kasperrek Umwelt Gesellschaft mbH`(organisation)
- `Hohenkogl 4, 8255 Steinhöf, Österreich`(address)
- `Dr. Lydia Friedle`(person)
- `Büchner Holz GmbH`(organisation)
- `Schedifkaplatz 3, 3134 Fräuleinmühle, Österreich`(address)
- `Dr. Franz Gütlbauer`(person)
- `Dr. Siegfried Sieghartsleitner`(person)
- `Dr. Michael Pichlmair`(person)
- `Feigle + Hinzelin Cloud Gesellschaft mbH`(organisation)
- `Josef-Wolf-Platz 10, 4063 Rudelsdorf, Österreich`(address)
- `Mag. Thomas Braun`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Wels`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/3Ob32_17b`) (sent_id: `deanon_260716_TRAIN/3Ob32_17b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Jensik und Dr. Roch und die Hofrätin Dr. Kodek als weitere Richter in der Exekutionssache der betreibenden Partei Balthasar Düppen, Italien, vertreten durch Oberhammer Rechtsanwälte GmbH in Wien, wider die verpflichtete Partei Ober Talnor gesellschaft mbH, Pesenbachtal 28, 5121 Eckldorf, Österreich, vertreten durch Dr. Daniel Charim und Mag. Jakob Charim, Rechtsanwälte in Wien, wegen (restlich) 347.093,53 EUR sA über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 7. Dezember 2016, GZ 46 R 323/16i-61, womit der Beschluss des Bezirksgerichts Josefstadt vom 24. Juni 2016, GZ 11 E 2966/11p-56, bestätigt wurde, den Beschluss gefasst:  Spruch I.Der Revisionsrekurs der verpflichteten Partei wird, soweit er die Bestätigung der Exekutionsbewilligung bekämpft, als jedenfalls unzulässig zurückgewiesen.

**False Positives:**

- `Partei Ober Talnor gesellschaft mbH` — partial — gold is substring of pred: `Ober Talnor gesellschaft mbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hoch`(person)
- `Dr. Lovrek`(person)
- `Dr. Jensik`(person)
- `Dr. Roch`(person)
- `Dr. Kodek`(person)
- `Balthasar Düppen`(person)
- `Oberhammer Rechtsanwälte GmbH`(organisation)
- `Ober Talnor gesellschaft mbH`(organisation)
- `Pesenbachtal 28, 5121 Eckldorf, Österreich`(address)
- `Dr. Daniel Charim`(person)
- `Mag. Jakob Charim`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Josefstadt`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/4Ob19_10p`) (sent_id: `deanon_260716_TRAIN/4Ob19_10p_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei StadtEnergie Planung gesellschaft mbH,*****, vertreten durch Prof. Haslinger & Partner, Rechtsanwälte in Linz, gegen die beklagte Partei Deecken Event AG,*****, vertreten durch Rechtsanwälte Konrad & Schröttner OG in Graz, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 65.000 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 25. November 2009, GZ 6 R 169/09h-37, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei StadtEnergie Planung gesellschaft mbH` — partial — gold is substring of pred: `StadtEnergie Planung gesellschaft mbH`

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

</details>

---

## `Domain_Organisation` 💣

**F1:** 0.002 | **Precision:** 0.308 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `8d2a6af2`  
**Description:**
Matches organization names ending in .at (e.g., 'Logderfurt-Logistik.at', 'YNKW Elektro.at').

**Content:**
```
\b[A-Z][a-zA-Z]+(?:[-+&][A-Z][a-zA-Z]+)*\.at\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.308 | 0.001 | 0.002 | 13 | 4 | 9 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 9 | 2777 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__5`)


Logderfurt-Logistik.at erfolgte Veröffentlichung eines Links zu einem am selben Tag auf der Website www.

| Predicted | Gold |
|---|---|
| `Logderfurt-Logistik.at` | `Logderfurt-Logistik.at` |

**Example 1** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__14`)


Das Erstgericht traf zum betreffenden Facebook-Posting folgende – wörtlich wiedergegebenen – Feststellungen (US 15 f):  „Der Besucher des Facebook-Auftritts von Nieder-Touristik.at konnte diesem Posting entnehmen, dass es sich um einen Link zum Artikel 'Die dreckigen Fantasien des Katharina Scheiffgen ' auf der Website www.

| Predicted | Gold |
|---|---|
| `Nieder-Touristik.at` | `Nieder-Touristik.at` |

**Missed by this rule (FN):**

- `Katharina Scheiffgen` (person)

**Example 2** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__15`)


HochSolar.at handelt. Nähere Informationen zu diesen 'dreckigen Fantasien' erschließen sich dem Besucher aus Facebook heraus aber noch nicht.

| Predicted | Gold |
|---|---|
| `HochSolar.at` | `HochSolar.at` |

**Example 3** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__58`)


Logder.at erfolgte Veröffentlichung eines – mit dem Lichtbild des Antragstellers und dem Text „Einzige Entschuldigung für die Sudelfeder: Alkoholeinfluss“ und „Die dreckigen Fantasien des Dipl.-Ing. Werner Gebramczyk “ versehenen – Links zum auf der Website www.

| Predicted | Gold |
|---|---|
| `Logder.at` | `Logder.at` |

**Missed by this rule (FN):**

- `Dipl.-Ing. Werner Gebramczyk` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__6`)


YNKW Elektro.at veröffentlichten Artikel eine Entschädigungszahlung nach § 6 Abs 1 MedienG aufzuerlegen, abgewiesen wurde, sowie 2./ des Oberlandesgerichts Wien als Berufungsgericht vom 28. November 2018, AZ 17 Bs 153/18a (ON 74 der Hv-Akten), soweit damit der gegen Punkt III./ gerichteten Berufung des Antragstellers nicht Folge gegeben wurde, jeweils § 6 Abs 1 MedienG.

**False Positives:**

- `Elektro.at` — partial — pred is substring of gold: `YNKW Elektro.at`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `YNKW Elektro.at`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__8`)


Wien Dorftratri Technologien.at und www.facebook.com/ RheinMöbel.at) und eine weitere Antragsgegnerin (nunmehr Mediengruppe „ Stadt Logderder “ GmbH) wegen § 6 Abs 1 und § 8a Abs 6 MedienG, AZ 91 Hv 49/17t des Landesgerichts für Strafsachen Wien, erkannte der Einzelrichter dieses Gerichts mit Urteil vom 26. März 2018 (ON 65) – soweit im Folgenden für die Nichtigkeitsbeschwerde zur Wahrung des Gesetzes von Relevanz – ua dahin, dass durch die am 4. Juni 2017 auf der Website www.

**False Positives:**

- `Technologien.at` — partial — pred is substring of gold: `Wien Dorftratri Technologien.at`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien Dorftratri Technologien.at`(organisation)
- `RheinMöbel.at`(organisation)
- `Stadt Logderder`(organisation)
- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__9`)


Nornexver Versand.at erfolgte Veröffentlichung des Artikels mit dem Titel „Die dreckigen Fantasien des Timothy Cornelißen “in einem Medium in Ansehung des Antragstellers der objektive Tatbestand der üblen Nachrede nach § 111 Abs 1 StGB hergestellt wurde, weil darin wiederholt behauptet wurde, der Antragsteller „würde seine Tätigkeit als Kolumnist in stark alkoholisiertem Zustand verrichten“;

**False Positives:**

- `Versand.at` — partial — pred is substring of gold: `Nornexver Versand.at`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nornexver Versand.at`(organisation)
- `Timothy Cornelißen`(person)

**Example 3** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__12`)


Endris Solar.at erfolgte Veröffentlichung eines – mit dem Lichtbild des Antragstellers und dem Text „Einzige Entschuldigung für die Sudelfeder: Alkoholeinfluss“ und „Die dreckigen Fantasien des HR KzlR Marilyn Splettstoeßer “ versehenen (vgl US 15) – Links zum vorgenannten Artikel auf der Website www.

**False Positives:**

- `Solar.at` — partial — pred is substring of gold: `Endris Solar.at`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Endris Solar.at`(organisation)
- `HR KzlR Marilyn Splettstoeßer`(person)

**Example 4** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__13`)


Köllisch Software.at eine (weitere) Entschädigungszahlung nach § 6 Abs 1 MedienG aufzuerlegen, abgewiesen (Punkt III./).

**False Positives:**

- `Software.at` — partial — pred is substring of gold: `Köllisch Software.at`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Köllisch Software.at`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__21`)


Zur Begründung führte das Berufungsgericht – soweit im Folgenden von Relevanz – in ausdrücklicher Abkehr von einer früher vertretenen Rechtsansicht (Urteil des Oberlandesgerichts Wien vom 14. Februar 2018, AZ 17 Bs 212/17a = MR 2018, 7) wie folgt aus (US 32 f): Die Antragsgegnerin Berg-Finanzen Planung GmbH habe auf einer Website (www. Hermani & Grebner Logistik.at) und damit in einem Medium (§ 1 Abs 1 Z 1 MedienG) den Tatbestand der üblen Nachrede hergestellt;

**False Positives:**

- `Logistik.at` — partial — pred is substring of gold: `Hermani & Grebner Logistik.at`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberlandesgerichts Wien`(organisation)
- `Berg-Finanzen Planung GmbH`(organisation)
- `Hermani & Grebner Logistik.at`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__27`)


Fritzsch Immobilien.at] in Betracht.

**False Positives:**

- `Immobilien.at` — partial — pred is substring of gold: `Fritzsch Immobilien.at`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fritzsch Immobilien.at`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_260716_TRAIN/15Os66_19y_15Os67_19w__59`)


Kosziollek Marine.at veröffentlichten (tatbildlichen) Artikel vom selben Tag zu Unrecht verneint.

**False Positives:**

- `Marine.at` — partial — pred is substring of gold: `Kosziollek Marine.at`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kosziollek Marine.at`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/3Nc39_24a`) (sent_id: `deanon_260716_TRAIN/3Nc39_24a_29`)


Als örtlich zuständiges Exekutionsgericht für die beabsichtigte Rechteexekution ist das Bezirksgericht Salzburg zu bestimmen, weil die Rhein Kraftnor.at GmbH als Registrierungsstelle der von der beabsichtigten Exekutionsführung betroffenen Domain der Verpflichteten im Sprengel dieses Gerichts ihren Sitz hat.

**False Positives:**

- `Kraftnor.at` — partial — pred is substring of gold: `Rhein Kraftnor.at`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Salzburg`(organisation)
- `Rhein Kraftnor.at`(organisation)

</details>

---

## `Generic_KG_Entity` 💣

**F1:** 0.001 | **Precision:** 0.077 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2d7a84d3`  
**Description:**
Matches generic corporate entities ending in KG (Kommanditgesellschaft) which were previously missing.

**Content:**
```
(?<![\w])(?:[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*|[A-Z][a-zA-Z]+(?:-[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\+[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s+und\s+[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s*&\s*[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s+&\s*[A-Z][a-zA-Z]+)+)\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.077 | 0.000 | 0.001 | 26 | 2 | 24 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 24 | 3720 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


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

**Example 1** (doc_id: `deanon_260716_TRAIN/4Ob196_10t`) (sent_id: `deanon_260716_TRAIN/4Ob196_10t_4`)


Monderdorf Cloud GmbH, R.-Hamerling-Gasse 4, 6373 Jochberg, Österreich, beide vertreten durch Ruggenthaler Rechtsanwalts KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 62.000 EUR) über den außerordentlichen Revisionsrekurs der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Wien vom 20. September 2010, GZ 30 R 29/10w-9, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ruggenthaler Rechtsanwalts KG` | `Ruggenthaler Rechtsanwalts KG` |

**Missed by this rule (FN):**

- `Monderdorf Cloud GmbH` (organisation)
- `R.-Hamerling-Gasse 4, 6373 Jochberg, Österreich` (address)
- `Oberlandesgerichts Wien` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_4`)


Norsee Technologien GmbH & Co KG und 2.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Norsee Technologien GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Norsee Technologien GmbH & Co KG`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_5`)


Text Begründung: Der Kläger erwarb als Verbraucher im Juni 2003 über Vermittlung eines selbständigen Vermögensberaters Kommanditanteile an der GBJU Getränke GmbH & Co KG im Nominale von 17.000 EUR zuzüglich 850 EUR Agio.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `GBJU Getränke GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `GBJU Getränke GmbH & Co KG`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_6`)


Text Gründe: Mit dem angefochtenen Urteil wurden Bernhard Berti und Norbert Wierich von der wider sie erhobenen Anklage, sie hätten am 7. Februar 2009 in Sebastian-Stief-Gasse 48, 2632 Altendorf, Österreich /Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der Hauenschildt&Mesarec Medien GesmbH & Co KG, Susanne Schwarzhuber, durch die Vorgabe, die Donau-Transport GmbH sei eine zahlungsfähige Leasingnehmerin, somit durch Täuschung über Tatsachen, zum Abschluss eines Leasingvertrags über ein Rennfahrzeug für die Dauer von 24 Monaten zu einem monatlichen Entgelt von 10.698,10 Euro, somit zu einer Handlung verleitet, welche die TraunTouristik Werke GesmbH & Co KG in einem 50.000 Euro übersteigenden Betrag von insgesamt 235.358,20 Euro am Vermögen schädigte, gemäß § 259 Z 3 StPO (verfehlt auch von der rechtlichen Kategorie; vglLendl, WK-StPO § 259 Rz 1) freigesprochen.

**False Positives:**

- `GesmbH & Co KG` — partial — pred is substring of gold: `Hauenschildt&Mesarec Medien GesmbH & Co KG`
- `GesmbH & Co KG` — similar text (different position): `Hauenschildt&Mesarec Medien GesmbH & Co KG`

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

- `GesmbH & Co KG` — partial — pred is substring of gold: `Prentl Handel GesmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Susanna Steen`(person)
- `Prentl Handel GesmbH & Co KG`(organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_4`)


In der Medienrechtssache der Antragsteller Dr. Patrick Schneeweiss und Chen Hölzle gegen die Antragsgegnerin TQGK Versicherung Holding GmbH & Co KG wegen §§ 7 f MedienG, AZ 93 Hv 56/18p, verletzt der Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 9. März 2020, AZ 18 Bs 340/19k (ON 27), § 395 Abs 2 StPO (iVm § 41 Abs 1 MedienG).

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `TQGK Versicherung Holding GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Patrick Schneeweiss`(person)
- `Chen Hölzle`(person)
- `TQGK Versicherung Holding GmbH & Co KG`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_5`)


Text Gründe: In der Medienrechtssache der Antragsteller Dr. Wieland Skocdopole und Priv.-Doz.in Heidrun Aguera, BA MSc gegen die Antragsgegnerin Wald Fenkraftal GmbH & Co KG wegen §§ 7 f MedienG brachten die Antragsteller beim Landesgericht für Strafsachen Wien gesondert, jeweils in einem eigenen Schriftsatz aber vertreten durch dieselbe Rechtsanwältin selbständige Entschädigungsanträge gegen die Antragsgegnerin ein.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Wald Fenkraftal GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Wieland Skocdopole`(person)
- `Priv.-Doz.in Heidrun Aguera, BA MSc`(person)
- `Wald Fenkraftal GmbH & Co KG`(organisation)
- `Landesgericht für Strafsachen Wien`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/1Ob152_24w`) (sent_id: `deanon_260716_TRAIN/1Ob152_24w_3`)


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

**Example 8** (doc_id: `deanon_260716_TRAIN/1Ob29_20a`) (sent_id: `deanon_260716_TRAIN/1Ob29_20a_19`)


Der Mann hat sich an einem Immobilienprojekt, das von einer GmbH & Co KG verwirklicht wird, beteiligt.

**False Positives:**

- `GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_260716_TRAIN/2Ob194_19x`) (sent_id: `deanon_260716_TRAIN/2Ob194_19x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden und den Hofrat Dr. Musger, die Hofrätin Dr. Solé und die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Haßtenteufel Umwelt GmbH & Co KG, Peter Zauner Weg 324, 5273 Wesen, Österreich, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Klagenfurt, gegen die beklagte Partei Isaak Tomzak, vertreten durch Dr. Maximilian Motschiunig, Rechtsanwalt in Klagenfurt, wegen Vertragsaufhebung und Abgabe einer Willenserklärung (Streitwert 35.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 1. Oktober 2019, GZ 2 R 141/19a, 2 R 142/19y-95, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Haßtenteufel Umwelt GmbH & Co KG`

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

**Example 10** (doc_id: `deanon_260716_TRAIN/3Ob114_14g`) (sent_id: `deanon_260716_TRAIN/3Ob114_14g_4`)


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

**Example 11** (doc_id: `deanon_260716_TRAIN/3Ob114_14g`) (sent_id: `deanon_260716_TRAIN/3Ob114_14g_5`)


Begründung:  Rechtliche Beurteilung Die Erstklägerin (eine Rechtsanwalts KG), der Zweitkläger (deren Komplementär) und die Mutter des Zweitklägers (in Hinkunft: Pensionsberechtigte) führten als Kläger und Widerbeklagte ein Schiedsverfahren gegen den (hier) Beklagten (als ausgeschiedenen Komplementär) als Beklagten und Widerkläger, das mit einem Schiedsspruch vom 2. Mai 2011 endete.

**False Positives:**

- `Rechtsanwalts KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_260716_TRAIN/3Ob209_21p`) (sent_id: `deanon_260716_TRAIN/3Ob209_21p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei APHU Solar GmbH & Co KG, Hochkreuth 39, 8144 Bischofegg, Österreich, vertreten durch DDr. Heinz Dietmar Schimanko, Rechtsanwalt in Wien, gegen die beklagte Partei Traun-Transport GmbH, Stauderstraße 30, 8200 Pircha, Österreich, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH & Co KG in Wien, wegen 7.906,82 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 7. Juni 2021, GZ 38 R 66/21v-16, mit dem das Urteil des Bezirksgerichts Favoriten vom 19. Jänner 2021, GZ 3 C 503/20f-12, abgeändert wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `APHU Solar GmbH & Co KG`

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

**Example 13** (doc_id: `deanon_260716_TRAIN/3Ob45_19t`) (sent_id: `deanon_260716_TRAIN/3Ob45_19t_3`)


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

**Example 14** (doc_id: `deanon_260716_TRAIN/3Ob49_11v`) (sent_id: `deanon_260716_TRAIN/3Ob49_11v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie durch den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Julius ZYR Automotive GmbH & Co KG, Schamingstraße 16, 8262 Reigersberg, Österreich, vertreten durch Dr. Wolfgang Dartmann und andere Rechtsanwälte in Linz, wider die beklagten Parteien 1. Friedrich Strahsburg und 2.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `ZYR Automotive GmbH & Co KG`

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

**Example 15** (doc_id: `deanon_260716_TRAIN/4Ob119_22m`) (sent_id: `deanon_260716_TRAIN/4Ob119_22m_3`)


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

**Example 16** (doc_id: `deanon_260716_TRAIN/4Ob180_10i`) (sent_id: `deanon_260716_TRAIN/4Ob180_10i_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Nimtz Pharma GmbH, Mildenbergstraße 11, 3072 Furth, Österreich, vertreten durch Berger Saurer Zöchbauer, Rechtsanwälte in Wien, gegen die beklagten Parteien 1) Unikel Landwirtschaft GmbH & Co KG und 2) Gode+Panköker Getränke GmbH, Martinsplatz 1-31, 9831 Kleindorf, Österreich, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Provisorialverfahren 36.000 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 6. August 2010, GZ 5 R 150/10f-7, womit der Beschluss des Handelsgerichts Wien vom 24. Juni 2010, GZ 11 Cg 117/10h-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Unikel Landwirtschaft GmbH & Co KG`

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

**Example 17** (doc_id: `deanon_260716_TRAIN/4Ob196_10t`) (sent_id: `deanon_260716_TRAIN/4Ob196_10t_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Lemlemcon GmbH, Albert-Schultz-Eishalle 4, 6863 Großdorf, Österreich, vertreten durch Berger Saurer Zöchbauer, Rechtsanwälte in Wien, gegen die beklagten Parteien 1. Koldere und Heddrich Versicherung GmbH & Co KG, 2.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Koldere und Heddrich Versicherung GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schenk`(person)
- `Dr. Vogel`(person)
- `Dr. Jensik`(person)
- `Dr. Musger`(person)
- `Dr. Schwarzenbacher`(person)
- `Lemlemcon GmbH`(organisation)
- `Albert-Schultz-Eishalle 4, 6863 Großdorf, Österreich`(address)
- `Berger Saurer Zöchbauer, Rechtsanwälte`(organisation)
- `Koldere und Heddrich Versicherung GmbH & Co KG`(organisation)

**Example 18** (doc_id: `deanon_260716_TRAIN/5Ob146_16f`) (sent_id: `deanon_260716_TRAIN/5Ob146_16f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers Mag. Pamela Keilonat, vertreten durch Dr. Anke Reisch, Rechtsanwältin in Kitzbühel, gegen die Antragsgegnerin Hoch Dorfder GmbH & Co KG, Lichtensternweg 19, 4714 Meggenhofen, Österreich, vertreten durch Dr. Lisbeth Lass und Dr. Hans Christian Lass, Rechtsanwälte in Innsbruck, wegen § 52 Abs 1 Z 6 iVm § 20 Abs 3 WEG 2002, infolge des „außerordentlichen“ Revisionsrekurses des Antragstellers gegen den (richtig) Sachbeschluss des Landesgerichts Innsbruck vom 24. Mai 2016, GZ 4 R 128/16a-50, mit dem der Sachbeschluss des Bezirksgerichts Kitzbühel vom 14. März 2016, GZ 4 Msch 7/14x-36, abgeändert wurde, den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt. Begründung:  Rechtliche Beurteilung Der Antragsteller begehrt Rechnungslegung nach § 52 Abs 1 Z 6 iVm § 20 Abs 3 WEG 2002.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Hoch Dorfder GmbH & Co KG`

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

**Example 21** (doc_id: `deanon_260716_TRAIN/9ObA124_19d`) (sent_id: `deanon_260716_TRAIN/9ObA124_19d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Hopf als Vorsitzenden, die Hofrätin Dr. Fichtenau und den Hofrat Dr. Hargassner sowie die fachkundigen Laienrichter Dr. Peter Zeitler (aus dem Kreis der Arbeitnehmer) und Angela Taschek (aus dem Kreis der Arbeitgeber) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Bartscherer und Wagenknecht Holz GmbH & Co KG, Gotthelfgasse 57 - 74, 9361 Leimersberg, Österreich, vertreten durch Burgstaller & Preyer Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Richard Armgart, vertreten durch Mag. Franjo Schruiff, LL.M. Rechtsanwalt in Wien, wegen 14.927,23 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. August 2019, GZ 10 Ra 33/19z-30, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Bartscherer und Wagenknecht Holz GmbH & Co KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hopf`(person)
- `Dr. Fichtenau`(person)
- `Dr. Hargassner`(person)
- `Dr. Peter Zeitler`(person)
- `Bartscherer und Wagenknecht Holz GmbH & Co KG`(organisation)
- `Gotthelfgasse 57 - 74, 9361 Leimersberg, Österreich`(address)
- `Burgstaller & Preyer Rechtsanwälte GmbH`(organisation)
- `Richard Armgart`(person)
- `Mag. Franjo Schruiff, LL.M.`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 22** (doc_id: `deanon_260716_TRAIN/9ObA144_14p`) (sent_id: `deanon_260716_TRAIN/9ObA144_14p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden und die Hofräte des Obersten Gerichtshofs Mag. Ziegelbauer und Dr. Hargassner sowie die fachkundigen Laienrichter KR Mag. Paul Kunsky und Harald Kohlruss als weitere Richter in der Arbeitsrechtssache der klagenden Partei Franziska Schönmeier, vertreten durch Held Berdnik Astner & Partner Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Heizung Bachkraftlog GmbH & Co KG, Schlangglfeld 48, 4980 Viehausen, Österreich, vertreten durch die Klein, Wuntschek & Partner Rechtsanwälte GmbH in Graz, wegen Kündigungsanfechtung, über die außerordentliche Revision und den „Kostenrekurs“ der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 26. September 2014, GZ 7 Ra 66/14a-25, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `GmbH & Co KG` — partial — pred is substring of gold: `Heizung Bachkraftlog GmbH & Co KG`

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

## `Bezirksgericht_Grieskirchen` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d4143cce`  
**Description:**
Matches District Court Grieskirchen specifically.

**Content:**
```
\bBezirksgerichts?\s+Grieskirchen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `PVA_Abbreviation` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f8d063bd`  
**Description:**
Matches the abbreviation PVA (Pensionsversicherungsanstalt).

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

## `SAK_Abbreviation` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `93985d06`  
**Description:**
Matches the abbreviation SAK (Schweizer Ausgleichskasse).

**Content:**
```
\bSAK\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Schweizer_Ausgleichskasse_SAK` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `88d65288`  
**Description:**
Matches the full name 'Schweizer Ausgleichskasse SAK' including the abbreviation.

**Content:**
```
\bSchweizer\s+Ausgleichskasse\s+(?:SAK|\(SAK\))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wien_Telekom_Betriebe_GmbH` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `66a6c49d`  
**Description:**
Matches the specific entity 'Wien-Telekom Betriebe GmbH'.

**Content:**
```
\bWien\-[Tt]elekom\s+Betriebe\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `OGK_Abbreviation` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ec038233`  
**Description:**
Matches the abbreviation ÖGK (Österreichische Gebietskrankenkasse).

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

## `Vorarlberger_Gebietskrankenkasse` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `faeb40bb`  
**Description:**
Matches the specific entity 'Vorarlberger Gebietskrankenkasse'.

**Content:**
```
\bVorarlberger\s+Gebietskrankenkasse\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Landesgericht_Krems` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a11c5340`  
**Description:**
Matches Regional Courts for Krems an der Donau.

**Content:**
```
\bLandesgerichts?\s+(?:Krems\s+an\s+der\s+Donau)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Hyphenated_Gesellschaft_mbh` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b649abaa`  
**Description:**
Matches hyphenated corporate names ending in 'Gesellschaft mbH' (lowercase), e.g., 'WienTransport Werke -GesmbH'.

**Content:**
```
(?<![\w])([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*|[A-Z][a-zA-Z]+(?:-[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\+[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s+und\s+[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s*&\s*[A-Z][a-zA-Z]+)+|[A-Z][a-zA-Z]+(?:\s+&\s*[A-Z][a-zA-Z]+)+)\s*-GesmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Slash_Separated_Corporate_Name` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `38c29e5b`  
**Description:**
Matches corporate names with slash-separated components (e.g., 'urbanek/lind/schmied/reisch Rechtsanwälte OG').

**Content:**
```
(?<![\w])([A-Za-z]+(?:/[A-Za-z]+)+)\s+(?:Rechtsanwälte|Anwälte|Anwaltsgesellschaft)\s+(?:OG|KG|GmbH|mbH|GmbH\s+&\s+Co\s+KG)\b
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

