# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-05-11T12:46:29.170658

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/ris/Qwen_Qwen3.5-35B-A3B/organisation/2026-05-11_v2/config.yaml 
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
| Batch size | 20 |
| Refine per batch | 1 |
| Manually annotated examples | 0 |
| First batch with manual data | None |

</details>

---

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 98.7% |
| True Positives | 35 |
| False Positives | 227 |
| False Negatives | 310 |
| Total Gold Entities | 345 |
| Micro Precision | 13.4% |
| Micro Recall | 10.1% |
| Micro F1 | 11.5% |
| Macro F1 | 11.5% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `German Gesellschaft mbH Entity` | 1.1% | 66.7% | 0.6% | 3 | 2 | 1 |
| `German E-Commerce Entity` | 0.6% | 50.0% | 0.3% | 2 | 1 | 1 |
| `German GmbH Entity` | 10.5% | 15.1% | 8.1% | 186 | 28 | 158 |
| `German AG Entity` | 2.9% | 9.7% | 1.7% | 62 | 6 | 56 |
| `German Ltd Entity` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `German u. Kirchmann Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `German Bezirksgericht Entity` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `German Tal-Gastronomie Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `German GmbH & Co KG Entity` | 0.0% | 0.0% | 0.0% | 8 | 0 | 8 |
| `German Bank AG Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `German Limited Entity` | 0.0% | 0.0% | 0.0% | 5 | 0 | 5 |
| `German Aktiengesellschaft Entity` | 0.0% | 0.0% | 0.0% | 7 | 0 | 7 |
| `German Specific NoSuffix Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `German Trilog Institut Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `German Specific GmbH Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `German GmbH Entity`

**F1:** 0.105 | **Precision:** 0.151 | **Recall:** 0.081  

**Format:** `regex`  
**Description:**
Matches entities ending in 'GmbH' with strict boundary, excluding preceding legal terms and ensuring the name starts with a capital letter not preceded by 'Partei' or 'der'.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!Richter\s)(?<!Richterin\s)(?<!Senatspr\u00e4sident\s)(?<!Senatspr\u00e4sidentin\s)(?<!Hofrat\s)(?<!Hofr\u00e4tin\s)(?<!Hofr\u00e4t\s)(?<!Mag\.\s)(?<!Dr\.\s)(?<!Prof\.\s)(?<!Hon\.\s)(?<!Kanzlei\s)(?<!Anwalt\s)(?<!Gesellschafter\s)(?<!klagenden\s)(?<!beklagten\s)(?<!Nebenintervenient\s)(?<!Nebenintervenientin\s)(?<!Nebenintervenienten\s)(?<!Nebenintervenientinnen\s)(?<!Rechtssache\s)(?<!Firmenbuchsache\s)(?<!im\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)([A-Z][A-Za-z0-9\s&+\-]*[A-Z][A-Za-z0-9\s&+\-]*\s+GmbH|[A-Z][A-Z][A-Za-z0-9\s&+\-]*\s+GmbH)(?=[,\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.151 | 0.081 | 0.105 | 186 | 28 | 158 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 28 | 158 | 317 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei C. Dersudheim Digital GmbH, Taxlbergstraße 247, 8151 Rohrbach, Österreich, vertreten durch Dr. Carl Benkhofer, Rechtsanwalt in Wien, gegen die beklagte Partei Ingolf Grimpe, vertreten durch Greiml & Horwath Rechtsanwaltspartnerschaft in Graz, wegen 5.232 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 14 C 1302/11a des Bezirksgerichts Graz-West in nichtöffentlicher Sitzung, den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Graz-West das Bezirksgericht Fünfhaus bestimmt.

| Predicted | Gold |
|---|---|
| `Dersudheim Digital GmbH` | `Dersudheim Digital GmbH` |

**Missed by this rule (FN):**

- `Taxlbergstraße 247, 8151 Rohrbach, Österreich` (address)
- `Ingolf Grimpe` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob23_15b`) (sent_id: `deanon_TRAIN/10Ob23_15b_4`)


Steintra Solar GmbH, Kospachstraße 35, 3162 Rainfeld, Österreich, vertreten durch Dr. Paul Vavrovsky und Mag. Christian Schrott, Rechtsanwälte in Salzburg, 2. Umwelt Dorfwald ges.m.b.H., Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich, vertreten durch Dr. Katharina Sedlazeck-Gschaider, Rechtsanwältin in Salzburg, wegen 11.921,56 EUR sA und Feststellung (Streitwert 5.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 27. Jänner 2015, GZ 11 R 14/14d-34, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Steintra Solar GmbH` | `Steintra Solar GmbH` |

**Missed by this rule (FN):**

- `Kospachstraße 35, 3162 Rainfeld, Österreich` (address)
- `Umwelt Dorfwald ges.m.b.H.` (organisation)
- `Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich` (address)

**Example 2** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_4`)


Energie Conwald GmbH & Co KG und 2.

| Predicted | Gold |
|---|---|
| `Energie Conwald GmbH` | `Energie Conwald GmbH` |

**Example 3** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_5`)


Metall Monglanz GmbH, beide Johann-Puch-Straße 5, 8741 Reisstraße, Österreich, beide vertreten durch Dr. Michael Schneditz-Bolfras und andere Rechtsanwälte in Gmunden, wegen Bucheinsicht (in eventu Rechnungslegung) und Zahlung (Streitwert: 70.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Teilurteil des Oberlandesgerichts Linz als Berufungsgericht vom 17. Februar 2014, GZ 3 R 13/14y-90, womit das Urteil des Landesgerichts Wels vom 27. November 2013 (in der mit Beschluss vom 12. Dezember 2013 berichtigten Fassung), GZ 2 Cg 78/10p-82 und -84, abgeändert wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Metall Monglanz GmbH` | `Metall Monglanz GmbH` |

**Missed by this rule (FN):**

- `Johann-Puch-Straße 5, 8741 Reisstraße, Österreich` (address)

**Example 4** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_5`)


Maschinenbau Heimfurtcon GmbH, Fretzschner Medien, 2.

| Predicted | Gold |
|---|---|
| `Maschinenbau Heimfurtcon GmbH` | `Maschinenbau Heimfurtcon GmbH` |

**Missed by this rule (FN):**

- `Fretzschner Medien` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc22_13m`) (sent_id: `deanon_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Catharina Frielinghausen, Russische Föderation, gegen die verpflichtete Partei Gartcondon-Bildung GmbH, Alan Looß, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

**False Positives:**

- `Partei Gartcondon-Bildung GmbH` — partial — gold is substring of pred: `Gartcondon-Bildung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Catharina Frielinghausen`(person)
- `Gartcondon-Bildung GmbH`(organisation)
- `Alan Looß`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob105_15m`) (sent_id: `deanon_TRAIN/10Ob105_15m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Alsteinost GmbH, Anna Kisaoglu, Bakk. iur., vertreten durch Dr. Erich Kafka und Dr. Manfred Palkovits, Rechtsanwälte in Wien, gegen die beklagte Partei Ing. Mag. Adam Kratki, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 11. Juni 2015, GZ 39 R 41/15s-29, in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Alsteinost GmbH` — partial — gold is substring of pred: `Alsteinost GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alsteinost GmbH`(organisation)
- `Anna Kisaoglu, Bakk. iur.`(person)
- `Mag. Adam Kratki`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob18_25g`) (sent_id: `deanon_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Stanley Plogmeyer, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Tal-Daten GmbH, Karlheinz Hornschuck, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Partei Tal-Daten GmbH` — partial — gold is substring of pred: `Tal-Daten GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stanley Plogmeyer`(person)
- `Tal-Daten GmbH`(organisation)
- `Karlheinz Hornschuck`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob20_19t`) (sent_id: `deanon_TRAIN/10Ob20_19t_8`)


Text Begründung: Im Jahr 2004 errichtete eine GmbH (im Folgenden Unternehmerin) auf einer Liegenschaft eine Stützmauer aus unvermörtelten geschlichteten Natursteinen (Steinschlichtung).

**False Positives:**

- `Im Jahr 2004 errichtete eine GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Ob23_18g`) (sent_id: `deanon_TRAIN/10Ob23_18g_4`)


Severin Simaitis, geboren 20. November 2002, 2. 8. Juli 1967, geboren 17. November 2004, und 3. Nepomuk Sprinzl, geboren 11. September 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Miklos Stiening, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Doschek Rechtsanwalts GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Severin Simaitis`(person)
- `20. November`(date)
- `8. Juli 1967`(date)
- `17. November`(date)
- `Nepomuk Sprinzl`(person)
- `11. September`(date)
- `Mag. Miklos Stiening`(person)

</details>

---

## `German AG Entity`

**F1:** 0.029 | **Precision:** 0.097 | **Recall:** 0.017  

**Format:** `regex`  
**Description:**
Matches entities ending in 'AG' with strict boundary, excluding preceding legal terms and ensuring the name starts with a capital letter not preceded by 'Partei' or 'der'.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!Richter\s)(?<!Richterin\s)(?<!Senatspr\u00e4sident\s)(?<!Senatspr\u00e4sidentin\s)(?<!Hofrat\s)(?<!Hofr\u00e4tin\s)(?<!Hofr\u00e4t\s)(?<!Mag\.\s)(?<!Dr\.\s)(?<!Prof\.\s)(?<!Hon\.\s)(?<!Kanzlei\s)(?<!Anwalt\s)(?<!Gesellschafter\s)(?<!klagenden\s)(?<!beklagten\s)(?<!Nebenintervenient\s)(?<!Nebenintervenientin\s)(?<!Nebenintervenienten\s)(?<!Nebenintervenientinnen\s)(?<!Rechtssache\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)([A-Z][A-Za-z0-9\s&+\-]*[A-Z][A-Za-z0-9\s&+\-]*\s+AG|[A-Z][A-Z][A-Za-z0-9\s&+\-]*\s+AG)(?=[,\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.097 | 0.017 | 0.029 | 62 | 6 | 56 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 56 | 337 |

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

**Example 3** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_4`)


Logdercon-Digital, Dänemark, 2. Fengart GmbH, Oberer Weinweg 87, 9020 Klagenfurt, Österreich, beide vertreten durch Graf & Pitkowitz Rechtsanwälte GmbH in Wien, gegen die Beklagten 1. LGR Medien GmbH, OVX Finanzen, 2. Analyse Kelunizor AG, Fahnberg 42, 4100 Großamberg, Österreich, Deutschland, beide vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Gesamtstreitwert 69.500 EUR), über den Ordinationsantrag der Klägerinnen den Beschluss gefasst:  Spruch Dem Ordinationsantrag wird stattgegeben.

| Predicted | Gold |
|---|---|
| `Analyse Kelunizor AG` | `Analyse Kelunizor AG` |

**Missed by this rule (FN):**

- `Logdercon-Digital` (organisation)
- `Fengart GmbH` (organisation)
- `Oberer Weinweg 87, 9020 Klagenfurt, Österreich` (address)
- `LGR Medien GmbH` (organisation)
- `OVX Finanzen` (organisation)
- `Fahnberg 42, 4100 Großamberg, Österreich` (address)

**Example 4** (doc_id: `deanon_TRAIN/4Ob9_20g`) (sent_id: `deanon_TRAIN/4Ob9_20g_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Ing. KzlR MedR Brunhild Syndikus, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1) Böhnstedt+Bittlmeier Verlag GmbH, Wien Traalmon Betriebe, und 2) TraunBau AG, Schneeballenweg 6, 4232 Penzendorf, Österreich, beide vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 11.091,23 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 6. November 2019, GZ 2 R 158/19x-27, mit dem das Urteil des Landesgerichts Linz vom 29. August 2019, GZ 36 Cg 14/18h-22, bestätigt wurde, den Beschluss gefasst:  Spruch I. Das Revisionsverfahren zu 4 Ob 9/20g wird bis zur Vorabentscheidung des Gerichtshofs der Europäischen Union über das Vorabentscheidungsersuchen des Obersten Gerichtshofs vom 17.

| Predicted | Gold |
|---|---|
| `TraunBau AG` | `TraunBau AG` |

**Missed by this rule (FN):**

- `Ing. KzlR MedR Brunhild Syndikus` (person)
- `Böhnstedt+Bittlmeier Verlag GmbH` (organisation)
- `Wien Traalmon Betriebe` (organisation)
- `Schneeballenweg 6, 4232 Penzendorf, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob102_18z`) (sent_id: `deanon_TRAIN/10Ob102_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG, Adelheid Lochmaier, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Ursula Antoniadis, vertreten durch Knirsch – Braun – Fellner Rechtsanwälte in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 5. September 2018, GZ 40 R 39/18h-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG` — partial — gold is substring of pred: `Skrzypczik + Duchscherer Digital AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Skrzypczik + Duchscherer Digital AG`(organisation)
- `Adelheid Lochmaier`(person)
- `Ursula Antoniadis`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob2_20x`) (sent_id: `deanon_TRAIN/10Ob2_20x_4`)


Matzka und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Ignaz Jungmichel, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei TalAlvalRobotik AG, Delila Leiteritz, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 25.617,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 29. Oktober 2019, GZ 2 R 151/19t-23, mit dem das Urteil des Landesgerichts Linz vom 21. August 2019, GZ 5 Cg 118/18z-19, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

**False Positives:**

- `Partei TalAlvalRobotik AG` — partial — gold is substring of pred: `TalAlvalRobotik AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ignaz Jungmichel`(person)
- `TalAlvalRobotik AG`(organisation)
- `Delila Leiteritz`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob31_16f`) (sent_id: `deanon_TRAIN/10Ob31_16f_3`)


Kopf Der Oberste Gerichtshof als Revisionsgericht hat durch den Hofrat Univ.-Prof. Dr. Neumayr als Vorsitzenden und den Hofrat Dr. Schramm, die Hofrätinnen Dr. Fichtenau und Dr. Tarmann-Prentner sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1060 Wien, Linke Wienzeile 18, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei CESW Technik Services AG, Mike Zachariä, vertreten durch Doralt Seist Csoklich Rechtsanwalts-Partnerschaft in Wien, wegen Unterlassung (30.500 EUR) und Urteilsveröffentlichung (5.500 EUR) über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Jänner 2016, GZ 30 R 35/15k-13, womit das Urteil des Landesgerichts St. Pölten vom 17. Juli 2015, GZ 3 Cg 7/15w-9, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Partei CESW Technik Services AG` — partial — gold is substring of pred: `CESW Technik Services AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `CESW Technik Services AG`(organisation)
- `Mike Zachariä`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob33_15y`) (sent_id: `deanon_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Inn Sudconkraft AG, Elisabeth Breitschwerdt, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Mazik Heizung GmbH, Hemma Rahn, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Inn Sudconkraft AG` — partial — gold is substring of pred: `Inn Sudconkraft AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Sudconkraft AG`(organisation)
- `Elisabeth Breitschwerdt`(person)
- `Mazik Heizung GmbH`(organisation)
- `Hemma Rahn`(person)

**Example 4** (doc_id: `deanon_TRAIN/1Ob106_20z`) (sent_id: `deanon_TRAIN/1Ob106_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Kodek, Mag. Wurzer, Mag. Dr. Wurdinger und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei IGK Bau Consulting AG, Ariadne Seebalt, vertreten durch Dr. Manfred Angerer und andere Rechtsanwälte in Klagenfurt am Wörthersee, gegen die beklagte Partei DI Roxana Pöll, vertreten durch Mag. Claudia Egarter, Rechtsanwältin in Klagenfurt am Wörthersee, wegen 5.457.559,15 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 28. Februar 2020, GZ 2 R 9/20s-150, mit dem das Urteil des Landesgerichts Klagenfurt vom 20. Februar 2017, GZ 21 Cg 24/13h-102, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei IGK Bau Consulting AG` — partial — gold is substring of pred: `IGK Bau Consulting AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `IGK Bau Consulting AG`(organisation)
- `Ariadne Seebalt`(person)
- `DI Roxana Pöll`(person)

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `German GmbH & Co KG Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches entities ending in 'GmbH & Co KG' with strict boundary.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!Richter\s)(?<!Richterin\s)(?<!Senatspr\u00e4sident\s)(?<!Senatspr\u00e4sidentin\s)(?<!Hofrat\s)(?<!Hofr\u00e4tin\s)(?<!Hofr\u00e4t\s)(?<!Mag\.\s)(?<!Dr\.\s)(?<!Prof\.\s)(?<!Hon\.\s)(?<!Kanzlei\s)(?<!Anwalt\s)(?<!Gesellschafter\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!klagenden\s)(?<!beklagten\s)(?<!Nebenintervenient\s)(?<!Nebenintervenientin\s)(?<!Nebenintervenienten\s)(?<!Nebenintervenientinnen\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)([A-Z][A-Za-z0-9\s&+\-]*[A-Z][A-Za-z0-9\s&+\-]*\s+GmbH\s+&\s+Co\s+KG)(?=[,\s]|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 8 | 0 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 8 | 315 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_4`)


Energie Conwald GmbH & Co KG und 2.

**False Positives:**

- `Energie Conwald GmbH & Co KG` — partial — gold is substring of pred: `Energie Conwald GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Energie Conwald GmbH`(organisation)

**Example 1** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_5`)


Text Begründung: Der Kläger erwarb im Jahr 2004 als Verbraucher über Vermittlung eines Wertpapierdienstleistungsunternehmens Kommanditanteile an der Contra GmbH & Co KG im Nominale von 20.000 EUR zuzüglich 1.000 EUR Agio.

**False Positives:**

- `Vermittlung eines Wertpapierdienstleistungsunternehmens Kommanditanteile an der Contra GmbH & Co KG` — partial — gold is substring of pred: `Contra GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Contra GmbH`(organisation)

**Example 2** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt, aus denen Erträge erzielt werden sollen.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/1Ob197_18d`) (sent_id: `deanon_TRAIN/1Ob197_18d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Volze KI GmbH & Co KG, Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich, vertreten durch Dr. Klaus-Dieter Strobach und andere Rechtsanwälte, Grieskirchen, gegen die beklagte Partei Land Oberösterreich, Linz, Landhausplatz 1, vertreten durch Dr. Thomas J. A. Langer, LL.M., Rechtsanwalt in Linz, wegen 475.550,18 EUR sA, über die (außerordentliche) Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2018, GZ 4 R 56/18k-17, mit dem das Urteil des Landesgerichts Wels vom 1. März 2018, GZ 3 Cg 3/16z-13, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Volze KI GmbH & Co KG` — partial — gold is substring of pred: `Volze KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Volze KI GmbH`(organisation)
- `Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich`(address)

</details>

---

## `German Aktiengesellschaft Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches entities ending in 'Aktiengesellschaft' with strict boundary.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!Richter\s)(?<!Richterin\s)(?<!Senatspr\u00e4sident\s)(?<!Senatspr\u00e4sidentin\s)(?<!Hofrat\s)(?<!Hofr\u00e4tin\s)(?<!Hofr\u00e4t\s)(?<!Mag\.\s)(?<!Dr\.\s)(?<!Prof\.\s)(?<!Hon\.\s)(?<!Kanzlei\s)(?<!Anwalt\s)(?<!Gesellschafter\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)([A-Z][A-Za-z0-9\s&+\-]*[A-Z][A-Za-z0-9\s&+\-]*\s+Aktiengesellschaft)(?=[,\s]|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 7 | 0 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 7 | 345 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_5`)


Sie habe im Jahr 2012 mit einer Aktiengesellschaft einen Ansparplan abgeschlossen.

**False Positives:**

- `Sie habe im Jahr 2012 mit einer Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/1Ob140_14s`) (sent_id: `deanon_TRAIN/1Ob140_14s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer und Mag. Dr. Wurdinger sowie die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft, Meidlinger Hauptstraße 19, 5233 Erlach, Österreich, vertreten durch die Walch & Zehetbauer Rechtsanwälte OG, Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 344.011,19 EUR und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Juni 2014, GZ 4 R 202/13g-54, mit dem das Teilzwischenurteil des Landesgerichts Feldkirch vom 2. August 2013, GZ 8 Cg 143/11y-46, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

**False Positives:**

- `Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft` — partial — gold is substring of pred: `Tracondon Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tracondon Aktiengesellschaft`(organisation)
- `Meidlinger Hauptstraße 19, 5233 Erlach, Österreich`(address)

**Example 2** (doc_id: `deanon_TRAIN/2Ob256_12d`) (sent_id: `deanon_TRAIN/2Ob256_12d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Stallbauer Telekom Aktiengesellschaft, Poysdorfer Straße 5, 9341 Dobersberg, Österreich, vertreten durch Dr. Manfred Steininger, Rechtsanwalt in Wien, gegen die beklagte Partei DDr. Viktor Junkmanns, Bakk. iur., vertreten durch die ANWALTGMBH Rinner Teuchtmann in Linz, wegen 50.932,89 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2012, GZ 4 R 158/12a-20, womit das Urteil des Landesgerichts Linz vom 14. Juni 2012, GZ 5 Cg 119/11m-14, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Stallbauer Telekom Aktiengesellschaft` — partial — gold is substring of pred: `Stallbauer Telekom Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stallbauer Telekom Aktiengesellschaft`(organisation)
- `Poysdorfer Straße 5, 9341 Dobersberg, Österreich`(address)
- `DDr. Viktor Junkmanns, Bakk. iur.`(person)

**Example 3** (doc_id: `deanon_TRAIN/3Ob17_20a`) (sent_id: `deanon_TRAIN/3Ob17_20a_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie die Hofräte Priv.-Doz. Dr. Rassi und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Exekutionssache betreibenden Partei Heizung Werkuni Aktiengesellschaft, P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich, vertreten durch Dr. Roland Grilc ua, Rechtsanwälte in Klagenfurt am Wörthersee, gegen die verpflichtete Partei Dorothea Eiken Bank, Peter Eitenmüller, vertreten durch Diwok Hermann Petsche Rechtsanwälte LLP Co KG in Wien, wegen 12.602.980,92 EUR sA, über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. November 2019, GZ 46 R 293/19g-18, mit dem der Beschluss des Bezirksgerichts Favoriten vom 17. April 2019, GZ 17 E 1298/19z-2, bestätigt wurde, den Beschluss gefasst:  Spruch I. Der Revisionsrekurs wird, soweit er sich gegen die Bestätigung der Exekutionsbewilligung richtet, als jedenfalls unzulässig zurückgewiesen.

**False Positives:**

- `Richter in der Exekutionssache betreibenden Partei Heizung Werkuni Aktiengesellschaft` — partial — gold is substring of pred: `Heizung Werkuni Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Heizung Werkuni Aktiengesellschaft`(organisation)
- `P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich`(address)
- `Dorothea Eiken`(person)
- `Peter Eitenmüller`(person)

**Example 4** (doc_id: `deanon_TRAIN/4Ob13_17s`) (sent_id: `deanon_TRAIN/4Ob13_17s_4`)


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

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `German u. Kirchmann Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific pattern 'u.' (und) in company names like Guggemos u. Kirchmann Möbel GmbH.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)([A-Z][A-Za-z0-9\s&+\-]*\s+u\.\s+[A-Z][A-Za-z0-9\s&+\-]*\s+M\u00f6bel\s+GmbH)(?=[,\s]|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `German Tal-Gastronomie Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific entity 'TalFenbruckbruckGastronomie GmbH'.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(TalFenbruckbruckGastronomie\s+GmbH)(?=[,\s]|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `German Bank AG Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific bank names followed by 'Bank AG' to capture only the company name part.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)([A-Z][A-Za-z0-9\s&+\-]*[A-Z][A-Za-z0-9\s&+\-]*\s+Bank\s+AG)(?=[,\s]|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `German Specific NoSuffix Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific entities without standard suffixes or with unique structures found in training data.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!Richter\s)(?<!Richterin\s)(?<!Senatspr\u00e4sident\s)(?<!Senatspr\u00e4sidentin\s)(?<!Hofrat\s)(?<!Hofr\u00e4tin\s)(?<!Hofr\u00e4t\s)(?<!Mag\.\s)(?<!Dr\.\s)(?<!Prof\.\s)(?<!Hon\.\s)(?<!Kanzlei\s)(?<!Anwalt\s)(?<!Gesellschafter\s)(?<!klagenden\s)(?<!beklagten\s)(?<!Nebenintervenient\s)(?<!Nebenintervenientin\s)(?<!Nebenintervenienten\s)(?<!Nebenintervenientinnen\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(NordSicherheit|Druck\s+Glanzfen|Kupferberg\s+\+\s+Kleinen\s+Finanzen|NUSA\s+Analyse\s+Vertrieb|Spendler\s+Maschinenbau|Dontraost\s+Marine|Mur\s+Brucktridon|SeeDruck\s+Gruppe|NiederPflege|EnnsVersicherung|Sevki\s+Event|HochDigital|Pietruszak\s+Recycling|BergMedien|Talal-Energie|Tempel\s+Logistik|Unitradon-Telekom|Vertra-Elektro|Schmerschneider\s+Transport)(?=[,\s]|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `German Trilog Institut Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific entity 'Trilog Institut gesellschaft mbH'.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!Richter\s)(?<!Richterin\s)(?<!Senatspr\u00e4sident\s)(?<!Senatspr\u00e4sidentin\s)(?<!Hofrat\s)(?<!Hofr\u00e4tin\s)(?<!Hofr\u00e4t\s)(?<!Mag\.\s)(?<!Dr\.\s)(?<!Prof\.\s)(?<!Hon\.\s)(?<!Kanzlei\s)(?<!Anwalt\s)(?<!Gesellschafter\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!klagenden\s)(?<!beklagten\s)(?<!Nebenintervenient\s)(?<!Nebenintervenientin\s)(?<!Nebenintervenienten\s)(?<!Nebenintervenientinnen\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(Trilog\s+Institut\s+gesellschaft\s+mbH)(?=[,\s]|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `German Specific GmbH Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific GmbH entities that were missed.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!Richter\s)(?<!Richterin\s)(?<!Senatspr\u00e4sident\s)(?<!Senatspr\u00e4sidentin\s)(?<!Hofrat\s)(?<!Hofr\u00e4tin\s)(?<!Hofr\u00e4t\s)(?<!Mag\.\s)(?<!Dr\.\s)(?<!Prof\.\s)(?<!Hon\.\s)(?<!Kanzlei\s)(?<!Anwalt\s)(?<!Gesellschafter\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!klagenden\s)(?<!beklagten\s)(?<!Nebenintervenient\s)(?<!Nebenintervenientin\s)(?<!Nebenintervenienten\s)(?<!Nebenintervenientinnen\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(Hoffschroer\s+Sanit\u00e4r\s+gesellschaft\s+mbH|Trinorglanz\s+Landwirtschaft\s+Gesellschaft\s+mbH|G\u00e4bel\s+Druck\s+GmbH|Schiffl\s+Bau\s+Limited|Unter\s+Bachlog\s+AG|Transport\s+Fenwald\s+GmbH|Sudalost-Immobilien\s+AG|Beckm\u00f6ller\s+Textil\s+AG|S\u00fcd\s+Monnex\s+Entwicklung\s+GmbH|Seegartnex-Marine|Wien\s+Donostuni\s+GmbH|Ost-Bildung\s+Werke|IQSW\s+Druck\s+GmbH|Stockhorst\s+und\s+Welfle\s+Verlag\s+GmbH)(?=[,\s]|\.|$)
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

## `German GmbH Entity`

**F1:** 0.105 | **Precision:** 0.151 | **Recall:** 0.081  

**Format:** `regex`  
**Description:**
Matches entities ending in 'GmbH' with strict boundary, excluding preceding legal terms and ensuring the name starts with a capital letter not preceded by 'Partei' or 'der'.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!Richter\s)(?<!Richterin\s)(?<!Senatspr\u00e4sident\s)(?<!Senatspr\u00e4sidentin\s)(?<!Hofrat\s)(?<!Hofr\u00e4tin\s)(?<!Hofr\u00e4t\s)(?<!Mag\.\s)(?<!Dr\.\s)(?<!Prof\.\s)(?<!Hon\.\s)(?<!Kanzlei\s)(?<!Anwalt\s)(?<!Gesellschafter\s)(?<!klagenden\s)(?<!beklagten\s)(?<!Nebenintervenient\s)(?<!Nebenintervenientin\s)(?<!Nebenintervenienten\s)(?<!Nebenintervenientinnen\s)(?<!Rechtssache\s)(?<!Firmenbuchsache\s)(?<!im\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)([A-Z][A-Za-z0-9\s&+\-]*[A-Z][A-Za-z0-9\s&+\-]*\s+GmbH|[A-Z][A-Z][A-Za-z0-9\s&+\-]*\s+GmbH)(?=[,\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.151 | 0.081 | 0.105 | 186 | 28 | 158 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 28 | 158 | 317 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei C. Dersudheim Digital GmbH, Taxlbergstraße 247, 8151 Rohrbach, Österreich, vertreten durch Dr. Carl Benkhofer, Rechtsanwalt in Wien, gegen die beklagte Partei Ingolf Grimpe, vertreten durch Greiml & Horwath Rechtsanwaltspartnerschaft in Graz, wegen 5.232 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 14 C 1302/11a des Bezirksgerichts Graz-West in nichtöffentlicher Sitzung, den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Graz-West das Bezirksgericht Fünfhaus bestimmt.

| Predicted | Gold |
|---|---|
| `Dersudheim Digital GmbH` | `Dersudheim Digital GmbH` |

**Missed by this rule (FN):**

- `Taxlbergstraße 247, 8151 Rohrbach, Österreich` (address)
- `Ingolf Grimpe` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob23_15b`) (sent_id: `deanon_TRAIN/10Ob23_15b_4`)


Steintra Solar GmbH, Kospachstraße 35, 3162 Rainfeld, Österreich, vertreten durch Dr. Paul Vavrovsky und Mag. Christian Schrott, Rechtsanwälte in Salzburg, 2. Umwelt Dorfwald ges.m.b.H., Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich, vertreten durch Dr. Katharina Sedlazeck-Gschaider, Rechtsanwältin in Salzburg, wegen 11.921,56 EUR sA und Feststellung (Streitwert 5.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 27. Jänner 2015, GZ 11 R 14/14d-34, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Steintra Solar GmbH` | `Steintra Solar GmbH` |

**Missed by this rule (FN):**

- `Kospachstraße 35, 3162 Rainfeld, Österreich` (address)
- `Umwelt Dorfwald ges.m.b.H.` (organisation)
- `Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich` (address)

**Example 2** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_4`)


Energie Conwald GmbH & Co KG und 2.

| Predicted | Gold |
|---|---|
| `Energie Conwald GmbH` | `Energie Conwald GmbH` |

**Example 3** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_5`)


Metall Monglanz GmbH, beide Johann-Puch-Straße 5, 8741 Reisstraße, Österreich, beide vertreten durch Dr. Michael Schneditz-Bolfras und andere Rechtsanwälte in Gmunden, wegen Bucheinsicht (in eventu Rechnungslegung) und Zahlung (Streitwert: 70.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Teilurteil des Oberlandesgerichts Linz als Berufungsgericht vom 17. Februar 2014, GZ 3 R 13/14y-90, womit das Urteil des Landesgerichts Wels vom 27. November 2013 (in der mit Beschluss vom 12. Dezember 2013 berichtigten Fassung), GZ 2 Cg 78/10p-82 und -84, abgeändert wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Metall Monglanz GmbH` | `Metall Monglanz GmbH` |

**Missed by this rule (FN):**

- `Johann-Puch-Straße 5, 8741 Reisstraße, Österreich` (address)

**Example 4** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_5`)


Maschinenbau Heimfurtcon GmbH, Fretzschner Medien, 2.

| Predicted | Gold |
|---|---|
| `Maschinenbau Heimfurtcon GmbH` | `Maschinenbau Heimfurtcon GmbH` |

**Missed by this rule (FN):**

- `Fretzschner Medien` (organisation)

**Example 5** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_4`)


Republik Österreich, vertreten durch die Finanzprokuratur in Wien, 2. Dr. Ralph Kreidenweiß, und 3. Donau-Automotive GmbH, Ebersreith 11, 8761 Götzendorf, Österreich, beide vertreten durch Dr. Hubert Simon, Rechtsanwalt in Wien, wegen Leistung und Feststellung, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. April 2014, GZ 7 R 21/14h-7, mit dem der Beschluss des Landesgerichts Leoben vom 30. Jänner 2014, GZ 2 Nc 2/14y-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Donau-Automotive GmbH` | `Donau-Automotive GmbH` |

**Missed by this rule (FN):**

- `Dr. Ralph Kreidenweiß` (person)
- `Ebersreith 11, 8761 Götzendorf, Österreich` (address)

**Example 6** (doc_id: `deanon_TRAIN/1Ob66_13g_1Ob67_13d_`) (sent_id: `deanon_TRAIN/1Ob66_13g_1Ob67_13d__4`)


Republik Österreich, vertreten durch die Finanzprokuratur in Wien, 2. Dr. Josefine Rummelt und 3. Hammerla Umwelt GmbH, Friedgasse 46, 3264 Unteramt, Österreich, beide vertreten durch Dr. Hubert Simon, Rechtsanwalt in Wien, wegen Leistung und Feststellung, über den Revisionsrekurs der klagenden Partei gegen die Beschlüsse des Oberlandesgerichts Graz als Rekursgericht vom 1. Februar 2013, GZ 7 R 4/13g-31 und 7 R 5/13d-32, womit die Beschlüsse des Landesgerichts Leoben vom 30. Juli 2012, GZ 2 Nc 25/11a-16, und vom 2. Oktober 2012, GZ 2 Nc 25/11a, 28/11t-22, bestätigt wurden, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hammerla Umwelt GmbH` | `Hammerla Umwelt GmbH` |

**Missed by this rule (FN):**

- `Dr. Josefine Rummelt` (person)
- `Friedgasse 46, 3264 Unteramt, Österreich` (address)

**Example 7** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_19`)


Die beklagte Partei brachte das Gerät nach der Rücknahme zur KI Lexglanzber GmbH, deren Geschäftsführer der Cousin des Geschäftsführers der beklagten Partei ist.

| Predicted | Gold |
|---|---|
| `KI Lexglanzber GmbH` | `KI Lexglanzber GmbH` |

**Example 8** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_4`)


Logdercon-Digital, Dänemark, 2. Fengart GmbH, Oberer Weinweg 87, 9020 Klagenfurt, Österreich, beide vertreten durch Graf & Pitkowitz Rechtsanwälte GmbH in Wien, gegen die Beklagten 1. LGR Medien GmbH, OVX Finanzen, 2. Analyse Kelunizor AG, Fahnberg 42, 4100 Großamberg, Österreich, Deutschland, beide vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Gesamtstreitwert 69.500 EUR), über den Ordinationsantrag der Klägerinnen den Beschluss gefasst:  Spruch Dem Ordinationsantrag wird stattgegeben.

| Predicted | Gold |
|---|---|
| `LGR Medien GmbH` | `LGR Medien GmbH` |

**Missed by this rule (FN):**

- `Logdercon-Digital` (organisation)
- `Fengart GmbH` (organisation)
- `Oberer Weinweg 87, 9020 Klagenfurt, Österreich` (address)
- `OVX Finanzen` (organisation)
- `Analyse Kelunizor AG` (organisation)
- `Fahnberg 42, 4100 Großamberg, Österreich` (address)

**Example 9** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_5`)


Klingenbeil Versand GmbH & Co KG, 2.

| Predicted | Gold |
|---|---|
| `Klingenbeil Versand GmbH` | `Klingenbeil Versand GmbH` |

**Example 10** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_6`)


JQV Finanzen Gruppe GmbH, Innovationsplatz 79, 9751 Nigglai, Österreich, beide vertreten durch Ruggenthaler Rechtsanwalts KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 62.000 EUR) über den außerordentlichen Revisionsrekurs der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Wien vom 20. September 2010, GZ 30 R 29/10w-9, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `JQV Finanzen Gruppe GmbH` | `JQV Finanzen Gruppe GmbH` |

**Missed by this rule (FN):**

- `Innovationsplatz 79, 9751 Nigglai, Österreich` (address)

**Example 11** (doc_id: `deanon_TRAIN/4Ob90_16p`) (sent_id: `deanon_TRAIN/4Ob90_16p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Vogel als Vorsitzenden und die Hofräte Dr. Jensik, Dr. Musger, Dr. Schwarzenbacher und Dr. Rassi als weitere Richter in der Rechtssache der klagenden Partei Lebensmittel Glanzconuni AG, Immanuel Gspan, vertreten durch Fellner Wratzfeld & Partner Rechtsanwälte GmbH in Wien, gegen die beklagten Parteien 1. Fridolin Braunhold, 2. Mag. Frauke Steinweg, und 3. DonauLexlogbruckPlanung GmbH, Felberbachstraße 4, 3631 Jungschlag, Österreich, alle vertreten durch Dr. Peter Zöchbauer, Rechtsanwalt in Wien, wegen Unterlassung (Streitwert 102.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Februar 2016, GZ 2 R 93/15h-25, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `DonauLexlogbruckPlanung GmbH` | `DonauLexlogbruckPlanung GmbH` |

**Missed by this rule (FN):**

- `Lebensmittel Glanzconuni AG` (organisation)
- `Immanuel Gspan` (person)
- `Fridolin Braunhold` (person)
- `Mag. Frauke Steinweg` (person)
- `Felberbachstraße 4, 3631 Jungschlag, Österreich` (address)

**Example 12** (doc_id: `deanon_TRAIN/4Ob98_20w`) (sent_id: `deanon_TRAIN/4Ob98_20w_4`)


Matzka als weitere Richter in der Rechtssache der Klägerin Dr. Imre Grosse-Budde, vertreten durch Huber Swoboda Oswald Aixberger Rechtsanwälte GmbH in Wien, gegen die Beklagte IFS Telekom Technologien GmbH, Großtaxen 13, 6345 Kössen, Österreich, vertreten durch Wiedenbauer Mutz Winkler & Partner Rechtsanwälte GmbH in Wien, und die Nebenintervenienten auf Seiten der Beklagten 1.

| Predicted | Gold |
|---|---|
| `IFS Telekom Technologien GmbH` | `IFS Telekom Technologien GmbH` |

**Missed by this rule (FN):**

- `Dr. Imre Grosse-Budde` (person)
- `Großtaxen 13, 6345 Kössen, Österreich` (address)

**Example 13** (doc_id: `deanon_TRAIN/4Ob98_20w`) (sent_id: `deanon_TRAIN/4Ob98_20w_7`)


Roedel Textil GmbH, Hasledt 4, 9634 Bodenmühl, Österreich, vertreten durch Mag. Wolfgang Weilguni, Rechtsanwalt in Wien, wegen 1.028.146,05 EUR sA und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der Klägerin gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 21. April 2020, GZ 5 R 158/19w-116, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Roedel Textil GmbH` | `Roedel Textil GmbH` |

**Missed by this rule (FN):**

- `Hasledt 4, 9634 Bodenmühl, Österreich` (address)

**Example 14** (doc_id: `deanon_TRAIN/5Ob84_16p`) (sent_id: `deanon_TRAIN/5Ob84_16p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der Rechtssache der klagenden Partei Dimitri Ringlstetter, vertreten durch Dr. Friedrich Gatscha, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. Heimaluni-Event GmbH, Vorderstraß 39, 3920 Harruck, Österreich, vertreten durch Mag. Gerhard Walzl, Rechtsanwalt in Wien, 2. IJWQ Digital Services GmbH, Dr.-Stephan-Krause-Gasse 73, 3244 Baulanden, Österreich, vertreten durch Mag. Alain Danner, Rechtsanwalt in Wien, 3. Dr. Amalia Brodke, vertreten durch Mag. Gerhard Walzl, Rechtsanwalt in Wien, wegen 1. Übertragung der Zusage auf Einräumung von Wohnungseigentum (30.000 EUR), 2. Einverleibung von Miteigentum (50.000 EUR), 3. Zahlung (122.785,01 EUR sA), 4. Feststellung (15.000 EUR), über die außerordentliche Revision der klagenden Partei (Revisionsinteresse 95.000 EUR) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. März 2016, GZ 34 R 152/15w-50, den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Heimaluni-Event GmbH` | `Heimaluni-Event GmbH` |
| `IJWQ Digital Services GmbH` | `IJWQ Digital Services GmbH` |

**Missed by this rule (FN):**

- `Dimitri Ringlstetter` (person)
- `Vorderstraß 39, 3920 Harruck, Österreich` (address)
- `Dr.-Stephan-Krause-Gasse 73, 3244 Baulanden, Österreich` (address)
- `Dr. Amalia Brodke` (person)

**Example 15** (doc_id: `deanon_TRAIN/6Ob105_20i`) (sent_id: `deanon_TRAIN/6Ob105_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden, die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Josepha Imhof, vertreten durch Mag. Erwin Falkner, Rechtsanwalt in Wien, gegen die beklagte Partei R. Nieder Logmonbruck GmbH, Anselm Froncek, vertreten durch Hoffmann & Sykora Rechtsanwälte KG in Tulln, wegen 6.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts St. Pölten als Berufungsgericht vom 13. November 2019, GZ 21 R 208/19z-53, womit über Berufung der klagenden Partei das Urteil des Bezirksgerichts Tulln vom 23. Juni 2019, GZ 11 C 276/18p-49, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Nieder Logmonbruck GmbH` | `Nieder Logmonbruck GmbH` |

**Missed by this rule (FN):**

- `Josepha Imhof` (person)
- `Anselm Froncek` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc22_13m`) (sent_id: `deanon_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Catharina Frielinghausen, Russische Föderation, gegen die verpflichtete Partei Gartcondon-Bildung GmbH, Alan Looß, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

**False Positives:**

- `Partei Gartcondon-Bildung GmbH` — partial — gold is substring of pred: `Gartcondon-Bildung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Catharina Frielinghausen`(person)
- `Gartcondon-Bildung GmbH`(organisation)
- `Alan Looß`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob105_15m`) (sent_id: `deanon_TRAIN/10Ob105_15m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Alsteinost GmbH, Anna Kisaoglu, Bakk. iur., vertreten durch Dr. Erich Kafka und Dr. Manfred Palkovits, Rechtsanwälte in Wien, gegen die beklagte Partei Ing. Mag. Adam Kratki, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 11. Juni 2015, GZ 39 R 41/15s-29, in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Alsteinost GmbH` — partial — gold is substring of pred: `Alsteinost GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alsteinost GmbH`(organisation)
- `Anna Kisaoglu, Bakk. iur.`(person)
- `Mag. Adam Kratki`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob18_25g`) (sent_id: `deanon_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Stanley Plogmeyer, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Tal-Daten GmbH, Karlheinz Hornschuck, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Partei Tal-Daten GmbH` — partial — gold is substring of pred: `Tal-Daten GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stanley Plogmeyer`(person)
- `Tal-Daten GmbH`(organisation)
- `Karlheinz Hornschuck`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob20_19t`) (sent_id: `deanon_TRAIN/10Ob20_19t_8`)


Text Begründung: Im Jahr 2004 errichtete eine GmbH (im Folgenden Unternehmerin) auf einer Liegenschaft eine Stützmauer aus unvermörtelten geschlichteten Natursteinen (Steinschlichtung).

**False Positives:**

- `Im Jahr 2004 errichtete eine GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Ob23_18g`) (sent_id: `deanon_TRAIN/10Ob23_18g_4`)


Severin Simaitis, geboren 20. November 2002, 2. 8. Juli 1967, geboren 17. November 2004, und 3. Nepomuk Sprinzl, geboren 11. September 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Miklos Stiening, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Doschek Rechtsanwalts GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Severin Simaitis`(person)
- `20. November`(date)
- `8. Juli 1967`(date)
- `17. November`(date)
- `Nepomuk Sprinzl`(person)
- `11. September`(date)
- `Mag. Miklos Stiening`(person)

**Example 5** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_15`)


Mit Vertrag vom 28. 3. 2007 wurden die Lizenznehmerinnen nach Firmenänderung als übertragende Gesellschaften mit der Mittel Bachnexlem Betriebe GmbH als übernehmende Gesellschaft verschmolzen, die am 26.

**False Positives:**

- `Gesellschaften mit der Mittel Bachnexlem Betriebe GmbH` — partial — gold is substring of pred: `Mittel Bachnexlem Betriebe GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mittel Bachnexlem Betriebe GmbH`(organisation)

**Example 6** (doc_id: `deanon_TRAIN/10Ob28_19v`) (sent_id: `deanon_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei HochAnalyse GmbH, Piedro Ehmken, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Ludewigs Handel GmbH, Deborah Lochhuber, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei HochAnalyse GmbH` — partial — gold is substring of pred: `HochAnalyse GmbH`
- `Partei Ludewigs Handel GmbH` — partial — gold is substring of pred: `Ludewigs Handel GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `HochAnalyse GmbH`(organisation)
- `Piedro Ehmken`(person)
- `Ludewigs Handel GmbH`(organisation)
- `Deborah Lochhuber`(person)

**Example 7** (doc_id: `deanon_TRAIN/10Ob2_22z`) (sent_id: `deanon_TRAIN/10Ob2_22z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Calvin Amorelli, vertreten durch Dr. Martin Hembach, Rechtsanwalt in Wiener Neustadt, gegen die beklagte Partei Strathewerd u. Niemetz Metall GmbH, Dolores Chatzakis, vertreten durch Mag. Martin Trapichler, Rechtsanwalt in Wien, wegen 13.639,20 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 25. Oktober 2021, GZ 18 R 67/21p-16, mit dem das Urteil des Bezirksgerichts Wiener Neustadt vom 7. Juni 2021, GZ 7 C 117/21b-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Niemetz Metall GmbH` — partial — pred is substring of gold: `Strathewerd u. Niemetz Metall GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Calvin Amorelli`(person)
- `Strathewerd u. Niemetz Metall GmbH`(organisation)
- `Dolores Chatzakis`(person)

**Example 8** (doc_id: `deanon_TRAIN/10Ob33_15y`) (sent_id: `deanon_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Inn Sudconkraft AG, Elisabeth Breitschwerdt, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Mazik Heizung GmbH, Hemma Rahn, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Partei Mazik Heizung GmbH` — partial — gold is substring of pred: `Mazik Heizung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Sudconkraft AG`(organisation)
- `Elisabeth Breitschwerdt`(person)
- `Mazik Heizung GmbH`(organisation)
- `Hemma Rahn`(person)

**Example 9** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Dr. Marlon Richel, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Freimut & Assenov Sicherheit GmbH in Liqu, Spazgasse 41, 8524 Greim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 31.596,47 EUR und Feststellung (6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 18. Juni 2019, GZ 129 R 50/19z-21, mit dem das Urteil des Handelsgerichts Wien vom 28. März 2019, GZ 54 Cg 71/18x-17, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Vogl Rechtsanwalt GmbH` — no gold match — likely missing annotation
- `Partei Freimut & Assenov Sicherheit GmbH` — partial — gold is substring of pred: `Freimut & Assenov Sicherheit GmbH`
- `Wess Kux Kispert & Eckert Rechtsanwalts GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 2

**Gold Entities:**

- `Dr. Marlon Richel`(person)
- `Freimut & Assenov Sicherheit GmbH`(organisation)
- `Spazgasse 41, 8524 Greim, Österreich`(address)

**Example 10** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_5`)


Text Begründung: Der Kläger erwarb im Jahr 2004 als Verbraucher über Vermittlung eines Wertpapierdienstleistungsunternehmens Kommanditanteile an der Contra GmbH & Co KG im Nominale von 20.000 EUR zuzüglich 1.000 EUR Agio.

**False Positives:**

- `Vermittlung eines Wertpapierdienstleistungsunternehmens Kommanditanteile an der Contra GmbH` — partial — gold is substring of pred: `Contra GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Contra GmbH`(organisation)

**Example 11** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt, aus denen Erträge erzielt werden sollen.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_34`)


10. 2019 zu einem völlig gleichgelagerten Fall zu der vom Berufungsgericht angesprochenen Rechtsfrage Stellung genommen hat (beklagte Partei ist hier wie dort die Derber GmbH in Liqu).

**False Positives:**

- `Partei ist hier wie dort die Derber GmbH` — partial — gold is substring of pred: `Derber GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Derber GmbH`(organisation)

**Example 13** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Daniel Wiegand, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei West-Medien Manufaktur GmbH in Liqu, Kanzelweg 32, 4850 Oberthalheim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Vogl Rechtsanwalt GmbH` — no gold match — likely missing annotation
- `Partei West-Medien Manufaktur GmbH` — partial — gold is substring of pred: `West-Medien Manufaktur GmbH`
- `Wess Kux Kispert & Eckert Rechtsanwalts GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 2

**Gold Entities:**

- `DI Daniel Wiegand`(person)
- `West-Medien Manufaktur GmbH`(organisation)
- `Kanzelweg 32, 4850 Oberthalheim, Österreich`(address)

**Example 14** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_23`)


Auch diesen Aspekt nimmt die Staatsanwaltschaft in der Rechtsrüge (Z 9 lit a) ausreichend in den Blick, indem sie auf - in Richtung der Erfüllung auch der objektiven Tatbestandsmerkmale der §§ 146, 147 Abs 3 StGB weisende - Beweisergebnisse zum vorliegenden Vertragsab-schluss trotz mangelnder finanzieller Ausstattung und Absicherung der Inn Dorfdersee GmbH hinweist.

**False Positives:**

- `Abs 3 StGB weisende - Beweisergebnisse zum vorliegenden Vertragsab-schluss trotz mangelnder finanzieller Ausstattung und Absicherung der Inn Dorfdersee GmbH` — partial — gold is substring of pred: `Inn Dorfdersee GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Dorfdersee GmbH`(organisation)

**Example 16** (doc_id: `deanon_TRAIN/12Ns34_18y`) (sent_id: `deanon_TRAIN/12Ns34_18y_4`)


2005 den Beschluss gefasst:  Spruch Vizepräsidentin des Obersten Gerichtshofs Mag. Marek ist von der Entscheidung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Dr. Tilo Bräutigam sowie über die Berufungen der Staatsanwaltschaft und der Privatbeteiligten Hoch Seefurtlem GmbH gegen das Urteil des Landesgerichts Klagenfurt als Schöffengericht vom 30. Juni 2017, GZ 72 Hv 8/17g-80, ausgeschlossen.

**False Positives:**

- `Hoch Seefurtlem GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_TRAIN/13Os109_17d_13Os110_17a_`) (sent_id: `deanon_TRAIN/13Os109_17d_13Os110_17a__26`)


Indem das vorliegende Urteil in Ansehung der Hup & Glossner Solar GmbH in gekürzter Form (§ 270 Abs 4 StPO) ausgefertigt wurde, verletzt es das Gesetz in § 22 Abs 5 VbVG iVm § 270 Abs 2 Z 5 StPO.“

**False Positives:**

- `Indem das vorliegende Urteil in Ansehung der Hup & Glossner Solar GmbH` — partial — gold is substring of pred: `Hup & Glossner Solar GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hup & Glossner Solar GmbH`(organisation)

**Example 18** (doc_id: `deanon_TRAIN/15Os161_11g`) (sent_id: `deanon_TRAIN/15Os161_11g_14`)


Rechtliche Beurteilung Die Mängelrüge (Z 5 zweiter Fall) vermisst zu I./ eine Erörterung der eine Täterschaft des Beschwerdeführers in Abrede stellenden Verantwortungen der beiden Angeklagten, zu IV./ wiederum eine Auseinandersetzung einerseits mit der Aussage des Angeklagten Gisbert Springler, dass die in Serbien sichergestellte Maschine nicht mit jener der Trübe&Conz Landwirtschaft GmbH ident sei, andererseits mit der seine Tatbeteiligung leugnenden Verantwortung des Angeklagten Buchhalla.

**False Positives:**

- `Conz Landwirtschaft GmbH` — partial — pred is substring of gold: `Trübe&Conz Landwirtschaft GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gisbert Springler`(person)
- `Trübe&Conz Landwirtschaft GmbH`(organisation)
- `Buchhalla`(person)

**Example 19** (doc_id: `deanon_TRAIN/17Ob17_10i`) (sent_id: `deanon_TRAIN/17Ob17_10i_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Griss als Vorsitzende und durch die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei VRDN Versand GmbH, David Tanzler, vertreten durch Held Berdnik Astner & Partner Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Dr. Livia Zinkel, vertreten durch Dr. Johannes Dörner und Dr. Alexander Singer, Rechtsanwälte in Graz, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 18.000 EUR), infolge „außerordentlichen“ Revisionsrekurses der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 28. September 2010, GZ 1 R 3/10h-23, womit infolge Rekurses der beklagten Partei der Beschluss des Handelsgerichts Wien vom 25. Oktober 2009, GZ 10 Cg 126/09y-10, bestätigt wurde, folgenden Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei VRDN Versand GmbH` — partial — gold is substring of pred: `VRDN Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VRDN Versand GmbH`(organisation)
- `David Tanzler`(person)
- `Dr. Livia Zinkel`(person)

**Example 20** (doc_id: `deanon_TRAIN/18OCg12_19t`) (sent_id: `deanon_TRAIN/18OCg12_19t_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Veith und die Hofräte Dr. Höllwerth, Priv.-Doz. Dr. Rassi und Mag. Painsi als weitere Richter in der Schiedsrechtssache der klagenden Partei Trabruckgart Holding GmbH, Jean Nellner, vertreten durch die SRG Stock Rafaseder Gruszkiewicz Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Lydia Astorre, Bulgarien, wegen Aufhebung eines Schiedsspruchs (Streitwert 257.397,45 EUR), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Klage wird als nicht zur Bestimmung einer Tagsatzung zur mündlichen Verhandlung geeignet zurückgewiesen.

**False Positives:**

- `Richter in der Schiedsrechtssache der klagenden Partei Trabruckgart Holding GmbH` — partial — gold is substring of pred: `Trabruckgart Holding GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Trabruckgart Holding GmbH`(organisation)
- `Jean Nellner`(person)
- `Lydia Astorre`(person)

**Example 21** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Herbes&Vißers Heizung GmbH, Waldemar Lokämper, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Traun-Luftfahrt GmbH, VetR DDr. Walter Stuehrmann, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

**False Positives:**

- `Partei Traun-Luftfahrt GmbH` — partial — gold is substring of pred: `Traun-Luftfahrt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Herbes&Vißers Heizung GmbH`(organisation)
- `Waldemar Lokämper`(person)
- `Traun-Luftfahrt GmbH`(organisation)
- `VetR DDr. Walter Stuehrmann`(person)

**Example 22** (doc_id: `deanon_TRAIN/1Ob139_18z`) (sent_id: `deanon_TRAIN/1Ob139_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Angelina Töpker Inc., Ronja Straßgschwandtner, vertreten durch Mag. Ralph Kilches, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Lilia Anderßon, als Insolvenzverwalter im Insolvenzverfahren über das Vermögen der Vanek und Eloy Analyse GmbH, Kanischaberg 21, 4742 Kornrödt, Österreich, vertreten durch die Haslinger/Nagele & Partner Rechtsanwälte GmbH, Linz, wegen Feststellung einer Insolvenzforderung (Streitwert 447.352,05 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 28. Juni 2018, GZ 1 R 83/18h-8, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Eloy Analyse GmbH` — partial — pred is substring of gold: `Vanek und Eloy Analyse GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Angelina Töpker`(person)
- `Ronja Straßgschwandtner`(person)
- `Mag. Lilia Anderßon`(person)
- `Vanek und Eloy Analyse GmbH`(organisation)
- `Kanischaberg 21, 4742 Kornrödt, Österreich`(address)

**Example 23** (doc_id: `deanon_TRAIN/1Ob187_14b`) (sent_id: `deanon_TRAIN/1Ob187_14b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der außerstreitigen Rechtssache der Antragstellerin Juliana Enssle, vertreten durch Dr. Albert Heiss, Rechtsanwalt in Innsbruck, gegen den Antragsgegner PhD MedR Oskar Sträßer, vertreten durch Dr. Christian Fuchs Rechtsanwalt GmbH, Innsbruck, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse nach den §§ 81 ff EheG, über die außerordentlichen Revisionsrekurse beider Parteien gegen den Beschluss des Landesgerichts Innsbruck als Rekursgericht vom 30. Mai 2014, GZ 52 R 76/13b-174, womit dem Rekurs des Antragsgegners nicht Folge gegeben und über Rekurs der Antragstellerin der Beschluss des Bezirksgerichts Innsbruck vom 30. November 2012, GZ 1 C 8/07f-163, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Der Beschluss vom 19. März 2015 wird dahin berichtigt, dass es im zweiten Absatz des Spruchs „Dem außerordentlichen Revisionsrekurs des Antragsgegners [anstelle von Antragstellers] wird teilweise Folge gegeben“ und auf Seite 5 der Begründung „Das Erstgericht verpflichtete […] den Antragsgegner zur Leistung […] lautet.

**False Positives:**

- `Fuchs Rechtsanwalt GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Juliana Enssle`(person)
- `PhD MedR Oskar Sträßer`(person)

**Example 24** (doc_id: `deanon_TRAIN/1Ob197_18d`) (sent_id: `deanon_TRAIN/1Ob197_18d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Volze KI GmbH & Co KG, Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich, vertreten durch Dr. Klaus-Dieter Strobach und andere Rechtsanwälte, Grieskirchen, gegen die beklagte Partei Land Oberösterreich, Linz, Landhausplatz 1, vertreten durch Dr. Thomas J. A. Langer, LL.M., Rechtsanwalt in Linz, wegen 475.550,18 EUR sA, über die (außerordentliche) Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2018, GZ 4 R 56/18k-17, mit dem das Urteil des Landesgerichts Wels vom 1. März 2018, GZ 3 Cg 3/16z-13, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Volze KI GmbH` — partial — gold is substring of pred: `Volze KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Volze KI GmbH`(organisation)
- `Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich`(address)

**Example 25** (doc_id: `deanon_TRAIN/1Ob216_15v`) (sent_id: `deanon_TRAIN/1Ob216_15v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Ashley Meinering, vertreten durch Hon.-Prof. Dr. Michel Walter, Rechtsanwalt in Wien, gegen die beklagte Partei Walddon GmbH, Linn Voegelein, vertreten durch die Schlösser & Partner Rechtsanwälte OG, Graz, wegen 33.930 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 19. August 2015, GZ 13 R 74/15w-55, mit dem das Endurteil des Landesgerichts Korneuburg vom 26. Februar 2015, GZ 3 Cg 15/13h-50, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Walddon GmbH` — partial — gold is substring of pred: `Walddon GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ashley Meinering`(person)
- `Walddon GmbH`(organisation)
- `Linn Voegelein`(person)

**Example 26** (doc_id: `deanon_TRAIN/1Ob221_17g`) (sent_id: `deanon_TRAIN/1Ob221_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und Hofrätinnen Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Boothe u. Sandmeier IT GmbH (früher OberTelekom GmbH), Ewaldgasse 28, 4084 Mitterberg, Österreich, vormals vertreten durch Dr. Wolfgang Poleschinski, Rechtsanwalt in Hartberg, gegen die beklagte Partei Yelec Dangelmeier, vertreten durch die Dr. Farhad Paya Rechtsanwalt GmbH, Klagenfurt am Wörthersee, wegen 7.583,60 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 24. August 2017, GZ 1 R 127/17x-69, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 28. März 2017, GZ 16 C 1333/14i-65, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

**False Positives:**

- `Sandmeier IT GmbH` — partial — pred is substring of gold: `Boothe u. Sandmeier IT GmbH`
- `Paya Rechtsanwalt GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Boothe u. Sandmeier IT GmbH`(organisation)
- `OberTelekom GmbH`(organisation)
- `Ewaldgasse 28, 4084 Mitterberg, Österreich`(address)
- `Yelec Dangelmeier`(person)

**Example 27** (doc_id: `deanon_TRAIN/1Ob226_20x`) (sent_id: `deanon_TRAIN/1Ob226_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Ibrahim Gerlicher GmbH, Gabriel van Straaten, vertreten durch Dr. Martin Leitner und andere, Rechtsanwälte in Wien, gegen die beklagte Partei Stadt Olaf Doerrien, vertreten durch die Estermann Pock Rechtsanwälte GmbH, Wien, wegen 19.002,01 EUR, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 7. September 2020, GZ 14 R 61/20y-27, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 28. Jänner 2020, GZ 31 Cg 1/19y-22, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Ibrahim Gerlicher GmbH` — partial — gold is substring of pred: `Ibrahim Gerlicher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ibrahim Gerlicher`(person)
- `Gabriel van Straaten`(person)
- `Olaf Doerrien`(person)

**Example 28** (doc_id: `deanon_TRAIN/1Ob26_20k`) (sent_id: `deanon_TRAIN/1Ob26_20k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Synsynfurt-Finanzen GmbH, Tanja Thielike, vertreten durch die Draxler Rexeis Sozietät von Rechtsanwälten OG, Graz, gegen die beklagte Partei Roberta Reumschüssel, Bakk. phil., vertreten durch Mag. Dr. Alfred Wansch, Rechtsanwalt in Wien, wegen Räumung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtsachen Wien als Berufungsgericht vom 13. November 2019, GZ 39 R 228/19x-70, mit dem das Urteil des Bezirksgerichts Hernals vom 30. April 2019, GZ 4 C 277/16f-64, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Synsynfurt-Finanzen GmbH` — partial — gold is substring of pred: `Synsynfurt-Finanzen GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Synsynfurt-Finanzen GmbH`(organisation)
- `Tanja Thielike`(person)
- `Roberta Reumschüssel, Bakk. phil.`(person)

**Example 29** (doc_id: `deanon_TRAIN/1Ob51_11y`) (sent_id: `deanon_TRAIN/1Ob51_11y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei mj Kurt Schwenckel, vertreten durch Mag. Erich Frenner, Rechtsanwalt in Saalfelden, gegen die beklagte Partei Condon Planung GmbH, Corvin Heidtmeyer, vertreten durch Dr. Harald Schwendinger und Dr. Brigitte Piber Rechtsanwälte in Salzburg, wegen 5.100 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 30. Dezember 2010, GZ 53 R 273/10v-12, mit dem über die Berufung der beklagten Partei das Zwischenurteil des Bezirksgerichts Saalfelden vom 23. Juni 2010, GZ 2 C 454/10z-7, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei Condon Planung GmbH` — partial — gold is substring of pred: `Condon Planung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kurt Schwenckel`(person)
- `Condon Planung GmbH`(organisation)
- `Corvin Heidtmeyer`(person)

**Example 30** (doc_id: `deanon_TRAIN/1Ob51_14b`) (sent_id: `deanon_TRAIN/1Ob51_14b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Landwirtschaft Glanzlemglanz GmbH, Erhard Blaufuß, vertreten durch Dr. Arno Kempf, Rechtsanwalt in Spittal an der Drau, gegen die beklagten Parteien 1.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Landwirtschaft Glanzlemglanz GmbH` — partial — gold is substring of pred: `Landwirtschaft Glanzlemglanz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landwirtschaft Glanzlemglanz GmbH`(organisation)
- `Erhard Blaufuß`(person)

**Example 31** (doc_id: `deanon_TRAIN/1Ob53_25p`) (sent_id: `deanon_TRAIN/1Ob53_25p_44`)


Dem Vorwurf, der Beklagte habe es verabsäumt, einem (irrtümlichen) Verkauf fremder Fahrzeuge und Maschinen durch die GmbH durch ein geeignetesKontrollsystem vorzubeugen(vgl RS0023927), sind die Feststellungen entgegenzuhalten: Er hatte ein System eingeführt, nach dem alle auf Betriebsliegenschaften der GmbH befindlichen Geräte und Maschinen in Listen eingetragen und die jeweiligen Eigentümer vermerkt wurden, sodass über im fremden Eigentum stehende Sachen keine Rechnung und kein Lieferschein ausgestellt werden konnten.

**False Positives:**

- `Verkauf fremder Fahrzeuge und Maschinen durch die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_TRAIN/1Ob82_18t`) (sent_id: `deanon_TRAIN/1Ob82_18t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei MurUmwelt GmbH, Oskar Stelzel, vertreten durch die KRONBERGER Rechtsanwälte Gesellschaft mbH, Wien, gegen die beklagte Partei Brian Hüpsch, vertreten durch Dr. Werner Loos, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 14. März 2018, GZ 38 R 303/17s-48, mit dem das Urteil des Bezirksgerichts Fünfhaus vom 4. August 2017, GZ 22 C 163/16w-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei MurUmwelt GmbH` — partial — gold is substring of pred: `MurUmwelt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MurUmwelt GmbH`(organisation)
- `Oskar Stelzel`(person)
- `Brian Hüpsch`(person)

**Example 33** (doc_id: `deanon_TRAIN/2Ob159_18y`) (sent_id: `deanon_TRAIN/2Ob159_18y_11`)


Er selbst war ua als Fenstermonteur in der GmbH tätig.

**False Positives:**

- `Er selbst war ua als Fenstermonteur in der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_TRAIN/2Ob159_18y`) (sent_id: `deanon_TRAIN/2Ob159_18y_20`)


In weiterer Folge brachte er – zusammengefasst – vor, der Verdienstentgang errechne sich aus dem Ausfall des hypothetischen Gewinns seiner GmbH, der erzielbar gewesen wäre, hätte das Unternehmen nicht geschlossen werden müssen (ON 8, vgl auch ON 45 und 51).

**False Positives:**

- `Ausfall des hypothetischen Gewinns seiner GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_TRAIN/2Ob178_18t`) (sent_id: `deanon_TRAIN/2Ob178_18t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Veith als Vorsitzenden, den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé sowie die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Garttri Sicherheit -GesmbH, Alpendorfsiedlung 14, 4209 Linzerberg, Österreich, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, wider die beklagte Partei Vogelsanger Marine GmbH, Juri Büttgens, vertreten durch Mag. Dr. Dirk Just, Rechtsanwalt in Wien, wegen (restlich) 30.000 EUR sA, über die „außerordentliche Revision“ der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Juli 2018, GZ 4 R 79/18v-157, mit welchem das Endurteil des Handelsgerichts Wien vom 9. April 2018, GZ 40 Cg 12/11g-153, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

**False Positives:**

- `Partei Vogelsanger Marine GmbH` — partial — gold is substring of pred: `Vogelsanger Marine GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Garttri Sicherheit`(organisation)
- `Alpendorfsiedlung 14, 4209 Linzerberg, Österreich`(address)
- `Vogelsanger Marine GmbH`(organisation)
- `Juri Büttgens`(person)

**Example 36** (doc_id: `deanon_TRAIN/2Ob194_24d`) (sent_id: `deanon_TRAIN/2Ob194_24d_4`)


Sloboda, Dr. Thunhart, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Rut Dolff, vertreten durch Gottgeisl Leinsmer Weber Rechtsanwälte GmbH in Wien, wider die beklagte Partei Samuel Nachtwei, Malta, vertreten durch Mag. Simon Wallner Rechtsanwalt GmbH in Wien, wegen 30.895 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 1. Oktober 2024, GZ 12 R 72/24g-21, den Beschluss gefasst:  Spruch I. Der Antrag auf Unterbrechung des Revisionsverfahrens bis zur Entscheidung des Europäischen Gerichtshofs zu C-683/24 wird abgewiesen.

**False Positives:**

- `Wallner Rechtsanwalt GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Rut Dolff`(person)
- `Samuel Nachtwei`(person)

**Example 37** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden, die Hofräte Dr. Veith und Dr. Musger sowie die Hofrätinnen Dr. E. Solé und Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Luigi Neimeier, vertreten durch Rechtsanwälte Estermann & Partner OG in Mattighofen, gegen die beklagte Partei LNC KI Solutions GmbH, Kordelia Grauel, vertreten durch Dr. Herbert Harlander und Mag. Wolfgang Harlander, Rechtsanwälte in Salzburg, wegen 33.251,85 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. März 2015, GZ 2 R 1/15b-37, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Salzburg vom 23. Oktober 2014, GZ 4 Cg 27/13d-33, bestätigt wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Partei LNC KI Solutions GmbH` — partial — gold is substring of pred: `LNC KI Solutions GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Luigi Neimeier`(person)
- `LNC KI Solutions GmbH`(organisation)
- `Kordelia Grauel`(person)

**Example 38** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_25`)


Im Herbst 2012 habe sich ein Aufkleber der Ostvallem-Robotik GmbH vom Luftentfeuchter gelöst und ein Typenschild mit dem Baujahr 1986 freigelegt.

**False Positives:**

- `Im Herbst 2012 habe sich ein Aufkleber der Ostvallem-Robotik GmbH` — partial — gold is substring of pred: `Ostvallem-Robotik GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ostvallem-Robotik GmbH`(organisation)

**Example 39** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_61`)


Die beklagte Partei führte gemeinsam mit der LHS Lebensmittel Consulting GmbH eine Einschulungsveranstaltung für Heutrocknungsgeräte durch, an der auch der Kläger teilnahm.

**False Positives:**

- `Lebensmittel Consulting GmbH` — partial — pred is substring of gold: `LHS Lebensmittel Consulting GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `LHS Lebensmittel Consulting GmbH`(organisation)

**Example 40** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_62`)


Dabei wiesen die anwesenden Mitarbeiter der GmbH darauf hin, dass dieses Unternehmen Ansprechpartner für Serviceleistungen ist.

**False Positives:**

- `Dabei wiesen die anwesenden Mitarbeiter der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_63`)


Eine Plakette mit Namen, Anschrift und Kontaktdaten der GmbH war auch auf dem an den Kläger verkauften Gerät angebracht.

**False Positives:**

- `Anschrift und Kontaktdaten der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_78`)


Die Bachtri GmbH hat vor der Auslieferung des neu zusammengesetzten Geräts eine Druckprobe durchgeführt.

**False Positives:**

- `Die Bachtri GmbH` — partial — gold is substring of pred: `Bachtri GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bachtri GmbH`(organisation)

**Example 43** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_80`)


Die Maerklin und Steckelmann Software GmbH befüllte den neu zusammengesetzten Luftentfeuchter Anfang 2011 mit dem Kältemittel R22, dessen Verwendung seit 1. 1.

**False Positives:**

- `Die Maerklin und Steckelmann Software GmbH` — partial — gold is substring of pred: `Maerklin und Steckelmann Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maerklin und Steckelmann Software GmbH`(organisation)

**Example 44** (doc_id: `deanon_TRAIN/3Nc11_13t`) (sent_id: `deanon_TRAIN/3Nc11_13t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie die Hofräte Univ.-Prof Dr. Neumayr und Dr. Jensik als weitere Richter in der Ordinationssache der Antragstellerin Waldzorval Technologien GmbH, Dr.-Kühne-Gasse 29, 9560 Albern, Österreich, vertreten durch Dr. Clemens Thiele, Rechtsanwalt in Salzburg, gegen die Antragsgegnerin Pflege Allemkraft GmbH, Schirmerstraße 61, 8967 Oberhausberg, Österreich, wegen Exekutionsführung nach § 355 EO, infolge Antrags gemäß § 28 JN den Beschluss gefasst:  Spruch Für die Bewilligung und die Vollziehung der beabsichtigten Unterlassungsexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Richter in der Ordinationssache der Antragstellerin Waldzorval Technologien GmbH` — partial — gold is substring of pred: `Waldzorval Technologien GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Waldzorval Technologien GmbH`(organisation)
- `Dr.-Kühne-Gasse 29, 9560 Albern, Österreich`(address)
- `Pflege Allemkraft GmbH`(organisation)
- `Schirmerstraße 61, 8967 Oberhausberg, Österreich`(address)

**Example 45** (doc_id: `deanon_TRAIN/3Nc19_22g`) (sent_id: `deanon_TRAIN/3Nc19_22g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek sowie den Hofrat Dr. Stefula als weitere Richter in der Ordinationssache der Antragstellerin Stadt-Robotik GmbH, Hum 65, 9241 Kantnig, Österreich, vertreten durch Specht & Partner Rechtsanwalt GmbH in Wien, gegen die Antragsgegnerin Ing. Verona Obersteiner, Russische Föderation, wegen § 355 EO, über den Ordinationsantrag der Antragstellerin, den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Richter in der Ordinationssache der Antragstellerin Stadt-Robotik GmbH` — partial — gold is substring of pred: `Stadt-Robotik GmbH`
- `Specht & Partner Rechtsanwalt GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Stadt-Robotik GmbH`(organisation)
- `Hum 65, 9241 Kantnig, Österreich`(address)
- `Ing. Verona Obersteiner`(person)

**Example 46** (doc_id: `deanon_TRAIN/3Ob12_11b`) (sent_id: `deanon_TRAIN/3Ob12_11b_30`)


5. Die Beurteilung des Berufungsgerichts, der Oppositionskläger habe ausreichend dargetan, dass die von ihm behobenen Beträge in Höhe von insgesamt 114.500 EUR in den Bilanzen der GmbH nicht verbucht wurden, weshalb er auch in diesem Umfang der Titelverpflichtung entsprochen habe, wirft ebenfalls keine im Rahmen einer außerordentlichen Revision aufzugreifende erhebliche Rechtsfrage auf: Es steht durch die gelegte Rechnung in Verbindung mit den Bilanzen der GmbH, in deren Besitz der Oppositionsbeklagte unstrittig ist, fest, dass weder der Gesamtbetrag von 114.500 EUR noch Teilbeträge davon in den Bilanzen der GmbH verbucht wurde.

**False Positives:**

- `EUR in den Bilanzen der GmbH` — no gold match — likely missing annotation
- `Es steht durch die gelegte Rechnung in Verbindung mit den Bilanzen der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 47** (doc_id: `deanon_TRAIN/3Ob147_20v`) (sent_id: `deanon_TRAIN/3Ob147_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Kraftnorost Wind GmbH, Roderich Holtze, vertreten durch Mag. Andreas Kleiber, Rechtsanwalt in Wien, gegen die beklagte Partei Annette Fiss verein Ing. Kirstin Movcan, vertreten durch Pflaum Karlberger Wiener Opetnik, Rechtsanwälte in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 22. Juli 2020, GZ 40 R 37/20t-27, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Kraftnorost Wind GmbH` — partial — gold is substring of pred: `Kraftnorost Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kraftnorost Wind GmbH`(organisation)
- `Roderich Holtze`(person)
- `Annette Fiss`(person)
- `Ing. Kirstin Movcan`(person)

**Example 48** (doc_id: `deanon_TRAIN/3Ob150_16d`) (sent_id: `deanon_TRAIN/3Ob150_16d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Jensik und Dr. Roch und die Hofrätin Dr. Kodek als weitere Richter in der Exekutionssache der betreibenden Partei SGQ Versand GmbH, Hon.-Prof.in Dr.in Silvana Früboes, vertreten durch Dr. Andrea Gesinger, Rechtsanwältin in Salzburg, gegen die verpflichtete Partei Talseemon GmbH, Finn Auctor, vertreten durch Doschek Rechtsanwalts GmbH in Wien, wegen 9.718,32 EUR sA, über den Revisionsrekurs und Rekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 24. Mai 2016, GZ 22 R 132/16i, 133/16m-21, womit der Beschluss des Bezirksgerichts St. Johann im Pongau vom 17. März 2016, GZ 22 E 1592/15d-14, abgeändert und der Beschluss des Bezirksgerichts St. Johann im Pongau vom 6. April 2016, GZ 22 E 1592/15d-13, aufgehoben wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs und der Rekurs werden zurückgewiesen.

**False Positives:**

- `Richter in der Exekutionssache der betreibenden Partei SGQ Versand GmbH` — partial — gold is substring of pred: `SGQ Versand GmbH`
- `Partei Talseemon GmbH` — partial — gold is substring of pred: `Talseemon GmbH`
- `Doschek Rechtsanwalts GmbH` — no gold match — likely missing annotation

> overlaps gold: 2  |  likely missing annotation: 1

**Gold Entities:**

- `SGQ Versand GmbH`(organisation)
- `Hon.-Prof.in Dr.in Silvana Früboes`(person)
- `Talseemon GmbH`(organisation)
- `Finn Auctor`(person)

**Example 49** (doc_id: `deanon_TRAIN/3Ob164_20v`) (sent_id: `deanon_TRAIN/3Ob164_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Bruckgartver GmbH, MedR StR René Titz, vertreten durch Dr. Reinhard Schanda, Rechtsanwalt in Wien, gegen die beklagte Partei Ofczarczik Planung AG, Dipl.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Bruckgartver GmbH` — partial — gold is substring of pred: `Bruckgartver GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bruckgartver GmbH`(organisation)
- `MedR StR René Titz`(person)
- `Ofczarczik Planung AG`(organisation)

**Example 50** (doc_id: `deanon_TRAIN/3Ob185_22k`) (sent_id: `deanon_TRAIN/3Ob185_22k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn und die Hofrätinnen Dr. Weixelbraun-Mohr, Dr. Kodek und Mag. Wessely-Kristöfel als weitere Richter in der Exekutionssache der betreibenden Partei Dr. Brian Adamska, vertreten durch Dr. Martin Neuwirth, Dr. Alexander Neurauter, Rechtsanwälte in Wien, gegen die verpflichtete Partei Kelglanzver-Software GmbH, Egon Libert, vertreten durch Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH in Wien, wegen zwangsweiser Räumung, über den Revisionsrekurs der betreibenden Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 12. August 2022, GZ 40 R 104/22y-20, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 8. April 2022, GZ 49 E 11/22w-3, abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Partei Kelglanzver-Software GmbH` — partial — gold is substring of pred: `Kelglanzver-Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Brian Adamska`(person)
- `Kelglanzver-Software GmbH`(organisation)
- `Egon Libert`(person)

**Example 51** (doc_id: `deanon_TRAIN/3Ob204_19z`) (sent_id: `deanon_TRAIN/3Ob204_19z_11`)


Darüber hinausgehende Buchhaltungsunterlagen betreffend die Unternehmensgruppe Petkovic Forschung GmbH könne er nicht vorlegen, weil er darauf keinen direkten Zugriff (mehr) habe und die derzeitige Eigentümerin dieses Unternehmens jegliche Offenbarung für Zwecke der Rechnungslegung ablehne.

**False Positives:**

- `Buchhaltungsunterlagen betreffend die Unternehmensgruppe Petkovic Forschung GmbH` — partial — gold is substring of pred: `Petkovic Forschung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Petkovic Forschung GmbH`(organisation)

**Example 52** (doc_id: `deanon_TRAIN/3Ob209_21p`) (sent_id: `deanon_TRAIN/3Ob209_21p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Nexostlem GmbH & Co KG, Rehlackenweg 5G, 8451 Pernitsch, Österreich, vertreten durch DDr. Heinz Dietmar Schimanko, Rechtsanwalt in Wien, gegen die beklagte Partei RheinLandwirtschaft Vertrieb GmbH, Klaus Dissler, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH & Co KG in Wien, wegen 7.906,82 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 7. Juni 2021, GZ 38 R 66/21v-16, mit dem das Urteil des Bezirksgerichts Favoriten vom 19. Jänner 2021, GZ 3 C 503/20f-12, abgeändert wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Nexostlem GmbH` — partial — gold is substring of pred: `Nexostlem GmbH`
- `Partei RheinLandwirtschaft Vertrieb GmbH` — partial — gold is substring of pred: `RheinLandwirtschaft Vertrieb GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Nexostlem GmbH`(organisation)
- `Rehlackenweg 5G, 8451 Pernitsch, Österreich`(address)
- `RheinLandwirtschaft Vertrieb GmbH`(organisation)
- `Klaus Dissler`(person)

**Example 53** (doc_id: `deanon_TRAIN/3Ob248_10g`) (sent_id: `deanon_TRAIN/3Ob248_10g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Riecken Maschinenbau GmbH, Hubert Englmaier, vertreten durch Dr. Martin Holzer, Rechtsanwalt in Bruck an der Mur, gegen die beklagte Partei Florian Corvetti, vertreten durch Dr. Heimo Jilek, Rechtsanwalt in Leoben, wegen Einwendungen gegen den Anspruch (§ 35 EO), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Leoben als Berufungsgericht vom 3. November 2010, GZ 1 R 244/10i-34, womit über Berufung der beklagten Partei das Urteil des Bezirksgerichts Leoben vom 9. Juni 2010, GZ 5 C 315/09y-28, abgeändert wurde, den Beschluss gefasst:  Spruch Der außerordentlichen Revision der klagenden Partei wird Folge gegeben, das angefochtene Urteil aufgehoben und die Rechtssache zur neuerlichen Entscheidung an das Berufungsgericht zurückverwiesen.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Riecken Maschinenbau GmbH` — partial — gold is substring of pred: `Riecken Maschinenbau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Riecken Maschinenbau GmbH`(organisation)
- `Hubert Englmaier`(person)
- `Florian Corvetti`(person)

**Example 54** (doc_id: `deanon_TRAIN/3Ob32_17b`) (sent_id: `deanon_TRAIN/3Ob32_17b_82`)


Auch die damalige Ortsabwesenheit des Geschäftsführers der Verpflichteten verlangt keine andere Beurteilung, weil dieser – wie feststeht – „mit dem täglichen Geschäft, dem internen Postlauf und der Organisation in der GmbH weniger vertraut war“.

**False Positives:**

- `Postlauf und der Organisation in der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_TRAIN/3Ob54_21v`) (sent_id: `deanon_TRAIN/3Ob54_21v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in den verbundenen Rechtssachen der klagenden und widerbeklagten Partei Gambal Software GmbH, Esra Bubenischek, vertreten durch Mag. Gerold Schwarzer, Rechtsanwalt in Wien, gegen die beklagte und widerklagende Partei HR Hilde vom Dorf, wegen 286.300,47 EUR sA und 41.219,24 EUR sA, über die außerordentliche Revision der klagenden und widerbeklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 11. Februar 2021, GZ 1 R 168/20m-26, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Richter in den verbundenen Rechtssachen der klagenden und widerbeklagten Partei Gambal Software GmbH` — partial — gold is substring of pred: `Gambal Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gambal Software GmbH`(organisation)
- `Esra Bubenischek`(person)
- `HR Hilde vom Dorf`(person)

**Example 56** (doc_id: `deanon_TRAIN/3Ob69_19x`) (sent_id: `deanon_TRAIN/3Ob69_19x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Roch und Priv.-Doz. Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Li Hillerbrandt, vertreten durch Dr. Klaus Plätzer, Rechtsanwalt in Salzburg, gegen die beklagte Partei Stadt Derlextra GmbH, Frederik Vlothoerbäumer, vertreten durch Dr. Patrick Ruth, Rechtsanwalt in Innsbruck, wegen Unterlassung (Streitwert 50.000 EUR), über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 7. Februar 2019, GZ 3 R 164/18k-44, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Stadt Derlextra GmbH` — partial — gold is substring of pred: `Stadt Derlextra GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Li Hillerbrandt`(person)
- `Stadt Derlextra GmbH`(organisation)
- `Frederik Vlothoerbäumer`(person)

**Example 57** (doc_id: `deanon_TRAIN/4Nc3_12x`) (sent_id: `deanon_TRAIN/4Nc3_12x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel und Dr. Jensik als weitere Richter in der beim Landesgericht Innsbruck zu AZ 59 Cg 92/11x anhängigen Rechtssache der klagenden Partei Rudigkeit Finanzen GmbH, Ing. Sascha Rohkrämer, vertreten durch Mag. Heinz Heher, Rechtsanwalt in Wien, gegen die beklagte Partei Suddorftra Manufaktur GmbH, Ludmilla Nottelmann, vertreten durch Dr. Adrian Hollaender, Rechtsanwalt in Innsbruck, wegen Unterlassung, Urteilsveröffentlichung und 67.606 EUR sA, über die Delegierungsanträge der beklagten Partei gemäß § 31 Abs 2 JN, folgenden Beschluss gefasst:  Spruch Die Anträge der beklagten Partei, die Rechtssache an das „Landesgericht Wien“ bzw Handelsgericht Wien zu delegieren, werden abgewiesen.

**False Positives:**

- `Rechtssache der klagenden Partei Rudigkeit Finanzen GmbH` — partial — gold is substring of pred: `Rudigkeit Finanzen GmbH`
- `Partei Suddorftra Manufaktur GmbH` — partial — gold is substring of pred: `Suddorftra Manufaktur GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Rudigkeit Finanzen GmbH`(organisation)
- `Ing. Sascha Rohkrämer`(person)
- `Suddorftra Manufaktur GmbH`(organisation)
- `Ludmilla Nottelmann`(person)

**Example 58** (doc_id: `deanon_TRAIN/4Ob119_22m`) (sent_id: `deanon_TRAIN/4Ob119_22m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Kodek sowie die Hofräte Dr. Schwarzenbacher, Dr. Nowotny und Hon.-Prof. PD Dr. Rassi und die Hofrätin Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei Hartwig Schimmangk KG, Pawel Lorenczyk, vertreten durch Dr. Franz Krainer, Rechtsanwalt in Graz, gegen die beklagte Partei Wien Bachtal GmbH, Kai Mündelein, vertreten durch die Hohenberg Rechtsanwälte GmbH in Graz, wegen 84.521,61 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz vom 12. Mai 2022, GZ 5 R 170/21s-33, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Wien Bachtal GmbH` — partial — gold is substring of pred: `Wien Bachtal GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hartwig Schimmangk`(person)
- `Pawel Lorenczyk`(person)
- `Wien Bachtal GmbH`(organisation)
- `Kai Mündelein`(person)

**Example 59** (doc_id: `deanon_TRAIN/4Ob145_18d`) (sent_id: `deanon_TRAIN/4Ob145_18d_4`)


Matzka und Dr. Parzmayr in der Rechtssache der klagenden Partei MGL Forschung Consulting GmbH, Lieselotte Wesp, vertreten durch Hauswirth - Kleiber Rechtsanwälte OG in Wien, gegen die beklagten Parteien 1) DI Amber Rzehatschek, 2) DI Esra Noth, ebendort, beide vertreten durch Dr. Herbert Salficky, Rechtsanwalt in Wien, 3) Trinks Möbel GmbH, Hütten 15, 5221 Lasberg, Österreich, vertreten durch Mag. Thomas Stenitzer und Mag. Kurt Schick, Rechtsanwälte in Laa an der Thaya, und 4) DI (FH) Wladimir Runzheimer, vertreten durch Mag. Bernhard Österreicher, Rechtsanwalt in Pfaffstätten, wegen 127.614,09 EUR sA und Feststellung (Streitwert: 5.200 EUR), über die außerordentliche Revision der erst- und zweitbeklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. April 2018, GZ 1 R 179/17a-29, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Forschung Consulting GmbH` — partial — pred is substring of gold: `MGL Forschung Consulting GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MGL Forschung Consulting GmbH`(organisation)
- `Lieselotte Wesp`(person)
- `DI Amber Rzehatschek`(person)
- `DI Esra Noth`(person)
- `Trinks Möbel GmbH`(organisation)
- `Hütten 15, 5221 Lasberg, Österreich`(address)
- `Wladimir Runzheimer`(person)

**Example 60** (doc_id: `deanon_TRAIN/4Ob149_13k`) (sent_id: `deanon_TRAIN/4Ob149_13k_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Tatjana Sellnow, vertreten durch Dr. Marcella Prunbauer, Rechtsanwältin in Wien, wider die beklagte Partei MittelAltalalTransport GmbH, Johann Haverkamp, vertreten durch Prof. Haslinger & Partner, Rechtsanwälte in Linz, wegen Unterlassung (Streitwert 40.000 EUR) und Urteilsveröffentlichung (Streitwert 4.000 EUR), im Verfahren über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 3. Juli 2013, GZ 2 R 55/13s-13, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Steyr vom 28. Jänner 2013, GZ 2 Cg 134/12t-9, bestätigt wurde, folgenden Beschluss gefasst:  Spruch Das Urteil vom 17. Dezember 2013, 4 Ob 149/13k, wird wie folgt berichtigt: 1.

**False Positives:**

- `Partei MittelAltalalTransport GmbH` — partial — gold is substring of pred: `MittelAltalalTransport GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tatjana Sellnow`(person)
- `MittelAltalalTransport GmbH`(organisation)
- `Johann Haverkamp`(person)

**Example 61** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei XDC Druck GmbH, Scarlett Augustus, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Wien, gegen die beklagte Partei UBER B.V., Larissa Ebele, Niederlande, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Unterlassung, Veröffentlichung und Feststellung (Streitwert im Sicherungsverfahren 70.000 EUR), über den Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 4. Juli 2018, GZ 3 R 32/18z-14, mit dem der Beschluss des Handelsgerichts Wien vom 24. April 2018, GZ 58 Cg 10/18f-6, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei XDC Druck GmbH` — partial — gold is substring of pred: `XDC Druck GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `XDC Druck GmbH`(organisation)
- `Scarlett Augustus`(person)
- `Larissa Ebele`(person)

**Example 62** (doc_id: `deanon_TRAIN/4Ob165_09g`) (sent_id: `deanon_TRAIN/4Ob165_09g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Schenk als Vorsitzende sowie die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Donostzor-Software AG, Florian Gretenkordt, vertreten durch Ewald Weninger Rechtsanwalts GmbH in Wien, gegen die beklagte Partei WienDigital Planung AG, KzlR Volker Chang, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Feststellung und Anfechtung (Streitwert: 101.000.000 EUR), im Verfahren über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Juni 2009, GZ 5 R 44/09s-15, womit das Urteil des Handelsgerichts Wien vom 26. Jänner 2008, GZ 19 Cg 98/08w-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Zurückziehung der außerordentlichen Revision der klagenden Partei dient zur Kenntnis.

**False Positives:**

- `Ewald Weninger Rechtsanwalts GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Donostzor-Software AG`(organisation)
- `Florian Gretenkordt`(person)
- `WienDigital Planung AG`(organisation)
- `KzlR Volker Chang`(person)

**Example 63** (doc_id: `deanon_TRAIN/4Ob18_20f`) (sent_id: `deanon_TRAIN/4Ob18_20f_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Jörg Drathschmidt, vertreten durch Dr. Winfried Sattlegger und andere Rechtsanwälte in Linz, gegen die beklagte Partei Wien Dorfsud GmbH, Gerlinde Balcerzak, vertreten durch Dr. Helmut Trenkwalder, Rechtsanwalt in Linz, und die Nebenintervenientin auf Seiten der beklagten Partei Waldfen-Versand GmbH, Eva Boztas, vertreten durch Schneider & Schneider Rechtsanwalts GmbH in Wien, wegen 35.628,94 EUR sA Zug um Zug gegen Herausgabe eines Fahrzeugs, über den Rekurs der Nebenintervenientin gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht vom 7. November 2019, GZ 6 R 114/19f-41, mit dem das Urteil des Landesgerichts Linz vom 3. Juli 2019, GZ 36 Cg 4/17m-36, im klagsstattgebenden Teil (Spruchpunkt 1.) aufgehoben wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Partei Wien Dorfsud GmbH` — partial — gold is substring of pred: `Wien Dorfsud GmbH`
- `Seiten der beklagten Partei Waldfen-Versand GmbH` — partial — gold is substring of pred: `Waldfen-Versand GmbH`
- `Schneider & Schneider Rechtsanwalts GmbH` — no gold match — likely missing annotation

> overlaps gold: 2  |  likely missing annotation: 1

**Gold Entities:**

- `Jörg Drathschmidt`(person)
- `Wien Dorfsud GmbH`(organisation)
- `Gerlinde Balcerzak`(person)
- `Waldfen-Versand GmbH`(organisation)
- `Eva Boztas`(person)

**Example 64** (doc_id: `deanon_TRAIN/4Ob194_22s`) (sent_id: `deanon_TRAIN/4Ob194_22s_4`)


Matzka und Dr. Annerl sowie die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Dueckers Wind GmbH, Corvin Cetinbag, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, gegen die beklagten Parteien 1. Wendy Goetzen (Verein), 2. Birkfeld+Münzenrieder Daten GmbH, beide Stegg 92, 3925 Neumelon, Österreich, vertreten durch Dr. Brigitte Birnbaum, Dr. Rainer Toperczer, Rechtsanwälte in Wien, wegen Unterlassung, Herausgabe, Feststellung und Urteilsveröffentlichung (Gesamtstreitwert 75.000 EUR), über die außerordentliche Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Juli 2022, GZ 2 R 47/22d-41, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Dueckers Wind GmbH` — partial — gold is substring of pred: `Dueckers Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dueckers Wind GmbH`(organisation)
- `Corvin Cetinbag`(person)
- `Wendy Goetzen`(person)
- `Birkfeld+Münzenrieder Daten GmbH`(organisation)
- `Stegg 92, 3925 Neumelon, Österreich`(address)

**Example 65** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Kraftheimglanz-Versand GmbH, OStR Dipl.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Kraftheimglanz-Versand GmbH` — partial — gold is substring of pred: `Kraftheimglanz-Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kraftheimglanz-Versand GmbH`(organisation)

**Example 66** (doc_id: `deanon_TRAIN/4Ob224_23d`) (sent_id: `deanon_TRAIN/4Ob224_23d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, den Hofrat Mag. Dr. Wurdinger und die Hofrätin Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Verlexglanz-Marine GmbH, Andreas Häntsch, Deutschland, vertreten durch die Saxinger Chalupsky & Partner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Emma Bergner kammer, Cathleen Hofschulte, vertreten durch Dr. Friedrich Schulz, Rechtsanwalt in Wien, wegen Unterlassung, Widerruf und Veröffentlichung desselben (Gesamtstreitwert 46.200 EUR), aus Anlass der außerordentlichen Revisionen der klagenden und der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 23. Oktober 2023, GZ 4 R 99/23t-32, mit dem das Urteil des Handelsgerichts Wien vom 27. April 2023, GZ 57 Cg 34/21g-24, bestätigt wurde, den Beschluss gefasst:  Spruch Die gemeinsame Anzeige beider Parteien vom 27. August 2024 über das vereinbarte Ruhen des Verfahrens wird zur Kenntnis genommen.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Verlexglanz-Marine GmbH` — partial — gold is substring of pred: `Verlexglanz-Marine GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Verlexglanz-Marine GmbH`(organisation)
- `Andreas Häntsch`(person)
- `Emma Bergner`(person)
- `Cathleen Hofschulte`(person)

**Example 67** (doc_id: `deanon_TRAIN/4Ob26_20g`) (sent_id: `deanon_TRAIN/4Ob26_20g_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Evelyn Peterhansel GmbH, Corbinian Wischnowski, LLM, vertreten durch Rechtsanwaltskanzlei Dr. Wendling GmbH in Kitzbühel, gegen die beklagte Partei Osttallem Getränke GmbH, Zdenko Weimer, BA, Deutschland, vertreten durch Dr. Dan Katzlinger, Rechtsanwalt in Innsbruck, wegen 70.000 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. Dezember 2019, GZ 10 R 49/19k-32, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei Evelyn Peterhansel GmbH` — partial — gold is substring of pred: `Evelyn Peterhansel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Evelyn Peterhansel`(person)
- `Corbinian Wischnowski, LLM`(person)
- `Osttallem Getränke GmbH`(organisation)
- `Zdenko Weimer, BA`(person)

**Example 68** (doc_id: `deanon_TRAIN/4Ob56_14k`) (sent_id: `deanon_TRAIN/4Ob56_14k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Andrea Schliekermann KG, Veit Faustmann, vertreten durch Dr. Ludwig Beurle und andere Rechtsanwälte in Linz, gegen die beklagte Partei Boerrigter Planung GmbH, Edith Merschmeier, vertreten durch Univ.-Prof. Dr. Bruno Binder und andere Rechtsanwälte in Linz, wegen 101.736,01 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. Februar 2014, GZ 6 R 12/14y-69, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Boerrigter Planung GmbH` — partial — gold is substring of pred: `Boerrigter Planung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Andrea Schliekermann`(person)
- `Veit Faustmann`(person)
- `Boerrigter Planung GmbH`(organisation)
- `Edith Merschmeier`(person)

**Example 69** (doc_id: `deanon_TRAIN/4Ob76_14a`) (sent_id: `deanon_TRAIN/4Ob76_14a_73`)


Die gesetzlichen Vergütungsansprüche könnten allerdings nur von Verwertungsgesellschaften geltend gemacht werden, weshalb der Beklagte die ihm an dem von ihm produzierten Filmen zustehenden gesetzlichen Vergütungsansprüche (einschließlich derjenigen an dem gegenständlichen Film) der Verwertungsgesellschaft für audio-visuelle Medien VAM GmbH zur treuhändigen Wahrnehmung abgetreten habe.

**False Positives:**

- `Medien VAM GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_TRAIN/4Ob9_20g`) (sent_id: `deanon_TRAIN/4Ob9_20g_4`)


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

**Example 71** (doc_id: `deanon_TRAIN/5Nc20_14g`) (sent_id: `deanon_TRAIN/5Nc20_14g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und die Hofrätin Dr. Lovrek sowie den Hofrat Dr. Höllwerth als weitere Richter in der Rechtssache der klagenden Partei Dr. Sean Schoenenborn, gegen die beklagte Partei Dr. Hagen Kanat, vertreten durch Eisenberger & Herzog Rechtsanwalts GmbH in Graz, wegen 234.164,98 EUR sA, über den Delegierungsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, gemäß § 31 JN anstelle des Landesgerichts für Zivilrechtssachen Graz das Landesgericht Wiener Neustadt, in eventu das Landesgericht Leoben, zur Verhandlung und Entscheidung dieser Rechtssache zu bestimmen, wird abgewiesen.

**False Positives:**

- `Eisenberger & Herzog Rechtsanwalts GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Sean Schoenenborn`(person)
- `Dr. Hagen Kanat`(person)

**Example 72** (doc_id: `deanon_TRAIN/5Ob129_18h`) (sent_id: `deanon_TRAIN/5Ob129_18h_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer, Mag. Painsi und Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Futerer u. Dirrnagel Luftfahrt GmbH, Susette Wülfken, vertreten durch Dr. Stefan Hoffmann, Dr. Thomas Herzog, Rechtsanwälte in Vöcklabruck, gegen die beklagte Partei Doris Grosscurth, vertreten durch Mag. Percy Hirsch, Rechtsanwalt in Wels, wegen 5.092,80 EUR sA, über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Wels als Berufungsgericht vom 25. April 2018, GZ 22 R 135/18m-47, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Dirrnagel Luftfahrt GmbH` — partial — pred is substring of gold: `Futerer u. Dirrnagel Luftfahrt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Futerer u. Dirrnagel Luftfahrt GmbH`(organisation)
- `Susette Wülfken`(person)
- `Doris Grosscurth`(person)

**Example 73** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Penners Medien GmbH, Wilhelmine Kobinger, vertreten durch Dr. Manfred Sommerbauer, DDr. Michael Dohr, LL.M., LL.M., Rechtsanwälte in Wiener Neustadt, gegen die beklagte Partei JRQA Landwirtschaft Rechtsanwälte GmbH, Kometenweg 43, 3200 Rennersdorf, Österreich, wegen Unterlassung (Streitwert 36.000 EUR) und Feststellung (Streitwert 3.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien vom 30. Mai 2022, GZ 5 R 6/22x-46, mit dem das Urteil des Handelsgerichts Wien vom 3. November 2021, GZ 21 Cg 21/21f-39, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Penners Medien GmbH` — partial — gold is substring of pred: `Penners Medien GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Penners Medien GmbH`(organisation)
- `Wilhelmine Kobinger`(person)
- `JRQA Landwirtschaft`(organisation)
- `Kometenweg 43, 3200 Rennersdorf, Österreich`(address)

**Example 74** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_22`)


[5] Die Klägerin argumentiere zudem mit ihrer Stellung als Minderheitsgesellschafterin an der GmbH und dem Umstand, dass die Beklagte die GmbH und gleichzeitig deren Mehrheitsgesellschafterin vertrete.

**False Positives:**

- `Stellung als Minderheitsgesellschafterin an der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_TRAIN/5Ob171_22s`) (sent_id: `deanon_TRAIN/5Ob171_22s_31`)


Das mit der dritten im Klagebegehren genannten Angelegenheit angestrebte per se-Verbot der Vertretung der GmbH gegenüber Dritten könne außerdem mit einem Interessenkonflikt zwischen der Gesellschaft und dem Mehrheitsgesellschafter keinesfalls begründet werden.

**False Positives:**

- `Das mit der dritten im Klagebegehren genannten Angelegenheit angestrebte per se-Verbot der Vertretung der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_TRAIN/5Ob184_21a`) (sent_id: `deanon_TRAIN/5Ob184_21a_4`)


Techn R Jaden Damcke, 2. Florian Adatepe, ebenda, beide vertreten durch Schlösser & Partner Rechtsanwälte OG in Wien, gegen die Antragsgegnerin Xenia Droeßler, vertreten durch Mag. Michael Operschal Rechtsanwalt GmbH in Wien, wegen § 37 Abs 1 Z 8 iVm § 16 MRG, über den Revisionsrekurs der Antragsteller gegen den Sachbeschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 19. Mai 2021, GZ 40 R 2/21x-15, mit dem der Sachbeschluss des Bezirksgerichts Floridsdorf vom 30. Oktober 2020, GZ 28 Msch 9/19g-11, abgeändert wurde, den Sachbeschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Operschal Rechtsanwalt GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Techn R Jaden Damcke`(person)
- `Florian Adatepe`(person)
- `Xenia Droeßler`(person)

**Example 77** (doc_id: `deanon_TRAIN/5Ob200_24h`) (sent_id: `deanon_TRAIN/5Ob200_24h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Wurzer als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Painsi, Dr. Weixelbraun-Mohr, Dr. Steger und Dr. Pfurtscheller als weitere Richter in der Rechtssache der klagenden Partei Ing. Harald Josepeit, vertreten durch die Wutte-Lang Rechtsanwalts GmbH in Klagenfurt, und der Nebenintervenientin auf Seiten der klagenden Partei MMag.

**False Positives:**

- `Lang Rechtsanwalts GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ing. Harald Josepeit`(person)

**Example 78** (doc_id: `deanon_TRAIN/5Ob200_24h`) (sent_id: `deanon_TRAIN/5Ob200_24h_4`)


Karen Marzy, vertreten durch Mag. Max Verdino, Mag. Gernot Funder, Mag. Eduard Sommeregger, Rechtsanwälte in St. Veit/Glan, gegen die beklagte Partei Textil Trabachfen GmbH, Christoph Rossmayer, vertreten durch Mag. Patrick Thun-Hohenstein, Rechtsanwalt in Salzburg, wegen 2.251 EUR sA und Feststellung (Streitwert 5.000 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 22. August 2024, GZ 1 R 139/24x-59, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 29. Februar 2024, GZ 20 C 100/22g-53, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei Textil Trabachfen GmbH` — partial — gold is substring of pred: `Textil Trabachfen GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Textil Trabachfen GmbH`(organisation)
- `Christoph Rossmayer`(person)

**Example 79** (doc_id: `deanon_TRAIN/5Ob221_22v`) (sent_id: `deanon_TRAIN/5Ob221_22v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Fabian + Michailoff Analyse GmbH in Liquidation, Steugasse 3, 6123 Vomperbach, Österreich, vertreten durch Mag. Gottfried Tazol, Rechtsanwalt in Völkermarkt, gegen die beklagte Partei SeeSanitär AG, Helge Schreyvogel, BEd, vertreten durch Mag. Alexander Todor-Kostic LL.M., Mag. Silke Todor-Kostic, Rechtsanwälte in Velden am Wörthersee, wegen 84.999,13 EUR sA, über die außerordentliche Revision der klagenden Partei (Revisionsinteresse 62.200,50 EUR sA) gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 12. Oktober 2022, GZ 5 R 74/22z-53, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Fabian + Michailoff Analyse GmbH` — partial — gold is substring of pred: `Fabian + Michailoff Analyse GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fabian + Michailoff Analyse GmbH`(organisation)
- `Steugasse 3, 6123 Vomperbach, Österreich`(address)
- `SeeSanitär AG`(organisation)
- `Helge Schreyvogel, BEd`(person)

**Example 80** (doc_id: `deanon_TRAIN/5Ob41_23z`) (sent_id: `deanon_TRAIN/5Ob41_23z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Erna Steinweh, vertreten durch Mag. Max Verdino ua, Rechtsanwälte in St. Veit an der Glan, gegen die beklagte Partei Sparkasse Laurence Holzbock, vertreten durch KS Kiechl Schaffer Rechtsanwalt GmbH in Wien, wegen 89.000 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 23. November 2022, GZ 4 R 157/22y-20, mit dem das Urteil des Landesgerichts Klagenfurt vom 30. Mai 2022, GZ 69 Cg 53/21p-16, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `KS Kiechl Schaffer Rechtsanwalt GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Erna Steinweh`(person)
- `Laurence Holzbock`(person)

**Example 81** (doc_id: `deanon_TRAIN/5Ob71_24p`) (sent_id: `deanon_TRAIN/5Ob71_24p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Mag. Wurzer als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Painsi, Dr. Weixelbraun-Mohr, Dr. Steger und Dr. Pfurtscheller als weitere Richter in der Rechtssache der klagenden Partei Ignaz Schaufel, vertreten durch die Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Mur Waldbach GmbH, StR Martin Leitenbauer, vertreten durch die Wolf Theiss Rechtsanwälte GmbH & Co KG in Wien, wegen 7.140 EUR und Feststellung (Streitwert 2.000 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Steyr als Berufungsgericht vom 8. Februar 2024, GZ 1 R 120/23z-43, mit dem das Urteil des Bezirksgerichts Steyr vom 28. September 2023, GZ 2 C 288/21x-39, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das Verfahren über die Revision der beklagten Partei wird bis zur Entscheidung des Gerichtshofs der Europäischen Union (EuGH) über die Vorabentscheidungsersuchen des Landgerichts Ravensburg (Deutschland) vom 9. November 2023, Rechtssache C-666/23, vom 9. November 2023, Rechtssache C-667/23, und vom 15. November 2023, Rechtssache C-668/23, unterbrochen.

**False Positives:**

- `Partei Mur Waldbach GmbH` — partial — gold is substring of pred: `Mur Waldbach GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ignaz Schaufel`(person)
- `Mur Waldbach GmbH`(organisation)
- `StR Martin Leitenbauer`(person)

**Example 82** (doc_id: `deanon_TRAIN/5Ob93_24y`) (sent_id: `deanon_TRAIN/5Ob93_24y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei Jozwiak Robotik GmbH, Florenzia Lohmöller, vertreten durch Rechtsanwälte Dr. Amhof & Dr. Damian GmbH in Wien, gegen die beklagte Partei Dipl.-Ing. Juliana Maurice, wegen Unterfertigung eines Wohnungseigentumsvertrags und Feststellung, hier: Anmerkung der Klage, über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 26. April 2024, GZ 15 R 41/24w-18, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 126 Abs 1 GBG iVm § 62 Abs 1 AußStrG zurückgewiesen.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Jozwiak Robotik GmbH` — partial — gold is substring of pred: `Jozwiak Robotik GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jozwiak Robotik GmbH`(organisation)
- `Florenzia Lohmöller`(person)
- `Dipl.-Ing. Juliana Maurice`(person)

**Example 83** (doc_id: `deanon_TRAIN/6Ob10_22x`) (sent_id: `deanon_TRAIN/6Ob10_22x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Nowotny, Dr. Hofer-Zeni-Rennhofer, Dr. Faber und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Mozar und Kuebler Daten Versicherungs AG, Grindelstraße 99, 4723 Tal, Österreich, vertreten durch Musey Rechtsanwalt GmbH in Salzburg, gegen die beklagte Partei Maschinenbau Ostlogber GmbH, Richarda Vetterer, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 7.246.839 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 1. Dezember 2021, GZ 2 R 165/21d-49, womit das Teil- und Zwischenurteil des Landesgerichts Salzburg vom 6. September 2021, GZ 6 Cg 16/20m-45, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Musey Rechtsanwalt GmbH` — no gold match — likely missing annotation
- `Partei Maschinenbau Ostlogber GmbH` — partial — gold is substring of pred: `Maschinenbau Ostlogber GmbH`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Mozar und Kuebler Daten`(organisation)
- `Grindelstraße 99, 4723 Tal, Österreich`(address)
- `Maschinenbau Ostlogber GmbH`(organisation)
- `Richarda Vetterer`(person)

</details>

---

## `German AG Entity`

**F1:** 0.029 | **Precision:** 0.097 | **Recall:** 0.017  

**Format:** `regex`  
**Description:**
Matches entities ending in 'AG' with strict boundary, excluding preceding legal terms and ensuring the name starts with a capital letter not preceded by 'Partei' or 'der'.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!Richter\s)(?<!Richterin\s)(?<!Senatspr\u00e4sident\s)(?<!Senatspr\u00e4sidentin\s)(?<!Hofrat\s)(?<!Hofr\u00e4tin\s)(?<!Hofr\u00e4t\s)(?<!Mag\.\s)(?<!Dr\.\s)(?<!Prof\.\s)(?<!Hon\.\s)(?<!Kanzlei\s)(?<!Anwalt\s)(?<!Gesellschafter\s)(?<!klagenden\s)(?<!beklagten\s)(?<!Nebenintervenient\s)(?<!Nebenintervenientin\s)(?<!Nebenintervenienten\s)(?<!Nebenintervenientinnen\s)(?<!Rechtssache\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)([A-Z][A-Za-z0-9\s&+\-]*[A-Z][A-Za-z0-9\s&+\-]*\s+AG|[A-Z][A-Z][A-Za-z0-9\s&+\-]*\s+AG)(?=[,\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.097 | 0.017 | 0.029 | 62 | 6 | 56 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 56 | 337 |

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

**Example 3** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_4`)


Logdercon-Digital, Dänemark, 2. Fengart GmbH, Oberer Weinweg 87, 9020 Klagenfurt, Österreich, beide vertreten durch Graf & Pitkowitz Rechtsanwälte GmbH in Wien, gegen die Beklagten 1. LGR Medien GmbH, OVX Finanzen, 2. Analyse Kelunizor AG, Fahnberg 42, 4100 Großamberg, Österreich, Deutschland, beide vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Gesamtstreitwert 69.500 EUR), über den Ordinationsantrag der Klägerinnen den Beschluss gefasst:  Spruch Dem Ordinationsantrag wird stattgegeben.

| Predicted | Gold |
|---|---|
| `Analyse Kelunizor AG` | `Analyse Kelunizor AG` |

**Missed by this rule (FN):**

- `Logdercon-Digital` (organisation)
- `Fengart GmbH` (organisation)
- `Oberer Weinweg 87, 9020 Klagenfurt, Österreich` (address)
- `LGR Medien GmbH` (organisation)
- `OVX Finanzen` (organisation)
- `Fahnberg 42, 4100 Großamberg, Österreich` (address)

**Example 4** (doc_id: `deanon_TRAIN/4Ob9_20g`) (sent_id: `deanon_TRAIN/4Ob9_20g_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Ing. KzlR MedR Brunhild Syndikus, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1) Böhnstedt+Bittlmeier Verlag GmbH, Wien Traalmon Betriebe, und 2) TraunBau AG, Schneeballenweg 6, 4232 Penzendorf, Österreich, beide vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 11.091,23 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 6. November 2019, GZ 2 R 158/19x-27, mit dem das Urteil des Landesgerichts Linz vom 29. August 2019, GZ 36 Cg 14/18h-22, bestätigt wurde, den Beschluss gefasst:  Spruch I. Das Revisionsverfahren zu 4 Ob 9/20g wird bis zur Vorabentscheidung des Gerichtshofs der Europäischen Union über das Vorabentscheidungsersuchen des Obersten Gerichtshofs vom 17.

| Predicted | Gold |
|---|---|
| `TraunBau AG` | `TraunBau AG` |

**Missed by this rule (FN):**

- `Ing. KzlR MedR Brunhild Syndikus` (person)
- `Böhnstedt+Bittlmeier Verlag GmbH` (organisation)
- `Wien Traalmon Betriebe` (organisation)
- `Schneeballenweg 6, 4232 Penzendorf, Österreich` (address)

**Example 5** (doc_id: `deanon_TRAIN/8Ob35_23i`) (sent_id: `deanon_TRAIN/8Ob35_23i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn und die Hofräte Dr. Stefula und Dr. Thunhart in der Rechtssache der klagenden Parteien 1. Pflege Deruni, und 2. Marchesi+Kusnezow Transport AG, Grabenseeweg 48, 8272 Ebersdorf, Österreich, beide vertreten durch Dr. Heinrich Fassl, Rechtsanwalt in Wien, wider die beklagte Partei DI Valerie Wilczenski, vertreten durch Dr. Andreas A. Lintl, Rechtsanwalt in Wien, wegen 59.868,50 EUR sA und 170.440,94 EUR sA, über die Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Wien vom 26. Jänner 2023, GZ 11 R 235/22t-206, mit welchem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 30. Mai 2022, GZ 20 Cg 11/15g-194, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Marchesi+Kusnezow Transport AG` | `Marchesi+Kusnezow Transport AG` |

**Missed by this rule (FN):**

- `Pflege Deruni` (organisation)
- `Grabenseeweg 48, 8272 Ebersdorf, Österreich` (address)
- `DI Valerie Wilczenski` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob102_18z`) (sent_id: `deanon_TRAIN/10Ob102_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG, Adelheid Lochmaier, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Ursula Antoniadis, vertreten durch Knirsch – Braun – Fellner Rechtsanwälte in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 5. September 2018, GZ 40 R 39/18h-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG` — partial — gold is substring of pred: `Skrzypczik + Duchscherer Digital AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Skrzypczik + Duchscherer Digital AG`(organisation)
- `Adelheid Lochmaier`(person)
- `Ursula Antoniadis`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Ob2_20x`) (sent_id: `deanon_TRAIN/10Ob2_20x_4`)


Matzka und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Ignaz Jungmichel, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei TalAlvalRobotik AG, Delila Leiteritz, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 25.617,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 29. Oktober 2019, GZ 2 R 151/19t-23, mit dem das Urteil des Landesgerichts Linz vom 21. August 2019, GZ 5 Cg 118/18z-19, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

**False Positives:**

- `Partei TalAlvalRobotik AG` — partial — gold is substring of pred: `TalAlvalRobotik AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ignaz Jungmichel`(person)
- `TalAlvalRobotik AG`(organisation)
- `Delila Leiteritz`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob31_16f`) (sent_id: `deanon_TRAIN/10Ob31_16f_3`)


Kopf Der Oberste Gerichtshof als Revisionsgericht hat durch den Hofrat Univ.-Prof. Dr. Neumayr als Vorsitzenden und den Hofrat Dr. Schramm, die Hofrätinnen Dr. Fichtenau und Dr. Tarmann-Prentner sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1060 Wien, Linke Wienzeile 18, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei CESW Technik Services AG, Mike Zachariä, vertreten durch Doralt Seist Csoklich Rechtsanwalts-Partnerschaft in Wien, wegen Unterlassung (30.500 EUR) und Urteilsveröffentlichung (5.500 EUR) über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Jänner 2016, GZ 30 R 35/15k-13, womit das Urteil des Landesgerichts St. Pölten vom 17. Juli 2015, GZ 3 Cg 7/15w-9, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Partei CESW Technik Services AG` — partial — gold is substring of pred: `CESW Technik Services AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `CESW Technik Services AG`(organisation)
- `Mike Zachariä`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob33_15y`) (sent_id: `deanon_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Inn Sudconkraft AG, Elisabeth Breitschwerdt, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Mazik Heizung GmbH, Hemma Rahn, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Inn Sudconkraft AG` — partial — gold is substring of pred: `Inn Sudconkraft AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Sudconkraft AG`(organisation)
- `Elisabeth Breitschwerdt`(person)
- `Mazik Heizung GmbH`(organisation)
- `Hemma Rahn`(person)

**Example 4** (doc_id: `deanon_TRAIN/1Ob106_20z`) (sent_id: `deanon_TRAIN/1Ob106_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Kodek, Mag. Wurzer, Mag. Dr. Wurdinger und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei IGK Bau Consulting AG, Ariadne Seebalt, vertreten durch Dr. Manfred Angerer und andere Rechtsanwälte in Klagenfurt am Wörthersee, gegen die beklagte Partei DI Roxana Pöll, vertreten durch Mag. Claudia Egarter, Rechtsanwältin in Klagenfurt am Wörthersee, wegen 5.457.559,15 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 28. Februar 2020, GZ 2 R 9/20s-150, mit dem das Urteil des Landesgerichts Klagenfurt vom 20. Februar 2017, GZ 21 Cg 24/13h-102, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei IGK Bau Consulting AG` — partial — gold is substring of pred: `IGK Bau Consulting AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `IGK Bau Consulting AG`(organisation)
- `Ariadne Seebalt`(person)
- `DI Roxana Pöll`(person)

**Example 5** (doc_id: `deanon_TRAIN/1Ob16_20i`) (sent_id: `deanon_TRAIN/1Ob16_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Stadt Christina Schorer, vertreten durch die Benn-Ibler Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Donsteinlex AG, Natalie Gieseking, MSc, vertreten durch die Weber Rechtsanwälte GmbH & Co KG, Wien, wegen 312.706,88 EUR sowie Feststellung (Streitwert 80.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Oktober 2019, GZ 6 R 71/19g-17, mit dem das Urteil des Landesgerichts Steyr vom 29. März 2019, GZ 9 Cg 39/18g-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Donsteinlex AG` — partial — gold is substring of pred: `Donsteinlex AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Christina Schorer`(person)
- `Donsteinlex AG`(organisation)
- `Natalie Gieseking, MSc`(person)

**Example 6** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Dr. Wurdinger als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Steger, Mag. Wessely-Kristöfel, Dr. Parzmayr und Dr. Pfurtscheller als weitere Richterinnen und Richter in der Rechtssache der klagenden Partei Bundeskammer für Arbeiter und Angestellte, Wien 4, Prinz-Eugen-Straße 20–22, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Alsynwald-Recycling AG, RgR Mag. Dr. Evelyn Steinkröger, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH in Wien, wegen Unterlassung und Urteilsveröffentlichung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. Juli 2024, GZ 2 R 77/24v-15, mit dem das Urteil des Handelsgerichts Wien vom 28. Februar 2024, GZ 57 Cg 36/23d-8, bestätigt wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Alsynwald-Recycling AG` — partial — gold is substring of pred: `Alsynwald-Recycling AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alsynwald-Recycling AG`(organisation)
- `RgR Mag. Dr. Evelyn Steinkröger`(person)

**Example 7** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_115`)


3. Klausel 5: „2. Änderungen Z 2. (1) Änderungen dieser zwischen dem Kunden und dem Kreditinstitut vereinbarten Bedingungen gelten nach Ablauf von zwei Monaten ab Zugang der Mitteilung der angebotenen Änderungen an den Kunden als vereinbart, sofern bis dahin kein schriftlicher Widerspruch des Kunden bei der DFA Planung AG einlangt.

**False Positives:**

- `Widerspruch des Kunden bei der DFA Planung AG` — partial — gold is substring of pred: `DFA Planung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DFA Planung AG`(organisation)

**Example 8** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_116`)


Die Nieder Norber AG wird den Kunden in der Mitteilung auf die Änderungen hinweisen und darauf aufmerksam machen, dass sein Stillschweigen nach Ablauf der zwei Monate ab Zugang der Mitteilung durch das Unterlassen eines Widerspruchs in Schriftform als Zustimmung zu den Änderungen gilt.

**False Positives:**

- `Die Nieder Norber AG` — partial — gold is substring of pred: `Nieder Norber AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Norber AG`(organisation)

**Example 9** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_118`)


auch darauf wird die Landwerlin&Plumke Versand AG in derMitteilung hinweisen.

**False Positives:**

- `Plumke Versand AG` — partial — pred is substring of gold: `Landwerlin&Plumke Versand AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landwerlin&Plumke Versand AG`(organisation)

**Example 10** (doc_id: `deanon_TRAIN/1Ob226_20x`) (sent_id: `deanon_TRAIN/1Ob226_20x_54`)


C-620/17,Hochtief Solutions AG, Rn 35, jeweils mwN).

**False Positives:**

- `Hochtief Solutions AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_6`)


Text Gründe: Mit dem angefochtenen Erkenntnis wurde Dr. Nadja Köpers, Rechtsanwalt in Laahen 3, 3240 Pölla, Österreich, wegen des Verstoßes gegen die Bestimmungen des § 9 (Abs 1) RAO und des § 2 RL-BA der Disziplinarvergehen der Verletzung von Berufspflichten und der Beeinträchtigung von Ehre oder (richtig:) Ansehen des Standes nach § 1 Abs 1 erster und zweiter Fall DSt schuldig erkannt, weil er als Rechtsvertreter der Ehegatten Roman und Elfriede Jakubus in Anträgen auf Aufschiebung der Zwangsversteigerungen für seine Mandanten vom 5. September 2013 in näher bezeichneten Verfahren des Bezirksgerichts Innsbruck und des Bezirksgerichts Amstetten sowie in einer näher genannten Feststellungsklage an das Landesgericht Linz vom 7. Oktober 2013 und in einer Impugnationsklage an das Bezirksgericht Amstetten vom 10. Oktober 2013 jeweils vorgebracht hatte, seine Mandanten hätten sämtliche Verpflichtungen aus einer mit der Bachseewald Heizung AG abgeschlossenen Vereinbarung vom 11. Dezember 2012, insbesondere jene zur unwiderruflichen Antragstellung auf Aufhebung der Höfeeigenschaft einer näher bezeichnenden Liegenschaft in Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich, eingehalten, obwohl ihm zum Zeitpunkt der Antragstellung und Klagseinbringung bekannt war, dass der Antrag auf Aufhebung der Höfeeigenschaft vom 13. Dezember 2012 bereits am 14. Juni 2013 von Roman Janis, durch ihn vertreten, entgegen der zuvor genannten Vereinbarung vom 11. Dezember 2012 wieder zurückgezogen worden war.

**False Positives:**

- `Verpflichtungen aus einer mit der Bachseewald Heizung AG` — partial — gold is substring of pred: `Bachseewald Heizung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Nadja Köpers`(person)
- `Laahen 3, 3240 Pölla, Österreich`(address)
- `Jakubus`(person)
- `Bachseewald Heizung AG`(organisation)
- `Wallsiedlung 66, 8044 Purgstall bei Eggersdorf, Österreich`(address)
- `Janis`(person)

**Example 12** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_9`)


Die Besetzungsrüge (Z 1) zeigt zwar keine Tatsachengrundlage für die reklamierte Ausgeschlossenheit des Vorsitzenden des Disziplinarrats wegen Befangenheit (§ 43 Abs 1 Z 3 StPO iVm § 77 Abs 3 DSt) auf, weil aufgrund der Mitteilung des Genannten vom 5. Dezember 2014, wonach er keine Veranlassung sehe, seine „rechtsgeschäftlichen Kontakte“ dem Disziplinarbeschuldigten gegenüber offenzulegen, entgegen dem rein spekulativen Berufungsstandpunkt nicht „anzunehmen ist, dass ein berufsbedingtes Naheverhältnis“ des Vorsitzenden des Disziplinarrats zur Traun Lemalnor AG (Prozessgegnerin der vom Disziplinarbeschuldigten vertretenen Mandanten)“ besteht (vgl RIS-Justiz RS0125768, RS0097054).

**False Positives:**

- `Vorsitzenden des Disziplinarrats zur Traun Lemalnor AG` — partial — gold is substring of pred: `Traun Lemalnor AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Traun Lemalnor AG`(organisation)

**Example 13** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei OMedR Eleonore Wunderling, 9020 Klagenfurt, vertreten durch Mag. Michael Hirm, Rechtsanwalt in Klagenfurt, sowie der Nebenintervenientin auf Seiten der klagenden Partei Fildhaut & Claeser Forschung AG, Amanda Deutschlender, vertreten durch Dr. Martin Wuelz, Rechtsanwalt in Innsbruck, gegen die beklagten Parteien 1.

**False Positives:**

- `Seiten der klagenden Partei Fildhaut & Claeser Forschung AG` — partial — gold is substring of pred: `Fildhaut & Claeser Forschung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OMedR Eleonore Wunderling`(person)
- `Fildhaut & Claeser Forschung AG`(organisation)
- `Amanda Deutschlender`(person)

**Example 14** (doc_id: `deanon_TRAIN/3Ob164_20v`) (sent_id: `deanon_TRAIN/3Ob164_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Bruckgartver GmbH, MedR StR René Titz, vertreten durch Dr. Reinhard Schanda, Rechtsanwalt in Wien, gegen die beklagte Partei Ofczarczik Planung AG, Dipl.

**False Positives:**

- `Partei Ofczarczik Planung AG` — partial — gold is substring of pred: `Ofczarczik Planung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bruckgartver GmbH`(organisation)
- `MedR StR René Titz`(person)
- `Ofczarczik Planung AG`(organisation)

**Example 15** (doc_id: `deanon_TRAIN/3Ob215_19t`) (sent_id: `deanon_TRAIN/3Ob215_19t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie die Hofräte Dr. Roch und Priv.-Doz. Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Bartholomäus Kurth, vertreten durch die Torggler Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Traberval AG, Vera Lindenstruth, vertreten durch Dr. Manfred Angerer ua, Rechtsanwälte in Klagenfurt am Wörthersee, wegen 300.000 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 10. September 2019, GZ 5 R 68/19p-19, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Traberval AG` — partial — gold is substring of pred: `Traberval AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bartholomäus Kurth`(person)
- `Traberval AG`(organisation)
- `Vera Lindenstruth`(person)

**Example 16** (doc_id: `deanon_TRAIN/4Ob165_09g`) (sent_id: `deanon_TRAIN/4Ob165_09g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Schenk als Vorsitzende sowie die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Donostzor-Software AG, Florian Gretenkordt, vertreten durch Ewald Weninger Rechtsanwalts GmbH in Wien, gegen die beklagte Partei WienDigital Planung AG, KzlR Volker Chang, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Feststellung und Anfechtung (Streitwert: 101.000.000 EUR), im Verfahren über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Juni 2009, GZ 5 R 44/09s-15, womit das Urteil des Handelsgerichts Wien vom 26. Jänner 2008, GZ 19 Cg 98/08w-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Zurückziehung der außerordentlichen Revision der klagenden Partei dient zur Kenntnis.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Donostzor-Software AG` — partial — gold is substring of pred: `Donostzor-Software AG`
- `Partei WienDigital Planung AG` — partial — gold is substring of pred: `WienDigital Planung AG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Donostzor-Software AG`(organisation)
- `Florian Gretenkordt`(person)
- `WienDigital Planung AG`(organisation)
- `KzlR Volker Chang`(person)

**Example 17** (doc_id: `deanon_TRAIN/4Ob188_14x`) (sent_id: `deanon_TRAIN/4Ob188_14x_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Bachkelwerk Pflege AG, Eva Selcuk, vertreten durch Ebert Huber Swoboda Oswald & Partner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Christiane Rechenauer e.U., Dossenweg 6, 4924 Dundeck, Österreich, vertreten durch Dr. Patrick Ruth, Rechtsanwalt in Innsbruck, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 34.900 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz vom 5. August 2014, GZ 2 R 139/14w-13, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Bachkelwerk Pflege AG` — partial — gold is substring of pred: `Bachkelwerk Pflege AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bachkelwerk Pflege AG`(organisation)
- `Eva Selcuk`(person)
- `Christiane Rechenauer`(person)
- `Dossenweg 6, 4924 Dundeck, Österreich`(address)

**Example 18** (doc_id: `deanon_TRAIN/4Ob19_10p`) (sent_id: `deanon_TRAIN/4Ob19_10p_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Traun-Sanitär gesellschaft mbH,*****, vertreten durch Prof. Haslinger & Partner, Rechtsanwälte in Linz, gegen die beklagte Partei NWJ KI Dienstleistungen AG,*****, vertreten durch Rechtsanwälte Konrad & Schröttner OG in Graz, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 65.000 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 25. November 2009, GZ 6 R 169/09h-37, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei NWJ KI Dienstleistungen AG` — partial — gold is substring of pred: `NWJ KI Dienstleistungen AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Traun-Sanitär gesellschaft mbH`(organisation)
- `NWJ KI Dienstleistungen AG`(organisation)

**Example 19** (doc_id: `deanon_TRAIN/4Ob90_16p`) (sent_id: `deanon_TRAIN/4Ob90_16p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Vogel als Vorsitzenden und die Hofräte Dr. Jensik, Dr. Musger, Dr. Schwarzenbacher und Dr. Rassi als weitere Richter in der Rechtssache der klagenden Partei Lebensmittel Glanzconuni AG, Immanuel Gspan, vertreten durch Fellner Wratzfeld & Partner Rechtsanwälte GmbH in Wien, gegen die beklagten Parteien 1. Fridolin Braunhold, 2. Mag. Frauke Steinweg, und 3. DonauLexlogbruckPlanung GmbH, Felberbachstraße 4, 3631 Jungschlag, Österreich, alle vertreten durch Dr. Peter Zöchbauer, Rechtsanwalt in Wien, wegen Unterlassung (Streitwert 102.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Februar 2016, GZ 2 R 93/15h-25, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Lebensmittel Glanzconuni AG` — partial — gold is substring of pred: `Lebensmittel Glanzconuni AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lebensmittel Glanzconuni AG`(organisation)
- `Immanuel Gspan`(person)
- `Fridolin Braunhold`(person)
- `Mag. Frauke Steinweg`(person)
- `DonauLexlogbruckPlanung GmbH`(organisation)
- `Felberbachstraße 4, 3631 Jungschlag, Österreich`(address)

**Example 20** (doc_id: `deanon_TRAIN/5Ob102_24x`) (sent_id: `deanon_TRAIN/5Ob102_24x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei OSR Wolfram Dag, MA, wider die beklagte Partei MLUD Pharma Planung AG, Leila Wildvang, Deutschland vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 13.607,40 EUR sA und Feststellung über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Ried im Innkreis als Berufungsgericht vom 13. März 2024, GZ 18 R 2/24k-29, mit dem das Urteil des Bezirksgerichts Schärding vom 6. November 2023, GZ 2 C 478/20g-24, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei MLUD Pharma Planung AG` — partial — gold is substring of pred: `MLUD Pharma Planung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OSR Wolfram Dag, MA`(person)
- `MLUD Pharma Planung AG`(organisation)
- `Leila Wildvang`(person)

**Example 21** (doc_id: `deanon_TRAIN/5Ob141_23f`) (sent_id: `deanon_TRAIN/5Ob141_23f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei OMedR Univ.-Prof.in Eugenia Breitenfelder, vertreten durch Poduschka Partner AnwaltsGmbH in Linz, gegen die beklagte Partei Werkfurtval-Lebensmittel AG, Meinrad Birkenmeyer, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 19.600 EUR sA über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 22. Mai 2023, GZ 12 R 6/23y-34, mit dem das Urteil des Landesgerichts Wels vom 11. Jänner 2023, GZ 8 Cg 29/20s-29, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Partei Werkfurtval-Lebensmittel AG` — partial — gold is substring of pred: `Werkfurtval-Lebensmittel AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OMedR Univ.-Prof.in Eugenia Breitenfelder`(person)
- `Werkfurtval-Lebensmittel AG`(organisation)
- `Meinrad Birkenmeyer`(person)

**Example 22** (doc_id: `deanon_TRAIN/5Ob141_23f`) (sent_id: `deanon_TRAIN/5Ob141_23f_17`)


Ende des Jahres 2018 schloss er sich der deutschen Musterfeststellungsklage gegen die Conkraftnor-Event AG an.

**False Positives:**

- `Ende des Jahres 2018 schloss er sich der deutschen Musterfeststellungsklage gegen die Conkraftnor-Event AG` — partial — gold is substring of pred: `Conkraftnor-Event AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Conkraftnor-Event AG`(organisation)

**Example 23** (doc_id: `deanon_TRAIN/6Ob10_22x`) (sent_id: `deanon_TRAIN/6Ob10_22x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Nowotny, Dr. Hofer-Zeni-Rennhofer, Dr. Faber und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Mozar und Kuebler Daten Versicherungs AG, Grindelstraße 99, 4723 Tal, Österreich, vertreten durch Musey Rechtsanwalt GmbH in Salzburg, gegen die beklagte Partei Maschinenbau Ostlogber GmbH, Richarda Vetterer, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 7.246.839 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 1. Dezember 2021, GZ 2 R 165/21d-49, womit das Teil- und Zwischenurteil des Landesgerichts Salzburg vom 6. September 2021, GZ 6 Cg 16/20m-45, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Mozar und Kuebler Daten Versicherungs AG` — partial — gold is substring of pred: `Mozar und Kuebler Daten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mozar und Kuebler Daten`(organisation)
- `Grindelstraße 99, 4723 Tal, Österreich`(address)
- `Maschinenbau Ostlogber GmbH`(organisation)
- `Richarda Vetterer`(person)

**Example 24** (doc_id: `deanon_TRAIN/6Ob231_24z`) (sent_id: `deanon_TRAIN/6Ob231_24z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Hofer-Zeni-Rennhofer als Vorsitzende sowie die Hofrätinnen und Hofräte Hon.-Prof. Dr. Faber, Mag. Pertmayr, Dr. Weber und Mag. Nigl LL.M. als weitere Richter in der Rechtssache der klagenden Partei Ing. Egon Jurguttis, vertreten durch Poduschka Partner Anwaltsgesellschaft mbH in Linz, wider die beklagte Partei UnterFinanzen AG, Silvius Haagmans, Deutschland, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 9.600 EUR sA, im Verfahren über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Linz als Berufungsgericht vom 7. Oktober 2024, GZ 6 R 57/24b-31, womit das Urteil des Bezirksgerichts Traun vom 16. Februar 2024, GZ 2 C 198/23z-22, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei vom 9. Dezember 2025 auf Fortsetzung des Verfahrens wird abgewiesen.

**False Positives:**

- `Partei UnterFinanzen AG` — partial — gold is substring of pred: `UnterFinanzen AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Egon Jurguttis`(person)
- `UnterFinanzen AG`(organisation)
- `Silvius Haagmans`(person)

**Example 25** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_31`)


Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG wäre hinsichtlich § 14 Abs 3 FBG sachlich nicht gerechtfertigt.

**False Positives:**

- `Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_52`)


Auch wenn die Prüfpflichten des Revisionsverbands gemäß § 28 Abs 4 WGG die Genehmigungspflicht durch die Landesregierung beim Erwerb von Anteilen an Unternehmungen mit dem überwiegenden Geschäftszweck des (un-)mittelbaren Erwerbs/Haltens/Verwaltens von Anteilen an Bauvereinigungen nach § 10a WGG erfassten, sei nicht anzunehmen, der Gesetzgeber habe in § 14 Abs 3 FBG die Möglichkeit, gemeinnützige Bauvereinigungen auch in der Rechtsform der GmbH oder der AG zu betreiben, vergessen.

**False Positives:**

- `Bauvereinigungen auch in der Rechtsform der GmbH oder der AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_64`)


Eine Unterscheidung dahingehend, dass § 14 Abs 3 FBG dem Revisionsverband Parteistellung nur bei gemeinnützigen Bauvereinigungen in der Rechtsform einer Genossenschaft, nicht aber auch einer GmbH oder AG zuerkenne, wäre sachlich nicht gerechtfertigt.

**False Positives:**

- `GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_66`)


Die Bestimmung sei daher analog auch auf gemeinnützige Bauvereinigungen in der Rechtsform der GmbH oder AG anzuwenden.

**False Positives:**

- `Bauvereinigungen in der Rechtsform der GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_107`)


Wenn nun kraft ausdrücklicher gesetzlicher Vorschrift gemeinnützige Bauvereinigungen auch in den Rechtsformen einer GmbH oder AG erlaubt sind (§ 1 Abs 1 WGG) und gleichzeitig auch für diese die Pflicht statuiert wird, einem Revisionsverband anzugehören (§ 5 Abs 1 WGG), so ist auch für eine in der Rechtsform einer GmbH oder AG bestehende Bauvereinigung der Revisionsverband als „zuständig“ im Sinn von § 14 Abs 3 FBG und demgemäß insoweit als Amtspartei anzusehen.

**False Positives:**

- `Bauvereinigungen auch in den Rechtsformen einer GmbH oder AG` — no gold match — likely missing annotation
- `GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 30** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_111`)


Es muss daher davon ausgegangen werden, dass sowohl der Gesetzgeber des FBG als auch der mehrfache (Novellen-)Gesetzgeber des WGG die Zuständigkeit des Revisionsverbands für Bauvereinigungen in der Rechtsform einer GmbH oder AG übersehen hat.

**False Positives:**

- `Bauvereinigungen in der Rechtsform einer GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_112`)


Es liegt nach Ansicht des Senats daher insoweit eine durch Analogie zu füllende Gesetzeslücke dahingehend vor, dass der für eine gemeinnützige Bauvereinigung zuständige Revisionsverband auch dann Amtspartei im Sinne des § 14 Abs 3 FBG ist, wenn die Bauvereinigung nicht in der Rechtsform einer Erwerbs- und Wirtschaftsgenossenschaft, sondern einer GmbH oder AG besteht (in diesem Sinn auchSchwetz/Gahler, Wohnungsgemeinnützigkeit und Firmenbuch – Wechselwirkung und Spannungsbogen?

**False Positives:**

- `GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_TRAIN/6Ob47_25t`) (sent_id: `deanon_TRAIN/6Ob47_25t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Hofer-Zeni-Rennhofer als Vorsitzende sowie die Hofrätinnen und Hofräte Dr. Faber, Mag. Pertmayr, Dr. Weber und Mag. Nigl LL.M. als weitere Richter in der Rechtssache der klagenden Partei Timothy Scheppan, vertreten durch Dr. Alexander Amann LL.M., Rechtsanwalt in Gamprin-Bendern, Liechtenstein, wider die beklagte Partei Nord-Luftfahrt AG, Niklas Kühlewind, Deutschland, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 71.888,75 EUR sA Zug um Zug gegen die Rückstellung eines Fahrzeugs, in eventu wegen 17.972,19 EUR sA und Feststellung, im Verfahren über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Jänner 2025, GZ 11 R 7/25t-63, den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Partei Nord-Luftfahrt AG` — partial — gold is substring of pred: `Nord-Luftfahrt AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Timothy Scheppan`(person)
- `Nord-Luftfahrt AG`(organisation)
- `Niklas Kühlewind`(person)

**Example 33** (doc_id: `deanon_TRAIN/6Ob51_21z`) (sent_id: `deanon_TRAIN/6Ob51_21z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Univ.-Prof. Dr. Kodek, Dr. Nowotny, Dr. Faber und Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei Mag. Frank Mahrhold, vertreten durch Dr. Wolfgang Haslinger, LL.M., Rechtsanwalt in Wien, gegen die beklagte Partei PKLA Textil Bank Verwilnex Betriebe AG, Valerie Kallweidt, vertreten durch Dr. Anton Ehm und Mag. Thomas Mödlagl, Rechtsanwälte in Wien, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Jänner 2021, GZ 3 R 63/20m-18, mit dem das Urteil des Handelsgerichts Wien vom 7. September 2020, GZ 56 Cg 9/20x-14, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wirdFolge gegeben.

**False Positives:**

- `Partei PKLA Textil Bank Verwilnex Betriebe AG` — partial — gold is substring of pred: `PKLA Textil`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Frank Mahrhold`(person)
- `PKLA Textil`(organisation)
- `Verwilnex Betriebe AG`(organisation)
- `Valerie Kallweidt`(person)

**Example 34** (doc_id: `deanon_TRAIN/7Nc6_13m`) (sent_id: `deanon_TRAIN/7Nc6_13m_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Huber als Vorsitzende und die Hofrätinnen und Hofräte Dr. Hoch, Dr. Kalivoda, Mag. Dr. Wurdinger und Mag. Malesich als weitere Richter in der Arbeitsrechtssache der klagenden Partei Dr. Norbert Overdick, vertreten durch Dr. Clemens Gärner, Rechtsanwalt in Wien, gegen die beklagte Partei Daten Lexunilog AG, Marlon Jerabeck, vertreten durch Dr. Helmut Engelbrecht und andere Rechtsanwälte in Wien, wegen 4.868,07 EUR sA und Feststellung, über die Befangenheitsanzeige des Hofrats des Obersten Gerichtshofs Dr. Richard Hargassner im Verfahren 9 ObA 29/13z den Beschluss gefasst:  Spruch Der Hofrat des Obersten Gerichtshofs Dr. Richard Hargassner ist ausgeschlossen.

**False Positives:**

- `Partei Daten Lexunilog AG` — partial — gold is substring of pred: `Daten Lexunilog AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Norbert Overdick`(person)
- `Daten Lexunilog AG`(organisation)
- `Marlon Jerabeck`(person)

**Example 35** (doc_id: `deanon_TRAIN/7Ob162_20d`) (sent_id: `deanon_TRAIN/7Ob162_20d_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei DDr.in Gisela Loy, vertreten durch Mag. Marco und Mag. Amelie Kunczicky, Rechtsanwälte in Mayrhofen, gegen die beklagte Partei Helferich & Zeitler Marine AG, Jessica Seebald, vertreten durch Mag. Thomas Anker und DI Mag. Nikolaus Gratl, Rechtsanwäte in Innsbruck, wegen Urkundeneinsicht, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. Juni 2020, GZ 4 R 55/20z-18, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Helferich & Zeitler Marine AG` — partial — gold is substring of pred: `Helferich & Zeitler Marine AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DDr.in Gisela Loy`(person)
- `Helferich & Zeitler Marine AG`(organisation)
- `Jessica Seebald`(person)

**Example 36** (doc_id: `deanon_TRAIN/7Ob165_23z`) (sent_id: `deanon_TRAIN/7Ob165_23z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und die Hofräte Mag. Dr. Wurdinger, Mag. Malesich, Dr. Weber und Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Mag. Norbert Faulwasser, vertreten durch Mag. Alexandra Schwarz, Rechtsanwältin in Wien, gegen die beklagte Partei AlpenMaschinenbau AG, Sibylle von Wachtendonk, vertreten durch Dr. Günter Niebauer, Rechtsanwalt in Wien, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Juli 2023, GZ 3 R 74/23h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei AlpenMaschinenbau AG` — partial — gold is substring of pred: `AlpenMaschinenbau AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Norbert Faulwasser`(person)
- `AlpenMaschinenbau AG`(organisation)
- `Sibylle von Wachtendonk`(person)

**Example 37** (doc_id: `deanon_TRAIN/7Ob55_25a`) (sent_id: `deanon_TRAIN/7Ob55_25a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Malesich, Dr. Weber, Mag. Fitz und Mag. Jelinek als weitere Richter in der Rechtssache der klagenden Partei Laurin Tieltges, vertreten durch die Poduschka Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Guender Medien AG, Lothar Sax, vertreten durch die CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 6.090 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 13. Dezember 2024, GZ 2 R 125/24g-42, mit dem das Urteil des Bezirksgerichts Innsbruck vom 28. Mai 2024, GZ 26 C 450/20h-37, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei Guender Medien AG` — partial — gold is substring of pred: `Guender Medien AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Laurin Tieltges`(person)
- `Guender Medien AG`(organisation)
- `Lothar Sax`(person)

**Example 38** (doc_id: `deanon_TRAIN/7Ob85_15y`) (sent_id: `deanon_TRAIN/7Ob85_15y_4`)


Cynthia Martchenko AG, Schmidhuberstraße 73, 4792 Landertsberg, Österreich, vertreten durch Jank Weiler Operenyi Rechtsanwälte OG in Wien, 2. Reisch + Weißert Getränke AG und 3.

**False Positives:**

- `Cynthia Martchenko AG` — partial — gold is substring of pred: `Cynthia Martchenko`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Cynthia Martchenko`(person)
- `Schmidhuberstraße 73, 4792 Landertsberg, Österreich`(address)
- `Reisch + Weißert Getränke AG`(organisation)

**Example 39** (doc_id: `deanon_TRAIN/7Ob92_19h`) (sent_id: `deanon_TRAIN/7Ob92_19h_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Tosca Janetscheck, vertreten durch Dr. Herwig Ernst, Rechtsanwalt in Korneuburg, gegen die beklagte Partei Domingo + Sinner Robotik AG Liliana Böbe, vertreten durch Dr. Herbert Laimböck, Rechtsanwalt in Wien, wegen 521.151,28 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. April 2019, GZ 5 R 32/19s-29, womit das Urteil des Handelsgerichts Wien vom 14. Jänner 2019, GZ 10 Cg 70/17z-25, bestätigt wurde, beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Domingo + Sinner Robotik AG` — partial — gold is substring of pred: `Domingo + Sinner Robotik AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tosca Janetscheck`(person)
- `Domingo + Sinner Robotik AG`(organisation)
- `Liliana Böbe`(person)

**Example 40** (doc_id: `deanon_TRAIN/7Ob94_20d`) (sent_id: `deanon_TRAIN/7Ob94_20d_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Mag. Bernhard Siegloch, vertreten durch Brand Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Aspleiter Forschung AG, Chen Karime, vertreten durch Dorda Rechtsanwälte GmbH in Wien, wegen 16.354,47 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 31. Jänner 2020, GZ 1 R 120/19b-21, womit das Urteil des Handelsgerichts Wien vom 22. Juli 2019, GZ 16 Cg 50/18d-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei Aspleiter Forschung AG` — partial — gold is substring of pred: `Aspleiter Forschung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Bernhard Siegloch`(person)
- `Aspleiter Forschung AG`(organisation)
- `Chen Karime`(person)

**Example 41** (doc_id: `deanon_TRAIN/7Ob97_18t`) (sent_id: `deanon_TRAIN/7Ob97_18t_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Dr. Leila Werntz, vertreten durch Dr. Peter Gregorich, Rechtsanwalt in Wien, gegen die beklagte Partei Valber Solar AG, Alexander Lukoszek, vertreten durch Dr. Matthias Bacher, Rechtsanwalt in Wien, wegen 1.057.200 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. März 2018, GZ 1 R 160/17g-116, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Valber Solar AG` — partial — gold is substring of pred: `Valber Solar AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Leila Werntz`(person)
- `Valber Solar AG`(organisation)
- `Alexander Lukoszek`(person)

**Example 42** (doc_id: `deanon_TRAIN/8Ob11_11t`) (sent_id: `deanon_TRAIN/8Ob11_11t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner sowie die Hofräte Mag. Ziegelbauer und Dr. Brenn als weitere Richter in der Rechtssache der klagenden Partei, Guggeis Automotive Bank InnBildung Betriebe AG, Olga Wohlbrück-Gasse 5, 3482 Gösing am Wagram, Österreich, vertreten durch Dr. Mag. Günther Riess, Mag. Christine Schneider, Rechtsanwälte in Innsbruck, gegen die beklagte Partei Doris Froemmel, vertreten durch Czernich Hofstädter Guggenberger & Partner, Rechtsanwälte in Innsbruck, wegen 2.278.895,88 EUR sA, über die Rekurse beider Parteien gegen den Beschluss des Oberlandesgerichts Innsbruck als Berufungsgericht vom 11. Oktober 2010, GZ 4 R 168/10b-76, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Feldkirch vom 20. Mai 2010, GZ 6 Cg 71/08s-71, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch 1.

**False Positives:**

- `Guggeis Automotive Bank InnBildung Betriebe AG` — partial — gold is substring of pred: `Guggeis Automotive`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Guggeis Automotive`(organisation)
- `InnBildung Betriebe AG`(organisation)
- `Olga Wohlbrück-Gasse 5, 3482 Gösing am Wagram, Österreich`(address)
- `Doris Froemmel`(person)

**Example 43** (doc_id: `deanon_TRAIN/8Ob121_22k`) (sent_id: `deanon_TRAIN/8Ob121_22k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn und die Hofräte Dr. Stefula und Dr. Thunhart in der Rechtssache der klagenden Partei Roettgermann + Soldmann Heizung AG, Theophil Bings, vertreten durch die Schönherr Rechtsanwälte GmbH in Wien, gegen die beklagte Partei ÖkR Christoph Adamske Privatstiftung,*, vertreten durch Dr. Felix Michael Klement, Rechtsanwalt in Wien, wegen 1.500.000 USD sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien vom 28. April 2022, GZ 2 R 133/21z-42, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Soldmann Heizung AG` — partial — pred is substring of gold: `Roettgermann + Soldmann Heizung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Roettgermann + Soldmann Heizung AG`(organisation)
- `Theophil Bings`(person)
- `ÖkR Christoph Adamske`(person)

**Example 44** (doc_id: `deanon_TRAIN/8Ob39_24d`) (sent_id: `deanon_TRAIN/8Ob39_24d_7`)


Er brachte vor, über seine depotführende Bank in Graz mehrfach Aktien der Daten Monfen AG mit Sitz in Deutschland gekauft zu haben (und zwar, wie aus den von ihm vorgelegten Beilagen ersichtlich, „loco Düsseldorf“).

**False Positives:**

- `Bank in Graz mehrfach Aktien der Daten Monfen AG` — partial — gold is substring of pred: `Daten Monfen AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Daten Monfen AG`(organisation)

**Example 45** (doc_id: `deanon_TRAIN/8Ob39_24d`) (sent_id: `deanon_TRAIN/8Ob39_24d_9`)


Hätte sie pflichtgemäß gehandelt und den von ihr geprüften Jahresabschlüssen den Bestätigungsvermerk versagt, hätte er die Aktien nicht gekauft und damit – wegen der kurz nach seinen Käufen von der Nieder-Analyse Solutions AG beantragten Insolvenzeröffnung – keinen Schaden erlitten.

**False Positives:**

- `Analyse Solutions AG` — partial — pred is substring of gold: `Nieder-Analyse Solutions AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder-Analyse Solutions AG`(organisation)

**Example 46** (doc_id: `deanon_TRAIN/8Ob39_24d`) (sent_id: `deanon_TRAIN/8Ob39_24d_13`)


Die West Heimwaldstein Solutions AG habe insofern auch Offenlegungspflichten in Österreich getroffen.

**False Positives:**

- `Die West Heimwaldstein Solutions AG` — partial — gold is substring of pred: `West Heimwaldstein Solutions AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `West Heimwaldstein Solutions AG`(organisation)

**Example 47** (doc_id: `deanon_TRAIN/8ObA18_17f`) (sent_id: `deanon_TRAIN/8ObA18_17f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Brenn als weitere Richter sowie die fachkundigen Laienrichter Mag. Dr. Bernhard Gruber und Harald Kohlruss in der Arbeitsrechtssache der klagenden Partei Cassandra Hennel, vertreten durch Freimüller/Obereder/Pilz Rechtsanwält_innen GmbH in Wien, gegen die beklagte Partei SeeTextil AG, Othmar Dempewolf, vertreten durch DLA Piper Weiss-Tessbach Rechtsanwälte GmbH in Wien, wegen Feststellung (Streitwert 282,56 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. November 2016, GZ 7 Ra 90/16f-19, mit dem das Urteil des Arbeits- und Sozialgerichts Wien vom 20. Juli 2016, GZ 33 Cga 50/16p-15, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Partei SeeTextil AG` — partial — gold is substring of pred: `SeeTextil AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Cassandra Hennel`(person)
- `SeeTextil AG`(organisation)
- `Othmar Dempewolf`(person)

**Example 48** (doc_id: `deanon_TRAIN/8ObA59_23v`) (sent_id: `deanon_TRAIN/8ObA59_23v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Stefula als weitere Richter und die fachkundigen Laienrichter OAR Prof. Franz Neuhauser (aus dem Kreis der Arbeitgeber) und Gerald Fida (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Benjamin Saeltzer, vertreten durch Dr. Charlotte Böhm, Rechtsanwältin in Wien, gegen die beklagte Partei WaldGlanzdorflogIT Institut AG, Techn R Roswitha Voitl, vertreten durch die Lansky, Ganzger, Goeth, Frankl & Partner Rechtsanwälte GmbH in Wien, wegen Kündigungsanfechtung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 21. Juni 2023, GZ 10 Ra 47/23i-120, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei WaldGlanzdorflogIT Institut AG` — partial — gold is substring of pred: `WaldGlanzdorflogIT Institut AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Benjamin Saeltzer`(person)
- `WaldGlanzdorflogIT Institut AG`(organisation)
- `Techn R Roswitha Voitl`(person)

**Example 49** (doc_id: `deanon_TRAIN/8ObA69_19h`) (sent_id: `deanon_TRAIN/8ObA69_19h_4`)


Dr. Susanne Binder-Novak, Rechtsanwältin in St. Pölten, gegen die beklagte Partei Heizung Trimonwald AG, Ashley Hoeksma, vertreten durch Dr. Helmut Engelbrecht, Rechtsanwalt in Wien, wegen 14.426 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 26. September 2019, GZ 7 Ra 79/19t-15, in nichtöffentlicher Sitzung Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 2 ASGG, § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Heizung Trimonwald AG` — partial — gold is substring of pred: `Heizung Trimonwald AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Heizung Trimonwald AG`(organisation)
- `Ashley Hoeksma`(person)

**Example 50** (doc_id: `deanon_TRAIN/9Ob10_21t`) (sent_id: `deanon_TRAIN/9Ob10_21t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätinnen und Hofräte Dr. Fichtenau, Hon.-Prof. Dr. Dehn, Dr. Hargassner, und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Schnake Robotik gmbh, Jeanne Großkopf, vertreten durch Forcher-Mayr & Kantner Rechtsanwälte Partnerschaft in Innsbruck, gegen die beklagte Partei Volkmar Kapelner GmbH, Reinberg-Litschau 11, 9343 Aich, Österreich, vertreten durch Advokatur Dr. Herbert Schöpf, LL.M., Rechtsanwalt-GmbH in Innsbruck, sowie die Nebenintervenientin auf Seiten der beklagten Partei EKFS Landwirtschaft AG & Co KG, Burgstallerstraße 10, 4892 Röth, Österreich, vertreten durch Hämmerle & Hübner Rechtsanwälte OG in Innsbruck, wegen 115.062,53 EUR sA, über die außerordentliche Revision der beklagten Partei (Revisionsinteresse 104.999,62 EUR sA) gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 11. Jänner 2021, GZ 3 R 76/20f-144, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Seiten der beklagten Partei EKFS Landwirtschaft AG` — partial — gold is substring of pred: `EKFS Landwirtschaft AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schnake Robotik gmbh`(organisation)
- `Jeanne Großkopf`(person)
- `Volkmar Kapelner`(person)
- `Reinberg-Litschau 11, 9343 Aich, Österreich`(address)
- `EKFS Landwirtschaft AG`(organisation)
- `Burgstallerstraße 10, 4892 Röth, Österreich`(address)

**Example 51** (doc_id: `deanon_TRAIN/9Ob45_10y`) (sent_id: `deanon_TRAIN/9Ob45_10y_4`)


Carla Blaessing, vertreten durch die Poduschka Anwaltsgesellschaft mbH in Perg, gegen die beklagte Partei TraunMaschinenbau AG, Vivian Lammerschmidt, wegen 11.040,07 EUR sA, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Handelsgerichts Wien als Rekursgericht vom 31. Mai 2010, GZ 1 R 130/10d-5, mit dem der Beschluss des Bezirksgerichts für Handelssachen Wien vom 18. März 2010, GZ 14 C 385/10k-2, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Partei TraunMaschinenbau AG` — partial — gold is substring of pred: `TraunMaschinenbau AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `TraunMaschinenbau AG`(organisation)
- `Vivian Lammerschmidt`(person)

**Example 52** (doc_id: `deanon_TRAIN/9Ob6_24h`) (sent_id: `deanon_TRAIN/9Ob6_24h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende, die Hofrätinnen und Hofräte des Obersten Gerichtshofs Mag. Ziegelbauer, Dr. Hargassner, Mag. Korn und Dr. Stiefsohn in der Rechtssache der klagenden Partei Isaak Feyereis, vertreten durch Dr. Alexander Amann LL.M., Rechtsanwalt in Gamprin-Bendern, Fürstentum Liechtenstein, gegen die beklagte Partei Mur Monsteinsee Technologien AG, Floriane Mavrou, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 2.375 EUR und Feststellung (Streitwert: 4.000 EUR), über die Revision der beklagten Partei gegen das Zwischenurteil des Landesgerichts Wels als Berufungsgericht vom 25. Oktober 2023, GZ 22 R 198/23h-31, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Vöcklabruck vom 15. Juni 2023, GZ 13 C 630/22f-26, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I.Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei Mur Monsteinsee Technologien AG` — partial — gold is substring of pred: `Mur Monsteinsee Technologien AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Isaak Feyereis`(person)
- `Mur Monsteinsee Technologien AG`(organisation)
- `Floriane Mavrou`(person)

**Example 53** (doc_id: `deanon_TRAIN/9ObA134_09k`) (sent_id: `deanon_TRAIN/9ObA134_09k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsrekursgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten des Obersten Gerichtshofs Dr. Rohrer als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Dr. Hradil und Dr. Hopf als weitere Richter in der Arbeitsrechtssache der klagenden Partei Dipl.-Ing. Ursula Weeverink, vertreten durch Dr. Andreas Lintl, Rechtsanwalt in Wien, gegen die beklagte Partei Thenert Analyse AG, Stanley Helmli, vertreten durch die Winkler Reich-Rohrwig Illedits Rechtsanwälte-Partnerschaft in Wien, wegen Kündigungsanfechtung, über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht in Arbeits- und Sozialrechtssachen vom 14. Oktober 2009, GZ 10 Ra 108/09i-17, womit der Beschluss des Landesgerichts Krems an der Donau als Arbeits- und Sozialgericht vom 13. August 2009, GZ 7 Cga 42/09b-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs der klagenden Partei wird gemäß § 526 Abs 2 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Thenert Analyse AG` — partial — gold is substring of pred: `Thenert Analyse AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. Ursula Weeverink`(person)
- `Thenert Analyse AG`(organisation)
- `Stanley Helmli`(person)

</details>

---

## `German Gesellschaft mbH Entity`

**F1:** 0.011 | **Precision:** 0.667 | **Recall:** 0.006  

**Format:** `regex`  
**Description:**
Matches entities ending in 'Gesellschaft mbH' or 'gesmbH' with flexible spacing.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!Richter\s)(?<!Richterin\s)(?<!Senatspr\u00e4sident\s)(?<!Senatspr\u00e4sidentin\s)(?<!Hofrat\s)(?<!Hofr\u00e4tin\s)(?<!Hofr\u00e4t\s)(?<!Mag\.\s)(?<!Dr\.\s)(?<!Prof\.\s)(?<!Hon\.\s)(?<!Kanzlei\s)(?<!Anwalt\s)(?<!Gesellschafter\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!klagenden\s)(?<!beklagten\s)(?<!Nebenintervenient\s)(?<!Nebenintervenientin\s)(?<!Nebenintervenienten\s)(?<!Nebenintervenientinnen\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)([A-Z][A-Za-z0-9\s&+\-]*\s+Gesellschaft\s+mbH|[A-Z][A-Za-z0-9\s&+\-]*\s+gesmbH)(?=[,\s]|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.667 | 0.006 | 0.011 | 3 | 2 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 1 | 277 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/17Ob19_23b`) (sent_id: `deanon_TRAIN/17Ob19_23b_7`)


Die Kläger brachten gegen den Beklagten als ehemaligen Insolvenzverwalter der A. Rater Finanzen Gesellschaft mbH eine von ihnen selbst verfasste Schadenersatzklage verbunden mit einem Antrag auf Bewilligung der Verfahrenshilfe ein.

| Predicted | Gold |
|---|---|
| `Rater Finanzen Gesellschaft mbH` | `Rater Finanzen Gesellschaft mbH` |

**Example 1** (doc_id: `deanon_TRAIN/7Ob31_19p`) (sent_id: `deanon_TRAIN/7Ob31_19p_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Alpen Traostal GmbH, Florens Mühle, vertreten durch Mag. Stefan Korab, Rechtsanwalt in Wien, gegen die beklagte Partei Ing. RheinImmobilien Gesellschaft mbH, Melcherweg 193, 8242 Kronegg, Österreich, vertreten durch KWR Karasek Wietrzyk Rechtsanwälte GmbH in Wien, wegen 151.623,74 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 20. Dezember 2018, GZ 129 R 98/18g-76, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `RheinImmobilien Gesellschaft mbH` | `RheinImmobilien Gesellschaft mbH` |

**Missed by this rule (FN):**

- `Alpen Traostal GmbH` (organisation)
- `Florens Mühle` (person)
- `Melcherweg 193, 8242 Kronegg, Österreich` (address)

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

## `German E-Commerce Entity`

**F1:** 0.006 | **Precision:** 0.500 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches entities containing 'E‑Commerce' (en-dash) followed by GmbH or Limited.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)([A-Z][A-Za-z0-9\s&+\-]*E\u2011Commerce\s+(?:GmbH|Limited))(?=[,\s]|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.003 | 0.006 | 2 | 1 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 1 | 212 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/3Ob204_19z`) (sent_id: `deanon_TRAIN/3Ob204_19z_37`)


Das ist hier schon deshalb nicht der Fall, weil der Verpflichtete selbst davon ausgeht, noch nicht alle Unterlagen vorgelegt zu haben, weil die derzeitige Eigentümerin der Unternehmensgruppe PJS E‑Commerce GmbH bis dato jede Offenbarung von Buchhaltungsunterlagen abgelehnt habe.

| Predicted | Gold |
|---|---|
| `PJS E‑Commerce GmbH` | `PJS E‑Commerce GmbH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/9Ob82_21f`) (sent_id: `deanon_TRAIN/9Ob82_21f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Mag. Ziegelbauer, Hon.-Prof. Dr. Dehn, Dr. Hargassner und Mag. Korn in der Rechtssache der klagenden Partei Gwendolin Masik, vertreten durch Wallner Jorthan Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Froschmeier+Mildner E‑Commerce GmbH, Gottfried Tomaszeski, vertreten durch Hajek & Boss & Wagner Rechtsanwälte OG in Eisenstadt, wegen Unterlassung, in eventu Feststellung (Interesse: 16.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien vom 23. September 2021, GZ 4 R 32/21m-26, mit dem der Berufung der klagenden Partei gegen das Urteil des Landesgerichts Eisenstadt vom 12. Jänner 2021, GZ 2 Cg 75/20v-16, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision der klagenden Partei wird zurückgewiesen.

**False Positives:**

- `Partei Froschmeier+Mildner E‑Commerce GmbH` — partial — gold is substring of pred: `Froschmeier+Mildner E‑Commerce GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gwendolin Masik`(person)
- `Froschmeier+Mildner E‑Commerce GmbH`(organisation)
- `Gottfried Tomaszeski`(person)

</details>

---

## `German Ltd Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches entities ending in 'Ltd.'

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)([A-Z][A-Za-z0-9\s&+\-]*[A-Z][A-Za-z0-9\s&+\-]*\s+Ltd\.|[A-Z][A-Za-z0-9\s&+\-]*\s+Ltd\.)(?=[,\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 176 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/4Ob223_21d`) (sent_id: `deanon_TRAIN/4Ob223_21d_4`)


Matzka sowie Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei Ilhan Mertzlufft, vertreten durch Dr. Sven Rudolf Thorstensen, LL.M., Rechtsanwalt in Wien, gegen die beklagte Partei Gartval Ltd., Erich Jaruszowic, vertreten durch Dr. David Christian Bauer, Rechtsanwalt in Wien, wegen 51.422,54 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 8. November 2021, GZ 5 R 69/21k-25, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 2 ZPO zurückgewiesen.

**False Positives:**

- `Partei Gartval Ltd.` — partial — gold is substring of pred: `Gartval Ltd.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ilhan Mertzlufft`(person)
- `Gartval Ltd.`(organisation)
- `Erich Jaruszowic`(person)

</details>

---

## `German u. Kirchmann Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific pattern 'u.' (und) in company names like Guggemos u. Kirchmann Möbel GmbH.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)([A-Z][A-Za-z0-9\s&+\-]*\s+u\.\s+[A-Z][A-Za-z0-9\s&+\-]*\s+M\u00f6bel\s+GmbH)(?=[,\s]|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `German Bezirksgericht Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific court entities 'Bezirksgericht [City]'.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(Bezirksgericht\s+(?:St\.\s*P\u00f6lten|Meidling))(?=[,\s]|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 134 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/6Ob199_10y`) (sent_id: `deanon_TRAIN/6Ob199_10y_5`)


Im vorliegenden Verfahren geht es um die pflegschaftsbehördliche Genehmigung eines Vergleichs vor dem Bezirksgericht Meidling.

**False Positives:**

- `Bezirksgericht Meidling` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `German Tal-Gastronomie Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific entity 'TalFenbruckbruckGastronomie GmbH'.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(TalFenbruckbruckGastronomie\s+GmbH)(?=[,\s]|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `German GmbH & Co KG Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches entities ending in 'GmbH & Co KG' with strict boundary.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!Richter\s)(?<!Richterin\s)(?<!Senatspr\u00e4sident\s)(?<!Senatspr\u00e4sidentin\s)(?<!Hofrat\s)(?<!Hofr\u00e4tin\s)(?<!Hofr\u00e4t\s)(?<!Mag\.\s)(?<!Dr\.\s)(?<!Prof\.\s)(?<!Hon\.\s)(?<!Kanzlei\s)(?<!Anwalt\s)(?<!Gesellschafter\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!klagenden\s)(?<!beklagten\s)(?<!Nebenintervenient\s)(?<!Nebenintervenientin\s)(?<!Nebenintervenienten\s)(?<!Nebenintervenientinnen\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)([A-Z][A-Za-z0-9\s&+\-]*[A-Z][A-Za-z0-9\s&+\-]*\s+GmbH\s+&\s+Co\s+KG)(?=[,\s]|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 8 | 0 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 8 | 315 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_4`)


Energie Conwald GmbH & Co KG und 2.

**False Positives:**

- `Energie Conwald GmbH & Co KG` — partial — gold is substring of pred: `Energie Conwald GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Energie Conwald GmbH`(organisation)

**Example 1** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_5`)


Text Begründung: Der Kläger erwarb im Jahr 2004 als Verbraucher über Vermittlung eines Wertpapierdienstleistungsunternehmens Kommanditanteile an der Contra GmbH & Co KG im Nominale von 20.000 EUR zuzüglich 1.000 EUR Agio.

**False Positives:**

- `Vermittlung eines Wertpapierdienstleistungsunternehmens Kommanditanteile an der Contra GmbH & Co KG` — partial — gold is substring of pred: `Contra GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Contra GmbH`(organisation)

**Example 2** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt, aus denen Erträge erzielt werden sollen.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/1Ob197_18d`) (sent_id: `deanon_TRAIN/1Ob197_18d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Volze KI GmbH & Co KG, Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich, vertreten durch Dr. Klaus-Dieter Strobach und andere Rechtsanwälte, Grieskirchen, gegen die beklagte Partei Land Oberösterreich, Linz, Landhausplatz 1, vertreten durch Dr. Thomas J. A. Langer, LL.M., Rechtsanwalt in Linz, wegen 475.550,18 EUR sA, über die (außerordentliche) Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2018, GZ 4 R 56/18k-17, mit dem das Urteil des Landesgerichts Wels vom 1. März 2018, GZ 3 Cg 3/16z-13, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Volze KI GmbH & Co KG` — partial — gold is substring of pred: `Volze KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Volze KI GmbH`(organisation)
- `Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich`(address)

**Example 5** (doc_id: `deanon_TRAIN/3Ob209_21p`) (sent_id: `deanon_TRAIN/3Ob209_21p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Nexostlem GmbH & Co KG, Rehlackenweg 5G, 8451 Pernitsch, Österreich, vertreten durch DDr. Heinz Dietmar Schimanko, Rechtsanwalt in Wien, gegen die beklagte Partei RheinLandwirtschaft Vertrieb GmbH, Klaus Dissler, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH & Co KG in Wien, wegen 7.906,82 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 7. Juni 2021, GZ 38 R 66/21v-16, mit dem das Urteil des Bezirksgerichts Favoriten vom 19. Jänner 2021, GZ 3 C 503/20f-12, abgeändert wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Nexostlem GmbH & Co KG` — partial — gold is substring of pred: `Nexostlem GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nexostlem GmbH`(organisation)
- `Rehlackenweg 5G, 8451 Pernitsch, Österreich`(address)
- `RheinLandwirtschaft Vertrieb GmbH`(organisation)
- `Klaus Dissler`(person)

**Example 6** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_5`)


Klingenbeil Versand GmbH & Co KG, 2.

**False Positives:**

- `Klingenbeil Versand GmbH & Co KG` — partial — gold is substring of pred: `Klingenbeil Versand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Klingenbeil Versand GmbH`(organisation)

**Example 7** (doc_id: `deanon_TRAIN/8Ob60_12z`) (sent_id: `deanon_TRAIN/8Ob60_12z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner sowie die Hofräte Mag. Ziegelbauer und Dr. Brenn als weitere Richter in der Rechtssache der klagenden Partei Arabella Witkopf, vertreten durch Mag. Renate Aigner, Rechtsanwältin in Kallham, gegen die beklagte Partei Abramczyk & Krollpfeifer Wind GmbH & Co KG, Pühra 22, 8010 Edelsbach bei Graz, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen (Revisionsinteresse) 10.000 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 15. März 2012, GZ 3 R 42/12k-38, womit das Urteil des Landesgerichts Linz vom 28. Dezember 2011, GZ 1 Cg 167/10i-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Partei Abramczyk & Krollpfeifer Wind GmbH & Co KG` — partial — gold is substring of pred: `Abramczyk & Krollpfeifer Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Arabella Witkopf`(person)
- `Abramczyk & Krollpfeifer Wind GmbH`(organisation)
- `Pühra 22, 8010 Edelsbach bei Graz, Österreich`(address)

</details>

---

## `German Bank AG Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific bank names followed by 'Bank AG' to capture only the company name part.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)([A-Z][A-Za-z0-9\s&+\-]*[A-Z][A-Za-z0-9\s&+\-]*\s+Bank\s+AG)(?=[,\s]|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `German Limited Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches entities ending in 'Limited' with strict boundary, excluding preceding legal terms.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!Richter\s)(?<!Richterin\s)(?<!Senatspr\u00e4sident\s)(?<!Senatspr\u00e4sidentin\s)(?<!Hofrat\s)(?<!Hofr\u00e4tin\s)(?<!Hofr\u00e4t\s)(?<!Mag\.\s)(?<!Dr\.\s)(?<!Prof\.\s)(?<!Hon\.\s)(?<!Kanzlei\s)(?<!Anwalt\s)(?<!Gesellschafter\s)(?<!klagenden\s)(?<!beklagten\s)(?<!Nebenintervenient\s)(?<!Nebenintervenientin\s)(?<!Nebenintervenienten\s)(?<!Nebenintervenientinnen\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)([A-Z][A-Za-z0-9\s&+\-]*[A-Z][A-Za-z0-9\s&+\-]*\s+Limited)(?=[,\s]|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 5 | 0 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 5 | 318 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob22_22s`) (sent_id: `deanon_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludger Radek, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Solar Fenwerk Limited, Amanda Ziergöbel Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei Solar Fenwerk Limited` — partial — gold is substring of pred: `Solar Fenwerk Limited`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ludger Radek`(person)
- `Solar Fenwerk Limited`(organisation)
- `Amanda Ziergöbel`(person)

**Example 1** (doc_id: `deanon_TRAIN/1Ob171_22m`) (sent_id: `deanon_TRAIN/1Ob171_22m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Musger als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Leonie Dommke, vertreten durch Mag. Klaus Mayer, Rechtsanwalt in Premstätten, gegen die beklagte Partei Grashuber+Kovatchev Immobilien Limited, Elisabeth Hallmanns, vertreten durch Dr. Fabian Maschke, Rechtsanwalt in Wien, wegen 36.070 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 3. August 2022, GZ 4 R 98/22x-24, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Grashuber+Kovatchev Immobilien Limited` — partial — gold is substring of pred: `Grashuber+Kovatchev Immobilien Limited`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Leonie Dommke`(person)
- `Grashuber+Kovatchev Immobilien Limited`(organisation)
- `Elisabeth Hallmanns`(person)

**Example 2** (doc_id: `deanon_TRAIN/1Ob192_11h`) (sent_id: `deanon_TRAIN/1Ob192_11h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Hamberg Marine Limited, London, Kapellergasse 9, 4925 Lungdorf, Österreich, vertreten durch Thum Weinreich Schwarz Fuchsbauer Rechtsanwälte OG in St. Pölten, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 1,8 Mio EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Juni 2011, GZ 14 R 214/10h-39, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 3. September 2010, GZ 33 Cg 3/09t-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Hamberg Marine Limited` — partial — gold is substring of pred: `Hamberg Marine Limited`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hamberg Marine Limited`(organisation)
- `Kapellergasse 9, 4925 Lungdorf, Österreich`(address)

**Example 3** (doc_id: `deanon_TRAIN/3Nc39_24a`) (sent_id: `deanon_TRAIN/3Nc39_24a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn und die Hofrätin Dr. Kodek als weitere Richter in der Ordinationssache der betreibenden Partei Wendy Janacek, vertreten durch Dr. Florian Johann Ernst Knaipp, Rechtsanwalt in Wien, gegen die verpflichtete Partei Siege KI Limited, Edgar Dölle, wegen 47.126,91 EUR sA, über den Antrag auf Ordination nach § 28 JN, den Beschluss gefasst:  Spruch Für die Bewilligung und den Vollzug der von der betreibenden Partei beabsichtigten Rechteexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Partei Siege KI Limited` — partial — gold is substring of pred: `Siege KI Limited`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wendy Janacek`(person)
- `Siege KI Limited`(organisation)
- `Edgar Dölle`(person)

**Example 4** (doc_id: `deanon_TRAIN/8Ob31_24b`) (sent_id: `deanon_TRAIN/8Ob31_24b_4`)


Matzka, Dr. Stefula, Dr. Thunhart und Mag. Dr. Sengstschmid als weitere Richter in der Rechtssache der klagenden Partei Arnold Uhlemeier, LLM, vertreten durch Mag. Alexander Tupy, Rechtsanwalt in Wien, gegen die beklagte Partei Lemwilbruck-Marine Limited, Nadja Buhrfeindt, Malta, vertreten durch Mag. Marcus Marakovics, Rechtsanwalt in Wien, wegen 18.842,85 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Dezember 2023, GZ 11 R 284/23z-19, mit dem der Berufung der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 16. Oktober 2023, GZ 17 Cg 26/23b-11, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision der beklagten Partei wird zurückgewiesen.

**False Positives:**

- `Partei Lemwilbruck-Marine Limited` — partial — gold is substring of pred: `Lemwilbruck-Marine Limited`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Arnold Uhlemeier, LLM`(person)
- `Lemwilbruck-Marine Limited`(organisation)
- `Nadja Buhrfeindt`(person)

</details>

---

## `German Aktiengesellschaft Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches entities ending in 'Aktiengesellschaft' with strict boundary.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!Richter\s)(?<!Richterin\s)(?<!Senatspr\u00e4sident\s)(?<!Senatspr\u00e4sidentin\s)(?<!Hofrat\s)(?<!Hofr\u00e4tin\s)(?<!Hofr\u00e4t\s)(?<!Mag\.\s)(?<!Dr\.\s)(?<!Prof\.\s)(?<!Hon\.\s)(?<!Kanzlei\s)(?<!Anwalt\s)(?<!Gesellschafter\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)([A-Z][A-Za-z0-9\s&+\-]*[A-Z][A-Za-z0-9\s&+\-]*\s+Aktiengesellschaft)(?=[,\s]|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 7 | 0 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 7 | 345 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_5`)


Sie habe im Jahr 2012 mit einer Aktiengesellschaft einen Ansparplan abgeschlossen.

**False Positives:**

- `Sie habe im Jahr 2012 mit einer Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/1Ob140_14s`) (sent_id: `deanon_TRAIN/1Ob140_14s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer und Mag. Dr. Wurdinger sowie die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft, Meidlinger Hauptstraße 19, 5233 Erlach, Österreich, vertreten durch die Walch & Zehetbauer Rechtsanwälte OG, Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 344.011,19 EUR und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Juni 2014, GZ 4 R 202/13g-54, mit dem das Teilzwischenurteil des Landesgerichts Feldkirch vom 2. August 2013, GZ 8 Cg 143/11y-46, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

**False Positives:**

- `Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft` — partial — gold is substring of pred: `Tracondon Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tracondon Aktiengesellschaft`(organisation)
- `Meidlinger Hauptstraße 19, 5233 Erlach, Österreich`(address)

**Example 2** (doc_id: `deanon_TRAIN/2Ob256_12d`) (sent_id: `deanon_TRAIN/2Ob256_12d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Stallbauer Telekom Aktiengesellschaft, Poysdorfer Straße 5, 9341 Dobersberg, Österreich, vertreten durch Dr. Manfred Steininger, Rechtsanwalt in Wien, gegen die beklagte Partei DDr. Viktor Junkmanns, Bakk. iur., vertreten durch die ANWALTGMBH Rinner Teuchtmann in Linz, wegen 50.932,89 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2012, GZ 4 R 158/12a-20, womit das Urteil des Landesgerichts Linz vom 14. Juni 2012, GZ 5 Cg 119/11m-14, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Richter in der Rechtssache der klagenden Partei Stallbauer Telekom Aktiengesellschaft` — partial — gold is substring of pred: `Stallbauer Telekom Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stallbauer Telekom Aktiengesellschaft`(organisation)
- `Poysdorfer Straße 5, 9341 Dobersberg, Österreich`(address)
- `DDr. Viktor Junkmanns, Bakk. iur.`(person)

**Example 3** (doc_id: `deanon_TRAIN/3Ob17_20a`) (sent_id: `deanon_TRAIN/3Ob17_20a_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie die Hofräte Priv.-Doz. Dr. Rassi und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Exekutionssache betreibenden Partei Heizung Werkuni Aktiengesellschaft, P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich, vertreten durch Dr. Roland Grilc ua, Rechtsanwälte in Klagenfurt am Wörthersee, gegen die verpflichtete Partei Dorothea Eiken Bank, Peter Eitenmüller, vertreten durch Diwok Hermann Petsche Rechtsanwälte LLP Co KG in Wien, wegen 12.602.980,92 EUR sA, über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. November 2019, GZ 46 R 293/19g-18, mit dem der Beschluss des Bezirksgerichts Favoriten vom 17. April 2019, GZ 17 E 1298/19z-2, bestätigt wurde, den Beschluss gefasst:  Spruch I. Der Revisionsrekurs wird, soweit er sich gegen die Bestätigung der Exekutionsbewilligung richtet, als jedenfalls unzulässig zurückgewiesen.

**False Positives:**

- `Richter in der Exekutionssache betreibenden Partei Heizung Werkuni Aktiengesellschaft` — partial — gold is substring of pred: `Heizung Werkuni Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Heizung Werkuni Aktiengesellschaft`(organisation)
- `P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich`(address)
- `Dorothea Eiken`(person)
- `Peter Eitenmüller`(person)

**Example 4** (doc_id: `deanon_TRAIN/4Ob13_17s`) (sent_id: `deanon_TRAIN/4Ob13_17s_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Daten Steinlem Aktiengesellschaft, Inderstadt 17, 2564 Furth, Österreich, vertreten durch die Huber Swoboda Oswald Aixberger Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Muran Fass, vertreten durch Dr. Fabian Maschke, Rechtsanwalt in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert 35.000 EUR), über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Dezember 2016, GZ 2 R 74/16i-24, womit das Urteil des Landesgerichts Ried im Innkreis vom 25. Februar 2016, GZ 5 Cg 191/14m-14, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei Daten Steinlem Aktiengesellschaft` — partial — gold is substring of pred: `Daten Steinlem Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Daten Steinlem Aktiengesellschaft`(organisation)
- `Inderstadt 17, 2564 Furth, Österreich`(address)
- `Muran Fass`(person)

**Example 5** (doc_id: `deanon_TRAIN/7Ob141_16k`) (sent_id: `deanon_TRAIN/7Ob141_16k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofräte Dr. Höllwerth, Mag. Dr. Wurdinger, Mag. Malesich und Dr. Singer als weitere Richter in der Rechtssache der klagenden Partei Seedorf Vertrieb GmbH, Felix Bernloehr, vertreten durch Dr. Helmut Fetz und andere, Rechtsanwälte in Leoben, gegen die beklagte Partei Mlynarik Handel Aktiengesellschaft, Veropastraße 16, 2413 Edelstal, Österreich, vertreten durch Dr. Heimo Jilek und Dr. Martin Sommer, Rechtsanwälte in Leoben, wegen 61.848,15 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 25. Mai 2016, GZ 5 R 9/16g-32, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Mlynarik Handel Aktiengesellschaft` — partial — gold is substring of pred: `Mlynarik Handel Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Seedorf Vertrieb GmbH`(organisation)
- `Felix Bernloehr`(person)
- `Mlynarik Handel Aktiengesellschaft`(organisation)
- `Veropastraße 16, 2413 Edelstal, Österreich`(address)

**Example 6** (doc_id: `deanon_TRAIN/8ObA41_17p`) (sent_id: `deanon_TRAIN/8ObA41_17p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn als weitere Richter sowie die fachkundigen Laienrichter Dr. Ingomar Stupar und Mag. Matthias Schachner in der Arbeitsrechtssache der klagenden Partei Edgar Springob, vertreten durch Dr. Anton Tschann, Rechtsanwalt in Bludenz, gegen die beklagte Partei Zach + Merkeli Daten Aktiengesellschaft, Saggau 133, 3240 Poppendorf, Österreich, wegen Vertragsanfechtung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 13. Juni 2017, GZ 15 Ra 26/17m-39, in nichtöffentlicher Sitzungden Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO iVm § 2 Abs 1 ASGG).

**False Positives:**

- `Partei Zach + Merkeli Daten Aktiengesellschaft` — partial — gold is substring of pred: `Zach + Merkeli Daten Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Edgar Springob`(person)
- `Zach + Merkeli Daten Aktiengesellschaft`(organisation)
- `Saggau 133, 3240 Poppendorf, Österreich`(address)

</details>

---

## `German Specific NoSuffix Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific entities without standard suffixes or with unique structures found in training data.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!Richter\s)(?<!Richterin\s)(?<!Senatspr\u00e4sident\s)(?<!Senatspr\u00e4sidentin\s)(?<!Hofrat\s)(?<!Hofr\u00e4tin\s)(?<!Hofr\u00e4t\s)(?<!Mag\.\s)(?<!Dr\.\s)(?<!Prof\.\s)(?<!Hon\.\s)(?<!Kanzlei\s)(?<!Anwalt\s)(?<!Gesellschafter\s)(?<!klagenden\s)(?<!beklagten\s)(?<!Nebenintervenient\s)(?<!Nebenintervenientin\s)(?<!Nebenintervenienten\s)(?<!Nebenintervenientinnen\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(NordSicherheit|Druck\s+Glanzfen|Kupferberg\s+\+\s+Kleinen\s+Finanzen|NUSA\s+Analyse\s+Vertrieb|Spendler\s+Maschinenbau|Dontraost\s+Marine|Mur\s+Brucktridon|SeeDruck\s+Gruppe|NiederPflege|EnnsVersicherung|Sevki\s+Event|HochDigital|Pietruszak\s+Recycling|BergMedien|Talal-Energie|Tempel\s+Logistik|Unitradon-Telekom|Vertra-Elektro|Schmerschneider\s+Transport)(?=[,\s]|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `German Trilog Institut Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific entity 'Trilog Institut gesellschaft mbH'.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!Richter\s)(?<!Richterin\s)(?<!Senatspr\u00e4sident\s)(?<!Senatspr\u00e4sidentin\s)(?<!Hofrat\s)(?<!Hofr\u00e4tin\s)(?<!Hofr\u00e4t\s)(?<!Mag\.\s)(?<!Dr\.\s)(?<!Prof\.\s)(?<!Hon\.\s)(?<!Kanzlei\s)(?<!Anwalt\s)(?<!Gesellschafter\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!klagenden\s)(?<!beklagten\s)(?<!Nebenintervenient\s)(?<!Nebenintervenientin\s)(?<!Nebenintervenienten\s)(?<!Nebenintervenientinnen\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(Trilog\s+Institut\s+gesellschaft\s+mbH)(?=[,\s]|\.|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `German Specific GmbH Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific GmbH entities that were missed.

**Content:**
```
(?<![\w])(?<!Partei\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!Richter\s)(?<!Richterin\s)(?<!Senatspr\u00e4sident\s)(?<!Senatspr\u00e4sidentin\s)(?<!Hofrat\s)(?<!Hofr\u00e4tin\s)(?<!Hofr\u00e4t\s)(?<!Mag\.\s)(?<!Dr\.\s)(?<!Prof\.\s)(?<!Hon\.\s)(?<!Kanzlei\s)(?<!Anwalt\s)(?<!Gesellschafter\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(?<!klagenden\s)(?<!beklagten\s)(?<!Nebenintervenient\s)(?<!Nebenintervenientin\s)(?<!Nebenintervenienten\s)(?<!Nebenintervenientinnen\s)(?<!der\s)(?<!die\s)(?<!den\s)(?<!bei\s)(?<!von\s)(?<!Antragsgegnerin\s)(?<!Antragsteller\s)(?<!Rechtsanwalt\s)(?<!Vertreten\s)(Hoffschroer\s+Sanit\u00e4r\s+gesellschaft\s+mbH|Trinorglanz\s+Landwirtschaft\s+Gesellschaft\s+mbH|G\u00e4bel\s+Druck\s+GmbH|Schiffl\s+Bau\s+Limited|Unter\s+Bachlog\s+AG|Transport\s+Fenwald\s+GmbH|Sudalost-Immobilien\s+AG|Beckm\u00f6ller\s+Textil\s+AG|S\u00fcd\s+Monnex\s+Entwicklung\s+GmbH|Seegartnex-Marine|Wien\s+Donostuni\s+GmbH|Ost-Bildung\s+Werke|IQSW\s+Druck\s+GmbH|Stockhorst\s+und\s+Welfle\s+Verlag\s+GmbH)(?=[,\s]|\.|$)
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

