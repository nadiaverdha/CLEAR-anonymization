# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-08-19T18:59:54.579601

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
| Training documents | 2517 |
| Validation documents | 630 |
| Test documents | 477 |
| Train sentences | 4815 |
| Validation sentences | 1344 |
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
| Accuracy (exact match) | 96.4% |
| True Positives | 2074 |
| False Positives | 1230 |
| False Negatives | 2101 |
| Total Gold Entities | 4175 |
| Micro Precision | 62.8% |
| Micro Recall | 49.7% |
| Micro F1 | 55.5% |
| Macro F1 | 55.5% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Judge/Official Titles` | 56.8% | 66.9% | 49.3% | 3078 | 2059 | 1019 |
| `Against/Complaint Context` | 0.7% | 45.2% | 0.3% | 31 | 14 | 17 |
| `Representative Context` | 0.0% | 0.5% | 0.0% | 193 | 1 | 192 |
| `Complaint Case Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Herr/Frau Address` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Deceased Person Context` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Judge/Official Titles` 🏆

**F1:** 0.568 | **Precision:** 0.669 | **Recall:** 0.493  

**Format:** `regex`  
**Rule ID:** `21bec86d`  
**Description:**
Matches persons identified by judicial titles like Richter, Richterin, Mag., Dr., Prof., etc., specifically when preceded by 'durch' (by) or 'hat durch' (has by).

**Content:**
```
(?:durch\s+(?:die\s+)?(?:Richterin|Richter|Vorsitzender|Laienrichter)\s+)?(?:Mag\.?\.?\.?|Dr\.?\.?\.?|Univ\.-Prof\.?|Hon\.-Prof\.?|Priv\.-Doz\.?|Mag\.a|Dr\.in|LL\.M\.?)(?:\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)+
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.669 | 0.493 | 0.568 | 3078 | 2059 | 1019 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2059 | 1019 | 2116 |

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
| `Mag. Alexander Gerngross` | `Mag. Alexander Gerngross` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Jason Langeloh` (person)
- `Mag. Martin Rützler` (person)
- `Selma Einoeder` (person)
- `Mag. Klaus Köck` (person)
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

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Landesgericht Linz` (organisation)
- `Steidlen+Ysner Daten GmbH` (organisation)
- `Kaminweg 34, 8200 Laßnitzthal, Österreich` (address)
- `Verlag Waldlemder GmbH` (organisation)
- `Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich` (address)
- `Prof. Haslinger` (person)
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

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Bartholomäus Junghahn` (person)
- `HR Sophie Elefteriadis` (person)
- `Magistrat der Stadt Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Favoriten` (organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


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

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_3`)


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

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob15_12x`) (sent_id: `deanon_260716_TRAIN/10Ob15_12x_3`)


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

**Example 19** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


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

**Example 20** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludmilla von Amelunxen, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, gegen die beklagte Partei Svetlana Leinhäuser, vertreten durch Dr. Thomas Brückl, Mag. Christian Breit, Rechtsanwälte in Ried im Innkreis, wegen 1.778,52 EUR und Unterlassung (Streitwert 2.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Wels als Berufungsgericht vom 25. Jänner 2023, GZ 21 R 2/23b-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Grieskirchen vom 27. Oktober 2022, GZ 3 C 642/20h-27, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Mag. Ziegelbauer` | `Mag. Ziegelbauer` |
| `Dr. Faber` | `Dr. Faber` |
| `Mag. Schober` | `Mag. Schober` |
| `Dr. Annerl` | `Dr. Annerl` |
| `Dr. Bernhard Birek` | `Dr. Bernhard Birek` |
| `Mag. Christian Breit` | `Mag. Christian Breit` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Ludmilla von Amelunxen` (person)
- `Svetlana Leinhäuser` (person)
- `Dr. Thomas Brückl` (person)
- `Landesgerichts Wels` (organisation)
- `Bezirksgerichts Grieskirchen` (organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_3`)


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

**Example 22** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden, die Hofräte Mag. Schober, Dr. Annerl und Dr. Vollmaier sowie die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Ing. Mag. Pamela Gotterbauer, vertreten durch Mag. Helwig Schuster, Rechtsanwalt in Melk, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Mag. Schober` | `Mag. Schober` |
| `Dr. Annerl` | `Dr. Annerl` |
| `Dr. Vollmaier` | `Dr. Vollmaier` |
| `Mag. Helwig Schuster` | `Mag. Helwig Schuster` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Dr. Wallner-Friedl` (person)
- `Ing. Mag. Pamela Gotterbauer` (person)

**Example 23** (doc_id: `deanon_260716_TRAIN/10Ob18_13i`) (sent_id: `deanon_260716_TRAIN/10Ob18_13i_3`)


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

**Example 24** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Ralph Prusseit, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Akbayrak Metall GmbH, Schroateck 57, 4710 Niederweng, Österreich, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Steger` | `Dr. Steger` |
| `Dr. Annerl` | `Dr. Annerl` |
| `Mag. Franz Eckl` | `Mag. Franz Eckl` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Hon.-Prof. PD Dr. Rassi` (person)
- `Dr. Wallner-Friedl` (person)
- `Ralph Prusseit` (person)
- `Akbayrak Metall GmbH` (organisation)
- `Schroateck 57, 4710 Niederweng, Österreich` (address)
- `Skribe Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Krems an der Donau` (organisation)
- `Bezirksgerichts Zwettl` (organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_3`)


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

**Example 26** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_3`)


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

**Example 27** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_3`)


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

**Example 28** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_3`)


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

**Example 29** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_4`)


Malik Schoch, geboren 7. November 2002, 2. 7. Juli 2025, geboren 10. Juli 2004, und 3. Alan Schindlmair, geboren 7. August 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Timon Schönswetter, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Florian Kucera` | `Mag. Florian Kucera` |

**Missed by this rule (FN):**

- `Malik Schoch` (person)
- `7. November` (date)
- `7. Juli 2025` (date)
- `10. Juli` (date)
- `Alan Schindlmair` (person)
- `7. August` (date)
- `Mag. Timon Schönswetter` (person)
- `Doschek Rechtsanwalts GmbH` (organisation)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Döbling` (organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_3`)


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

**Example 31** (doc_id: `deanon_260716_TRAIN/10Ob26_10m`) (sent_id: `deanon_260716_TRAIN/10Ob26_10m_3`)


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

**Example 32** (doc_id: `deanon_260716_TRAIN/10Ob26_10m`) (sent_id: `deanon_260716_TRAIN/10Ob26_10m_5`)


Lars Ballogh, geboren am 3. Juli 2003, alle vertreten durch das Land Wien als Jugendwohlfahrtsträger (Amt für Jugend und Familie - Rechtsfürsorge Bezirke 17., 18. und 19., 1190 Wien, Gatterburggasse 12-14), wegen Unterhaltsvorschuss, über den „außerordentlichen Revisionsrekurs“ des Vaters Mag. Anton Bohmert, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. April 2009, GZ 44 R 193/08w-U140, womit der als Zulassungsvorstellung zu wertende „außerordentliche Revisionsrekurs“ des Vaters zurückgewiesen wurde, den Beschluss gefasst:  Spruch Der „außerordentliche Revisionsrekurs“ wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Anton Bohmert` | `Mag. Anton Bohmert` |

**Missed by this rule (FN):**

- `Lars Ballogh` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 33** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_3`)


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

**Example 34** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_41`)


Ein Schreiben von Dr. Hagen Janischewsky mit dem Inhalt, dass die Lizenzverträge einvernehmlich aufgehoben oder beendet worden seien, erreichte den Kläger nie.

| Predicted | Gold |
|---|---|
| `Dr. Hagen Janischewsky` | `Dr. Hagen Janischewsky` |

**Example 35** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Brigitte Martz, geboren am 16. November 1978, wegen Kontaktrechts des Vaters Dr. Gustav Thöning, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Madeleine Musialik, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

| Predicted | Gold |
|---|---|
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Dr. Grohmann` | `Dr. Grohmann` |
| `Mag. Ziegelbauer` | `Mag. Ziegelbauer` |
| `Dr. Madeleine Musialik` | `Dr. Madeleine Musialik` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Brigitte Martz` (person)
- `16. November 1978` (date)
- `Dr. Gustav Thöning` (person)
- `Pieler & Pieler & Partner KG` (organisation)
- `Kosch & Partner Rechtsanwälte GmbH` (organisation)
- `Landesgerichts Wiener Neustadt` (organisation)
- `Bezirksgerichts Wiener Neustadt` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 36** (doc_id: `deanon_260716_TRAIN/10Ob28_19v`) (sent_id: `deanon_260716_TRAIN/10Ob28_19v_3`)


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

**Example 37** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_3`)


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

**Example 38** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_6`)


11. 2008, GZ 38 Nc 13/08i-2, den Ablehnungsantrag des Mag. Herwig Berkenbrink in dessen Rekurs gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 13.

| Predicted | Gold |
|---|---|
| `Mag. Herwig Berkenbrink` | `Mag. Herwig Berkenbrink` |

**Missed by this rule (FN):**

- `Landesgerichts für Zivilrechtssachen Wien` (organisation)

**Example 39** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_9`)


Senat in der Besetzung Senatspräsidentin Dr. Sandra Hilt, Mag. Manuel Kumas und MMMag. Gottfried Fegbeitel mit Beschluss vom 3. 8. 2009, AZ 11 R 105/09f, keine Folge und verhängte über den Ablehnungswerber wegen beleidigender Äußerungen im Rechtsmittel eine Ordnungsstrafe von 1.600 EUR.

| Predicted | Gold |
|---|---|
| `Dr. Sandra Hilt` | `Dr. Sandra Hilt` |
| `Mag. Manuel Kumas` | `Mag. Manuel Kumas` |

**Missed by this rule (FN):**

- `MMMag. Gottfried Fegbeitel` (person)

**Example 40** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_13`)


Senat des Oberlandesgerichts Wien in der Besetzung Senatspräsidentin Dr. Paolo Barley sowie Mag. Klarissa Hausteiner und Mag. Viola Brauch als weitere Richter den Ablehnungsantrag des Ablehnungswerbers vom 24. 8. 2009 zurück.

| Predicted | Gold |
|---|---|
| `Dr. Paolo Barley` | `Dr. Paolo Barley` |
| `Mag. Klarissa Hausteiner` | `Mag. Klarissa Hausteiner` |
| `Mag. Viola Brauch` | `Mag. Viola Brauch` |

**Missed by this rule (FN):**

- `Oberlandesgerichts Wien` (organisation)

**Example 41** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_3`)


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

**Example 42** (doc_id: `deanon_260716_TRAIN/10Ob30_14f`) (sent_id: `deanon_260716_TRAIN/10Ob30_14f_3`)


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

**Example 43** (doc_id: `deanon_260716_TRAIN/10Ob30_19p`) (sent_id: `deanon_260716_TRAIN/10Ob30_19p_3`)


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

**Example 44** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende, den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber sowie die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Leander Andermann, vertreten durch Dr. Martin Leitner, Rechtsanwalt in Wien, gegen die beklagte Partei Ing. Ferdinand Abramova, vertreten durch Mag. Wilhelm Deutschmann MBA und Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M., Rechtsanwälte in Linz, wegen 500.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 11. Mai 2022, GZ 2 R 64/22b-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Ziegelbauer` | `Mag. Ziegelbauer` |
| `Dr. Faber` | `Dr. Faber` |
| `Mag. Schober` | `Mag. Schober` |
| `Dr. Annerl` | `Dr. Annerl` |
| `Dr. Martin Leitner` | `Dr. Martin Leitner` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Lovrek` (person)
- `Leander Andermann` (person)
- `Ing. Ferdinand Abramova` (person)
- `Mag. Wilhelm Deutschmann MBA` (person)
- `Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M.` (person)
- `Oberlandesgerichts Linz` (organisation)

**Example 45** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Mag. Korn` | `Mag. Korn` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Langhansl+Antonewitz Chemie AG` (organisation)
- `Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich` (address)
- `Poinstingl & Partner Rechtsanwälte OG` (organisation)
- `Drau-Pharma GmbH` (organisation)
- `Strazzegasse 12, 8762 Oberzeiring, Österreich` (address)
- `Mag. Johannes Bügler` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts Wiener Neustadt` (organisation)

**Example 46** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Karim Mielewczik, gegen die beklagte Partei Dr. Sandro Gädecken, vertreten durch Ing. Dr. Stefan Krall und Dr. Oliver Kühnl, Rechtsanwälte in Innsbruck, wegen 9.456 EUR sA (Revisionsinteresse 9.268,50 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 25. Februar 2025, GZ 21 R 434/24f-29, mit dem das Urteil des Bezirksgerichts Seekirchen am Wallersee vom 5. September 2024, GZ 2 C 1107/23d-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Annerl` | `Dr. Annerl` |
| `Dr. Vollmaier` | `Dr. Vollmaier` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Hon.-Prof. Dr. Nowotny` (person)
- `Hon.-Prof. PD Dr. Rassi` (person)
- `Dr. Wallner-Friedl` (person)
- `Karim Mielewczik` (person)
- `Dr. Sandro Gädecken` (person)
- `Ing. Dr. Stefan Krall` (person)
- `Dr. Oliver Kühnl` (person)
- `Landesgerichts Salzburg` (organisation)
- `Bezirksgerichts Seekirchen` (organisation)

**Example 47** (doc_id: `deanon_260716_TRAIN/10Ob3_12g`) (sent_id: `deanon_260716_TRAIN/10Ob3_12g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Maja Pirkmayr, vertreten durch Dr. Georg Gorton und DDr. Birgit Gorton, Rechtsanwälte in Klagenfurt, gegen die beklagte Partei Ing. Emanuel Puff, vertreten durch Dr. Gottfried Kassin, Rechtsanwalt in St. Veit an der Glan, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 26. Mai 2011, GZ 2 R 83/11z-49, mit dem das Urteil des Bezirksgerichts St. Veit an der Glan vom 29. Oktober 2010, GZ 3 C 333/09h-34, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hradil` | `Dr. Hradil` |
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Hoch` | `Dr. Hoch` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Dr. Georg Gorton` | `Dr. Georg Gorton` |
| `Dr. Gottfried Kassin` | `Dr. Gottfried Kassin` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Maja Pirkmayr` (person)
- `DDr. Birgit Gorton` (person)
- `Ing. Emanuel Puff` (person)
- `Landesgerichts Klagenfurt` (organisation)

**Example 48** (doc_id: `deanon_260716_TRAIN/10Ob3_23y`) (sent_id: `deanon_260716_TRAIN/10Ob3_23y_3`)


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

**Example 49** (doc_id: `deanon_260716_TRAIN/10Ob41_14y`) (sent_id: `deanon_260716_TRAIN/10Ob41_14y_3`)


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

**Example 50** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_3`)


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

**Example 51** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_4`)


Dr. Serge Schieferle, Niederlande, und 3.)

| Predicted | Gold |
|---|---|
| `Dr. Serge Schieferle` | `Dr. Serge Schieferle` |

**Example 52** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_5`)


Dr. Felix Cornils, Niederlande, beide vertreten durch Tramposch & Partner, Rechtsanwälte KG in Innsbruck, gegen die beklagte Partei Mag.a Constanze Rizzo, vertreten durch König Ermacora Klotz & Partner, Rechtsanwälte in Innsbruck, wegen je 15.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 1. Juli 2020, GZ 10 R 16/20h-49, mit dem das Urteil des Landesgerichts Innsbruck vom 6. Februar 2020, GZ 41 Cg 11/19i-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Felix Cornils` | `Dr. Felix Cornils` |
| `Mag.a Constanze Rizzo` | `Mag.a Constanze Rizzo` |

**Missed by this rule (FN):**

- `Tramposch & Partner, Rechtsanwälte KG` (organisation)
- `Oberlandesgerichts Innsbruck` (organisation)
- `Landesgerichts Innsbruck` (organisation)

**Example 53** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_3`)


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

**Example 54** (doc_id: `deanon_260716_TRAIN/10Ob43_19z`) (sent_id: `deanon_260716_TRAIN/10Ob43_19z_3`)


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

**Example 55** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_3`)


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

**Example 56** (doc_id: `deanon_260716_TRAIN/10Ob57_13z`) (sent_id: `deanon_260716_TRAIN/10Ob57_13z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der Kinder Mikolaj Eleftheriadou, geboren am 9. August 1991, Helge Schuchmann, geboren am 30. September 1992, mj Isabel Rahnfeld, geboren am 22. Dezember 1998 und mj PhD Daniel Coutand, geboren am 18. Jänner 2001, wegen Unterhaltsvorschuss, infolge Revisionsrekurses des Vaters Mag. Dirk Hükelheim, vertreten durch Mag. Roland Marko, Rechtsanwalt in Wien, dieser vertreten durch Dr. Francisco Rumpf, Rechtsanwalt in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 7. Juni 2013, GZ 43 R 391/08f ua -U-458, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 12. November 2007, GZ 2 P 88/07t-U-238, abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hradil` | `Dr. Hradil` |
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Hoch` | `Dr. Hoch` |
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Mag. Roland Marko` | `Mag. Roland Marko` |
| `Dr. Francisco Rumpf` | `Dr. Francisco Rumpf` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Mikolaj Eleftheriadou` (person)
- `Helge Schuchmann` (person)
- `Isabel Rahnfeld` (person)
- `PhD Daniel Coutand` (person)
- `Mag. Dirk Hükelheim` (person)
- `Landesgerichts für Zivilrechtssachen Wien` (organisation)
- `Bezirksgerichts Innere Stadt Wien` (organisation)

**Example 57** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_3`)


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

**Example 58** (doc_id: `deanon_260716_TRAIN/10Ob6_24s`) (sent_id: `deanon_260716_TRAIN/10Ob6_24s_3`)


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

**Example 59** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Ing. Christian Stangl-Brachnik, MA BA und Mag. Claudia Gründel (beide aus dem Kreis der Arbeitgeber) als weitere Richter in der Sozialrechtssache der klagenden Partei Mathias Jendl, vertreten durch Dr. Thomas Stampfer und Dr. Christoph Orgler, Rechtsanwälte in Graz, gegen die beklagte Partei Sozialversicherungsanstalt der Bauern, 1031 Wien, Ghegastraße 1, vertreten durch Dr. Michael Stögerer, Rechtsanwalt in Wien, wegen Ausgleichszulage, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2017, GZ 7 Rs 37/17s-11, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. April 2017, GZ 43 Cgs 113/17p-7, teils bestätigt und teils abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Schramm` | `Dr. Schramm` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Dr. Thomas Stampfer` | `Dr. Thomas Stampfer` |
| `Dr. Christoph Orgler` | `Dr. Christoph Orgler` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Ing. Christian Stangl-Brachnik, MA BA` (person)
- `Mag. Claudia Gründel` (person)
- `Mathias Jendl` (person)
- `Dr. Michael Stögerer` (person)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)

**Example 60** (doc_id: `deanon_260716_TRAIN/10ObS63_13g`) (sent_id: `deanon_260716_TRAIN/10ObS63_13g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, den Hofrat Dr. Fellinger und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter KR Hermann Furtner (aus dem Kreis der Arbeitgeber) und AR Angelika Neuhauser (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Birgit Jaros, vertreten durch Dr. Herbert Pochieser, Rechtsanwalt in Wien, gegen die beklagte Partei Wiener Gebietskrankenkasse, 1100 Wien, Wienerbergstraße 15-19, vertreten durch Dr. Heinz Edelmann, Rechtsanwalt in Wien, wegen Kostenerstattung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 11. September 2012, GZ 8 Rs 49/12b-28, womit das Urteil des Arbeits- und Sozialgerichts Wien vom 21. November 2011, GZ 17 Cgs 120/10a-24, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Hradil` | `Dr. Hradil` |
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Fichtenau` | `Dr. Fichtenau` |
| `Dr. Herbert Pochieser` | `Dr. Herbert Pochieser` |
| `Dr. Heinz Edelmann` | `Dr. Heinz Edelmann` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `KR Hermann Furtner` (person)
- `AR Angelika Neuhauser` (person)
- `Birgit Jaros` (person)
- `Wiener Gebietskrankenkasse` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 61** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_3`)


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

**Example 62** (doc_id: `deanon_260716_TRAIN/10ObS99_15d`) (sent_id: `deanon_260716_TRAIN/10ObS99_15d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die fachkundigen Laienrichter Mag. Dr. Wolfgang Höfle (aus dem Kreis der Arbeitgeber) und Ing. Thomas Bauer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Willibald Kollowrat, BEd, vertreten durch Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH in Graz, gegen die beklagte Partei Versicherungsanstalt für Eisenbahnen und Bergbau, Linke Wienzeile 48-52, 1060 Wien, vertreten durch Dr. Marie-Luise Safranek, Rechtsanwältin in Graz, wegen Wochengeld, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Juni 2015, GZ 7 Rs 28/15i-9, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 25. Februar 2015, GZ 36 Cgs 216/14d-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Fellinger` | `Dr. Fellinger` |
| `Dr. Schramm` | `Dr. Schramm` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Univ.-Prof. Dr. Neumayr` (person)
- `Mag. Dr. Wolfgang Höfle` (person)
- `Ing. Thomas Bauer` (person)
- `Willibald Kollowrat, BEd` (person)
- `Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH` (organisation)
- `Versicherungsanstalt für Eisenbahnen und Bergbau` (organisation)
- `Dr. Marie-Luise Safranek` (person)
- `Oberlandesgerichts Graz` (organisation)
- `Landesgerichts für Zivilrechtssachen Graz` (organisation)

**Example 63** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_3`)


Kopf Der Oberste Gerichtshof hat am 15. Jänner 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart der Richteramtsanwärterin Dr. Parapatits als Schriftführerin, in der Strafsache gegen Bernhard Buddäus und Norbert Wehrhahn wegen des Verbrechens des schweren Betrugs nach §§ 146, 147 Abs 3 StGB über die Nichtigkeitsbeschwerde und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 29. März 2012, GZ 31 Hv 51/10y-84, nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Angeklagten sowie des Verteidigers des Zweitangeklagten Mag. Rienmüller zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Zehetner` | `Dr. Zehetner` |
| `Dr. Schwab` | `Dr. Schwab` |
| `Mag. Lendl` | `Mag. Lendl` |
| `Mag. Michel` | `Mag. Michel` |
| `Dr. Oshidari` | `Dr. Oshidari` |
| `Dr. Parapatits` | `Dr. Parapatits` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Bernhard Buddäus` (person)
- `Norbert Wehrhahn` (person)
- `Landesgerichts Salzburg` (organisation)
- `Mag. Höpler` (person)
- `Mag. Rienmüller` (person)

**Example 64** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_3`)


Kopf Der Oberste Gerichtshof hat am 17. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Sommer als Schriftführer, in der Strafsache gegen Richard Lindt wegen des Vergehens der vorsätzlichen Beeinträchtigung der Umwelt nach § 180 Abs 2 Z 1, Z 2 StGB und einer weiteren strafbaren Handlung, AZ 40 Hv 147/10g des Landesgerichts Salzburg, über die Beschwerde des Genannten gegen den Beschluss dieses Gerichts vom 7. September 2011, ON 547, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Zehetner` | `Dr. Zehetner` |
| `Dr. Schwab` | `Dr. Schwab` |
| `Mag. Lendl` | `Mag. Lendl` |
| `Mag. Michel` | `Mag. Michel` |
| `Mag. Sommer` | `Mag. Sommer` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Richard Lindt` (person)
- `Landesgerichts Salzburg` (organisation)

**Example 65** (doc_id: `deanon_260716_TRAIN/11Os59_13f`) (sent_id: `deanon_260716_TRAIN/11Os59_13f_3`)


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

**Example 66** (doc_id: `deanon_260716_TRAIN/11Os67_16m`) (sent_id: `deanon_260716_TRAIN/11Os67_16m_3`)


Kopf Der Oberste Gerichtshof hat am 13. September 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Rathgeb als Schriftführerin in der Strafsache gegen Daniel Kur wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 1 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 22. April 2016, GZ 22 Hv 14/16s-43, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Schwab` | `Dr. Schwab` |
| `Mag. Michel` | `Mag. Michel` |
| `Dr. Oberressl` | `Dr. Oberressl` |
| `Mag. Rathgeb` | `Mag. Rathgeb` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Fürnkranz` (person)
- `Obersten Gerichtshofs` (organisation)
- `Daniel Kur` (person)
- `Landesgerichts Innsbruck` (organisation)

**Example 67** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_4`)


Augst 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Vizepräsidentin des Obersten Gerichtshofs Mag. Marek, die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Wieser als Schriftführerin in der Maßnahmenvollzugssache des Gerald Winand wegen bedingter Nachsicht einer mit Freiheitsentziehung verbundenen vorbeugenden Maßnahme (§ 21 Abs 1 StGB) über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien vom 16. Mai 2018, AZ 22 Bs 119/18p (AZ 606 Hv 1/17k des Landesgerichts Korneuburg), nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Schwab` | `Dr. Schwab` |
| `Mag. Marek` | `Mag. Marek` |
| `Dr. Oberressl` | `Dr. Oberressl` |
| `Mag. Wieser` | `Mag. Wieser` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Fürnkranz` (person)
- `Obersten Gerichtshofs` (organisation)
- `Gerald Winand` (person)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts Korneuburg` (organisation)

**Example 68** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_3`)


Kopf Der Oberste Gerichtshof hat am 18. März 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski im Verfahren zur Unterbringung des Mag. Herwig Bäseke in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB, AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz gemäß § 62 Abs 1 zweiter Satz OGH-Geo 2019 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger sowie Mag. Fürnkranz sind von der Entscheidung über die Anträge des Mag. Herwig Berto auf Erneuerung des Strafverfahrens AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, ausgeschlossen.

| Predicted | Gold |
|---|---|
| `Dr. Oshidari` | `Dr. Oshidari` |
| `Dr. Schwab` | `Dr. Schwab` |
| `Dr. Schwab` | `Dr. Schwab` |
| `Mag. Herwig Berto` | `Mag. Herwig Berto` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Herwig Bäseke` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Fürnkranz` (person)
- `OGH` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Fürnkranz` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 69** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_6`)


Senatspräsident des Obersten Gerichtshofs Dr. Schwab sowie Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz sind Mitglieder des zuständigen 11.

| Predicted | Gold |
|---|---|
| `Dr. Schwab` | `Dr. Schwab` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Mag. Fürnkranz` (person)

**Example 70** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_8`)


Der vorliegende Antrag des Mag. Herwig Bleuler bezieht sich auf das Urteil des Oberlandesgerichts Wien vom 21. August 2019, AZ 17 Bs 168/19h, mit dem der Berufung des Betroffenen gegen das Urteil des Landesgerichts für Strafsachen Wien vom 14. November 2018, GZ 22 Hv 7/18k-350, nicht Folge gegeben wurde.

| Predicted | Gold |
|---|---|
| `Mag. Herwig Bleuler` | `Mag. Herwig Bleuler` |

**Missed by this rule (FN):**

- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 71** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_3`)


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

**Example 72** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_4`)


2005 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab ist von der Entscheidung über die Beschwerde des Oliver Paukstat gegen den Beschluss des Oberlandesgerichts Wien vom 8. Februar 2016, AZ 32 Bs 12/16y, ausgeschlossen.

| Predicted | Gold |
|---|---|
| `Dr. Schwab` | `Dr. Schwab` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Oliver Paukstat` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 73** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_5`)


An Stelle der nunmehr als Vorsitzende einschreitenden Hofrätin des Obersten Gerichtshofs Dr. Bachner-Foregger tritt Hofrat des Obersten Gerichtshofs Dr. Nordmeyer.

| Predicted | Gold |
|---|---|
| `Dr. Nordmeyer` | `Dr. Nordmeyer` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)
- `Obersten Gerichtshofs` (organisation)

**Example 74** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_7`)


Senatspräsident des Obersten Gerichtshofs Dr. Schwab ist Vorsitzender des zuständigen 11.

| Predicted | Gold |
|---|---|
| `Dr. Schwab` | `Dr. Schwab` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)

**Example 75** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_9`)


An der angefochtenen Entscheidung des Oberlandesgerichts Wien hat die mit ihm in einem Angehörigenverhältnis im Sinne des § 72 StGB stehende Senatspräsidentin des Oberlandesgerichts Dr. Christine Schwab als Richterin mitgewirkt.

| Predicted | Gold |
|---|---|
| `Dr. Christine Schwab` | `Dr. Christine Schwab` |

**Missed by this rule (FN):**

- `Oberlandesgerichts Wien` (organisation)

**Example 76** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_10`)


Als deren Angehöriger (§ 72 StGB) ist Senatspräsident des Obersten Gerichtshofs Dr. Schwab gemäß § 43 Abs 3 StPO von der Entscheidung über die vorliegende Beschwerde ausgeschlossen.

| Predicted | Gold |
|---|---|
| `Dr. Schwab` | `Dr. Schwab` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)

**Example 77** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_11`)


Hofrat des Obersten Gerichtshofs Dr. Nordmeyer tritt aufgrund der laufenden Vertretungsregelung der Geschäftsverteilung des Obersten Gerichtshofs anstelle der nunmehr als Vorsitzende einschreitenden Hofrätin des Obersten Gerichtshofs Dr. Bachner-Foregger (§ 45 Abs 2 StPO).

| Predicted | Gold |
|---|---|
| `Dr. Nordmeyer` | `Dr. Nordmeyer` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Bachner-Foregger` (person)

**Example 78** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_3`)


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

**Example 79** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_4`)


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

**Example 80** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_5`)


An deren Stelle treten Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski.

| Predicted | Gold |
|---|---|
| `Dr. Nordmeyer` | `Dr. Nordmeyer` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)

**Example 81** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_7`)


Senatspräsident des Obersten Gerichtshofs Dr. Schwab ist Vorsitzender, Hofrätin des Obersten Gerichtshofs Mag. Michel ist Mitglied des zuständigen 11.

| Predicted | Gold |
|---|---|
| `Dr. Schwab` | `Dr. Schwab` |
| `Mag. Michel` | `Mag. Michel` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 82** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_9`)


1. Senatspräsident des Obersten Gerichtshofs Dr. Schwab zeigt seine Ausgeschlossenheit unter Hinweis auf die (Vor-)Entscheidung des Obersten Gerichtshofs vom 8. August 2013, GZ 12 Ns 48/13z-3, sowie den Umstand an, dass er mit Senatspräsidentin des Oberlandesgerichts Wien Dr. Christine Schwab, die an mehreren (vom Anzeiger im einzelnen bezeichneten) früheren Entscheidungen dieses Gerichts in dieser Sache mit Bezug auf die Prüfung des Tatverdachts teilgenommen hat, im Angehörigenverhältnis des § 72 StGB stehe.

| Predicted | Gold |
|---|---|
| `Dr. Schwab` | `Dr. Schwab` |
| `Dr. Christine Schwab` | `Dr. Christine Schwab` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Oberlandesgerichts Wien` (organisation)

**Example 83** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_15`)


Senatspräsident des Obersten Gerichtshofs Dr. Schwab ist damit von der Entscheidung über das vorliegende Rechtsmittel ausgeschlossen.

| Predicted | Gold |
|---|---|
| `Dr. Schwab` | `Dr. Schwab` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)

**Example 84** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_16`)


2. Hofrätin des Obersten Gerichtshofs Mag. Michel war in diesem Verfahren zu 1 OStA 74/08s als Staatsanwältin tätig, sodass sie gemäß § 43 Abs 1 Z 1 StPO als Richterin vom gesamten Verfahren ausgeschlossen ist.

| Predicted | Gold |
|---|---|
| `Mag. Michel` | `Mag. Michel` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)

**Example 85** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_17`)


3. An die Stelle der Ausgeschlossenen treten aufgrund der laufenden Vertretungsregelung Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski. (§ 45 Abs 2 StPO).

| Predicted | Gold |
|---|---|
| `Dr. Nordmeyer` | `Dr. Nordmeyer` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 86** (doc_id: `deanon_260716_TRAIN/12Ns94_11m`) (sent_id: `deanon_260716_TRAIN/12Ns94_11m_3`)


Kopf Der Oberste Gerichtshof hat am 28. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in der Strafsache gegen Mag. Herwig Bernts wegen des Vergehens des Widerstands gegen die Staatsgewalt nach § 269 Abs 1 erster Fall StGB und anderer strafbarer Handlungen, AZ 20 Hv 38/11f des Landesgerichts Linz, über den Antrag des Angeklagten auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

| Predicted | Gold |
|---|---|
| `Mag. Herwig Bernts` | `Mag. Herwig Bernts` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Schroll` (person)
- `Obersten Gerichtshofs` (organisation)
- `Hon.-Prof. Dr. Kirchbacher` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Landesgerichts Linz` (organisation)
- `OGH` (organisation)

**Example 87** (doc_id: `deanon_260716_TRAIN/12Ns94_11m`) (sent_id: `deanon_260716_TRAIN/12Ns94_11m_6`)


Der nunmehr vorliegende Antrag des Mag. Herwig Billmeir enthält gegenüber seinen früheren Anträgen kein neues Vorbringen, weshalb er zurückzuweisen war (res iudicata).

| Predicted | Gold |
|---|---|
| `Mag. Herwig Billmeir` | `Mag. Herwig Billmeir` |

**Example 88** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_3`)


Kopf Der Oberste Gerichtshof hat am 9. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Brenner und Dr. Setz-Hummel in der Strafsache gegen Ahmed Koehnen wegen des Verbrechens des Mordes nach § 75 StGB, AZ 606 Hv 1/11m des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit der Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

| Predicted | Gold |
|---|---|
| `Dr. Brenner` | `Dr. Brenner` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Setz-Hummel` (person)
- `Ahmed Koehnen` (person)
- `Landesgerichts für Strafsachen Wien` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `OGH` (organisation)

**Example 89** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_5`)


An ihre Stelle tritt Hofrat des Obersten Gerichtshofs Dr. Oshidari.

| Predicted | Gold |
|---|---|
| `Dr. Oshidari` | `Dr. Oshidari` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)

**Example 90** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_11`)


Hofrat des Obersten Gerichtshofs Dr. Oshidari tritt aufgrund der laufenden Vertretungsregelung der Geschäftsverteilung des Obersten Gerichtshofs an ihre Stelle (§ 45 Abs 2 StPO).

| Predicted | Gold |
|---|---|
| `Dr. Oshidari` | `Dr. Oshidari` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)

**Example 91** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Thomas Michenfelder wegen des Verbrechens des schweren gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 2 und Z 5, 129 Abs 1 Z 1, Z 2 und Z 3, 130 Abs 2 zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 38 Hv 40/18z des Landesgerichts Krems an der Donau, über die von der Generalprokuratur gegen den Beschluss des Präsidenten des Oberlandesgerichts Wien vom 17. Oktober 2018, AZ 130 Ns 31/18w, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Mag. Gföller und der Verteidigerin Dr. Zeh-Gindl zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Dr. Oshidari` | `Dr. Oshidari` |
| `Dr. Mann` | `Dr. Mann` |
| `Dr. Brenner` | `Dr. Brenner` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. T. Solé` (person)
- `Obersten Gerichtshofs` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Mag. Rögner` (person)
- `Thomas Michenfelder` (person)
- `Landesgerichts Krems an der Donau` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Mag. Gföller` (person)
- `Dr. Zeh-Gindl` (person)

**Example 92** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_5`)


Dieser Beschluss wird aufgehoben und es wird in der Sache selbst erkannt, dass der Senatspräsident des Oberlandesgerichts Wien Dr. Krenn sowie die Richterinnen des Oberlandesgerichts Wien Mag. Edwards und Mag. Sanda von der Entscheidung über die Berufung des Angeklagten gegen das Urteil des Landesgerichts Krems an der Donau vom 8. August 2018, GZ 38 Hv 40/18z-100, nicht ausgeschlossen sind.

| Predicted | Gold |
|---|---|
| `Dr. Krenn` | `Dr. Krenn` |
| `Mag. Edwards` | `Mag. Edwards` |
| `Mag. Sanda` | `Mag. Sanda` |

**Missed by this rule (FN):**

- `Oberlandesgerichts Wien` (organisation)
- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts Krems an der Donau` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc10_25i`) (sent_id: `deanon_260716_TRAIN/10Nc10_25i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Jason Langeloh, vertreten durch die Mag. Martin Rützler, Rechtsanwalt in Dornbirn, gegen die beklagte Partei, Selma Einoeder, vertreten durch Mag. Alexander Gerngross und Mag. Klaus Köck, Rechtsanwälte in Premstätten bei Graz, wegen 6.795,66 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 223 C 1313/24w des Bezirksgerichts Graz-Ost den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an das Bezirksgericht Dornbirn wird abgewiesen.

**False Positives:**

- `Hon.-Prof. Dr` — partial — pred is substring of gold: `Hon.-Prof. Dr. Nowotny`
- `Mag. Martin` — partial — pred is substring of gold: `Mag. Martin Rützler`
- `Mag. Klaus` — partial — pred is substring of gold: `Mag. Klaus Köck`

> overlaps gold: 3  |  likely missing annotation: 0

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

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Kordelia Meelis, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Fatima Tengel, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Kordelia Meelis`(person)
- `Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft`(organisation)
- `Fatima Tengel`(person)
- `Mag. Ernst Michael Lang`(person)

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der beim Landesgericht Linz zu AZ 3 Cg 46/21a anhängigen Rechtssache der klagenden Partei Hollengk Planung GmbH, Am Steindl 3, 9873 Döbriach, Österreich, vertreten durch Huber Berchtold Rechtsanwälte OG in Wien, gegen die beklagte Partei Wind Nexheimval GmbH, Wiesbergsiedlung 4, 8341 Pöllau, Österreich, vertreten durch ScherbaumSeebacher Rechtsanwälte GmbH in Graz, wegen 188.117,55 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN folgenden Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, zur Verhandlung und Entscheidung der Rechtssache anstelle des Landesgerichts Linz das Landesgericht Korneuburg zu bestimmen, wird abgewiesen.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc18_16b`) (sent_id: `deanon_260716_TRAIN/10Nc18_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Schramm als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Florens Drehkopf, LLB, geboren am 16. Dezember 1952, AZ 7 P 203/15g des Bezirksgerichts Mödling, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Mödling zurückgestellt.  Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc3_21d`) (sent_id: `deanon_260716_TRAIN/10Nc3_21d_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin mj Dietlind Schiewick, geboren 23. Oktober 2017, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger, (Bezirkshauptmannschaft Vöcklabruck, 4840 Vöcklabruck, Sportplatzstraße 1–3), deren Mutter Gisela Akcakaya, MSc, und des Antragsgegners Ernst Hartjens, Russische Föderation, wegen Feststellung der Abstammung, aufgrund der vom Bezirksgericht Josefstadt verfügten Vorlage des Akts AZ 23 Fam 2/21y zur Entscheidung gemäß § 111 Abs 2 JN den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Villach zurückgestellt.  Text Begründung: [1] Gegenstand des Verfahrens ist der Antrag auf Feststellung der Abstammung der zum Zeitpunkt der Antragstellung am 24.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 5** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie durch die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Hon.-Prof.in KzlR Iris Makowska, vertreten durch Skribe Rechtsanwaelte GmbH in Wien, gegen die beklagte Partei Dieter Apfelbacher Ltd, Am Fundbach 31w, 9170 Tratten, Österreich, wegen 400 EUR sA, über den Ordinationsantrag nach § 28 JN in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`

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

**Example 6** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Paulina Nüsken, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Oliver Eylart, Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Paulina Nüsken`(person)
- `Skribe Rechtsanwälte GmbH`(organisation)
- `Oliver Eylart`(person)
- `Bezirksgericht Schwechat`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/10Nc7_10a`) (sent_id: `deanon_260716_TRAIN/10Nc7_10a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger und Hon.-Prof. Dr. Neumayr als weitere Richter in der Verlassenschaftssache nach dem am 9. September 2009 verstorbenen, zuletzt in Zum Wetterkreuz 15, 5121 Hofstadt, Österreich, wohnhaft gewesenen Manfred Johann Puff, AZ 1 A 349/09w des Bezirksgerichts Kitzbühel, über den Delegierungsantrag der Karin Ciliberto, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, den B e s c h l u s s gefasst:  Spruch Dem Delegierungsantrag wird stattgegeben.

**False Positives:**

- `Hon.-Prof. Dr` — partial — pred is substring of gold: `Hon.-Prof. Dr. Neumayr`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 8** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Steidlen+Ysner Daten GmbH, Kaminweg 34, 8200 Laßnitzthal, Österreich, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Verlag Waldlemder GmbH, Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 9** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Rechtssache der klagenden Partei Mur Dorftalnex Technologien -GmbH, Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich, vertreten durch Dr. Peter Lechner und Dr. Hermann Pfurtscheller, Rechtsanwälte in Innsbruck, und ihrer Nebenintervenientin Ober Dertri GmbH, Hintereggweg 93, 2070 Kleinhöflein, Österreich, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Rudolf Ketelhut GmbH, Fiebrichgasse 17, 5120 Seeleiten, Österreich, vertreten durch Rechtsanwaltskanzlei Dr. Bernhard Hämmerle GmbH in Innsbruck, und ihrer Nebenintervenientin Völkertz Energie GmbH, Brunnbachweg 19, 4653 Mayersdorf, Österreich, vertreten durch Dr. Franz Pechmann, Rechtsanwalt in Wien, wegen 696.238,34 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck vom 2. Oktober 2009, GZ 4 R 108/09b-167, mit dem das Urteil des Landesgerichts Innsbruck vom 23. Februar 2009, GZ 41 Cg 228/01z-152, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

**False Positives:**

- `Hon.-Prof. Dr` — partial — pred is substring of gold: `Hon.-Prof. Dr. Neumayr`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 10** (doc_id: `deanon_260716_TRAIN/10Ob10_18w`) (sent_id: `deanon_260716_TRAIN/10Ob10_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Schneidergruberweg 37, 5132 Reith, Österreich, vertreten durch Dr. Alois Schneider, Rechtsanwalt in Rattenberg, wider die beklagte Partei Dario von Ebers, vertreten durch Dr. Walter Hausberger, Dr. Katharina Moritz und Dr. Alfred Schmidt, Rechtsanwälte in Wörgl, wegen Entfernung und Unterlassung (Revisionsinteresse 10.000 EUR), infolge Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 3. November 2017, GZ 3 R 172/17s-22, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Rattenberg vom 17. Mai 2017, GZ 3 C 401/15k-18, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`

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

**Example 11** (doc_id: `deanon_260716_TRAIN/10Ob11_11g`) (sent_id: `deanon_260716_TRAIN/10Ob11_11g_15`)


1. 2015 in Höhe von monatlich 210 EUR für den minderjährigen Dr.in Anna Javorsky, BEd und von 180 EUR für die minderjährige Klara Eppelmann.

**False Positives:**

- `Dr.in Anna Javorsky` — partial — pred is substring of gold: `Dr.in Anna Javorsky, BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Anna Javorsky, BEd`(person)
- `Klara Eppelmann`(person)

**Example 12** (doc_id: `deanon_260716_TRAIN/10Ob13_15g`) (sent_id: `deanon_260716_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Eva Abdelrahman, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei Hochenadel Immobilien GmbH, Ritterhof 11, 2661 Graben, Österreich, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`
- `Dr. Karl` — partial — pred is substring of gold: `Dr. Karl-Heinz Plankel`

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

**Example 13** (doc_id: `deanon_260716_TRAIN/10Ob13_23v`) (sent_id: `deanon_260716_TRAIN/10Ob13_23v_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Juri Gerstl GmbH, Mutten 18, 3251 Schauboden, Österreich, vertreten durch Dr. Ralph Trischler, Rechtsanwalt in Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, sowie die Nebenintervenientin auf Seiten der beklagten Partei Bundesbeschaffung GmbH, 1020 Wien, Lassallestraße 9b, vertreten durch die Olischar Rechtsanwaltsgesellschaft mbH in Wien, wegen 15.535 EUR sA, über den Revisionsrekurs der klagenden Partei (Revisionsinteresse: 7.460 EUR), gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 23. Februar 2023, GZ 16 R 168/22a-20, mit welchem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 5. September 2022, GZ 11 Cg 48/22t-12, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Hon.-Prof. Dr` — partial — pred is substring of gold: `Hon.-Prof. Dr. Lovrek`

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

**Example 14** (doc_id: `deanon_260716_TRAIN/10Ob15_16b`) (sent_id: `deanon_260716_TRAIN/10Ob15_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des minderjährigen Cedric Annamüller, geboren am 8. März 2007, 16. Mai 1964, vertreten durch das Land Kärnten als Kinder- und Jugendhilfeträger (Magistrat der Landeshauptstadt Klagenfurt, Abteilung für Jugend und Familie, Bahnhofstraße 35, 9010 Klagenfurt am Wörthersee), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Graz, gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 8. Jänner 2016, GZ 4 R 283/15g-16, womit der Beschluss des Bezirksgerichts Klagenfurt vom 17. November 2015, GZ 1 Pu 69/10x-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`

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

**Example 15** (doc_id: `deanon_260716_TRAIN/10Ob15_23p`) (sent_id: `deanon_260716_TRAIN/10Ob15_23p_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludmilla von Amelunxen, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, gegen die beklagte Partei Svetlana Leinhäuser, vertreten durch Dr. Thomas Brückl, Mag. Christian Breit, Rechtsanwälte in Ried im Innkreis, wegen 1.778,52 EUR und Unterlassung (Streitwert 2.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Wels als Berufungsgericht vom 25. Jänner 2023, GZ 21 R 2/23b-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Grieskirchen vom 27. Oktober 2022, GZ 3 C 642/20h-27, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Hon.-Prof. Dr` — partial — pred is substring of gold: `Hon.-Prof. Dr. Lovrek`
- `Dr. Thomas Br` — partial — pred is substring of gold: `Dr. Thomas Brückl`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 16** (doc_id: `deanon_260716_TRAIN/10Ob16_16z`) (sent_id: `deanon_260716_TRAIN/10Ob16_16z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Mag. Kevin Maassen, vertreten durch Dr. Clemens Lintschinger, Rechtsanwalt in Wien, gegen die beklagte Partei Hon.-Prof. Friedhelm Adde, vertreten durch Mag. Dr. Georg Backhausen, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 27. Jänner 2016, GZ 38 R 265/15z-45, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`
- `Mag. Dr` — partial — pred is substring of gold: `Mag. Dr. Georg Backhausen`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob16_24m`) (sent_id: `deanon_260716_TRAIN/10Ob16_24m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden, die Hofräte Mag. Schober, Dr. Annerl und Dr. Vollmaier sowie die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Ing. Mag. Pamela Gotterbauer, vertreten durch Mag. Helwig Schuster, Rechtsanwalt in Melk, gegen die beklagten Parteien 1.

**False Positives:**

- `Hon.-Prof. Dr` — partial — pred is substring of gold: `Hon.-Prof. Dr. Nowotny`
- `Dr. Wallner` — partial — pred is substring of gold: `Dr. Wallner-Friedl`
- `Mag. Pamela Gotterbauer` — partial — pred is substring of gold: `Ing. Mag. Pamela Gotterbauer`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Nowotny`(person)
- `Mag. Schober`(person)
- `Dr. Annerl`(person)
- `Dr. Vollmaier`(person)
- `Dr. Wallner-Friedl`(person)
- `Ing. Mag. Pamela Gotterbauer`(person)
- `Mag. Helwig Schuster`(person)

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob18_25g`) (sent_id: `deanon_260716_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Ralph Prusseit, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Akbayrak Metall GmbH, Schroateck 57, 4710 Niederweng, Österreich, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Hon.-Prof. Dr` — partial — pred is substring of gold: `Hon.-Prof. Dr. Nowotny`
- `Dr. Rassi` — partial — pred is substring of gold: `Hon.-Prof. PD Dr. Rassi`
- `Dr. Wallner` — partial — pred is substring of gold: `Dr. Wallner-Friedl`

> overlaps gold: 3  |  likely missing annotation: 0

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

**Example 19** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Heimcon Software GmbH, H - Am Hang 3, 4912 Rettenbrunn, Österreich, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, gegen die beklagte Partei Gunter Landwirtschaft GmbH, Schlossfeld 38, 9300 Graßdorf, Österreich, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, wegen 7.731,06 EUR und Feststellung (Streitwert 20.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse insgesamt 11.597,42 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 216/14h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`

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

**Example 20** (doc_id: `deanon_260716_TRAIN/10Ob22_10y`) (sent_id: `deanon_260716_TRAIN/10Ob22_10y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der minderjährigen Annabelle Thurnher, geboren am 24. Juni 2001, vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung, Bezirk 10, 1100 Wien, Van der Nüll-Gasse 20), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 17. September 2009, GZ 44 R 454/09d-38, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Favoriten vom 16. Juni 2009, GZ 40 P 36/08f-U-26, teilweise abgeändert wurde, den B e s c h l u s s gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Hon.-Prof. Dr` — partial — pred is substring of gold: `Hon.-Prof. Dr. Neumayr`

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

**Example 21** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei DDr.in Cornelia Rinaldo, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Conmon-Verlag Limited, Kroisegg 20, 4052 Fleckendorf, Österreich Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`
- `Dr.in Cornelia Rinaldo` — partial — pred is substring of gold: `DDr.in Cornelia Rinaldo`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 22** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der Kinder 1.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)

**Example 23** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_4`)


Malik Schoch, geboren 7. November 2002, 2. 7. Juli 2025, geboren 10. Juli 2004, und 3. Alan Schindlmair, geboren 7. August 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Timon Schönswetter, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Mag. Timon Sch` — partial — pred is substring of gold: `Mag. Timon Schönswetter`

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

**Example 24** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_3`)


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

**Example 25** (doc_id: `deanon_260716_TRAIN/10Ob26_10m`) (sent_id: `deanon_260716_TRAIN/10Ob26_10m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der mj 1.)

**False Positives:**

- `Hon.-Prof. Dr` — partial — pred is substring of gold: `Hon.-Prof. Dr. Neumayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schinko`(person)
- `Dr. Fellinger`(person)
- `Dr. Hoch`(person)
- `Hon.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)

**Example 26** (doc_id: `deanon_260716_TRAIN/10Ob26_14t`) (sent_id: `deanon_260716_TRAIN/10Ob26_14t_5`)


Unter Alver GmbH, beide Granglitzweg 11, 3251 Kroißenberg, Österreich, beide vertreten durch Dr. Michael Schneditz-Bolfras und andere Rechtsanwälte in Gmunden, wegen Bucheinsicht (in eventu Rechnungslegung) und Zahlung (Streitwert: 70.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Teilurteil des Oberlandesgerichts Linz als Berufungsgericht vom 17. Februar 2014, GZ 3 R 13/14y-90, womit das Urteil des Landesgerichts Wels vom 27. November 2013 (in der mit Beschluss vom 12. Dezember 2013 berichtigten Fassung), GZ 2 Cg 78/10p-82 und -84, abgeändert wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Michael Schneditz` — partial — pred is substring of gold: `Dr. Michael Schneditz-Bolfras`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unter Alver GmbH`(organisation)
- `Granglitzweg 11, 3251 Kroißenberg, Österreich`(address)
- `Dr. Michael Schneditz-Bolfras`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Wels`(organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Brigitte Martz, geboren am 16. November 1978, wegen Kontaktrechts des Vaters Dr. Gustav Thöning, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Madeleine Musialik, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`
- `Dr. Gustav Th` — partial — pred is substring of gold: `Dr. Gustav Thöning`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 28** (doc_id: `deanon_260716_TRAIN/10Ob28_19v`) (sent_id: `deanon_260716_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Bau Zorostfurt GmbH, Isbarystraße 47, 4152 Schölling, Österreich, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Buitenkamp und Rothauge Landwirtschaft GmbH, Gewerbegebiet Mathon 17, 3672 Reitern, Österreich, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`

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

**Example 29** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der zur AZ 38 Nc 13/08i beim Landesgericht für Zivilrechtssachen Wien anhängigen Ablehnungssache des Ablehnungswerbers Mag. Herwig Bortzlaff, über den Rekurs des Ablehnungswerbers gegen den Beschluss des Oberlandesgerichts Wien vom 10. November 2009, GZ 13 Nc 14/09x-2, womit ein Ablehnungsantrag zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Hon.-Prof. Dr` — partial — pred is substring of gold: `Hon.-Prof. Dr. Neumayr`

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

**Example 30** (doc_id: `deanon_260716_TRAIN/10Ob2_10g`) (sent_id: `deanon_260716_TRAIN/10Ob2_10g_9`)


Senat in der Besetzung Senatspräsidentin Dr. Sandra Hilt, Mag. Manuel Kumas und MMMag. Gottfried Fegbeitel mit Beschluss vom 3. 8. 2009, AZ 11 R 105/09f, keine Folge und verhängte über den Ablehnungswerber wegen beleidigender Äußerungen im Rechtsmittel eine Ordnungsstrafe von 1.600 EUR.

**False Positives:**

- `Mag. Gottfried Fegbeitel` — partial — pred is substring of gold: `MMMag. Gottfried Fegbeitel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Sandra Hilt`(person)
- `Mag. Manuel Kumas`(person)
- `MMMag. Gottfried Fegbeitel`(person)

**Example 31** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Jaden Meyerjohann, geboren am 3. Juli 2020, Leroy Jungschmidt, geboren am 28. Mai 1965 und Clemens Theocharakis, geboren am 25. März 1999, in Pflege und Erziehung der Mutter Emanuela Janischefsky, vertreten durch das Land Vorarlberg als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Feldkirch, Schlossgraben 1, 6800 Feldkirch), wegen Gewährung von Unterhaltsvorschuss, über den Revisionsrekurs des Vaters Ashley Biesert, vertreten durch Mag. Hans-Christian Obernberger, Rechtsanwalt in Feldkirch, gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 12. Juli 2011, GZ 3 R 198/11g, 3 R 199/11d, 3 R 200/11a-18, womit die Beschlüsse des Bezirksgerichts Feldkirch vom 18. Mai 2011, GZ 12 Pu 141/11f-4 bis 6, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Mag. Hans` — partial — pred is substring of gold: `Mag. Hans-Christian Obernberger`

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

**Example 32** (doc_id: `deanon_260716_TRAIN/10Ob2_14p`) (sent_id: `deanon_260716_TRAIN/10Ob2_14p_81`)


Nach dem Unterhaltsherabsetzungsantrag des Vaters vom 20. 12. 2011 (Band I, ON 29 und ON 30) wurde mit der Vorschussgewährung ohnehin bereits teilweise innegehalten, sodass anstatt der ursprünglich gewährten 791,50 EUR monatlich pro Kind nunmehr - wie der Vater beantragte - nur noch monatliche Unterhaltsvorschüsse von 300 EUR für Delila Maschmeier, 340 EUR für DDr.in Helena Jakobskötter und 330 EUR für Jaromir Tägder zur Auszahlung gelangen (Band I, ON 31, vgl auch Band II, ON 75, womit das Rekursgericht dem Erstgericht die Fortsetzung des Unterhaltsherabsetzungsverfahrens auftrug).

**False Positives:**

- `Dr.in Helena Jakobsk` — partial — pred is substring of gold: `DDr.in Helena Jakobskötter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Delila Maschmeier`(person)
- `DDr.in Helena Jakobskötter`(person)
- `Jaromir Tägder`(person)

**Example 33** (doc_id: `deanon_260716_TRAIN/10Ob30_19p`) (sent_id: `deanon_260716_TRAIN/10Ob30_19p_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der minderjährigen Maja Dolleschell, geboren 14. August 2009, vertreten durch das Land Niederösterreich als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Melk, 3390 Melk, Abt Karl-Straße 25a) wegen Unterhaltsvorschüssen, über den Revisionsrekurs des Kindes gegen den Beschluss des Landesgerichts St. Pölten als Rekursgericht vom 23. Jänner 2019, GZ 23 R 6/19h-52, mit dem der Beschluss des Bezirksgerichts Melk vom 21. November 2018, GZ 22 Pu 194/16m-42, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`

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

**Example 34** (doc_id: `deanon_260716_TRAIN/10Ob32_22m`) (sent_id: `deanon_260716_TRAIN/10Ob32_22m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende, den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber sowie die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Leander Andermann, vertreten durch Dr. Martin Leitner, Rechtsanwalt in Wien, gegen die beklagte Partei Ing. Ferdinand Abramova, vertreten durch Mag. Wilhelm Deutschmann MBA und Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M., Rechtsanwälte in Linz, wegen 500.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 11. Mai 2022, GZ 2 R 64/22b-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Hon.-Prof. Dr` — partial — pred is substring of gold: `Hon.-Prof. Dr. Lovrek`
- `Mag. Wilhelm Deutschmann` — partial — pred is substring of gold: `Mag. Wilhelm Deutschmann MBA`
- `Priv.-Doz. Mag` — partial — pred is substring of gold: `Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M.`
- `Dr. Henriette Boscheinen` — partial — pred is substring of gold: `Priv.-Doz. Mag. Dr. Henriette Boscheinen-Duursma LL.M., MAS, LL.M.`

> overlaps gold: 4  |  likely missing annotation: 0

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

**Example 35** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`
- `Mag. Johannes` — partial — pred is substring of gold: `Mag. Johannes Bügler`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 36** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Karim Mielewczik, gegen die beklagte Partei Dr. Sandro Gädecken, vertreten durch Ing. Dr. Stefan Krall und Dr. Oliver Kühnl, Rechtsanwälte in Innsbruck, wegen 9.456 EUR sA (Revisionsinteresse 9.268,50 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 25. Februar 2025, GZ 21 R 434/24f-29, mit dem das Urteil des Bezirksgerichts Seekirchen am Wallersee vom 5. September 2024, GZ 2 C 1107/23d-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Hon.-Prof. Dr` — partial — pred is substring of gold: `Hon.-Prof. Dr. Nowotny`
- `Dr. Rassi` — partial — pred is substring of gold: `Hon.-Prof. PD Dr. Rassi`
- `Dr. Wallner` — partial — pred is substring of gold: `Dr. Wallner-Friedl`
- `Dr. Sandro` — partial — pred is substring of gold: `Dr. Sandro Gädecken`
- `Dr. Stefan Krall` — partial — pred is substring of gold: `Ing. Dr. Stefan Krall`
- `Dr. Oliver` — partial — pred is substring of gold: `Dr. Oliver Kühnl`

> overlaps gold: 6  |  likely missing annotation: 0

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

**Example 37** (doc_id: `deanon_260716_TRAIN/10Ob3_12g`) (sent_id: `deanon_260716_TRAIN/10Ob3_12g_3`)


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

**Example 38** (doc_id: `deanon_260716_TRAIN/10Ob41_14y`) (sent_id: `deanon_260716_TRAIN/10Ob41_14y_3`)


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

**Example 39** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Parteien 2.)

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)

**Example 40** (doc_id: `deanon_260716_TRAIN/10Ob42_15x`) (sent_id: `deanon_260716_TRAIN/10Ob42_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Pflegschaftssache 1. der mj Emma Mittelstaedt, geboren am 21. Mai 2025 und 2. des mj Milena Roesche, geboren am 25. Juni 1957, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung Bezirk 22, 1220 Wien, Hirschstettner Straße 19-21/Stiege N), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 10. Dezember 2014, GZ 42 R 343/13x, 42 R 344/13v und 42 R 345/13s-106, womit den Rekursen der Minderjährigen gegen den Beschluss des Bezirksgerichts Donaustadt vom 14. März 2013, GZ 3 Pu 61/12x-40, teilweise Folge gegeben wurde (Pkt 1 des Spruchs), dem Rekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen die Beschlüsse des Bezirksgerichts Donaustadt (jeweils) vom 6. Juni 2013, GZ 3 Pu 61/12x-49 und 3 Pu 61/12x-50, Folge gegeben (Pkt 2a des Spruchs), und aus Anlass des Rekurses die Anträge der Minderjährigen auf Gewährung von Unterhaltsvorschüssen zur Gänze abgewiesen wurden (Pkt 2b des Spruchs), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 41** (doc_id: `deanon_260716_TRAIN/10Ob43_19z`) (sent_id: `deanon_260716_TRAIN/10Ob43_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Othmar Mertl, vertreten durch Nitsch Pajor Zöllner Rechtsanwälte OG in Mödling, gegen die beklagte Partei Stadtgemeinde Malik Fridt, vertreten durch Krist Bubits Rechtsanwälte OG in Mödling, wegen 1.) 21.216,92 EUR sA und 2.) Feststellung (Streitwert: 2.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Februar 2019, GZ 12 R 96/18b-36, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Wiener Neustadt vom 31. August 2018, GZ 20 Cg 86/17h-31, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`

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

**Example 42** (doc_id: `deanon_260716_TRAIN/10Ob4_17m`) (sent_id: `deanon_260716_TRAIN/10Ob4_17m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und den Hofrat Dr. Schramm, die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Familienrechtssache der Antragstellerin Scarlett Achatzi, gegen den Antragsgegner Mag. Ewald Aszmutat, wegen Unterhalt, infolge Rekurses des Antragsgegners gegen den Beschluss des Oberlandesgerichts Wien vom 4. Jänner 2017, GZ 12 Nc 28/16h-3, womit der Ablehnungsantrag des Antragsgegners zurückgewiesen wurde, sowie über den Ablehnungsantrag gegen alle Richter des Oberlandesgerichts Wien, folgenden Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Schramm`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Mag. Ziegelbauer`(person)
- `Scarlett Achatzi`(person)
- `Mag. Ewald Aszmutat`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/10Ob57_13z`) (sent_id: `deanon_260716_TRAIN/10Ob57_13z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der Kinder Mikolaj Eleftheriadou, geboren am 9. August 1991, Helge Schuchmann, geboren am 30. September 1992, mj Isabel Rahnfeld, geboren am 22. Dezember 1998 und mj PhD Daniel Coutand, geboren am 18. Jänner 2001, wegen Unterhaltsvorschuss, infolge Revisionsrekurses des Vaters Mag. Dirk Hükelheim, vertreten durch Mag. Roland Marko, Rechtsanwalt in Wien, dieser vertreten durch Dr. Francisco Rumpf, Rechtsanwalt in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 7. Juni 2013, GZ 43 R 391/08f ua -U-458, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 12. November 2007, GZ 2 P 88/07t-U-238, abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Mag. Dirk` — partial — pred is substring of gold: `Mag. Dirk Hükelheim`

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

**Example 44** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Cassandra Wespi, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Bilek Lebensmittel GmbH in Liqu, Dreijochgasse 11, 4722 Stefansdorf, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`

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

**Example 45** (doc_id: `deanon_260716_TRAIN/10Ob6_24s`) (sent_id: `deanon_260716_TRAIN/10Ob6_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Dr. Weber, Mag. Schober, Dr. Annerl und Dr. Vollmaier als weitere Richter in der Rechtssache des (ehemaligen) Klägers und Gegners der gefährdeten Parteien Agatha von der Heide, vertreten durch MMag. Dr. Sebastian Pribas, Rechtsanwalt in Dornbirn, als Verfahrenshelfer, dieser vertreten durch Mag. Benedikt Walch, Rechtsanwalt in Lech am Arlberg, gegen die (ehemals) Beklagte und erstgefährdete Partei Alva Sengül, sowie die zweitgefährdete Partei mj Selina Birkmeir, und die drittgefährdete Partei mj Harald Ladwig, LLM, alle wohnhaft in In der Klaus 72, 4785 Bach, Österreich, und vertreten durch Mag. German Bertsch, Rechtsanwalt in Feldkirch, wegen Ehescheidung sowie einstweiligem Ehegatten- und Kindesunterhalt, über den außerordentlichen Revisionsrekurs des Gegners der gefährdeten Parteien gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 22. September 2022, GZ 3 R 187/22f-323, womit der Beschluss des Bezirksgerichts Feldkirch vom 29. April 2022, GZ 2 C 23/17g-306, bestätigt wurde, den Beschluss gefasst:  Spruch In Ansehung der auf Zahlung von einstweiligem Ehegattenunterhalt gerichteten Begehren wird der außerordentliche Revisionsrekurs gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Hon.-Prof. Dr` — partial — pred is substring of gold: `Hon.-Prof. Dr. Nowotny`
- `Mag. Dr` — partial — pred is substring of gold: `MMag. Dr. Sebastian Pribas`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 46** (doc_id: `deanon_260716_TRAIN/10ObS150_17g`) (sent_id: `deanon_260716_TRAIN/10ObS150_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Ing. Christian Stangl-Brachnik, MA BA und Mag. Claudia Gründel (beide aus dem Kreis der Arbeitgeber) als weitere Richter in der Sozialrechtssache der klagenden Partei Mathias Jendl, vertreten durch Dr. Thomas Stampfer und Dr. Christoph Orgler, Rechtsanwälte in Graz, gegen die beklagte Partei Sozialversicherungsanstalt der Bauern, 1031 Wien, Ghegastraße 1, vertreten durch Dr. Michael Stögerer, Rechtsanwalt in Wien, wegen Ausgleichszulage, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2017, GZ 7 Rs 37/17s-11, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. April 2017, GZ 43 Cgs 113/17p-7, teils bestätigt und teils abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`
- `Mag. Claudia Gr` — partial — pred is substring of gold: `Mag. Claudia Gründel`
- `Dr. Michael St` — partial — pred is substring of gold: `Dr. Michael Stögerer`

> overlaps gold: 3  |  likely missing annotation: 0

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

**Example 47** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Roland Soukup, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 48** (doc_id: `deanon_260716_TRAIN/10ObS99_15d`) (sent_id: `deanon_260716_TRAIN/10ObS99_15d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die fachkundigen Laienrichter Mag. Dr. Wolfgang Höfle (aus dem Kreis der Arbeitgeber) und Ing. Thomas Bauer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Willibald Kollowrat, BEd, vertreten durch Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH in Graz, gegen die beklagte Partei Versicherungsanstalt für Eisenbahnen und Bergbau, Linke Wienzeile 48-52, 1060 Wien, vertreten durch Dr. Marie-Luise Safranek, Rechtsanwältin in Graz, wegen Wochengeld, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Juni 2015, GZ 7 Rs 28/15i-9, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 25. Februar 2015, GZ 36 Cgs 216/14d-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. Neumayr`
- `Mag. Dr` — partial — pred is substring of gold: `Mag. Dr. Wolfgang Höfle`
- `Dr. Reinhard` — partial — pred is substring of gold: `Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH`
- `Dr. Marie` — partial — pred is substring of gold: `Dr. Marie-Luise Safranek`

> overlaps gold: 4  |  likely missing annotation: 0

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

**Example 49** (doc_id: `deanon_260716_TRAIN/11Os113_12w`) (sent_id: `deanon_260716_TRAIN/11Os113_12w_3`)


Kopf Der Oberste Gerichtshof hat am 15. Jänner 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter, in Gegenwart der Richteramtsanwärterin Dr. Parapatits als Schriftführerin, in der Strafsache gegen Bernhard Buddäus und Norbert Wehrhahn wegen des Verbrechens des schweren Betrugs nach §§ 146, 147 Abs 3 StGB über die Nichtigkeitsbeschwerde und die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 29. März 2012, GZ 31 Hv 51/10y-84, nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Höpler, der Angeklagten sowie des Verteidigers des Zweitangeklagten Mag. Rienmüller zu Recht erkannt:  Spruch

**False Positives:**

- `Mag. Rienm` — partial — pred is substring of gold: `Mag. Rienmüller`

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
- `Dr. Parapatits`(person)
- `Bernhard Buddäus`(person)
- `Norbert Wehrhahn`(person)
- `Landesgerichts Salzburg`(organisation)
- `Mag. Höpler`(person)
- `Mag. Rienmüller`(person)

**Example 50** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_3`)


Kopf Der Oberste Gerichtshof hat am 17. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Sommer als Schriftführer, in der Strafsache gegen Richard Lindt wegen des Vergehens der vorsätzlichen Beeinträchtigung der Umwelt nach § 180 Abs 2 Z 1, Z 2 StGB und einer weiteren strafbaren Handlung, AZ 40 Hv 147/10g des Landesgerichts Salzburg, über die Beschwerde des Genannten gegen den Beschluss dieses Gerichts vom 7. September 2011, ON 547, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Dr. Michel` — partial — pred is substring of gold: `Dr. Michel-Kwapinski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Zehetner`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Mag. Lendl`(person)
- `Mag. Michel`(person)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Sommer`(person)
- `Richard Lindt`(person)
- `Landesgerichts Salzburg`(organisation)

**Example 51** (doc_id: `deanon_260716_TRAIN/11Os67_16m`) (sent_id: `deanon_260716_TRAIN/11Os67_16m_3`)


Kopf Der Oberste Gerichtshof hat am 13. September 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Rathgeb als Schriftführerin in der Strafsache gegen Daniel Kur wegen des Verbrechens des schweren Raubes nach §§ 142 Abs 1, 143 Abs 1 zweiter Fall StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten sowie über die Berufung der Staatsanwaltschaft gegen das Urteil des Landesgerichts Innsbruck als Schöffengericht vom 22. April 2016, GZ 22 Hv 14/16s-43, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Dr. Bachner` — partial — pred is substring of gold: `Dr. Bachner-Foregger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Michel`(person)
- `Mag. Fürnkranz`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Oberressl`(person)
- `Mag. Rathgeb`(person)
- `Daniel Kur`(person)
- `Landesgerichts Innsbruck`(organisation)

**Example 52** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_4`)


Augst 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Vizepräsidentin des Obersten Gerichtshofs Mag. Marek, die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Wieser als Schriftführerin in der Maßnahmenvollzugssache des Gerald Winand wegen bedingter Nachsicht einer mit Freiheitsentziehung verbundenen vorbeugenden Maßnahme (§ 21 Abs 1 StGB) über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien vom 16. Mai 2018, AZ 22 Bs 119/18p (AZ 606 Hv 1/17k des Landesgerichts Korneuburg), nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Dr. Bachner` — partial — pred is substring of gold: `Dr. Bachner-Foregger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Marek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Fürnkranz`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Oberressl`(person)
- `Mag. Wieser`(person)
- `Gerald Winand`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Korneuburg`(organisation)

**Example 53** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_3`)


Kopf Der Oberste Gerichtshof hat am 18. März 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski im Verfahren zur Unterbringung des Mag. Herwig Bäseke in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB, AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz gemäß § 62 Abs 1 zweiter Satz OGH-Geo 2019 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger sowie Mag. Fürnkranz sind von der Entscheidung über die Anträge des Mag. Herwig Berto auf Erneuerung des Strafverfahrens AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, ausgeschlossen.

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`
- `Dr. Michel` — partial — pred is substring of gold: `Dr. Michel-Kwapinski`
- `Mag. Herwig` — partial — pred is substring of gold: `Mag. Herwig Bäseke`
- `Dr. Bachner` — partial — pred is substring of gold: `Dr. Bachner-Foregger`
- `Dr. Bachner` — similar text (different position): `Dr. Bachner-Foregger`

> overlaps gold: 5  |  likely missing annotation: 0

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

**Example 54** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_4`)


An ihre Stelle treten Senatspräsident des Obersten Gerichtshofs Dr. Solé sowie Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Setz-Hummel.

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`
- `Dr. Michel` — partial — pred is substring of gold: `Dr. Michel-Kwapinski`
- `Dr. Setz` — partial — pred is substring of gold: `Dr. Setz-Hummel`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Dr. Setz-Hummel`(person)

**Example 55** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_6`)


Senatspräsident des Obersten Gerichtshofs Dr. Schwab sowie Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz sind Mitglieder des zuständigen 11.

**False Positives:**

- `Dr. Bachner` — partial — pred is substring of gold: `Dr. Bachner-Foregger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Fürnkranz`(person)

**Example 56** (doc_id: `deanon_260716_TRAIN/12Ns18_20y`) (sent_id: `deanon_260716_TRAIN/12Ns18_20y_12`)


Senatspräsident des Obersten Gerichtshofs Dr. Solé sowie Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski und Dr. Setz-Hummel treten aufgrund der laufenden Vertretungsregelung der Geschäftsverteilung des Obersten Gerichtshofs an deren Stelle (§ 45 Abs 2 StPO).

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`
- `Dr. Michel` — partial — pred is substring of gold: `Dr. Michel-Kwapinski`
- `Dr. Setz` — partial — pred is substring of gold: `Dr. Setz-Hummel`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Solé`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Dr. Setz-Hummel`(person)
- `Obersten Gerichtshofs`(organisation)

**Example 57** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_3`)


Kopf Der Oberste Gerichtshof hat am 16. März 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Brenner in der Strafvollzugssache des Oliver Pekarek, AZ 39 Ns 43/15i des Landesgerichts Krems an der Donau, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Hon.-Prof. Dr` — partial — pred is substring of gold: `Hon.-Prof. Dr. Schroll`

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

**Example 58** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_5`)


An Stelle der nunmehr als Vorsitzende einschreitenden Hofrätin des Obersten Gerichtshofs Dr. Bachner-Foregger tritt Hofrat des Obersten Gerichtshofs Dr. Nordmeyer.

**False Positives:**

- `Dr. Bachner` — partial — pred is substring of gold: `Dr. Bachner-Foregger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)

**Example 59** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_11`)


Hofrat des Obersten Gerichtshofs Dr. Nordmeyer tritt aufgrund der laufenden Vertretungsregelung der Geschäftsverteilung des Obersten Gerichtshofs anstelle der nunmehr als Vorsitzende einschreitenden Hofrätin des Obersten Gerichtshofs Dr. Bachner-Foregger (§ 45 Abs 2 StPO).

**False Positives:**

- `Dr. Bachner` — partial — pred is substring of gold: `Dr. Bachner-Foregger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Obersten Gerichtshofs`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)

**Example 60** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_3`)


Kopf Der Oberste Gerichtshof hat am 11. März 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Dr. Oshidari als weitere Richter in der Strafsache gegen Gerhard Bukowska wegen des Verbrechens des schweren gewerbsmäßigen Betrugs nach §§ 146, 147 Abs 3, 148 erster Fall, 15 Abs 1 StGB und weiterer strafbarer Handlungen, AZ 16 Hv 20/14x des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätin des Obersten Gerichtshofs Mag. Michel gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Hon.-Prof. Dr` — partial — pred is substring of gold: `Hon.-Prof. Dr. Schroll`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Schroll`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. T. Solé`(person)
- `Dr. Oshidari`(person)
- `Gerhard Bukowska`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Michel`(person)
- `OGH`(organisation)

**Example 61** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_5`)


An deren Stelle treten Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski.

**False Positives:**

- `Dr. Michel` — partial — pred is substring of gold: `Dr. Michel-Kwapinski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)

**Example 62** (doc_id: `deanon_260716_TRAIN/12Ns4_15g`) (sent_id: `deanon_260716_TRAIN/12Ns4_15g_17`)


3. An die Stelle der Ausgeschlossenen treten aufgrund der laufenden Vertretungsregelung Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski. (§ 45 Abs 2 StPO).

**False Positives:**

- `Dr. Michel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Nordmeyer`(person)
- `Obersten Gerichtshofs`(organisation)

**Example 63** (doc_id: `deanon_260716_TRAIN/12Ns94_11m`) (sent_id: `deanon_260716_TRAIN/12Ns94_11m_3`)


Kopf Der Oberste Gerichtshof hat am 28. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in der Strafsache gegen Mag. Herwig Bernts wegen des Vergehens des Widerstands gegen die Staatsgewalt nach § 269 Abs 1 erster Fall StGB und anderer strafbarer Handlungen, AZ 20 Hv 38/11f des Landesgerichts Linz, über den Antrag des Angeklagten auf Delegierung nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 Satz 2 OGH-Geo.

**False Positives:**

- `Hon.-Prof. Dr` — partial — pred is substring of gold: `Hon.-Prof. Dr. Schroll`
- `Hon.-Prof. Dr` — similar text (different position): `Hon.-Prof. Dr. Schroll`
- `Dr. Michel` — partial — pred is substring of gold: `Dr. Michel-Kwapinski`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Schroll`(person)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Herwig Bernts`(person)
- `Landesgerichts Linz`(organisation)
- `OGH`(organisation)

**Example 64** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_3`)


Kopf Der Oberste Gerichtshof hat am 9. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Brenner und Dr. Setz-Hummel in der Strafsache gegen Ahmed Koehnen wegen des Verbrechens des Mordes nach § 75 StGB, AZ 606 Hv 1/11m des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit der Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Dr. Sol` — partial — pred is substring of gold: `Dr. Solé`
- `Dr. Setz` — partial — pred is substring of gold: `Dr. Setz-Hummel`
- `Dr. Michel` — partial — pred is substring of gold: `Dr. Michel-Kwapinski`

> overlaps gold: 3  |  likely missing annotation: 0

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

**Example 65** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_4`)


2005 den Beschluss gefasst:  Spruch Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski ist von der Entscheidung über die Beschwerde des Ahmed Kleinmayer gegen den Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 25. November 2019, AZ 23 Bs 343/19p, ausgeschlossen.

**False Positives:**

- `Dr. Michel` — partial — pred is substring of gold: `Dr. Michel-Kwapinski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)
- `Ahmed Kleinmayer`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 66** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_8`)


Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski ist Mitglied des zuständigen Senats 15.

**False Positives:**

- `Dr. Michel` — partial — pred is substring of gold: `Dr. Michel-Kwapinski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Michel-Kwapinski`(person)

**Example 67** (doc_id: `deanon_260716_TRAIN/12Os11_19p`) (sent_id: `deanon_260716_TRAIN/12Os11_19p_3`)


Kopf Der Oberste Gerichtshof hat am 4. März 2019 durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Mann und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Rögner als Schriftführerin in der Strafsache gegen Thomas Michenfelder wegen des Verbrechens des schweren gewerbsmäßigen Diebstahls durch Einbruch nach §§ 127, 128 Abs 1 Z 2 und Z 5, 129 Abs 1 Z 1, Z 2 und Z 3, 130 Abs 2 zweiter Fall und 15 StGB sowie weiterer strafbarer Handlungen, AZ 38 Hv 40/18z des Landesgerichts Krems an der Donau, über die von der Generalprokuratur gegen den Beschluss des Präsidenten des Oberlandesgerichts Wien vom 17. Oktober 2018, AZ 130 Ns 31/18w, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Mag. Gföller und der Verteidigerin Dr. Zeh-Gindl zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Michel` — partial — pred is substring of gold: `Dr. Michel-Kwapinski`
- `Mag. Gf` — partial — pred is substring of gold: `Mag. Gföller`
- `Dr. Zeh` — partial — pred is substring of gold: `Dr. Zeh-Gindl`

> overlaps gold: 3  |  likely missing annotation: 0

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

</details>

---

## `Against/Complaint Context` 🏆

**F1:** 0.007 | **Precision:** 0.452 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `5550e203`  
**Description:**
Matches persons mentioned after 'gegen' (against) or 'Beschwerde der/des' (complaint of).

**Content:**
```
(?:gegen\s+(?:die\s+)?Bescheide|gegen\s+den\s+Bescheid|Beschwerde\s+der|Beschwerde\s+des|Beschwerde\s+der\s+Partei)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.452 | 0.003 | 0.007 | 31 | 14 | 17 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 14 | 17 | 3685 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_5`)


Dagegen richtet sich die als Rekurs bezeichnete, prozessordnungswidrig an das Oberlandesgericht Linz gerichtete Beschwerde des Richard Laumeyer.

| Predicted | Gold |
|---|---|
| `Richard Laumeyer` | `Richard Laumeyer` |

**Missed by this rule (FN):**

- `Oberlandesgericht Linz` (organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_5`)


Gründe:  Rechtliche Beurteilung Der gegen den Beschluss des Oberlandesgerichts Wien, mit dem eine Beschwerde des Gerald Wandscheer gegen den Beschluss des Landesgerichts Korneuburg vom 21. Februar 2018, GZ 606 Hv 1/17k-94, als verspätet zurückgewiesen worden war, gerichtete „Einspruch“ war ebenso zurückzuweisen, weil gegen derartige Entscheidungen eines Beschwerdegerichts kein weiterer Rechtszug vorgesehen ist (§ 89 Abs 6 StPO).

| Predicted | Gold |
|---|---|
| `Gerald Wandscheer` | `Gerald Wandscheer` |

**Missed by this rule (FN):**

- `Oberlandesgerichts Wien` (organisation)
- `Landesgerichts Korneuburg` (organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/12Ns22_16f`) (sent_id: `deanon_260716_TRAIN/12Ns22_16f_4`)


2005 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab ist von der Entscheidung über die Beschwerde des Oliver Paukstat gegen den Beschluss des Oberlandesgerichts Wien vom 8. Februar 2016, AZ 32 Bs 12/16y, ausgeschlossen.

| Predicted | Gold |
|---|---|
| `Oliver Paukstat` | `Oliver Paukstat` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Dr. Schwab` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_4`)


2005 den Beschluss gefasst:  Spruch Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski ist von der Entscheidung über die Beschwerde des Ahmed Kleinmayer gegen den Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 25. November 2019, AZ 23 Bs 343/19p, ausgeschlossen.

| Predicted | Gold |
|---|---|
| `Ahmed Kleinmayer` | `Ahmed Kleinmayer` |

**Missed by this rule (FN):**

- `Obersten Gerichtshofs` (organisation)
- `Dr. Michel-Kwapinski` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/12Ns98_19m`) (sent_id: `deanon_260716_TRAIN/12Ns98_19m_7`)


Mit dem erwähnten Beschluss vom 25. November 2019 hatte das Oberlandesgericht Wien einer Beschwerde des Ahmed Kocks gegen einen Beschluss des Landesgerichts für Strafsachen Wien auf Ablehnung eines Antrags des Genannten auf Wiederaufnahme des Verfahrens AZ 606 Hv 1/11m jenes Gerichts nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ahmed Kocks` | `Ahmed Kocks` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 5** (doc_id: `deanon_260716_TRAIN/12Os152_12p`) (sent_id: `deanon_260716_TRAIN/12Os152_12p_3`)


Kopf Der Oberste Gerichtshof hat am 13. Dezember 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Fruhmann als Schriftführerin in der Strafsache gegen unbekannte Täter wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB, AZ 130 Bl 65/12s des Landesgerichts für Strafsachen Wien, über die Beschwerde des Gebhard Sayin gegen den Beschluss des Oberlandesgerichts Wien vom 23. Oktober 2012, AZ 17 Bs 410/12m, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Gebhard Sayin` | `Gebhard Sayin` |

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
- `Oberlandesgerichts Wien` (organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/12Os152_12p`) (sent_id: `deanon_260716_TRAIN/12Os152_12p_4`)


Text Gründe: Mit der angefochtenen Entscheidung wies das Oberlandesgericht Wien die Beschwerde des Gebhard Senkfeil gegen den Beschluss des Landesgerichts für Strafsachen Wien vom 25. September 2012, GZ 130 Bl 65/12s-10, mit welchem der Antrag des Beschwerdeführers auf Fortführung des Verfahrens AZ 20 UT 91/12p der Staatsanwaltschaft Wien gegen unbekannte Täter wegen § 302 Abs 1 StGB zurückgewiesen worden war, als unzulässig zurück (§ 196 Abs 1 StPO).

| Predicted | Gold |
|---|---|
| `Gebhard Senkfeil` | `Gebhard Senkfeil` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/12Os17_18v`) (sent_id: `deanon_260716_TRAIN/12Os17_18v_5`)


Text Gründe: Mit dem angefochtenen Beschluss vom 9. Jänner 2018, AZ 131 Bs 370/17z, gab das Oberlandesgericht Wien als Rechtsmittelgericht der Beschwerde des Andreas Wackerow gegen den Beschluss des Landesgerichts für Strafsachen Wien vom 20. November 2017, GZ 181 BE 143/17y-16, mit dem die bedingte Entlassung aus einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 2 StGB abgelehnt worden war, nicht Folge.

| Predicted | Gold |
|---|---|
| `Andreas Wackerow` | `Andreas Wackerow` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)
- `Landesgerichts für Strafsachen Wien` (organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/12Os17_18v`) (sent_id: `deanon_260716_TRAIN/12Os17_18v_6`)


Rechtliche Beurteilung Die dagegen gerichtete Beschwerde des Andreas Wienant war als unzulässig zurückzuweisen, weil gegen solche Entscheidungen kein weiterer Rechtszug zusteht (§ 89 Abs 6 StPO).

| Predicted | Gold |
|---|---|
| `Andreas Wienant` | `Andreas Wienant` |

**Example 9** (doc_id: `deanon_260716_TRAIN/13Os108_19k`) (sent_id: `deanon_260716_TRAIN/13Os108_19k_5`)


Die dagegen gerichtete Beschwerde des Sebastian Naegeler wies das Oberlandesgericht Graz mit Beschluss vom 1. August 2019, AZ 10 Bs 202/19k, unter Hinweis auf § 196 Abs 1 zweiter Halbsatz StPO als unzulässig zurück.

| Predicted | Gold |
|---|---|
| `Sebastian Naegeler` | `Sebastian Naegeler` |

**Missed by this rule (FN):**

- `Oberlandesgericht Graz` (organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/13Os16_15z`) (sent_id: `deanon_260716_TRAIN/13Os16_15z_3`)


Kopf Der Oberste Gerichtshof hat am 25. Februar 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Bachl als Schriftführerin in der Strafsache gegen Mag. Johanna Fletcher wegen des Verbrechens des Missbrauchs der Amtsgewalt nach § 302 Abs 1 StGB, AZ 3 St 166/14k der Staatsanwaltschaft Wels, über die Beschwerde des Herbert Onesseit gegen den Beschluss des Oberlandesgerichts Linz vom 9. Jänner 2015, AZ 7 Bs 218/14d (ON 12), nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Herbert Onesseit` | `Herbert Onesseit` |

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
- `Oberlandesgerichts Linz` (organisation)

**Example 11** (doc_id: `deanon_260716_TRAIN/13Os16_15z`) (sent_id: `deanon_260716_TRAIN/13Os16_15z_4`)


Gründe:  Rechtliche Beurteilung Mit dem angefochtenen Beschluss wies das Oberlandesgericht Linz die Beschwerde des Herbert Oehlschlager gegen den Beschluss des Landesgerichts Wels vom 19. November 2014, AZ 24 Bl 81/14h (ON 9 der Ermittlungsakten), mit dem der Antrag des Genannten auf Fortführung des Verfahrens zurückgewiesen worden war, gemäß § 196 Abs 1 erster Satz StPO zurück (ON 12 der Ermittlungsakten).

| Predicted | Gold |
|---|---|
| `Herbert Oehlschlager` | `Herbert Oehlschlager` |

**Missed by this rule (FN):**

- `Oberlandesgericht Linz` (organisation)
- `Landesgerichts Wels` (organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/14Os70_10s`) (sent_id: `deanon_260716_TRAIN/14Os70_10s_3`)


Kopf Der Oberste Gerichtshof hat am 15. Juni 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Dr. Lässig, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger sowie die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Mag. Hautz in Gegenwart der Richteramtsanwärterin Mag. Wöss als Schriftführerin in der Strafsache gegen Heinrich Käter wegen des Vergehens der Urkundenunterdrückung nach § 229 Abs 1 StGB, AZ 5 U 21/09y des Bezirksgerichts Ybbs, über die Beschwerde des Heinrich Kowacki und der Annemarie Kloiber gegen den Beschluss des Oberlandesgerichts Wien vom 8. April 2010, AZ 18 Bs 73/10g (ON 11), nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Heinrich Kowacki` | `Heinrich Kowacki` |

**Missed by this rule (FN):**

- `Oberste Gerichtshof` (organisation)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Philipp` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Lässig` (person)
- `Obersten Gerichtshofs` (organisation)
- `Mag. Hetlinger` (person)
- `Obersten Gerichtshofs` (organisation)
- `Dr. Nordmeyer` (person)
- `Mag. Hautz` (person)
- `Mag. Wöss` (person)
- `Heinrich Käter` (person)
- `Annemarie Kloiber` (person)
- `Oberlandesgerichts Wien` (organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/14Os70_10s`) (sent_id: `deanon_260716_TRAIN/14Os70_10s_4`)


Gründe:  Rechtliche Beurteilung Mit dem angefochtenen Beschluss wies das Oberlandesgericht Wien die Beschwerde des Heinrich Knot gegen den Beschluss des Landesgerichts St. Pölten als Beschwerdegericht vom 11. Februar 2010, GZ 9 Bl 158/09y-7, unter Hinweis auf § 89 Abs 6 StPO zurück.

| Predicted | Gold |
|---|---|
| `Heinrich Knot` | `Heinrich Knot` |

**Missed by this rule (FN):**

- `Oberlandesgericht Wien` (organisation)
- `Landesgerichts St. Pölten` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/11Os140_11i`) (sent_id: `deanon_260716_TRAIN/11Os140_11i_3`)


Kopf Der Oberste Gerichtshof hat am 17. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Michel-Kwapinski als weitere Richter, in Gegenwart des Richteramtsanwärters Mag. Sommer als Schriftführer, in der Strafsache gegen Richard Lindt wegen des Vergehens der vorsätzlichen Beeinträchtigung der Umwelt nach § 180 Abs 2 Z 1, Z 2 StGB und einer weiteren strafbaren Handlung, AZ 40 Hv 147/10g des Landesgerichts Salzburg, über die Beschwerde des Genannten gegen den Beschluss dieses Gerichts vom 7. September 2011, ON 547, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Genannten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Zehetner`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Mag. Lendl`(person)
- `Mag. Michel`(person)
- `Dr. Michel-Kwapinski`(person)
- `Mag. Sommer`(person)
- `Richard Lindt`(person)
- `Landesgerichts Salzburg`(organisation)

**Example 1** (doc_id: `deanon_260716_TRAIN/11Os91_18v`) (sent_id: `deanon_260716_TRAIN/11Os91_18v_4`)


Augst 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab als Vorsitzenden sowie die Vizepräsidentin des Obersten Gerichtshofs Mag. Marek, die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Wieser als Schriftführerin in der Maßnahmenvollzugssache des Gerald Winand wegen bedingter Nachsicht einer mit Freiheitsentziehung verbundenen vorbeugenden Maßnahme (§ 21 Abs 1 StGB) über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien vom 16. Mai 2018, AZ 22 Bs 119/18p (AZ 606 Hv 1/17k des Landesgerichts Korneuburg), nach Einsichtnahme der Generalprokuratur in die Akten in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Genannten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Obersten Gerichtshofs`(organisation)
- `Dr. Schwab`(person)
- `Obersten Gerichtshofs`(organisation)
- `Mag. Marek`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Bachner-Foregger`(person)
- `Mag. Fürnkranz`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Oberressl`(person)
- `Mag. Wieser`(person)
- `Gerald Winand`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Korneuburg`(organisation)

**Example 2** (doc_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_260716_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__18`)


Über die rechtzeitige Beschwerde der Staatsanwaltschaft gegen den Beschluss auf Widerruf bedingter Strafnachsicht (ON 28) wurde noch nicht entschieden (AZ 131 Bl 94/18x des Landesgerichts für Strafsachen Wien).

**False Positives:**

- `Staatsanwaltschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 3** (doc_id: `deanon_260716_TRAIN/12Os17_18v`) (sent_id: `deanon_260716_TRAIN/12Os17_18v_3`)


Kopf Der Oberste Gerichtshof hat am 15. März 2018 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. T. Solé, Dr. Oshidari, Dr. Michel-Kwapinski und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Ettel als Schriftführerin in der Maßnahmenvollzugssache des Andreas Wegele, AZ 181 BE 143/17y des Landesgerichts für Strafsachen Wien, über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien vom 9. Jänner 2018, AZ 131 Bs 370/17z, und seinen Antrag auf Bewilligung der Verfahrenshilfe nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Genannten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Schroll`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. T. Solé`(person)
- `Dr. Oshidari`(person)
- `Dr. Michel-Kwapinski`(person)
- `Dr. Brenner`(person)
- `Mag. Ettel`(person)
- `Andreas Wegele`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/12Os34_10g`) (sent_id: `deanon_260716_TRAIN/12Os34_10g_3`)


Kopf Der Oberste Gerichtshof hat am 8. April 2010 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Holzweber als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll, Dr. Schwab, Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger in Gegenwart der Richteramtsanwärterin Mag. Bayer als Schriftführerin in der Strafsache gegen Dr. Ernst-Peter Nepomuk Lieschke wegen des Vergehens der Fälschung besonders geschützter Urkunden nach §§ 223 Abs 2, 224 StGB über die Beschwerde des Verurteilten gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 19. Jänner 2010, AZ 20 Bs 461/09d (GZ 20 Hv 73/09p-19 des Landesgerichts St. Pölten), nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Verurteilten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 5** (doc_id: `deanon_260716_TRAIN/12Os34_19w`) (sent_id: `deanon_260716_TRAIN/12Os34_19w_5`)


Das Oberlandesgericht Wien als Rechtsmittelgericht gab der dagegen erhobenen Beschwerde des Beschuldigten (ON 661) mit Beschluss vom 28. August 2018, AZ 20 Bs 199/18p, nicht Folge (ON 683).

**False Positives:**

- `Beschuldigten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberlandesgericht Wien`(organisation)

**Example 6** (doc_id: `deanon_260716_TRAIN/12Os6_15x`) (sent_id: `deanon_260716_TRAIN/12Os6_15x_19`)


Am 17. Oktober 2014 langte beim Landesgericht Feldkirch zu AZ 51 Hv 32/13i eine vom Verfahrenshilfeverteidiger im Verfahren AZ 39 Hv 64/14h dieses Landesgerichts verfasste Beschwerde des Angeklagten Johannes Bartlmäß (ON 42 im Akt AZ 51 Hv 32/13i des Landesgerichts Feldkirch) gegen den Beschluss des Landesgerichts Feldkirch vom 4. Mai 2014 auf Wiederaufnahme des Strafverfahrens ein.

**False Positives:**

- `Angeklagten Johannes Bartlm` — positional overlap with gold: `Johannes Bartlmäß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landesgericht Feldkirch`(organisation)
- `Johannes Bartlmäß`(person)
- `Landesgerichts Feldkirch`(organisation)
- `Landesgerichts Feldkirch`(organisation)

**Example 7** (doc_id: `deanon_260716_TRAIN/13Os126_17d`) (sent_id: `deanon_260716_TRAIN/13Os126_17d_3`)


Kopf Der Oberste Gerichtshof hat am 6. Dezember 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Schuber als Schriftführer in der Strafsache gegen Mehdi Rekemeyer wegen des Verbrechens des Raubes nach §§ 15, 142 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Salzburg als Schöffengericht vom 19. Juli 2017, GZ 63 Hv 56/17d-44, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Anordnung von Bewährungshilfe nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Angeklagten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Lässig`(person)
- `Mag. Michel`(person)
- `Dr. Oberressl`(person)
- `Dr. Brenner`(person)
- `Mag. Schuber`(person)
- `Mehdi Rekemeyer`(person)
- `Landesgerichts Salzburg`(organisation)

**Example 8** (doc_id: `deanon_260716_TRAIN/13Os23_15d`) (sent_id: `deanon_260716_TRAIN/13Os23_15d_3`)


Kopf Der Oberste Gerichtshof hat am 15. April 2015 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart der Richteramtsanwärterin Mag. Ableidinger als Schriftführerin in der Strafsache gegen Karl Wolniak wegen des Verbrechens der Vergewaltigung nach § 201 Abs 1 StGB über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 26. November 2014, GZ 31 Hv 87/14k-77, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Widerruf einer bedingten Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Angeklagten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Lässig`(person)
- `Mag. Michel`(person)
- `Dr. Oberressl`(person)
- `Dr. Brenner`(person)
- `Mag. Ableidinger`(person)
- `Karl Wolniak`(person)
- `Landesgerichts für Strafsachen Wien`(organisation)

**Example 9** (doc_id: `deanon_260716_TRAIN/13Os74_17g`) (sent_id: `deanon_260716_TRAIN/13Os74_17g_3`)


Kopf Der Oberste Gerichtshof hat am 6. September 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Wetter als Schriftführer in der Strafsache gegen Michael Wakup wegen des Verbrechens des sexuellen Missbrauchs einer wehrlosen oder psychisch beeinträchtigten Person nach §§ 15, 205 Abs 1 StGB sowie weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts Linz als Schöffengericht vom 21. März 2017, GZ 22 Hv 1/17p-32, sowie die Beschwerde des Angeklagten gegen den zugleich ergangenen Beschluss auf Widerruf bedingter Strafnachsicht nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Nichtigkeitsbeschwerde wird zurückgewiesen.

**False Positives:**

- `Angeklagten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Kirchbacher`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Lässig`(person)
- `Mag. Michel`(person)
- `Dr. Oberressl`(person)
- `Dr. Brenner`(person)
- `Mag. Wetter`(person)
- `Michael Wakup`(person)
- `Landesgerichts Linz`(organisation)

**Example 10** (doc_id: `deanon_260716_TRAIN/14Os133_19v`) (sent_id: `deanon_260716_TRAIN/14Os133_19v_3`)


Kopf Der Oberste Gerichtshof hat am 14. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Mann und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Finanzstrafsache gegen Dr. Peter Johanni wegen des Finanzvergehens der Abgabenhinterziehung nach §§ 33 Abs 1, 13 FinStrG, AZ 14 Hv 3/10a des Landesgerichts für Strafsachen Wien, über die Beschwerde des Genannten gegen den Beschluss des Oberlandesgerichts Wien als Beschwerdegericht vom 23. Oktober 2019, AZ 23 Bs 323/19x, nach Einsichtnahme der Generalprokuratur in die Akten den Beschluss gefasst:  Spruch Die Beschwerde wird zurückgewiesen.

**False Positives:**

- `Genannten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 11** (doc_id: `deanon_260716_TRAIN/14Os133_19v`) (sent_id: `deanon_260716_TRAIN/14Os133_19v_5`)


Rechtliche Beurteilung Die dagegen erhobene – auch als Rekurs und Einspruch bezeichnete – Beschwerde des Genannten war zurückzuweisen, weil gegen derartige Entscheidungen des Beschwerdegerichts kein weiterer Rechtszug vorgesehen ist (§ 89 Abs 6 StPO).

**False Positives:**

- `Genannten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h_`) (sent_id: `deanon_260716_TRAIN/14Os156_11i_14Os157_11m_14Os158_11h__14`)


Der dagegen erhobenen (irrig „an das Oberlandesgericht Graz“ gerichteten) Beschwerde des Angeklagten gab das Oberlandesgericht Graz mit Beschluss vom 11. August 2011, AZ 9 Bs 259/11y (ON 47 des Akts), nicht Folge.

**False Positives:**

- `Angeklagten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberlandesgericht Graz`(organisation)
- `Oberlandesgericht Graz`(organisation)

**Example 13** (doc_id: `deanon_260716_TRAIN/15Os107_16y`) (sent_id: `deanon_260716_TRAIN/15Os107_16y_9`)


Gegen diesen Beschluss richtet sich eine Beschwerde des Privatanklägers (ON 46), über welche noch nicht entschieden wurde.

**False Positives:**

- `Privatankl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_260716_TRAIN/15Os110_17s`) (sent_id: `deanon_260716_TRAIN/15Os110_17s_11`)


Der dagegen gerichteten Beschwerde des Angeklagten (ON 99) gab das Oberlandesgericht Graz mit Beschluss vom 8. März 2017, AZ 10 Bs 65/17k (ON 107), nicht Folge und setzte die Untersuchungshaft aus den vom Erstgericht angenommenen Haftgründen fort.

**False Positives:**

- `Angeklagten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberlandesgericht Graz`(organisation)

**Example 15** (doc_id: `deanon_260716_TRAIN/15Os88_20k`) (sent_id: `deanon_260716_TRAIN/15Os88_20k_9`)


Der dagegen gerichteten Beschwerde der Antragsgegnerin gab die Einzelrichterin des Oberlandesgerichts Wien mit Beschluss vom 9. März 2020, AZ 18 Bs 340/19k (ON 27), dahin Folge, dass die Antragsgegnerin den Antragstellern (gemeinsam) nur 3.850,98 Euro zu ersetzen habe, weil die verfahrenseinleitenden, „nahezu wortident(en)“ Anträge für beide Antragsteller „ungeachtet ihrer hier geringgradig unterschiedlichen Betroffenheit zweckmäßigerweise im Sinn des § 395 Abs 2 StPO mit gemeinsamen Schriftsatz einzubringen gewesen“ wären.

**False Positives:**

- `Antragsgegnerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberlandesgerichts Wien`(organisation)

**Example 16** (doc_id: `deanon_260716_TRAIN/8ObA20_13v`) (sent_id: `deanon_260716_TRAIN/8ObA20_13v_169`)


Der Verwaltungsgerichtshof gab der Beschwerde des Lehrers statt und sprach aus, dass dem Beschwerdeführer ein Gehalt in der höheren Gehaltsstufe gebühre.

**False Positives:**

- `Lehrers` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Representative Context` 💣

**F1:** 0.000 | **Precision:** 0.005 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b33b27c5`  
**Description:**
Matches persons mentioned as representatives (vertreten durch) or in 'VetR' (Verfahrensbevollmächtigter) contexts.

**Content:**
```
(?:vertreten\s+durch|VetR)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.005 | 0.000 | 0.000 | 193 | 1 | 192 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 192 | 4166 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_260716_TRAIN/10Nc11_19b`) (sent_id: `deanon_260716_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Kordelia Meelis, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Fatima Tengel, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Neumayer` — partial — pred is substring of gold: `Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Fichtenau`(person)
- `Dr. Grohmann`(person)
- `Kordelia Meelis`(person)
- `Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft`(organisation)
- `Fatima Tengel`(person)
- `Mag. Ernst Michael Lang`(person)

**Example 1** (doc_id: `deanon_260716_TRAIN/10Nc16_21s`) (sent_id: `deanon_260716_TRAIN/10Nc16_21s_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der beim Landesgericht Linz zu AZ 3 Cg 46/21a anhängigen Rechtssache der klagenden Partei Hollengk Planung GmbH, Am Steindl 3, 9873 Döbriach, Österreich, vertreten durch Huber Berchtold Rechtsanwälte OG in Wien, gegen die beklagte Partei Wind Nexheimval GmbH, Wiesbergsiedlung 4, 8341 Pöllau, Österreich, vertreten durch ScherbaumSeebacher Rechtsanwälte GmbH in Graz, wegen 188.117,55 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN folgenden Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, zur Verhandlung und Entscheidung der Rechtssache anstelle des Landesgerichts Linz das Landesgericht Korneuburg zu bestimmen, wird abgewiesen.

**False Positives:**

- `Huber Berchtold Rechtsanw` — partial — pred is substring of gold: `Huber Berchtold Rechtsanwälte OG`
- `Scherbaum` — partial — pred is substring of gold: `ScherbaumSeebacher Rechtsanwälte GmbH`

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

**Example 2** (doc_id: `deanon_260716_TRAIN/10Nc45_19b`) (sent_id: `deanon_260716_TRAIN/10Nc45_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie durch die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Hon.-Prof.in KzlR Iris Makowska, vertreten durch Skribe Rechtsanwaelte GmbH in Wien, gegen die beklagte Partei Dieter Apfelbacher Ltd, Am Fundbach 31w, 9170 Tratten, Österreich, wegen 400 EUR sA, über den Ordinationsantrag nach § 28 JN in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Skribe Rechtsanwaelte Gmb` — partial — pred is substring of gold: `Skribe Rechtsanwaelte GmbH`

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

**Example 3** (doc_id: `deanon_260716_TRAIN/10Nc6_22x`) (sent_id: `deanon_260716_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Paulina Nüsken, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Oliver Eylart, Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Skribe Rechtsanw` — partial — pred is substring of gold: `Skribe Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Mag. Ziegelbauer`(person)
- `Dr. Faber`(person)
- `Paulina Nüsken`(person)
- `Skribe Rechtsanwälte GmbH`(organisation)
- `Oliver Eylart`(person)
- `Bezirksgericht Schwechat`(organisation)

**Example 4** (doc_id: `deanon_260716_TRAIN/10Nc9_15b`) (sent_id: `deanon_260716_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Steidlen+Ysner Daten GmbH, Kaminweg 34, 8200 Laßnitzthal, Österreich, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Verlag Waldlemder GmbH, Im Bachl 121, 9620 St. Lorenzen im Gitschtal, Österreich, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

**False Positives:**

- `Prof` — similar text (different position): `Univ.-Prof. Dr. Neumayr`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 5** (doc_id: `deanon_260716_TRAIN/10Ob10_10h`) (sent_id: `deanon_260716_TRAIN/10Ob10_10h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Rechtssache der klagenden Partei Mur Dorftalnex Technologien -GmbH, Grete-Zimmer-Gasse 16, 9133 Homelitschach, Österreich, vertreten durch Dr. Peter Lechner und Dr. Hermann Pfurtscheller, Rechtsanwälte in Innsbruck, und ihrer Nebenintervenientin Ober Dertri GmbH, Hintereggweg 93, 2070 Kleinhöflein, Österreich, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Rudolf Ketelhut GmbH, Fiebrichgasse 17, 5120 Seeleiten, Österreich, vertreten durch Rechtsanwaltskanzlei Dr. Bernhard Hämmerle GmbH in Innsbruck, und ihrer Nebenintervenientin Völkertz Energie GmbH, Brunnbachweg 19, 4653 Mayersdorf, Österreich, vertreten durch Dr. Franz Pechmann, Rechtsanwalt in Wien, wegen 696.238,34 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck vom 2. Oktober 2009, GZ 4 R 108/09b-167, mit dem das Urteil des Landesgerichts Innsbruck vom 23. Februar 2009, GZ 41 Cg 228/01z-152, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

**False Positives:**

- `Rechtsanwaltskanzlei Dr` — positional overlap with gold: `Dr. Bernhard Hämmerle GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

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

- `Lederer Rechtsanwalt Gmb` — partial — pred is substring of gold: `Lederer Rechtsanwalt GmbH`

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

**Example 7** (doc_id: `deanon_260716_TRAIN/10Ob18_13i`) (sent_id: `deanon_260716_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei SüdSanitär Gruppe GmbH, Rinzendorf 28, 4501 Lindach, Österreich, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Kraft` — partial — pred is substring of gold: `Kraft & Winternitz Rechtsanwälte GmbH`

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

**Example 8** (doc_id: `deanon_260716_TRAIN/10Ob21_15h`) (sent_id: `deanon_260716_TRAIN/10Ob21_15h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Heimcon Software GmbH, H - Am Hang 3, 4912 Rettenbrunn, Österreich, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, gegen die beklagte Partei Gunter Landwirtschaft GmbH, Schlossfeld 38, 9300 Graßdorf, Österreich, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, wegen 7.731,06 EUR und Feststellung (Streitwert 20.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse insgesamt 11.597,42 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 216/14h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Vavrovsky Heine Marth Rechtsanw` — partial — pred is substring of gold: `Vavrovsky Heine Marth Rechtsanwälte GmbH`
- `Stolz` — partial — pred is substring of gold: `Stolz & Schartner Rechtsanwälte GmbH`

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

**Example 9** (doc_id: `deanon_260716_TRAIN/10Ob22_22s`) (sent_id: `deanon_260716_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei DDr.in Cornelia Rinaldo, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Conmon-Verlag Limited, Kroisegg 20, 4052 Fleckendorf, Österreich Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Brandl Talos Rechtsanw` — partial — pred is substring of gold: `Brandl Talos Rechtsanwälte GmbH`

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

**Example 10** (doc_id: `deanon_260716_TRAIN/10Ob23_18g`) (sent_id: `deanon_260716_TRAIN/10Ob23_18g_4`)


Malik Schoch, geboren 7. November 2002, 2. 7. Juli 2025, geboren 10. Juli 2004, und 3. Alan Schindlmair, geboren 7. August 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Timon Schönswetter, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Doschek Rechtsanwalts Gmb` — partial — pred is substring of gold: `Doschek Rechtsanwalts GmbH`

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

**Example 11** (doc_id: `deanon_260716_TRAIN/10Ob24_15z`) (sent_id: `deanon_260716_TRAIN/10Ob24_15z_4`)


Enns-Umwelt Consulting Limited, Alpineweg 221, 5730 Jochbergthurn, Österreich, 2. Ing. Lara Markart, letztere vertreten durch Radel Stampf Supper Rechtsanwälte OG in Mattersburg, wegen 160.422,79 EUR sA, infolge Revision der klagenden Partei (Revisionsinteresse 107.422,79 EUR sA) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Jänner 2015, GZ 4 R 119/14w-32, womit das Urteil des Landesgerichts St. Pölten vom 25. April 2014, GZ 37 Cg 96/13f-28, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Radel Stampf Supper Rechtsanw` — partial — pred is substring of gold: `Radel Stampf Supper Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Enns-Umwelt`(organisation)
- `Alpineweg 221, 5730 Jochbergthurn, Österreich`(address)
- `Ing. Lara Markart`(person)
- `Radel Stampf Supper Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts St. Pölten`(organisation)

**Example 12** (doc_id: `deanon_260716_TRAIN/10Ob28_17s`) (sent_id: `deanon_260716_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Brigitte Martz, geboren am 16. November 1978, wegen Kontaktrechts des Vaters Dr. Gustav Thöning, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Madeleine Musialik, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

**False Positives:**

- `Rechtsanw` — similar text (different position): `Kosch & Partner Rechtsanwälte GmbH`
- `Kosch` — partial — pred is substring of gold: `Kosch & Partner Rechtsanwälte GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 13** (doc_id: `deanon_260716_TRAIN/10Ob28_19v`) (sent_id: `deanon_260716_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Bau Zorostfurt GmbH, Isbarystraße 47, 4152 Schölling, Österreich, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Buitenkamp und Rothauge Landwirtschaft GmbH, Gewerbegebiet Mathon 17, 3672 Reitern, Österreich, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Grassner` — partial — pred is substring of gold: `Grassner, Lenz, Thewanger & Partner, Rechtsanwälte`

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

**Example 14** (doc_id: `deanon_260716_TRAIN/10Ob33_15y`) (sent_id: `deanon_260716_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Langhansl+Antonewitz Chemie AG, Camping Geras 16, 9062 Pörtschach am Wörther See, Österreich, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Drau-Pharma GmbH, Strazzegasse 12, 8762 Oberzeiring, Österreich, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Poinstingl` — partial — pred is substring of gold: `Poinstingl & Partner Rechtsanwälte OG`

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

**Example 15** (doc_id: `deanon_260716_TRAIN/10Ob38_25y`) (sent_id: `deanon_260716_TRAIN/10Ob38_25y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Karim Mielewczik, gegen die beklagte Partei Dr. Sandro Gädecken, vertreten durch Ing. Dr. Stefan Krall und Dr. Oliver Kühnl, Rechtsanwälte in Innsbruck, wegen 9.456 EUR sA (Revisionsinteresse 9.268,50 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 25. Februar 2025, GZ 21 R 434/24f-29, mit dem das Urteil des Bezirksgerichts Seekirchen am Wallersee vom 5. September 2024, GZ 2 C 1107/23d-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Ing` — partial — pred is substring of gold: `Ing. Dr. Stefan Krall`

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

**Example 16** (doc_id: `deanon_260716_TRAIN/10Ob41_20g`) (sent_id: `deanon_260716_TRAIN/10Ob41_20g_5`)


Dr. Felix Cornils, Niederlande, beide vertreten durch Tramposch & Partner, Rechtsanwälte KG in Innsbruck, gegen die beklagte Partei Mag.a Constanze Rizzo, vertreten durch König Ermacora Klotz & Partner, Rechtsanwälte in Innsbruck, wegen je 15.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 1. Juli 2020, GZ 10 R 16/20h-49, mit dem das Urteil des Landesgerichts Innsbruck vom 6. Februar 2020, GZ 41 Cg 11/19i-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Tramposch` — partial — pred is substring of gold: `Tramposch & Partner, Rechtsanwälte KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Felix Cornils`(person)
- `Tramposch & Partner, Rechtsanwälte KG`(organisation)
- `Mag.a Constanze Rizzo`(person)
- `Oberlandesgerichts Innsbruck`(organisation)
- `Landesgerichts Innsbruck`(organisation)

**Example 17** (doc_id: `deanon_260716_TRAIN/10Ob43_19z`) (sent_id: `deanon_260716_TRAIN/10Ob43_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Othmar Mertl, vertreten durch Nitsch Pajor Zöllner Rechtsanwälte OG in Mödling, gegen die beklagte Partei Stadtgemeinde Malik Fridt, vertreten durch Krist Bubits Rechtsanwälte OG in Mödling, wegen 1.) 21.216,92 EUR sA und 2.) Feststellung (Streitwert: 2.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Februar 2019, GZ 12 R 96/18b-36, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Wiener Neustadt vom 31. August 2018, GZ 20 Cg 86/17h-31, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Nitsch Pajor` — partial — pred is substring of gold: `Nitsch Pajor Zöllner Rechtsanwälte OG`
- `Krist Bubits Rechtsanw` — partial — pred is substring of gold: `Krist Bubits Rechtsanwälte OG`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 18** (doc_id: `deanon_260716_TRAIN/10Ob69_19y`) (sent_id: `deanon_260716_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Cassandra Wespi, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Bilek Lebensmittel GmbH in Liqu, Dreijochgasse 11, 4722 Stefansdorf, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Vogl Rechtsanwalt Gmb` — partial — pred is substring of gold: `Vogl Rechtsanwalt GmbH`
- `Wess Kux Kispert` — partial — pred is substring of gold: `Wess Kux Kispert & Eckert Rechtsanwalts GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 19** (doc_id: `deanon_260716_TRAIN/10ObS92_17b`) (sent_id: `deanon_260716_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Roland Soukup, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Mahringer Steinwender Bestebner Rechtsanw` — partial — pred is substring of gold: `Mahringer Steinwender Bestebner Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 20** (doc_id: `deanon_260716_TRAIN/17Ob10_19y`) (sent_id: `deanon_260716_TRAIN/17Ob10_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende und die Hofräte Dr. Musger und Priv.-Doz. Dr. Rassi, die Hofrätin Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Dr. Joshua Reupold, als Masseverwalter über das Vermögen der Wald-Versand Gesellschaft mbH, Kugelmannplatz 4, 5121 Döstling, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, gegen die beklagten Parteien 1. Johanna Baldczus, und 2. MedR Nadja Grela, beide vertreten durch Schöpf & Maurer, Rechtsanwalt in Salzburg, wegen 59.028,60 EUR sA, aus Anlass der außerordentlichen Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. April 2019, GZ 1 R 161/18d-52, mit dem das Urteil des Landesgerichts Salzburg vom 30. August 2018, GZ 57 Cg 10/17z-43, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das angefochtene Urteil wird, soweit es die Abweisung des Teilbegehens, die beklagten Parteien seien zur ungeteilten Hand schuldig, der klagenden Partei 18.168,21 EUR samt 4 % Zinsen seit 15.

**False Positives:**

- `Pressl Endl Heinrich Bamberger Rechtsanw` — partial — pred is substring of gold: `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`
- `Sch` — similar text (different position): `Wald-Versand Gesellschaft mbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Lovrek`(person)
- `Dr. Musger`(person)
- `Priv.-Doz. Dr. Rassi`(person)
- `Dr. Kodek`(person)
- `Dr. Stefula`(person)
- `Dr. Joshua Reupold`(person)
- `Wald-Versand Gesellschaft mbH`(organisation)
- `Kugelmannplatz 4, 5121 Döstling, Österreich`(address)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`(organisation)
- `Johanna Baldczus`(person)
- `MedR Nadja Grela`(person)
- `Maurer`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Salzburg`(organisation)

**Example 21** (doc_id: `deanon_260716_TRAIN/17Ob10_20z`) (sent_id: `deanon_260716_TRAIN/17Ob10_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätinnen Mag. Malesich und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Pascal Alsweh, vertreten durch Stephan Briem Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Dr. Simone Pittruff als Treuhänder der Insolvenzgläubiger der Unter-Analyse Aktiengesellschaft, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH in Linz, wegen Feststellung (Streitwert 18.335,66 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. März 2020, GZ 1 R 31/20i-13, womit das Urteil des Landesgerichts Linz vom 9. Dezember 2019, GZ 4 Cg 73/18z-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Stephan Briem Rechtsanwalt Gmb` — partial — pred is substring of gold: `Stephan Briem Rechtsanwalt GmbH`
- `Shamiyeh` — partial — pred is substring of gold: `Shamiyeh & Reiser Rechtsanwälte GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 22** (doc_id: `deanon_260716_TRAIN/1Ob121_25p`) (sent_id: `deanon_260716_TRAIN/1Ob121_25p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Dr. Wurdinger als Vorsitzenden sowie die Hofrätin und die Hofräte Dr. Steger, Mag. Wessely-Kristöfel, Dr. Parzmayr und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Severin Griguschies, vertreten durch Mag. Michael Lang, Rechtsanwalt in Wien, gegen die beklagte Partei Ilhan Sieper, vertreten durch Thomas Wagner-Szemethy, LL.M., Rechtsanwalt in Schwechat, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts Korneuburg als Berufungsgericht vom 13. Mai 2025, GZ 22 R 38/25f-28, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Thomas Wagner` — partial — pred is substring of gold: `Thomas Wagner-Szemethy, LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Steger`(person)
- `Mag. Wessely-Kristöfel`(person)
- `Dr. Parzmayr`(person)
- `Dr. Vollmaier`(person)
- `Severin Griguschies`(person)
- `Mag. Michael Lang`(person)
- `Ilhan Sieper`(person)
- `Thomas Wagner-Szemethy, LL.M.`(person)
- `Landesgerichts Korneuburg`(organisation)

**Example 23** (doc_id: `deanon_260716_TRAIN/1Ob173_11i`) (sent_id: `deanon_260716_TRAIN/1Ob173_11i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Dr. Florenzia Münsterer, vertreten durch Rechtsanwälte Dr. Amhof & Dr. Damian GmbH in Wien, gegen die beklagte Partei MittelEnergie Werke Bank AG, Altlassing 110, 4183 Ahorn, Österreich, vertreten durch Urbanek Lind Schmied Reisch Rechtsanwälte OG in Wien, wegen 600.090 EUR sA, über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 25. Mai 2011, GZ 15 R 64/11h-54, mit dem das Urteil des Handelsgerichts Wien vom 14. Jänner 2011, GZ 16 Cg 20/10f-50, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Rechtsanw` — partial — pred is substring of gold: `Rechtsanwälte Dr. Amhof & Dr. Damian GmbH`
- `Urbanek Lind Schmied Reisch Rechtsanw` — partial — pred is substring of gold: `Urbanek Lind Schmied Reisch Rechtsanwälte OG`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 24** (doc_id: `deanon_260716_TRAIN/1Ob186_12b`) (sent_id: `deanon_260716_TRAIN/1Ob186_12b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Thomas Plüm, vertreten durch Kammler & Koll Rechtsanwälte OG in Freistadt, gegen die beklagte Partei Patrick Dimpfel, vertreten durch Mag. Klaus Burgholzer, Rechtsanwalt in Linz, wegen 100.000 EUR sA und Feststellung (Streitwert: 5.000 EUR), über die außerordentliche Revision der klagenden Partei (Revisionsinteresse: 70.000 EUR sA) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. Juli 2012, GZ 2 R 79/12v-22, mit dem das Urteil des Landesgerichts Linz vom 27. Februar 2012, GZ 5 Cg 61/11d-18, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Kammler` — partial — pred is substring of gold: `Kammler & Koll Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Dr. Grohmann`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Thomas Plüm`(person)
- `Kammler & Koll Rechtsanwälte OG`(organisation)
- `Patrick Dimpfel`(person)
- `Mag. Klaus Burgholzer`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Linz`(organisation)

**Example 25** (doc_id: `deanon_260716_TRAIN/1Ob192_11h`) (sent_id: `deanon_260716_TRAIN/1Ob192_11h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Hierle Sanitär Limited, London, Zirkinger Straße 3, 8082 Glatzau, Österreich, vertreten durch Thum Weinreich Schwarz Fuchsbauer Rechtsanwälte OG in St. Pölten, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 1,8 Mio EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Juni 2011, GZ 14 R 214/10h-39, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 3. September 2010, GZ 33 Cg 3/09t-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Thum Weinreich Schwarz Fuchsbauer Rechtsanw` — partial — pred is substring of gold: `Thum Weinreich Schwarz Fuchsbauer Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Dr. Grohmann`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Hierle Sanitär Limited`(organisation)
- `Zirkinger Straße 3, 8082 Glatzau, Österreich`(address)
- `Thum Weinreich Schwarz Fuchsbauer Rechtsanwälte OG`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 26** (doc_id: `deanon_260716_TRAIN/1Ob34_22i`) (sent_id: `deanon_260716_TRAIN/1Ob34_22i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Vivian Frenkmann, vertreten durch Dr. Günter Wappel, Rechtsanwalt in Wien, gegen die beklagte Partei Erna Mitterneder, vertreten durch Mag. Petra Thurner, Rechtsanwältin in Wien, wegen Feststellung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 15. Dezember 2021, GZ 42 R 332/21s-55, mit dem das Urteil des Bezirksgerichts Fünfhaus vom 14. Juni 2021, GZ 3 C 23/19x-50, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.  Text Begründung: [1]

**False Positives:**

- `Dr` — similar text (different position): `Univ.-Prof. Dr. Bydlinski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Mag. Wessely-Kristöfel`(person)
- `Dr. Parzmayr`(person)
- `Vivian Frenkmann`(person)
- `Dr. Günter Wappel`(person)
- `Erna Mitterneder`(person)
- `Mag. Petra Thurner`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Fünfhaus`(organisation)

**Example 27** (doc_id: `deanon_260716_TRAIN/1Ob77_15b`) (sent_id: `deanon_260716_TRAIN/1Ob77_15b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Shoshana Grosse-Brockhoff, vertreten durch Dr. Günther Loibner, Rechtsanwalt in Wien, gegen die beklagte Partei Yelec Zameit, vertreten durch Dr. Markus Bernhauser, Rechtsanwalt in Wien, wegen Einwilligung in die Einverleibung des Eigentumsrechts, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 23. Dezember 2014, GZ 15 R 234/14p-32, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 26. August 2014, GZ 17 Cg 98/13a-23, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Hon.-Prof. Dr. Sailer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Shoshana Grosse-Brockhoff`(person)
- `Dr. Günther Loibner`(person)
- `Yelec Zameit`(person)
- `Dr. Markus Bernhauser`(person)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 28** (doc_id: `deanon_260716_TRAIN/1Ob85_16f`) (sent_id: `deanon_260716_TRAIN/1Ob85_16f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Janis Ringler, Deutschland, vertreten durch Dr. Günther Klepp und andere, Rechtsanwälte in Linz, gegen die beklagte Partei Dr. Hermine Seib, vertreten durch Mag. Dagmar Hoppstädter, Rechtsanwältin in Weißkirchen an der Traun, wegen 39.000 EUR und Vertragsaufhebung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 31. März 2016, GZ 4 R 169/15y-28, mit dem das Urteil des Landesgerichts Linz vom 19. August 2015, GZ 5 Cg 79/14h-24, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Hon.-Prof. Dr. Sailer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Sailer`(person)
- `Univ.-Prof. Dr. Bydlinski`(person)
- `Mag. Wurzer`(person)
- `Mag. Dr. Wurdinger`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Janis Ringler`(person)
- `Dr. Günther Klepp`(person)
- `Dr. Hermine Seib`(person)
- `Mag. Dagmar Hoppstädter`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Linz`(organisation)

**Example 29** (doc_id: `deanon_260716_TRAIN/2Ob114_24i`) (sent_id: `deanon_260716_TRAIN/2Ob114_24i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte MMag. Sloboda, Dr. Thunhart, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Dorothea Woltzen, vertreten durch Metzler & Partner Rechtsanwälte GmbH in Linz, gegen die beklagte Partei Edeltraud Eickemeyer, vertreten durch Nenning & Tockner, Rechtsanwälte in Steyr, wegen Herstellung, Ausfolgung und Unterlassung über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Steyr als Berufungsgericht vom 21. Dezember 2023, GZ 1 R 116/23m-12, mit dem einer Berufung der beklagten Partei gegen das Urteil des Bezirksgerichts Kirchdorf an der Krems vom 26. Juli 2023, GZ 1 C 132/23y-7, Folge gegeben wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Metzler` — partial — pred is substring of gold: `Metzler & Partner Rechtsanwälte GmbH`
- `Nenning` — partial — pred is substring of gold: `Nenning & Tockner, Rechtsanwälte`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Grohmann`(person)
- `MMag. Sloboda`(person)
- `Dr. Thunhart`(person)
- `Dr. Kikinger`(person)
- `Mag. Fitz`(person)
- `Dorothea Woltzen`(person)
- `Metzler & Partner Rechtsanwälte GmbH`(organisation)
- `Edeltraud Eickemeyer`(person)
- `Nenning & Tockner, Rechtsanwälte`(organisation)
- `Landesgerichts Steyr`(organisation)
- `Bezirksgerichts Kirchdorf an der Krems`(organisation)

**Example 30** (doc_id: `deanon_260716_TRAIN/2Ob145_15k`) (sent_id: `deanon_260716_TRAIN/2Ob145_15k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé und den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei VetR Julia Schnicke, vertreten durch Dr. Michael Langhofer, Rechtsanwalt in Neumarkt am Wallersee, gegen die beklagte Partei Jason Hegenloh, vertreten durch Dr. Anton Waltl, Rechtsanwalt in Zell am See, wegen 197.272,07 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 13. Mai 2015, GZ 6 R 69/15g-81, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Julia Schnicke` — partial — pred is substring of gold: `VetR Julia Schnicke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Danzl`(person)
- `Dr. Veith`(person)
- `Dr. Musger`(person)
- `Dr. E. Solé`(person)
- `Dr. Nowotny`(person)
- `VetR Julia Schnicke`(person)
- `Dr. Michael Langhofer`(person)
- `Jason Hegenloh`(person)
- `Dr. Anton Waltl`(person)
- `Oberlandesgerichts Linz`(organisation)

**Example 31** (doc_id: `deanon_260716_TRAIN/2Ob162_23x`) (sent_id: `deanon_260716_TRAIN/2Ob162_23x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte Hon.-Prof. PD Dr. Rassi, MMag. Sloboda und Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Prof.in Romana Janaseck, vertreten durch Lirk Spielbüchler Hirtzberger Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Simone Gintautas, wegen Feststellung, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 18. Juli 2023, GZ 21 R 75/23k-7, mit dem der Beschluss des Bezirksgerichts St. Johann im Pongau vom 28. Februar 2023, GZ 305 C 9/23x-3, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Lirk Spielb` — partial — pred is substring of gold: `Lirk Spielbüchler Hirtzberger Rechtsanwälte OG`

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

**Example 32** (doc_id: `deanon_260716_TRAIN/2Ob180_21s`) (sent_id: `deanon_260716_TRAIN/2Ob180_21s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden sowie den Hofrat Dr. Musger, die Hofrätin Dr. Solé und die Hofräte Dr. Nowotny und MMag. Sloboda als weitere Richter in der Rechtssache der klagenden Partei Ing. Serge Keilacker, vertreten durch Dr. Alexander Bosio, Rechtsanwalt in Zell am See, gegen die beklagten Parteien 1. KzlR Gerhard Baltronat, Bakk. art., und 2. Gerald Povilaitis, MSc, beide vertreten durch Kinberger-Schuberth-Fischer Rechtsanwälte-GmbH in Zell am See, wegen 21.376,95 EUR sA und Feststellung (Streitwert: 10.000 EUR), über die Revisionen der klagenden und der zweitbeklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 6. August 2021, GZ 53 R 110/21i-23, womit das Teil- und Teilzwischenurteil des Bezirksgerichts Zell am See vom 6. April 2021, GZ 18 C 892/20z-17, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revisionen der klagenden und der zweitbeklagten Partei werden zurückgewiesen.

**False Positives:**

- `Kinberger` — partial — pred is substring of gold: `Kinberger-Schuberth-Fischer Rechtsanwälte-GmbH`

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

**Example 33** (doc_id: `deanon_260716_TRAIN/2Ob193_23f`) (sent_id: `deanon_260716_TRAIN/2Ob193_23f_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte Hon.-Prof. PD Dr. Rassi, MMag. Sloboda, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Denise Markstaler, vertreten durch Weber Rechtsanwälte GmbH & Co KG in Wien 1, gegen die beklagte Partei Rut Adamheit, vertreten durch BEURLE Rechtsanwälte GmbH & Co KG in Linz, wegen Herausgabe (Streitwert 1.525.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2023, GZ 2 R 87/23m-32, mit dem das Urteil des Landesgerichts Salzburg vom 5. April 2023, GZ 8 Cg 9/23a-22, aufgehoben wurde zu Recht erkannt:  Spruch

**False Positives:**

- `Weber Rechtsanw` — partial — pred is substring of gold: `Weber Rechtsanwälte GmbH & Co KG`

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

**Example 34** (doc_id: `deanon_260716_TRAIN/2Ob194_19x`) (sent_id: `deanon_260716_TRAIN/2Ob194_19x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden und den Hofrat Dr. Musger, die Hofrätin Dr. Solé und die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Haßtenteufel Umwelt GmbH & Co KG, Peter Zauner Weg 324, 5273 Wesen, Österreich, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Klagenfurt, gegen die beklagte Partei Isaak Tomzak, vertreten durch Dr. Maximilian Motschiunig, Rechtsanwalt in Klagenfurt, wegen Vertragsaufhebung und Abgabe einer Willenserklärung (Streitwert 35.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 1. Oktober 2019, GZ 2 R 141/19a, 2 R 142/19y-95, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Gheneff` — partial — pred is substring of gold: `Gheneff - Rami - Sommer Rechtsanwälte OG`

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

**Example 35** (doc_id: `deanon_260716_TRAIN/2Ob194_24d`) (sent_id: `deanon_260716_TRAIN/2Ob194_24d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte MMag. Sloboda, Dr. Thunhart, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Dagobert Drügemöller, vertreten durch Gottgeisl Leinsmer Weber Rechtsanwälte GmbH in Wien, wider die beklagte Partei Rosalinde Nölker, Malta, vertreten durch Mag. Simon Wallner Rechtsanwalt GmbH in Wien, wegen 30.895 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 1. Oktober 2024, GZ 12 R 72/24g-21, den Beschluss gefasst:  Spruch I. Der Antrag auf Unterbrechung des Revisionsverfahrens bis zur Entscheidung des Europäischen Gerichtshofs zu C-683/24 wird abgewiesen.

**False Positives:**

- `Gottgeisl Leinsmer Weber Rechtsanw` — partial — pred is substring of gold: `Gottgeisl Leinsmer Weber Rechtsanwälte GmbH`

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

**Example 36** (doc_id: `deanon_260716_TRAIN/2Ob71_23i`) (sent_id: `deanon_260716_TRAIN/2Ob71_23i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Grohmann als Vorsitzende sowie die Hofräte Dr. Nowotny, Hon.-Prof. PD Dr. Rassi, MMag. Sloboda und Dr. Kikinger als weitere Richter in der Rechtssache der klagenden Partei Hon.-Prof. Hon.-Prof. Egon Mlinaric, vertreten durch Klepp Nöbauer Hintringer Primetshofer Rechtsanwälte (GbR) in Linz, gegen die beklagte Partei Jaden Rembe, vertreten durch Dr. Christoph Arbeithuber, Rechtsanwalt in Linz, wegen 26.843,50 EUR sA und Feststellung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 27. Februar 2023, GZ 4 R 17/23g-28, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Klepp` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Grohmann`(person)
- `Dr. Nowotny`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `MMag. Sloboda und Dr. Kikinger`(person)
- `Hon.-Prof. Hon.-Prof. Egon Mlinaric`(person)
- `Jaden Rembe`(person)
- `Dr. Christoph Arbeithuber`(person)
- `Oberlandesgerichts Linz`(organisation)

**Example 37** (doc_id: `deanon_260716_TRAIN/2Ob79_11y`) (sent_id: `deanon_260716_TRAIN/2Ob79_11y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Angelika Erdönmez, vertreten durch Hengstschläger Lindner und Partner Rechtsanwälte GmbH in Linz, gegen die beklagte Partei Sabine Lance, vertreten durch Mag. Gerlach Bachinger, Rechtsanwalt in Traun, wegen 14.957,31 EUR sA und Feststellung (Streitinteresse: 7.500 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 15. März 2011, GZ 3 R 34/11g-24, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts Linz vom 22. Dezember 2010, GZ 1 Cg 210/09m-20, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Hengstschl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Baumann`(person)
- `Dr. Veith`(person)
- `Dr. E. Solé`(person)
- `Dr. Schwarzenbacher`(person)
- `Dr. Nowotny`(person)
- `Angelika Erdönmez`(person)
- `Lindner und Partner Rechtsanwälte GmbH`(organisation)
- `Sabine Lance`(person)
- `Mag. Gerlach Bachinger`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Linz`(organisation)

**Example 38** (doc_id: `deanon_260716_TRAIN/2Ob86_12d`) (sent_id: `deanon_260716_TRAIN/2Ob86_12d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Erika Huwold, vertreten durch Gruböck & Lentschig Rechtsanwälte OG in Baden, wider die beklagte Partei „ MedR Dr.in Sara Stehlig “ Arnold Schleicherdt, vertreten durch Themmer, Toth & Partner Rechtsanwälte OG in Wien, wegen 144.329,55 EUR sA (Revisionsinteresse 54.717 EUR sA), infolge der außerordentlichen Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Februar 2012, GZ 4 R 598/11g-25, den Beschluss gefasst:  Spruch Das Revisionsverfahren wird bis zur rechtskräftigen Erledigung des Verfahrens über den Ablehnungsantrag der beklagten Partei gegen die Erstrichterin unterbrochen.

**False Positives:**

- `Grub` — partial — pred is substring of gold: `Gruböck & Lentschig Rechtsanwälte OG`
- `Themmer` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

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

**Example 39** (doc_id: `deanon_260716_TRAIN/2Ob89_17b`) (sent_id: `deanon_260716_TRAIN/2Ob89_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende, die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé sowie den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Dipl.-Ing. Eleonore Wagenbret, vertreten durch Posch, Schausberger & Lutz Rechtsanwälte GmbH in Wels, gegen die beklagten Parteien 1. Rudolfa Schoenmaekers, 2. Lorena Sieckkötter, und 3. TraunSanitär Dienstleistungen Versicherungs-AG, Georg Pfligersdorffer-Gasse 71, 3610 Maigen, Österreich, alle vertreten durch Mag. Dr. A. Michael Dallinger, Rechtsanwalt in Wels, wegen 187.040,19 EUR sA und Feststellung (Streitinteresse: 5.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 1. März 2017, GZ 6 R 30/17z-42, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Posch` — partial — pred is substring of gold: `Posch, Schausberger & Lutz Rechtsanwälte GmbH`

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

**Example 40** (doc_id: `deanon_260716_TRAIN/3Ob108_18f`) (sent_id: `deanon_260716_TRAIN/3Ob108_18f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Roch und Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Dr. Denis Aichmüller, vertreten durch Scherbaum Seebacher Rechtsanwälte GmbH in Graz, wider die beklagte Partei Hemma Fenski, vertreten durch Dr. Destaller ua, Rechtsanwälte in Graz, wegen (eingeschränkt) Räumung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 23. Februar 2018, GZ 7 R 137/17v-19, mit dem das Urteil des Bezirksgerichts Graz-Ost vom 29. September 2017, GZ 213 C 131/16m-15, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Scherbaum Seebacher Rechtsanw` — partial — pred is substring of gold: `Scherbaum Seebacher Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hoch`(person)
- `Dr. Roch`(person)
- `Dr. Rassi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Dr. Denis Aichmüller`(person)
- `Scherbaum Seebacher Rechtsanwälte GmbH`(organisation)
- `Hemma Fenski`(person)
- `Dr. Destaller`(person)
- `Landesgerichts für Zivilrechtssachen Graz`(organisation)
- `Bezirksgerichts Graz-Ost`(organisation)

**Example 41** (doc_id: `deanon_260716_TRAIN/3Ob12_11b`) (sent_id: `deanon_260716_TRAIN/3Ob12_11b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Dagobert Schoeler, vertreten durch Hopmeier & Wagner Rechtsanwälte OG in Wien, gegen die beklagte Partei Peter Cuypers, vertreten durch Kaufmann & Thurnher Rechtsanwälte GmbH in Dornbirn, wegen Einwendungen gegen den Anspruch (§ 35 EO), über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts Feldkirch als Berufungsgericht vom 9. November 2010, GZ 3 R 354/10x-15, womit über Berufung der klagenden Partei das Urteil des Bezirksgerichts Bludenz vom 9. August 2010, GZ 4 C 516/10z-11, abgeändert wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Hopmeier` — partial — pred is substring of gold: `Hopmeier & Wagner Rechtsanwälte OG`
- `Kaufmann` — partial — pred is substring of gold: `Kaufmann & Thurnher Rechtsanwälte GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Prückner`(person)
- `Hon.-Prof. Dr. Neumayr`(person)
- `Dr. Lovrek`(person)
- `Dr. Jensik`(person)
- `Dr. Roch`(person)
- `Dagobert Schoeler`(person)
- `Hopmeier & Wagner Rechtsanwälte OG`(organisation)
- `Peter Cuypers`(person)
- `Kaufmann & Thurnher Rechtsanwälte GmbH`(organisation)
- `Landesgerichts Feldkirch`(organisation)
- `Bezirksgerichts Bludenz`(organisation)

**Example 42** (doc_id: `deanon_260716_TRAIN/3Ob137_17v`) (sent_id: `deanon_260716_TRAIN/3Ob137_17v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Jensik und Dr. Roch und die Hofrätin Dr. Kodek als weitere Richter in der Pflegschaftssache der Minderjährigen 1. StR Corvin Lengenfelder, geboren am 16. September 2007, 2. Alva Dielschneider, geboren am 28. April 2009, beide wohnhaft beim Vater Mag. Gottfried Clef, dieser vertreten durch Dr. Johann Etienne Korab, Rechtsanwalt in Wien, über den außerordentlichen Revisionsrekurs der Mutter Mag. Alma Plohn, vertreten durch Hornek Hubacek Lichtenstrasser Rechtsanwälte OG in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 15. Mai 2017, GZ 48 R 101/17b-137, womit Punkt 1. und 2. des Beschlusses des Bezirksgerichts Döbling vom 9. Jänner 2017, GZ 1 Ps 119/13b-90, bestätigt wurde, den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Hornek Hubacek Lichtenstrasser Rechtsanw` — partial — pred is substring of gold: `Hornek Hubacek Lichtenstrasser Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hoch`(person)
- `Dr. Lovrek`(person)
- `Dr. Jensik`(person)
- `Dr. Roch`(person)
- `Dr. Kodek`(person)
- `StR Corvin Lengenfelder`(person)
- `16. September`(date)
- `Alva Dielschneider`(person)
- `28. April`(date)
- `Mag. Gottfried Clef`(person)
- `Dr. Johann Etienne Korab`(person)
- `Mag. Alma Plohn`(person)
- `Hornek Hubacek Lichtenstrasser Rechtsanwälte OG`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Döbling`(organisation)

**Example 43** (doc_id: `deanon_260716_TRAIN/3Ob139_20t`) (sent_id: `deanon_260716_TRAIN/3Ob139_20t_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der gefährdeten Partei Dr. Günter Geusau, Rechtsanwalt in Wels, als Masseverwalter über das Vermögen der Kelwald GmbH, Friedelstraße 1, 8350 Pertlstein, Österreich, gegen die Gegnerin der gefährdeten Partei Füsslin Telekom GmbH, Kaltbach 4, 8733 Hof, Österreich, vertreten durch Stock Rechtsanwälte PartnerschaftsgesellschaftmbB in Siegen, Deutschland, im Einvernehmen mit Mag. Martin Schönmair, Rechtsanwalt in Wels, wegen einstweiliger Verfügung nach § 381 Z 1 EO (265.239,60 EUR), aus Anlass des außerordentlichen Revisionsrekurses der gefährdeten Partei gegen den Beschluss des Landesgerichts Wels als Rekursgericht vom 1. Juli 2020, GZ 22 R 129/20g-12, mit dem der Beschluss des Bezirksgerichts Wels vom 3. April 2020, GZ 8 C 302/20g-2, abgeändert wurde, den Beschluss gefasst:  Spruch Aus Anlass des Revisionsrekurses der gefährdeten Partei wird der Beschluss des Rekursgerichts, mit dem über den Rekurs der Gegnerin der gefährdeten Partei meritorisch entschieden wurde, als nichtig aufgehoben, und dem Erstgericht aufgetragen, den Schriftsatz der Gegnerin der gefährdeten Partei vom 29. April 2020 (nur) als Widerspruch gegen die Einstweilige Verfügung des Erstgerichts vom 3. April 2020, GZ 8 C 302/20g-2, zu behandeln und darüber das gesetzmäßige Verfahren einzuleiten.

**False Positives:**

- `Stock Rechtsanw` — partial — pred is substring of gold: `Stock Rechtsanwälte PartnerschaftsgesellschaftmbB`

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

**Example 44** (doc_id: `deanon_260716_TRAIN/3Ob147_20v`) (sent_id: `deanon_260716_TRAIN/3Ob147_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Glanzval Dienstleistungen GmbH, Otto-Hittmair-Platz 29, 9423 Steinberg-Hart, Österreich, vertreten durch Mag. Andreas Kleiber, Rechtsanwalt in Wien, gegen die beklagte Partei Gisela Filippovic, MBA verein Arthur Hoelle, vertreten durch Pflaum Karlberger Wiener Opetnik, Rechtsanwälte in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 22. Juli 2020, GZ 40 R 37/20t-27, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Pflaum Karlberger Wiener Opetnik` — partial — pred is substring of gold: `Pflaum Karlberger Wiener Opetnik, Rechtsanwälte`

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

**Example 45** (doc_id: `deanon_260716_TRAIN/3Ob150_16d`) (sent_id: `deanon_260716_TRAIN/3Ob150_16d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Jensik und Dr. Roch und die Hofrätin Dr. Kodek als weitere Richter in der Exekutionssache der betreibenden Partei Fenmon Versicherung GmbH, Grundwiesenweg 291, 3141 Panzing, Österreich, vertreten durch Dr. Andrea Gesinger, Rechtsanwältin in Salzburg, gegen die verpflichtete Partei Unter Condon Consulting GmbH, Pengersdorf 5, 9556 Gößeberg, Österreich, vertreten durch Doschek Rechtsanwalts GmbH in Wien, wegen 9.718,32 EUR sA, über den Revisionsrekurs und Rekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 24. Mai 2016, GZ 22 R 132/16i, 133/16m-21, womit der Beschluss des Bezirksgerichts St. Johann im Pongau vom 17. März 2016, GZ 22 E 1592/15d-14, abgeändert und der Beschluss des Bezirksgerichts St. Johann im Pongau vom 6. April 2016, GZ 22 E 1592/15d-13, aufgehoben wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs und der Rekurs werden zurückgewiesen.

**False Positives:**

- `Doschek Rechtsanwalts Gmb` — partial — pred is substring of gold: `Doschek Rechtsanwalts GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 46** (doc_id: `deanon_260716_TRAIN/3Ob185_22k`) (sent_id: `deanon_260716_TRAIN/3Ob185_22k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn und die Hofrätinnen Dr. Weixelbraun-Mohr, Dr. Kodek und Mag. Wessely-Kristöfel als weitere Richter in der Exekutionssache der betreibenden Partei Dr. Moritz Absmeier, vertreten durch Dr. Martin Neuwirth, Dr. Alexander Neurauter, Rechtsanwälte in Wien, gegen die verpflichtete Partei DENU Immobilien GmbH, Gürtel 12, 5145 Schmalzhofen, Österreich, vertreten durch Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH in Wien, wegen zwangsweiser Räumung, über den Revisionsrekurs der betreibenden Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 12. August 2022, GZ 40 R 104/22y-20, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 8. April 2022, GZ 49 E 11/22w-3, abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Hochedlinger Luschin Marenzi Kapsch Rechtsanw` — partial — pred is substring of gold: `Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH`

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

**Example 47** (doc_id: `deanon_260716_TRAIN/3Ob201_19h`) (sent_id: `deanon_260716_TRAIN/3Ob201_19h_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Roch als Vorsitzenden sowie die Hofräte Priv.-Doz. Dr. Rassi und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Exekutionssache der betreibenden Partei Brunhild Mauchel, vertreten durch Korn & Gärtner Rechtsanwälte OG in Salzburg, gegen die verpflichtete Partei Evamaria Jaguste, vertreten durch Dr. Wolfgang Lang, Rechtsanwalt in Salzburg, wegen 7.711,58 EUR sA, über den Revisionsrekurs der betreibenden Partei gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 3. Juli 2019, GZ 22 R 171/19d-26, womit der Beschluss des Bezirksgerichts Salzburg vom 1. Februar 2019, GZ 5 E 2444/18x-7, abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Korn` — partial — pred is substring of gold: `Korn & Gärtner Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Roch`(person)
- `Priv.-Doz. Dr. Rassi`(person)
- `Mag. Painsi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Brunhild Mauchel`(person)
- `Korn & Gärtner Rechtsanwälte OG`(organisation)
- `Evamaria Jaguste`(person)
- `Dr. Wolfgang Lang`(person)
- `Landesgerichts Salzburg`(organisation)
- `Bezirksgerichts Salzburg`(organisation)

**Example 48** (doc_id: `deanon_260716_TRAIN/3Ob209_21p`) (sent_id: `deanon_260716_TRAIN/3Ob209_21p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei APHU Solar GmbH & Co KG, Hochkreuth 39, 8144 Bischofegg, Österreich, vertreten durch DDr. Heinz Dietmar Schimanko, Rechtsanwalt in Wien, gegen die beklagte Partei Traun-Transport GmbH, Stauderstraße 30, 8200 Pircha, Österreich, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH & Co KG in Wien, wegen 7.906,82 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 7. Juni 2021, GZ 38 R 66/21v-16, mit dem das Urteil des Bezirksgerichts Favoriten vom 19. Jänner 2021, GZ 3 C 503/20f-12, abgeändert wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Bichler Zrzavy Rechtsanw` — partial — pred is substring of gold: `Bichler Zrzavy Rechtsanwälte GmbH & Co KG`

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

**Example 49** (doc_id: `deanon_260716_TRAIN/3Ob229_14v`) (sent_id: `deanon_260716_TRAIN/3Ob229_14v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Vizepräsidentin Dr. Lovrek und die Hofräte Univ.-Prof. Dr. Neumayr, Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Mag. Helga Nusskern, vertreten durch Hochleitner Rechtsanwälte GmbH in Linz, gegen die beklagte Partei Stadtgemeine Nicoletta Schusterius, vertreten durch Dr. Günther Klepp und andere Rechtsanwälte in Linz, wegen Aufhebung eines Kaufvertrags, infolge außerordentlicher Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 8. Oktober 2014, GZ 6 R 163/14d-32, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Linz vom 25. Juli 2014, GZ 2 Cg 65/13a-27, mit einer Maßgabe bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Hochleitner Rechtsanw` — partial — pred is substring of gold: `Hochleitner Rechtsanwälte GmbH`
- `Dr` — similar text (different position): `Dr. Hoch`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hoch`(person)
- `Dr. Lovrek`(person)
- `Univ.-Prof. Dr. Neumayr`(person)
- `Dr. Jensik`(person)
- `Dr. Roch`(person)
- `Mag. Helga Nusskern`(person)
- `Hochleitner Rechtsanwälte GmbH`(organisation)
- `Nicoletta Schusterius`(person)
- `Dr. Günther Klepp`(person)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Linz`(organisation)

**Example 50** (doc_id: `deanon_260716_TRAIN/3Ob236_17b`) (sent_id: `deanon_260716_TRAIN/3Ob236_17b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Roch und Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Babette Ermentraut, vertreten durch Harb & Postl Rechtsanwälte OG in Graz, gegen die beklagte Partei OSR Dipl. Kfm. OMedR Raimund Stolarik, vertreten durch Dr. Paul Bauer, Dr. Anton Triendl, Rechtsanwälte in Innsbruck, wegen 32.173,22 EUR sA und Feststellung, über die außerordentliche Revision der beklagten Partei (Revisionsinteresse 23.653,60 EUR sA und Feststellung) gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 29. November 2017, GZ 10 R 59/17b-27, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Harb` — partial — pred is substring of gold: `Harb & Postl Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Hoch`(person)
- `Dr. Roch`(person)
- `Dr. Rassi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Babette Ermentraut`(person)
- `Harb & Postl Rechtsanwälte OG`(organisation)
- `OSR Dipl. Kfm. OMedR Raimund Stolarik`(person)
- `Dr. Paul`(person)
- `Dr. Anton Triendl`(person)
- `Oberlandesgerichts Innsbruck`(organisation)

**Example 51** (doc_id: `deanon_260716_TRAIN/3Ob26_23d`) (sent_id: `deanon_260716_TRAIN/3Ob26_23d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Anton Reuschel, vertreten durch Mag. Christopher Schmied, Rechtsanwalt in Salzburg, gegen die beklagte Partei Marktgemeinde KommR Frieda Goetzens, vertreten durch Ebner Aichinger Guggenberger Rechtsanwälte GmbH in Salzburg, wegen Feststellung einer Dienstbarkeit und Beseitigung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 7. Dezember 2022, GZ 3 R 142/22f-17, womit das Urteil des Landesgerichts Salzburg vom 29. September 2022, GZ 9 Cg 47/22w-12, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Ebner Aichinger Guggenberger Rechtsanw` — partial — pred is substring of gold: `Ebner Aichinger Guggenberger Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Höllwerth`(person)
- `Hon.-Prof. Dr. Brenn`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Dr. Stefula`(person)
- `Anton Reuschel`(person)
- `Mag. Christopher Schmied`(person)
- `KommR Frieda Goetzens`(person)
- `Ebner Aichinger Guggenberger Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Salzburg`(organisation)

**Example 52** (doc_id: `deanon_260716_TRAIN/3Ob32_17b`) (sent_id: `deanon_260716_TRAIN/3Ob32_17b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Jensik und Dr. Roch und die Hofrätin Dr. Kodek als weitere Richter in der Exekutionssache der betreibenden Partei Balthasar Düppen, Italien, vertreten durch Oberhammer Rechtsanwälte GmbH in Wien, wider die verpflichtete Partei Ober Talnor gesellschaft mbH, Pesenbachtal 28, 5121 Eckldorf, Österreich, vertreten durch Dr. Daniel Charim und Mag. Jakob Charim, Rechtsanwälte in Wien, wegen (restlich) 347.093,53 EUR sA über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 7. Dezember 2016, GZ 46 R 323/16i-61, womit der Beschluss des Bezirksgerichts Josefstadt vom 24. Juni 2016, GZ 11 E 2966/11p-56, bestätigt wurde, den Beschluss gefasst:  Spruch I.Der Revisionsrekurs der verpflichteten Partei wird, soweit er die Bestätigung der Exekutionsbewilligung bekämpft, als jedenfalls unzulässig zurückgewiesen.

**False Positives:**

- `Oberhammer Rechtsanw` — partial — pred is substring of gold: `Oberhammer Rechtsanwälte GmbH`

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

**Example 53** (doc_id: `deanon_260716_TRAIN/3Ob37_25z`) (sent_id: `deanon_260716_TRAIN/3Ob37_25z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Brenn als Vorsitzenden sowie die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und die Hofräte Dr. Stefula und Mag. Schober als weitere Richter in der Rechtssache der klagenden Partei MedR Peter Reitschmied, vertreten durch MMag. Eva Kathrein, Rechtsanwältin in Innsbruck, gegen die beklagte Partei Annkathrin Peperkock, vertreten durch Ing. MMag. Dr. Gerhard Benda, Rechtsanwalt in Innsbruck, wegen 5.505 EUR sA, über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Innsbruck als Berufungsgericht vom 21. Oktober 2024, GZ 2 R 116/24h-16.1, mit dem die Berufung gegen das Versäumungsurteil des Bezirksgerichts Innsbruck vom 11. Juni 2024, GZ 30 C 63/24g-10, zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Ing` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Brenn`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Kodek`(person)
- `Dr. Stefula`(person)
- `Mag. Schober`(person)
- `MedR Peter Reitschmied`(person)
- `MMag. Eva Kathrein`(person)
- `Annkathrin Peperkock`(person)
- `MMag. Dr. Gerhard Benda`(person)
- `Landesgerichts Innsbruck`(organisation)
- `Bezirksgerichts Innsbruck`(organisation)

**Example 54** (doc_id: `deanon_260716_TRAIN/3Ob45_19t`) (sent_id: `deanon_260716_TRAIN/3Ob45_19t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Roch und Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Mag. Daniel Kutluk, vertreten durch Dr. Johannes Eltz, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Ferdinand Rittgerott, vertreten durch Piaty Müller-Mezin Schöller Rechtsanwälte GmbH & Co KG in Graz, wegen Einwendungen gegen den Anspruch (§ 35 EO), über die „außerordentliche“ Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 25. September 2018, GZ 4 R 102/18a-11, womit das Urteil des Bezirksgerichts Graz-West vom 27. Februar 2018, GZ 211 C 2/17g-7, bestätigt wurde, den Beschluss gefasst:  Spruch Die „außerordentliche“ Revision wird zurückgewiesen.

**False Positives:**

- `Piaty` — partial — pred is substring of gold: `Piaty Müller-Mezin Schöller Rechtsanwälte GmbH & Co KG`

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

**Example 55** (doc_id: `deanon_260716_TRAIN/3Ob72_20i`) (sent_id: `deanon_260716_TRAIN/3Ob72_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Marktgemeinde James Weyand, MA, vertreten durch Dr. Nader Karl Mahdi, Rechtsanwalt in Wattens, gegen die beklagte Partei Lützeler Garten AG, Esteplatz 2, 9064 Schöpfendorf, Österreich, vertreten durch Altenweisl Wallnöfer Watschinger Zimmermann Rechtsanwälte GmbH in Innsbruck, und die auf Seiten der beklagten Partei beigetretene Nebenintervenientin Demeyer u. Köktas Analyse GmbH, Zinkendorferstraße 100, 9321 Schöttlhof, Österreich, vertreten durch Dr. Christian Girardi, LL.M., Ing. Dr. Stefan Schwärzler, Mag. Daniel Pichler, Rechtsanwälte in Innsbruck, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. März 2020, GZ 1 R 5/20z-27, womit das Urteil des Landesgerichts Innsbruck vom 14. November 2019, GZ 12 Cg 33/19m-18, teilweise bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Altenweisl Walln` — partial — pred is substring of gold: `Altenweisl Wallnöfer Watschinger Zimmermann Rechtsanwälte GmbH`

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

**Example 56** (doc_id: `deanon_260716_TRAIN/3Ob99_10w`) (sent_id: `deanon_260716_TRAIN/3Ob99_10w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Senatspräsidenten Hon.-Prof. Dr. Sailer, den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und den Hofrat Dr. Jensik als weitere Richter in der Rechtssache der klagenden Partei Dr. Johannes Müller, Rechtsanwalt, Wien 3, Ditscheinergasse 2, als Masseverwalter im Konkurs der Wald-Event GmbH, gegen die beklagte Partei Wiener Gebietskrankenkasse, Wien 10, Wienerbergstraße 15-19, vertreten durch Preslmayr Rechtsanwälte OG in Wien, und der Nebenintervenienten auf der Seite der beklagten Partei 1.)

**False Positives:**

- `Preslmayr Rechtsanw` — partial — pred is substring of gold: `Preslmayr Rechtsanwälte OG`

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

**Example 57** (doc_id: `deanon_260716_TRAIN/3Ob99_23i`) (sent_id: `deanon_260716_TRAIN/3Ob99_23i_4`)


VetR Istvan  Stini, geboren am 3. April 2010, und 2. Karsten von Ackern, geboren am 3. November 2011, Mutter Sabrina Eisner, vertreten durch Dr. Serpil Dogan, Rechtsanwältin in Feldkirch, Vater Malik Eckolt, vertreten durch Mag. Manuel Dietrich, Rechtsanwalt in Hard, wegen Obsorge, über den außerordentlichen Revisionsrekurs des Vaters gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 16. März 2023, GZ 10 R 39/23v-52, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

**False Positives:**

- `Istvan  Stini` — partial — pred is substring of gold: `VetR Istvan  Stini`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VetR Istvan  Stini`(person)
- `3. April`(date)
- `Karsten von Ackern`(person)
- `3. November`(date)
- `Sabrina Eisner`(person)
- `Dr. Serpil Dogan`(person)
- `Malik Eckolt`(person)
- `Mag. Manuel Dietrich`(person)
- `Landesgerichts Feldkirch`(organisation)

**Example 58** (doc_id: `deanon_260716_TRAIN/4Nc4_17a`) (sent_id: `deanon_260716_TRAIN/4Nc4_17a_4`)


HFJY Getränke Consulting, Dänemark, 2. SeeTouristik Dienstleistungen GmbH, Poysbrunner Straße 102, 4112 Rottenegg, Österreich, beide vertreten durch Graf & Pitkowitz Rechtsanwälte GmbH in Wien, gegen die Beklagten 1. Cizmeci + Janda Chemie GmbH, Lahntalweg 53, 9413 Kamp, Österreich, 2.

**False Positives:**

- `Graf` — partial — pred is substring of gold: `Graf & Pitkowitz Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `HFJY Getränke Consulting`(organisation)
- `SeeTouristik Dienstleistungen GmbH`(organisation)
- `Poysbrunner Straße 102, 4112 Rottenegg, Österreich`(address)
- `Graf & Pitkowitz Rechtsanwälte GmbH`(organisation)
- `Cizmeci + Janda Chemie GmbH`(organisation)
- `Lahntalweg 53, 9413 Kamp, Österreich`(address)

**Example 59** (doc_id: `deanon_260716_TRAIN/4Ob100_13d`) (sent_id: `deanon_260716_TRAIN/4Ob100_13d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Verein Karen Böckel, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei Düwall + Rief Daten -Aktiengesellschaft, Gassing/Burgweg 63, 4613 Mistelbach bei Wels, Österreich, vertreten durch Raits Bleiziffer Rechtsanwälte GmbH in Salzburg, und die Nebenintervenientin auf Seiten der beklagten Partei „ Eberhard Besemer ” Linda Hukauf, vertreten durch Dr. Peter Zöchbauer und andere Rechtsanwälte in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert 36.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz vom 19. April 2013, GZ 1 R 192/12d-14, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Kosesnik` — partial — pred is substring of gold: `Kosesnik-Wehrle & Langer Rechtsanwälte KG`
- `Raits Bleiziffer Rechtsanw` — partial — pred is substring of gold: `Raits Bleiziffer Rechtsanwälte GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 60** (doc_id: `deanon_260716_TRAIN/4Ob113_24g`) (sent_id: `deanon_260716_TRAIN/4Ob113_24g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Mag. Istjan, LL.M., und Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Inn Glanzvalstein GmbH, Unterschaden 15, 8693 Tebrin, Österreich, vertreten durch Grassner Rechtsanwalts GmbH in Linz, gegen die beklagte Partei Antonia Wedderhahn, vertreten durch Dr. Manfred Palkovits, Mag. Martin Sohm, Rechtsanwälte in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 24. April 2024, GZ 38 R 247/23i-46, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Grassner Rechtsanwalts Gmb` — partial — pred is substring of gold: `Grassner Rechtsanwalts GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schwarzenbacher`(person)
- `Hon.-Prof. PD Dr. Rassi`(person)
- `Mag. Istjan, LL.M.`(person)
- `Mag. Waldstätten`(person)
- `Dr. Stiefsohn`(person)
- `Inn Glanzvalstein GmbH`(organisation)
- `Unterschaden 15, 8693 Tebrin, Österreich`(address)
- `Grassner Rechtsanwalts GmbH`(organisation)
- `Antonia Wedderhahn`(person)
- `Dr. Manfred Palkovits`(person)
- `Mag. Martin Sohm`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)

**Example 61** (doc_id: `deanon_260716_TRAIN/4Ob142_21t`) (sent_id: `deanon_260716_TRAIN/4Ob142_21t_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Hon.-Prof. PD Dr. Rassi als Vorsitzenden und die Hofräte und Hofrätinnen Dr. Schwarzenbacher, Dr. Kodek, MMag. Matzka sowie Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei Laurence Perger, vertreten durch Viehböck Breiter Schenk & Nau Rechtsanwälte OG in Mödling, gegen die beklagte Partei EIPD Chemie ges.m.b.H., Insel 21, 4840 Diesenbach, Österreich, vertreten durch Celar Senoner Weber-Wilfert Rechtsanwälte GmbH in Wien, wegen Herausgabe eines Buchauszugs (Streitwert 4.000 EUR) und 41.049,64 EUR sA, über die außerordentliche Revision der klagenden Partei, gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Mai 2021, GZ 5 R 162/20k-66, mit dem das Urteil des Handelsgerichts Wien vom 30. September 2020, GZ 48 Cg 28/19f-59, bestätigt wurde, beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Viehb` — partial — pred is substring of gold: `Viehböck Breiter Schenk & Nau Rechtsanwälte OG`
- `Celar Senoner Weber` — positional overlap with gold: `Weber-Wilfert Rechtsanwälte GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 62** (doc_id: `deanon_260716_TRAIN/4Ob149_13k`) (sent_id: `deanon_260716_TRAIN/4Ob149_13k_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Dimitri Stegmeyr, vertreten durch Dr. Marcella Prunbauer, Rechtsanwältin in Wien, wider die beklagte Partei Okumus Chemie GmbH, Littrowgasse 6, 3474 Kollersdorf, Österreich, vertreten durch Prof. Haslinger & Partner, Rechtsanwälte in Linz, wegen Unterlassung (Streitwert 40.000 EUR) und Urteilsveröffentlichung (Streitwert 4.000 EUR), im Verfahren über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 3. Juli 2013, GZ 2 R 55/13s-13, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Steyr vom 28. Jänner 2013, GZ 2 Cg 134/12t-9, bestätigt wurde, folgenden Beschluss gefasst:  Spruch Das Urteil vom 17. Dezember 2013, 4 Ob 149/13k, wird wie folgt berichtigt: 1.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof. Haslinger & Partner, Rechtsanwälte`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schenk`(person)
- `Dr. Vogel`(person)
- `Dr. Jensik`(person)
- `Dr. Musger`(person)
- `Dr. Schwarzenbacher`(person)
- `Dimitri Stegmeyr`(person)
- `Dr. Marcella Prunbauer`(person)
- `Okumus Chemie GmbH`(organisation)
- `Littrowgasse 6, 3474 Kollersdorf, Österreich`(address)
- `Prof. Haslinger & Partner, Rechtsanwälte`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Steyr`(organisation)

**Example 63** (doc_id: `deanon_260716_TRAIN/4Ob165_09g`) (sent_id: `deanon_260716_TRAIN/4Ob165_09g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Schenk als Vorsitzende sowie die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei DRH Cloud AG, Viertlerweg 451, 2533 Glashütten, Österreich, vertreten durch Ewald Weninger Rechtsanwalts GmbH in Wien, gegen die beklagte Partei West Steinfen AG, Josef-Kainzmayer-Gasse 9, 4271 Witzelsberg, Österreich, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Feststellung und Anfechtung (Streitwert: 101.000.000 EUR), im Verfahren über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Juni 2009, GZ 5 R 44/09s-15, womit das Urteil des Handelsgerichts Wien vom 26. Jänner 2008, GZ 19 Cg 98/08w-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Zurückziehung der außerordentlichen Revision der klagenden Partei dient zur Kenntnis.

**False Positives:**

- `Ewald Weninger Rechtsanwalts Gmb` — partial — pred is substring of gold: `Ewald Weninger Rechtsanwalts GmbH`
- `Sch` — similar text (different position): `Dr. Schenk`

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

**Example 64** (doc_id: `deanon_260716_TRAIN/4Ob180_10i`) (sent_id: `deanon_260716_TRAIN/4Ob180_10i_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Nimtz Pharma GmbH, Mildenbergstraße 11, 3072 Furth, Österreich, vertreten durch Berger Saurer Zöchbauer, Rechtsanwälte in Wien, gegen die beklagten Parteien 1) Unikel Landwirtschaft GmbH & Co KG und 2) Gode+Panköker Getränke GmbH, Martinsplatz 1-31, 9831 Kleindorf, Österreich, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Provisorialverfahren 36.000 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 6. August 2010, GZ 5 R 150/10f-7, womit der Beschluss des Handelsgerichts Wien vom 24. Juni 2010, GZ 11 Cg 117/10h-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Berger Saurer` — partial — pred is substring of gold: `Berger Saurer Zöchbauer, Rechtsanwälte`
- `Gheneff` — partial — pred is substring of gold: `Gheneff - Rami - Sommer Rechtsanwälte KG`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 65** (doc_id: `deanon_260716_TRAIN/4Ob185_22t`) (sent_id: `deanon_260716_TRAIN/4Ob185_22t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Kodek als Vorsitzenden und die Hofräte Dr. Schwarzenbacher und MMag. Matzka sowie die Hofrätinnen Mag. Istjan, LL.M., und Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Brümann Bau GmbH, Simon-von-Stampfer-Straße 3T, 3943 Gebharts, Österreich, vertreten durch Univ.-Doz.

**False Positives:**

- `Univ` — similar text (different position): `Univ.-Prof. Dr. Kodek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. Schwarzenbacher`(person)
- `MMag. Matzka`(person)
- `Mag. Istjan, LL.M.`(person)
- `Mag. Fitz`(person)
- `Brümann Bau GmbH`(organisation)
- `Simon-von-Stampfer-Straße 3T, 3943 Gebharts, Österreich`(address)

**Example 66** (doc_id: `deanon_260716_TRAIN/4Ob196_10t`) (sent_id: `deanon_260716_TRAIN/4Ob196_10t_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Lemlemcon GmbH, Albert-Schultz-Eishalle 4, 6863 Großdorf, Österreich, vertreten durch Berger Saurer Zöchbauer, Rechtsanwälte in Wien, gegen die beklagten Parteien 1. Koldere und Heddrich Versicherung GmbH & Co KG, 2.

**False Positives:**

- `Berger Saurer` — partial — pred is substring of gold: `Berger Saurer Zöchbauer, Rechtsanwälte`

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

**Example 67** (doc_id: `deanon_260716_TRAIN/4Ob196_10t`) (sent_id: `deanon_260716_TRAIN/4Ob196_10t_4`)


Monderdorf Cloud GmbH, R.-Hamerling-Gasse 4, 6373 Jochberg, Österreich, beide vertreten durch Ruggenthaler Rechtsanwalts KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 62.000 EUR) über den außerordentlichen Revisionsrekurs der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Wien vom 20. September 2010, GZ 30 R 29/10w-9, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Ruggenthaler Rechtsanwalts` — partial — pred is substring of gold: `Ruggenthaler Rechtsanwalts KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Monderdorf Cloud GmbH`(organisation)
- `R.-Hamerling-Gasse 4, 6373 Jochberg, Österreich`(address)
- `Ruggenthaler Rechtsanwalts KG`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 68** (doc_id: `deanon_260716_TRAIN/4Ob19_10p`) (sent_id: `deanon_260716_TRAIN/4Ob19_10p_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei StadtEnergie Planung gesellschaft mbH,*****, vertreten durch Prof. Haslinger & Partner, Rechtsanwälte in Linz, gegen die beklagte Partei Deecken Event AG,*****, vertreten durch Rechtsanwälte Konrad & Schröttner OG in Graz, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 65.000 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 25. November 2009, GZ 6 R 169/09h-37, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof. Haslinger & Partner, Rechtsanwälte`
- `Rechtsanw` — similar text (different position): `Prof. Haslinger & Partner, Rechtsanwälte`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 69** (doc_id: `deanon_260716_TRAIN/4Ob201_10b`) (sent_id: `deanon_260716_TRAIN/4Ob201_10b_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Kevin Woelfel OEG, Rudolf Radinger-Straße 110o, 4623 Moostal, Österreich, vertreten durch Dr. Martin Leitner und Dr. Ralph Trischler, Rechtsanwälte in Wien, gegen die beklagte Partei Rätz Handel GmbH, Schögglstraße 25, 4085 Dankmairing, Österreich, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung, Rechnungslegung, Schadenersatz und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 36.000 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 27. September 2010, GZ 1 R 192/10b-13, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß Der Antrag auf Zuspruch der Kosten der Revisionsrekursbeantwortung wird gemäß § 508a Abs 2 Satz 2 und § 521a Abs 2 ZPO abgewiesen.

**False Positives:**

- `Bichler Zrzavy Rechtsanw` — partial — pred is substring of gold: `Bichler Zrzavy Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schenk`(person)
- `Dr. Vogel`(person)
- `Dr. Jensik`(person)
- `Dr. Musger`(person)
- `Dr. Schwarzenbacher`(person)
- `Kevin Woelfel`(person)
- `Rudolf Radinger-Straße 110o, 4623 Moostal, Österreich`(address)
- `Dr. Martin Leitner`(person)
- `Dr. Ralph Trischler`(person)
- `Rätz Handel GmbH`(organisation)
- `Schögglstraße 25, 4085 Dankmairing, Österreich`(address)
- `Bichler Zrzavy Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)

**Example 70** (doc_id: `deanon_260716_TRAIN/4Ob24_20p`) (sent_id: `deanon_260716_TRAIN/4Ob24_20p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Vogel als Vorsitzenden und die Hofräte Dr. Schwarzenbacher, Hon.-Prof. Dr. Brenn, Priv.-Doz. Dr. Rassi und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Parteien 1. MittelLogunitraForschung Consulting GmbH, In der Hofau 11, 3623 Leopolds, Österreich, 2. BZLB Umwelt GmbH, Lahnweg 79, 9572 Messaneggen, Österreich, beide vertreten durch Partnerschaft SCHUPPICH SPORN & WINISCHHOFER Rechtsanwälte in Wien, gegen die beklagte Partei Fennex Elektro GmbH, Rohner 20, 9470 Johannesberg, Österreich, vertreten durch PISTOTNIK & KRILYSZYN Rechtsanwälte in Wien, und die Nebenintervenientin auf Seiten der beklagten Partei Mittel Tranexber GmbH, Eichhaltweg 18, 4582 Seebach, Österreich, vertreten durch Mag. Dr. Dirk Just, Rechtsanwalt in Wien, wegen zuletzt 4.264.783,18 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. November 2019, GZ 129 R 91/19d-367, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partnerschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Vogel`(person)
- `Dr. Schwarzenbacher`(person)
- `Hon.-Prof. Dr. Brenn`(person)
- `Priv.-Doz. Dr. Rassi`(person)
- `MMag. Matzka`(person)
- `MittelLogunitraForschung Consulting GmbH`(organisation)
- `In der Hofau 11, 3623 Leopolds, Österreich`(address)
- `BZLB Umwelt GmbH`(organisation)
- `Lahnweg 79, 9572 Messaneggen, Österreich`(address)
- `SCHUPPICH SPORN & WINISCHHOFER Rechtsanwälte`(organisation)
- `Fennex Elektro GmbH`(organisation)
- `Rohner 20, 9470 Johannesberg, Österreich`(address)
- `PISTOTNIK & KRILYSZYN Rechtsanwälte`(organisation)
- `Mittel Tranexber GmbH`(organisation)
- `Eichhaltweg 18, 4582 Seebach, Österreich`(address)
- `Mag. Dr. Dirk Just`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 71** (doc_id: `deanon_260716_TRAIN/4Ob26_20g`) (sent_id: `deanon_260716_TRAIN/4Ob26_20g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Vogel als Vorsitzenden und die Hofräte Dr. Schwarzenbacher, Hon.-Prof. Dr. Brenn, Priv.-Doz. Dr. Rassi und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Xenia Pintar GmbH, Alfred Leiner-Straße 15, 8674 Grubbauer, Österreich, vertreten durch Rechtsanwaltskanzlei Dr. Wendling GmbH in Kitzbühel, gegen die beklagte Partei Sudwil-Umwelt GmbH, Pleschberg 7, 9872 Gössering, Österreich, Deutschland, vertreten durch Dr. Dan Katzlinger, Rechtsanwalt in Innsbruck, wegen 70.000 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. Dezember 2019, GZ 10 R 49/19k-32, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rechtsanwaltskanzlei Dr` — positional overlap with gold: `Dr. Wendling GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Vogel`(person)
- `Dr. Schwarzenbacher`(person)
- `Hon.-Prof. Dr. Brenn`(person)
- `Priv.-Doz. Dr. Rassi`(person)
- `MMag. Matzka`(person)
- `Xenia Pintar`(person)
- `Alfred Leiner-Straße 15, 8674 Grubbauer, Österreich`(address)
- `Dr. Wendling GmbH`(organisation)
- `Sudwil-Umwelt GmbH`(organisation)
- `Pleschberg 7, 9872 Gössering, Österreich`(address)
- `Dr. Dan Katzlinger`(person)
- `Oberlandesgerichts Innsbruck`(organisation)

**Example 72** (doc_id: `deanon_260716_TRAIN/4Ob29_17v`) (sent_id: `deanon_260716_TRAIN/4Ob29_17v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Vogel als Vorsitzenden sowie die Hofräte Dr. Jensik, Dr. Schwarzenbacher, Dr. Rassi und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Techn R Xaver Alfert, vertreten durch Dr. Dieter Brandstätter, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Edith Finkbohner, vertreten durch Lorenz & Strobl, Rechtsanwälte in Innsbruck, wegen 7.200 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 25. November 2016, GZ 4 R 230/16a-30, womit das Urteil des Bezirksgerichts Innsbruck vom 4. August 2016, GZ 13 C 423/15k-22, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Lorenz` — partial — pred is substring of gold: `Lorenz & Strobl, Rechtsanwälte`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Vogel`(person)
- `Dr. Jensik`(person)
- `Dr. Schwarzenbacher`(person)
- `Dr. Rassi`(person)
- `MMag. Matzka`(person)
- `Techn R Xaver Alfert`(person)
- `Dr. Dieter Brandstätter`(person)
- `Edith Finkbohner`(person)
- `Lorenz & Strobl, Rechtsanwälte`(organisation)
- `Landesgerichts Innsbruck`(organisation)
- `Bezirksgerichts Innsbruck`(organisation)

**Example 73** (doc_id: `deanon_260716_TRAIN/4Ob9_20g`) (sent_id: `deanon_260716_TRAIN/4Ob9_20g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Vogel als Vorsitzenden und die Hofräte Dr. Schwarzenbacher, Hon.-Prof. Dr. Brenn, Priv.-Doz. Dr. Rassi und MMag. Matzka als weitere Richter in der Rechtssache der klagenden Partei Ingrid Marke, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1) ZTYW Solar Vertrieb GmbH, Hans-Woerle-Weg 13, 4852 Gahberg, Österreich, und 2) Hoch Fenfurtmon Systeme AG, Raxer Straße 24, 8952 Kienach, Österreich, beide vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 11.091,23 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 6. November 2019, GZ 2 R 158/19x-27, mit dem das Urteil des Landesgerichts Linz vom 29. August 2019, GZ 36 Cg 14/18h-22, bestätigt wurde, den Beschluss gefasst:  Spruch I. Das Revisionsverfahren zu 4 Ob 9/20g wird bis zur Vorabentscheidung des Gerichtshofs der Europäischen Union über das Vorabentscheidungsersuchen des Obersten Gerichtshofs vom 17.

**False Positives:**

- `Poduschka Anwaltsgesellschaft` — partial — pred is substring of gold: `Poduschka Anwaltsgesellschaft mbH`
- `Pressl Endl Heinrich Bamberger Rechtsanw` — partial — pred is substring of gold: `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Vogel`(person)
- `Dr. Schwarzenbacher`(person)
- `Hon.-Prof. Dr. Brenn`(person)
- `Priv.-Doz. Dr. Rassi`(person)
- `MMag. Matzka`(person)
- `Ingrid Marke`(person)
- `Poduschka Anwaltsgesellschaft mbH`(organisation)
- `ZTYW Solar Vertrieb GmbH`(organisation)
- `Hans-Woerle-Weg 13, 4852 Gahberg, Österreich`(address)
- `Hoch Fenfurtmon Systeme AG`(organisation)
- `Raxer Straße 24, 8952 Kienach, Österreich`(address)
- `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`(organisation)
- `Oberlandesgerichts Linz`(organisation)
- `Landesgerichts Linz`(organisation)
- `Obersten Gerichtshofs`(organisation)

**Example 74** (doc_id: `deanon_260716_TRAIN/5Nc28_19s`) (sent_id: `deanon_260716_TRAIN/5Nc28_19s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofrätin Dr. Grohmann und den Hofrat Dr. Steger als weitere Richter in der Pflegschaftssache des mj Aron Margwarth, geboren am 29. März 1957, Vater Klaus Rufer, vertreten durch Prof. Dr. Georg Zanger, Rechtsanwalt in Wien, wegen Obsorge, über den Delegierungsantrag der Mutter Rafaela Erreth, vertreten durch Mag. Britta Schönhart-Loinig, Rechtsanwältin in Wien, den Beschluss gefasst:  Spruch Der Antrag auf Delegierung der Pflegschaftssache vom Bezirksgericht Gänserndorf an das Bezirksgericht Villach wird abgewiesen.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof. Dr. Georg Zanger`

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

**Example 75** (doc_id: `deanon_260716_TRAIN/5Ob102_24x`) (sent_id: `deanon_260716_TRAIN/5Ob102_24x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei ÖkR KzlR Sonja Doganoglu, wider die beklagte Partei Stoeberl Bau AG, Bernhard-Paumgartner-Weg 41, 3233 Hohenbrand, Österreich, Deutschland vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 13.607,40 EUR sA und Feststellung über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Ried im Innkreis als Berufungsgericht vom 13. März 2024, GZ 18 R 2/24k-29, mit dem das Urteil des Bezirksgerichts Schärding vom 6. November 2023, GZ 2 C 478/20g-24, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Pressl Endl Heinrich Bamberger Rechtsanw` — partial — pred is substring of gold: `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`

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

**Example 76** (doc_id: `deanon_260716_TRAIN/5Ob106_20d`) (sent_id: `deanon_260716_TRAIN/5Ob106_20d_28`)


Es führte Erhebungen durch Einholung einer Auskunft der Schule des mj Igor Doelfel, Einsicht in die im Rekursverfahren vorgelegten Urkunden und Einvernahme beider Eltern im Zug einer mündlichen Verhandlung durch und traf ergänzende Festellungen zur schulischen Situation des mj VetR Marion Dickopp und zur Wohnsituation bei den Eltern.

**False Positives:**

- `Marion Dickopp` — partial — pred is substring of gold: `VetR Marion Dickopp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Igor Doelfel`(person)
- `VetR Marion Dickopp`(person)

**Example 77** (doc_id: `deanon_260716_TRAIN/5Ob141_23f`) (sent_id: `deanon_260716_TRAIN/5Ob141_23f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Svenja Brochtrup, vertreten durch Poduschka Partner AnwaltsGmbH in Linz, gegen die beklagte Partei EnnsFinanzen AG, Bartlstraße 9, 8490 Zelting, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 19.600 EUR sA über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 22. Mai 2023, GZ 12 R 6/23y-34, mit dem das Urteil des Landesgerichts Wels vom 11. Jänner 2023, GZ 8 Cg 29/20s-29, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Poduschka Partner Anwalts` — no gold match — likely missing annotation
- `Pressl Endl Heinrich Bamberger Rechtsanw` — partial — pred is substring of gold: `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`

> overlaps gold: 1  |  likely missing annotation: 1

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

**Example 78** (doc_id: `deanon_260716_TRAIN/5Ob174_15x`) (sent_id: `deanon_260716_TRAIN/5Ob174_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der außerstreitigen Wohnrechtssache der Antragstellerin Ulrike Richardson, vertreten durch Mag. Valerie Gröschl, Mietervereinigung Österreichs, 1010 Wien, Reichsratsstraße 15, gegen die Antragsgegnerin Traun Nortriost Holding GmbH, Prof.-Ernst-Schandl-Park 18J, 4343 Inzing, Österreich, vertreten durch Mag. Günter Petzelbauer, Rechtsanwalt in Wien, wegen § 37 Abs 1 Z 8 iVm § 16 MRG, über den außerordentlichen Revisionsrekurs der Antragsgegnerin gegen den Sachbeschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 27. Mai 2015, GZ 39 R 136/15m-17, mit dem der Sachbeschluss des Bezirksgerichts Hernals vom 30. Dezember 2014, GZ 5 Msch 15/14g-12, bestätigt wurde, den Beschluss gefasst:  Spruch Dem außerordentlichen Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Mag` — similar text (different position): `Mag. Wurzer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Hradil`(person)
- `Dr. Höllwerth`(person)
- `Dr. Grohmann`(person)
- `Mag. Wurzer`(person)
- `Mag. Painsi`(person)
- `Ulrike Richardson`(person)
- `Mag. Valerie Gröschl`(person)
- `Traun Nortriost Holding GmbH`(organisation)
- `Prof.-Ernst-Schandl-Park 18J, 4343 Inzing, Österreich`(address)
- `Mag. Günter Petzelbauer`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Hernals`(organisation)

**Example 79** (doc_id: `deanon_260716_TRAIN/5Ob184_21a`) (sent_id: `deanon_260716_TRAIN/5Ob184_21a_4`)


Christian den Drijver, 2. Techn R Adalbert Amirzadeh, ebenda, beide vertreten durch Schlösser & Partner Rechtsanwälte OG in Wien, gegen die Antragsgegnerin Marion Döhnert, vertreten durch Mag. Michael Operschal Rechtsanwalt GmbH in Wien, wegen § 37 Abs 1 Z 8 iVm § 16 MRG, über den Revisionsrekurs der Antragsteller gegen den Sachbeschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 19. Mai 2021, GZ 40 R 2/21x-15, mit dem der Sachbeschluss des Bezirksgerichts Floridsdorf vom 30. Oktober 2020, GZ 28 Msch 9/19g-11, abgeändert wurde, den Sachbeschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Schl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Christian den Drijver`(person)
- `Techn R Adalbert Amirzadeh`(person)
- `Partner Rechtsanwälte OG`(organisation)
- `Marion Döhnert`(person)
- `Mag. Michael Operschal Rechtsanwalt GmbH`(organisation)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Floridsdorf`(organisation)

**Example 80** (doc_id: `deanon_260716_TRAIN/5Ob22_24g`) (sent_id: `deanon_260716_TRAIN/5Ob22_24g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Lemheim GmbH, Galling 115, 3464 Zaina, Österreich, vertreten durch Dr. Manfred Palkovits, Mag. Martin Sohm, Rechtsanwälte in Wien, gegen die beklagte Partei Christina Kucharzewski, vertreten durch Dr. Günter Schandor, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtsachen Wien als Berufungsgericht vom 8. November 2023, GZ 38 R 142/23y-27, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Jensik`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Jensik`(person)
- `Mag. Wurzer`(person)
- `Mag. Painsi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Steger`(person)
- `Lemheim GmbH`(organisation)
- `Galling 115, 3464 Zaina, Österreich`(address)
- `Dr. Manfred Palkovits`(person)
- `Mag. Martin Sohm`(person)
- `Christina Kucharzewski`(person)
- `Dr. Günter Schandor`(person)

**Example 81** (doc_id: `deanon_260716_TRAIN/5Ob259_15x`) (sent_id: `deanon_260716_TRAIN/5Ob259_15x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers Shoshana Dimpfel, vertreten durch Hofbauer & Wagner Rechtsanwälte KG in St. Pölten, gegen den Antragsgegner Adolf Beehr, vertreten durch Dr. Franz Gütlbauer, Dr. Siegfried Sieghartsleitner, Dr. Michael Pichlmair, Rechtsanwälte in Wels, wegen § 8 Abs 2 MRG (hier: wegen Abänderung des Sachbeschlusses des Bezirksgerichts Traun vom 18. März 2014, GZ 17 Msch 6/13m-8) über den „Rekurs“ des Antragsgegners gegen den Beschluss des Landesgerichts Linz als Rekursgericht vom 8. Oktober 2015, GZ 14 R 56/15a-22, mit dem der Beschluss des Bezirksgerichts Traun vom 25. Februar 2015, GZ 17 Msch 6/13m-18, bestätigt wurde, den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Hofbauer` — partial — pred is substring of gold: `Hofbauer & Wagner Rechtsanwälte KG`

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

**Example 82** (doc_id: `deanon_260716_TRAIN/5Ob30_11i`) (sent_id: `deanon_260716_TRAIN/5Ob30_11i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und die Hofrätinnen Dr. Hurch und Dr. Lovrek sowie die Hofräte Dr. Höllwerth und Mag. Wurzer als weitere Richter in der wohnrechtlichen Außerstreitsache der Antragstellerin Edith Ilse Semyonov, vertreten durch Maraszto Milisits Rechtsanwälte OG in Wien, gegen den Antragsgegner DDr. Ernest Bayraktar, vertreten durch Dr. Erich Kafka und Dr. Manfred Palkovits, Rechtsanwälte in Wien, wegen §§ 6 Abs 2, 37 Abs 1 Z 2 MRG, über den Revisionsrekurs des Antragsgegners gegen den Sachbeschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 27. Oktober 2010, GZ 39 R 248/10z-60, mit dem infolge Rekurses des Antragsgegners der Sachbeschluss des Bezirksgerichts Döbling vom 27. April 2010, GZ 15 Msch 10/07p-51, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Maraszto Milisits Rechtsanw` — partial — pred is substring of gold: `Maraszto Milisits Rechtsanwälte OG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Danzl`(person)
- `Dr. Hurch`(person)
- `Dr. Lovrek`(person)
- `Dr. Höllwerth`(person)
- `Mag. Wurzer`(person)
- `Edith Ilse Semyonov`(person)
- `Maraszto Milisits Rechtsanwälte OG`(organisation)
- `DDr. Ernest Bayraktar`(person)
- `Dr. Erich Kafka`(person)
- `Dr. Manfred Palkovits`(person)
- `Landesgerichts für Zivilrechtssachen Wien`(organisation)
- `Bezirksgerichts Döbling`(organisation)

**Example 83** (doc_id: `deanon_260716_TRAIN/5Ob63_21g`) (sent_id: `deanon_260716_TRAIN/5Ob63_21g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer, Mag. Painsi und Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Alexander Imberg, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Antonia Diemar, vertreten durch Lansky, Ganzger & Partner Rechtsanwälte GmbH in Wien, wegen 405.188,80 EUR sA und Feststellung (Streitwert 35.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 18. Februar 2021, GZ 11 R 8/21h-28, mit dem die Berufung der beklagten Partei gegen das Versäumungsurteil des Landesgerichts für Zivilrechtssachen Wien vom 11. August 2020, GZ 17 Cg 55/20p-4, zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Lansky` — partial — pred is substring of gold: `Lansky, Ganzger & Partner Rechtsanwälte GmbH`

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

**Example 84** (doc_id: `deanon_260716_TRAIN/5Ob93_24y`) (sent_id: `deanon_260716_TRAIN/5Ob93_24y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Schoenknecht Elektro GmbH, Stinygasse 3V, 3383 Löbersdorf, Österreich, vertreten durch Rechtsanwälte Dr. Amhof & Dr. Damian GmbH in Wien, gegen die beklagte Partei Esra Mevis, wegen Unterfertigung eines Wohnungseigentumsvertrags und Feststellung, hier: Anmerkung der Klage, über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 26. April 2024, GZ 15 R 41/24w-18, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 126 Abs 1 GBG iVm § 62 Abs 1 AußStrG zurückgewiesen.

**False Positives:**

- `Rechtsanw` — partial — pred is substring of gold: `Rechtsanwälte Dr. Amhof & Dr. Damian GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Jensik`(person)
- `Mag. Wurzer`(person)
- `Mag. Painsi`(person)
- `Dr. Weixelbraun-Mohr`(person)
- `Dr. Steger`(person)
- `Schoenknecht Elektro GmbH`(organisation)
- `Stinygasse 3V, 3383 Löbersdorf, Österreich`(address)
- `Rechtsanwälte Dr. Amhof & Dr. Damian GmbH`(organisation)
- `Esra Mevis`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 85** (doc_id: `deanon_260716_TRAIN/6Ob101_22d`) (sent_id: `deanon_260716_TRAIN/6Ob101_22d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Nowotny, Dr. Hofer-Zeni-Rennhofer, Dr. Faber und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei DDr.in Jeannine Friemberger, vertreten durch Dr. Karl Hepperger, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Synnex Daten GmbH, Starz 11, 4642 Sattledt, Österreich, vertreten durch Dr. Günther Egger und Dr. Karl Heiss, Rechtsanwälte in Innsbruck, wegen 31.238,92 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 14. April 2022, GZ 2 R 38/22p-54, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Dr` — similar text (different position): `Hon.-Prof. Dr. Gitschthaler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Gitschthaler`(person)
- `Dr. Nowotny`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Faber`(person)
- `Mag. Pertmayr`(person)
- `DDr.in Jeannine Friemberger`(person)
- `Dr. Karl Hepperger`(person)
- `Synnex Daten GmbH`(organisation)
- `Starz 11, 4642 Sattledt, Österreich`(address)
- `Dr. Günther Egger`(person)
- `Dr. Karl Heiss`(person)
- `Oberlandesgerichts Innsbruck`(organisation)

**Example 86** (doc_id: `deanon_260716_TRAIN/6Ob105_20i`) (sent_id: `deanon_260716_TRAIN/6Ob105_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden, die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Jaden Ince, vertreten durch Mag. Erwin Falkner, Rechtsanwalt in Wien, gegen die beklagte Partei R. Enns Verfurt GmbH, Greifenberg 38, 4972 Windhag, Österreich, vertreten durch Hoffmann & Sykora Rechtsanwälte KG in Tulln, wegen 6.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts St. Pölten als Berufungsgericht vom 13. November 2019, GZ 21 R 208/19z-53, womit über Berufung der klagenden Partei das Urteil des Bezirksgerichts Tulln vom 23. Juni 2019, GZ 11 C 276/18p-49, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Hoffmann` — partial — pred is substring of gold: `Hoffmann & Sykora Rechtsanwälte KG`

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

**Example 87** (doc_id: `deanon_260716_TRAIN/6Ob10_22x`) (sent_id: `deanon_260716_TRAIN/6Ob10_22x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Nowotny, Dr. Hofer-Zeni-Rennhofer, Dr. Faber und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Tralog-KI Versicherungs AG, Adolf Schwayer-Gasse 22, 3371 Hofa, Österreich, vertreten durch Musey Rechtsanwalt GmbH in Salzburg, gegen die beklagte Partei WaldRecycling GmbH, Georg-Rendl-Weg 28, 9065 Ebenthal, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 7.246.839 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 1. Dezember 2021, GZ 2 R 165/21d-49, womit das Teil- und Zwischenurteil des Landesgerichts Salzburg vom 6. September 2021, GZ 6 Cg 16/20m-45, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Musey Rechtsanwalt Gmb` — partial — pred is substring of gold: `Musey Rechtsanwalt GmbH`
- `Pressl Endl Heinrich Bamberger Rechtsanw` — partial — pred is substring of gold: `Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 88** (doc_id: `deanon_260716_TRAIN/6Ob118_16w`) (sent_id: `deanon_260716_TRAIN/6Ob118_16w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden und durch die Hofräte Dr. Schramm, Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Ing. Laurence Joester, vertreten durch Dr. Wolfgang Leitner, Priv.-Doz. Dr. Max Leitner, Dr. Mara-Sophie Häusler, Rechtsanwälte in Wien, gegen die beklagte Partei Jasper Ratloff, vertreten durch Lederer Rechtsanwalt GmbH in Wien, und der Nebenintervenienten auf Seite der beklagten Partei 1.

**False Positives:**

- `Lederer Rechtsanwalt Gmb` — partial — pred is substring of gold: `Lederer Rechtsanwalt GmbH`

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

**Example 89** (doc_id: `deanon_260716_TRAIN/6Ob118_16w`) (sent_id: `deanon_260716_TRAIN/6Ob118_16w_4`)


Unizorbach GmbH in Liquidation, Hallhuber&Jaecklin Garten, 2. Mühlenjost Digital GmbH, Handelberg 13, 8573 Gallmannsegg, Österreich, Deutschland, beide vertreten durch Wess Kispert Rechtsanwalts GmbH in Wien, wegen 103.578,16 EUR sA und Feststellung, über die Rekurse der beklagten Partei und der Nebenintervenienten gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 13. April 2016, GZ 14 R 173/16m-39, womit das Urteil des Landesgerichts Eisenstadt vom 31. August 2015, GZ 3 Cg 166/13y-34, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Den Rekursen wird nicht Folge gegeben.

**False Positives:**

- `Wess Kispert Rechtsanwalts Gmb` — partial — pred is substring of gold: `Wess Kispert Rechtsanwalts GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unizorbach GmbH`(organisation)
- `Hallhuber&Jaecklin Garten`(organisation)
- `Mühlenjost Digital GmbH`(organisation)
- `Handelberg 13, 8573 Gallmannsegg, Österreich`(address)
- `Wess Kispert Rechtsanwalts GmbH`(organisation)
- `Oberlandesgerichts Wien`(organisation)
- `Landesgerichts Eisenstadt`(organisation)

**Example 90** (doc_id: `deanon_260716_TRAIN/6Ob11_23w`) (sent_id: `deanon_260716_TRAIN/6Ob11_23w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Nowotny, Dr. Hofer-Zeni-Rennhofer, Dr. Faber und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Gloria Thurn, vertreten durch Mag. Volkan Kaya, Rechtsanwalt in Wien, wider die beklagte Partei Dr.in Griselda Heilmeier, vertreten durch Mag. Gülay Aydemir, Rechtsanwältin in Wien, wegen Rechnungslegung und Zahlung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Juni 2022, GZ 5 R 28/22g-53, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mag` — similar text (different position): `Mag. Pertmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Hon.-Prof. Dr. Gitschthaler`(person)
- `Dr. Nowotny`(person)
- `Dr. Hofer-Zeni-Rennhofer`(person)
- `Dr. Faber`(person)
- `Mag. Pertmayr`(person)
- `Gloria Thurn`(person)
- `Mag. Volkan Kaya`(person)
- `Dr.in Griselda Heilmeier`(person)
- `Mag. Gülay Aydemir`(person)
- `Oberlandesgerichts Wien`(organisation)

**Example 91** (doc_id: `deanon_260716_TRAIN/6Ob139_19p`) (sent_id: `deanon_260716_TRAIN/6Ob139_19p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Balthasar Teske, vertreten durch Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG in Wien, gegen die beklagte Partei Prof. Dr. Roderich Claaßens, vertreten durch Brauneis Klauser Prändl Rechtsanwälte GmbH in Wien, wegen Rechnungslegung und Zahlung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 22. April 2019, GZ 14 R 152/18b-16, womit das Teilurteil des Landesgerichts für Zivilrechtssachen Wien vom 27. September 2018, GZ 4 Cg 50/17b-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Brauneis Klauser Pr` — partial — pred is substring of gold: `Brauneis Klauser Prändl Rechtsanwälte GmbH`

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

**Example 92** (doc_id: `deanon_260716_TRAIN/6Ob169_12i`) (sent_id: `deanon_260716_TRAIN/6Ob169_12i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Pimmer als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Dr. Schramm, Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Seesteincon-Transport GmbH, Wildbacher Straße 174, 3623 Bernhards, Österreich, vertreten durch List Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Heimnor GmbH, Am Johannisgraben 44, 8200 Albersdorf, Österreich, vertreten durch Dr. Christoph Brenner - Mag. Severin Perschl Rechtsanwälte OG in Krems, wegen 7.641,30 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Korneuburg als Berufungsgericht vom 16. Februar 2012, GZ 21 R 262/11v-50, womit das Urteil des Bezirksgerichts Gänserndorf vom 2. August 2011, GZ 12 C 1036/10h-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `List Rechtsanw` — partial — pred is substring of gold: `List Rechtsanwälte GmbH`

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

**Example 93** (doc_id: `deanon_260716_TRAIN/6Ob177_10p`) (sent_id: `deanon_260716_TRAIN/6Ob177_10p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Pimmer als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Dr. Schramm, Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Edgar Hoffschroer, BA, vertreten durch Dr. Karl Maier Rechtsanwaltsgesellschaft mbH in Knittelfeld, gegen die beklagte Partei Esra Kunhardt, vertreten durch Ing. Mag. Dr. Felix Jurak, Rechtsanwalt in Klagenfurt, und ihres Nebenintervenienten DI Paul Domgörgen, vertreten durch Frimmel/Anetter Rechtsanwaltsgesellschaft mbH in Klagenfurt, wegen 15.644,98 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 29. April 2010, GZ 4 R 15/10y-73, womit das Urteil des Landesgerichts Klagenfurt vom 27. Oktober 2009, GZ 20 Cg 183/06y-66, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Ing` — partial — pred is substring of gold: `Ing. Mag. Dr. Felix Jurak`
- `Frimmel` — partial — pred is substring of gold: `Frimmel/Anetter Rechtsanwaltsgesellschaft mbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Obersten Gerichtshofs`(organisation)
- `Hon.-Prof. Dr. Pimmer`(person)
- `Obersten Gerichtshofs`(organisation)
- `Dr. Schramm`(person)
- `Dr. Gitschthaler`(person)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. Nowotny`(person)
- `Edgar Hoffschroer, BA`(person)
- `Dr. Karl`(person)
- `Esra Kunhardt`(person)
- `Ing. Mag. Dr. Felix Jurak`(person)
- `DI Paul Domgörgen`(person)
- `Frimmel/Anetter Rechtsanwaltsgesellschaft mbH`(organisation)
- `Oberlandesgerichts Graz`(organisation)
- `Landesgerichts Klagenfurt`(organisation)

**Example 94** (doc_id: `deanon_260716_TRAIN/6Ob182_20p`) (sent_id: `deanon_260716_TRAIN/6Ob182_20p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden und die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des Minderjährigen ÖkR Techn R Mag.a Helge Cigan, geboren am 13. Dezember 2007, 3. September 1976, vertreten durch das Land Wien (Stadt Wien Kinder- und Jugendhilfe Rechtsvertretung Bezirk 22, 1220 Wien, Simone-de-Beauvoir-Platz 6) als Kinder- und Jugendhilfeträger, über den Revisionsrekurs des Vaters Quentin Martschinke, vertreten durch Anwaltssocietät Sattlegger Dorninger Steiner & Partner in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 25. Juni 2020, GZ 43 R 237/20a-31, mit dem der Beschluss des Bezirksgerichts Donaustadt vom 21. April 2020, GZ 1 P 135/18y-22, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wirdzurückgewiesen.

**False Positives:**

- `Anwaltssociet` — no gold match — likely missing annotation

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

**Example 95** (doc_id: `deanon_260716_TRAIN/6Ob18_20w`) (sent_id: `deanon_260716_TRAIN/6Ob18_20w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden, durch die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny sowie durch die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Iris Blumstock, vertreten durch Dorda Rechtsanwälte GmbH in Wien, wider die beklagte Partei Dr. Peter Temir, vertreten durch Dr. Thomas Weber, Rechtsanwalt in Baden, und den Nebenintervenienten auf Seiten der beklagten Partei Dr. Emanuela Brinkhuis, vertreten durch Prettenhofer Raimann Pérez Rechtsanwaltspartnerschaft in Wien, wegen Löschung und Unterlassung, über die außerordentlichen Revisionen der beklagten Partei und des Nebenintervenienten gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 19. November 2019, GZ 58 R 58/19f-36, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentlichen Revisionen werden gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dorda Rechtsanw` — partial — pred is substring of gold: `Dorda Rechtsanwälte GmbH`
- `Prettenhofer Raimann` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schramm`(person)
- `Dr. Gitschthaler`(person)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. Nowotny`(person)
- `Dr. Faber`(person)
- `Iris Blumstock`(person)
- `Dorda Rechtsanwälte GmbH`(organisation)
- `Dr. Peter Temir`(person)
- `Dr. Thomas Weber`(person)
- `Dr. Emanuela Brinkhuis`(person)
- `Landesgerichts Wiener Neustadt`(organisation)

**Example 96** (doc_id: `deanon_260716_TRAIN/6Ob207_18m`) (sent_id: `deanon_260716_TRAIN/6Ob207_18m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden und die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Dr. Ophelia Teegelbeckers, vertreten durch Ruggenthaler, Rest & Borsky, Rechtsanwälte OG in Wien, gegen die beklagten Parteien 1. IT Sudwerk GmbH, sowie 2.

**False Positives:**

- `Ruggenthaler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schramm`(person)
- `Dr. Gitschthaler`(person)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. Nowotny`(person)
- `Dr. Faber`(person)
- `Dr. Ophelia Teegelbeckers`(person)
- `IT Sudwerk GmbH`(organisation)

**Example 97** (doc_id: `deanon_260716_TRAIN/6Ob231_24z`) (sent_id: `deanon_260716_TRAIN/6Ob231_24z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Hofer-Zeni-Rennhofer als Vorsitzende sowie die Hofrätinnen und Hofräte Hon.-Prof. Dr. Faber, Mag. Pertmayr, Dr. Weber und Mag. Nigl LL.M. als weitere Richter in der Rechtssache der klagenden Partei Ing. Tiffany Jähncke, vertreten durch Poduschka Partner Anwaltsgesellschaft mbH in Linz, wider die beklagte Partei Sudconbach-Bau AG, Hart, Akazienstraße 15v, 4064 Oftering, Österreich, Deutschland, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 9.600 EUR sA, im Verfahren über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Linz als Berufungsgericht vom 7. Oktober 2024, GZ 6 R 57/24b-31, womit das Urteil des Bezirksgerichts Traun vom 16. Februar 2024, GZ 2 C 198/23z-22, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei vom 9. Dezember 2025 auf Fortsetzung des Verfahrens wird abgewiesen.

**False Positives:**

- `Poduschka Partner Anwaltsgesellschaft` — partial — pred is substring of gold: `Poduschka Partner Anwaltsgesellschaft mbH`

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

**Example 98** (doc_id: `deanon_260716_TRAIN/6Ob2_20t`) (sent_id: `deanon_260716_TRAIN/6Ob2_20t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden und die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Corvin Kohlmeier, vertreten durch ANWALTGMBH Rinner Teuchtmann in Linz, gegen die beklagte Partei Eckard Balbierer, vertreten durch Pallauf Meißnitzer Staindl & Partner, Rechtsanwälte in Salzburg, wegen 2.343.698,52 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. November 2019, GZ 3 R 125/19a-50, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Pallauf Mei` — partial — pred is substring of gold: `Pallauf Meißnitzer Staindl & Partner, Rechtsanwälte`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Oberste Gerichtshof`(organisation)
- `Dr. Schramm`(person)
- `Dr. Gitschthaler`(person)
- `Univ.-Prof. Dr. Kodek`(person)
- `Dr. Nowotny`(person)
- `Dr. Faber`(person)
- `Corvin Kohlmeier`(person)
- `ANWALTGMBH Rinner Teuchtmann`(organisation)
- `Eckard Balbierer`(person)
- `Pallauf Meißnitzer Staindl & Partner, Rechtsanwälte`(organisation)
- `Oberlandesgerichts Linz`(organisation)

**Example 99** (doc_id: `deanon_260716_TRAIN/6Ob56_19g`) (sent_id: `deanon_260716_TRAIN/6Ob56_19g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1060 Wien, Linke Wienzeile 18, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei QUMV Pflege GmbH, Nordring 89q, 2770 Gutenstein, Österreich, vertreten durch Dr. Peter Lindinger Dr. Andreas Pramer GesbR, Rechtsanwälte in Linz, wegen Unterlassung und Urteilsveröffentlichung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2019, GZ 3 R 141/18b-17, mit dem über Berufungen der klagenden und der beklagten Partei das Urteil des Landesgerichts Linz vom 2. September 2018, GZ 31 Cg 4/18a-9, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Kosesnik` — partial — pred is substring of gold: `Kosesnik-Wehrle & Langer Rechtsanwälte KG`

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

## `Herr/Frau Address` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ce712b26`  
**Description:**
Matches persons addressed as Herr or Frau in the text.

**Content:**
```
(?:Herr|Frau)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)
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

</details>

---

