# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-05-12T22:07:21.209504

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/ris/Qwen_Qwen3.5-35B-A3B/organisation/2026-05-11/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 600 |
| Validation documents | 151 |
| Test documents | 476 |
| Train sentences | 912 |
| Validation sentences | 238 |
| Test sentences | 23285 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 30 |
| Max samples in prompt | 60 |
| Refinement iterations | 0 |
| Seed | 42 |
| Agentic | False |
| Enable Critic | False |
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

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 98.4% |
| True Positives | 72 |
| False Positives | 510 |
| False Negatives | 273 |
| Total Gold Entities | 345 |
| Micro Precision | 12.4% |
| Micro Recall | 20.9% |
| Micro F1 | 15.5% |
| Macro F1 | 15.5% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Hyphenated_Organisations_Fixed` | 16.0% | 72.1% | 9.0% | 43 | 31 | 12 |
| `Hyphenated_Organisations` | 17.0% | 15.6% | 18.6% | 409 | 64 | 345 |
| `AG_Suffix_Tight` | 2.1% | 13.3% | 1.2% | 30 | 4 | 26 |
| `GmbH_Suffix_Tight` | 5.9% | 10.7% | 4.1% | 131 | 14 | 117 |
| `Limited_Suffix` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Ges_m_b_H_Suffix` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `GmbH_Co_KG_Pattern` | 0.0% | 0.0% | 0.0% | 22 | 0 | 22 |
| `Gesellschaft_m_b_H_Spaces` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Aktiengesellschaft_Pattern` | 0.0% | 0.0% | 0.0% | 6 | 0 | 6 |
| `Gesellschaft_m_b_H_Lowercase` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Industry_NoSuffix` | 0.0% | 0.0% | 0.0% | 10 | 0 | 10 |
| `Werke_Organisation` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `Gesellschaft_m_b_H_Prefix` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Versicherung_Organisation` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Gruppe_Organisation` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Compound_Organisations_NoSuffix` | 0.0% | 0.0% | 0.0% | 10 | 0 | 10 |
| `Acronym_Industry_Org` | 0.0% | 0.0% | 0.0% | 13 | 0 | 13 |
| `Specific_Org_List` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `Hyphenated_Organisations_Fixed`

**F1:** 0.160 | **Precision:** 0.721 | **Recall:** 0.090  

**Format:** `regex`  
**Description:**
Matches hyphenated organisation names specifically, ensuring the full name is captured.

**Content:**
```
\b([A-Z][a-zA-ZäöüÄÖÜß]+-[A-Z][a-zA-ZäöüÄÖÜß]+(?:\s+[A-Z][a-zA-ZäöüÄÖÜß]+)*\s+(?:GmbH|AG))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.721 | 0.090 | 0.160 | 43 | 31 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 31 | 12 | 314 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc22_13m`) (sent_id: `deanon_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Catharina Frielinghausen, Russische Föderation, gegen die verpflichtete Partei Gartcondon-Bildung GmbH, Alan Looß, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

| Predicted | Gold |
|---|---|
| `Gartcondon-Bildung GmbH` | `Gartcondon-Bildung GmbH` |

**Missed by this rule (FN):**

- `Catharina Frielinghausen` (person)
- `Alan Looß` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob18_25g`) (sent_id: `deanon_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Stanley Plogmeyer, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Tal-Daten GmbH, Karlheinz Hornschuck, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Tal-Daten GmbH` | `Tal-Daten GmbH` |

**Missed by this rule (FN):**

- `Stanley Plogmeyer` (person)
- `Karlheinz Hornschuck` (person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Daniel Wiegand, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei West-Medien Manufaktur GmbH in Liqu, Kanzelweg 32, 4850 Oberthalheim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `West-Medien Manufaktur GmbH` | `West-Medien Manufaktur GmbH` |

**Missed by this rule (FN):**

- `DI Daniel Wiegand` (person)
- `Kanzelweg 32, 4850 Oberthalheim, Österreich` (address)

**Example 3** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_8`)


Nach den wesentlichen Feststellungen (US 3 bis 6) befand sich die See-Maschinenbau GmbH in der zweiten Jahreshälfte 2008 in erheblichen Zahlungsschwierigkeiten.

| Predicted | Gold |
|---|---|
| `See-Maschinenbau GmbH` | `See-Maschinenbau GmbH` |

**Example 4** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__9`)


Text Gründe: Mit unbekämpft in Rechtskraft erwachsenen Urteilen des Bezirksgerichts Spittal an der Drau vom 22. Juni 2017, GZ 5 U 5/17f-26, wurden (I) Andreas Feiereisen des Vergehens der fahrlässigen Tötung nach § 80 Abs 1 StGB schuldig erkannt und hiefür zu einer Geldstrafe verurteilt sowie (II) die Werksynstein-Wind GmbH gemäß § 3 Abs 1 Z 2, Abs 2 VbVG für die vom Schuldspruch (I) erfasste Straftat ihres Entscheidungsträgers verantwortlich erklärt und über diese Gesellschaft eine Verbandsgeldbuße von 70 Tagessätzen zu je 50 Euro verhängt, die unter Bestimmung einer Probezeit von drei Jahren bedingt nachgesehen wurde.

| Predicted | Gold |
|---|---|
| `Werksynstein-Wind GmbH` | `Werksynstein-Wind GmbH` |

**Missed by this rule (FN):**

- `Feiereisen` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/1Ob16_20i`) (sent_id: `deanon_TRAIN/1Ob16_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Stadt Christina Schorer, vertreten durch die Benn-Ibler Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Donsteinlex AG, Natalie Gieseking, MSc, vertreten durch die Weber Rechtsanwälte GmbH & Co KG, Wien, wegen 312.706,88 EUR sowie Feststellung (Streitwert 80.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Oktober 2019, GZ 6 R 71/19g-17, mit dem das Urteil des Landesgerichts Steyr vom 29. März 2019, GZ 9 Cg 39/18g-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Benn-Ibler Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Christina Schorer`(person)
- `Donsteinlex AG`(organisation)
- `Natalie Gieseking, MSc`(person)

**Example 1** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_4`)


Logdercon-Digital, Dänemark, 2. Fengart GmbH, Oberer Weinweg 87, 9020 Klagenfurt, Österreich, beide vertreten durch Graf & Pitkowitz Rechtsanwälte GmbH in Wien, gegen die Beklagten 1. LGR Medien GmbH, OVX Finanzen, 2. Analyse Kelunizor AG, Fahnberg 42, 4100 Großamberg, Österreich, Deutschland, beide vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Gesamtstreitwert 69.500 EUR), über den Ordinationsantrag der Klägerinnen den Beschluss gefasst:  Spruch Dem Ordinationsantrag wird stattgegeben.

**False Positives:**

- `Reich-Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Logdercon-Digital`(organisation)
- `Fengart GmbH`(organisation)
- `Oberer Weinweg 87, 9020 Klagenfurt, Österreich`(address)
- `LGR Medien GmbH`(organisation)
- `OVX Finanzen`(organisation)
- `Analyse Kelunizor AG`(organisation)
- `Fahnberg 42, 4100 Großamberg, Österreich`(address)

**Example 2** (doc_id: `deanon_TRAIN/4Ob142_21t`) (sent_id: `deanon_TRAIN/4Ob142_21t_4`)


Matzka sowie Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei Natalie Diestel, vertreten durch Viehböck Breiter Schenk & Nau Rechtsanwälte OG in Mödling, gegen die beklagte Partei Siggelko & Tannenberger Logistik ges.m.b.H., Felix Vogelsanger, vertreten durch Celar Senoner Weber-Wilfert Rechtsanwälte GmbH in Wien, wegen Herausgabe eines Buchauszugs (Streitwert 4.000 EUR) und 41.049,64 EUR sA, über die außerordentliche Revision der klagenden Partei, gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Mai 2021, GZ 5 R 162/20k-66, mit dem das Urteil des Handelsgerichts Wien vom 30. September 2020, GZ 48 Cg 28/19f-59, bestätigt wurde, beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Weber-Wilfert Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Natalie Diestel`(person)
- `Siggelko & Tannenberger Logistik ges.m.b.H.`(organisation)
- `Felix Vogelsanger`(person)

**Example 3** (doc_id: `deanon_TRAIN/5Ob200_24h`) (sent_id: `deanon_TRAIN/5Ob200_24h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Wurzer als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Painsi, Dr. Weixelbraun-Mohr, Dr. Steger und Dr. Pfurtscheller als weitere Richter in der Rechtssache der klagenden Partei Ing. Harald Josepeit, vertreten durch die Wutte-Lang Rechtsanwalts GmbH in Klagenfurt, und der Nebenintervenientin auf Seiten der klagenden Partei MMag.

**False Positives:**

- `Wutte-Lang Rechtsanwalts GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ing. Harald Josepeit`(person)

**Example 4** (doc_id: `deanon_TRAIN/6Ob231_24z`) (sent_id: `deanon_TRAIN/6Ob231_24z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Hofer-Zeni-Rennhofer als Vorsitzende sowie die Hofrätinnen und Hofräte Hon.-Prof. Dr. Faber, Mag. Pertmayr, Dr. Weber und Mag. Nigl LL.M. als weitere Richter in der Rechtssache der klagenden Partei Ing. Egon Jurguttis, vertreten durch Poduschka Partner Anwaltsgesellschaft mbH in Linz, wider die beklagte Partei UnterFinanzen AG, Silvius Haagmans, Deutschland, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 9.600 EUR sA, im Verfahren über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Linz als Berufungsgericht vom 7. Oktober 2024, GZ 6 R 57/24b-31, womit das Urteil des Bezirksgerichts Traun vom 16. Februar 2024, GZ 2 C 198/23z-22, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei vom 9. Dezember 2025 auf Fortsetzung des Verfahrens wird abgewiesen.

**False Positives:**

- `Reich-Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ing. Egon Jurguttis`(person)
- `UnterFinanzen AG`(organisation)
- `Silvius Haagmans`(person)

</details>

---

## `Hyphenated_Organisations`

**F1:** 0.170 | **Precision:** 0.156 | **Recall:** 0.186  

**Format:** `regex`  
**Description:**
Matches hyphenated organisation names with mandatory suffix, handling 'u.' and '+' separators, ensuring the name part is valid.

**Content:**
```
\b([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+u\.\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+|\s+\+\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+|\-[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)?)?)\s+(GmbH|AG|Ges\.m\.b\.H\.|Limited|Holding)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.156 | 0.186 | 0.170 | 409 | 64 | 345 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 64 | 345 | 281 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc22_13m`) (sent_id: `deanon_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Catharina Frielinghausen, Russische Föderation, gegen die verpflichtete Partei Gartcondon-Bildung GmbH, Alan Looß, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

| Predicted | Gold |
|---|---|
| `Gartcondon-Bildung GmbH` | `Gartcondon-Bildung GmbH` |

**Missed by this rule (FN):**

- `Catharina Frielinghausen` (person)
- `Alan Looß` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob105_15m`) (sent_id: `deanon_TRAIN/10Ob105_15m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Alsteinost GmbH, Anna Kisaoglu, Bakk. iur., vertreten durch Dr. Erich Kafka und Dr. Manfred Palkovits, Rechtsanwälte in Wien, gegen die beklagte Partei Ing. Mag. Adam Kratki, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 11. Juni 2015, GZ 39 R 41/15s-29, in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch

| Predicted | Gold |
|---|---|
| `Alsteinost GmbH` | `Alsteinost GmbH` |

**Missed by this rule (FN):**

- `Anna Kisaoglu, Bakk. iur.` (person)
- `Mag. Adam Kratki` (person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob18_25g`) (sent_id: `deanon_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Stanley Plogmeyer, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Tal-Daten GmbH, Karlheinz Hornschuck, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Tal-Daten GmbH` | `Tal-Daten GmbH` |

**Missed by this rule (FN):**

- `Stanley Plogmeyer` (person)
- `Karlheinz Hornschuck` (person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob28_19v`) (sent_id: `deanon_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei HochAnalyse GmbH, Piedro Ehmken, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Ludewigs Handel GmbH, Deborah Lochhuber, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `HochAnalyse GmbH` | `HochAnalyse GmbH` |

**Missed by this rule (FN):**

- `Piedro Ehmken` (person)
- `Ludewigs Handel GmbH` (organisation)
- `Deborah Lochhuber` (person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob2_20x`) (sent_id: `deanon_TRAIN/10Ob2_20x_4`)


Matzka und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Ignaz Jungmichel, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei TalAlvalRobotik AG, Delila Leiteritz, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 25.617,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 29. Oktober 2019, GZ 2 R 151/19t-23, mit dem das Urteil des Landesgerichts Linz vom 21. August 2019, GZ 5 Cg 118/18z-19, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

| Predicted | Gold |
|---|---|
| `TalAlvalRobotik AG` | `TalAlvalRobotik AG` |

**Missed by this rule (FN):**

- `Ignaz Jungmichel` (person)
- `Delila Leiteritz` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc24_22v`) (sent_id: `deanon_TRAIN/10Nc24_22v_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofräte Mag. Ziegelbauer und Mag. Schober als weitere Richter in der Rechtssache der klagenden Partei Yorick Nosczyk, vertreten durch die Skribe Rechtsanwaelte GmbH in Wien, gegen die beklagte Partei Dipl.

**False Positives:**

- `Rechtsanwaelte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Yorick Nosczyk`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei C. Dersudheim Digital GmbH, Taxlbergstraße 247, 8151 Rohrbach, Österreich, vertreten durch Dr. Carl Benkhofer, Rechtsanwalt in Wien, gegen die beklagte Partei Ingolf Grimpe, vertreten durch Greiml & Horwath Rechtsanwaltspartnerschaft in Graz, wegen 5.232 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 14 C 1302/11a des Bezirksgerichts Graz-West in nichtöffentlicher Sitzung, den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Graz-West das Bezirksgericht Fünfhaus bestimmt.

**False Positives:**

- `Digital GmbH` — partial — pred is substring of gold: `Dersudheim Digital GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dersudheim Digital GmbH`(organisation)
- `Taxlbergstraße 247, 8151 Rohrbach, Österreich`(address)
- `Ingolf Grimpe`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob102_18z`) (sent_id: `deanon_TRAIN/10Ob102_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG, Adelheid Lochmaier, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Ursula Antoniadis, vertreten durch Knirsch – Braun – Fellner Rechtsanwälte in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 5. September 2018, GZ 40 R 39/18h-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Digital AG` — partial — pred is substring of gold: `Skrzypczik + Duchscherer Digital AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Skrzypczik + Duchscherer Digital AG`(organisation)
- `Adelheid Lochmaier`(person)
- `Ursula Antoniadis`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob18_25g`) (sent_id: `deanon_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Stanley Plogmeyer, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Tal-Daten GmbH, Karlheinz Hornschuck, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stanley Plogmeyer`(person)
- `Tal-Daten GmbH`(organisation)
- `Karlheinz Hornschuck`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob19_25d`) (sent_id: `deanon_TRAIN/10Ob19_25d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober, Dr. Annerl, Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Ernestine Feifel, vertreten durch die Salburg Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Jean Kandziora, vertreten durch die BEURLE Rechtsanwälte GmbH & Co KG in Linz, wegen Feststellung (Streitwert 5.100 EUR), über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 19. Dezember 2024, GZ 1 R 255/24f-28, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 31. Mai 2024, GZ 15 C 939/23d-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Rechtsanwalts GmbH` — no gold match — likely missing annotation
- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Ernestine Feifel`(person)
- `Jean Kandziora`(person)

</details>

---

## `GmbH_Suffix_Tight`

**F1:** 0.059 | **Precision:** 0.107 | **Recall:** 0.041  

**Format:** `regex`  
**Description:**
Matches entities ending with 'GmbH' with strict boundaries, ensuring the name starts with a Capital letter and excludes titles and common nouns.

**Content:**
```
(?<![A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s])(?<![A-Z])([A-Z][A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df0-9\s\.\-\+&]*?[A-Za-z0-9])\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.107 | 0.041 | 0.059 | 131 | 14 | 117 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 14 | 117 | 331 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob23_15b`) (sent_id: `deanon_TRAIN/10Ob23_15b_4`)


Steintra Solar GmbH, Kospachstraße 35, 3162 Rainfeld, Österreich, vertreten durch Dr. Paul Vavrovsky und Mag. Christian Schrott, Rechtsanwälte in Salzburg, 2. Umwelt Dorfwald ges.m.b.H., Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich, vertreten durch Dr. Katharina Sedlazeck-Gschaider, Rechtsanwältin in Salzburg, wegen 11.921,56 EUR sA und Feststellung (Streitwert 5.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 27. Jänner 2015, GZ 11 R 14/14d-34, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Steintra Solar GmbH` | `Steintra Solar GmbH` |

**Missed by this rule (FN):**

- `Kospachstraße 35, 3162 Rainfeld, Österreich` (address)
- `Umwelt Dorfwald ges.m.b.H.` (organisation)
- `Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich` (address)

**Example 1** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_4`)


Energie Conwald GmbH & Co KG und 2.

| Predicted | Gold |
|---|---|
| `Energie Conwald GmbH` | `Energie Conwald GmbH` |

**Example 2** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_5`)


Metall Monglanz GmbH, beide Johann-Puch-Straße 5, 8741 Reisstraße, Österreich, beide vertreten durch Dr. Michael Schneditz-Bolfras und andere Rechtsanwälte in Gmunden, wegen Bucheinsicht (in eventu Rechnungslegung) und Zahlung (Streitwert: 70.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Teilurteil des Oberlandesgerichts Linz als Berufungsgericht vom 17. Februar 2014, GZ 3 R 13/14y-90, womit das Urteil des Landesgerichts Wels vom 27. November 2013 (in der mit Beschluss vom 12. Dezember 2013 berichtigten Fassung), GZ 2 Cg 78/10p-82 und -84, abgeändert wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Metall Monglanz GmbH` | `Metall Monglanz GmbH` |

**Missed by this rule (FN):**

- `Johann-Puch-Straße 5, 8741 Reisstraße, Österreich` (address)

**Example 3** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_5`)


Maschinenbau Heimfurtcon GmbH, Fretzschner Medien, 2.

| Predicted | Gold |
|---|---|
| `Maschinenbau Heimfurtcon GmbH` | `Maschinenbau Heimfurtcon GmbH` |

**Missed by this rule (FN):**

- `Fretzschner Medien` (organisation)

**Example 4** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_5`)


Klingenbeil Versand GmbH & Co KG, 2.

| Predicted | Gold |
|---|---|
| `Klingenbeil Versand GmbH` | `Klingenbeil Versand GmbH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc22_13m`) (sent_id: `deanon_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Catharina Frielinghausen, Russische Föderation, gegen die verpflichtete Partei Gartcondon-Bildung GmbH, Alan Looß, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

**False Positives:**

- `Bildung GmbH` — partial — pred is substring of gold: `Gartcondon-Bildung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Catharina Frielinghausen`(person)
- `Gartcondon-Bildung GmbH`(organisation)
- `Alan Looß`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei C. Dersudheim Digital GmbH, Taxlbergstraße 247, 8151 Rohrbach, Österreich, vertreten durch Dr. Carl Benkhofer, Rechtsanwalt in Wien, gegen die beklagte Partei Ingolf Grimpe, vertreten durch Greiml & Horwath Rechtsanwaltspartnerschaft in Graz, wegen 5.232 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 14 C 1302/11a des Bezirksgerichts Graz-West in nichtöffentlicher Sitzung, den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Graz-West das Bezirksgericht Fünfhaus bestimmt.

**False Positives:**

- `Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei C. Dersudheim Digital GmbH` — partial — gold is substring of pred: `Dersudheim Digital GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dersudheim Digital GmbH`(organisation)
- `Taxlbergstraße 247, 8151 Rohrbach, Österreich`(address)
- `Ingolf Grimpe`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob18_25g`) (sent_id: `deanon_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Stanley Plogmeyer, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Tal-Daten GmbH, Karlheinz Hornschuck, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Daten GmbH` — partial — pred is substring of gold: `Tal-Daten GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stanley Plogmeyer`(person)
- `Tal-Daten GmbH`(organisation)
- `Karlheinz Hornschuck`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob20_19t`) (sent_id: `deanon_TRAIN/10Ob20_19t_11`)


Der Zweitkläger ist geschäftsführender Alleingesellschafter einer GmbH.

**False Positives:**

- `Der Zweitkläger ist geschäftsführender Alleingesellschafter einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Ob20_19t`) (sent_id: `deanon_TRAIN/10Ob20_19t_38`)


Auftraggeber sei nur die GmbH gewesen.

**False Positives:**

- `Auftraggeber sei nur die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `AG_Suffix_Tight`

**F1:** 0.021 | **Precision:** 0.133 | **Recall:** 0.012  

**Format:** `regex`  
**Description:**
Matches entities ending with 'AG' with strict boundaries, ensuring the name starts with a Capital letter and excludes titles.

**Content:**
```
(?<![A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s])(?<![A-Z])([A-Z][A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df0-9\s\.\-\+&]*?[A-Za-z0-9])\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.133 | 0.012 | 0.021 | 30 | 4 | 26 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 26 | 301 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_6`)


OberTratraSoftware Dienstleistungen AG, Prägrader Weg 43, 8616 Gasen, Österreich, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung (5.000 EUR) und 11.561,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2019, GZ 2 R 140/19z-30, mit dem das Urteil des Landesgerichts Wels vom 22. Juli 2019, GZ 26 Cg 66/18m-26, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

| Predicted | Gold |
|---|---|
| `OberTratraSoftware Dienstleistungen AG` | `OberTratraSoftware Dienstleistungen AG` |

**Missed by this rule (FN):**

- `Prägrader Weg 43, 8616 Gasen, Österreich` (address)

**Example 1** (doc_id: `deanon_TRAIN/2Ob63_11w`) (sent_id: `deanon_TRAIN/2Ob63_11w_4`)


Holz Seewald AG, Kaiserbrunnengasse 6, 5122 Lindach, Österreich, beide vertreten durch Dr. Leopold Hirsch, Rechtsanwalt in Salzburg, wegen 38.967,48 EUR sA und Feststellung (Streitinteresse 20.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 10. Februar 2011, GZ 4 R 206/10g-29, womit das Urteil des Landesgerichts Salzburg vom 17. August 2010, GZ 7 Cg 49/09f-25, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Holz Seewald AG` | `Holz Seewald AG` |

**Missed by this rule (FN):**

- `Kaiserbrunnengasse 6, 5122 Lindach, Österreich` (address)

**Example 2** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_5`)


RheinPharma Services AG, Unterhillinglah 5, 9853 Dornbach, Österreich, vertreten durch Dr. Harald Burmann und andere Rechtsanwälte in Innsbruck, und 3.

| Predicted | Gold |
|---|---|
| `RheinPharma Services AG` | `RheinPharma Services AG` |

**Missed by this rule (FN):**

- `Unterhillinglah 5, 9853 Dornbach, Österreich` (address)

**Example 3** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_6`)


Glöckler Daten AG, Arbeiterstrandbadstraße 492, 8680 Pernreit, Österreich, vertreten durch Dr. Walter Heel, Rechtsanwalt in Innsbruck, wegen 62.404,99 EUR sA und Feststellung (Streitinteresse: 10.000 EUR), über die Revisionen der klagenden, der erstbeklagten und der zweitbeklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Jänner 2011, GZ 4 R 250/10m-85, womit infolge der Berufungen der klagenden, der erstbeklagten und der zweitbeklagten Partei das Urteil des Landesgerichts Innsbruck vom 25. August 2010, GZ 5 Cg 160/08w-74, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Sämtliche Revisionen werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Glöckler Daten AG` | `Glöckler Daten AG` |

**Missed by this rule (FN):**

- `Arbeiterstrandbadstraße 492, 8680 Pernreit, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob33_15y`) (sent_id: `deanon_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Inn Sudconkraft AG, Elisabeth Breitschwerdt, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Mazik Heizung GmbH, Hemma Rahn, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Inn Sudconkraft AG` — partial — gold is substring of pred: `Inn Sudconkraft AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Sudconkraft AG`(organisation)
- `Elisabeth Breitschwerdt`(person)
- `Mazik Heizung GmbH`(organisation)
- `Hemma Rahn`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_7`)


Der Fonds wurde von einer in Deutschland ansässigen AG aufgelegt.

**False Positives:**

- `Der Fonds wurde von einer in Deutschland ansässigen AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Dr. Wurdinger als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Steger, Mag. Wessely-Kristöfel, Dr. Parzmayr und Dr. Pfurtscheller als weitere Richterinnen und Richter in der Rechtssache der klagenden Partei Bundeskammer für Arbeiter und Angestellte, Wien 4, Prinz-Eugen-Straße 20–22, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Alsynwald-Recycling AG, RgR Mag. Dr. Evelyn Steinkröger, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH in Wien, wegen Unterlassung und Urteilsveröffentlichung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. Juli 2024, GZ 2 R 77/24v-15, mit dem das Urteil des Handelsgerichts Wien vom 28. Februar 2024, GZ 57 Cg 36/23d-8, bestätigt wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Recycling AG` — partial — pred is substring of gold: `Alsynwald-Recycling AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alsynwald-Recycling AG`(organisation)
- `RgR Mag. Dr. Evelyn Steinkröger`(person)

**Example 3** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_116`)


Die Nieder Norber AG wird den Kunden in der Mitteilung auf die Änderungen hinweisen und darauf aufmerksam machen, dass sein Stillschweigen nach Ablauf der zwei Monate ab Zugang der Mitteilung durch das Unterlassen eines Widerspruchs in Schriftform als Zustimmung zu den Änderungen gilt.

**False Positives:**

- `Die Nieder Norber AG` — partial — gold is substring of pred: `Nieder Norber AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Norber AG`(organisation)

**Example 4** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_117`)


Außerdem wird die Valwalduni-Handel AG eine Gegenüberstellung über die von der Änderung betroffenen Bestimmungen sowie die vollständige Fassung der neuen Bedingungen auf ihrer Internetseite veröffentlichen und die Gegenüberstellung dem Kunden auf sein Verlangen zur Verfügung stellen;

**False Positives:**

- `Außerdem wird die Valwalduni-Handel AG` — partial — gold is substring of pred: `Valwalduni-Handel AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Valwalduni-Handel AG`(organisation)

</details>

---

## `GmbH_Co_KG_Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches entities ending with 'GmbH & Co KG' to capture the full name, ensuring the name part is captured correctly.

**Content:**
```
\b([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s\.\-\+&]*?[A-Za-z0-9])\s+GmbH\s+&\s+Co\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 22 | 0 | 22 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 22 | 318 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob19_25d`) (sent_id: `deanon_TRAIN/10Ob19_25d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober, Dr. Annerl, Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Ernestine Feifel, vertreten durch die Salburg Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Jean Kandziora, vertreten durch die BEURLE Rechtsanwälte GmbH & Co KG in Linz, wegen Feststellung (Streitwert 5.100 EUR), über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 19. Dezember 2024, GZ 1 R 255/24f-28, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 31. Mai 2024, GZ 15 C 939/23d-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `BEURLE Rechtsanwälte GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ernestine Feifel`(person)
- `Jean Kandziora`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_4`)


Energie Conwald GmbH & Co KG und 2.

**False Positives:**

- `Energie Conwald GmbH & Co KG` — partial — gold is substring of pred: `Energie Conwald GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Energie Conwald GmbH`(organisation)

**Example 2** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_5`)


Text Begründung: Der Kläger erwarb im Jahr 2004 als Verbraucher über Vermittlung eines Wertpapierdienstleistungsunternehmens Kommanditanteile an der Contra GmbH & Co KG im Nominale von 20.000 EUR zuzüglich 1.000 EUR Agio.

**False Positives:**

- `Verbraucher über Vermittlung eines Wertpapierdienstleistungsunternehmens Kommanditanteile an der Contra GmbH & Co KG` — partial — gold is substring of pred: `Contra GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Contra GmbH`(organisation)

**Example 3** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt, aus denen Erträge erzielt werden sollen.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_5`)


Text Begründung: Der Kläger erwarb als Verbraucher im Juni 2003 über Vermittlung eines selbständigen Vermögensberaters Kommanditanteile an der Bestelmeyer+Keßelheim Software GmbH & Co KG im Nominale von 17.000 EUR zuzüglich 850 EUR Agio.

**False Positives:**

- `Vermittlung eines selbständigen Vermögensberaters Kommanditanteile an der Bestelmeyer+Keßelheim Software GmbH & Co KG` — partial — gold is substring of pred: `Bestelmeyer+Keßelheim Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bestelmeyer+Keßelheim Software GmbH`(organisation)

</details>

---

## `Acronym_Industry_Org`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches organisation names starting with an acronym (all caps) followed by a specific industry term or legal suffix, filtering out titles and section references.

**Content:**
```
\b([A-Z]{2,}\s+(?:IT|Vertrieb|Technik|Sicherheit|Immobilien|Verlag|Handel|Versand|GmbH|AG|Limited|KG|GesbR))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 13 | 0 | 13 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 13 | 313 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_13`)


Am 1. 5. 1999 schloss der Kläger als Lizenzgeber mit der Ellbrecht Robotik GesmbH und der ZZMK Technik GesmbH als Lizenznehmerinnen zwei gleichlautende Lizenzverträge.

**False Positives:**

- `ZZMK Technik` — partial — pred is substring of gold: `ZZMK Technik GesmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ellbrecht Robotik GesmbH`(organisation)
- `ZZMK Technik GesmbH`(organisation)

**Example 1** (doc_id: `deanon_TRAIN/10Ob31_16f`) (sent_id: `deanon_TRAIN/10Ob31_16f_3`)


Kopf Der Oberste Gerichtshof als Revisionsgericht hat durch den Hofrat Univ.-Prof. Dr. Neumayr als Vorsitzenden und den Hofrat Dr. Schramm, die Hofrätinnen Dr. Fichtenau und Dr. Tarmann-Prentner sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1060 Wien, Linke Wienzeile 18, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei CESW Technik Services AG, Mike Zachariä, vertreten durch Doralt Seist Csoklich Rechtsanwalts-Partnerschaft in Wien, wegen Unterlassung (30.500 EUR) und Urteilsveröffentlichung (5.500 EUR) über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Jänner 2016, GZ 30 R 35/15k-13, womit das Urteil des Landesgerichts St. Pölten vom 17. Juli 2015, GZ 3 Cg 7/15w-9, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `CESW Technik` — partial — pred is substring of gold: `CESW Technik Services AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `CESW Technik Services AG`(organisation)
- `Mike Zachariä`(person)

**Example 2** (doc_id: `deanon_TRAIN/17Ob17_10i`) (sent_id: `deanon_TRAIN/17Ob17_10i_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Griss als Vorsitzende und durch die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei VRDN Versand GmbH, David Tanzler, vertreten durch Held Berdnik Astner & Partner Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Dr. Livia Zinkel, vertreten durch Dr. Johannes Dörner und Dr. Alexander Singer, Rechtsanwälte in Graz, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 18.000 EUR), infolge „außerordentlichen“ Revisionsrekurses der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 28. September 2010, GZ 1 R 3/10h-23, womit infolge Rekurses der beklagten Partei der Beschluss des Handelsgerichts Wien vom 25. Oktober 2009, GZ 10 Cg 126/09y-10, bestätigt wurde, folgenden Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.

**False Positives:**

- `VRDN Versand` — partial — pred is substring of gold: `VRDN Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VRDN Versand GmbH`(organisation)
- `David Tanzler`(person)
- `Dr. Livia Zinkel`(person)

**Example 3** (doc_id: `deanon_TRAIN/1Ob197_18d`) (sent_id: `deanon_TRAIN/1Ob197_18d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Volze KI GmbH & Co KG, Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich, vertreten durch Dr. Klaus-Dieter Strobach und andere Rechtsanwälte, Grieskirchen, gegen die beklagte Partei Land Oberösterreich, Linz, Landhausplatz 1, vertreten durch Dr. Thomas J. A. Langer, LL.M., Rechtsanwalt in Linz, wegen 475.550,18 EUR sA, über die (außerordentliche) Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2018, GZ 4 R 56/18k-17, mit dem das Urteil des Landesgerichts Wels vom 1. März 2018, GZ 3 Cg 3/16z-13, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `KI GmbH` — partial — pred is substring of gold: `Volze KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Volze KI GmbH`(organisation)
- `Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich`(address)

**Example 4** (doc_id: `deanon_TRAIN/1Ob221_17g`) (sent_id: `deanon_TRAIN/1Ob221_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und Hofrätinnen Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Boothe u. Sandmeier IT GmbH (früher OberTelekom GmbH), Ewaldgasse 28, 4084 Mitterberg, Österreich, vormals vertreten durch Dr. Wolfgang Poleschinski, Rechtsanwalt in Hartberg, gegen die beklagte Partei Yelec Dangelmeier, vertreten durch die Dr. Farhad Paya Rechtsanwalt GmbH, Klagenfurt am Wörthersee, wegen 7.583,60 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 24. August 2017, GZ 1 R 127/17x-69, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 28. März 2017, GZ 16 C 1333/14i-65, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

**False Positives:**

- `IT GmbH` — partial — pred is substring of gold: `Boothe u. Sandmeier IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Boothe u. Sandmeier IT GmbH`(organisation)
- `OberTelekom GmbH`(organisation)
- `Ewaldgasse 28, 4084 Mitterberg, Österreich`(address)
- `Yelec Dangelmeier`(person)

</details>

---

## `Industry_NoSuffix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches organisation names ending in industry terms without a legal suffix, excluding 'Aktiengesellschaft' which is handled separately.

**Content:**
```
(?<![A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s])(?<![A-Z])([A-Z][A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)?)\s+(Maschinenbau|Forschung|Robotik|Verlag|Bank|Institut|Gesellschaft|Handel|Planung|Gastronomie|Elektro|Druck|Pflege|Möbel|Event|Vertrieb|Technologie|Technologien)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 10 | 0 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 10 | 208 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/3Ob223_19v`) (sent_id: `deanon_TRAIN/3Ob223_19v_15`)


[Die Bank] und [die Zessionarin] vereinbaren hiermit ausdrücklich, dass auch das solcherart in ein Festbetragspfandrecht (Verkehrshypothek) mit einem Kapitalbetrag in Höhe von 611.255,25 EUR zuzüglich 7,25 %Zinsen aus 520.326,03 EUR und 9,375 % Zinsen aus 90.929,22 EUR ex lege umgewandelte, ob der Liegenschaft […] einverleibte Höchstbetragspfandrecht zugleich mit den zessionsgegenständlichen Forderungen von [der Bank] auf [die Zessionarin] übertragen wird.“

**False Positives:**

- `Die Bank` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/4Ob9_20g`) (sent_id: `deanon_TRAIN/4Ob9_20g_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Ing. KzlR MedR Brunhild Syndikus, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1) Böhnstedt+Bittlmeier Verlag GmbH, Wien Traalmon Betriebe, und 2) TraunBau AG, Schneeballenweg 6, 4232 Penzendorf, Österreich, beide vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 11.091,23 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 6. November 2019, GZ 2 R 158/19x-27, mit dem das Urteil des Landesgerichts Linz vom 29. August 2019, GZ 36 Cg 14/18h-22, bestätigt wurde, den Beschluss gefasst:  Spruch I. Das Revisionsverfahren zu 4 Ob 9/20g wird bis zur Vorabentscheidung des Gerichtshofs der Europäischen Union über das Vorabentscheidungsersuchen des Obersten Gerichtshofs vom 17.

**False Positives:**

- `Bittlmeier Verlag` — partial — pred is substring of gold: `Böhnstedt+Bittlmeier Verlag GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. KzlR MedR Brunhild Syndikus`(person)
- `Böhnstedt+Bittlmeier Verlag GmbH`(organisation)
- `Wien Traalmon Betriebe`(organisation)
- `TraunBau AG`(organisation)
- `Schneeballenweg 6, 4232 Penzendorf, Österreich`(address)

**Example 2** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_28`)


Die Gesellschaft halte 99,99 % der Anteile an der Bauvereinigung;

**False Positives:**

- `Die Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/6Ob2_12f`) (sent_id: `deanon_TRAIN/6Ob2_12f_5`)


Jakubiak Handel GmbH, Rudolf-Kassner-Gasse 42, 5134 Sengthal, Österreich, 2.

**False Positives:**

- `Jakubiak Handel` — partial — pred is substring of gold: `Jakubiak Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jakubiak Handel GmbH`(organisation)
- `Rudolf-Kassner-Gasse 42, 5134 Sengthal, Österreich`(address)

**Example 4** (doc_id: `deanon_TRAIN/7Ob85_15y`) (sent_id: `deanon_TRAIN/7Ob85_15y_5`)


Schefuss Forschung GmbH, beide Raidenstraße 62, 8354 Aigen, Österreich, vertreten durch Dorda Brugger Jordis Rechtsanwälte GmbH in Wien, wegen 7.523,16 EUR sA, über den Rekurs der erstbeklagten Partei gegen den Beschluss des Handelsgerichts Wien als Berufungsgericht vom 19. Februar 2015, GZ 1 R 6/15a-49, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 29. September 2014, GZ 13 C 134/10s-45, hinsichtlich der erstbeklagten Partei aufgehoben wurde, den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Schefuss Forschung` — partial — pred is substring of gold: `Schefuss Forschung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schefuss Forschung GmbH`(organisation)
- `Raidenstraße 62, 8354 Aigen, Österreich`(address)

</details>

---

## `Compound_Organisations_NoSuffix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches compound organisation names without a legal suffix, excluding court terms and focusing on industry/business terms.

**Content:**
```
(?<![A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s])(?<![A-Z])([A-Z][A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)?)\s+(Vertrieb|Gastronomie|Digital|Event|Gruppe|Medien|Handel|Pharma|Versicherung|Logistik|Möbel|Bau|Analyse|Textil|Stadt|Nord|Drau|Donau|Willus|BTF|IDUS|Raffler|Süd|NordGarten|Kazantzis|Inn|Algart|Aktiengesellschaft)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 10 | 0 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 10 | 345 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_6`)


Die Aktiengesellschaft habe damit geworben, mit den eingezahlten Beträgen Edelmetalle zu marktüblichen Preisen zu erwerben, zu lagern und zu verwalten und habe dem Beklagten in dessen Funktion als Rechtsanwalt und öffentlicher Notar den Auftrag erteilt, jährliche Prüfberichte über den vollständigen Bestand zu erstellen.

**False Positives:**

- `Die Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/1Ob9_22p`) (sent_id: `deanon_TRAIN/1Ob9_22p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. HR Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Parteien 1. Mag. Tosca Xyländer und 2. Mag. Heinrich Vlachojannis, vertreten durch die Koch Jilek Rechtsanwälte Partnerschaft, Bruck an der Mur, gegen die beklagte Partei Grüttemann E‑Commerce Aktiengesellschaft, Friedhof Döbling 165, 8401 Abtissendorf, Österreich, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH, Wien, wegen 40.358,88 EUR sA, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. November 2021, GZ 5 R 163/21h-43, mit dem das Urteil des Handelsgerichts Wien vom 31. August 2021, GZ 55 Cg 60/20i-36, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Commerce Aktiengesellschaft` — partial — pred is substring of gold: `Grüttemann E‑Commerce Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Tosca Xyländer`(person)
- `Mag. Heinrich Vlachojannis`(person)
- `Grüttemann E‑Commerce Aktiengesellschaft`(organisation)
- `Friedhof Döbling 165, 8401 Abtissendorf, Österreich`(address)

**Example 2** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_6`)


JQV Finanzen Gruppe GmbH, Innovationsplatz 79, 9751 Nigglai, Österreich, beide vertreten durch Ruggenthaler Rechtsanwalts KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 62.000 EUR) über den außerordentlichen Revisionsrekurs der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Wien vom 20. September 2010, GZ 30 R 29/10w-9, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `JQV Finanzen Gruppe` — partial — pred is substring of gold: `JQV Finanzen Gruppe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `JQV Finanzen Gruppe GmbH`(organisation)
- `Innovationsplatz 79, 9751 Nigglai, Österreich`(address)

**Example 3** (doc_id: `deanon_TRAIN/4Ob220_09w`) (sent_id: `deanon_TRAIN/4Ob220_09w_9`)


Dementsprechend sah das Rekursgericht nicht die Mitgliedschaft der Mutter bei der Sahaja-Yoga Gruppe als solche als bestimmend für die Obsorgeentscheidung.

**False Positives:**

- `Yoga Gruppe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/4Ob98_20w`) (sent_id: `deanon_TRAIN/4Ob98_20w_7`)


Roedel Textil GmbH, Hasledt 4, 9634 Bodenmühl, Österreich, vertreten durch Mag. Wolfgang Weilguni, Rechtsanwalt in Wien, wegen 1.028.146,05 EUR sA und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der Klägerin gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 21. April 2020, GZ 5 R 158/19w-116, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Roedel Textil` — partial — pred is substring of gold: `Roedel Textil GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Roedel Textil GmbH`(organisation)
- `Hasledt 4, 9634 Bodenmühl, Österreich`(address)

</details>

---

## `Aktiengesellschaft_Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches entities ending with 'Aktiengesellschaft' (full word).

**Content:**
```
(?<![A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s])(?<![A-Z])([A-Z][A-Za-z0-9\s\.\-\+&]*?[A-Za-z0-9])\s+Aktiengesellschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 6 | 0 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 6 | 345 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_5`)


Sie habe im Jahr 2012 mit einer Aktiengesellschaft einen Ansparplan abgeschlossen.

**False Positives:**

- `Sie habe im Jahr 2012 mit einer Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_6`)


Die Aktiengesellschaft habe damit geworben, mit den eingezahlten Beträgen Edelmetalle zu marktüblichen Preisen zu erwerben, zu lagern und zu verwalten und habe dem Beklagten in dessen Funktion als Rechtsanwalt und öffentlicher Notar den Auftrag erteilt, jährliche Prüfberichte über den vollständigen Bestand zu erstellen.

**False Positives:**

- `Die Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/1Ob140_14s`) (sent_id: `deanon_TRAIN/1Ob140_14s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer und Mag. Dr. Wurdinger sowie die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft, Meidlinger Hauptstraße 19, 5233 Erlach, Österreich, vertreten durch die Walch & Zehetbauer Rechtsanwälte OG, Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 344.011,19 EUR und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Juni 2014, GZ 4 R 202/13g-54, mit dem das Teilzwischenurteil des Landesgerichts Feldkirch vom 2. August 2013, GZ 8 Cg 143/11y-46, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

**False Positives:**

- `Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft` — partial — gold is substring of pred: `Tracondon Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tracondon Aktiengesellschaft`(organisation)
- `Meidlinger Hauptstraße 19, 5233 Erlach, Österreich`(address)

**Example 3** (doc_id: `deanon_TRAIN/1Ob9_22p`) (sent_id: `deanon_TRAIN/1Ob9_22p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. HR Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Parteien 1. Mag. Tosca Xyländer und 2. Mag. Heinrich Vlachojannis, vertreten durch die Koch Jilek Rechtsanwälte Partnerschaft, Bruck an der Mur, gegen die beklagte Partei Grüttemann E‑Commerce Aktiengesellschaft, Friedhof Döbling 165, 8401 Abtissendorf, Österreich, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH, Wien, wegen 40.358,88 EUR sA, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. November 2021, GZ 5 R 163/21h-43, mit dem das Urteil des Handelsgerichts Wien vom 31. August 2021, GZ 55 Cg 60/20i-36, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Commerce Aktiengesellschaft` — partial — pred is substring of gold: `Grüttemann E‑Commerce Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Tosca Xyländer`(person)
- `Mag. Heinrich Vlachojannis`(person)
- `Grüttemann E‑Commerce Aktiengesellschaft`(organisation)
- `Friedhof Döbling 165, 8401 Abtissendorf, Österreich`(address)

**Example 4** (doc_id: `deanon_TRAIN/3Ob17_20a`) (sent_id: `deanon_TRAIN/3Ob17_20a_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie die Hofräte Priv.-Doz. Dr. Rassi und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Exekutionssache betreibenden Partei Heizung Werkuni Aktiengesellschaft, P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich, vertreten durch Dr. Roland Grilc ua, Rechtsanwälte in Klagenfurt am Wörthersee, gegen die verpflichtete Partei Dorothea Eiken Bank, Peter Eitenmüller, vertreten durch Diwok Hermann Petsche Rechtsanwälte LLP Co KG in Wien, wegen 12.602.980,92 EUR sA, über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. November 2019, GZ 46 R 293/19g-18, mit dem der Beschluss des Bezirksgerichts Favoriten vom 17. April 2019, GZ 17 E 1298/19z-2, bestätigt wurde, den Beschluss gefasst:  Spruch I. Der Revisionsrekurs wird, soweit er sich gegen die Bestätigung der Exekutionsbewilligung richtet, als jedenfalls unzulässig zurückgewiesen.

**False Positives:**

- `Mohr und Dr. Kodek als weitere Richter in der Exekutionssache betreibenden Partei Heizung Werkuni Aktiengesellschaft` — partial — gold is substring of pred: `Heizung Werkuni Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Heizung Werkuni Aktiengesellschaft`(organisation)
- `P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich`(address)
- `Dorothea Eiken`(person)
- `Peter Eitenmüller`(person)

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `Ges_m_b_H_Suffix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches entities ending with 'Ges.m.b.H.' or 'GmbH & Co KG' (partial match for the main name).

**Content:**
```
(?<![A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s])(?<![A-Z])([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)?)\s+Ges\.m\.b\.H\.
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific_Org_List`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches known specific organisation names from training data that do not fit generic patterns, including hyphenated names and multi-word names.

**Content:**
```
\b(Tal\s+Kelfurtzor\s+Betriebe\s+GmbH|Hamrosi\s+Garten\s+AG|SKSP\s+Immobilien\s+GmbH|Scherg\s+und\s+Kintzli\s+Holz\s+GmbH|Wagenlöhner\s+Versand\s+GmbH|SKRV\s+IT\s+Vertrieb|Medien\s+Gartheim|WestGarten|Maschinenbau\s+Waldtra\s+GmbH|Bersud-Technik\s+GmbH|JUPL\s+Sicherheit\s+GmbH|Mur\s+Dorfheim\s+GmbH|Norglanz|Gruetze\s+Handel\s+Limited|RheinLogistik\s+GmbH)\b
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

## `Hyphenated_Organisations`

**F1:** 0.170 | **Precision:** 0.156 | **Recall:** 0.186  

**Format:** `regex`  
**Description:**
Matches hyphenated organisation names with mandatory suffix, handling 'u.' and '+' separators, ensuring the name part is valid.

**Content:**
```
\b([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+u\.\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+|\s+\+\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+|\-[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)?)?)\s+(GmbH|AG|Ges\.m\.b\.H\.|Limited|Holding)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.156 | 0.186 | 0.170 | 409 | 64 | 345 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 64 | 345 | 281 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc22_13m`) (sent_id: `deanon_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Catharina Frielinghausen, Russische Föderation, gegen die verpflichtete Partei Gartcondon-Bildung GmbH, Alan Looß, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

| Predicted | Gold |
|---|---|
| `Gartcondon-Bildung GmbH` | `Gartcondon-Bildung GmbH` |

**Missed by this rule (FN):**

- `Catharina Frielinghausen` (person)
- `Alan Looß` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob105_15m`) (sent_id: `deanon_TRAIN/10Ob105_15m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Alsteinost GmbH, Anna Kisaoglu, Bakk. iur., vertreten durch Dr. Erich Kafka und Dr. Manfred Palkovits, Rechtsanwälte in Wien, gegen die beklagte Partei Ing. Mag. Adam Kratki, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 11. Juni 2015, GZ 39 R 41/15s-29, in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch

| Predicted | Gold |
|---|---|
| `Alsteinost GmbH` | `Alsteinost GmbH` |

**Missed by this rule (FN):**

- `Anna Kisaoglu, Bakk. iur.` (person)
- `Mag. Adam Kratki` (person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob18_25g`) (sent_id: `deanon_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Stanley Plogmeyer, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Tal-Daten GmbH, Karlheinz Hornschuck, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Tal-Daten GmbH` | `Tal-Daten GmbH` |

**Missed by this rule (FN):**

- `Stanley Plogmeyer` (person)
- `Karlheinz Hornschuck` (person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob28_19v`) (sent_id: `deanon_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei HochAnalyse GmbH, Piedro Ehmken, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Ludewigs Handel GmbH, Deborah Lochhuber, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `HochAnalyse GmbH` | `HochAnalyse GmbH` |

**Missed by this rule (FN):**

- `Piedro Ehmken` (person)
- `Ludewigs Handel GmbH` (organisation)
- `Deborah Lochhuber` (person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob2_20x`) (sent_id: `deanon_TRAIN/10Ob2_20x_4`)


Matzka und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Ignaz Jungmichel, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei TalAlvalRobotik AG, Delila Leiteritz, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 25.617,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 29. Oktober 2019, GZ 2 R 151/19t-23, mit dem das Urteil des Landesgerichts Linz vom 21. August 2019, GZ 5 Cg 118/18z-19, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

| Predicted | Gold |
|---|---|
| `TalAlvalRobotik AG` | `TalAlvalRobotik AG` |

**Missed by this rule (FN):**

- `Ignaz Jungmichel` (person)
- `Delila Leiteritz` (person)

**Example 5** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_5`)


Text Begründung: Der Kläger erwarb im Jahr 2004 als Verbraucher über Vermittlung eines Wertpapierdienstleistungsunternehmens Kommanditanteile an der Contra GmbH & Co KG im Nominale von 20.000 EUR zuzüglich 1.000 EUR Agio.

| Predicted | Gold |
|---|---|
| `Contra GmbH` | `Contra GmbH` |

**Example 6** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_34`)


10. 2019 zu einem völlig gleichgelagerten Fall zu der vom Berufungsgericht angesprochenen Rechtsfrage Stellung genommen hat (beklagte Partei ist hier wie dort die Derber GmbH in Liqu).

| Predicted | Gold |
|---|---|
| `Derber GmbH` | `Derber GmbH` |

**Example 7** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Daniel Wiegand, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei West-Medien Manufaktur GmbH in Liqu, Kanzelweg 32, 4850 Oberthalheim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `West-Medien Manufaktur GmbH` | `West-Medien Manufaktur GmbH` |

**Missed by this rule (FN):**

- `DI Daniel Wiegand` (person)
- `Kanzelweg 32, 4850 Oberthalheim, Österreich` (address)

**Example 8** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_6`)


Text Gründe: Mit dem angefochtenen Urteil wurden Bernhard Beinicke und Norbert Wentzlick von der wider sie erhobenen Anklage, sie hätten am 7. Februar 2009 in Churer Straße 54, 9064 St. Michael ob der Gurk, Österreich /Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der DKZ Solar GesmbH & Co KG, Susanne Schueßler, durch die Vorgabe, die HochForschung GmbH sei eine zahlungsfähige Leasingnehmerin, somit durch Täuschung über Tatsachen, zum Abschluss eines Leasingvertrags über ein Rennfahrzeug für die Dauer von 24 Monaten zu einem monatlichen Entgelt von 10.698,10 Euro, somit zu einer Handlung verleitet, welche die Stadt-Sanitär Services GesmbH & Co KG in einem 50.000 Euro übersteigenden Betrag von insgesamt 235.358,20 Euro am Vermögen schädigte, gemäß § 259 Z 3 StPO (verfehlt auch von der rechtlichen Kategorie; vglLendl, WK-StPO § 259 Rz 1) freigesprochen.

| Predicted | Gold |
|---|---|
| `HochForschung GmbH` | `HochForschung GmbH` |

**Missed by this rule (FN):**

- `Beinicke` (person)
- `Wentzlick` (person)
- `Churer Straße 54, 9064 St. Michael ob der Gurk, Österreich` (address)
- `DKZ Solar GesmbH` (organisation)
- `Schueßler` (person)
- `Stadt-Sanitär Services GesmbH` (organisation)

**Example 9** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_8`)


Nach den wesentlichen Feststellungen (US 3 bis 6) befand sich die See-Maschinenbau GmbH in der zweiten Jahreshälfte 2008 in erheblichen Zahlungsschwierigkeiten.

| Predicted | Gold |
|---|---|
| `See-Maschinenbau GmbH` | `See-Maschinenbau GmbH` |

**Example 10** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__9`)


Text Gründe: Mit unbekämpft in Rechtskraft erwachsenen Urteilen des Bezirksgerichts Spittal an der Drau vom 22. Juni 2017, GZ 5 U 5/17f-26, wurden (I) Andreas Feiereisen des Vergehens der fahrlässigen Tötung nach § 80 Abs 1 StGB schuldig erkannt und hiefür zu einer Geldstrafe verurteilt sowie (II) die Werksynstein-Wind GmbH gemäß § 3 Abs 1 Z 2, Abs 2 VbVG für die vom Schuldspruch (I) erfasste Straftat ihres Entscheidungsträgers verantwortlich erklärt und über diese Gesellschaft eine Verbandsgeldbuße von 70 Tagessätzen zu je 50 Euro verhängt, die unter Bestimmung einer Probezeit von drei Jahren bedingt nachgesehen wurde.

| Predicted | Gold |
|---|---|
| `Werksynstein-Wind GmbH` | `Werksynstein-Wind GmbH` |

**Missed by this rule (FN):**

- `Feiereisen` (person)

**Example 11** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Herbes&Vißers Heizung GmbH, Waldemar Lokämper, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Traun-Luftfahrt GmbH, VetR DDr. Walter Stuehrmann, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

| Predicted | Gold |
|---|---|
| `Traun-Luftfahrt GmbH` | `Traun-Luftfahrt GmbH` |

**Missed by this rule (FN):**

- `Herbes&Vißers Heizung GmbH` (organisation)
- `Waldemar Lokämper` (person)
- `VetR DDr. Walter Stuehrmann` (person)

**Example 12** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_4`)


Republik Österreich, vertreten durch die Finanzprokuratur in Wien, 2. Dr. Ralph Kreidenweiß, und 3. Donau-Automotive GmbH, Ebersreith 11, 8761 Götzendorf, Österreich, beide vertreten durch Dr. Hubert Simon, Rechtsanwalt in Wien, wegen Leistung und Feststellung, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. April 2014, GZ 7 R 21/14h-7, mit dem der Beschluss des Landesgerichts Leoben vom 30. Jänner 2014, GZ 2 Nc 2/14y-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Donau-Automotive GmbH` | `Donau-Automotive GmbH` |

**Missed by this rule (FN):**

- `Dr. Ralph Kreidenweiß` (person)
- `Ebersreith 11, 8761 Götzendorf, Österreich` (address)

**Example 13** (doc_id: `deanon_TRAIN/1Ob16_20i`) (sent_id: `deanon_TRAIN/1Ob16_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Stadt Christina Schorer, vertreten durch die Benn-Ibler Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Donsteinlex AG, Natalie Gieseking, MSc, vertreten durch die Weber Rechtsanwälte GmbH & Co KG, Wien, wegen 312.706,88 EUR sowie Feststellung (Streitwert 80.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Oktober 2019, GZ 6 R 71/19g-17, mit dem das Urteil des Landesgerichts Steyr vom 29. März 2019, GZ 9 Cg 39/18g-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Donsteinlex AG` | `Donsteinlex AG` |

**Missed by this rule (FN):**

- `Christina Schorer` (person)
- `Natalie Gieseking, MSc` (person)

**Example 14** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Dr. Wurdinger als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Steger, Mag. Wessely-Kristöfel, Dr. Parzmayr und Dr. Pfurtscheller als weitere Richterinnen und Richter in der Rechtssache der klagenden Partei Bundeskammer für Arbeiter und Angestellte, Wien 4, Prinz-Eugen-Straße 20–22, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Alsynwald-Recycling AG, RgR Mag. Dr. Evelyn Steinkröger, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH in Wien, wegen Unterlassung und Urteilsveröffentlichung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. Juli 2024, GZ 2 R 77/24v-15, mit dem das Urteil des Handelsgerichts Wien vom 28. Februar 2024, GZ 57 Cg 36/23d-8, bestätigt wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Alsynwald-Recycling AG` | `Alsynwald-Recycling AG` |

**Missed by this rule (FN):**

- `RgR Mag. Dr. Evelyn Steinkröger` (person)

**Example 15** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_117`)


Außerdem wird die Valwalduni-Handel AG eine Gegenüberstellung über die von der Änderung betroffenen Bestimmungen sowie die vollständige Fassung der neuen Bedingungen auf ihrer Internetseite veröffentlichen und die Gegenüberstellung dem Kunden auf sein Verlangen zur Verfügung stellen;

| Predicted | Gold |
|---|---|
| `Valwalduni-Handel AG` | `Valwalduni-Handel AG` |

**Example 16** (doc_id: `deanon_TRAIN/1Ob216_15v`) (sent_id: `deanon_TRAIN/1Ob216_15v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Ashley Meinering, vertreten durch Hon.-Prof. Dr. Michel Walter, Rechtsanwalt in Wien, gegen die beklagte Partei Walddon GmbH, Linn Voegelein, vertreten durch die Schlösser & Partner Rechtsanwälte OG, Graz, wegen 33.930 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 19. August 2015, GZ 13 R 74/15w-55, mit dem das Endurteil des Landesgerichts Korneuburg vom 26. Februar 2015, GZ 3 Cg 15/13h-50, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Walddon GmbH` | `Walddon GmbH` |

**Missed by this rule (FN):**

- `Ashley Meinering` (person)
- `Linn Voegelein` (person)

**Example 17** (doc_id: `deanon_TRAIN/1Ob221_17g`) (sent_id: `deanon_TRAIN/1Ob221_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und Hofrätinnen Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Boothe u. Sandmeier IT GmbH (früher OberTelekom GmbH), Ewaldgasse 28, 4084 Mitterberg, Österreich, vormals vertreten durch Dr. Wolfgang Poleschinski, Rechtsanwalt in Hartberg, gegen die beklagte Partei Yelec Dangelmeier, vertreten durch die Dr. Farhad Paya Rechtsanwalt GmbH, Klagenfurt am Wörthersee, wegen 7.583,60 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 24. August 2017, GZ 1 R 127/17x-69, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 28. März 2017, GZ 16 C 1333/14i-65, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

| Predicted | Gold |
|---|---|
| `OberTelekom GmbH` | `OberTelekom GmbH` |

**Missed by this rule (FN):**

- `Boothe u. Sandmeier IT GmbH` (organisation)
- `Ewaldgasse 28, 4084 Mitterberg, Österreich` (address)
- `Yelec Dangelmeier` (person)

**Example 18** (doc_id: `deanon_TRAIN/1Ob26_20k`) (sent_id: `deanon_TRAIN/1Ob26_20k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Synsynfurt-Finanzen GmbH, Tanja Thielike, vertreten durch die Draxler Rexeis Sozietät von Rechtsanwälten OG, Graz, gegen die beklagte Partei Roberta Reumschüssel, Bakk. phil., vertreten durch Mag. Dr. Alfred Wansch, Rechtsanwalt in Wien, wegen Räumung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtsachen Wien als Berufungsgericht vom 13. November 2019, GZ 39 R 228/19x-70, mit dem das Urteil des Bezirksgerichts Hernals vom 30. April 2019, GZ 4 C 277/16f-64, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Synsynfurt-Finanzen GmbH` | `Synsynfurt-Finanzen GmbH` |

**Missed by this rule (FN):**

- `Tanja Thielike` (person)
- `Roberta Reumschüssel, Bakk. phil.` (person)

**Example 19** (doc_id: `deanon_TRAIN/1Ob82_18t`) (sent_id: `deanon_TRAIN/1Ob82_18t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei MurUmwelt GmbH, Oskar Stelzel, vertreten durch die KRONBERGER Rechtsanwälte Gesellschaft mbH, Wien, gegen die beklagte Partei Brian Hüpsch, vertreten durch Dr. Werner Loos, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 14. März 2018, GZ 38 R 303/17s-48, mit dem das Urteil des Bezirksgerichts Fünfhaus vom 4. August 2017, GZ 22 C 163/16w-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `MurUmwelt GmbH` | `MurUmwelt GmbH` |

**Missed by this rule (FN):**

- `Oskar Stelzel` (person)
- `Brian Hüpsch` (person)

**Example 20** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_11`)


Denn die Beweisthemen (Geschäftsgrundlage der eingangs genannten Vereinbarung vom 11. Dezember 2012 mit der Süd-Immobilien AG; von derselben intendierte Verwertung der Liegenschaften in Draskovichgasse 12, 8240 Friedberg, Österreich durch Zwangsversteigerung ungeachtet eines allfälligen Abverkaufs von Liegenschaften in Steghof 15, 4891 Höhenwarth, Österreich ; Auftrag der Mandanten des Disziplinarbeschuldigten zur Zurückziehung des Antrags auf Aufhebung der Höfeeigenschaft;

| Predicted | Gold |
|---|---|
| `Süd-Immobilien AG` | `Süd-Immobilien AG` |

**Missed by this rule (FN):**

- `Draskovichgasse 12, 8240 Friedberg, Österreich` (address)
- `Steghof 15, 4891 Höhenwarth, Österreich` (address)

**Example 21** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_25`)


Im Herbst 2012 habe sich ein Aufkleber der Ostvallem-Robotik GmbH vom Luftentfeuchter gelöst und ein Typenschild mit dem Baujahr 1986 freigelegt.

| Predicted | Gold |
|---|---|
| `Ostvallem-Robotik GmbH` | `Ostvallem-Robotik GmbH` |

**Example 22** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_78`)


Die Bachtri GmbH hat vor der Auslieferung des neu zusammengesetzten Geräts eine Druckprobe durchgeführt.

| Predicted | Gold |
|---|---|
| `Bachtri GmbH` | `Bachtri GmbH` |

**Example 23** (doc_id: `deanon_TRAIN/3Nc19_22g`) (sent_id: `deanon_TRAIN/3Nc19_22g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek sowie den Hofrat Dr. Stefula als weitere Richter in der Ordinationssache der Antragstellerin Stadt-Robotik GmbH, Hum 65, 9241 Kantnig, Österreich, vertreten durch Specht & Partner Rechtsanwalt GmbH in Wien, gegen die Antragsgegnerin Ing. Verona Obersteiner, Russische Föderation, wegen § 355 EO, über den Ordinationsantrag der Antragstellerin, den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Stadt-Robotik GmbH` | `Stadt-Robotik GmbH` |

**Missed by this rule (FN):**

- `Hum 65, 9241 Kantnig, Österreich` (address)
- `Ing. Verona Obersteiner` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc24_22v`) (sent_id: `deanon_TRAIN/10Nc24_22v_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofräte Mag. Ziegelbauer und Mag. Schober als weitere Richter in der Rechtssache der klagenden Partei Yorick Nosczyk, vertreten durch die Skribe Rechtsanwaelte GmbH in Wien, gegen die beklagte Partei Dipl.

**False Positives:**

- `Rechtsanwaelte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Yorick Nosczyk`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei C. Dersudheim Digital GmbH, Taxlbergstraße 247, 8151 Rohrbach, Österreich, vertreten durch Dr. Carl Benkhofer, Rechtsanwalt in Wien, gegen die beklagte Partei Ingolf Grimpe, vertreten durch Greiml & Horwath Rechtsanwaltspartnerschaft in Graz, wegen 5.232 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 14 C 1302/11a des Bezirksgerichts Graz-West in nichtöffentlicher Sitzung, den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Graz-West das Bezirksgericht Fünfhaus bestimmt.

**False Positives:**

- `Digital GmbH` — partial — pred is substring of gold: `Dersudheim Digital GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dersudheim Digital GmbH`(organisation)
- `Taxlbergstraße 247, 8151 Rohrbach, Österreich`(address)
- `Ingolf Grimpe`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob102_18z`) (sent_id: `deanon_TRAIN/10Ob102_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG, Adelheid Lochmaier, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Ursula Antoniadis, vertreten durch Knirsch – Braun – Fellner Rechtsanwälte in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 5. September 2018, GZ 40 R 39/18h-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Digital AG` — partial — pred is substring of gold: `Skrzypczik + Duchscherer Digital AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Skrzypczik + Duchscherer Digital AG`(organisation)
- `Adelheid Lochmaier`(person)
- `Ursula Antoniadis`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob18_25g`) (sent_id: `deanon_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Stanley Plogmeyer, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Tal-Daten GmbH, Karlheinz Hornschuck, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stanley Plogmeyer`(person)
- `Tal-Daten GmbH`(organisation)
- `Karlheinz Hornschuck`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob19_25d`) (sent_id: `deanon_TRAIN/10Ob19_25d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober, Dr. Annerl, Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Ernestine Feifel, vertreten durch die Salburg Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Jean Kandziora, vertreten durch die BEURLE Rechtsanwälte GmbH & Co KG in Linz, wegen Feststellung (Streitwert 5.100 EUR), über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 19. Dezember 2024, GZ 1 R 255/24f-28, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 31. Mai 2024, GZ 15 C 939/23d-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Rechtsanwalts GmbH` — no gold match — likely missing annotation
- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Ernestine Feifel`(person)
- `Jean Kandziora`(person)

**Example 5** (doc_id: `deanon_TRAIN/10Ob22_22s`) (sent_id: `deanon_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludger Radek, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Solar Fenwerk Limited, Amanda Ziergöbel Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Fenwerk Limited` — partial — pred is substring of gold: `Solar Fenwerk Limited`
- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Ludger Radek`(person)
- `Solar Fenwerk Limited`(organisation)
- `Amanda Ziergöbel`(person)

**Example 6** (doc_id: `deanon_TRAIN/10Ob23_15b`) (sent_id: `deanon_TRAIN/10Ob23_15b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Bruno Altevogt, BA MBA, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, gegen die beklagten Parteien 1.

**False Positives:**

- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bruno Altevogt, BA MBA`(person)

**Example 7** (doc_id: `deanon_TRAIN/10Ob23_15b`) (sent_id: `deanon_TRAIN/10Ob23_15b_4`)


Steintra Solar GmbH, Kospachstraße 35, 3162 Rainfeld, Österreich, vertreten durch Dr. Paul Vavrovsky und Mag. Christian Schrott, Rechtsanwälte in Salzburg, 2. Umwelt Dorfwald ges.m.b.H., Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich, vertreten durch Dr. Katharina Sedlazeck-Gschaider, Rechtsanwältin in Salzburg, wegen 11.921,56 EUR sA und Feststellung (Streitwert 5.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 27. Jänner 2015, GZ 11 R 14/14d-34, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Solar GmbH` — partial — pred is substring of gold: `Steintra Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Steintra Solar GmbH`(organisation)
- `Kospachstraße 35, 3162 Rainfeld, Österreich`(address)
- `Umwelt Dorfwald ges.m.b.H.`(organisation)
- `Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich`(address)

**Example 8** (doc_id: `deanon_TRAIN/10Ob23_18g`) (sent_id: `deanon_TRAIN/10Ob23_18g_4`)


Severin Simaitis, geboren 20. November 2002, 2. 8. Juli 1967, geboren 17. November 2004, und 3. Nepomuk Sprinzl, geboren 11. September 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Miklos Stiening, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Rechtsanwalts GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Severin Simaitis`(person)
- `20. November`(date)
- `8. Juli 1967`(date)
- `17. November`(date)
- `Nepomuk Sprinzl`(person)
- `11. September`(date)
- `Mag. Miklos Stiening`(person)

**Example 9** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_4`)


Energie Conwald GmbH & Co KG und 2.

**False Positives:**

- `Conwald GmbH` — partial — pred is substring of gold: `Energie Conwald GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Energie Conwald GmbH`(organisation)

**Example 10** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_5`)


Metall Monglanz GmbH, beide Johann-Puch-Straße 5, 8741 Reisstraße, Österreich, beide vertreten durch Dr. Michael Schneditz-Bolfras und andere Rechtsanwälte in Gmunden, wegen Bucheinsicht (in eventu Rechnungslegung) und Zahlung (Streitwert: 70.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Teilurteil des Oberlandesgerichts Linz als Berufungsgericht vom 17. Februar 2014, GZ 3 R 13/14y-90, womit das Urteil des Landesgerichts Wels vom 27. November 2013 (in der mit Beschluss vom 12. Dezember 2013 berichtigten Fassung), GZ 2 Cg 78/10p-82 und -84, abgeändert wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Monglanz GmbH` — partial — pred is substring of gold: `Metall Monglanz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Metall Monglanz GmbH`(organisation)
- `Johann-Puch-Straße 5, 8741 Reisstraße, Österreich`(address)

**Example 11** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_15`)


Mit Vertrag vom 28. 3. 2007 wurden die Lizenznehmerinnen nach Firmenänderung als übertragende Gesellschaften mit der Mittel Bachnexlem Betriebe GmbH als übernehmende Gesellschaft verschmolzen, die am 26.

**False Positives:**

- `Betriebe GmbH` — partial — pred is substring of gold: `Mittel Bachnexlem Betriebe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mittel Bachnexlem Betriebe GmbH`(organisation)

**Example 12** (doc_id: `deanon_TRAIN/10Ob28_17s`) (sent_id: `deanon_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Jaroslaw Mlynarik, geboren am 1. Juli 2009, wegen Kontaktrechts des Vaters Dr. Eckard Tschernig, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Bettina Makswietat, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

**False Positives:**

- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jaroslaw Mlynarik`(person)
- `1. Juli 2009`(date)
- `Dr. Eckard Tschernig`(person)
- `Dr. Bettina Makswietat`(person)

**Example 13** (doc_id: `deanon_TRAIN/10Ob28_19v`) (sent_id: `deanon_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei HochAnalyse GmbH, Piedro Ehmken, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Ludewigs Handel GmbH, Deborah Lochhuber, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Handel GmbH` — partial — pred is substring of gold: `Ludewigs Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `HochAnalyse GmbH`(organisation)
- `Piedro Ehmken`(person)
- `Ludewigs Handel GmbH`(organisation)
- `Deborah Lochhuber`(person)

**Example 14** (doc_id: `deanon_TRAIN/10Ob2_20x`) (sent_id: `deanon_TRAIN/10Ob2_20x_4`)


Matzka und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Ignaz Jungmichel, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei TalAlvalRobotik AG, Delila Leiteritz, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 25.617,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 29. Oktober 2019, GZ 2 R 151/19t-23, mit dem das Urteil des Landesgerichts Linz vom 21. August 2019, GZ 5 Cg 118/18z-19, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

**False Positives:**

- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ignaz Jungmichel`(person)
- `TalAlvalRobotik AG`(organisation)
- `Delila Leiteritz`(person)

**Example 15** (doc_id: `deanon_TRAIN/10Ob2_22z`) (sent_id: `deanon_TRAIN/10Ob2_22z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Calvin Amorelli, vertreten durch Dr. Martin Hembach, Rechtsanwalt in Wiener Neustadt, gegen die beklagte Partei Strathewerd u. Niemetz Metall GmbH, Dolores Chatzakis, vertreten durch Mag. Martin Trapichler, Rechtsanwalt in Wien, wegen 13.639,20 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 25. Oktober 2021, GZ 18 R 67/21p-16, mit dem das Urteil des Bezirksgerichts Wiener Neustadt vom 7. Juni 2021, GZ 7 C 117/21b-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Metall GmbH` — partial — pred is substring of gold: `Strathewerd u. Niemetz Metall GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Calvin Amorelli`(person)
- `Strathewerd u. Niemetz Metall GmbH`(organisation)
- `Dolores Chatzakis`(person)

**Example 16** (doc_id: `deanon_TRAIN/10Ob31_16f`) (sent_id: `deanon_TRAIN/10Ob31_16f_3`)


Kopf Der Oberste Gerichtshof als Revisionsgericht hat durch den Hofrat Univ.-Prof. Dr. Neumayr als Vorsitzenden und den Hofrat Dr. Schramm, die Hofrätinnen Dr. Fichtenau und Dr. Tarmann-Prentner sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1060 Wien, Linke Wienzeile 18, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei CESW Technik Services AG, Mike Zachariä, vertreten durch Doralt Seist Csoklich Rechtsanwalts-Partnerschaft in Wien, wegen Unterlassung (30.500 EUR) und Urteilsveröffentlichung (5.500 EUR) über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Jänner 2016, GZ 30 R 35/15k-13, womit das Urteil des Landesgerichts St. Pölten vom 17. Juli 2015, GZ 3 Cg 7/15w-9, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Services AG` — partial — pred is substring of gold: `CESW Technik Services AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `CESW Technik Services AG`(organisation)
- `Mike Zachariä`(person)

**Example 17** (doc_id: `deanon_TRAIN/10Ob33_15y`) (sent_id: `deanon_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Inn Sudconkraft AG, Elisabeth Breitschwerdt, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Mazik Heizung GmbH, Hemma Rahn, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Sudconkraft AG` — partial — pred is substring of gold: `Inn Sudconkraft AG`
- `Heizung GmbH` — partial — pred is substring of gold: `Mazik Heizung GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Sudconkraft AG`(organisation)
- `Elisabeth Breitschwerdt`(person)
- `Mazik Heizung GmbH`(organisation)
- `Hemma Rahn`(person)

**Example 18** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Dr. Marlon Richel, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Freimut & Assenov Sicherheit GmbH in Liqu, Spazgasse 41, 8524 Greim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 31.596,47 EUR und Feststellung (6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 18. Juni 2019, GZ 129 R 50/19z-21, mit dem das Urteil des Handelsgerichts Wien vom 28. März 2019, GZ 54 Cg 71/18x-17, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Rechtsanwalt GmbH` — no gold match — likely missing annotation
- `Sicherheit GmbH` — partial — pred is substring of gold: `Freimut & Assenov Sicherheit GmbH`
- `Rechtsanwalts GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 2

**Gold Entities:**

- `Dr. Marlon Richel`(person)
- `Freimut & Assenov Sicherheit GmbH`(organisation)
- `Spazgasse 41, 8524 Greim, Österreich`(address)

**Example 19** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Daniel Wiegand, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei West-Medien Manufaktur GmbH in Liqu, Kanzelweg 32, 4850 Oberthalheim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Rechtsanwalt GmbH` — no gold match — likely missing annotation
- `Rechtsanwalts GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `DI Daniel Wiegand`(person)
- `West-Medien Manufaktur GmbH`(organisation)
- `Kanzelweg 32, 4850 Oberthalheim, Österreich`(address)

**Example 20** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_5`)


Text Begründung: Der Kläger erwarb als Verbraucher im Juni 2003 über Vermittlung eines selbständigen Vermögensberaters Kommanditanteile an der Bestelmeyer+Keßelheim Software GmbH & Co KG im Nominale von 17.000 EUR zuzüglich 850 EUR Agio.

**False Positives:**

- `Software GmbH` — partial — pred is substring of gold: `Bestelmeyer+Keßelheim Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bestelmeyer+Keßelheim Software GmbH`(organisation)

**Example 21** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_5`)


Maschinenbau Heimfurtcon GmbH, Fretzschner Medien, 2.

**False Positives:**

- `Heimfurtcon GmbH` — partial — pred is substring of gold: `Maschinenbau Heimfurtcon GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maschinenbau Heimfurtcon GmbH`(organisation)
- `Fretzschner Medien`(organisation)

**Example 22** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_6`)


OberTratraSoftware Dienstleistungen AG, Prägrader Weg 43, 8616 Gasen, Österreich, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung (5.000 EUR) und 11.561,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2019, GZ 2 R 140/19z-30, mit dem das Urteil des Landesgerichts Wels vom 22. Juli 2019, GZ 26 Cg 66/18m-26, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

**False Positives:**

- `Dienstleistungen AG` — partial — pred is substring of gold: `OberTratraSoftware Dienstleistungen AG`
- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `OberTratraSoftware Dienstleistungen AG`(organisation)
- `Prägrader Weg 43, 8616 Gasen, Österreich`(address)

**Example 23** (doc_id: `deanon_TRAIN/10ObS7_10t`) (sent_id: `deanon_TRAIN/10ObS7_10t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Schinko als Vorsitzenden, die Hofräte Dr. Fellinger und Hon.-Prof. Dr. Neumayr sowie die fachkundigen Laienrichter Dr. Thomas Neumann (aus dem Kreis der Arbeitgeber) und KR Mag. Michaela Haydter (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Wilhelm Peter Perlt, vertreten durch Wukovits & Eppelein Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Pensionsversicherungsanstalt, Friedrich Hillegeist-Straße 1, 1021 Wien, wegen Feststellung der Versicherungszeiten, infolge außerordentlicher Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 19. Dezember 2008, GZ 9 Rs 160/08b-19, den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Perlt`(person)

**Example 24** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_9`)


Am 7. Februar 2009 schlossen die Angeklagten namens der genannten Gesellschaft mit der von Susanna Szczech vertretenen Inn Triconal Holding GesmbH & Co KG einen Leasingvertrag über einen Rennwagen samt Ersatzteilpaket.

**False Positives:**

- `Triconal Holding` — partial — pred is substring of gold: `Inn Triconal Holding GesmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Szczech`(person)
- `Inn Triconal Holding GesmbH`(organisation)

**Example 25** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_11`)


„Nachdem“ es für die Wilken E‑Commerce GmbH notwendig geworden war, für die Aufnahme des Rennbetriebs 35.000 Euro in das Fahrzeug zu investieren, konnte aufgrund dessen schlechten Zustands kein Rennen erfolgreich beendet werden.

**False Positives:**

- `Commerce GmbH` — partial — pred is substring of gold: `Wilken E‑Commerce GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wilken E‑Commerce GmbH`(organisation)

**Example 26** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_23`)


Auch diesen Aspekt nimmt die Staatsanwaltschaft in der Rechtsrüge (Z 9 lit a) ausreichend in den Blick, indem sie auf - in Richtung der Erfüllung auch der objektiven Tatbestandsmerkmale der §§ 146, 147 Abs 3 StGB weisende - Beweisergebnisse zum vorliegenden Vertragsab-schluss trotz mangelnder finanzieller Ausstattung und Absicherung der Inn Dorfdersee GmbH hinweist.

**False Positives:**

- `Dorfdersee GmbH` — partial — pred is substring of gold: `Inn Dorfdersee GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Dorfdersee GmbH`(organisation)

**Example 27** (doc_id: `deanon_TRAIN/12Ns34_18y`) (sent_id: `deanon_TRAIN/12Ns34_18y_4`)


2005 den Beschluss gefasst:  Spruch Vizepräsidentin des Obersten Gerichtshofs Mag. Marek ist von der Entscheidung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Dr. Tilo Bräutigam sowie über die Berufungen der Staatsanwaltschaft und der Privatbeteiligten Hoch Seefurtlem GmbH gegen das Urteil des Landesgerichts Klagenfurt als Schöffengericht vom 30. Juni 2017, GZ 72 Hv 8/17g-80, ausgeschlossen.

**False Positives:**

- `Seefurtlem GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__3`)


Kopf Der Oberste Gerichtshof hat am 6. Dezember 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Kirchbacher als Vorsitzenden sowie die Hofräte und die Hofrätinnen des Obersten Gerichtshofs Dr. Lässig, Mag. Michel, Dr. Oberressl und Dr. Brenner in Gegenwart des Richteramtsanwärters Mag. Schuber als Schriftführer in der Verbandsverantwortlichkeitssache der Kränzl Pflege GmbH wegen des Vergehens der fahrlässigen Tötung nach § 80 Abs 1 StGB, AZ 5 U 5/17f des Bezirksgerichts Spittal an der Drau, über die von der Generalprokuratur gegen das Urteil dieses Gerichts vom 22. Juni 2017, GZ 5 U 5/17f-26, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Leitner, zu Recht erkannt:  Spruch

**False Positives:**

- `Pflege GmbH` — partial — pred is substring of gold: `Kränzl Pflege GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kränzl Pflege GmbH`(organisation)

**Example 29** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__17`)


Indem das Bezirksgericht über die Jusepeitis&Niemöller Bildung GmbH eine (das Höchstmaß von somit 55 Tagessätzen übersteigende) Verbandsgeldbuße von 70 Tagessätzen verhängte, verletzte es § 4 Abs 3 VbVG).

**False Positives:**

- `Bildung GmbH` — partial — pred is substring of gold: `Jusepeitis&Niemöller Bildung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jusepeitis&Niemöller Bildung GmbH`(organisation)

**Example 30** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__26`)


Indem das vorliegende Urteil in Ansehung der Hup & Glossner Solar GmbH in gekürzter Form (§ 270 Abs 4 StPO) ausgefertigt wurde, verletzt es das Gesetz in § 22 Abs 5 VbVG iVm § 270 Abs 2 Z 5 StPO.“

**False Positives:**

- `Solar GmbH` — partial — pred is substring of gold: `Hup & Glossner Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hup & Glossner Solar GmbH`(organisation)

**Example 31** (doc_id: `deanon_TRAIN/15Os161_11g`) (sent_id: `deanon_TRAIN/15Os161_11g_9`)


Danach hat er - ebenso wie Bramsiepe - in Wien und im Burgenland fremde bewegliche Sachen in einem 3.000 Euro übersteigenden Wert Nachgenannten mit dem Vorsatz weggenommen, sich durch deren Zueignung unrechtmäßig zu bereichern, wobei er die schweren Diebstähle - zu Punkt II./ auch durch Einbruch - in der Absicht beging, sich durch deren wiederkehrende Begehung eine fortlaufende Einnahme zu verschaffen, und zwar I./ zwischen 30. April und 1. Mai 2011 Verfügungsberechtigten der Flotow Gastronomie GmbH eine Betonpumpe im Wert von 20.000 Euro;

**False Positives:**

- `Gastronomie GmbH` — partial — pred is substring of gold: `Flotow Gastronomie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bramsiepe`(person)
- `Flotow Gastronomie GmbH`(organisation)

**Example 32** (doc_id: `deanon_TRAIN/15Os161_11g`) (sent_id: `deanon_TRAIN/15Os161_11g_12`)


IV./ zwischen 1. und 30. April 2011 Verfügungsberechtigten der Rhein Steinglanz GmbH einen Kompressor im Wert von zirka 10.000 Euro.

**False Positives:**

- `Steinglanz GmbH` — partial — pred is substring of gold: `Rhein Steinglanz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Rhein Steinglanz GmbH`(organisation)

**Example 33** (doc_id: `deanon_TRAIN/15Os161_11g`) (sent_id: `deanon_TRAIN/15Os161_11g_14`)


Rechtliche Beurteilung Die Mängelrüge (Z 5 zweiter Fall) vermisst zu I./ eine Erörterung der eine Täterschaft des Beschwerdeführers in Abrede stellenden Verantwortungen der beiden Angeklagten, zu IV./ wiederum eine Auseinandersetzung einerseits mit der Aussage des Angeklagten Gisbert Springler, dass die in Serbien sichergestellte Maschine nicht mit jener der Trübe&Conz Landwirtschaft GmbH ident sei, andererseits mit der seine Tatbeteiligung leugnenden Verantwortung des Angeklagten Buchhalla.

**False Positives:**

- `Landwirtschaft GmbH` — partial — pred is substring of gold: `Trübe&Conz Landwirtschaft GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gisbert Springler`(person)
- `Trübe&Conz Landwirtschaft GmbH`(organisation)
- `Buchhalla`(person)

**Example 34** (doc_id: `deanon_TRAIN/17Ob17_10i`) (sent_id: `deanon_TRAIN/17Ob17_10i_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Griss als Vorsitzende und durch die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei VRDN Versand GmbH, David Tanzler, vertreten durch Held Berdnik Astner & Partner Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Dr. Livia Zinkel, vertreten durch Dr. Johannes Dörner und Dr. Alexander Singer, Rechtsanwälte in Graz, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 18.000 EUR), infolge „außerordentlichen“ Revisionsrekurses der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 28. September 2010, GZ 1 R 3/10h-23, womit infolge Rekurses der beklagten Partei der Beschluss des Handelsgerichts Wien vom 25. Oktober 2009, GZ 10 Cg 126/09y-10, bestätigt wurde, folgenden Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.

**False Positives:**

- `Versand GmbH` — partial — pred is substring of gold: `VRDN Versand GmbH`
- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `VRDN Versand GmbH`(organisation)
- `David Tanzler`(person)
- `Dr. Livia Zinkel`(person)

**Example 35** (doc_id: `deanon_TRAIN/18OCg12_19t`) (sent_id: `deanon_TRAIN/18OCg12_19t_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Veith und die Hofräte Dr. Höllwerth, Priv.-Doz. Dr. Rassi und Mag. Painsi als weitere Richter in der Schiedsrechtssache der klagenden Partei Trabruckgart Holding GmbH, Jean Nellner, vertreten durch die SRG Stock Rafaseder Gruszkiewicz Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Lydia Astorre, Bulgarien, wegen Aufhebung eines Schiedsspruchs (Streitwert 257.397,45 EUR), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Klage wird als nicht zur Bestimmung einer Tagsatzung zur mündlichen Verhandlung geeignet zurückgewiesen.

**False Positives:**

- `Trabruckgart Holding` — partial — pred is substring of gold: `Trabruckgart Holding GmbH`
- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Trabruckgart Holding GmbH`(organisation)
- `Jean Nellner`(person)
- `Lydia Astorre`(person)

**Example 36** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Herbes&Vißers Heizung GmbH, Waldemar Lokämper, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Traun-Luftfahrt GmbH, VetR DDr. Walter Stuehrmann, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

**False Positives:**

- `Heizung GmbH` — partial — pred is substring of gold: `Herbes&Vißers Heizung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Herbes&Vißers Heizung GmbH`(organisation)
- `Waldemar Lokämper`(person)
- `Traun-Luftfahrt GmbH`(organisation)
- `VetR DDr. Walter Stuehrmann`(person)

**Example 37** (doc_id: `deanon_TRAIN/1Ob105_18z`) (sent_id: `deanon_TRAIN/1Ob105_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Familienrechtssache des Antragstellers Ilona Hoerhold, vertreten durch die Korp Rechtsanwalts GmbH, Andorf, gegen die Antragsgegnerin Farina Prokofyev, vertreten durch die Puttinger Vogl Rechtsanwälte GmbH, Ried im Innkreis, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts Wels als Rekursgericht vom 2. Mai 2018, GZ 21 R 50/18d-32, mit dem der Rekurs des Antragstellers gegen den Beschluss des Bezirksgerichts Grieskirchen vom 8. Jänner 2018, GZ 8 Fam 37/16i-26, zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

**False Positives:**

- `Rechtsanwalts GmbH` — no gold match — likely missing annotation
- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Ilona Hoerhold`(person)
- `Farina Prokofyev`(person)

**Example 38** (doc_id: `deanon_TRAIN/1Ob106_20z`) (sent_id: `deanon_TRAIN/1Ob106_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Kodek, Mag. Wurzer, Mag. Dr. Wurdinger und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei IGK Bau Consulting AG, Ariadne Seebalt, vertreten durch Dr. Manfred Angerer und andere Rechtsanwälte in Klagenfurt am Wörthersee, gegen die beklagte Partei DI Roxana Pöll, vertreten durch Mag. Claudia Egarter, Rechtsanwältin in Klagenfurt am Wörthersee, wegen 5.457.559,15 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 28. Februar 2020, GZ 2 R 9/20s-150, mit dem das Urteil des Landesgerichts Klagenfurt vom 20. Februar 2017, GZ 21 Cg 24/13h-102, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Consulting AG` — partial — pred is substring of gold: `IGK Bau Consulting AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `IGK Bau Consulting AG`(organisation)
- `Ariadne Seebalt`(person)
- `DI Roxana Pöll`(person)

**Example 39** (doc_id: `deanon_TRAIN/1Ob139_18z`) (sent_id: `deanon_TRAIN/1Ob139_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Angelina Töpker Inc., Ronja Straßgschwandtner, vertreten durch Mag. Ralph Kilches, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Lilia Anderßon, als Insolvenzverwalter im Insolvenzverfahren über das Vermögen der Vanek und Eloy Analyse GmbH, Kanischaberg 21, 4742 Kornrödt, Österreich, vertreten durch die Haslinger/Nagele & Partner Rechtsanwälte GmbH, Linz, wegen Feststellung einer Insolvenzforderung (Streitwert 447.352,05 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 28. Juni 2018, GZ 1 R 83/18h-8, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Analyse GmbH` — partial — pred is substring of gold: `Vanek und Eloy Analyse GmbH`
- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Angelina Töpker`(person)
- `Ronja Straßgschwandtner`(person)
- `Mag. Lilia Anderßon`(person)
- `Vanek und Eloy Analyse GmbH`(organisation)
- `Kanischaberg 21, 4742 Kornrödt, Österreich`(address)

**Example 40** (doc_id: `deanon_TRAIN/1Ob152_24w`) (sent_id: `deanon_TRAIN/1Ob152_24w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Musger als Vorsitzenden sowie die Hofrätin und die Hofräte Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei VetR Volkmar Acar KG, FN FN823951l, vertreten durch Dr. Eva-Maria Bachmann-Lang, Dr. Christian Bachmann, Rechtsanwälte in Wien, gegen die beklagte Partei „ Nemtschok Touristik “ Wilnorlex Werke gmbH, FN FN545761v, vertreten durch die GRAF ISOLA Rechtsanwälte GmbH in Wien, wegen 51.843,91 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 3. Juli 2024, GZ 1 R 17/24p-39, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `VetR Volkmar Acar`(person)
- `FN823951l`(business_register_number)
- `Nemtschok Touristik`(organisation)
- `Wilnorlex Werke gmbH`(organisation)
- `FN545761v`(business_register_number)

**Example 41** (doc_id: `deanon_TRAIN/1Ob16_20i`) (sent_id: `deanon_TRAIN/1Ob16_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Stadt Christina Schorer, vertreten durch die Benn-Ibler Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Donsteinlex AG, Natalie Gieseking, MSc, vertreten durch die Weber Rechtsanwälte GmbH & Co KG, Wien, wegen 312.706,88 EUR sowie Feststellung (Streitwert 80.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Oktober 2019, GZ 6 R 71/19g-17, mit dem das Urteil des Landesgerichts Steyr vom 29. März 2019, GZ 9 Cg 39/18g-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Benn-Ibler Rechtsanwälte GmbH` — no gold match — likely missing annotation
- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Christina Schorer`(person)
- `Donsteinlex AG`(organisation)
- `Natalie Gieseking, MSc`(person)

**Example 42** (doc_id: `deanon_TRAIN/1Ob171_22m`) (sent_id: `deanon_TRAIN/1Ob171_22m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Musger als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Leonie Dommke, vertreten durch Mag. Klaus Mayer, Rechtsanwalt in Premstätten, gegen die beklagte Partei Grashuber+Kovatchev Immobilien Limited, Elisabeth Hallmanns, vertreten durch Dr. Fabian Maschke, Rechtsanwalt in Wien, wegen 36.070 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 3. August 2022, GZ 4 R 98/22x-24, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Immobilien Limited` — partial — pred is substring of gold: `Grashuber+Kovatchev Immobilien Limited`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Leonie Dommke`(person)
- `Grashuber+Kovatchev Immobilien Limited`(organisation)
- `Elisabeth Hallmanns`(person)

**Example 43** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Dr. Wurdinger als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Steger, Mag. Wessely-Kristöfel, Dr. Parzmayr und Dr. Pfurtscheller als weitere Richterinnen und Richter in der Rechtssache der klagenden Partei Bundeskammer für Arbeiter und Angestellte, Wien 4, Prinz-Eugen-Straße 20–22, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Alsynwald-Recycling AG, RgR Mag. Dr. Evelyn Steinkröger, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH in Wien, wegen Unterlassung und Urteilsveröffentlichung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. Juli 2024, GZ 2 R 77/24v-15, mit dem das Urteil des Handelsgerichts Wien vom 28. Februar 2024, GZ 57 Cg 36/23d-8, bestätigt wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Alsynwald-Recycling AG`(organisation)
- `RgR Mag. Dr. Evelyn Steinkröger`(person)

**Example 44** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_115`)


3. Klausel 5: „2. Änderungen Z 2. (1) Änderungen dieser zwischen dem Kunden und dem Kreditinstitut vereinbarten Bedingungen gelten nach Ablauf von zwei Monaten ab Zugang der Mitteilung der angebotenen Änderungen an den Kunden als vereinbart, sofern bis dahin kein schriftlicher Widerspruch des Kunden bei der DFA Planung AG einlangt.

**False Positives:**

- `Planung AG` — partial — pred is substring of gold: `DFA Planung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DFA Planung AG`(organisation)

**Example 45** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_116`)


Die Nieder Norber AG wird den Kunden in der Mitteilung auf die Änderungen hinweisen und darauf aufmerksam machen, dass sein Stillschweigen nach Ablauf der zwei Monate ab Zugang der Mitteilung durch das Unterlassen eines Widerspruchs in Schriftform als Zustimmung zu den Änderungen gilt.

**False Positives:**

- `Norber AG` — partial — pred is substring of gold: `Nieder Norber AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Norber AG`(organisation)

**Example 46** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_118`)


auch darauf wird die Landwerlin&Plumke Versand AG in derMitteilung hinweisen.

**False Positives:**

- `Versand AG` — partial — pred is substring of gold: `Landwerlin&Plumke Versand AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landwerlin&Plumke Versand AG`(organisation)

**Example 47** (doc_id: `deanon_TRAIN/1Ob178_19m`) (sent_id: `deanon_TRAIN/1Ob178_19m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Manfred Dietmayr, vertreten durch die Korn und Gärtner Rechtsanwälte OG, Salzburg, gegen die beklagte Partei Sakura Assmacher, MSc, vertreten durch die Ferner Hornung & Partner Rechtsanwälte GmbH, Salzburg, wegen Wiederaufnahme des Verfahrens AZ 17 C 1538/16p des Bezirksgerichts Salzburg, über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 12. Juni 2019, GZ 22 R 163/19b-7, mit dem der Beschluss des Bezirksgerichts Salzburg vom 25. Jänner 2019, GZ 17 C 80/19f-2, mit einer Maßgabe bestätigt wurde, den Beschluss gefasst:  Spruch Dem außerordentlichen Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Manfred Dietmayr`(person)
- `Sakura Assmacher, MSc`(person)

**Example 48** (doc_id: `deanon_TRAIN/1Ob187_14b`) (sent_id: `deanon_TRAIN/1Ob187_14b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der außerstreitigen Rechtssache der Antragstellerin Juliana Enssle, vertreten durch Dr. Albert Heiss, Rechtsanwalt in Innsbruck, gegen den Antragsgegner PhD MedR Oskar Sträßer, vertreten durch Dr. Christian Fuchs Rechtsanwalt GmbH, Innsbruck, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse nach den §§ 81 ff EheG, über die außerordentlichen Revisionsrekurse beider Parteien gegen den Beschluss des Landesgerichts Innsbruck als Rekursgericht vom 30. Mai 2014, GZ 52 R 76/13b-174, womit dem Rekurs des Antragsgegners nicht Folge gegeben und über Rekurs der Antragstellerin der Beschluss des Bezirksgerichts Innsbruck vom 30. November 2012, GZ 1 C 8/07f-163, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Der Beschluss vom 19. März 2015 wird dahin berichtigt, dass es im zweiten Absatz des Spruchs „Dem außerordentlichen Revisionsrekurs des Antragsgegners [anstelle von Antragstellers] wird teilweise Folge gegeben“ und auf Seite 5 der Begründung „Das Erstgericht verpflichtete […] den Antragsgegner zur Leistung […] lautet.

**False Positives:**

- `Rechtsanwalt GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Juliana Enssle`(person)
- `PhD MedR Oskar Sträßer`(person)

**Example 49** (doc_id: `deanon_TRAIN/1Ob192_11h`) (sent_id: `deanon_TRAIN/1Ob192_11h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Hamberg Marine Limited, London, Kapellergasse 9, 4925 Lungdorf, Österreich, vertreten durch Thum Weinreich Schwarz Fuchsbauer Rechtsanwälte OG in St. Pölten, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 1,8 Mio EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Juni 2011, GZ 14 R 214/10h-39, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 3. September 2010, GZ 33 Cg 3/09t-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Marine Limited` — partial — pred is substring of gold: `Hamberg Marine Limited`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hamberg Marine Limited`(organisation)
- `Kapellergasse 9, 4925 Lungdorf, Österreich`(address)

**Example 50** (doc_id: `deanon_TRAIN/1Ob197_18d`) (sent_id: `deanon_TRAIN/1Ob197_18d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Volze KI GmbH & Co KG, Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich, vertreten durch Dr. Klaus-Dieter Strobach und andere Rechtsanwälte, Grieskirchen, gegen die beklagte Partei Land Oberösterreich, Linz, Landhausplatz 1, vertreten durch Dr. Thomas J. A. Langer, LL.M., Rechtsanwalt in Linz, wegen 475.550,18 EUR sA, über die (außerordentliche) Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2018, GZ 4 R 56/18k-17, mit dem das Urteil des Landesgerichts Wels vom 1. März 2018, GZ 3 Cg 3/16z-13, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `KI GmbH` — partial — pred is substring of gold: `Volze KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Volze KI GmbH`(organisation)
- `Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich`(address)

**Example 51** (doc_id: `deanon_TRAIN/1Ob221_17g`) (sent_id: `deanon_TRAIN/1Ob221_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und Hofrätinnen Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Boothe u. Sandmeier IT GmbH (früher OberTelekom GmbH), Ewaldgasse 28, 4084 Mitterberg, Österreich, vormals vertreten durch Dr. Wolfgang Poleschinski, Rechtsanwalt in Hartberg, gegen die beklagte Partei Yelec Dangelmeier, vertreten durch die Dr. Farhad Paya Rechtsanwalt GmbH, Klagenfurt am Wörthersee, wegen 7.583,60 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 24. August 2017, GZ 1 R 127/17x-69, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 28. März 2017, GZ 16 C 1333/14i-65, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

**False Positives:**

- `IT GmbH` — partial — pred is substring of gold: `Boothe u. Sandmeier IT GmbH`
- `Rechtsanwalt GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Boothe u. Sandmeier IT GmbH`(organisation)
- `OberTelekom GmbH`(organisation)
- `Ewaldgasse 28, 4084 Mitterberg, Österreich`(address)
- `Yelec Dangelmeier`(person)

**Example 52** (doc_id: `deanon_TRAIN/1Ob226_20x`) (sent_id: `deanon_TRAIN/1Ob226_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Ibrahim Gerlicher GmbH, Gabriel van Straaten, vertreten durch Dr. Martin Leitner und andere, Rechtsanwälte in Wien, gegen die beklagte Partei Stadt Olaf Doerrien, vertreten durch die Estermann Pock Rechtsanwälte GmbH, Wien, wegen 19.002,01 EUR, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 7. September 2020, GZ 14 R 61/20y-27, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 28. Jänner 2020, GZ 31 Cg 1/19y-22, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Gerlicher GmbH` — positional overlap with gold: `Ibrahim Gerlicher`
- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Ibrahim Gerlicher`(person)
- `Gabriel van Straaten`(person)
- `Olaf Doerrien`(person)

**Example 53** (doc_id: `deanon_TRAIN/1Ob226_20x`) (sent_id: `deanon_TRAIN/1Ob226_20x_54`)


C-620/17,Hochtief Solutions AG, Rn 35, jeweils mwN).

**False Positives:**

- `Solutions AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_TRAIN/1Ob51_11y`) (sent_id: `deanon_TRAIN/1Ob51_11y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei mj Kurt Schwenckel, vertreten durch Mag. Erich Frenner, Rechtsanwalt in Saalfelden, gegen die beklagte Partei Condon Planung GmbH, Corvin Heidtmeyer, vertreten durch Dr. Harald Schwendinger und Dr. Brigitte Piber Rechtsanwälte in Salzburg, wegen 5.100 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 30. Dezember 2010, GZ 53 R 273/10v-12, mit dem über die Berufung der beklagten Partei das Zwischenurteil des Bezirksgerichts Saalfelden vom 23. Juni 2010, GZ 2 C 454/10z-7, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Planung GmbH` — partial — pred is substring of gold: `Condon Planung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kurt Schwenckel`(person)
- `Condon Planung GmbH`(organisation)
- `Corvin Heidtmeyer`(person)

**Example 55** (doc_id: `deanon_TRAIN/1Ob51_14b`) (sent_id: `deanon_TRAIN/1Ob51_14b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Landwirtschaft Glanzlemglanz GmbH, Erhard Blaufuß, vertreten durch Dr. Arno Kempf, Rechtsanwalt in Spittal an der Drau, gegen die beklagten Parteien 1.

**False Positives:**

- `Glanzlemglanz GmbH` — partial — pred is substring of gold: `Landwirtschaft Glanzlemglanz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landwirtschaft Glanzlemglanz GmbH`(organisation)
- `Erhard Blaufuß`(person)

**Example 56** (doc_id: `deanon_TRAIN/1Ob53_25p`) (sent_id: `deanon_TRAIN/1Ob53_25p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Dr. Wurdinger als Vorsitzenden sowie die Hofrätin und die Hofräte Dr. Steger, Mag. Wessely-Kristöfel, Dr. Parzmayr und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Ariadne Ludger, vertreten durch die ANWALTGMBH Rinner Teuchtmann in Linz, gegen die beklagte Partei Ing. Siegbert Fräde, vertreten durch die Wintersberger Rechtsanwälte GmbH in Ried im Innkreis, wegen 200.500 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 30. Jänner 2025, GZ 1 R 2/25g-86, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ariadne Ludger`(person)
- `Ing. Siegbert Fräde`(person)

**Example 57** (doc_id: `deanon_TRAIN/1Ob53_25p`) (sent_id: `deanon_TRAIN/1Ob53_25p_7`)


Die GmbH verkaufte diesen ohne sein Wissen an ihre rumänische Tochtergesellschaft, die ihn an einen Kunden weiterverkaufte.

**False Positives:**

- `Die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_TRAIN/1Ob66_13g_1Ob67_13d_`) (sent_id: `deanon_TRAIN/1Ob66_13g_1Ob67_13d__4`)


Republik Österreich, vertreten durch die Finanzprokuratur in Wien, 2. Dr. Josefine Rummelt und 3. Hammerla Umwelt GmbH, Friedgasse 46, 3264 Unteramt, Österreich, beide vertreten durch Dr. Hubert Simon, Rechtsanwalt in Wien, wegen Leistung und Feststellung, über den Revisionsrekurs der klagenden Partei gegen die Beschlüsse des Oberlandesgerichts Graz als Rekursgericht vom 1. Februar 2013, GZ 7 R 4/13g-31 und 7 R 5/13d-32, womit die Beschlüsse des Landesgerichts Leoben vom 30. Juli 2012, GZ 2 Nc 25/11a-16, und vom 2. Oktober 2012, GZ 2 Nc 25/11a, 28/11t-22, bestätigt wurden, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Umwelt GmbH` — partial — pred is substring of gold: `Hammerla Umwelt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Josefine Rummelt`(person)
- `Hammerla Umwelt GmbH`(organisation)
- `Friedgasse 46, 3264 Unteramt, Österreich`(address)

**Example 59** (doc_id: `deanon_TRAIN/1Ob7_20s`) (sent_id: `deanon_TRAIN/1Ob7_20s_5`)


Francois Klingsoehr, vertreten durch die Dr. Schartner Rechtsanwalt GmbH, Altenmarkt im Pongau, gegen die beklagte Partei Egon Lammprecht, vertreten durch Dr. Reinfried Eberl und andere Rechtsanwälte in Salzburg, wegen Wiederherstellung, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 20. November 2019, GZ 22 R 322/19k-13, mit dem das Urteil des Bezirksgerichts St. Johann im Pongau vom 12. September 2019, GZ 2 C 152/19t-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Entscheidungen der Vorinstanzen werden aus Anlass der Revision einschließlich des durchgeführten Verfahrens als nichtig aufgehoben.

**False Positives:**

- `Rechtsanwalt GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Francois Klingsoehr`(person)
- `Egon Lammprecht`(person)

**Example 60** (doc_id: `deanon_TRAIN/1Ob93_17h`) (sent_id: `deanon_TRAIN/1Ob93_17h_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Hochsprung+Süssmayer Luftfahrt GmbH, Enrico Achmann, Deutschland, vertreten durch Dr. Stefan Gulner, Rechtsanwalt in Wien, gegen die beklagte Partei VetR Techn R Delila Schneeganß, vertreten durch die Maggi Brandl Kathollnig RechtsanwaltsGmbH-Studio Legale, Klagenfurt am Wörthersee, wegen 191.469 EUR sA, über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 10. April 2017, GZ 4 R 32/17h-28, mit dem der Beschluss des Landesgerichts Klagenfurt vom 25. Jänner 2017, GZ 49 Cg 60/14k-24, teilweise bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Luftfahrt GmbH` — partial — pred is substring of gold: `Hochsprung+Süssmayer Luftfahrt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hochsprung+Süssmayer Luftfahrt GmbH`(organisation)
- `Enrico Achmann`(person)
- `VetR Techn R Delila Schneeganß`(person)

**Example 61** (doc_id: `deanon_TRAIN/1Ob9_22p`) (sent_id: `deanon_TRAIN/1Ob9_22p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. HR Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Parteien 1. Mag. Tosca Xyländer und 2. Mag. Heinrich Vlachojannis, vertreten durch die Koch Jilek Rechtsanwälte Partnerschaft, Bruck an der Mur, gegen die beklagte Partei Grüttemann E‑Commerce Aktiengesellschaft, Friedhof Döbling 165, 8401 Abtissendorf, Österreich, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH, Wien, wegen 40.358,88 EUR sA, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. November 2021, GZ 5 R 163/21h-43, mit dem das Urteil des Handelsgerichts Wien vom 31. August 2021, GZ 55 Cg 60/20i-36, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Tosca Xyländer`(person)
- `Mag. Heinrich Vlachojannis`(person)
- `Grüttemann E‑Commerce Aktiengesellschaft`(organisation)
- `Friedhof Döbling 165, 8401 Abtissendorf, Österreich`(address)

**Example 62** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_6`)


Text Gründe: Mit dem angefochtenen Erkenntnis wurde Dr. Nadja Köpers, Rechtsanwalt in Laahen 3, 3240 Pölla, Österreich, wegen des Verstoßes gegen die Bestimmungen des § 9 (Abs 1) RAO und des § 2 RL-BA der Disziplinarvergehen der Verletzung von Berufspflichten und der Beeinträchtigung von Ehre oder (richtig:) Ansehen des Standes nach § 1 Abs 1 erster und zweiter Fall DSt schuldig erkannt, weil er als Rechtsvertreter der Ehegatten Roman und Elfriede Jakubus in Anträgen auf Aufschiebung der Zwangsversteigerungen für seine Mandanten vom 5. September 2013 in näher bezeichneten Verfahren des Bezirksgerichts Innsbruck und des Bezirksgerichts Amstetten sowie in einer näher genannten Feststellungsklage an das Landesgericht Linz vom 7. Oktober 2013 und in einer Impugnationsklage an das Bezirksgericht Amstetten vom 10. Oktober 2013 jeweils vorgebracht hatte, seine Mandanten hätten sämtliche Verpflichtungen aus einer mit der Bachseewald Heizung AG abgeschlossenen Vereinbarung vom 11. Dezember 2012, insbesondere jene zur unwiderruflichen Antragstellung auf Aufhebung der Höfeeigenschaft einer näher bezeichnenden Liegenschaft in Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich, eingehalten, obwohl ihm zum Zeitpunkt der Antragstellung und Klagseinbringung bekannt war, dass der Antrag auf Aufhebung der Höfeeigenschaft vom 13. Dezember 2012 bereits am 14. Juni 2013 von Roman Janis, durch ihn vertreten, entgegen der zuvor genannten Vereinbarung vom 11. Dezember 2012 wieder zurückgezogen worden war.

**False Positives:**

- `Heizung AG` — partial — pred is substring of gold: `Bachseewald Heizung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Nadja Köpers`(person)
- `Laahen 3, 3240 Pölla, Österreich`(address)
- `Jakubus`(person)
- `Bachseewald Heizung AG`(organisation)
- `Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich`(address)
- `Janis`(person)

**Example 63** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_9`)


Die Besetzungsrüge (Z 1) zeigt zwar keine Tatsachengrundlage für die reklamierte Ausgeschlossenheit des Vorsitzenden des Disziplinarrats wegen Befangenheit (§ 43 Abs 1 Z 3 StPO iVm § 77 Abs 3 DSt) auf, weil aufgrund der Mitteilung des Genannten vom 5. Dezember 2014, wonach er keine Veranlassung sehe, seine „rechtsgeschäftlichen Kontakte“ dem Disziplinarbeschuldigten gegenüber offenzulegen, entgegen dem rein spekulativen Berufungsstandpunkt nicht „anzunehmen ist, dass ein berufsbedingtes Naheverhältnis“ des Vorsitzenden des Disziplinarrats zur Traun Lemalnor AG (Prozessgegnerin der vom Disziplinarbeschuldigten vertretenen Mandanten)“ besteht (vgl RIS-Justiz RS0125768, RS0097054).

**False Positives:**

- `Lemalnor AG` — partial — pred is substring of gold: `Traun Lemalnor AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Traun Lemalnor AG`(organisation)

**Example 64** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_12`)


Unkenntnis des Disziplinarbeschuldigten von den Gründen der Daten Unizorstein AG für die beantragte Fortsetzung der Zwangsversteigerungsverfahren;

**False Positives:**

- `Unizorstein AG` — partial — pred is substring of gold: `Daten Unizorstein AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Daten Unizorstein AG`(organisation)

**Example 65** (doc_id: `deanon_TRAIN/2Ob114_24i`) (sent_id: `deanon_TRAIN/2Ob114_24i_4`)


Sloboda, Dr. Thunhart, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Edith Wischnewsky, vertreten durch Metzler & Partner Rechtsanwälte GmbH in Linz, gegen die beklagte Partei KzlR Techn R Quirin Erler, vertreten durch Nenning & Tockner, Rechtsanwälte in Steyr, wegen Herstellung, Ausfolgung und Unterlassung über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Steyr als Berufungsgericht vom 21. Dezember 2023, GZ 1 R 116/23m-12, mit dem einer Berufung der beklagten Partei gegen das Urteil des Bezirksgerichts Kirchdorf an der Krems vom 26. Juli 2023, GZ 1 C 132/23y-7, Folge gegeben wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Edith Wischnewsky`(person)
- `KzlR Techn R Quirin Erler`(person)

**Example 66** (doc_id: `deanon_TRAIN/2Ob178_18t`) (sent_id: `deanon_TRAIN/2Ob178_18t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Veith als Vorsitzenden, den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé sowie die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Garttri Sicherheit -GesmbH, Alpendorfsiedlung 14, 4209 Linzerberg, Österreich, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, wider die beklagte Partei Vogelsanger Marine GmbH, Juri Büttgens, vertreten durch Mag. Dr. Dirk Just, Rechtsanwalt in Wien, wegen (restlich) 30.000 EUR sA, über die „außerordentliche Revision“ der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Juli 2018, GZ 4 R 79/18v-157, mit welchem das Endurteil des Handelsgerichts Wien vom 9. April 2018, GZ 40 Cg 12/11g-153, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

**False Positives:**

- `Marine GmbH` — partial — pred is substring of gold: `Vogelsanger Marine GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Garttri Sicherheit`(organisation)
- `Alpendorfsiedlung 14, 4209 Linzerberg, Österreich`(address)
- `Vogelsanger Marine GmbH`(organisation)
- `Juri Büttgens`(person)

**Example 67** (doc_id: `deanon_TRAIN/2Ob193_23f`) (sent_id: `deanon_TRAIN/2Ob193_23f_5`)


Kff. Magdalena Münsterberg, vertreten durch Weber Rechtsanwälte GmbH & Co KG in Wien 1, gegen die beklagte Partei Gisela Ammenn, vertreten durch BEURLE Rechtsanwälte GmbH & Co KG in Linz, wegen Herausgabe (Streitwert 1.525.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2023, GZ 2 R 87/23m-32, mit dem das Urteil des Landesgerichts Salzburg vom 5. April 2023, GZ 8 Cg 9/23a-22, aufgehoben wurde zu Recht erkannt:  Spruch

**False Positives:**

- `Rechtsanwälte GmbH` — no gold match — likely missing annotation
- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Gisela Ammenn`(person)

**Example 68** (doc_id: `deanon_TRAIN/2Ob194_24d`) (sent_id: `deanon_TRAIN/2Ob194_24d_4`)


Sloboda, Dr. Thunhart, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Rut Dolff, vertreten durch Gottgeisl Leinsmer Weber Rechtsanwälte GmbH in Wien, wider die beklagte Partei Samuel Nachtwei, Malta, vertreten durch Mag. Simon Wallner Rechtsanwalt GmbH in Wien, wegen 30.895 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 1. Oktober 2024, GZ 12 R 72/24g-21, den Beschluss gefasst:  Spruch I. Der Antrag auf Unterbrechung des Revisionsverfahrens bis zur Entscheidung des Europäischen Gerichtshofs zu C-683/24 wird abgewiesen.

**False Positives:**

- `Rechtsanwälte GmbH` — no gold match — likely missing annotation
- `Rechtsanwalt GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Rut Dolff`(person)
- `Samuel Nachtwei`(person)

**Example 69** (doc_id: `deanon_TRAIN/2Ob63_11w`) (sent_id: `deanon_TRAIN/2Ob63_11w_4`)


Holz Seewald AG, Kaiserbrunnengasse 6, 5122 Lindach, Österreich, beide vertreten durch Dr. Leopold Hirsch, Rechtsanwalt in Salzburg, wegen 38.967,48 EUR sA und Feststellung (Streitinteresse 20.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 10. Februar 2011, GZ 4 R 206/10g-29, womit das Urteil des Landesgerichts Salzburg vom 17. August 2010, GZ 7 Cg 49/09f-25, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Seewald AG` — partial — pred is substring of gold: `Holz Seewald AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Holz Seewald AG`(organisation)
- `Kaiserbrunnengasse 6, 5122 Lindach, Österreich`(address)

**Example 70** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden, die Hofräte Dr. Veith und Dr. Musger sowie die Hofrätinnen Dr. E. Solé und Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Luigi Neimeier, vertreten durch Rechtsanwälte Estermann & Partner OG in Mattighofen, gegen die beklagte Partei LNC KI Solutions GmbH, Kordelia Grauel, vertreten durch Dr. Herbert Harlander und Mag. Wolfgang Harlander, Rechtsanwälte in Salzburg, wegen 33.251,85 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. März 2015, GZ 2 R 1/15b-37, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Salzburg vom 23. Oktober 2014, GZ 4 Cg 27/13d-33, bestätigt wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Solutions GmbH` — partial — pred is substring of gold: `LNC KI Solutions GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Luigi Neimeier`(person)
- `LNC KI Solutions GmbH`(organisation)
- `Kordelia Grauel`(person)

**Example 71** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_19`)


Die beklagte Partei brachte das Gerät nach der Rücknahme zur KI Lexglanzber GmbH, deren Geschäftsführer der Cousin des Geschäftsführers der beklagten Partei ist.

**False Positives:**

- `Lexglanzber GmbH` — partial — pred is substring of gold: `KI Lexglanzber GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KI Lexglanzber GmbH`(organisation)

**Example 72** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_61`)


Die beklagte Partei führte gemeinsam mit der LHS Lebensmittel Consulting GmbH eine Einschulungsveranstaltung für Heutrocknungsgeräte durch, an der auch der Kläger teilnahm.

**False Positives:**

- `Consulting GmbH` — partial — pred is substring of gold: `LHS Lebensmittel Consulting GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `LHS Lebensmittel Consulting GmbH`(organisation)

**Example 73** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_80`)


Die Maerklin und Steckelmann Software GmbH befüllte den neu zusammengesetzten Luftentfeuchter Anfang 2011 mit dem Kältemittel R22, dessen Verwendung seit 1. 1.

**False Positives:**

- `Software GmbH` — partial — pred is substring of gold: `Maerklin und Steckelmann Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maerklin und Steckelmann Software GmbH`(organisation)

**Example 74** (doc_id: `deanon_TRAIN/2Ob79_11y`) (sent_id: `deanon_TRAIN/2Ob79_11y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Angelika Ebendorff, vertreten durch Hengstschläger Lindner und Partner Rechtsanwälte GmbH in Linz, gegen die beklagte Partei Sabine Landgraff, vertreten durch Mag. Gerlach Bachinger, Rechtsanwalt in Traun, wegen 14.957,31 EUR sA und Feststellung (Streitinteresse: 7.500 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 15. März 2011, GZ 3 R 34/11g-24, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts Linz vom 22. Dezember 2010, GZ 1 Cg 210/09m-20, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ebendorff`(person)
- `Landgraff`(person)

**Example 75** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei OMedR Eleonore Wunderling, 9020 Klagenfurt, vertreten durch Mag. Michael Hirm, Rechtsanwalt in Klagenfurt, sowie der Nebenintervenientin auf Seiten der klagenden Partei Fildhaut & Claeser Forschung AG, Amanda Deutschlender, vertreten durch Dr. Martin Wuelz, Rechtsanwalt in Innsbruck, gegen die beklagten Parteien 1.

**False Positives:**

- `Forschung AG` — partial — pred is substring of gold: `Fildhaut & Claeser Forschung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OMedR Eleonore Wunderling`(person)
- `Fildhaut & Claeser Forschung AG`(organisation)
- `Amanda Deutschlender`(person)

**Example 76** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_5`)


RheinPharma Services AG, Unterhillinglah 5, 9853 Dornbach, Österreich, vertreten durch Dr. Harald Burmann und andere Rechtsanwälte in Innsbruck, und 3.

**False Positives:**

- `Services AG` — partial — pred is substring of gold: `RheinPharma Services AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RheinPharma Services AG`(organisation)
- `Unterhillinglah 5, 9853 Dornbach, Österreich`(address)

**Example 77** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_6`)


Glöckler Daten AG, Arbeiterstrandbadstraße 492, 8680 Pernreit, Österreich, vertreten durch Dr. Walter Heel, Rechtsanwalt in Innsbruck, wegen 62.404,99 EUR sA und Feststellung (Streitinteresse: 10.000 EUR), über die Revisionen der klagenden, der erstbeklagten und der zweitbeklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Jänner 2011, GZ 4 R 250/10m-85, womit infolge der Berufungen der klagenden, der erstbeklagten und der zweitbeklagten Partei das Urteil des Landesgerichts Innsbruck vom 25. August 2010, GZ 5 Cg 160/08w-74, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Sämtliche Revisionen werden zurückgewiesen.

**False Positives:**

- `Daten AG` — partial — pred is substring of gold: `Glöckler Daten AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Glöckler Daten AG`(organisation)
- `Arbeiterstrandbadstraße 492, 8680 Pernreit, Österreich`(address)

**Example 78** (doc_id: `deanon_TRAIN/2Ob89_17b`) (sent_id: `deanon_TRAIN/2Ob89_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende, die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé sowie den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Aron Dawideit, vertreten durch Posch, Schausberger & Lutz Rechtsanwälte GmbH in Wels, gegen die beklagten Parteien 1. PhD Irvin Kindschuh, 2. Theodor Hermus, und 3.

**False Positives:**

- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Aron Dawideit`(person)
- `PhD Irvin Kindschuh`(person)
- `Theodor Hermus`(person)

**Example 79** (doc_id: `deanon_TRAIN/2Ob91_22d`) (sent_id: `deanon_TRAIN/2Ob91_22d_4`)


Sloboda und Dr. Kikinger als weitere Richter in der Rechtssache der klagenden Partei Farina Dirker, vertreten durch Dr. Sven Rudolf Thorstensen, LL.M., Rechtsanwalt in Wien, gegen die beklagte Partei Lüttge Chemie Limited, René Luidthard, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 40.150,26 EUR sA, im Verfahren über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. Februar 2022, GZ 15 R 171/21h-33, den Beschluss gefasst:  Spruch Die Zurücknahme der Revision wird zur Kenntnis genommen.

**False Positives:**

- `Chemie Limited` — partial — pred is substring of gold: `Lüttge Chemie Limited`
- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Farina Dirker`(person)
- `Lüttge Chemie Limited`(organisation)
- `René Luidthard`(person)

**Example 80** (doc_id: `deanon_TRAIN/3Nc11_13t`) (sent_id: `deanon_TRAIN/3Nc11_13t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie die Hofräte Univ.-Prof Dr. Neumayr und Dr. Jensik als weitere Richter in der Ordinationssache der Antragstellerin Waldzorval Technologien GmbH, Dr.-Kühne-Gasse 29, 9560 Albern, Österreich, vertreten durch Dr. Clemens Thiele, Rechtsanwalt in Salzburg, gegen die Antragsgegnerin Pflege Allemkraft GmbH, Schirmerstraße 61, 8967 Oberhausberg, Österreich, wegen Exekutionsführung nach § 355 EO, infolge Antrags gemäß § 28 JN den Beschluss gefasst:  Spruch Für die Bewilligung und die Vollziehung der beabsichtigten Unterlassungsexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Technologien GmbH` — partial — pred is substring of gold: `Waldzorval Technologien GmbH`
- `Allemkraft GmbH` — partial — pred is substring of gold: `Pflege Allemkraft GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Waldzorval Technologien GmbH`(organisation)
- `Dr.-Kühne-Gasse 29, 9560 Albern, Österreich`(address)
- `Pflege Allemkraft GmbH`(organisation)
- `Schirmerstraße 61, 8967 Oberhausberg, Österreich`(address)

**Example 81** (doc_id: `deanon_TRAIN/3Nc19_22g`) (sent_id: `deanon_TRAIN/3Nc19_22g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek sowie den Hofrat Dr. Stefula als weitere Richter in der Ordinationssache der Antragstellerin Stadt-Robotik GmbH, Hum 65, 9241 Kantnig, Österreich, vertreten durch Specht & Partner Rechtsanwalt GmbH in Wien, gegen die Antragsgegnerin Ing. Verona Obersteiner, Russische Föderation, wegen § 355 EO, über den Ordinationsantrag der Antragstellerin, den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Rechtsanwalt GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stadt-Robotik GmbH`(organisation)
- `Hum 65, 9241 Kantnig, Österreich`(address)
- `Ing. Verona Obersteiner`(person)

**Example 82** (doc_id: `deanon_TRAIN/3Nc39_24a`) (sent_id: `deanon_TRAIN/3Nc39_24a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn und die Hofrätin Dr. Kodek als weitere Richter in der Ordinationssache der betreibenden Partei Wendy Janacek, vertreten durch Dr. Florian Johann Ernst Knaipp, Rechtsanwalt in Wien, gegen die verpflichtete Partei Siege KI Limited, Edgar Dölle, wegen 47.126,91 EUR sA, über den Antrag auf Ordination nach § 28 JN, den Beschluss gefasst:  Spruch Für die Bewilligung und den Vollzug der von der betreibenden Partei beabsichtigten Rechteexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `KI Limited` — partial — pred is substring of gold: `Siege KI Limited`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wendy Janacek`(person)
- `Siege KI Limited`(organisation)
- `Edgar Dölle`(person)

**Example 83** (doc_id: `deanon_TRAIN/3Ob108_18f`) (sent_id: `deanon_TRAIN/3Ob108_18f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Roch und Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Dr. Lorena Arzet, vertreten durch Scherbaum Seebacher Rechtsanwälte GmbH in Graz, wider die beklagte Partei Priv.-Doz.in Rafaela Flamang, vertreten durch Dr. Destaller ua, Rechtsanwälte in Graz, wegen (eingeschränkt) Räumung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 23. Februar 2018, GZ 7 R 137/17v-19, mit dem das Urteil des Bezirksgerichts Graz-Ost vom 29. September 2017, GZ 213 C 131/16m-15, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Lorena Arzet`(person)
- `Priv.-Doz.in Rafaela Flamang`(person)

**Example 84** (doc_id: `deanon_TRAIN/3Ob116_23i_3Ob117_23m_`) (sent_id: `deanon_TRAIN/3Ob116_23i_3Ob117_23m__3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Exekutionssache der betreibenden Partei Gemeinde Florian Endrikat, vertreten durch Muhri & Werschitz Partnerschaft von Rechtsanwälten GmbH in Graz, gegen die verpflichtete Partei Pablo Kroiss, wegen 377,45 EUR sA, über den Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 20. Dezember 2022, GZ 4 R 257/22a-34, womit der Rekurs der verpflichteten Partei gegen den Beschluss des Bezirksgerichts Feldbach vom 20. September 2022, GZ 3 E 3781/21p-30, zurückgewiesen wurde, den Beschluss gefasst:  Spruch I.Der als Revisionsrekurs zu wertende „Einspruch“ des Verpflichteten wird zurückgewiesen.

**False Positives:**

- `Rechtsanwälten GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Florian Endrikat`(person)
- `Pablo Kroiss`(person)

</details>

---

## `Hyphenated_Organisations_Fixed`

**F1:** 0.160 | **Precision:** 0.721 | **Recall:** 0.090  

**Format:** `regex`  
**Description:**
Matches hyphenated organisation names specifically, ensuring the full name is captured.

**Content:**
```
\b([A-Z][a-zA-ZäöüÄÖÜß]+-[A-Z][a-zA-ZäöüÄÖÜß]+(?:\s+[A-Z][a-zA-ZäöüÄÖÜß]+)*\s+(?:GmbH|AG))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.721 | 0.090 | 0.160 | 43 | 31 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 31 | 12 | 314 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc22_13m`) (sent_id: `deanon_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Catharina Frielinghausen, Russische Föderation, gegen die verpflichtete Partei Gartcondon-Bildung GmbH, Alan Looß, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

| Predicted | Gold |
|---|---|
| `Gartcondon-Bildung GmbH` | `Gartcondon-Bildung GmbH` |

**Missed by this rule (FN):**

- `Catharina Frielinghausen` (person)
- `Alan Looß` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob18_25g`) (sent_id: `deanon_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Stanley Plogmeyer, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Tal-Daten GmbH, Karlheinz Hornschuck, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Tal-Daten GmbH` | `Tal-Daten GmbH` |

**Missed by this rule (FN):**

- `Stanley Plogmeyer` (person)
- `Karlheinz Hornschuck` (person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Daniel Wiegand, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei West-Medien Manufaktur GmbH in Liqu, Kanzelweg 32, 4850 Oberthalheim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `West-Medien Manufaktur GmbH` | `West-Medien Manufaktur GmbH` |

**Missed by this rule (FN):**

- `DI Daniel Wiegand` (person)
- `Kanzelweg 32, 4850 Oberthalheim, Österreich` (address)

**Example 3** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_8`)


Nach den wesentlichen Feststellungen (US 3 bis 6) befand sich die See-Maschinenbau GmbH in der zweiten Jahreshälfte 2008 in erheblichen Zahlungsschwierigkeiten.

| Predicted | Gold |
|---|---|
| `See-Maschinenbau GmbH` | `See-Maschinenbau GmbH` |

**Example 4** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__9`)


Text Gründe: Mit unbekämpft in Rechtskraft erwachsenen Urteilen des Bezirksgerichts Spittal an der Drau vom 22. Juni 2017, GZ 5 U 5/17f-26, wurden (I) Andreas Feiereisen des Vergehens der fahrlässigen Tötung nach § 80 Abs 1 StGB schuldig erkannt und hiefür zu einer Geldstrafe verurteilt sowie (II) die Werksynstein-Wind GmbH gemäß § 3 Abs 1 Z 2, Abs 2 VbVG für die vom Schuldspruch (I) erfasste Straftat ihres Entscheidungsträgers verantwortlich erklärt und über diese Gesellschaft eine Verbandsgeldbuße von 70 Tagessätzen zu je 50 Euro verhängt, die unter Bestimmung einer Probezeit von drei Jahren bedingt nachgesehen wurde.

| Predicted | Gold |
|---|---|
| `Werksynstein-Wind GmbH` | `Werksynstein-Wind GmbH` |

**Missed by this rule (FN):**

- `Feiereisen` (person)

**Example 5** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Herbes&Vißers Heizung GmbH, Waldemar Lokämper, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Traun-Luftfahrt GmbH, VetR DDr. Walter Stuehrmann, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

| Predicted | Gold |
|---|---|
| `Traun-Luftfahrt GmbH` | `Traun-Luftfahrt GmbH` |

**Missed by this rule (FN):**

- `Herbes&Vißers Heizung GmbH` (organisation)
- `Waldemar Lokämper` (person)
- `VetR DDr. Walter Stuehrmann` (person)

**Example 6** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_4`)


Republik Österreich, vertreten durch die Finanzprokuratur in Wien, 2. Dr. Ralph Kreidenweiß, und 3. Donau-Automotive GmbH, Ebersreith 11, 8761 Götzendorf, Österreich, beide vertreten durch Dr. Hubert Simon, Rechtsanwalt in Wien, wegen Leistung und Feststellung, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. April 2014, GZ 7 R 21/14h-7, mit dem der Beschluss des Landesgerichts Leoben vom 30. Jänner 2014, GZ 2 Nc 2/14y-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Donau-Automotive GmbH` | `Donau-Automotive GmbH` |

**Missed by this rule (FN):**

- `Dr. Ralph Kreidenweiß` (person)
- `Ebersreith 11, 8761 Götzendorf, Österreich` (address)

**Example 7** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Dr. Wurdinger als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Steger, Mag. Wessely-Kristöfel, Dr. Parzmayr und Dr. Pfurtscheller als weitere Richterinnen und Richter in der Rechtssache der klagenden Partei Bundeskammer für Arbeiter und Angestellte, Wien 4, Prinz-Eugen-Straße 20–22, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Alsynwald-Recycling AG, RgR Mag. Dr. Evelyn Steinkröger, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH in Wien, wegen Unterlassung und Urteilsveröffentlichung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. Juli 2024, GZ 2 R 77/24v-15, mit dem das Urteil des Handelsgerichts Wien vom 28. Februar 2024, GZ 57 Cg 36/23d-8, bestätigt wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Alsynwald-Recycling AG` | `Alsynwald-Recycling AG` |

**Missed by this rule (FN):**

- `RgR Mag. Dr. Evelyn Steinkröger` (person)

**Example 8** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_117`)


Außerdem wird die Valwalduni-Handel AG eine Gegenüberstellung über die von der Änderung betroffenen Bestimmungen sowie die vollständige Fassung der neuen Bedingungen auf ihrer Internetseite veröffentlichen und die Gegenüberstellung dem Kunden auf sein Verlangen zur Verfügung stellen;

| Predicted | Gold |
|---|---|
| `Valwalduni-Handel AG` | `Valwalduni-Handel AG` |

**Example 9** (doc_id: `deanon_TRAIN/1Ob26_20k`) (sent_id: `deanon_TRAIN/1Ob26_20k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Synsynfurt-Finanzen GmbH, Tanja Thielike, vertreten durch die Draxler Rexeis Sozietät von Rechtsanwälten OG, Graz, gegen die beklagte Partei Roberta Reumschüssel, Bakk. phil., vertreten durch Mag. Dr. Alfred Wansch, Rechtsanwalt in Wien, wegen Räumung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtsachen Wien als Berufungsgericht vom 13. November 2019, GZ 39 R 228/19x-70, mit dem das Urteil des Bezirksgerichts Hernals vom 30. April 2019, GZ 4 C 277/16f-64, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Synsynfurt-Finanzen GmbH` | `Synsynfurt-Finanzen GmbH` |

**Missed by this rule (FN):**

- `Tanja Thielike` (person)
- `Roberta Reumschüssel, Bakk. phil.` (person)

**Example 10** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_11`)


Denn die Beweisthemen (Geschäftsgrundlage der eingangs genannten Vereinbarung vom 11. Dezember 2012 mit der Süd-Immobilien AG; von derselben intendierte Verwertung der Liegenschaften in Draskovichgasse 12, 8240 Friedberg, Österreich durch Zwangsversteigerung ungeachtet eines allfälligen Abverkaufs von Liegenschaften in Steghof 15, 4891 Höhenwarth, Österreich ; Auftrag der Mandanten des Disziplinarbeschuldigten zur Zurückziehung des Antrags auf Aufhebung der Höfeeigenschaft;

| Predicted | Gold |
|---|---|
| `Süd-Immobilien AG` | `Süd-Immobilien AG` |

**Missed by this rule (FN):**

- `Draskovichgasse 12, 8240 Friedberg, Österreich` (address)
- `Steghof 15, 4891 Höhenwarth, Österreich` (address)

**Example 11** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_25`)


Im Herbst 2012 habe sich ein Aufkleber der Ostvallem-Robotik GmbH vom Luftentfeuchter gelöst und ein Typenschild mit dem Baujahr 1986 freigelegt.

| Predicted | Gold |
|---|---|
| `Ostvallem-Robotik GmbH` | `Ostvallem-Robotik GmbH` |

**Example 12** (doc_id: `deanon_TRAIN/3Nc19_22g`) (sent_id: `deanon_TRAIN/3Nc19_22g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek sowie den Hofrat Dr. Stefula als weitere Richter in der Ordinationssache der Antragstellerin Stadt-Robotik GmbH, Hum 65, 9241 Kantnig, Österreich, vertreten durch Specht & Partner Rechtsanwalt GmbH in Wien, gegen die Antragsgegnerin Ing. Verona Obersteiner, Russische Föderation, wegen § 355 EO, über den Ordinationsantrag der Antragstellerin, den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Stadt-Robotik GmbH` | `Stadt-Robotik GmbH` |

**Missed by this rule (FN):**

- `Hum 65, 9241 Kantnig, Österreich` (address)
- `Ing. Verona Obersteiner` (person)

**Example 13** (doc_id: `deanon_TRAIN/3Ob185_22k`) (sent_id: `deanon_TRAIN/3Ob185_22k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn und die Hofrätinnen Dr. Weixelbraun-Mohr, Dr. Kodek und Mag. Wessely-Kristöfel als weitere Richter in der Exekutionssache der betreibenden Partei Dr. Brian Adamska, vertreten durch Dr. Martin Neuwirth, Dr. Alexander Neurauter, Rechtsanwälte in Wien, gegen die verpflichtete Partei Kelglanzver-Software GmbH, Egon Libert, vertreten durch Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH in Wien, wegen zwangsweiser Räumung, über den Revisionsrekurs der betreibenden Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 12. August 2022, GZ 40 R 104/22y-20, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 8. April 2022, GZ 49 E 11/22w-3, abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Kelglanzver-Software GmbH` | `Kelglanzver-Software GmbH` |

**Missed by this rule (FN):**

- `Dr. Brian Adamska` (person)
- `Egon Libert` (person)

**Example 14** (doc_id: `deanon_TRAIN/3Ob248_10g`) (sent_id: `deanon_TRAIN/3Ob248_10g_5`)


Text Begründung: Der nunmehrige Oppositionsbeklagte Ronja Crux hatte im Jahr 2005 bei der nunmehrigen Oppositionsklägerin, der Synkraftal-Chemie GmbH, einen gebrauchten Pkw Porsche Carrera 4 gekauft.

| Predicted | Gold |
|---|---|
| `Synkraftal-Chemie GmbH` | `Synkraftal-Chemie GmbH` |

**Missed by this rule (FN):**

- `Ronja Crux` (person)

**Example 15** (doc_id: `deanon_TRAIN/4Ob165_09g`) (sent_id: `deanon_TRAIN/4Ob165_09g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Schenk als Vorsitzende sowie die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Donostzor-Software AG, Florian Gretenkordt, vertreten durch Ewald Weninger Rechtsanwalts GmbH in Wien, gegen die beklagte Partei WienDigital Planung AG, KzlR Volker Chang, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Feststellung und Anfechtung (Streitwert: 101.000.000 EUR), im Verfahren über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Juni 2009, GZ 5 R 44/09s-15, womit das Urteil des Handelsgerichts Wien vom 26. Jänner 2008, GZ 19 Cg 98/08w-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Zurückziehung der außerordentlichen Revision der klagenden Partei dient zur Kenntnis.

| Predicted | Gold |
|---|---|
| `Donostzor-Software AG` | `Donostzor-Software AG` |

**Missed by this rule (FN):**

- `Florian Gretenkordt` (person)
- `WienDigital Planung AG` (organisation)
- `KzlR Volker Chang` (person)

**Example 16** (doc_id: `deanon_TRAIN/4Ob18_20f`) (sent_id: `deanon_TRAIN/4Ob18_20f_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Jörg Drathschmidt, vertreten durch Dr. Winfried Sattlegger und andere Rechtsanwälte in Linz, gegen die beklagte Partei Wien Dorfsud GmbH, Gerlinde Balcerzak, vertreten durch Dr. Helmut Trenkwalder, Rechtsanwalt in Linz, und die Nebenintervenientin auf Seiten der beklagten Partei Waldfen-Versand GmbH, Eva Boztas, vertreten durch Schneider & Schneider Rechtsanwalts GmbH in Wien, wegen 35.628,94 EUR sA Zug um Zug gegen Herausgabe eines Fahrzeugs, über den Rekurs der Nebenintervenientin gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht vom 7. November 2019, GZ 6 R 114/19f-41, mit dem das Urteil des Landesgerichts Linz vom 3. Juli 2019, GZ 36 Cg 4/17m-36, im klagsstattgebenden Teil (Spruchpunkt 1.) aufgehoben wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Waldfen-Versand GmbH` | `Waldfen-Versand GmbH` |

**Missed by this rule (FN):**

- `Jörg Drathschmidt` (person)
- `Wien Dorfsud GmbH` (organisation)
- `Gerlinde Balcerzak` (person)
- `Eva Boztas` (person)

**Example 17** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Kraftheimglanz-Versand GmbH, OStR Dipl.

| Predicted | Gold |
|---|---|
| `Kraftheimglanz-Versand GmbH` | `Kraftheimglanz-Versand GmbH` |

**Example 18** (doc_id: `deanon_TRAIN/4Ob224_23d`) (sent_id: `deanon_TRAIN/4Ob224_23d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, den Hofrat Mag. Dr. Wurdinger und die Hofrätin Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Verlexglanz-Marine GmbH, Andreas Häntsch, Deutschland, vertreten durch die Saxinger Chalupsky & Partner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Emma Bergner kammer, Cathleen Hofschulte, vertreten durch Dr. Friedrich Schulz, Rechtsanwalt in Wien, wegen Unterlassung, Widerruf und Veröffentlichung desselben (Gesamtstreitwert 46.200 EUR), aus Anlass der außerordentlichen Revisionen der klagenden und der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 23. Oktober 2023, GZ 4 R 99/23t-32, mit dem das Urteil des Handelsgerichts Wien vom 27. April 2023, GZ 57 Cg 34/21g-24, bestätigt wurde, den Beschluss gefasst:  Spruch Die gemeinsame Anzeige beider Parteien vom 27. August 2024 über das vereinbarte Ruhen des Verfahrens wird zur Kenntnis genommen.

| Predicted | Gold |
|---|---|
| `Verlexglanz-Marine GmbH` | `Verlexglanz-Marine GmbH` |

**Missed by this rule (FN):**

- `Andreas Häntsch` (person)
- `Emma Bergner` (person)
- `Cathleen Hofschulte` (person)

**Example 19** (doc_id: `deanon_TRAIN/5Ob141_23f`) (sent_id: `deanon_TRAIN/5Ob141_23f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei OMedR Univ.-Prof.in Eugenia Breitenfelder, vertreten durch Poduschka Partner AnwaltsGmbH in Linz, gegen die beklagte Partei Werkfurtval-Lebensmittel AG, Meinrad Birkenmeyer, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 19.600 EUR sA über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 22. Mai 2023, GZ 12 R 6/23y-34, mit dem das Urteil des Landesgerichts Wels vom 11. Jänner 2023, GZ 8 Cg 29/20s-29, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Werkfurtval-Lebensmittel AG` | `Werkfurtval-Lebensmittel AG` |

**Missed by this rule (FN):**

- `OMedR Univ.-Prof.in Eugenia Breitenfelder` (person)
- `Meinrad Birkenmeyer` (person)

**Example 20** (doc_id: `deanon_TRAIN/5Ob141_23f`) (sent_id: `deanon_TRAIN/5Ob141_23f_17`)


Ende des Jahres 2018 schloss er sich der deutschen Musterfeststellungsklage gegen die Conkraftnor-Event AG an.

| Predicted | Gold |
|---|---|
| `Conkraftnor-Event AG` | `Conkraftnor-Event AG` |

**Example 21** (doc_id: `deanon_TRAIN/5Ob146_16f`) (sent_id: `deanon_TRAIN/5Ob146_16f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers Mag. Niels Mueter, vertreten durch Dr. Anke Reisch, Rechtsanwältin in Kitzbühel, gegen die Antragsgegnerin Talgart-Chemie GmbH & Co KG, Tiefe Gasse 5, 2061 Obritz, Österreich, vertreten durch Dr. Lisbeth Lass und Dr. Hans Christian Lass, Rechtsanwälte in Innsbruck, wegen § 52 Abs 1 Z 6 iVm § 20 Abs 3 WEG 2002, infolge des „außerordentlichen“ Revisionsrekurses des Antragstellers gegen den (richtig) Sachbeschluss des Landesgerichts Innsbruck vom 24. Mai 2016, GZ 4 R 128/16a-50, mit dem der Sachbeschluss des Bezirksgerichts Kitzbühel vom 14. März 2016, GZ 4 Msch 7/14x-36, abgeändert wurde, den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.

| Predicted | Gold |
|---|---|
| `Talgart-Chemie GmbH` | `Talgart-Chemie GmbH` |

**Missed by this rule (FN):**

- `Mag. Niels Mueter` (person)
- `Tiefe Gasse 5, 2061 Obritz, Österreich` (address)

**Example 22** (doc_id: `deanon_TRAIN/5Ob206_24s`) (sent_id: `deanon_TRAIN/5Ob206_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Painsi, Dr. Weixelbraun-Mohr, Dr. Steger und Dr. Pfurtscheller als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers OMedR Louisa Dutzke, vertreten durch Mag. Wolfgang Doppelhofer LL.M. LL.M., Rechtsanwalt in Wien, gegen die Antragsgegnerin Alsud-Pflege GmbH, Kirchenwaldweg 10, 3104 St. Pölten, Österreich, vertreten durch Weishaupt Horak Georgiev Rechtsanwälte GmbH & Co KG in Wien, wegen Feststellung der Ausstattungskategorie nach § 15a MRG, über den Revisionsrekurs der Antragsgegnerin gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 26. August 2024, GZ 39 R 144/24a-22, mit dem der Sachbeschluss des Bezirksgerichts Hietzing vom 29. Mai 2024, GZ 9 MSch 18/23k-18, aufgehoben wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Alsud-Pflege GmbH` | `Alsud-Pflege GmbH` |

**Missed by this rule (FN):**

- `OMedR Louisa Dutzke` (person)
- `Kirchenwaldweg 10, 3104 St. Pölten, Österreich` (address)

**Example 23** (doc_id: `deanon_TRAIN/5Ob84_16p`) (sent_id: `deanon_TRAIN/5Ob84_16p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der Rechtssache der klagenden Partei Dimitri Ringlstetter, vertreten durch Dr. Friedrich Gatscha, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. Heimaluni-Event GmbH, Vorderstraß 39, 3920 Harruck, Österreich, vertreten durch Mag. Gerhard Walzl, Rechtsanwalt in Wien, 2. IJWQ Digital Services GmbH, Dr.-Stephan-Krause-Gasse 73, 3244 Baulanden, Österreich, vertreten durch Mag. Alain Danner, Rechtsanwalt in Wien, 3. Dr. Amalia Brodke, vertreten durch Mag. Gerhard Walzl, Rechtsanwalt in Wien, wegen 1. Übertragung der Zusage auf Einräumung von Wohnungseigentum (30.000 EUR), 2. Einverleibung von Miteigentum (50.000 EUR), 3. Zahlung (122.785,01 EUR sA), 4. Feststellung (15.000 EUR), über die außerordentliche Revision der klagenden Partei (Revisionsinteresse 95.000 EUR) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. März 2016, GZ 34 R 152/15w-50, den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Heimaluni-Event GmbH` | `Heimaluni-Event GmbH` |

**Missed by this rule (FN):**

- `Dimitri Ringlstetter` (person)
- `Vorderstraß 39, 3920 Harruck, Österreich` (address)
- `IJWQ Digital Services GmbH` (organisation)
- `Dr.-Stephan-Krause-Gasse 73, 3244 Baulanden, Österreich` (address)
- `Dr. Amalia Brodke` (person)

**Example 24** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_15`)


[4] Zu FN FN110230q ist im Firmenbuch des Handelsgerichts Wien die Seetra-Recycling GmbH (in der Folge „Bauvereinigung“) mit einem Stammkapital von 6.033.342,30 EUR eingetragen.

| Predicted | Gold |
|---|---|
| `Seetra-Recycling GmbH` | `Seetra-Recycling GmbH` |

**Missed by this rule (FN):**

- `FN110230q` (business_register_number)

**Example 25** (doc_id: `deanon_TRAIN/6Ob47_25t`) (sent_id: `deanon_TRAIN/6Ob47_25t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Hofer-Zeni-Rennhofer als Vorsitzende sowie die Hofrätinnen und Hofräte Dr. Faber, Mag. Pertmayr, Dr. Weber und Mag. Nigl LL.M. als weitere Richter in der Rechtssache der klagenden Partei Timothy Scheppan, vertreten durch Dr. Alexander Amann LL.M., Rechtsanwalt in Gamprin-Bendern, Liechtenstein, wider die beklagte Partei Nord-Luftfahrt AG, Niklas Kühlewind, Deutschland, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 71.888,75 EUR sA Zug um Zug gegen die Rückstellung eines Fahrzeugs, in eventu wegen 17.972,19 EUR sA und Feststellung, im Verfahren über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Jänner 2025, GZ 11 R 7/25t-63, den Beschluss gefasst:  Spruch 1.

| Predicted | Gold |
|---|---|
| `Nord-Luftfahrt AG` | `Nord-Luftfahrt AG` |

**Missed by this rule (FN):**

- `Timothy Scheppan` (person)
- `Niklas Kühlewind` (person)

**Example 26** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_17`)


Diese Partner sind: Seedon-Touristik GmbH, Digital Donnor gmbh, YLHZ Umwelt GmbH oder die Verwendung sinngleicher Klauseln zuunterlassen;

| Predicted | Gold |
|---|---|
| `Seedon-Touristik GmbH` | `Seedon-Touristik GmbH` |

**Missed by this rule (FN):**

- `Digital Donnor gmbh` (organisation)
- `YLHZ Umwelt GmbH` (organisation)

**Example 27** (doc_id: `deanon_TRAIN/6Ob69_23z`) (sent_id: `deanon_TRAIN/6Ob69_23z_22`)


6. 2019 (bis 13. 1. 2020) von einer namentlich genannten Person „von Alexandropoulos Energie Bildungsinstituts, Waldunibach-Textil GmbH“ (die später vom Erstgericht in Bezug auf den Komplementär als „seine“ bezeichnet wird) dem Beklagten an eine auf die Fahrschule lautende E-Mail-Adresse unter Angabe (jeweils) von „Rechnungsnummer Fa Ruiters & Siegling Pflege GmbH“ (was einer gekürzten Angabe der GmbH entspricht) und einer Kurzbezeichnung des Inhalts (etwa: „Gehälter 06-2019“) übermittelt wurden, sie an die „Firma Fahrschule Ketterer Robotik [mit der Adresse des Hauptstandorts] gerichtet waren, wobei die UID-Nummer ab Dezember 2019 geändert wurde.

| Predicted | Gold |
|---|---|
| `Waldunibach-Textil GmbH` | `Waldunibach-Textil GmbH` |

**Missed by this rule (FN):**

- `Alexandropoulos Energie` (organisation)
- `Ruiters & Siegling Pflege GmbH` (organisation)
- `Ketterer Robotik` (organisation)

**Example 28** (doc_id: `deanon_TRAIN/8Ob100_19t`) (sent_id: `deanon_TRAIN/8Ob100_19t_4`)


Kraftzorstein-Telekom GmbH Karsten Öllinger, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, und 2. Univ.-Prof.in Rebecca Obermeyr GmbH Klöcklstraße 57, 9111 Berg ob Attendorf, Österreich, vertreten durch Lederer Hoff & Apfelbacher Rechtsanwälte GmbH in Wien, wegen 11.388,49 EUR sA und Feststellung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. Juni 2019, GZ 5 R 60/19h-33, mit dem das Urteil des Handelsgerichts Wien vom 12. März 2019, GZ 51 Cg 62/17z-28, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Kraftzorstein-Telekom GmbH` | `Kraftzorstein-Telekom GmbH` |

**Missed by this rule (FN):**

- `Karsten Öllinger` (person)
- `Univ.-Prof.in Rebecca Obermeyr` (person)
- `Klöcklstraße 57, 9111 Berg ob Attendorf, Österreich` (address)

**Example 29** (doc_id: `deanon_TRAIN/8Ob39_24d`) (sent_id: `deanon_TRAIN/8Ob39_24d_9`)


Hätte sie pflichtgemäß gehandelt und den von ihr geprüften Jahresabschlüssen den Bestätigungsvermerk versagt, hätte er die Aktien nicht gekauft und damit – wegen der kurz nach seinen Käufen von der Nieder-Analyse Solutions AG beantragten Insolvenzeröffnung – keinen Schaden erlitten.

| Predicted | Gold |
|---|---|
| `Nieder-Analyse Solutions AG` | `Nieder-Analyse Solutions AG` |

**Example 30** (doc_id: `deanon_TRAIN/9ObA112_19i`) (sent_id: `deanon_TRAIN/9ObA112_19i_4`)


Jasmin Mühlbredt, vertreten durch Dr. Robert Palka, Rechtsanwalt in Wien, gegen die beklagte Partei und Gegnerin der gefährdeten Partei Valdorf-Technik GmbH, OSR Nicola Holtfoeth, vertreten durch Mag. Kristina Silberbauer, Rechtsanwältin in Wien, wegen Zulassung zur Arbeitsleistung, hier wegen einstweiliger Verfügung, über den Revisionsrekurs der klagenden und gefährdeten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht in Arbeits- und Sozialrechtssachen vom 14. August 2019, GZ 9 Ra 71/19f-12, mit dem dem Rekurs der klagenden und gefährdeten Partei gegen den Beschluss des Landesgerichts Wiener Neustadt als Arbeits- und Sozialgericht vom 25. Juni 2019, GZ 9 Cga 30/19s-8, teilweise Folge gegeben wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Valdorf-Technik GmbH` | `Valdorf-Technik GmbH` |

**Missed by this rule (FN):**

- `OSR Nicola Holtfoeth` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/1Ob16_20i`) (sent_id: `deanon_TRAIN/1Ob16_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Stadt Christina Schorer, vertreten durch die Benn-Ibler Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Donsteinlex AG, Natalie Gieseking, MSc, vertreten durch die Weber Rechtsanwälte GmbH & Co KG, Wien, wegen 312.706,88 EUR sowie Feststellung (Streitwert 80.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Oktober 2019, GZ 6 R 71/19g-17, mit dem das Urteil des Landesgerichts Steyr vom 29. März 2019, GZ 9 Cg 39/18g-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Benn-Ibler Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Christina Schorer`(person)
- `Donsteinlex AG`(organisation)
- `Natalie Gieseking, MSc`(person)

**Example 1** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_4`)


Logdercon-Digital, Dänemark, 2. Fengart GmbH, Oberer Weinweg 87, 9020 Klagenfurt, Österreich, beide vertreten durch Graf & Pitkowitz Rechtsanwälte GmbH in Wien, gegen die Beklagten 1. LGR Medien GmbH, OVX Finanzen, 2. Analyse Kelunizor AG, Fahnberg 42, 4100 Großamberg, Österreich, Deutschland, beide vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Gesamtstreitwert 69.500 EUR), über den Ordinationsantrag der Klägerinnen den Beschluss gefasst:  Spruch Dem Ordinationsantrag wird stattgegeben.

**False Positives:**

- `Reich-Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Logdercon-Digital`(organisation)
- `Fengart GmbH`(organisation)
- `Oberer Weinweg 87, 9020 Klagenfurt, Österreich`(address)
- `LGR Medien GmbH`(organisation)
- `OVX Finanzen`(organisation)
- `Analyse Kelunizor AG`(organisation)
- `Fahnberg 42, 4100 Großamberg, Österreich`(address)

**Example 2** (doc_id: `deanon_TRAIN/4Ob142_21t`) (sent_id: `deanon_TRAIN/4Ob142_21t_4`)


Matzka sowie Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei Natalie Diestel, vertreten durch Viehböck Breiter Schenk & Nau Rechtsanwälte OG in Mödling, gegen die beklagte Partei Siggelko & Tannenberger Logistik ges.m.b.H., Felix Vogelsanger, vertreten durch Celar Senoner Weber-Wilfert Rechtsanwälte GmbH in Wien, wegen Herausgabe eines Buchauszugs (Streitwert 4.000 EUR) und 41.049,64 EUR sA, über die außerordentliche Revision der klagenden Partei, gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Mai 2021, GZ 5 R 162/20k-66, mit dem das Urteil des Handelsgerichts Wien vom 30. September 2020, GZ 48 Cg 28/19f-59, bestätigt wurde, beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Weber-Wilfert Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Natalie Diestel`(person)
- `Siggelko & Tannenberger Logistik ges.m.b.H.`(organisation)
- `Felix Vogelsanger`(person)

**Example 3** (doc_id: `deanon_TRAIN/5Ob200_24h`) (sent_id: `deanon_TRAIN/5Ob200_24h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Wurzer als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Painsi, Dr. Weixelbraun-Mohr, Dr. Steger und Dr. Pfurtscheller als weitere Richter in der Rechtssache der klagenden Partei Ing. Harald Josepeit, vertreten durch die Wutte-Lang Rechtsanwalts GmbH in Klagenfurt, und der Nebenintervenientin auf Seiten der klagenden Partei MMag.

**False Positives:**

- `Wutte-Lang Rechtsanwalts GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ing. Harald Josepeit`(person)

**Example 4** (doc_id: `deanon_TRAIN/6Ob231_24z`) (sent_id: `deanon_TRAIN/6Ob231_24z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Hofer-Zeni-Rennhofer als Vorsitzende sowie die Hofrätinnen und Hofräte Hon.-Prof. Dr. Faber, Mag. Pertmayr, Dr. Weber und Mag. Nigl LL.M. als weitere Richter in der Rechtssache der klagenden Partei Ing. Egon Jurguttis, vertreten durch Poduschka Partner Anwaltsgesellschaft mbH in Linz, wider die beklagte Partei UnterFinanzen AG, Silvius Haagmans, Deutschland, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 9.600 EUR sA, im Verfahren über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Linz als Berufungsgericht vom 7. Oktober 2024, GZ 6 R 57/24b-31, womit das Urteil des Bezirksgerichts Traun vom 16. Februar 2024, GZ 2 C 198/23z-22, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei vom 9. Dezember 2025 auf Fortsetzung des Verfahrens wird abgewiesen.

**False Positives:**

- `Reich-Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ing. Egon Jurguttis`(person)
- `UnterFinanzen AG`(organisation)
- `Silvius Haagmans`(person)

**Example 5** (doc_id: `deanon_TRAIN/6Ob244_17a`) (sent_id: `deanon_TRAIN/6Ob244_17a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden und durch die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny sowie die Hofrätin Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Dr.in Felizitas Kneussle, vertreten durch Kinberger-Schuberth-Fischer Rechtsanwälte GmbH in Zell am See, gegen die beklagte Partei Mag. Heinz Adickes, vertreten durch Mag. Wolfgang Sieder, Rechtsanwalt in Deutschlandsberg, als Verfahrenshelfer, wegen 5.665 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 5. Oktober 2017, GZ 5 R 149/17v-31, mit dem das Urteil des Bezirksgerichts Graz-Ost vom 27. April 2017, GZ 203 C 34/14w-23, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wirdzurückgewiesen.

**False Positives:**

- `Schuberth-Fischer Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr.in Felizitas Kneussle`(person)
- `Mag. Heinz Adickes`(person)

**Example 6** (doc_id: `deanon_TRAIN/6Ob47_25t`) (sent_id: `deanon_TRAIN/6Ob47_25t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Hofer-Zeni-Rennhofer als Vorsitzende sowie die Hofrätinnen und Hofräte Dr. Faber, Mag. Pertmayr, Dr. Weber und Mag. Nigl LL.M. als weitere Richter in der Rechtssache der klagenden Partei Timothy Scheppan, vertreten durch Dr. Alexander Amann LL.M., Rechtsanwalt in Gamprin-Bendern, Liechtenstein, wider die beklagte Partei Nord-Luftfahrt AG, Niklas Kühlewind, Deutschland, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 71.888,75 EUR sA Zug um Zug gegen die Rückstellung eines Fahrzeugs, in eventu wegen 17.972,19 EUR sA und Feststellung, im Verfahren über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Jänner 2025, GZ 11 R 7/25t-63, den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Reich-Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Timothy Scheppan`(person)
- `Nord-Luftfahrt AG`(organisation)
- `Niklas Kühlewind`(person)

**Example 7** (doc_id: `deanon_TRAIN/7Ob55_25a`) (sent_id: `deanon_TRAIN/7Ob55_25a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Malesich, Dr. Weber, Mag. Fitz und Mag. Jelinek als weitere Richter in der Rechtssache der klagenden Partei Laurin Tieltges, vertreten durch die Poduschka Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Guender Medien AG, Lothar Sax, vertreten durch die CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 6.090 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 13. Dezember 2024, GZ 2 R 125/24g-42, mit dem das Urteil des Bezirksgerichts Innsbruck vom 28. Mai 2024, GZ 26 C 450/20h-37, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Reich-Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Laurin Tieltges`(person)
- `Guender Medien AG`(organisation)
- `Lothar Sax`(person)

**Example 8** (doc_id: `deanon_TRAIN/8ObA18_17f`) (sent_id: `deanon_TRAIN/8ObA18_17f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Brenn als weitere Richter sowie die fachkundigen Laienrichter Mag. Dr. Bernhard Gruber und Harald Kohlruss in der Arbeitsrechtssache der klagenden Partei Cassandra Hennel, vertreten durch Freimüller/Obereder/Pilz Rechtsanwält_innen GmbH in Wien, gegen die beklagte Partei SeeTextil AG, Othmar Dempewolf, vertreten durch DLA Piper Weiss-Tessbach Rechtsanwälte GmbH in Wien, wegen Feststellung (Streitwert 282,56 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. November 2016, GZ 7 Ra 90/16f-19, mit dem das Urteil des Arbeits- und Sozialgerichts Wien vom 20. Juli 2016, GZ 33 Cga 50/16p-15, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Weiss-Tessbach Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Cassandra Hennel`(person)
- `SeeTextil AG`(organisation)
- `Othmar Dempewolf`(person)

**Example 9** (doc_id: `deanon_TRAIN/8ObS12_19a`) (sent_id: `deanon_TRAIN/8ObS12_19a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Wessely-Kristöfel als weitere Richter sowie die fachkundigen Laienrichter Mag. Thomas Stegmüller (aus dem Kreis der Arbeitgeber) und Gerald Fida (aus dem Kreis der Arbeitnehmer) in der Sozialrechtssache der klagenden Partei Titus Thüne, vertreten durch Dr. Christoph Orgler, Rechtsanwalt in Graz, gegen die beklagte Partei IEF-Service GmbH, Geschäftsstelle Graz, 8020 Graz, Europaplatz 12, vertreten durch die Finanzprokuratur, 1010 Wien, Singerstraße 17–19, wegen 3.159 EUR sA (Insolvenz-Entgelt), über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 12. September 2019, GZ 6 Rs 33/19y-9, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 6. Mai 2019, GZ 36 Cgs 47/19h-5, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `IEF-Service GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Titus Thüne`(person)

**Example 10** (doc_id: `deanon_TRAIN/8ObS8_22t`) (sent_id: `deanon_TRAIN/8ObS8_22t_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Stefula als weitere Richter (Senat gemäß § 11a Abs 3 Z 2 ASGG) in der Sozialrechtssache der klagenden Partei Holger Sykorski, vertreten durch Dr. Herbert Marschitz und andere Rechtsanwälte in Kufstein, gegen die beklagte Partei IEF-Service GmbH, 6020 Innsbruck, Meraner Straße 1, vertreten durch die Finanzprokuratur in Wien, wegen 34.726 EUR sA (Insolvenzentgelt), über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 18. Oktober 2022, GZ 25 Rs 56/22d-34, mit dem das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 9. Juni 2022, GZ 44 Cgs 43/21m-27, samt dem ihm vorangegangenen Verfahren für nichtig erklärt und die Klage zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird Folge gegeben.

**False Positives:**

- `IEF-Service GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Holger Sykorski`(person)

**Example 11** (doc_id: `deanon_TRAIN/9ObA20_22i`) (sent_id: `deanon_TRAIN/9ObA20_22i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende, die Hofräte des Obersten Gerichtshofs Mag. Ziegelbauer und Dr. Hargassner sowie die fachkundigen Laienrichter Mag. Thomas Stegmüller (aus dem Kreis der Arbeitgeber) und Mag. Dr. Robert Toder (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden Partei DI Johanna Nordbruch, vertreten durch Celar Senoner Weber-Wilfert Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Logkraft-Medien GesmbH, Adalbert Neybecker, vertreten durch e/n/w/c Natlacen Walderdorff Cancola Rechtsanwälte GmbH in Wien, wegen 1. Kündigungsanfechtung und 2. Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. Dezember 2021, GZ 10 Ra 82/21h-70, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision der beklagten Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Weber-Wilfert Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `DI Johanna Nordbruch`(person)
- `Logkraft-Medien GesmbH`(organisation)
- `Adalbert Neybecker`(person)

</details>

---

## `GmbH_Suffix_Tight`

**F1:** 0.059 | **Precision:** 0.107 | **Recall:** 0.041  

**Format:** `regex`  
**Description:**
Matches entities ending with 'GmbH' with strict boundaries, ensuring the name starts with a Capital letter and excludes titles and common nouns.

**Content:**
```
(?<![A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s])(?<![A-Z])([A-Z][A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df0-9\s\.\-\+&]*?[A-Za-z0-9])\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.107 | 0.041 | 0.059 | 131 | 14 | 117 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 14 | 117 | 331 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob23_15b`) (sent_id: `deanon_TRAIN/10Ob23_15b_4`)


Steintra Solar GmbH, Kospachstraße 35, 3162 Rainfeld, Österreich, vertreten durch Dr. Paul Vavrovsky und Mag. Christian Schrott, Rechtsanwälte in Salzburg, 2. Umwelt Dorfwald ges.m.b.H., Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich, vertreten durch Dr. Katharina Sedlazeck-Gschaider, Rechtsanwältin in Salzburg, wegen 11.921,56 EUR sA und Feststellung (Streitwert 5.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 27. Jänner 2015, GZ 11 R 14/14d-34, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Steintra Solar GmbH` | `Steintra Solar GmbH` |

**Missed by this rule (FN):**

- `Kospachstraße 35, 3162 Rainfeld, Österreich` (address)
- `Umwelt Dorfwald ges.m.b.H.` (organisation)
- `Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich` (address)

**Example 1** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_4`)


Energie Conwald GmbH & Co KG und 2.

| Predicted | Gold |
|---|---|
| `Energie Conwald GmbH` | `Energie Conwald GmbH` |

**Example 2** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_5`)


Metall Monglanz GmbH, beide Johann-Puch-Straße 5, 8741 Reisstraße, Österreich, beide vertreten durch Dr. Michael Schneditz-Bolfras und andere Rechtsanwälte in Gmunden, wegen Bucheinsicht (in eventu Rechnungslegung) und Zahlung (Streitwert: 70.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Teilurteil des Oberlandesgerichts Linz als Berufungsgericht vom 17. Februar 2014, GZ 3 R 13/14y-90, womit das Urteil des Landesgerichts Wels vom 27. November 2013 (in der mit Beschluss vom 12. Dezember 2013 berichtigten Fassung), GZ 2 Cg 78/10p-82 und -84, abgeändert wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Metall Monglanz GmbH` | `Metall Monglanz GmbH` |

**Missed by this rule (FN):**

- `Johann-Puch-Straße 5, 8741 Reisstraße, Österreich` (address)

**Example 3** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_5`)


Maschinenbau Heimfurtcon GmbH, Fretzschner Medien, 2.

| Predicted | Gold |
|---|---|
| `Maschinenbau Heimfurtcon GmbH` | `Maschinenbau Heimfurtcon GmbH` |

**Missed by this rule (FN):**

- `Fretzschner Medien` (organisation)

**Example 4** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_5`)


Klingenbeil Versand GmbH & Co KG, 2.

| Predicted | Gold |
|---|---|
| `Klingenbeil Versand GmbH` | `Klingenbeil Versand GmbH` |

**Example 5** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_6`)


JQV Finanzen Gruppe GmbH, Innovationsplatz 79, 9751 Nigglai, Österreich, beide vertreten durch Ruggenthaler Rechtsanwalts KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 62.000 EUR) über den außerordentlichen Revisionsrekurs der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Wien vom 20. September 2010, GZ 30 R 29/10w-9, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `JQV Finanzen Gruppe GmbH` | `JQV Finanzen Gruppe GmbH` |

**Missed by this rule (FN):**

- `Innovationsplatz 79, 9751 Nigglai, Österreich` (address)

**Example 6** (doc_id: `deanon_TRAIN/4Ob98_20w`) (sent_id: `deanon_TRAIN/4Ob98_20w_5`)


Malkmuß Marine GmbH, Fettinger-Gasse 7, 4615 Niederprisching, Österreich, vertreten durch MMag.

| Predicted | Gold |
|---|---|
| `Malkmuß Marine GmbH` | `Malkmuß Marine GmbH` |

**Missed by this rule (FN):**

- `Fettinger-Gasse 7, 4615 Niederprisching, Österreich` (address)

**Example 7** (doc_id: `deanon_TRAIN/4Ob98_20w`) (sent_id: `deanon_TRAIN/4Ob98_20w_7`)


Roedel Textil GmbH, Hasledt 4, 9634 Bodenmühl, Österreich, vertreten durch Mag. Wolfgang Weilguni, Rechtsanwalt in Wien, wegen 1.028.146,05 EUR sA und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der Klägerin gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 21. April 2020, GZ 5 R 158/19w-116, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Roedel Textil GmbH` | `Roedel Textil GmbH` |

**Missed by this rule (FN):**

- `Hasledt 4, 9634 Bodenmühl, Österreich` (address)

**Example 8** (doc_id: `deanon_TRAIN/6Ob174_20m`) (sent_id: `deanon_TRAIN/6Ob174_20m_5`)


Holzfuß Garten GmbH, Kindlehen 4, 4211 Kottingersdorf, Österreich, vertreten durch Dr. Hans-Peter Neher, Rechtsanwalt in Bad Ischl, wegen Räumung, Unterlassung und Duldung, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Wels als Berufungsgericht vom 5. Juni 2020, GZ 22 R 109/20s-25, mit dem das Urteil des Bezirksgerichts Bad Ischl vom 29. Jänner 2020, GZ 12 C 27/19y-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Holzfuß Garten GmbH` | `Holzfuß Garten GmbH` |

**Missed by this rule (FN):**

- `Kindlehen 4, 4211 Kottingersdorf, Österreich` (address)

**Example 9** (doc_id: `deanon_TRAIN/6Ob207_18m`) (sent_id: `deanon_TRAIN/6Ob207_18m_4`)


Balnuweit Technik GmbH, sowie 2. Ost Werkmon GmbH, alle Am Waidfeld 8, 5211 Gstöckat, Österreich, alle vertreten durch Dr. Peter Zöchbauer, Rechtsanwalt in Wien, wegen (zuletzt) Widerrufs, Veröffentlichung und Zahlung von 9.000 EUR, über die Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 30. Mai 2018, GZ 5 R 39/18v-27, womit über Berufung der beklagten Parteien das Urteil des Handelsgerichts Wien vom 24. Jänner 2018, GZ 39 Cg 26/17t-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Balnuweit Technik GmbH` | `Balnuweit Technik GmbH` |

**Missed by this rule (FN):**

- `Ost Werkmon GmbH` (organisation)
- `Am Waidfeld 8, 5211 Gstöckat, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc22_13m`) (sent_id: `deanon_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Catharina Frielinghausen, Russische Föderation, gegen die verpflichtete Partei Gartcondon-Bildung GmbH, Alan Looß, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

**False Positives:**

- `Bildung GmbH` — partial — pred is substring of gold: `Gartcondon-Bildung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Catharina Frielinghausen`(person)
- `Gartcondon-Bildung GmbH`(organisation)
- `Alan Looß`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei C. Dersudheim Digital GmbH, Taxlbergstraße 247, 8151 Rohrbach, Österreich, vertreten durch Dr. Carl Benkhofer, Rechtsanwalt in Wien, gegen die beklagte Partei Ingolf Grimpe, vertreten durch Greiml & Horwath Rechtsanwaltspartnerschaft in Graz, wegen 5.232 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 14 C 1302/11a des Bezirksgerichts Graz-West in nichtöffentlicher Sitzung, den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Graz-West das Bezirksgericht Fünfhaus bestimmt.

**False Positives:**

- `Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei C. Dersudheim Digital GmbH` — partial — gold is substring of pred: `Dersudheim Digital GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dersudheim Digital GmbH`(organisation)
- `Taxlbergstraße 247, 8151 Rohrbach, Österreich`(address)
- `Ingolf Grimpe`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob18_25g`) (sent_id: `deanon_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Stanley Plogmeyer, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Tal-Daten GmbH, Karlheinz Hornschuck, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Daten GmbH` — partial — pred is substring of gold: `Tal-Daten GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stanley Plogmeyer`(person)
- `Tal-Daten GmbH`(organisation)
- `Karlheinz Hornschuck`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob20_19t`) (sent_id: `deanon_TRAIN/10Ob20_19t_11`)


Der Zweitkläger ist geschäftsführender Alleingesellschafter einer GmbH.

**False Positives:**

- `Der Zweitkläger ist geschäftsführender Alleingesellschafter einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Ob20_19t`) (sent_id: `deanon_TRAIN/10Ob20_19t_38`)


Auftraggeber sei nur die GmbH gewesen.

**False Positives:**

- `Auftraggeber sei nur die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_15`)


Mit Vertrag vom 28. 3. 2007 wurden die Lizenznehmerinnen nach Firmenänderung als übertragende Gesellschaften mit der Mittel Bachnexlem Betriebe GmbH als übernehmende Gesellschaft verschmolzen, die am 26.

**False Positives:**

- `Mit Vertrag vom 28. 3. 2007 wurden die Lizenznehmerinnen nach Firmenänderung als übertragende Gesellschaften mit der Mittel Bachnexlem Betriebe GmbH` — partial — gold is substring of pred: `Mittel Bachnexlem Betriebe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mittel Bachnexlem Betriebe GmbH`(organisation)

**Example 6** (doc_id: `deanon_TRAIN/10Ob38_25y`) (sent_id: `deanon_TRAIN/10Ob38_25y_10`)


Die Beklagte wies bei diesem Gespräch auch auf ihre angespannte wirtschaftliche Situation hin und dass sie im GmbH-Recht nicht so bewandert sei; sie gab an, dass sie eine Gewinnauszahlung aus der GmbH erreichen wolle.

**False Positives:**

- `Die Beklagte wies bei diesem Gespräch auch auf ihre angespannte wirtschaftliche Situation hin und dass sie im GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt, aus denen Erträge erzielt werden sollen.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Daniel Wiegand, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei West-Medien Manufaktur GmbH in Liqu, Kanzelweg 32, 4850 Oberthalheim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Medien Manufaktur GmbH` — partial — pred is substring of gold: `West-Medien Manufaktur GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DI Daniel Wiegand`(person)
- `West-Medien Manufaktur GmbH`(organisation)
- `Kanzelweg 32, 4850 Oberthalheim, Österreich`(address)

**Example 9** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_5`)


Text Begründung: Der Kläger erwarb als Verbraucher im Juni 2003 über Vermittlung eines selbständigen Vermögensberaters Kommanditanteile an der Bestelmeyer+Keßelheim Software GmbH & Co KG im Nominale von 17.000 EUR zuzüglich 850 EUR Agio.

**False Positives:**

- `Keßelheim Software GmbH` — partial — pred is substring of gold: `Bestelmeyer+Keßelheim Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bestelmeyer+Keßelheim Software GmbH`(organisation)

**Example 10** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_8`)


Nach den wesentlichen Feststellungen (US 3 bis 6) befand sich die See-Maschinenbau GmbH in der zweiten Jahreshälfte 2008 in erheblichen Zahlungsschwierigkeiten.

**False Positives:**

- `Maschinenbau GmbH` — partial — pred is substring of gold: `See-Maschinenbau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `See-Maschinenbau GmbH`(organisation)

**Example 12** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_11`)


„Nachdem“ es für die Wilken E‑Commerce GmbH notwendig geworden war, für die Aufnahme des Rennbetriebs 35.000 Euro in das Fahrzeug zu investieren, konnte aufgrund dessen schlechten Zustands kein Rennen erfolgreich beendet werden.

**False Positives:**

- `Commerce GmbH` — partial — pred is substring of gold: `Wilken E‑Commerce GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wilken E‑Commerce GmbH`(organisation)

**Example 13** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__9`)


Text Gründe: Mit unbekämpft in Rechtskraft erwachsenen Urteilen des Bezirksgerichts Spittal an der Drau vom 22. Juni 2017, GZ 5 U 5/17f-26, wurden (I) Andreas Feiereisen des Vergehens der fahrlässigen Tötung nach § 80 Abs 1 StGB schuldig erkannt und hiefür zu einer Geldstrafe verurteilt sowie (II) die Werksynstein-Wind GmbH gemäß § 3 Abs 1 Z 2, Abs 2 VbVG für die vom Schuldspruch (I) erfasste Straftat ihres Entscheidungsträgers verantwortlich erklärt und über diese Gesellschaft eine Verbandsgeldbuße von 70 Tagessätzen zu je 50 Euro verhängt, die unter Bestimmung einer Probezeit von drei Jahren bedingt nachgesehen wurde.

**False Positives:**

- `Wind GmbH` — partial — pred is substring of gold: `Werksynstein-Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Feiereisen`(person)
- `Werksynstein-Wind GmbH`(organisation)

**Example 14** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__17`)


Indem das Bezirksgericht über die Jusepeitis&Niemöller Bildung GmbH eine (das Höchstmaß von somit 55 Tagessätzen übersteigende) Verbandsgeldbuße von 70 Tagessätzen verhängte, verletzte es § 4 Abs 3 VbVG).

**False Positives:**

- `Indem das Bezirksgericht über die Jusepeitis&Niemöller Bildung GmbH` — partial — gold is substring of pred: `Jusepeitis&Niemöller Bildung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jusepeitis&Niemöller Bildung GmbH`(organisation)

**Example 15** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__26`)


Indem das vorliegende Urteil in Ansehung der Hup & Glossner Solar GmbH in gekürzter Form (§ 270 Abs 4 StPO) ausgefertigt wurde, verletzt es das Gesetz in § 22 Abs 5 VbVG iVm § 270 Abs 2 Z 5 StPO.“

**False Positives:**

- `Indem das vorliegende Urteil in Ansehung der Hup & Glossner Solar GmbH` — partial — gold is substring of pred: `Hup & Glossner Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hup & Glossner Solar GmbH`(organisation)

**Example 16** (doc_id: `deanon_TRAIN/15Os161_11g`) (sent_id: `deanon_TRAIN/15Os161_11g_14`)


Rechtliche Beurteilung Die Mängelrüge (Z 5 zweiter Fall) vermisst zu I./ eine Erörterung der eine Täterschaft des Beschwerdeführers in Abrede stellenden Verantwortungen der beiden Angeklagten, zu IV./ wiederum eine Auseinandersetzung einerseits mit der Aussage des Angeklagten Gisbert Springler, dass die in Serbien sichergestellte Maschine nicht mit jener der Trübe&Conz Landwirtschaft GmbH ident sei, andererseits mit der seine Tatbeteiligung leugnenden Verantwortung des Angeklagten Buchhalla.

**False Positives:**

- `Conz Landwirtschaft GmbH` — partial — pred is substring of gold: `Trübe&Conz Landwirtschaft GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gisbert Springler`(person)
- `Trübe&Conz Landwirtschaft GmbH`(organisation)
- `Buchhalla`(person)

**Example 17** (doc_id: `deanon_TRAIN/18OCg12_19t`) (sent_id: `deanon_TRAIN/18OCg12_19t_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Veith und die Hofräte Dr. Höllwerth, Priv.-Doz. Dr. Rassi und Mag. Painsi als weitere Richter in der Schiedsrechtssache der klagenden Partei Trabruckgart Holding GmbH, Jean Nellner, vertreten durch die SRG Stock Rafaseder Gruszkiewicz Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Lydia Astorre, Bulgarien, wegen Aufhebung eines Schiedsspruchs (Streitwert 257.397,45 EUR), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Klage wird als nicht zur Bestimmung einer Tagsatzung zur mündlichen Verhandlung geeignet zurückgewiesen.

**False Positives:**

- `Doz. Dr. Rassi und Mag. Painsi als weitere Richter in der Schiedsrechtssache der klagenden Partei Trabruckgart Holding GmbH` — partial — gold is substring of pred: `Trabruckgart Holding GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Trabruckgart Holding GmbH`(organisation)
- `Jean Nellner`(person)
- `Lydia Astorre`(person)

**Example 18** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Herbes&Vißers Heizung GmbH, Waldemar Lokämper, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Traun-Luftfahrt GmbH, VetR DDr. Walter Stuehrmann, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

**False Positives:**

- `Vißers Heizung GmbH` — partial — pred is substring of gold: `Herbes&Vißers Heizung GmbH`
- `Luftfahrt GmbH` — partial — pred is substring of gold: `Traun-Luftfahrt GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Herbes&Vißers Heizung GmbH`(organisation)
- `Waldemar Lokämper`(person)
- `Traun-Luftfahrt GmbH`(organisation)
- `VetR DDr. Walter Stuehrmann`(person)

**Example 19** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_4`)


Republik Österreich, vertreten durch die Finanzprokuratur in Wien, 2. Dr. Ralph Kreidenweiß, und 3. Donau-Automotive GmbH, Ebersreith 11, 8761 Götzendorf, Österreich, beide vertreten durch Dr. Hubert Simon, Rechtsanwalt in Wien, wegen Leistung und Feststellung, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. April 2014, GZ 7 R 21/14h-7, mit dem der Beschluss des Landesgerichts Leoben vom 30. Jänner 2014, GZ 2 Nc 2/14y-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Automotive GmbH` — partial — pred is substring of gold: `Donau-Automotive GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Ralph Kreidenweiß`(person)
- `Donau-Automotive GmbH`(organisation)
- `Ebersreith 11, 8761 Götzendorf, Österreich`(address)

**Example 20** (doc_id: `deanon_TRAIN/1Ob139_18z`) (sent_id: `deanon_TRAIN/1Ob139_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Angelina Töpker Inc., Ronja Straßgschwandtner, vertreten durch Mag. Ralph Kilches, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Lilia Anderßon, als Insolvenzverwalter im Insolvenzverfahren über das Vermögen der Vanek und Eloy Analyse GmbH, Kanischaberg 21, 4742 Kornrödt, Österreich, vertreten durch die Haslinger/Nagele & Partner Rechtsanwälte GmbH, Linz, wegen Feststellung einer Insolvenzforderung (Streitwert 447.352,05 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 28. Juni 2018, GZ 1 R 83/18h-8, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Nagele & Partner Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Angelina Töpker`(person)
- `Ronja Straßgschwandtner`(person)
- `Mag. Lilia Anderßon`(person)
- `Vanek und Eloy Analyse GmbH`(organisation)
- `Kanischaberg 21, 4742 Kornrödt, Österreich`(address)

**Example 21** (doc_id: `deanon_TRAIN/1Ob16_20i`) (sent_id: `deanon_TRAIN/1Ob16_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Stadt Christina Schorer, vertreten durch die Benn-Ibler Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Donsteinlex AG, Natalie Gieseking, MSc, vertreten durch die Weber Rechtsanwälte GmbH & Co KG, Wien, wegen 312.706,88 EUR sowie Feststellung (Streitwert 80.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Oktober 2019, GZ 6 R 71/19g-17, mit dem das Urteil des Landesgerichts Steyr vom 29. März 2019, GZ 9 Cg 39/18g-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Ibler Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Christina Schorer`(person)
- `Donsteinlex AG`(organisation)
- `Natalie Gieseking, MSc`(person)

**Example 22** (doc_id: `deanon_TRAIN/1Ob197_18d`) (sent_id: `deanon_TRAIN/1Ob197_18d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Volze KI GmbH & Co KG, Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich, vertreten durch Dr. Klaus-Dieter Strobach und andere Rechtsanwälte, Grieskirchen, gegen die beklagte Partei Land Oberösterreich, Linz, Landhausplatz 1, vertreten durch Dr. Thomas J. A. Langer, LL.M., Rechtsanwalt in Linz, wegen 475.550,18 EUR sA, über die (außerordentliche) Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2018, GZ 4 R 56/18k-17, mit dem das Urteil des Landesgerichts Wels vom 1. März 2018, GZ 3 Cg 3/16z-13, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Volze KI GmbH` — partial — gold is substring of pred: `Volze KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Volze KI GmbH`(organisation)
- `Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich`(address)

**Example 23** (doc_id: `deanon_TRAIN/1Ob221_17g`) (sent_id: `deanon_TRAIN/1Ob221_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und Hofrätinnen Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Boothe u. Sandmeier IT GmbH (früher OberTelekom GmbH), Ewaldgasse 28, 4084 Mitterberg, Österreich, vormals vertreten durch Dr. Wolfgang Poleschinski, Rechtsanwalt in Hartberg, gegen die beklagte Partei Yelec Dangelmeier, vertreten durch die Dr. Farhad Paya Rechtsanwalt GmbH, Klagenfurt am Wörthersee, wegen 7.583,60 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 24. August 2017, GZ 1 R 127/17x-69, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 28. März 2017, GZ 16 C 1333/14i-65, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

**False Positives:**

- `Zeni-Rennhofer und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Boothe u. Sandmeier IT GmbH` — partial — gold is substring of pred: `Boothe u. Sandmeier IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Boothe u. Sandmeier IT GmbH`(organisation)
- `OberTelekom GmbH`(organisation)
- `Ewaldgasse 28, 4084 Mitterberg, Österreich`(address)
- `Yelec Dangelmeier`(person)

**Example 24** (doc_id: `deanon_TRAIN/1Ob226_20x`) (sent_id: `deanon_TRAIN/1Ob226_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Ibrahim Gerlicher GmbH, Gabriel van Straaten, vertreten durch Dr. Martin Leitner und andere, Rechtsanwälte in Wien, gegen die beklagte Partei Stadt Olaf Doerrien, vertreten durch die Estermann Pock Rechtsanwälte GmbH, Wien, wegen 19.002,01 EUR, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 7. September 2020, GZ 14 R 61/20y-27, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 28. Jänner 2020, GZ 31 Cg 1/19y-22, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Ibrahim Gerlicher GmbH` — partial — gold is substring of pred: `Ibrahim Gerlicher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ibrahim Gerlicher`(person)
- `Gabriel van Straaten`(person)
- `Olaf Doerrien`(person)

**Example 25** (doc_id: `deanon_TRAIN/1Ob26_20k`) (sent_id: `deanon_TRAIN/1Ob26_20k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Synsynfurt-Finanzen GmbH, Tanja Thielike, vertreten durch die Draxler Rexeis Sozietät von Rechtsanwälten OG, Graz, gegen die beklagte Partei Roberta Reumschüssel, Bakk. phil., vertreten durch Mag. Dr. Alfred Wansch, Rechtsanwalt in Wien, wegen Räumung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtsachen Wien als Berufungsgericht vom 13. November 2019, GZ 39 R 228/19x-70, mit dem das Urteil des Bezirksgerichts Hernals vom 30. April 2019, GZ 4 C 277/16f-64, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Synsynfurt-Finanzen GmbH` — partial — gold is substring of pred: `Synsynfurt-Finanzen GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synsynfurt-Finanzen GmbH`(organisation)
- `Tanja Thielike`(person)
- `Roberta Reumschüssel, Bakk. phil.`(person)

**Example 26** (doc_id: `deanon_TRAIN/1Ob53_25p`) (sent_id: `deanon_TRAIN/1Ob53_25p_5`)


Der Kläger vereinbarte mit einer GmbH (nachfolgend auch „Gesellschaft“) den Kauf eines neuen Mähdreschers gegen „Eintausch“ seines gebrauchten Mähdreschers und Zahlung eines Aufpreises nach Lieferung des neuen Fahrzeugs.

**False Positives:**

- `Der Kläger vereinbarte mit einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_TRAIN/1Ob53_25p`) (sent_id: `deanon_TRAIN/1Ob53_25p_7`)


Die GmbH verkaufte diesen ohne sein Wissen an ihre rumänische Tochtergesellschaft, die ihn an einen Kunden weiterverkaufte.

**False Positives:**

- `Die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_TRAIN/1Ob53_25p`) (sent_id: `deanon_TRAIN/1Ob53_25p_23`)


Der Geschäftsführer einer GmbH haftet nach § 25 GmbHG grundsätzlich nur gegenüber der Gesellschaft und nicht auch gegenüber den Gesellschaftsgläubigern (4 Ob 222/18b [Pkt 2.2];

**False Positives:**

- `Der Geschäftsführer einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_TRAIN/1Ob82_18t`) (sent_id: `deanon_TRAIN/1Ob82_18t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei MurUmwelt GmbH, Oskar Stelzel, vertreten durch die KRONBERGER Rechtsanwälte Gesellschaft mbH, Wien, gegen die beklagte Partei Brian Hüpsch, vertreten durch Dr. Werner Loos, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 14. März 2018, GZ 38 R 303/17s-48, mit dem das Urteil des Bezirksgerichts Fünfhaus vom 4. August 2017, GZ 22 C 163/16w-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei MurUmwelt GmbH` — partial — gold is substring of pred: `MurUmwelt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MurUmwelt GmbH`(organisation)
- `Oskar Stelzel`(person)
- `Brian Hüpsch`(person)

**Example 30** (doc_id: `deanon_TRAIN/1Ob93_17h`) (sent_id: `deanon_TRAIN/1Ob93_17h_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Hochsprung+Süssmayer Luftfahrt GmbH, Enrico Achmann, Deutschland, vertreten durch Dr. Stefan Gulner, Rechtsanwalt in Wien, gegen die beklagte Partei VetR Techn R Delila Schneeganß, vertreten durch die Maggi Brandl Kathollnig RechtsanwaltsGmbH-Studio Legale, Klagenfurt am Wörthersee, wegen 191.469 EUR sA, über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 10. April 2017, GZ 4 R 32/17h-28, mit dem der Beschluss des Landesgerichts Klagenfurt vom 25. Jänner 2017, GZ 49 Cg 60/14k-24, teilweise bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Hochsprung+Süssmayer Luftfahrt GmbH` — partial — gold is substring of pred: `Hochsprung+Süssmayer Luftfahrt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hochsprung+Süssmayer Luftfahrt GmbH`(organisation)
- `Enrico Achmann`(person)
- `VetR Techn R Delila Schneeganß`(person)

**Example 31** (doc_id: `deanon_TRAIN/2Ob159_18y`) (sent_id: `deanon_TRAIN/2Ob159_18y_10`)


Der Kläger war Alleingesellschafter und -geschäftsführer einer GmbH, die sich mit Fenstermontage beschäftigte.

**False Positives:**

- `Der Kläger war Alleingesellschafter und -geschäftsführer einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_TRAIN/2Ob159_18y`) (sent_id: `deanon_TRAIN/2Ob159_18y_11`)


Er selbst war ua als Fenstermonteur in der GmbH tätig.

**False Positives:**

- `Er selbst war ua als Fenstermonteur in der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_19`)


Die beklagte Partei brachte das Gerät nach der Rücknahme zur KI Lexglanzber GmbH, deren Geschäftsführer der Cousin des Geschäftsführers der beklagten Partei ist.

**False Positives:**

- `Die beklagte Partei brachte das Gerät nach der Rücknahme zur KI Lexglanzber GmbH` — partial — gold is substring of pred: `KI Lexglanzber GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KI Lexglanzber GmbH`(organisation)

**Example 34** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_25`)


Im Herbst 2012 habe sich ein Aufkleber der Ostvallem-Robotik GmbH vom Luftentfeuchter gelöst und ein Typenschild mit dem Baujahr 1986 freigelegt.

**False Positives:**

- `Im Herbst 2012 habe sich ein Aufkleber der Ostvallem-Robotik GmbH` — partial — gold is substring of pred: `Ostvallem-Robotik GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ostvallem-Robotik GmbH`(organisation)

**Example 35** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_61`)


Die beklagte Partei führte gemeinsam mit der LHS Lebensmittel Consulting GmbH eine Einschulungsveranstaltung für Heutrocknungsgeräte durch, an der auch der Kläger teilnahm.

**False Positives:**

- `Die beklagte Partei führte gemeinsam mit der LHS Lebensmittel Consulting GmbH` — partial — gold is substring of pred: `LHS Lebensmittel Consulting GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `LHS Lebensmittel Consulting GmbH`(organisation)

**Example 36** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_62`)


Dabei wiesen die anwesenden Mitarbeiter der GmbH darauf hin, dass dieses Unternehmen Ansprechpartner für Serviceleistungen ist.

**False Positives:**

- `Dabei wiesen die anwesenden Mitarbeiter der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

**Example 40** (doc_id: `deanon_TRAIN/3Nc11_13t`) (sent_id: `deanon_TRAIN/3Nc11_13t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie die Hofräte Univ.-Prof Dr. Neumayr und Dr. Jensik als weitere Richter in der Ordinationssache der Antragstellerin Waldzorval Technologien GmbH, Dr.-Kühne-Gasse 29, 9560 Albern, Österreich, vertreten durch Dr. Clemens Thiele, Rechtsanwalt in Salzburg, gegen die Antragsgegnerin Pflege Allemkraft GmbH, Schirmerstraße 61, 8967 Oberhausberg, Österreich, wegen Exekutionsführung nach § 355 EO, infolge Antrags gemäß § 28 JN den Beschluss gefasst:  Spruch Für die Bewilligung und die Vollziehung der beabsichtigten Unterlassungsexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie die Hofräte Univ.-Prof Dr. Neumayr und Dr. Jensik als weitere Richter in der Ordinationssache der Antragstellerin Waldzorval Technologien GmbH` — partial — gold is substring of pred: `Waldzorval Technologien GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Waldzorval Technologien GmbH`(organisation)
- `Dr.-Kühne-Gasse 29, 9560 Albern, Österreich`(address)
- `Pflege Allemkraft GmbH`(organisation)
- `Schirmerstraße 61, 8967 Oberhausberg, Österreich`(address)

**Example 41** (doc_id: `deanon_TRAIN/3Nc19_22g`) (sent_id: `deanon_TRAIN/3Nc19_22g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek sowie den Hofrat Dr. Stefula als weitere Richter in der Ordinationssache der Antragstellerin Stadt-Robotik GmbH, Hum 65, 9241 Kantnig, Österreich, vertreten durch Specht & Partner Rechtsanwalt GmbH in Wien, gegen die Antragsgegnerin Ing. Verona Obersteiner, Russische Föderation, wegen § 355 EO, über den Ordinationsantrag der Antragstellerin, den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Mohr und Dr. Kodek sowie den Hofrat Dr. Stefula als weitere Richter in der Ordinationssache der Antragstellerin Stadt-Robotik GmbH` — partial — gold is substring of pred: `Stadt-Robotik GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stadt-Robotik GmbH`(organisation)
- `Hum 65, 9241 Kantnig, Österreich`(address)
- `Ing. Verona Obersteiner`(person)

**Example 42** (doc_id: `deanon_TRAIN/3Nc39_24a`) (sent_id: `deanon_TRAIN/3Nc39_24a_30`)


Als örtlich zuständiges Exekutionsgericht für die beabsichtigte Rechteexekution ist das Bezirksgericht Salzburg zu bestimmen, weil die Logcon-Möbel.at GmbH als Registrierungsstelle der von der beabsichtigten Exekutionsführung betroffenen Domain der Verpflichteten im Sprengel dieses Gerichts ihren Sitz hat.

**False Positives:**

- `Möbel.at GmbH` — positional overlap with gold: `Logcon-Möbel.at`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Logcon-Möbel.at`(organisation)

**Example 43** (doc_id: `deanon_TRAIN/3Ob12_11b`) (sent_id: `deanon_TRAIN/3Ob12_11b_31`)


Vielmehr überwies der Oppositionskläger vom Geschäftskonto der GmbH einen Betrag von insgesamt 79.000 EUR als „Entnahmen“ auf das Privatkonto des Oppositionsbeklagten, von welchem er dann seinerseits in periodischen Abhebungen 114.500 EUR an sich brachte.

**False Positives:**

- `Vielmehr überwies der Oppositionskläger vom Geschäftskonto der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_TRAIN/3Ob147_20v`) (sent_id: `deanon_TRAIN/3Ob147_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Kraftnorost Wind GmbH, Roderich Holtze, vertreten durch Mag. Andreas Kleiber, Rechtsanwalt in Wien, gegen die beklagte Partei Annette Fiss verein Ing. Kirstin Movcan, vertreten durch Pflaum Karlberger Wiener Opetnik, Rechtsanwälte in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 22. Juli 2020, GZ 40 R 37/20t-27, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Kraftnorost Wind GmbH` — partial — gold is substring of pred: `Kraftnorost Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kraftnorost Wind GmbH`(organisation)
- `Roderich Holtze`(person)
- `Annette Fiss`(person)
- `Ing. Kirstin Movcan`(person)

**Example 45** (doc_id: `deanon_TRAIN/3Ob164_20v`) (sent_id: `deanon_TRAIN/3Ob164_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Bruckgartver GmbH, MedR StR René Titz, vertreten durch Dr. Reinhard Schanda, Rechtsanwalt in Wien, gegen die beklagte Partei Ofczarczik Planung AG, Dipl.

**False Positives:**

- `Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Bruckgartver GmbH` — partial — gold is substring of pred: `Bruckgartver GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bruckgartver GmbH`(organisation)
- `MedR StR René Titz`(person)
- `Ofczarczik Planung AG`(organisation)

**Example 46** (doc_id: `deanon_TRAIN/3Ob185_22k`) (sent_id: `deanon_TRAIN/3Ob185_22k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn und die Hofrätinnen Dr. Weixelbraun-Mohr, Dr. Kodek und Mag. Wessely-Kristöfel als weitere Richter in der Exekutionssache der betreibenden Partei Dr. Brian Adamska, vertreten durch Dr. Martin Neuwirth, Dr. Alexander Neurauter, Rechtsanwälte in Wien, gegen die verpflichtete Partei Kelglanzver-Software GmbH, Egon Libert, vertreten durch Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH in Wien, wegen zwangsweiser Räumung, über den Revisionsrekurs der betreibenden Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 12. August 2022, GZ 40 R 104/22y-20, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 8. April 2022, GZ 49 E 11/22w-3, abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Software GmbH` — partial — pred is substring of gold: `Kelglanzver-Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Brian Adamska`(person)
- `Kelglanzver-Software GmbH`(organisation)
- `Egon Libert`(person)

**Example 47** (doc_id: `deanon_TRAIN/3Ob204_19z`) (sent_id: `deanon_TRAIN/3Ob204_19z_11`)


Darüber hinausgehende Buchhaltungsunterlagen betreffend die Unternehmensgruppe Petkovic Forschung GmbH könne er nicht vorlegen, weil er darauf keinen direkten Zugriff (mehr) habe und die derzeitige Eigentümerin dieses Unternehmens jegliche Offenbarung für Zwecke der Rechnungslegung ablehne.

**False Positives:**

- `Darüber hinausgehende Buchhaltungsunterlagen betreffend die Unternehmensgruppe Petkovic Forschung GmbH` — partial — gold is substring of pred: `Petkovic Forschung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Petkovic Forschung GmbH`(organisation)

**Example 48** (doc_id: `deanon_TRAIN/3Ob204_19z`) (sent_id: `deanon_TRAIN/3Ob204_19z_37`)


Das ist hier schon deshalb nicht der Fall, weil der Verpflichtete selbst davon ausgeht, noch nicht alle Unterlagen vorgelegt zu haben, weil die derzeitige Eigentümerin der Unternehmensgruppe PJS E‑Commerce GmbH bis dato jede Offenbarung von Buchhaltungsunterlagen abgelehnt habe.

**False Positives:**

- `Commerce GmbH` — partial — pred is substring of gold: `PJS E‑Commerce GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PJS E‑Commerce GmbH`(organisation)

**Example 49** (doc_id: `deanon_TRAIN/3Ob209_21p`) (sent_id: `deanon_TRAIN/3Ob209_21p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Nexostlem GmbH & Co KG, Rehlackenweg 5G, 8451 Pernitsch, Österreich, vertreten durch DDr. Heinz Dietmar Schimanko, Rechtsanwalt in Wien, gegen die beklagte Partei RheinLandwirtschaft Vertrieb GmbH, Klaus Dissler, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH & Co KG in Wien, wegen 7.906,82 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 7. Juni 2021, GZ 38 R 66/21v-16, mit dem das Urteil des Bezirksgerichts Favoriten vom 19. Jänner 2021, GZ 3 C 503/20f-12, abgeändert wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Nexostlem GmbH` — partial — gold is substring of pred: `Nexostlem GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nexostlem GmbH`(organisation)
- `Rehlackenweg 5G, 8451 Pernitsch, Österreich`(address)
- `RheinLandwirtschaft Vertrieb GmbH`(organisation)
- `Klaus Dissler`(person)

**Example 50** (doc_id: `deanon_TRAIN/3Ob248_10g`) (sent_id: `deanon_TRAIN/3Ob248_10g_5`)


Text Begründung: Der nunmehrige Oppositionsbeklagte Ronja Crux hatte im Jahr 2005 bei der nunmehrigen Oppositionsklägerin, der Synkraftal-Chemie GmbH, einen gebrauchten Pkw Porsche Carrera 4 gekauft.

**False Positives:**

- `Chemie GmbH` — partial — pred is substring of gold: `Synkraftal-Chemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ronja Crux`(person)
- `Synkraftal-Chemie GmbH`(organisation)

**Example 51** (doc_id: `deanon_TRAIN/3Ob54_21v`) (sent_id: `deanon_TRAIN/3Ob54_21v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in den verbundenen Rechtssachen der klagenden und widerbeklagten Partei Gambal Software GmbH, Esra Bubenischek, vertreten durch Mag. Gerold Schwarzer, Rechtsanwalt in Wien, gegen die beklagte und widerklagende Partei HR Hilde vom Dorf, wegen 286.300,47 EUR sA und 41.219,24 EUR sA, über die außerordentliche Revision der klagenden und widerbeklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 11. Februar 2021, GZ 1 R 168/20m-26, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in den verbundenen Rechtssachen der klagenden und widerbeklagten Partei Gambal Software GmbH` — partial — gold is substring of pred: `Gambal Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gambal Software GmbH`(organisation)
- `Esra Bubenischek`(person)
- `HR Hilde vom Dorf`(person)

**Example 52** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_4`)


Logdercon-Digital, Dänemark, 2. Fengart GmbH, Oberer Weinweg 87, 9020 Klagenfurt, Österreich, beide vertreten durch Graf & Pitkowitz Rechtsanwälte GmbH in Wien, gegen die Beklagten 1. LGR Medien GmbH, OVX Finanzen, 2. Analyse Kelunizor AG, Fahnberg 42, 4100 Großamberg, Österreich, Deutschland, beide vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Gesamtstreitwert 69.500 EUR), über den Ordinationsantrag der Klägerinnen den Beschluss gefasst:  Spruch Dem Ordinationsantrag wird stattgegeben.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Logdercon-Digital`(organisation)
- `Fengart GmbH`(organisation)
- `Oberer Weinweg 87, 9020 Klagenfurt, Österreich`(address)
- `LGR Medien GmbH`(organisation)
- `OVX Finanzen`(organisation)
- `Analyse Kelunizor AG`(organisation)
- `Fahnberg 42, 4100 Großamberg, Österreich`(address)

**Example 53** (doc_id: `deanon_TRAIN/4Ob142_21t`) (sent_id: `deanon_TRAIN/4Ob142_21t_4`)


Matzka sowie Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei Natalie Diestel, vertreten durch Viehböck Breiter Schenk & Nau Rechtsanwälte OG in Mödling, gegen die beklagte Partei Siggelko & Tannenberger Logistik ges.m.b.H., Felix Vogelsanger, vertreten durch Celar Senoner Weber-Wilfert Rechtsanwälte GmbH in Wien, wegen Herausgabe eines Buchauszugs (Streitwert 4.000 EUR) und 41.049,64 EUR sA, über die außerordentliche Revision der klagenden Partei, gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Mai 2021, GZ 5 R 162/20k-66, mit dem das Urteil des Handelsgerichts Wien vom 30. September 2020, GZ 48 Cg 28/19f-59, bestätigt wurde, beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Wilfert Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Natalie Diestel`(person)
- `Siggelko & Tannenberger Logistik ges.m.b.H.`(organisation)
- `Felix Vogelsanger`(person)

**Example 54** (doc_id: `deanon_TRAIN/4Ob145_18d`) (sent_id: `deanon_TRAIN/4Ob145_18d_4`)


Matzka und Dr. Parzmayr in der Rechtssache der klagenden Partei MGL Forschung Consulting GmbH, Lieselotte Wesp, vertreten durch Hauswirth - Kleiber Rechtsanwälte OG in Wien, gegen die beklagten Parteien 1) DI Amber Rzehatschek, 2) DI Esra Noth, ebendort, beide vertreten durch Dr. Herbert Salficky, Rechtsanwalt in Wien, 3) Trinks Möbel GmbH, Hütten 15, 5221 Lasberg, Österreich, vertreten durch Mag. Thomas Stenitzer und Mag. Kurt Schick, Rechtsanwälte in Laa an der Thaya, und 4) DI (FH) Wladimir Runzheimer, vertreten durch Mag. Bernhard Österreicher, Rechtsanwalt in Pfaffstätten, wegen 127.614,09 EUR sA und Feststellung (Streitwert: 5.200 EUR), über die außerordentliche Revision der erst- und zweitbeklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. April 2018, GZ 1 R 179/17a-29, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Matzka und Dr. Parzmayr in der Rechtssache der klagenden Partei MGL Forschung Consulting GmbH` — partial — gold is substring of pred: `MGL Forschung Consulting GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MGL Forschung Consulting GmbH`(organisation)
- `Lieselotte Wesp`(person)
- `DI Amber Rzehatschek`(person)
- `DI Esra Noth`(person)
- `Trinks Möbel GmbH`(organisation)
- `Hütten 15, 5221 Lasberg, Österreich`(address)
- `Wladimir Runzheimer`(person)

**Example 55** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei XDC Druck GmbH, Scarlett Augustus, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Wien, gegen die beklagte Partei UBER B.V., Larissa Ebele, Niederlande, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Unterlassung, Veröffentlichung und Feststellung (Streitwert im Sicherungsverfahren 70.000 EUR), über den Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 4. Juli 2018, GZ 3 R 32/18z-14, mit dem der Beschluss des Handelsgerichts Wien vom 24. April 2018, GZ 58 Cg 10/18f-6, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei XDC Druck GmbH` — partial — gold is substring of pred: `XDC Druck GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `XDC Druck GmbH`(organisation)
- `Scarlett Augustus`(person)
- `Larissa Ebele`(person)

**Example 56** (doc_id: `deanon_TRAIN/4Ob189_19a`) (sent_id: `deanon_TRAIN/4Ob189_19a_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Prof. Dr. Daniela Bour, gegen die beklagte Partei UnterGetränke Consulting GmbH, Alois Willis, vertreten durch die Krüger/Bauer Rechtsanwälte GmbH in Wien, wegen Unterlassung, 21.000 EUR sA, Rechnungslegung, Beseitigung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 43.200 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 24. September 2019, GZ 5 R 86/19g-15, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Bauer Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Daniela Bour`(person)
- `UnterGetränke Consulting GmbH`(organisation)
- `Alois Willis`(person)

**Example 57** (doc_id: `deanon_TRAIN/4Ob18_20f`) (sent_id: `deanon_TRAIN/4Ob18_20f_4`)


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

**Example 58** (doc_id: `deanon_TRAIN/4Ob194_22s`) (sent_id: `deanon_TRAIN/4Ob194_22s_4`)


Matzka und Dr. Annerl sowie die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Dueckers Wind GmbH, Corvin Cetinbag, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, gegen die beklagten Parteien 1. Wendy Goetzen (Verein), 2. Birkfeld+Münzenrieder Daten GmbH, beide Stegg 92, 3925 Neumelon, Österreich, vertreten durch Dr. Brigitte Birnbaum, Dr. Rainer Toperczer, Rechtsanwälte in Wien, wegen Unterlassung, Herausgabe, Feststellung und Urteilsveröffentlichung (Gesamtstreitwert 75.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Juli 2022, GZ 2 R 47/22d-41, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Matzka und Dr. Annerl sowie die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Dueckers Wind GmbH` — partial — gold is substring of pred: `Dueckers Wind GmbH`
- `Münzenrieder Daten GmbH` — partial — pred is substring of gold: `Birkfeld+Münzenrieder Daten GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dueckers Wind GmbH`(organisation)
- `Corvin Cetinbag`(person)
- `Wendy Goetzen`(person)
- `Birkfeld+Münzenrieder Daten GmbH`(organisation)
- `Stegg 92, 3925 Neumelon, Österreich`(address)

**Example 59** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Kraftheimglanz-Versand GmbH, OStR Dipl.

**False Positives:**

- `Versand GmbH` — partial — pred is substring of gold: `Kraftheimglanz-Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kraftheimglanz-Versand GmbH`(organisation)

**Example 60** (doc_id: `deanon_TRAIN/4Ob224_23d`) (sent_id: `deanon_TRAIN/4Ob224_23d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, den Hofrat Mag. Dr. Wurdinger und die Hofrätin Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Verlexglanz-Marine GmbH, Andreas Häntsch, Deutschland, vertreten durch die Saxinger Chalupsky & Partner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Emma Bergner kammer, Cathleen Hofschulte, vertreten durch Dr. Friedrich Schulz, Rechtsanwalt in Wien, wegen Unterlassung, Widerruf und Veröffentlichung desselben (Gesamtstreitwert 46.200 EUR), aus Anlass der außerordentlichen Revisionen der klagenden und der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 23. Oktober 2023, GZ 4 R 99/23t-32, mit dem das Urteil des Handelsgerichts Wien vom 27. April 2023, GZ 57 Cg 34/21g-24, bestätigt wurde, den Beschluss gefasst:  Spruch Die gemeinsame Anzeige beider Parteien vom 27. August 2024 über das vereinbarte Ruhen des Verfahrens wird zur Kenntnis genommen.

**False Positives:**

- `Marine GmbH` — partial — pred is substring of gold: `Verlexglanz-Marine GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Verlexglanz-Marine GmbH`(organisation)
- `Andreas Häntsch`(person)
- `Emma Bergner`(person)
- `Cathleen Hofschulte`(person)

**Example 61** (doc_id: `deanon_TRAIN/4Ob26_20g`) (sent_id: `deanon_TRAIN/4Ob26_20g_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Evelyn Peterhansel GmbH, Corbinian Wischnowski, LLM, vertreten durch Rechtsanwaltskanzlei Dr. Wendling GmbH in Kitzbühel, gegen die beklagte Partei Osttallem Getränke GmbH, Zdenko Weimer, BA, Deutschland, vertreten durch Dr. Dan Katzlinger, Rechtsanwalt in Innsbruck, wegen 70.000 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. Dezember 2019, GZ 10 R 49/19k-32, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei Evelyn Peterhansel GmbH` — partial — gold is substring of pred: `Evelyn Peterhansel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Evelyn Peterhansel`(person)
- `Corbinian Wischnowski, LLM`(person)
- `Osttallem Getränke GmbH`(organisation)
- `Zdenko Weimer, BA`(person)

**Example 62** (doc_id: `deanon_TRAIN/4Ob28_18y`) (sent_id: `deanon_TRAIN/4Ob28_18y_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Bröseke Heizung GmbH, Siegfried Schubarth, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, gegen die beklagte Partei DI Ashley Laurenawitz, vertreten durch Dr. Josef-Michael Danler, Rechtsanwalt in Innsbruck, wegen 29.357,58 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. Oktober 2017, GZ 1 R 140/17y-40, mit dem das Urteil des Landesgerichts Innsbruck vom 23. August 2017, GZ 6 Cg 37/16a-35, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei Bröseke Heizung GmbH` — partial — gold is substring of pred: `Bröseke Heizung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bröseke Heizung GmbH`(organisation)
- `Siegfried Schubarth`(person)
- `DI Ashley Laurenawitz`(person)

**Example 63** (doc_id: `deanon_TRAIN/4Ob9_20g`) (sent_id: `deanon_TRAIN/4Ob9_20g_4`)


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

**Example 64** (doc_id: `deanon_TRAIN/5Ob146_16f`) (sent_id: `deanon_TRAIN/5Ob146_16f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers Mag. Niels Mueter, vertreten durch Dr. Anke Reisch, Rechtsanwältin in Kitzbühel, gegen die Antragsgegnerin Talgart-Chemie GmbH & Co KG, Tiefe Gasse 5, 2061 Obritz, Österreich, vertreten durch Dr. Lisbeth Lass und Dr. Hans Christian Lass, Rechtsanwälte in Innsbruck, wegen § 52 Abs 1 Z 6 iVm § 20 Abs 3 WEG 2002, infolge des „außerordentlichen“ Revisionsrekurses des Antragstellers gegen den (richtig) Sachbeschluss des Landesgerichts Innsbruck vom 24. Mai 2016, GZ 4 R 128/16a-50, mit dem der Sachbeschluss des Bezirksgerichts Kitzbühel vom 14. März 2016, GZ 4 Msch 7/14x-36, abgeändert wurde, den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.

**False Positives:**

- `Chemie GmbH` — partial — pred is substring of gold: `Talgart-Chemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Niels Mueter`(person)
- `Talgart-Chemie GmbH`(organisation)
- `Tiefe Gasse 5, 2061 Obritz, Österreich`(address)

**Example 65** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Penners Medien GmbH, Wilhelmine Kobinger, vertreten durch Dr. Manfred Sommerbauer, DDr. Michael Dohr, LL.M., LL.M., Rechtsanwälte in Wiener Neustadt, gegen die beklagte Partei JRQA Landwirtschaft Rechtsanwälte GmbH, Kometenweg 43, 3200 Rennersdorf, Österreich, wegen Unterlassung (Streitwert 36.000 EUR) und Feststellung (Streitwert 3.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien vom 30. Mai 2022, GZ 5 R 6/22x-46, mit dem das Urteil des Handelsgerichts Wien vom 3. November 2021, GZ 21 Cg 21/21f-39, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Penners Medien GmbH` — partial — gold is substring of pred: `Penners Medien GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Penners Medien GmbH`(organisation)
- `Wilhelmine Kobinger`(person)
- `JRQA Landwirtschaft`(organisation)
- `Kometenweg 43, 3200 Rennersdorf, Österreich`(address)

**Example 66** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_6`)


Die Klägerin ist (Minderheits-)Gesellschafterin einer GmbH.

**False Positives:**

- `Gesellschafterin einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_31`)


Das mit der dritten im Klagebegehren genannten Angelegenheit angestrebte per se-Verbot der Vertretung der GmbH gegenüber Dritten könne außerdem mit einem Interessenkonflikt zwischen der Gesellschaft und dem Mehrheitsgesellschafter keinesfalls begründet werden.

**False Positives:**

- `Das mit der dritten im Klagebegehren genannten Angelegenheit angestrebte per se-Verbot der Vertretung der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_78`)


Das von der Klägerin gewünschte Auslegungsergebnis gerät zudem mit dem für die GmbH in § 61 Abs 1 und 2 GmbHG normierten Trennungsprinzip in Konflikt, das eine strikte Trennung zwischen Gesellschaft und Gesellschaftern und damit auch zwischen Gesellschaftsvermögen und Privatvermögen der Gesellschafter anordnet (1 Ob 81/18w).

**False Positives:**

- `Das von der Klägerin gewünschte Auslegungsergebnis gerät zudem mit dem für die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_80`)


Wird eine GmbH durch einen Dritten geschädigt, ist der dem Gesellschafter dadurch entstehende Nachteil in seinem Vermögen ein nicht ersatzfähiger mittelbarer Schaden.

**False Positives:**

- `Wird eine GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_TRAIN/5Ob200_24h`) (sent_id: `deanon_TRAIN/5Ob200_24h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Wurzer als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Painsi, Dr. Weixelbraun-Mohr, Dr. Steger und Dr. Pfurtscheller als weitere Richter in der Rechtssache der klagenden Partei Ing. Harald Josepeit, vertreten durch die Wutte-Lang Rechtsanwalts GmbH in Klagenfurt, und der Nebenintervenientin auf Seiten der klagenden Partei MMag.

**False Positives:**

- `Lang Rechtsanwalts GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ing. Harald Josepeit`(person)

**Example 71** (doc_id: `deanon_TRAIN/5Ob206_24s`) (sent_id: `deanon_TRAIN/5Ob206_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Painsi, Dr. Weixelbraun-Mohr, Dr. Steger und Dr. Pfurtscheller als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers OMedR Louisa Dutzke, vertreten durch Mag. Wolfgang Doppelhofer LL.M. LL.M., Rechtsanwalt in Wien, gegen die Antragsgegnerin Alsud-Pflege GmbH, Kirchenwaldweg 10, 3104 St. Pölten, Österreich, vertreten durch Weishaupt Horak Georgiev Rechtsanwälte GmbH & Co KG in Wien, wegen Feststellung der Ausstattungskategorie nach § 15a MRG, über den Revisionsrekurs der Antragsgegnerin gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 26. August 2024, GZ 39 R 144/24a-22, mit dem der Sachbeschluss des Bezirksgerichts Hietzing vom 29. Mai 2024, GZ 9 MSch 18/23k-18, aufgehoben wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Pflege GmbH` — partial — pred is substring of gold: `Alsud-Pflege GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OMedR Louisa Dutzke`(person)
- `Alsud-Pflege GmbH`(organisation)
- `Kirchenwaldweg 10, 3104 St. Pölten, Österreich`(address)

**Example 72** (doc_id: `deanon_TRAIN/5Ob221_22v`) (sent_id: `deanon_TRAIN/5Ob221_22v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Fabian + Michailoff Analyse GmbH in Liquidation, Steugasse 3, 6123 Vomperbach, Österreich, vertreten durch Mag. Gottfried Tazol, Rechtsanwalt in Völkermarkt, gegen die beklagte Partei SeeSanitär AG, Helge Schreyvogel, BEd, vertreten durch Mag. Alexander Todor-Kostic LL.M., Mag. Silke Todor-Kostic, Rechtsanwälte in Velden am Wörthersee, wegen 84.999,13 EUR sA, über die außerordentliche Revision der klagenden Partei (Revisionsinteresse 62.200,50 EUR sA) gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 12. Oktober 2022, GZ 5 R 74/22z-53, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Fabian + Michailoff Analyse GmbH` — partial — gold is substring of pred: `Fabian + Michailoff Analyse GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fabian + Michailoff Analyse GmbH`(organisation)
- `Steugasse 3, 6123 Vomperbach, Österreich`(address)
- `SeeSanitär AG`(organisation)
- `Helge Schreyvogel, BEd`(person)

**Example 73** (doc_id: `deanon_TRAIN/5Ob84_16p`) (sent_id: `deanon_TRAIN/5Ob84_16p_3`)


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

**Example 74** (doc_id: `deanon_TRAIN/5Ob93_24y`) (sent_id: `deanon_TRAIN/5Ob93_24y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Jozwiak Robotik GmbH, Florenzia Lohmöller, vertreten durch Rechtsanwälte Dr. Amhof & Dr. Damian GmbH in Wien, gegen die beklagte Partei Dipl.-Ing. Juliana Maurice, wegen Unterfertigung eines Wohnungseigentumsvertrags und Feststellung, hier: Anmerkung der Klage, über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 26. April 2024, GZ 15 R 41/24w-18, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 126 Abs 1 GBG iVm § 62 Abs 1 AußStrG zurückgewiesen.

**False Positives:**

- `Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Jozwiak Robotik GmbH` — partial — gold is substring of pred: `Jozwiak Robotik GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jozwiak Robotik GmbH`(organisation)
- `Florenzia Lohmöller`(person)
- `Dipl.-Ing. Juliana Maurice`(person)

**Example 75** (doc_id: `deanon_TRAIN/6Ob123_19k`) (sent_id: `deanon_TRAIN/6Ob123_19k_10`)


Jedes dieser Unternehmen ist derzeit an das Fernwärmenetz der Fernwärme Wien GmbH angeschlossen.

**False Positives:**

- `Jedes dieser Unternehmen ist derzeit an das Fernwärmenetz der Fernwärme Wien GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_TRAIN/6Ob146_18s`) (sent_id: `deanon_TRAIN/6Ob146_18s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden und die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Paolo Weinrich, vertreten durch Mag. Max Verdino und andere Rechtsanwälte in St. Veit an der Glan, gegen die beklagte Partei Oberüber&Spanjardt Landwirtschaft GmbH, Karola Löcke, vertreten durch PHH Prochaska Havranek Rechtsanwälte GmbH & Co KG in Wien, wegen 18.664,48 EUR und Feststellung, über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 6. Juni 2018, GZ 4 R 51/18d-12, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Klagenfurt vom 20. Februar 2018, GZ 28 Cg 75/17s-8, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Spanjardt Landwirtschaft GmbH` — partial — pred is substring of gold: `Oberüber&Spanjardt Landwirtschaft GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Paolo Weinrich`(person)
- `Oberüber&Spanjardt Landwirtschaft GmbH`(organisation)
- `Karola Löcke`(person)

**Example 77** (doc_id: `deanon_TRAIN/6Ob169_12i`) (sent_id: `deanon_TRAIN/6Ob169_12i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Pimmer als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Dr. Schramm, Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Unlandherm KI GmbH, Ilona Hoernle, vertreten durch List Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Wickl Logistik GmbH, Vitus Glassbrenner, vertreten durch Dr. Christoph Brenner - Mag. Severin Perschl Rechtsanwälte OG in Krems, wegen 7.641,30 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Korneuburg als Berufungsgericht vom 16. Februar 2012, GZ 21 R 262/11v-50, womit das Urteil des Bezirksgerichts Gänserndorf vom 2. August 2011, GZ 12 C 1036/10h-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Prof. Dr. Kodek und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Unlandherm KI GmbH` — partial — gold is substring of pred: `Unlandherm KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unlandherm KI GmbH`(organisation)
- `Ilona Hoernle`(person)
- `Wickl Logistik GmbH`(organisation)
- `Vitus Glassbrenner`(person)

**Example 78** (doc_id: `deanon_TRAIN/6Ob18_20w`) (sent_id: `deanon_TRAIN/6Ob18_20w_6`)


Die GmbH war Eigentümerin einer Liegenschaft, der Beklagte ist Eigentümer der Nachbarliegenschaft.

**False Positives:**

- `Die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_TRAIN/6Ob18_20w`) (sent_id: `deanon_TRAIN/6Ob18_20w_7`)


Der Beklagte ließ auf seine Kosten auf der Liegenschaft der GmbH eine Tiefgarage mit 15 Stellplätzen errichten.

**False Positives:**

- `Der Beklagte ließ auf seine Kosten auf der Liegenschaft der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_TRAIN/6Ob18_20w`) (sent_id: `deanon_TRAIN/6Ob18_20w_9`)


Im Zuge dieser Veräußerung vereinbarte der Beklagte mit der durch den Käufer als Geschäftsführer vertretenen GmbH, dass diese auf ihrer Liegenschaft dem Beklagten und seinen Rechtsnachfolgern im Eigentum der Nachbarliegenschaft unentgeltlich die Dienstbarkeiten der Benützung der unterirdischen Tiefgaragenplätze sowie des Gehens und Fahrens (zu den Stellplätzen) einräume.

**False Positives:**

- `Im Zuge dieser Veräußerung vereinbarte der Beklagte mit der durch den Käufer als Geschäftsführer vertretenen GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_TRAIN/6Ob18_20w`) (sent_id: `deanon_TRAIN/6Ob18_20w_10`)


Diese Dienstbarkeiten wurden im C-Blatt der Liegenschaft der GmbH verbüchert.

**False Positives:**

- `Diese Dienstbarkeiten wurden im C-Blatt der Liegenschaft der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_TRAIN/6Ob18_20w`) (sent_id: `deanon_TRAIN/6Ob18_20w_11`)


In dem über die Liegenschaft der GmbH in der Folge durchgeführten Zwangsversteigerungsverfahren erhielt der Kläger im Jahr 2017 den Zuschlag und wurde als Alleineigentümer im Grundbuch einverleibt.

**False Positives:**

- `In dem über die Liegenschaft der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_TRAIN/6Ob18_20w`) (sent_id: `deanon_TRAIN/6Ob18_20w_12`)


Die GmbH wurde 2018 gemäß § 40 FBG wegen Vermögenslosigkeit im Firmenbuch gelöscht.

**False Positives:**

- `Die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_TRAIN/6Ob231_24z`) (sent_id: `deanon_TRAIN/6Ob231_24z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Hofer-Zeni-Rennhofer als Vorsitzende sowie die Hofrätinnen und Hofräte Hon.-Prof. Dr. Faber, Mag. Pertmayr, Dr. Weber und Mag. Nigl LL.M. als weitere Richter in der Rechtssache der klagenden Partei Ing. Egon Jurguttis, vertreten durch Poduschka Partner Anwaltsgesellschaft mbH in Linz, wider die beklagte Partei UnterFinanzen AG, Silvius Haagmans, Deutschland, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 9.600 EUR sA, im Verfahren über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Linz als Berufungsgericht vom 7. Oktober 2024, GZ 6 R 57/24b-31, womit das Urteil des Bezirksgerichts Traun vom 16. Februar 2024, GZ 2 C 198/23z-22, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei vom 9. Dezember 2025 auf Fortsetzung des Verfahrens wird abgewiesen.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ing. Egon Jurguttis`(person)
- `UnterFinanzen AG`(organisation)
- `Silvius Haagmans`(person)

**Example 85** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_9`)


Ihre ersten Gesellschafter waren Dr. Louisa Sittl mit einer voll eingezahlten Stammeinlage von 22.400 EUR sowie die Seezordorf GmbH mit einer voll eingezahlten Stammeinlage von 12.600 EUR.

**False Positives:**

- `Ihre ersten Gesellschafter waren Dr. Louisa Sittl mit einer voll eingezahlten Stammeinlage von 22.400 EUR sowie die Seezordorf GmbH` — partial — gold is substring of pred: `Dr. Louisa Sittl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Louisa Sittl`(person)
- `Seezordorf GmbH`(organisation)

**Example 86** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_12`)


Derzeit sind als Gesellschafter Dr. Jeremias Mehringer mit einer voll eingezahlten Stammeinlage von 12.600 EUR und die IJB Analyse GmbH mit einer voll eingezahlten Stammeinlage von 1.202.400 EUR eingetragen.

**False Positives:**

- `Derzeit sind als Gesellschafter Dr. Jeremias Mehringer mit einer voll eingezahlten Stammeinlage von 12.600 EUR und die IJB Analyse GmbH` — partial — gold is substring of pred: `Dr. Jeremias Mehringer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Jeremias Mehringer`(person)
- `IJB Analyse GmbH`(organisation)

**Example 87** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_15`)


[4] Zu FN FN110230q ist im Firmenbuch des Handelsgerichts Wien die Seetra-Recycling GmbH (in der Folge „Bauvereinigung“) mit einem Stammkapital von 6.033.342,30 EUR eingetragen.

**False Positives:**

- `Recycling GmbH` — partial — pred is substring of gold: `Seetra-Recycling GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FN110230q`(business_register_number)
- `Seetra-Recycling GmbH`(organisation)

**Example 88** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_31`)


Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG wäre hinsichtlich § 14 Abs 3 FBG sachlich nicht gerechtfertigt.

**False Positives:**

- `Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_66`)


Die Bestimmung sei daher analog auch auf gemeinnützige Bauvereinigungen in der Rechtsform der GmbH oder AG anzuwenden.

**False Positives:**

- `Die Bestimmung sei daher analog auch auf gemeinnützige Bauvereinigungen in der Rechtsform der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `AG_Suffix_Tight`

**F1:** 0.021 | **Precision:** 0.133 | **Recall:** 0.012  

**Format:** `regex`  
**Description:**
Matches entities ending with 'AG' with strict boundaries, ensuring the name starts with a Capital letter and excludes titles.

**Content:**
```
(?<![A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s])(?<![A-Z])([A-Z][A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df0-9\s\.\-\+&]*?[A-Za-z0-9])\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.133 | 0.012 | 0.021 | 30 | 4 | 26 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 26 | 301 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_6`)


OberTratraSoftware Dienstleistungen AG, Prägrader Weg 43, 8616 Gasen, Österreich, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung (5.000 EUR) und 11.561,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2019, GZ 2 R 140/19z-30, mit dem das Urteil des Landesgerichts Wels vom 22. Juli 2019, GZ 26 Cg 66/18m-26, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

| Predicted | Gold |
|---|---|
| `OberTratraSoftware Dienstleistungen AG` | `OberTratraSoftware Dienstleistungen AG` |

**Missed by this rule (FN):**

- `Prägrader Weg 43, 8616 Gasen, Österreich` (address)

**Example 1** (doc_id: `deanon_TRAIN/2Ob63_11w`) (sent_id: `deanon_TRAIN/2Ob63_11w_4`)


Holz Seewald AG, Kaiserbrunnengasse 6, 5122 Lindach, Österreich, beide vertreten durch Dr. Leopold Hirsch, Rechtsanwalt in Salzburg, wegen 38.967,48 EUR sA und Feststellung (Streitinteresse 20.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 10. Februar 2011, GZ 4 R 206/10g-29, womit das Urteil des Landesgerichts Salzburg vom 17. August 2010, GZ 7 Cg 49/09f-25, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Holz Seewald AG` | `Holz Seewald AG` |

**Missed by this rule (FN):**

- `Kaiserbrunnengasse 6, 5122 Lindach, Österreich` (address)

**Example 2** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_5`)


RheinPharma Services AG, Unterhillinglah 5, 9853 Dornbach, Österreich, vertreten durch Dr. Harald Burmann und andere Rechtsanwälte in Innsbruck, und 3.

| Predicted | Gold |
|---|---|
| `RheinPharma Services AG` | `RheinPharma Services AG` |

**Missed by this rule (FN):**

- `Unterhillinglah 5, 9853 Dornbach, Österreich` (address)

**Example 3** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_6`)


Glöckler Daten AG, Arbeiterstrandbadstraße 492, 8680 Pernreit, Österreich, vertreten durch Dr. Walter Heel, Rechtsanwalt in Innsbruck, wegen 62.404,99 EUR sA und Feststellung (Streitinteresse: 10.000 EUR), über die Revisionen der klagenden, der erstbeklagten und der zweitbeklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Jänner 2011, GZ 4 R 250/10m-85, womit infolge der Berufungen der klagenden, der erstbeklagten und der zweitbeklagten Partei das Urteil des Landesgerichts Innsbruck vom 25. August 2010, GZ 5 Cg 160/08w-74, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Sämtliche Revisionen werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Glöckler Daten AG` | `Glöckler Daten AG` |

**Missed by this rule (FN):**

- `Arbeiterstrandbadstraße 492, 8680 Pernreit, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob33_15y`) (sent_id: `deanon_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Inn Sudconkraft AG, Elisabeth Breitschwerdt, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Mazik Heizung GmbH, Hemma Rahn, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Inn Sudconkraft AG` — partial — gold is substring of pred: `Inn Sudconkraft AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Sudconkraft AG`(organisation)
- `Elisabeth Breitschwerdt`(person)
- `Mazik Heizung GmbH`(organisation)
- `Hemma Rahn`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_7`)


Der Fonds wurde von einer in Deutschland ansässigen AG aufgelegt.

**False Positives:**

- `Der Fonds wurde von einer in Deutschland ansässigen AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Dr. Wurdinger als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Steger, Mag. Wessely-Kristöfel, Dr. Parzmayr und Dr. Pfurtscheller als weitere Richterinnen und Richter in der Rechtssache der klagenden Partei Bundeskammer für Arbeiter und Angestellte, Wien 4, Prinz-Eugen-Straße 20–22, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Alsynwald-Recycling AG, RgR Mag. Dr. Evelyn Steinkröger, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH in Wien, wegen Unterlassung und Urteilsveröffentlichung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. Juli 2024, GZ 2 R 77/24v-15, mit dem das Urteil des Handelsgerichts Wien vom 28. Februar 2024, GZ 57 Cg 36/23d-8, bestätigt wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Recycling AG` — partial — pred is substring of gold: `Alsynwald-Recycling AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alsynwald-Recycling AG`(organisation)
- `RgR Mag. Dr. Evelyn Steinkröger`(person)

**Example 3** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_116`)


Die Nieder Norber AG wird den Kunden in der Mitteilung auf die Änderungen hinweisen und darauf aufmerksam machen, dass sein Stillschweigen nach Ablauf der zwei Monate ab Zugang der Mitteilung durch das Unterlassen eines Widerspruchs in Schriftform als Zustimmung zu den Änderungen gilt.

**False Positives:**

- `Die Nieder Norber AG` — partial — gold is substring of pred: `Nieder Norber AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Norber AG`(organisation)

**Example 4** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_117`)


Außerdem wird die Valwalduni-Handel AG eine Gegenüberstellung über die von der Änderung betroffenen Bestimmungen sowie die vollständige Fassung der neuen Bedingungen auf ihrer Internetseite veröffentlichen und die Gegenüberstellung dem Kunden auf sein Verlangen zur Verfügung stellen;

**False Positives:**

- `Außerdem wird die Valwalduni-Handel AG` — partial — gold is substring of pred: `Valwalduni-Handel AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Valwalduni-Handel AG`(organisation)

**Example 5** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_118`)


auch darauf wird die Landwerlin&Plumke Versand AG in derMitteilung hinweisen.

**False Positives:**

- `Plumke Versand AG` — partial — pred is substring of gold: `Landwerlin&Plumke Versand AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landwerlin&Plumke Versand AG`(organisation)

**Example 6** (doc_id: `deanon_TRAIN/1Ob226_20x`) (sent_id: `deanon_TRAIN/1Ob226_20x_54`)


C-620/17,Hochtief Solutions AG, Rn 35, jeweils mwN).

**False Positives:**

- `Hochtief Solutions AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_11`)


Denn die Beweisthemen (Geschäftsgrundlage der eingangs genannten Vereinbarung vom 11. Dezember 2012 mit der Süd-Immobilien AG; von derselben intendierte Verwertung der Liegenschaften in Draskovichgasse 12, 8240 Friedberg, Österreich durch Zwangsversteigerung ungeachtet eines allfälligen Abverkaufs von Liegenschaften in Steghof 15, 4891 Höhenwarth, Österreich ; Auftrag der Mandanten des Disziplinarbeschuldigten zur Zurückziehung des Antrags auf Aufhebung der Höfeeigenschaft;

**False Positives:**

- `Geschäftsgrundlage der eingangs genannten Vereinbarung vom 11. Dezember 2012 mit der Süd-Immobilien AG` — partial — gold is substring of pred: `Süd-Immobilien AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Süd-Immobilien AG`(organisation)
- `Draskovichgasse 12, 8240 Friedberg, Österreich`(address)
- `Steghof 15, 4891 Höhenwarth, Österreich`(address)

**Example 8** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_12`)


Unkenntnis des Disziplinarbeschuldigten von den Gründen der Daten Unizorstein AG für die beantragte Fortsetzung der Zwangsversteigerungsverfahren;

**False Positives:**

- `Unkenntnis des Disziplinarbeschuldigten von den Gründen der Daten Unizorstein AG` — partial — gold is substring of pred: `Daten Unizorstein AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Daten Unizorstein AG`(organisation)

**Example 9** (doc_id: `deanon_TRAIN/4Ob165_09g`) (sent_id: `deanon_TRAIN/4Ob165_09g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Schenk als Vorsitzende sowie die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Donostzor-Software AG, Florian Gretenkordt, vertreten durch Ewald Weninger Rechtsanwalts GmbH in Wien, gegen die beklagte Partei WienDigital Planung AG, KzlR Volker Chang, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Feststellung und Anfechtung (Streitwert: 101.000.000 EUR), im Verfahren über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Juni 2009, GZ 5 R 44/09s-15, womit das Urteil des Handelsgerichts Wien vom 26. Jänner 2008, GZ 19 Cg 98/08w-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Zurückziehung der außerordentlichen Revision der klagenden Partei dient zur Kenntnis.

**False Positives:**

- `Software AG` — partial — pred is substring of gold: `Donostzor-Software AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Donostzor-Software AG`(organisation)
- `Florian Gretenkordt`(person)
- `WienDigital Planung AG`(organisation)
- `KzlR Volker Chang`(person)

**Example 10** (doc_id: `deanon_TRAIN/5Ob141_23f`) (sent_id: `deanon_TRAIN/5Ob141_23f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei OMedR Univ.-Prof.in Eugenia Breitenfelder, vertreten durch Poduschka Partner AnwaltsGmbH in Linz, gegen die beklagte Partei Werkfurtval-Lebensmittel AG, Meinrad Birkenmeyer, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 19.600 EUR sA über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 22. Mai 2023, GZ 12 R 6/23y-34, mit dem das Urteil des Landesgerichts Wels vom 11. Jänner 2023, GZ 8 Cg 29/20s-29, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Lebensmittel AG` — partial — pred is substring of gold: `Werkfurtval-Lebensmittel AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OMedR Univ.-Prof.in Eugenia Breitenfelder`(person)
- `Werkfurtval-Lebensmittel AG`(organisation)
- `Meinrad Birkenmeyer`(person)

**Example 11** (doc_id: `deanon_TRAIN/5Ob141_23f`) (sent_id: `deanon_TRAIN/5Ob141_23f_17`)


Ende des Jahres 2018 schloss er sich der deutschen Musterfeststellungsklage gegen die Conkraftnor-Event AG an.

**False Positives:**

- `Ende des Jahres 2018 schloss er sich der deutschen Musterfeststellungsklage gegen die Conkraftnor-Event AG` — partial — gold is substring of pred: `Conkraftnor-Event AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Conkraftnor-Event AG`(organisation)

**Example 12** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_31`)


Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG wäre hinsichtlich § 14 Abs 3 FBG sachlich nicht gerechtfertigt.

**False Positives:**

- `Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_66`)


Die Bestimmung sei daher analog auch auf gemeinnützige Bauvereinigungen in der Rechtsform der GmbH oder AG anzuwenden.

**False Positives:**

- `Die Bestimmung sei daher analog auch auf gemeinnützige Bauvereinigungen in der Rechtsform der GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_107`)


Wenn nun kraft ausdrücklicher gesetzlicher Vorschrift gemeinnützige Bauvereinigungen auch in den Rechtsformen einer GmbH oder AG erlaubt sind (§ 1 Abs 1 WGG) und gleichzeitig auch für diese die Pflicht statuiert wird, einem Revisionsverband anzugehören (§ 5 Abs 1 WGG), so ist auch für eine in der Rechtsform einer GmbH oder AG bestehende Bauvereinigung der Revisionsverband als „zuständig“ im Sinn von § 14 Abs 3 FBG und demgemäß insoweit als Amtspartei anzusehen.

**False Positives:**

- `Wenn nun kraft ausdrücklicher gesetzlicher Vorschrift gemeinnützige Bauvereinigungen auch in den Rechtsformen einer GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_111`)


Es muss daher davon ausgegangen werden, dass sowohl der Gesetzgeber des FBG als auch der mehrfache (Novellen-)Gesetzgeber des WGG die Zuständigkeit des Revisionsverbands für Bauvereinigungen in der Rechtsform einer GmbH oder AG übersehen hat.

**False Positives:**

- `Gesetzgeber des WGG die Zuständigkeit des Revisionsverbands für Bauvereinigungen in der Rechtsform einer GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_TRAIN/6Ob36_20t`) (sent_id: `deanon_TRAIN/6Ob36_20t_140`)


Der EuGH teilte die von einigen Mitgliedstaaten (darunter auch Österreich) geäußerte Rechtsansicht, eine Befristung des Widerrufsrechts sei aus Gründen der Rechtssicherheit unerlässlich, nicht (EuGH C-481/99 [Georg und Helga Heininger/Bayerische Hypo- und Vereinsbank AG]).

**False Positives:**

- `Bayerische Hypo- und Vereinsbank AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_TRAIN/6Ob47_25t`) (sent_id: `deanon_TRAIN/6Ob47_25t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Hofer-Zeni-Rennhofer als Vorsitzende sowie die Hofrätinnen und Hofräte Dr. Faber, Mag. Pertmayr, Dr. Weber und Mag. Nigl LL.M. als weitere Richter in der Rechtssache der klagenden Partei Timothy Scheppan, vertreten durch Dr. Alexander Amann LL.M., Rechtsanwalt in Gamprin-Bendern, Liechtenstein, wider die beklagte Partei Nord-Luftfahrt AG, Niklas Kühlewind, Deutschland, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 71.888,75 EUR sA Zug um Zug gegen die Rückstellung eines Fahrzeugs, in eventu wegen 17.972,19 EUR sA und Feststellung, im Verfahren über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Jänner 2025, GZ 11 R 7/25t-63, den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Luftfahrt AG` — partial — pred is substring of gold: `Nord-Luftfahrt AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Timothy Scheppan`(person)
- `Nord-Luftfahrt AG`(organisation)
- `Niklas Kühlewind`(person)

**Example 18** (doc_id: `deanon_TRAIN/7Ob85_15y`) (sent_id: `deanon_TRAIN/7Ob85_15y_4`)


Cynthia Martchenko AG, Schmidhuberstraße 73, 4792 Landertsberg, Österreich, vertreten durch Jank Weiler Operenyi Rechtsanwälte OG in Wien, 2. Reisch + Weißert Getränke AG und 3.

**False Positives:**

- `Cynthia Martchenko AG` — partial — gold is substring of pred: `Cynthia Martchenko`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Cynthia Martchenko`(person)
- `Schmidhuberstraße 73, 4792 Landertsberg, Österreich`(address)
- `Reisch + Weißert Getränke AG`(organisation)

**Example 19** (doc_id: `deanon_TRAIN/8Ob121_22k`) (sent_id: `deanon_TRAIN/8Ob121_22k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn und die Hofräte Dr. Stefula und Dr. Thunhart in der Rechtssache der klagenden Partei Roettgermann + Soldmann Heizung AG, Theophil Bings, vertreten durch die Schönherr Rechtsanwälte GmbH in Wien, gegen die beklagte Partei ÖkR Christoph Adamske Privatstiftung,*, vertreten durch Dr. Felix Michael Klement, Rechtsanwalt in Wien, wegen 1.500.000 USD sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien vom 28. April 2022, GZ 2 R 133/21z-42, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn und die Hofräte Dr. Stefula und Dr. Thunhart in der Rechtssache der klagenden Partei Roettgermann + Soldmann Heizung AG` — partial — gold is substring of pred: `Roettgermann + Soldmann Heizung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Roettgermann + Soldmann Heizung AG`(organisation)
- `Theophil Bings`(person)
- `ÖkR Christoph Adamske`(person)

**Example 20** (doc_id: `deanon_TRAIN/8Ob35_23i`) (sent_id: `deanon_TRAIN/8Ob35_23i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn und die Hofräte Dr. Stefula und Dr. Thunhart in der Rechtssache der klagenden Parteien 1. Pflege Deruni, und 2. Marchesi+Kusnezow Transport AG, Grabenseeweg 48, 8272 Ebersdorf, Österreich, beide vertreten durch Dr. Heinrich Fassl, Rechtsanwalt in Wien, wider die beklagte Partei DI Valerie Wilczenski, vertreten durch Dr. Andreas A. Lintl, Rechtsanwalt in Wien, wegen 59.868,50 EUR sA und 170.440,94 EUR sA, über die Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Wien vom 26. Jänner 2023, GZ 11 R 235/22t-206, mit welchem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 30. Mai 2022, GZ 20 Cg 11/15g-194, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Kusnezow Transport AG` — partial — pred is substring of gold: `Marchesi+Kusnezow Transport AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Pflege Deruni`(organisation)
- `Marchesi+Kusnezow Transport AG`(organisation)
- `Grabenseeweg 48, 8272 Ebersdorf, Österreich`(address)
- `DI Valerie Wilczenski`(person)

**Example 21** (doc_id: `deanon_TRAIN/8Ob39_24d`) (sent_id: `deanon_TRAIN/8Ob39_24d_9`)


Hätte sie pflichtgemäß gehandelt und den von ihr geprüften Jahresabschlüssen den Bestätigungsvermerk versagt, hätte er die Aktien nicht gekauft und damit – wegen der kurz nach seinen Käufen von der Nieder-Analyse Solutions AG beantragten Insolvenzeröffnung – keinen Schaden erlitten.

**False Positives:**

- `Analyse Solutions AG` — partial — pred is substring of gold: `Nieder-Analyse Solutions AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder-Analyse Solutions AG`(organisation)

**Example 22** (doc_id: `deanon_TRAIN/8Ob39_24d`) (sent_id: `deanon_TRAIN/8Ob39_24d_13`)


Die West Heimwaldstein Solutions AG habe insofern auch Offenlegungspflichten in Österreich getroffen.

**False Positives:**

- `Die West Heimwaldstein Solutions AG` — partial — gold is substring of pred: `West Heimwaldstein Solutions AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `West Heimwaldstein Solutions AG`(organisation)

**Example 23** (doc_id: `deanon_TRAIN/8Ob39_24d`) (sent_id: `deanon_TRAIN/8Ob39_24d_14`)


Als Abschlussprüferin einer international notierten und in Österreich gehandelten AG habe die Beklagte vorhersehen müssen, dass sie in Folge eines unrichtigen Bestätigungsvermerks auch in Österreich verklagt werden könnte.

**False Positives:**

- `Als Abschlussprüferin einer international notierten und in Österreich gehandelten AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_TRAIN/8Ob41_17p`) (sent_id: `deanon_TRAIN/8Ob41_17p_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Vizepräsidenten des Obersten Gerichtshofs Prof. Dr. Spenling als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner, den Hofrat Dr. Brenn und die Hofrätinnen Mag. Korn und Dr. Weixelbraun-Mohr als weitere Richter in der Rechtssache der klagenden Partei TraunMöbel AG, Zlatan Löbbe, vertreten durch Dr. Christoph Ganahl, Rechtsanwalt in Dornbirn, gegen die beklagte Partei Miklos Dargatsch, vertreten durch die Welte Rechtsanwalt GmbH in Rankweil, wegen 106.586,06 EUR sA, über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Innsbruck als Berufungsgericht vom 2. März 2017, GZ 2 R 21/17f-16, mit dem das Urteil des Landesgerichts Feldkirch vom 12. Jänner 2017, GZ 8 Cg 101/16d-12, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Mohr als weitere Richter in der Rechtssache der klagenden Partei TraunMöbel AG` — partial — gold is substring of pred: `TraunMöbel AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `TraunMöbel AG`(organisation)
- `Zlatan Löbbe`(person)
- `Miklos Dargatsch`(person)

**Example 25** (doc_id: `deanon_TRAIN/9Ob68_22y`) (sent_id: `deanon_TRAIN/9Ob68_22y_111`)


Bei der gebotenen objektiven Betrachtung läge in der Mitwirkung der VW AG an der Verbesserung der Beklagten grundsätzlich noch kein ausreichender Grund für die Unzumutbarkeit des primären Gewährleistungsbehelfs, allerdings habe der Kläger auch negative Auswirkungen des für seinen Fahrzeugtyp entwickelten Software-Updates behauptet.

**False Positives:**

- `Bei der gebotenen objektiven Betrachtung läge in der Mitwirkung der VW AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Limited_Suffix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches entities ending with 'Limited', ensuring the name part is captured correctly and excluding titles like 'Partei'.

**Content:**
```
(?<![A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s])(?<![A-Z])([A-Z][A-Za-z0-9\s\.\-\+&]*?[A-Za-z0-9])\s+Limited\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 268 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/1Ob171_22m`) (sent_id: `deanon_TRAIN/1Ob171_22m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Musger als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Leonie Dommke, vertreten durch Mag. Klaus Mayer, Rechtsanwalt in Premstätten, gegen die beklagte Partei Grashuber+Kovatchev Immobilien Limited, Elisabeth Hallmanns, vertreten durch Dr. Fabian Maschke, Rechtsanwalt in Wien, wegen 36.070 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 3. August 2022, GZ 4 R 98/22x-24, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Kovatchev Immobilien Limited` — partial — pred is substring of gold: `Grashuber+Kovatchev Immobilien Limited`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Leonie Dommke`(person)
- `Grashuber+Kovatchev Immobilien Limited`(organisation)
- `Elisabeth Hallmanns`(person)

**Example 1** (doc_id: `deanon_TRAIN/8Ob31_24b`) (sent_id: `deanon_TRAIN/8Ob31_24b_4`)


Matzka, Dr. Stefula, Dr. Thunhart und Mag. Dr. Sengstschmid als weitere Richter in der Rechtssache der klagenden Partei Arnold Uhlemeier, LLM, vertreten durch Mag. Alexander Tupy, Rechtsanwalt in Wien, gegen die beklagte Partei Lemwilbruck-Marine Limited, Nadja Buhrfeindt, Malta, vertreten durch Mag. Marcus Marakovics, Rechtsanwalt in Wien, wegen 18.842,85 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Dezember 2023, GZ 11 R 284/23z-19, mit dem der Berufung der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 16. Oktober 2023, GZ 17 Cg 26/23b-11, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision der beklagten Partei wird zurückgewiesen.

**False Positives:**

- `Marine Limited` — partial — pred is substring of gold: `Lemwilbruck-Marine Limited`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Arnold Uhlemeier, LLM`(person)
- `Lemwilbruck-Marine Limited`(organisation)
- `Nadja Buhrfeindt`(person)

</details>

---

## `Ges_m_b_H_Suffix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches entities ending with 'Ges.m.b.H.' or 'GmbH & Co KG' (partial match for the main name).

**Content:**
```
(?<![A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s])(?<![A-Z])([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)?)\s+Ges\.m\.b\.H\.
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `GmbH_Co_KG_Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches entities ending with 'GmbH & Co KG' to capture the full name, ensuring the name part is captured correctly.

**Content:**
```
\b([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s\.\-\+&]*?[A-Za-z0-9])\s+GmbH\s+&\s+Co\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 22 | 0 | 22 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 22 | 318 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob19_25d`) (sent_id: `deanon_TRAIN/10Ob19_25d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober, Dr. Annerl, Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Ernestine Feifel, vertreten durch die Salburg Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Jean Kandziora, vertreten durch die BEURLE Rechtsanwälte GmbH & Co KG in Linz, wegen Feststellung (Streitwert 5.100 EUR), über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 19. Dezember 2024, GZ 1 R 255/24f-28, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 31. Mai 2024, GZ 15 C 939/23d-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `BEURLE Rechtsanwälte GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ernestine Feifel`(person)
- `Jean Kandziora`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_4`)


Energie Conwald GmbH & Co KG und 2.

**False Positives:**

- `Energie Conwald GmbH & Co KG` — partial — gold is substring of pred: `Energie Conwald GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Energie Conwald GmbH`(organisation)

**Example 2** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_5`)


Text Begründung: Der Kläger erwarb im Jahr 2004 als Verbraucher über Vermittlung eines Wertpapierdienstleistungsunternehmens Kommanditanteile an der Contra GmbH & Co KG im Nominale von 20.000 EUR zuzüglich 1.000 EUR Agio.

**False Positives:**

- `Verbraucher über Vermittlung eines Wertpapierdienstleistungsunternehmens Kommanditanteile an der Contra GmbH & Co KG` — partial — gold is substring of pred: `Contra GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Contra GmbH`(organisation)

**Example 3** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt, aus denen Erträge erzielt werden sollen.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_5`)


Text Begründung: Der Kläger erwarb als Verbraucher im Juni 2003 über Vermittlung eines selbständigen Vermögensberaters Kommanditanteile an der Bestelmeyer+Keßelheim Software GmbH & Co KG im Nominale von 17.000 EUR zuzüglich 850 EUR Agio.

**False Positives:**

- `Vermittlung eines selbständigen Vermögensberaters Kommanditanteile an der Bestelmeyer+Keßelheim Software GmbH & Co KG` — partial — gold is substring of pred: `Bestelmeyer+Keßelheim Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bestelmeyer+Keßelheim Software GmbH`(organisation)

**Example 5** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/1Ob16_20i`) (sent_id: `deanon_TRAIN/1Ob16_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Stadt Christina Schorer, vertreten durch die Benn-Ibler Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Donsteinlex AG, Natalie Gieseking, MSc, vertreten durch die Weber Rechtsanwälte GmbH & Co KG, Wien, wegen 312.706,88 EUR sowie Feststellung (Streitwert 80.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Oktober 2019, GZ 6 R 71/19g-17, mit dem das Urteil des Landesgerichts Steyr vom 29. März 2019, GZ 9 Cg 39/18g-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Weber Rechtsanwälte GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Christina Schorer`(person)
- `Donsteinlex AG`(organisation)
- `Natalie Gieseking, MSc`(person)

**Example 7** (doc_id: `deanon_TRAIN/1Ob197_18d`) (sent_id: `deanon_TRAIN/1Ob197_18d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Volze KI GmbH & Co KG, Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich, vertreten durch Dr. Klaus-Dieter Strobach und andere Rechtsanwälte, Grieskirchen, gegen die beklagte Partei Land Oberösterreich, Linz, Landhausplatz 1, vertreten durch Dr. Thomas J. A. Langer, LL.M., Rechtsanwalt in Linz, wegen 475.550,18 EUR sA, über die (außerordentliche) Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2018, GZ 4 R 56/18k-17, mit dem das Urteil des Landesgerichts Wels vom 1. März 2018, GZ 3 Cg 3/16z-13, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Volze KI GmbH & Co KG` — partial — gold is substring of pred: `Volze KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Volze KI GmbH`(organisation)
- `Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich`(address)

**Example 8** (doc_id: `deanon_TRAIN/2Ob193_23f`) (sent_id: `deanon_TRAIN/2Ob193_23f_5`)


Kff. Magdalena Münsterberg, vertreten durch Weber Rechtsanwälte GmbH & Co KG in Wien 1, gegen die beklagte Partei Gisela Ammenn, vertreten durch BEURLE Rechtsanwälte GmbH & Co KG in Linz, wegen Herausgabe (Streitwert 1.525.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2023, GZ 2 R 87/23m-32, mit dem das Urteil des Landesgerichts Salzburg vom 5. April 2023, GZ 8 Cg 9/23a-22, aufgehoben wurde zu Recht erkannt:  Spruch

**False Positives:**

- `Weber Rechtsanwälte GmbH & Co KG` — no gold match — likely missing annotation
- `BEURLE Rechtsanwälte GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Gisela Ammenn`(person)

**Example 9** (doc_id: `deanon_TRAIN/3Ob209_21p`) (sent_id: `deanon_TRAIN/3Ob209_21p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Nexostlem GmbH & Co KG, Rehlackenweg 5G, 8451 Pernitsch, Österreich, vertreten durch DDr. Heinz Dietmar Schimanko, Rechtsanwalt in Wien, gegen die beklagte Partei RheinLandwirtschaft Vertrieb GmbH, Klaus Dissler, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH & Co KG in Wien, wegen 7.906,82 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 7. Juni 2021, GZ 38 R 66/21v-16, mit dem das Urteil des Bezirksgerichts Favoriten vom 19. Jänner 2021, GZ 3 C 503/20f-12, abgeändert wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Nexostlem GmbH & Co KG` — partial — gold is substring of pred: `Nexostlem GmbH`
- `Bichler Zrzavy Rechtsanwälte GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Nexostlem GmbH`(organisation)
- `Rehlackenweg 5G, 8451 Pernitsch, Österreich`(address)
- `RheinLandwirtschaft Vertrieb GmbH`(organisation)
- `Klaus Dissler`(person)

**Example 10** (doc_id: `deanon_TRAIN/3Ob223_19v`) (sent_id: `deanon_TRAIN/3Ob223_19v_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Priv.-Doz. Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr, Dr. Kodek und Mag. Wessely-Kristöfel als weitere Richter in der Exekutionssache der betreibenden Partei Özbolat Forschung GesmbH, KommR James Anthis, vertreten durch Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG in Wien, gegen die verpflichtete Partei Dkfm.

**False Positives:**

- `In der Maur & Partner Rechtsanwälte GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Özbolat Forschung GesmbH`(organisation)
- `KommR James Anthis`(person)

**Example 11** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_5`)


Klingenbeil Versand GmbH & Co KG, 2.

**False Positives:**

- `Klingenbeil Versand GmbH & Co KG` — partial — gold is substring of pred: `Klingenbeil Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Klingenbeil Versand GmbH`(organisation)

**Example 12** (doc_id: `deanon_TRAIN/5Ob146_16f`) (sent_id: `deanon_TRAIN/5Ob146_16f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers Mag. Niels Mueter, vertreten durch Dr. Anke Reisch, Rechtsanwältin in Kitzbühel, gegen die Antragsgegnerin Talgart-Chemie GmbH & Co KG, Tiefe Gasse 5, 2061 Obritz, Österreich, vertreten durch Dr. Lisbeth Lass und Dr. Hans Christian Lass, Rechtsanwälte in Innsbruck, wegen § 52 Abs 1 Z 6 iVm § 20 Abs 3 WEG 2002, infolge des „außerordentlichen“ Revisionsrekurses des Antragstellers gegen den (richtig) Sachbeschluss des Landesgerichts Innsbruck vom 24. Mai 2016, GZ 4 R 128/16a-50, mit dem der Sachbeschluss des Bezirksgerichts Kitzbühel vom 14. März 2016, GZ 4 Msch 7/14x-36, abgeändert wurde, den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.

**False Positives:**

- `Antragsgegnerin Talgart-Chemie GmbH & Co KG` — partial — gold is substring of pred: `Talgart-Chemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Niels Mueter`(person)
- `Talgart-Chemie GmbH`(organisation)
- `Tiefe Gasse 5, 2061 Obritz, Österreich`(address)

**Example 13** (doc_id: `deanon_TRAIN/5Ob206_24s`) (sent_id: `deanon_TRAIN/5Ob206_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Painsi, Dr. Weixelbraun-Mohr, Dr. Steger und Dr. Pfurtscheller als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers OMedR Louisa Dutzke, vertreten durch Mag. Wolfgang Doppelhofer LL.M. LL.M., Rechtsanwalt in Wien, gegen die Antragsgegnerin Alsud-Pflege GmbH, Kirchenwaldweg 10, 3104 St. Pölten, Österreich, vertreten durch Weishaupt Horak Georgiev Rechtsanwälte GmbH & Co KG in Wien, wegen Feststellung der Ausstattungskategorie nach § 15a MRG, über den Revisionsrekurs der Antragsgegnerin gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 26. August 2024, GZ 39 R 144/24a-22, mit dem der Sachbeschluss des Bezirksgerichts Hietzing vom 29. Mai 2024, GZ 9 MSch 18/23k-18, aufgehoben wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Weishaupt Horak Georgiev Rechtsanwälte GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OMedR Louisa Dutzke`(person)
- `Alsud-Pflege GmbH`(organisation)
- `Kirchenwaldweg 10, 3104 St. Pölten, Österreich`(address)

**Example 14** (doc_id: `deanon_TRAIN/5Ob71_24p`) (sent_id: `deanon_TRAIN/5Ob71_24p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Mag. Wurzer als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Painsi, Dr. Weixelbraun-Mohr, Dr. Steger und Dr. Pfurtscheller als weitere Richter in der Rechtssache der klagenden Partei Ignaz Schaufel, vertreten durch die Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Mur Waldbach GmbH, StR Martin Leitenbauer, vertreten durch die Wolf Theiss Rechtsanwälte GmbH & Co KG in Wien, wegen 7.140 EUR und Feststellung (Streitwert 2.000 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Steyr als Berufungsgericht vom 8. Februar 2024, GZ 1 R 120/23z-43, mit dem das Urteil des Bezirksgerichts Steyr vom 28. September 2023, GZ 2 C 288/21x-39, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das Verfahren über die Revision der beklagten Partei wird bis zur Entscheidung des Gerichtshofs der Europäischen Union (EuGH) über die Vorabentscheidungsersuchen des Landgerichts Ravensburg (Deutschland) vom 9. November 2023, Rechtssache C-666/23, vom 9. November 2023, Rechtssache C-667/23, und vom 15. November 2023, Rechtssache C-668/23, unterbrochen.

**False Positives:**

- `Wolf Theiss Rechtsanwälte GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ignaz Schaufel`(person)
- `Mur Waldbach GmbH`(organisation)
- `StR Martin Leitenbauer`(person)

**Example 15** (doc_id: `deanon_TRAIN/6Ob146_18s`) (sent_id: `deanon_TRAIN/6Ob146_18s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden und die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny sowie die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Paolo Weinrich, vertreten durch Mag. Max Verdino und andere Rechtsanwälte in St. Veit an der Glan, gegen die beklagte Partei Oberüber&Spanjardt Landwirtschaft GmbH, Karola Löcke, vertreten durch PHH Prochaska Havranek Rechtsanwälte GmbH & Co KG in Wien, wegen 18.664,48 EUR und Feststellung, über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 6. Juni 2018, GZ 4 R 51/18d-12, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Klagenfurt vom 20. Februar 2018, GZ 28 Cg 75/17s-8, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `PHH Prochaska Havranek Rechtsanwälte GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Paolo Weinrich`(person)
- `Oberüber&Spanjardt Landwirtschaft GmbH`(organisation)
- `Karola Löcke`(person)

**Example 16** (doc_id: `deanon_TRAIN/8Ob60_12z`) (sent_id: `deanon_TRAIN/8Ob60_12z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner sowie die Hofräte Mag. Ziegelbauer und Dr. Brenn als weitere Richter in der Rechtssache der klagenden Partei Arabella Witkopf, vertreten durch Mag. Renate Aigner, Rechtsanwältin in Kallham, gegen die beklagte Partei Abramczyk & Krollpfeifer Wind GmbH & Co KG, Pühra 22, 8010 Edelsbach bei Graz, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen (Revisionsinteresse) 10.000 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 15. März 2012, GZ 3 R 42/12k-38, womit das Urteil des Landesgerichts Linz vom 28. Dezember 2011, GZ 1 Cg 167/10i-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Partei Abramczyk & Krollpfeifer Wind GmbH & Co KG` — partial — gold is substring of pred: `Abramczyk & Krollpfeifer Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Arabella Witkopf`(person)
- `Abramczyk & Krollpfeifer Wind GmbH`(organisation)
- `Pühra 22, 8010 Edelsbach bei Graz, Österreich`(address)

**Example 17** (doc_id: `deanon_TRAIN/9Ob58_20z`) (sent_id: `deanon_TRAIN/9Ob58_20z_6`)


Die Beklagte ist eine Treuhandgesellschaft mit Sitz in Deutschland und Gründungskommanditistin einer deutschen GmbH & Co KG, deren Geschäftsgegenstand die Beteiligung an nicht börsenotierten Kapitalgesellschaften ist, die unter anderem Grundstücke entwickeln und verwalten.

**False Positives:**

- `Die Beklagte ist eine Treuhandgesellschaft mit Sitz in Deutschland und Gründungskommanditistin einer deutschen GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_TRAIN/9Ob58_20z`) (sent_id: `deanon_TRAIN/9Ob58_20z_48`)


Nach den Feststellungen sollte sich der Kläger als Treugeber über die Beklagte an einer GmbH & Co KG beteiligen, welche wiederum bis zu 90 % der Anteile an einer Kapitalgesellschaft in den VAE erwerben sollte.

**False Positives:**

- `Nach den Feststellungen sollte sich der Kläger als Treugeber über die Beklagte an einer GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_TRAIN/9Ob68_22y`) (sent_id: `deanon_TRAIN/9Ob68_22y_4`)


Sloboda und Dr. Annerl in der Rechtssache der klagenden Partei Angelika Blochinger, vertreten durch Neubauer Fähnrich Rechtsanwälte GmbH & Co KG in Graz, gegen die beklagte Partei Laurence Klüs Gesellschaft m.b.H. (FN FN026367d ), FN434768w, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung und 19.490 EUR sA (Gesamtstreitwert: 19.490 EUR), über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 10. September 2019, GZ 4 R 89/19v-59, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 27. März 2019, GZ 20 Cg 15/18t-54, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Revisionsverfahren wird fortgesetzt.

**False Positives:**

- `Neubauer Fähnrich Rechtsanwälte GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Angelika Blochinger`(person)
- `Laurence Klüs`(person)
- `FN026367d`(business_register_number)
- `FN434768w`(business_register_number)

</details>

---

## `Gesellschaft_m_b_H_Spaces`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches entities ending with 'Gesellschaft mbH' (with spaces) to capture names like 'WestTrikelLandwirtschaft Institut Gesellschaft mbH'.

**Content:**
```
(?<![A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s])(?<![A-Z])([A-Z][A-Za-z0-9\s\.\-\+&]*?[A-Za-z0-9])\s+Gesellschaft\s+mbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 1 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/9ObA96_13b`) (sent_id: `deanon_TRAIN/9ObA96_13b_4`)


Brigitte Augustin und Mag. Andreas Hach als weitere Richter in der Arbeitsrechtssache der klagenden Partei DI Anita Crämer, vertreten durch Dr. Gerhard Hiebler und Dr. Gerd Grebenjak, Rechtsanwälte in Leoben, gegen die beklagte Partei, GQG E‑Commerce Gesellschaft mbH, Franz-Cäsar-Weg 5, 4115 Gumpesberg, Österreich, vertreten durch Siemer-Siegel-Füreder & Partner, Rechtsanwälte in Wien, wegen Feststellung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 18. April 2013, GZ 6 Ra 18/13h-10, mit dem der Berufung der beklagten Partei gegen das Urteil des Landesgerichts Leoben als Arbeits- und Sozialgericht vom 7. November 2012, GZ 23 Cga 115/12x-6, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Commerce Gesellschaft mbH` — partial — pred is substring of gold: `GQG E‑Commerce Gesellschaft mbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DI Anita Crämer`(person)
- `GQG E‑Commerce Gesellschaft mbH`(organisation)
- `Franz-Cäsar-Weg 5, 4115 Gumpesberg, Österreich`(address)

</details>

---

## `Aktiengesellschaft_Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches entities ending with 'Aktiengesellschaft' (full word).

**Content:**
```
(?<![A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s])(?<![A-Z])([A-Z][A-Za-z0-9\s\.\-\+&]*?[A-Za-z0-9])\s+Aktiengesellschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 6 | 0 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 6 | 345 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_5`)


Sie habe im Jahr 2012 mit einer Aktiengesellschaft einen Ansparplan abgeschlossen.

**False Positives:**

- `Sie habe im Jahr 2012 mit einer Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_6`)


Die Aktiengesellschaft habe damit geworben, mit den eingezahlten Beträgen Edelmetalle zu marktüblichen Preisen zu erwerben, zu lagern und zu verwalten und habe dem Beklagten in dessen Funktion als Rechtsanwalt und öffentlicher Notar den Auftrag erteilt, jährliche Prüfberichte über den vollständigen Bestand zu erstellen.

**False Positives:**

- `Die Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/1Ob140_14s`) (sent_id: `deanon_TRAIN/1Ob140_14s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer und Mag. Dr. Wurdinger sowie die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft, Meidlinger Hauptstraße 19, 5233 Erlach, Österreich, vertreten durch die Walch & Zehetbauer Rechtsanwälte OG, Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 344.011,19 EUR und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Juni 2014, GZ 4 R 202/13g-54, mit dem das Teilzwischenurteil des Landesgerichts Feldkirch vom 2. August 2013, GZ 8 Cg 143/11y-46, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

**False Positives:**

- `Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft` — partial — gold is substring of pred: `Tracondon Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tracondon Aktiengesellschaft`(organisation)
- `Meidlinger Hauptstraße 19, 5233 Erlach, Österreich`(address)

**Example 3** (doc_id: `deanon_TRAIN/1Ob9_22p`) (sent_id: `deanon_TRAIN/1Ob9_22p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. HR Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Parteien 1. Mag. Tosca Xyländer und 2. Mag. Heinrich Vlachojannis, vertreten durch die Koch Jilek Rechtsanwälte Partnerschaft, Bruck an der Mur, gegen die beklagte Partei Grüttemann E‑Commerce Aktiengesellschaft, Friedhof Döbling 165, 8401 Abtissendorf, Österreich, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH, Wien, wegen 40.358,88 EUR sA, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. November 2021, GZ 5 R 163/21h-43, mit dem das Urteil des Handelsgerichts Wien vom 31. August 2021, GZ 55 Cg 60/20i-36, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Commerce Aktiengesellschaft` — partial — pred is substring of gold: `Grüttemann E‑Commerce Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Tosca Xyländer`(person)
- `Mag. Heinrich Vlachojannis`(person)
- `Grüttemann E‑Commerce Aktiengesellschaft`(organisation)
- `Friedhof Döbling 165, 8401 Abtissendorf, Österreich`(address)

**Example 4** (doc_id: `deanon_TRAIN/3Ob17_20a`) (sent_id: `deanon_TRAIN/3Ob17_20a_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie die Hofräte Priv.-Doz. Dr. Rassi und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Exekutionssache betreibenden Partei Heizung Werkuni Aktiengesellschaft, P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich, vertreten durch Dr. Roland Grilc ua, Rechtsanwälte in Klagenfurt am Wörthersee, gegen die verpflichtete Partei Dorothea Eiken Bank, Peter Eitenmüller, vertreten durch Diwok Hermann Petsche Rechtsanwälte LLP Co KG in Wien, wegen 12.602.980,92 EUR sA, über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. November 2019, GZ 46 R 293/19g-18, mit dem der Beschluss des Bezirksgerichts Favoriten vom 17. April 2019, GZ 17 E 1298/19z-2, bestätigt wurde, den Beschluss gefasst:  Spruch I. Der Revisionsrekurs wird, soweit er sich gegen die Bestätigung der Exekutionsbewilligung richtet, als jedenfalls unzulässig zurückgewiesen.

**False Positives:**

- `Mohr und Dr. Kodek als weitere Richter in der Exekutionssache betreibenden Partei Heizung Werkuni Aktiengesellschaft` — partial — gold is substring of pred: `Heizung Werkuni Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Heizung Werkuni Aktiengesellschaft`(organisation)
- `P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich`(address)
- `Dorothea Eiken`(person)
- `Peter Eitenmüller`(person)

**Example 5** (doc_id: `deanon_TRAIN/4Ob13_17s`) (sent_id: `deanon_TRAIN/4Ob13_17s_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Daten Steinlem Aktiengesellschaft, Inderstadt 17, 2564 Furth, Österreich, vertreten durch die Huber Swoboda Oswald Aixberger Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Muran Fass, vertreten durch Dr. Fabian Maschke, Rechtsanwalt in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert 35.000 EUR), über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Dezember 2016, GZ 2 R 74/16i-24, womit das Urteil des Landesgerichts Ried im Innkreis vom 25. Februar 2016, GZ 5 Cg 191/14m-14, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei Daten Steinlem Aktiengesellschaft` — partial — gold is substring of pred: `Daten Steinlem Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Daten Steinlem Aktiengesellschaft`(organisation)
- `Inderstadt 17, 2564 Furth, Österreich`(address)
- `Muran Fass`(person)

</details>

---

## `Gesellschaft_m_b_H_Lowercase`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches entities ending with 'gesellschaft mbH' (lowercase 'g') to capture names like 'Hoffschroer Sanitär gesellschaft mbH'.

**Content:**
```
(?<![A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s])(?<![A-Z])([A-Z][A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s\.\-\+&]*?[A-Za-z0-9])\s+gesellschaft\s+mbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 178 |

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

</details>

---

## `Industry_NoSuffix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches organisation names ending in industry terms without a legal suffix, excluding 'Aktiengesellschaft' which is handled separately.

**Content:**
```
(?<![A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s])(?<![A-Z])([A-Z][A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)?)\s+(Maschinenbau|Forschung|Robotik|Verlag|Bank|Institut|Gesellschaft|Handel|Planung|Gastronomie|Elektro|Druck|Pflege|Möbel|Event|Vertrieb|Technologie|Technologien)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 10 | 0 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 10 | 208 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/3Ob223_19v`) (sent_id: `deanon_TRAIN/3Ob223_19v_15`)


[Die Bank] und [die Zessionarin] vereinbaren hiermit ausdrücklich, dass auch das solcherart in ein Festbetragspfandrecht (Verkehrshypothek) mit einem Kapitalbetrag in Höhe von 611.255,25 EUR zuzüglich 7,25 %Zinsen aus 520.326,03 EUR und 9,375 % Zinsen aus 90.929,22 EUR ex lege umgewandelte, ob der Liegenschaft […] einverleibte Höchstbetragspfandrecht zugleich mit den zessionsgegenständlichen Forderungen von [der Bank] auf [die Zessionarin] übertragen wird.“

**False Positives:**

- `Die Bank` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/4Ob9_20g`) (sent_id: `deanon_TRAIN/4Ob9_20g_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Ing. KzlR MedR Brunhild Syndikus, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1) Böhnstedt+Bittlmeier Verlag GmbH, Wien Traalmon Betriebe, und 2) TraunBau AG, Schneeballenweg 6, 4232 Penzendorf, Österreich, beide vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 11.091,23 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 6. November 2019, GZ 2 R 158/19x-27, mit dem das Urteil des Landesgerichts Linz vom 29. August 2019, GZ 36 Cg 14/18h-22, bestätigt wurde, den Beschluss gefasst:  Spruch I. Das Revisionsverfahren zu 4 Ob 9/20g wird bis zur Vorabentscheidung des Gerichtshofs der Europäischen Union über das Vorabentscheidungsersuchen des Obersten Gerichtshofs vom 17.

**False Positives:**

- `Bittlmeier Verlag` — partial — pred is substring of gold: `Böhnstedt+Bittlmeier Verlag GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. KzlR MedR Brunhild Syndikus`(person)
- `Böhnstedt+Bittlmeier Verlag GmbH`(organisation)
- `Wien Traalmon Betriebe`(organisation)
- `TraunBau AG`(organisation)
- `Schneeballenweg 6, 4232 Penzendorf, Österreich`(address)

**Example 2** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_28`)


Die Gesellschaft halte 99,99 % der Anteile an der Bauvereinigung;

**False Positives:**

- `Die Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/6Ob2_12f`) (sent_id: `deanon_TRAIN/6Ob2_12f_5`)


Jakubiak Handel GmbH, Rudolf-Kassner-Gasse 42, 5134 Sengthal, Österreich, 2.

**False Positives:**

- `Jakubiak Handel` — partial — pred is substring of gold: `Jakubiak Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jakubiak Handel GmbH`(organisation)
- `Rudolf-Kassner-Gasse 42, 5134 Sengthal, Österreich`(address)

**Example 4** (doc_id: `deanon_TRAIN/7Ob85_15y`) (sent_id: `deanon_TRAIN/7Ob85_15y_5`)


Schefuss Forschung GmbH, beide Raidenstraße 62, 8354 Aigen, Österreich, vertreten durch Dorda Brugger Jordis Rechtsanwälte GmbH in Wien, wegen 7.523,16 EUR sA, über den Rekurs der erstbeklagten Partei gegen den Beschluss des Handelsgerichts Wien als Berufungsgericht vom 19. Februar 2015, GZ 1 R 6/15a-49, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 29. September 2014, GZ 13 C 134/10s-45, hinsichtlich der erstbeklagten Partei aufgehoben wurde, den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Schefuss Forschung` — partial — pred is substring of gold: `Schefuss Forschung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schefuss Forschung GmbH`(organisation)
- `Raidenstraße 62, 8354 Aigen, Österreich`(address)

**Example 5** (doc_id: `deanon_TRAIN/8Ob100_19t`) (sent_id: `deanon_TRAIN/8Ob100_19t_9`)


Der Vertrieb des Fonds erfolgte über die Erstbeklagte und nachgeschaltete Vermittler/Vermögensberater mit Vertriebsvereinbarung zur Erstbeklagten, im Falle des Klägers durch die Zweitbeklagte.

**False Positives:**

- `Der Vertrieb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/8Ob11_11t`) (sent_id: `deanon_TRAIN/8Ob11_11t_169`)


Die Bank verletze ihre Beratungspflicht bereits dann, wenn sie den Kunden nicht auf den bereits zum Abschlusszeitpunkt für ihn negativen Marktwert des Vertrags hinweise, weil der bewusst strukturierte negative Marktwert Ausdruck eines schwerwiegenden Interessenkonflikts sei.

**False Positives:**

- `Die Bank` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/8Ob11_11t`) (sent_id: `deanon_TRAIN/8Ob11_11t_171`)


Die Bank sei jedoch dann aufklärungspflichtig, wenn über das reine Gewinnerzielungsinteresse hinaus besondere Umstände hinzutreten, insbesondere wenn sie die Risikostruktur eines Anlagegeschäfts bewusst zu Lasten des Anlegers gestaltet habe, um das von ihm übernommene Risiko unmittelbar im Zusammenhang mit dem Abschluss des Vertrags gewinnbringend verkaufen zu können.

**False Positives:**

- `Die Bank` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/8ObA72_16w`) (sent_id: `deanon_TRAIN/8ObA72_16w_4`)


Angelika Neuhauser als weitere Richter in der Arbeitsrechtssache der klagenden Partei Linus Jöbges, vertreten durch Dr. Guido Bach, Rechtsanwalt in Wien, gegen die beklagte Partei Schoessler+Schönrok Planung GmbH, Univ.-Prof. Alva Herdel, vertreten durch Dr. Helmut Engelbrecht, Rechtsanwalt in Wien, wegen Feststellung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 23. August 2016, GZ 7 Ra 75/15y-24, mit dem das Urteil des Arbeits- und Sozialgerichts Wien vom 26. Februar 2015, GZ 7 Cga 108/14y-9, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Schönrok Planung` — partial — pred is substring of gold: `Schoessler+Schönrok Planung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Linus Jöbges`(person)
- `Schoessler+Schönrok Planung GmbH`(organisation)
- `Univ.-Prof. Alva Herdel`(person)

**Example 9** (doc_id: `deanon_TRAIN/9ObA96_13b`) (sent_id: `deanon_TRAIN/9ObA96_13b_4`)


Brigitte Augustin und Mag. Andreas Hach als weitere Richter in der Arbeitsrechtssache der klagenden Partei DI Anita Crämer, vertreten durch Dr. Gerhard Hiebler und Dr. Gerd Grebenjak, Rechtsanwälte in Leoben, gegen die beklagte Partei, GQG E‑Commerce Gesellschaft mbH, Franz-Cäsar-Weg 5, 4115 Gumpesberg, Österreich, vertreten durch Siemer-Siegel-Füreder & Partner, Rechtsanwälte in Wien, wegen Feststellung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 18. April 2013, GZ 6 Ra 18/13h-10, mit dem der Berufung der beklagten Partei gegen das Urteil des Landesgerichts Leoben als Arbeits- und Sozialgericht vom 7. November 2012, GZ 23 Cga 115/12x-6, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Commerce Gesellschaft` — partial — pred is substring of gold: `GQG E‑Commerce Gesellschaft mbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DI Anita Crämer`(person)
- `GQG E‑Commerce Gesellschaft mbH`(organisation)
- `Franz-Cäsar-Weg 5, 4115 Gumpesberg, Österreich`(address)

</details>

---

## `Werke_Organisation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches organisation names ending in 'Werke' (e.g., 'Ost-Bildung Werke') which often lack standard legal suffixes.

**Content:**
```
(?<![A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s])(?<![A-Z])([A-Z][A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s\.\-\+&]*?[A-Za-z0-9])\s+Werke\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 3 | 259 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/1Ob216_15v`) (sent_id: `deanon_TRAIN/1Ob216_15v_5`)


Ihre Werke werden häufig publiziert.

**False Positives:**

- `Ihre Werke` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/4Ob76_14a`) (sent_id: `deanon_TRAIN/4Ob76_14a_15`)


Hinsichtlich künftiger Werke (Leistungen) bedarf es deshalb keiner gesonderten Rechtseinräumung.

**False Positives:**

- `Hinsichtlich künftiger Werke` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/8ObA21_11p`) (sent_id: `deanon_TRAIN/8ObA21_11p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn sowie die fachkundigen Laienrichter Dr. Manfred Engelmann und Alfred Klair als weitere Richter in der Arbeitsrechtssache der klagenden Partei Wilost Garten Werke GmbH & Co OG, Heinickegasse 3x, 4984 Klingersberg, Österreich, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Ing. Waltraud Seckl, vertreten durch Dr. Friedrich Schubert, Rechtsanwalt in Wien, wegen 19.335,55 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 31. Jänner 2011, GZ 7 Ra 121/10f-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO iVm § 2 Abs 1 ASGG).

**False Positives:**

- `Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn sowie die fachkundigen Laienrichter Dr. Manfred Engelmann und Alfred Klair als weitere Richter in der Arbeitsrechtssache der klagenden Partei Wilost Garten Werke` — positional overlap with gold: `Wilost Garten Werke GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wilost Garten Werke GmbH`(organisation)
- `Heinickegasse 3x, 4984 Klingersberg, Österreich`(address)
- `Ing. Waltraud Seckl`(person)

</details>

---

## `Gesellschaft_m_b_H_Prefix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches entities ending with '-Gesellschaft mbH' or 'Gesellschaft mbH' where the name part is captured correctly.

**Content:**
```
(?<![A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s])(?<![A-Z])([A-Z][A-Za-z0-9\s\.\-\+&]*?[A-Za-z0-9])\s+-?Gesellschaft\s+mbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 1 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/9ObA96_13b`) (sent_id: `deanon_TRAIN/9ObA96_13b_4`)


Brigitte Augustin und Mag. Andreas Hach als weitere Richter in der Arbeitsrechtssache der klagenden Partei DI Anita Crämer, vertreten durch Dr. Gerhard Hiebler und Dr. Gerd Grebenjak, Rechtsanwälte in Leoben, gegen die beklagte Partei, GQG E‑Commerce Gesellschaft mbH, Franz-Cäsar-Weg 5, 4115 Gumpesberg, Österreich, vertreten durch Siemer-Siegel-Füreder & Partner, Rechtsanwälte in Wien, wegen Feststellung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 18. April 2013, GZ 6 Ra 18/13h-10, mit dem der Berufung der beklagten Partei gegen das Urteil des Landesgerichts Leoben als Arbeits- und Sozialgericht vom 7. November 2012, GZ 23 Cga 115/12x-6, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Commerce Gesellschaft mbH` — partial — pred is substring of gold: `GQG E‑Commerce Gesellschaft mbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DI Anita Crämer`(person)
- `GQG E‑Commerce Gesellschaft mbH`(organisation)
- `Franz-Cäsar-Weg 5, 4115 Gumpesberg, Österreich`(address)

</details>

---

## `Versicherung_Organisation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches organisation names ending in 'Versicherung' (capitalized) without a legal suffix.

**Content:**
```
(?<![A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s])(?<![A-Z])([A-Z][A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)?)\s+Versicherung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 81 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/7Ob141_16k`) (sent_id: `deanon_TRAIN/7Ob141_16k_6`)


Die Versicherung erstreckt sich daher auch nicht auf Erfüllungssurrogate (RIS-Justiz RS0081685).

**False Positives:**

- `Die Versicherung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/7Ob205_19a`) (sent_id: `deanon_TRAIN/7Ob205_19a_13`)


Die Versicherung erstreckt sich grundsätzlich auf Versicherungsfälle, die während der Laufzeit des Versicherungsvertrages eintreten.

**False Positives:**

- `Die Versicherung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Gruppe_Organisation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches organisation names ending in 'Gruppe' (capitalized) without a legal suffix.

**Content:**
```
(?<![A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s])(?<![A-Z])([A-Z][A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)?)\s+Gruppe\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 179 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_6`)


JQV Finanzen Gruppe GmbH, Innovationsplatz 79, 9751 Nigglai, Österreich, beide vertreten durch Ruggenthaler Rechtsanwalts KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 62.000 EUR) über den außerordentlichen Revisionsrekurs der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Wien vom 20. September 2010, GZ 30 R 29/10w-9, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `JQV Finanzen Gruppe` — partial — pred is substring of gold: `JQV Finanzen Gruppe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `JQV Finanzen Gruppe GmbH`(organisation)
- `Innovationsplatz 79, 9751 Nigglai, Österreich`(address)

**Example 1** (doc_id: `deanon_TRAIN/4Ob220_09w`) (sent_id: `deanon_TRAIN/4Ob220_09w_9`)


Dementsprechend sah das Rekursgericht nicht die Mitgliedschaft der Mutter bei der Sahaja-Yoga Gruppe als solche als bestimmend für die Obsorgeentscheidung.

**False Positives:**

- `Yoga Gruppe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Compound_Organisations_NoSuffix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches compound organisation names without a legal suffix, excluding court terms and focusing on industry/business terms.

**Content:**
```
(?<![A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\s])(?<![A-Z])([A-Z][A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][A-Za-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)?)\s+(Vertrieb|Gastronomie|Digital|Event|Gruppe|Medien|Handel|Pharma|Versicherung|Logistik|Möbel|Bau|Analyse|Textil|Stadt|Nord|Drau|Donau|Willus|BTF|IDUS|Raffler|Süd|NordGarten|Kazantzis|Inn|Algart|Aktiengesellschaft)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 10 | 0 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 10 | 345 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_6`)


Die Aktiengesellschaft habe damit geworben, mit den eingezahlten Beträgen Edelmetalle zu marktüblichen Preisen zu erwerben, zu lagern und zu verwalten und habe dem Beklagten in dessen Funktion als Rechtsanwalt und öffentlicher Notar den Auftrag erteilt, jährliche Prüfberichte über den vollständigen Bestand zu erstellen.

**False Positives:**

- `Die Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/1Ob9_22p`) (sent_id: `deanon_TRAIN/1Ob9_22p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. HR Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Parteien 1. Mag. Tosca Xyländer und 2. Mag. Heinrich Vlachojannis, vertreten durch die Koch Jilek Rechtsanwälte Partnerschaft, Bruck an der Mur, gegen die beklagte Partei Grüttemann E‑Commerce Aktiengesellschaft, Friedhof Döbling 165, 8401 Abtissendorf, Österreich, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH, Wien, wegen 40.358,88 EUR sA, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. November 2021, GZ 5 R 163/21h-43, mit dem das Urteil des Handelsgerichts Wien vom 31. August 2021, GZ 55 Cg 60/20i-36, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Commerce Aktiengesellschaft` — partial — pred is substring of gold: `Grüttemann E‑Commerce Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Tosca Xyländer`(person)
- `Mag. Heinrich Vlachojannis`(person)
- `Grüttemann E‑Commerce Aktiengesellschaft`(organisation)
- `Friedhof Döbling 165, 8401 Abtissendorf, Österreich`(address)

**Example 2** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_6`)


JQV Finanzen Gruppe GmbH, Innovationsplatz 79, 9751 Nigglai, Österreich, beide vertreten durch Ruggenthaler Rechtsanwalts KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 62.000 EUR) über den außerordentlichen Revisionsrekurs der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Wien vom 20. September 2010, GZ 30 R 29/10w-9, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `JQV Finanzen Gruppe` — partial — pred is substring of gold: `JQV Finanzen Gruppe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `JQV Finanzen Gruppe GmbH`(organisation)
- `Innovationsplatz 79, 9751 Nigglai, Österreich`(address)

**Example 3** (doc_id: `deanon_TRAIN/4Ob220_09w`) (sent_id: `deanon_TRAIN/4Ob220_09w_9`)


Dementsprechend sah das Rekursgericht nicht die Mitgliedschaft der Mutter bei der Sahaja-Yoga Gruppe als solche als bestimmend für die Obsorgeentscheidung.

**False Positives:**

- `Yoga Gruppe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/4Ob98_20w`) (sent_id: `deanon_TRAIN/4Ob98_20w_7`)


Roedel Textil GmbH, Hasledt 4, 9634 Bodenmühl, Österreich, vertreten durch Mag. Wolfgang Weilguni, Rechtsanwalt in Wien, wegen 1.028.146,05 EUR sA und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der Klägerin gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 21. April 2020, GZ 5 R 158/19w-116, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Roedel Textil` — partial — pred is substring of gold: `Roedel Textil GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Roedel Textil GmbH`(organisation)
- `Hasledt 4, 9634 Bodenmühl, Österreich`(address)

**Example 5** (doc_id: `deanon_TRAIN/6Ob2_12f`) (sent_id: `deanon_TRAIN/6Ob2_12f_5`)


Jakubiak Handel GmbH, Rudolf-Kassner-Gasse 42, 5134 Sengthal, Österreich, 2.

**False Positives:**

- `Jakubiak Handel` — partial — pred is substring of gold: `Jakubiak Handel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jakubiak Handel GmbH`(organisation)
- `Rudolf-Kassner-Gasse 42, 5134 Sengthal, Österreich`(address)

**Example 6** (doc_id: `deanon_TRAIN/7Ob141_16k`) (sent_id: `deanon_TRAIN/7Ob141_16k_6`)


Die Versicherung erstreckt sich daher auch nicht auf Erfüllungssurrogate (RIS-Justiz RS0081685).

**False Positives:**

- `Die Versicherung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/7Ob205_19a`) (sent_id: `deanon_TRAIN/7Ob205_19a_13`)


Die Versicherung erstreckt sich grundsätzlich auf Versicherungsfälle, die während der Laufzeit des Versicherungsvertrages eintreten.

**False Positives:**

- `Die Versicherung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/7Ob92_19h`) (sent_id: `deanon_TRAIN/7Ob92_19h_220`)


Der Bau befand sich also bereits im Zeitpunkt des Versicherungsfalls in Herstellung und kann nach den diesbezüglich einhelligen Bedingungen auch aus diesem Grund nicht als Wiederherstellung gelten.

**False Positives:**

- `Der Bau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_TRAIN/8Ob100_19t`) (sent_id: `deanon_TRAIN/8Ob100_19t_9`)


Der Vertrieb des Fonds erfolgte über die Erstbeklagte und nachgeschaltete Vermittler/Vermögensberater mit Vertriebsvereinbarung zur Erstbeklagten, im Falle des Klägers durch die Zweitbeklagte.

**False Positives:**

- `Der Vertrieb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Acronym_Industry_Org`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches organisation names starting with an acronym (all caps) followed by a specific industry term or legal suffix, filtering out titles and section references.

**Content:**
```
\b([A-Z]{2,}\s+(?:IT|Vertrieb|Technik|Sicherheit|Immobilien|Verlag|Handel|Versand|GmbH|AG|Limited|KG|GesbR))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 13 | 0 | 13 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 13 | 313 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_13`)


Am 1. 5. 1999 schloss der Kläger als Lizenzgeber mit der Ellbrecht Robotik GesmbH und der ZZMK Technik GesmbH als Lizenznehmerinnen zwei gleichlautende Lizenzverträge.

**False Positives:**

- `ZZMK Technik` — partial — pred is substring of gold: `ZZMK Technik GesmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ellbrecht Robotik GesmbH`(organisation)
- `ZZMK Technik GesmbH`(organisation)

**Example 1** (doc_id: `deanon_TRAIN/10Ob31_16f`) (sent_id: `deanon_TRAIN/10Ob31_16f_3`)


Kopf Der Oberste Gerichtshof als Revisionsgericht hat durch den Hofrat Univ.-Prof. Dr. Neumayr als Vorsitzenden und den Hofrat Dr. Schramm, die Hofrätinnen Dr. Fichtenau und Dr. Tarmann-Prentner sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1060 Wien, Linke Wienzeile 18, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei CESW Technik Services AG, Mike Zachariä, vertreten durch Doralt Seist Csoklich Rechtsanwalts-Partnerschaft in Wien, wegen Unterlassung (30.500 EUR) und Urteilsveröffentlichung (5.500 EUR) über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Jänner 2016, GZ 30 R 35/15k-13, womit das Urteil des Landesgerichts St. Pölten vom 17. Juli 2015, GZ 3 Cg 7/15w-9, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `CESW Technik` — partial — pred is substring of gold: `CESW Technik Services AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `CESW Technik Services AG`(organisation)
- `Mike Zachariä`(person)

**Example 2** (doc_id: `deanon_TRAIN/17Ob17_10i`) (sent_id: `deanon_TRAIN/17Ob17_10i_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Griss als Vorsitzende und durch die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei VRDN Versand GmbH, David Tanzler, vertreten durch Held Berdnik Astner & Partner Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Dr. Livia Zinkel, vertreten durch Dr. Johannes Dörner und Dr. Alexander Singer, Rechtsanwälte in Graz, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 18.000 EUR), infolge „außerordentlichen“ Revisionsrekurses der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 28. September 2010, GZ 1 R 3/10h-23, womit infolge Rekurses der beklagten Partei der Beschluss des Handelsgerichts Wien vom 25. Oktober 2009, GZ 10 Cg 126/09y-10, bestätigt wurde, folgenden Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.

**False Positives:**

- `VRDN Versand` — partial — pred is substring of gold: `VRDN Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VRDN Versand GmbH`(organisation)
- `David Tanzler`(person)
- `Dr. Livia Zinkel`(person)

**Example 3** (doc_id: `deanon_TRAIN/1Ob197_18d`) (sent_id: `deanon_TRAIN/1Ob197_18d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Volze KI GmbH & Co KG, Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich, vertreten durch Dr. Klaus-Dieter Strobach und andere Rechtsanwälte, Grieskirchen, gegen die beklagte Partei Land Oberösterreich, Linz, Landhausplatz 1, vertreten durch Dr. Thomas J. A. Langer, LL.M., Rechtsanwalt in Linz, wegen 475.550,18 EUR sA, über die (außerordentliche) Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2018, GZ 4 R 56/18k-17, mit dem das Urteil des Landesgerichts Wels vom 1. März 2018, GZ 3 Cg 3/16z-13, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `KI GmbH` — partial — pred is substring of gold: `Volze KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Volze KI GmbH`(organisation)
- `Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich`(address)

**Example 4** (doc_id: `deanon_TRAIN/1Ob221_17g`) (sent_id: `deanon_TRAIN/1Ob221_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und Hofrätinnen Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Boothe u. Sandmeier IT GmbH (früher OberTelekom GmbH), Ewaldgasse 28, 4084 Mitterberg, Österreich, vormals vertreten durch Dr. Wolfgang Poleschinski, Rechtsanwalt in Hartberg, gegen die beklagte Partei Yelec Dangelmeier, vertreten durch die Dr. Farhad Paya Rechtsanwalt GmbH, Klagenfurt am Wörthersee, wegen 7.583,60 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 24. August 2017, GZ 1 R 127/17x-69, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 28. März 2017, GZ 16 C 1333/14i-65, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

**False Positives:**

- `IT GmbH` — partial — pred is substring of gold: `Boothe u. Sandmeier IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Boothe u. Sandmeier IT GmbH`(organisation)
- `OberTelekom GmbH`(organisation)
- `Ewaldgasse 28, 4084 Mitterberg, Österreich`(address)
- `Yelec Dangelmeier`(person)

**Example 5** (doc_id: `deanon_TRAIN/3Nc39_24a`) (sent_id: `deanon_TRAIN/3Nc39_24a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn und die Hofrätin Dr. Kodek als weitere Richter in der Ordinationssache der betreibenden Partei Wendy Janacek, vertreten durch Dr. Florian Johann Ernst Knaipp, Rechtsanwalt in Wien, gegen die verpflichtete Partei Siege KI Limited, Edgar Dölle, wegen 47.126,91 EUR sA, über den Antrag auf Ordination nach § 28 JN, den Beschluss gefasst:  Spruch Für die Bewilligung und den Vollzug der von der betreibenden Partei beabsichtigten Rechteexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `KI Limited` — partial — pred is substring of gold: `Siege KI Limited`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wendy Janacek`(person)
- `Siege KI Limited`(organisation)
- `Edgar Dölle`(person)

**Example 6** (doc_id: `deanon_TRAIN/3Ob150_16d`) (sent_id: `deanon_TRAIN/3Ob150_16d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Jensik und Dr. Roch und die Hofrätin Dr. Kodek als weitere Richter in der Exekutionssache der betreibenden Partei SGQ Versand GmbH, Hon.-Prof.in Dr.in Silvana Früboes, vertreten durch Dr. Andrea Gesinger, Rechtsanwältin in Salzburg, gegen die verpflichtete Partei Talseemon GmbH, Finn Auctor, vertreten durch Doschek Rechtsanwalts GmbH in Wien, wegen 9.718,32 EUR sA, über den Revisionsrekurs und Rekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 24. Mai 2016, GZ 22 R 132/16i, 133/16m-21, womit der Beschluss des Bezirksgerichts St. Johann im Pongau vom 17. März 2016, GZ 22 E 1592/15d-14, abgeändert und der Beschluss des Bezirksgerichts St. Johann im Pongau vom 6. April 2016, GZ 22 E 1592/15d-13, aufgehoben wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs und der Rekurs werden zurückgewiesen.

**False Positives:**

- `SGQ Versand` — partial — pred is substring of gold: `SGQ Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `SGQ Versand GmbH`(organisation)
- `Hon.-Prof.in Dr.in Silvana Früboes`(person)
- `Talseemon GmbH`(organisation)
- `Finn Auctor`(person)

**Example 7** (doc_id: `deanon_TRAIN/4Ob76_14a`) (sent_id: `deanon_TRAIN/4Ob76_14a_73`)


Die gesetzlichen Vergütungsansprüche könnten allerdings nur von Verwertungsgesellschaften geltend gemacht werden, weshalb der Beklagte die ihm an dem von ihm produzierten Filmen zustehenden gesetzlichen Vergütungsansprüche (einschließlich derjenigen an dem gegenständlichen Film) der Verwertungsgesellschaft für audio-visuelle Medien VAM GmbH zur treuhändigen Wahrnehmung abgetreten habe.

**False Positives:**

- `VAM GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/6Ob169_12i`) (sent_id: `deanon_TRAIN/6Ob169_12i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Pimmer als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Dr. Schramm, Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Unlandherm KI GmbH, Ilona Hoernle, vertreten durch List Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Wickl Logistik GmbH, Vitus Glassbrenner, vertreten durch Dr. Christoph Brenner - Mag. Severin Perschl Rechtsanwälte OG in Krems, wegen 7.641,30 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Korneuburg als Berufungsgericht vom 16. Februar 2012, GZ 21 R 262/11v-50, womit das Urteil des Bezirksgerichts Gänserndorf vom 2. August 2011, GZ 12 C 1036/10h-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `KI GmbH` — partial — pred is substring of gold: `Unlandherm KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unlandherm KI GmbH`(organisation)
- `Ilona Hoernle`(person)
- `Wickl Logistik GmbH`(organisation)
- `Vitus Glassbrenner`(person)

**Example 9** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_25`)


[7] Am 3. 3. 2020 beantragte derÖsterreichische Verband Gemeinnütziger Bauvereinigungen – Revisionsverband(in der Folge „Revisionsverband“) im Firmenbuch des Erstgerichts bei der Gesellschaft die Löschung der derzeit eingetragenen Gesellschafter und die Wiedereintragung der ursprünglichen Gesellschafter Dr. Anna Sierts mit einer voll eingezahlten Stammeinlage von 22.400 EUR und CYK IT GmbH mit einer voll eingezahlten Stammeinlage von 12.600 EUR.

**False Positives:**

- `CYK IT` — partial — pred is substring of gold: `CYK IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Anna Sierts`(person)
- `CYK IT GmbH`(organisation)

**Example 10** (doc_id: `deanon_TRAIN/7Ob4_12g`) (sent_id: `deanon_TRAIN/7Ob4_12g_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Huber als Vorsitzende und die Hofräte des Obersten Gerichtshofs Dr. Schaumüller, Dr. Hoch, Dr. Kalivoda und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei TVOW Verlag GmbH, Werner Megerlein, vertreten durch Dr. Roland Kometer, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Bruckzor Umwelt Services GmbH, Valerian Landwehrkamp, vertreten durch Rainer Kurbos, Rechtsanwalt in Graz, wegen 8.635,55 EUR sA, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Landesgerichts Innsbruck als Rekursgericht vom 25. Oktober 2011, GZ 1 R 84/11a-18, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `TVOW Verlag` — partial — pred is substring of gold: `TVOW Verlag GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `TVOW Verlag GmbH`(organisation)
- `Werner Megerlein`(person)
- `Bruckzor Umwelt Services GmbH`(organisation)
- `Valerian Landwehrkamp`(person)

**Example 11** (doc_id: `deanon_TRAIN/9Ob68_22y`) (sent_id: `deanon_TRAIN/9Ob68_22y_111`)


Bei der gebotenen objektiven Betrachtung läge in der Mitwirkung der VW AG an der Verbesserung der Beklagten grundsätzlich noch kein ausreichender Grund für die Unzumutbarkeit des primären Gewährleistungsbehelfs, allerdings habe der Kläger auch negative Auswirkungen des für seinen Fahrzeugtyp entwickelten Software-Updates behauptet.

**False Positives:**

- `VW AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_TRAIN/9ObA11_12a`) (sent_id: `deanon_TRAIN/9ObA11_12a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Hofrat des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras, die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter KR Mag. Paul Kunsky und Dr. Klaus Mayr als weitere Richter in der Arbeitsrechtssache der klagenden Partei DI Kira Gamma, vertreten durch Dr. Andreas Löw, Rechtsanwalt in 1070 Wien, wider die beklagte Partei Ammermüller KI GmbH, Zdenko Walendczus, vertreten durch Dr. Peter Rudeck, Dr. Gerhard Schlager, Rechtsanwälte in 1080 Wien, wegen Ausstellung eines Dienstzeugnisses, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 21. Oktober 2011, GZ 9 Ra 102/11b-10, mit dem der Berufung des Klägers gegen das Urteil des Arbeits- und Sozialgerichts Wien vom 30. Mai 2011, GZ 1 Cga 40/11z-6, keine Folge gegeben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `KI GmbH` — partial — pred is substring of gold: `Ammermüller KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DI Kira Gamma`(person)
- `Ammermüller KI GmbH`(organisation)
- `Zdenko Walendczus`(person)

</details>

---

## `Specific_Org_List`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches known specific organisation names from training data that do not fit generic patterns, including hyphenated names and multi-word names.

**Content:**
```
\b(Tal\s+Kelfurtzor\s+Betriebe\s+GmbH|Hamrosi\s+Garten\s+AG|SKSP\s+Immobilien\s+GmbH|Scherg\s+und\s+Kintzli\s+Holz\s+GmbH|Wagenlöhner\s+Versand\s+GmbH|SKRV\s+IT\s+Vertrieb|Medien\s+Gartheim|WestGarten|Maschinenbau\s+Waldtra\s+GmbH|Bersud-Technik\s+GmbH|JUPL\s+Sicherheit\s+GmbH|Mur\s+Dorfheim\s+GmbH|Norglanz|Gruetze\s+Handel\s+Limited|RheinLogistik\s+GmbH)\b
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

