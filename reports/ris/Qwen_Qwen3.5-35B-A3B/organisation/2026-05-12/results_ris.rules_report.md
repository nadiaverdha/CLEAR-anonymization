# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-05-12T10:40:19.041861

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/ris/Qwen_Qwen3.5-35B-A3B/organisation/2026-05-12/config.yaml 
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
| Accuracy (exact match) | 98.0% |
| True Positives | 98 |
| False Positives | 464 |
| False Negatives | 247 |
| Total Gold Entities | 345 |
| Micro Precision | 17.4% |
| Micro Recall | 28.4% |
| Micro F1 | 21.6% |
| Macro F1 | 21.6% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `German Legal Organisation Partial Name with Context Dr/Mag` | 28.0% | 25.2% | 31.6% | 433 | 109 | 324 |
| `German Legal Organisation AG` | 4.3% | 8.5% | 2.9% | 117 | 10 | 107 |
| `German Legal Organisation GmbH` | 0.0% | 0.0% | 0.0% | 12 | 0 | 12 |
| `German Legal Organisation Limited` | 0.0% | 0.0% | 0.0% | 6 | 0 | 6 |
| `German Legal Organisation e.U.` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `German Legal Organisation GmbH & Co KG` | 0.0% | 0.0% | 0.0% | 11 | 0 | 11 |
| `German Legal Organisation Aktiengesellschaft` | 0.0% | 0.0% | 0.0% | 13 | 0 | 13 |
| `German Legal Organisation Specific Entities List` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `German Legal Organisation Partial Name with Context Dr/Mag`

**F1:** 0.280 | **Precision:** 0.252 | **Recall:** 0.316  

**Format:** `regex`  
**Description:**
Extracts organisation names followed by titles like Dr. or Mag. STRICTLY requires the name to contain a space or hyphen to avoid matching single-word personal names (e.g., 'Dr. Uwe Jamal').

**Content:**
```
(?<=Partei\s)([A-Z][A-Za-z0-9\.]+(?:[ -][A-Z][A-Za-z0-9\.]+)+)(?=,|Dr\.?|Mag\.?|Prof\.?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.252 | 0.316 | 0.280 | 433 | 109 | 324 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 109 | 324 | 236 |

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

**Example 3** (doc_id: `deanon_TRAIN/10Ob22_22s`) (sent_id: `deanon_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludger Radek, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Solar Fenwerk Limited, Amanda Ziergöbel Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Solar Fenwerk Limited` | `Solar Fenwerk Limited` |

**Missed by this rule (FN):**

- `Ludger Radek` (person)
- `Amanda Ziergöbel` (person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob28_19v`) (sent_id: `deanon_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei HochAnalyse GmbH, Piedro Ehmken, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Ludewigs Handel GmbH, Deborah Lochhuber, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `HochAnalyse GmbH` | `HochAnalyse GmbH` |
| `Ludewigs Handel GmbH` | `Ludewigs Handel GmbH` |

**Missed by this rule (FN):**

- `Piedro Ehmken` (person)
- `Deborah Lochhuber` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Karin Meiwaldt, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Katharina Tomandl, MA, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Karin Meiwaldt` — type mismatch — same span as gold: `Karin Meiwaldt`
- `Katharina Tomandl` — partial — pred is substring of gold: `Katharina Tomandl, MA`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Karin Meiwaldt`(person)
- `Katharina Tomandl, MA`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc22_13m`) (sent_id: `deanon_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Catharina Frielinghausen, Russische Föderation, gegen die verpflichtete Partei Gartcondon-Bildung GmbH, Alan Looß, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

**False Positives:**

- `Catharina Frielinghausen` — type mismatch — same span as gold: `Catharina Frielinghausen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Catharina Frielinghausen`(person)
- `Gartcondon-Bildung GmbH`(organisation)
- `Alan Looß`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Nc24_22v`) (sent_id: `deanon_TRAIN/10Nc24_22v_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofräte Mag. Ziegelbauer und Mag. Schober als weitere Richter in der Rechtssache der klagenden Partei Yorick Nosczyk, vertreten durch die Skribe Rechtsanwaelte GmbH in Wien, gegen die beklagte Partei Dipl.

**False Positives:**

- `Yorick Nosczyk` — type mismatch — same span as gold: `Yorick Nosczyk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Yorick Nosczyk`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei C. Dersudheim Digital GmbH, Taxlbergstraße 247, 8151 Rohrbach, Österreich, vertreten durch Dr. Carl Benkhofer, Rechtsanwalt in Wien, gegen die beklagte Partei Ingolf Grimpe, vertreten durch Greiml & Horwath Rechtsanwaltspartnerschaft in Graz, wegen 5.232 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 14 C 1302/11a des Bezirksgerichts Graz-West in nichtöffentlicher Sitzung, den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Graz-West das Bezirksgericht Fünfhaus bestimmt.

**False Positives:**

- `C. Dersudheim Digital GmbH` — partial — gold is substring of pred: `Dersudheim Digital GmbH`
- `Ingolf Grimpe` — type mismatch — same span as gold: `Ingolf Grimpe`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dersudheim Digital GmbH`(organisation)
- `Taxlbergstraße 247, 8151 Rohrbach, Österreich`(address)
- `Ingolf Grimpe`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob102_18z`) (sent_id: `deanon_TRAIN/10Ob102_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG, Adelheid Lochmaier, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Ursula Antoniadis, vertreten durch Knirsch – Braun – Fellner Rechtsanwälte in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 5. September 2018, GZ 40 R 39/18h-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Ursula Antoniadis` — type mismatch — same span as gold: `Ursula Antoniadis`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Skrzypczik + Duchscherer Digital AG`(organisation)
- `Adelheid Lochmaier`(person)
- `Ursula Antoniadis`(person)

</details>

---

## `German Legal Organisation AG`

**F1:** 0.043 | **Precision:** 0.085 | **Recall:** 0.029  

**Format:** `regex`  
**Description:**
Matches German company names ending in AG (Aktiengesellschaft), handling hyphens and spaces in the name part. Tightened to exclude 'Partei' and 'Antragsgegnerin' prefixes.

**Content:**
```
(?<!\w)([A-Z][A-Za-z0-9\-\s&+\.]+(?:\s+[A-Z][A-Za-z0-9\-\s&+\.]+)*\s+AG)(?!\s+der\s+AG|\s+Partei|\s+Antragsgegnerin|\s+Antragstellerin)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.085 | 0.029 | 0.043 | 117 | 10 | 107 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 10 | 107 | 333 |

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

**Example 1** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_117`)


Außerdem wird die Valwalduni-Handel AG eine Gegenüberstellung über die von der Änderung betroffenen Bestimmungen sowie die vollständige Fassung der neuen Bedingungen auf ihrer Internetseite veröffentlichen und die Gegenüberstellung dem Kunden auf sein Verlangen zur Verfügung stellen;

| Predicted | Gold |
|---|---|
| `Valwalduni-Handel AG` | `Valwalduni-Handel AG` |

**Example 2** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_118`)


auch darauf wird die Landwerlin&Plumke Versand AG in derMitteilung hinweisen.

| Predicted | Gold |
|---|---|
| `Landwerlin&Plumke Versand AG` | `Landwerlin&Plumke Versand AG` |

**Example 3** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_12`)


Unkenntnis des Disziplinarbeschuldigten von den Gründen der Daten Unizorstein AG für die beantragte Fortsetzung der Zwangsversteigerungsverfahren;

| Predicted | Gold |
|---|---|
| `Daten Unizorstein AG` | `Daten Unizorstein AG` |

**Example 4** (doc_id: `deanon_TRAIN/2Ob63_11w`) (sent_id: `deanon_TRAIN/2Ob63_11w_4`)


Holz Seewald AG, Kaiserbrunnengasse 6, 5122 Lindach, Österreich, beide vertreten durch Dr. Leopold Hirsch, Rechtsanwalt in Salzburg, wegen 38.967,48 EUR sA und Feststellung (Streitinteresse 20.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 10. Februar 2011, GZ 4 R 206/10g-29, womit das Urteil des Landesgerichts Salzburg vom 17. August 2010, GZ 7 Cg 49/09f-25, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Holz Seewald AG` | `Holz Seewald AG` |

**Missed by this rule (FN):**

- `Kaiserbrunnengasse 6, 5122 Lindach, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob102_18z`) (sent_id: `deanon_TRAIN/10Ob102_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG, Adelheid Lochmaier, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Ursula Antoniadis, vertreten durch Knirsch – Braun – Fellner Rechtsanwälte in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 5. September 2018, GZ 40 R 39/18h-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG` — partial — gold is substring of pred: `Skrzypczik + Duchscherer Digital AG`

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

**Example 3** (doc_id: `deanon_TRAIN/10Ob31_16f`) (sent_id: `deanon_TRAIN/10Ob31_16f_24`)


DasBerufungsgerichtgab der Berufung der beklagten Partei nur insoweit Folge, als die Leistungsfrist mit vier (statt mit drei) Monaten festgesetzt wurde, und ließ die Revision mit der Begründung zu, dass es an höchstgerichtlicher Rechtsprechung zur Auslegung der hier beanstandeten AGB-Klauseln fehle.

**False Positives:**

- `Rechtsprechung zur Auslegung der hier beanstandeten AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Ob31_16f`) (sent_id: `deanon_TRAIN/10Ob31_16f_37`)


Ein Verweis auf die in den AGB der beklagten Partei enthaltene Definition des Begriffs „Terminsverlust“ hätte genügt, ohne dass die Gefahr gegeben gewesen wäre, dass die Kommunikationsfähigkeit der gesamten Branche zum Erliegen komme.

**False Positives:**

- `Ein Verweis auf die in den AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `German Legal Organisation Aktiengesellschaft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the full word Aktiengesellschaft instead of just AG.

**Content:**
```
(?<!\w)([A-Z][A-Za-z0-9\-\s&+\.]+(?:\s+[A-Z][A-Za-z0-9\-\s&+\.]+)*\s+Aktiengesellschaft)(?!\s+Partei)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 13 | 0 | 13 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 13 | 345 |

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

- `Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft` — partial — gold is substring of pred: `Tracondon Aktiengesellschaft`

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

**Example 4** (doc_id: `deanon_TRAIN/2Ob256_12d`) (sent_id: `deanon_TRAIN/2Ob256_12d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Stallbauer Telekom Aktiengesellschaft, Poysdorfer Straße 5, 9341 Dobersberg, Österreich, vertreten durch Dr. Manfred Steininger, Rechtsanwalt in Wien, gegen die beklagte Partei DDr. Viktor Junkmanns, Bakk. iur., vertreten durch die ANWALTGMBH Rinner Teuchtmann in Linz, wegen 50.932,89 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2012, GZ 4 R 158/12a-20, womit das Urteil des Landesgerichts Linz vom 14. Juni 2012, GZ 5 Cg 119/11m-14, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Stallbauer Telekom Aktiengesellschaft` — partial — gold is substring of pred: `Stallbauer Telekom Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stallbauer Telekom Aktiengesellschaft`(organisation)
- `Poysdorfer Straße 5, 9341 Dobersberg, Österreich`(address)
- `DDr. Viktor Junkmanns, Bakk. iur.`(person)

</details>

---

## `German Legal Organisation GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches German company names ending in GmbH, including those with & Co KG suffixes. Tightened to exclude 'Partei' and 'Antragsgegnerin' prefixes.

**Content:**
```
(?<!\w)([A-Z][A-Za-z0-9\-\s&+\.]+(?:\s+[A-Z][A-Za-z0-9\-\s&+\.]+)*\s+GmbH(?:\s*&\s*Co\.?(?:\s*KG)?))(?!\s+Partei|\s+Antragsgegnerin|\s+Antragstellerin)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 12 | 0 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 12 | 315 |

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

**Example 3** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_5`)


Text Begründung: Der Kläger erwarb als Verbraucher im Juni 2003 über Vermittlung eines selbständigen Vermögensberaters Kommanditanteile an der Bestelmeyer+Keßelheim Software GmbH & Co KG im Nominale von 17.000 EUR zuzüglich 850 EUR Agio.

**False Positives:**

- `Software GmbH & Co KG` — positional overlap with gold: `Bestelmeyer+Keßelheim Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bestelmeyer+Keßelheim Software GmbH`(organisation)

**Example 4** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `German Legal Organisation GmbH & Co KG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specifically targets the complex GmbH & Co KG structure.

**Content:**
```
(?<!\w)([A-Z][A-Za-z0-9\-\s&+\.]+(?:\s+[A-Z][A-Za-z0-9\-\s&+\.]+)*\s+GmbH\s*&\s*Co\.?\s*KG)(?!\s+Partei|\s+der|\s+des)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 11 | 0 | 11 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 11 | 315 |

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

**Example 3** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_5`)


Text Begründung: Der Kläger erwarb als Verbraucher im Juni 2003 über Vermittlung eines selbständigen Vermögensberaters Kommanditanteile an der Bestelmeyer+Keßelheim Software GmbH & Co KG im Nominale von 17.000 EUR zuzüglich 850 EUR Agio.

**False Positives:**

- `Software GmbH & Co KG` — positional overlap with gold: `Bestelmeyer+Keßelheim Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bestelmeyer+Keßelheim Software GmbH`(organisation)

**Example 4** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `German Legal Organisation Limited`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches English-style Limited entities which may appear in German legal texts. Tightened to exclude 'Partei' prefix.

**Content:**
```
(?<!\w)([A-Z][A-Za-z0-9\-\s&+\.]+(?:\s+[A-Z][A-Za-z0-9\-\s&+\.]+)*\s+Limited)(?!\s+Partei)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 6 | 0 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 6 | 318 |

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

- `Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Hamberg Marine Limited` — partial — gold is substring of pred: `Hamberg Marine Limited`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hamberg Marine Limited`(organisation)
- `Kapellergasse 9, 4925 Lungdorf, Österreich`(address)

**Example 3** (doc_id: `deanon_TRAIN/2Ob91_22d`) (sent_id: `deanon_TRAIN/2Ob91_22d_4`)


Sloboda und Dr. Kikinger als weitere Richter in der Rechtssache der klagenden Partei Farina Dirker, vertreten durch Dr. Sven Rudolf Thorstensen, LL.M., Rechtsanwalt in Wien, gegen die beklagte Partei Lüttge Chemie Limited, René Luidthard, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 40.150,26 EUR sA, im Verfahren über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. Februar 2022, GZ 15 R 171/21h-33, den Beschluss gefasst:  Spruch Die Zurücknahme der Revision wird zur Kenntnis genommen.

**False Positives:**

- `Chemie Limited` — partial — pred is substring of gold: `Lüttge Chemie Limited`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Farina Dirker`(person)
- `Lüttge Chemie Limited`(organisation)
- `René Luidthard`(person)

**Example 4** (doc_id: `deanon_TRAIN/3Nc39_24a`) (sent_id: `deanon_TRAIN/3Nc39_24a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn und die Hofrätin Dr. Kodek als weitere Richter in der Ordinationssache der betreibenden Partei Wendy Janacek, vertreten durch Dr. Florian Johann Ernst Knaipp, Rechtsanwalt in Wien, gegen die verpflichtete Partei Siege KI Limited, Edgar Dölle, wegen 47.126,91 EUR sA, über den Antrag auf Ordination nach § 28 JN, den Beschluss gefasst:  Spruch Für die Bewilligung und den Vollzug der von der betreibenden Partei beabsichtigten Rechteexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Partei Siege KI Limited` — partial — gold is substring of pred: `Siege KI Limited`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wendy Janacek`(person)
- `Siege KI Limited`(organisation)
- `Edgar Dölle`(person)

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `German Legal Organisation Specific Entities List`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known entities from training data to ensure high precision for rare names. Added missing entities like 'Buth Analyse GmbH', 'Inn Synmon GmbH', 'Donau Wilverlog', 'KRV Technik', 'Beratung Valtal GmbH', 'Nexberkraft AG', 'Werkber-Garten AG', 'Klüs Event AG'.

**Content:**
```
\b(Buth Analyse GmbH|Inn Synmon GmbH|Donau Wilverlog|KRV Technik|Beratung Valtal GmbH|Nexberkraft AG|Werkber-Garten AG|Klüs Event AG|Tal Kelfurtzor Betriebe GmbH|Hamrosi Garten AG|SKSP Immobilien GmbH|Scherg und Kintzli Holz GmbH|Wagenlöhner Versand GmbH|SKRV IT Vertrieb|Medien Gartheim|WestGarten|Norglanz|Gruetze Handel Limited|RheinLogistik GmbH|Maschinenbau Waldtra GmbH|Bersud-Technik GmbH|JUPL Sicherheit GmbH|Mur Dorfheim GmbH)\b
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

## `German Legal Organisation Partial Name with Context Dr/Mag`

**F1:** 0.280 | **Precision:** 0.252 | **Recall:** 0.316  

**Format:** `regex`  
**Description:**
Extracts organisation names followed by titles like Dr. or Mag. STRICTLY requires the name to contain a space or hyphen to avoid matching single-word personal names (e.g., 'Dr. Uwe Jamal').

**Content:**
```
(?<=Partei\s)([A-Z][A-Za-z0-9\.]+(?:[ -][A-Z][A-Za-z0-9\.]+)+)(?=,|Dr\.?|Mag\.?|Prof\.?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.252 | 0.316 | 0.280 | 433 | 109 | 324 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 109 | 324 | 236 |

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

**Example 3** (doc_id: `deanon_TRAIN/10Ob22_22s`) (sent_id: `deanon_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludger Radek, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Solar Fenwerk Limited, Amanda Ziergöbel Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Solar Fenwerk Limited` | `Solar Fenwerk Limited` |

**Missed by this rule (FN):**

- `Ludger Radek` (person)
- `Amanda Ziergöbel` (person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob28_19v`) (sent_id: `deanon_TRAIN/10Ob28_19v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei HochAnalyse GmbH, Piedro Ehmken, vertreten durch Dr. Alexandra Slama, Rechtsanwältin in Klagenfurt, gegen die beklagte Partei Ludewigs Handel GmbH, Deborah Lochhuber, vertreten durch Grassner, Lenz, Thewanger & Partner, Rechtsanwälte in Linz, wegen 32.247 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Jänner 2019, GZ 1 R 159/18k-140, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `HochAnalyse GmbH` | `HochAnalyse GmbH` |
| `Ludewigs Handel GmbH` | `Ludewigs Handel GmbH` |

**Missed by this rule (FN):**

- `Piedro Ehmken` (person)
- `Deborah Lochhuber` (person)

**Example 5** (doc_id: `deanon_TRAIN/10Ob2_20x`) (sent_id: `deanon_TRAIN/10Ob2_20x_4`)


Matzka und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Ignaz Jungmichel, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei TalAlvalRobotik AG, Delila Leiteritz, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 25.617,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 29. Oktober 2019, GZ 2 R 151/19t-23, mit dem das Urteil des Landesgerichts Linz vom 21. August 2019, GZ 5 Cg 118/18z-19, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

| Predicted | Gold |
|---|---|
| `TalAlvalRobotik AG` | `TalAlvalRobotik AG` |

**Missed by this rule (FN):**

- `Ignaz Jungmichel` (person)
- `Delila Leiteritz` (person)

**Example 6** (doc_id: `deanon_TRAIN/10Ob31_16f`) (sent_id: `deanon_TRAIN/10Ob31_16f_3`)


Kopf Der Oberste Gerichtshof als Revisionsgericht hat durch den Hofrat Univ.-Prof. Dr. Neumayr als Vorsitzenden und den Hofrat Dr. Schramm, die Hofrätinnen Dr. Fichtenau und Dr. Tarmann-Prentner sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1060 Wien, Linke Wienzeile 18, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei CESW Technik Services AG, Mike Zachariä, vertreten durch Doralt Seist Csoklich Rechtsanwalts-Partnerschaft in Wien, wegen Unterlassung (30.500 EUR) und Urteilsveröffentlichung (5.500 EUR) über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Jänner 2016, GZ 30 R 35/15k-13, womit das Urteil des Landesgerichts St. Pölten vom 17. Juli 2015, GZ 3 Cg 7/15w-9, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `CESW Technik Services AG` | `CESW Technik Services AG` |

**Missed by this rule (FN):**

- `Mike Zachariä` (person)

**Example 7** (doc_id: `deanon_TRAIN/10Ob33_15y`) (sent_id: `deanon_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Inn Sudconkraft AG, Elisabeth Breitschwerdt, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Mazik Heizung GmbH, Hemma Rahn, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Inn Sudconkraft AG` | `Inn Sudconkraft AG` |
| `Mazik Heizung GmbH` | `Mazik Heizung GmbH` |

**Missed by this rule (FN):**

- `Elisabeth Breitschwerdt` (person)
- `Hemma Rahn` (person)

**Example 8** (doc_id: `deanon_TRAIN/17Ob17_10i`) (sent_id: `deanon_TRAIN/17Ob17_10i_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Griss als Vorsitzende und durch die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei VRDN Versand GmbH, David Tanzler, vertreten durch Held Berdnik Astner & Partner Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Dr. Livia Zinkel, vertreten durch Dr. Johannes Dörner und Dr. Alexander Singer, Rechtsanwälte in Graz, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 18.000 EUR), infolge „außerordentlichen“ Revisionsrekurses der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 28. September 2010, GZ 1 R 3/10h-23, womit infolge Rekurses der beklagten Partei der Beschluss des Handelsgerichts Wien vom 25. Oktober 2009, GZ 10 Cg 126/09y-10, bestätigt wurde, folgenden Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.

| Predicted | Gold |
|---|---|
| `VRDN Versand GmbH` | `VRDN Versand GmbH` |

**Missed by this rule (FN):**

- `David Tanzler` (person)
- `Dr. Livia Zinkel` (person)

**Example 9** (doc_id: `deanon_TRAIN/18OCg12_19t`) (sent_id: `deanon_TRAIN/18OCg12_19t_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Veith und die Hofräte Dr. Höllwerth, Priv.-Doz. Dr. Rassi und Mag. Painsi als weitere Richter in der Schiedsrechtssache der klagenden Partei Trabruckgart Holding GmbH, Jean Nellner, vertreten durch die SRG Stock Rafaseder Gruszkiewicz Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Lydia Astorre, Bulgarien, wegen Aufhebung eines Schiedsspruchs (Streitwert 257.397,45 EUR), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Klage wird als nicht zur Bestimmung einer Tagsatzung zur mündlichen Verhandlung geeignet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Trabruckgart Holding GmbH` | `Trabruckgart Holding GmbH` |

**Missed by this rule (FN):**

- `Jean Nellner` (person)
- `Lydia Astorre` (person)

**Example 10** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Herbes&Vißers Heizung GmbH, Waldemar Lokämper, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Traun-Luftfahrt GmbH, VetR DDr. Walter Stuehrmann, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

| Predicted | Gold |
|---|---|
| `Traun-Luftfahrt GmbH` | `Traun-Luftfahrt GmbH` |

**Missed by this rule (FN):**

- `Herbes&Vißers Heizung GmbH` (organisation)
- `Waldemar Lokämper` (person)
- `VetR DDr. Walter Stuehrmann` (person)

**Example 11** (doc_id: `deanon_TRAIN/1Ob106_20z`) (sent_id: `deanon_TRAIN/1Ob106_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Kodek, Mag. Wurzer, Mag. Dr. Wurdinger und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei IGK Bau Consulting AG, Ariadne Seebalt, vertreten durch Dr. Manfred Angerer und andere Rechtsanwälte in Klagenfurt am Wörthersee, gegen die beklagte Partei DI Roxana Pöll, vertreten durch Mag. Claudia Egarter, Rechtsanwältin in Klagenfurt am Wörthersee, wegen 5.457.559,15 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 28. Februar 2020, GZ 2 R 9/20s-150, mit dem das Urteil des Landesgerichts Klagenfurt vom 20. Februar 2017, GZ 21 Cg 24/13h-102, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `IGK Bau Consulting AG` | `IGK Bau Consulting AG` |

**Missed by this rule (FN):**

- `Ariadne Seebalt` (person)
- `DI Roxana Pöll` (person)

**Example 12** (doc_id: `deanon_TRAIN/1Ob140_14s`) (sent_id: `deanon_TRAIN/1Ob140_14s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer und Mag. Dr. Wurdinger sowie die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft, Meidlinger Hauptstraße 19, 5233 Erlach, Österreich, vertreten durch die Walch & Zehetbauer Rechtsanwälte OG, Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 344.011,19 EUR und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Juni 2014, GZ 4 R 202/13g-54, mit dem das Teilzwischenurteil des Landesgerichts Feldkirch vom 2. August 2013, GZ 8 Cg 143/11y-46, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Tracondon Aktiengesellschaft` | `Tracondon Aktiengesellschaft` |

**Missed by this rule (FN):**

- `Meidlinger Hauptstraße 19, 5233 Erlach, Österreich` (address)

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

**Example 15** (doc_id: `deanon_TRAIN/1Ob192_11h`) (sent_id: `deanon_TRAIN/1Ob192_11h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Hamberg Marine Limited, London, Kapellergasse 9, 4925 Lungdorf, Österreich, vertreten durch Thum Weinreich Schwarz Fuchsbauer Rechtsanwälte OG in St. Pölten, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 1,8 Mio EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Juni 2011, GZ 14 R 214/10h-39, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 3. September 2010, GZ 33 Cg 3/09t-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hamberg Marine Limited` | `Hamberg Marine Limited` |

**Missed by this rule (FN):**

- `Kapellergasse 9, 4925 Lungdorf, Österreich` (address)

**Example 16** (doc_id: `deanon_TRAIN/1Ob216_15v`) (sent_id: `deanon_TRAIN/1Ob216_15v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Ashley Meinering, vertreten durch Hon.-Prof. Dr. Michel Walter, Rechtsanwalt in Wien, gegen die beklagte Partei Walddon GmbH, Linn Voegelein, vertreten durch die Schlösser & Partner Rechtsanwälte OG, Graz, wegen 33.930 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 19. August 2015, GZ 13 R 74/15w-55, mit dem das Endurteil des Landesgerichts Korneuburg vom 26. Februar 2015, GZ 3 Cg 15/13h-50, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Walddon GmbH` | `Walddon GmbH` |

**Missed by this rule (FN):**

- `Ashley Meinering` (person)
- `Linn Voegelein` (person)

**Example 17** (doc_id: `deanon_TRAIN/1Ob26_20k`) (sent_id: `deanon_TRAIN/1Ob26_20k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Synsynfurt-Finanzen GmbH, Tanja Thielike, vertreten durch die Draxler Rexeis Sozietät von Rechtsanwälten OG, Graz, gegen die beklagte Partei Roberta Reumschüssel, Bakk. phil., vertreten durch Mag. Dr. Alfred Wansch, Rechtsanwalt in Wien, wegen Räumung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtsachen Wien als Berufungsgericht vom 13. November 2019, GZ 39 R 228/19x-70, mit dem das Urteil des Bezirksgerichts Hernals vom 30. April 2019, GZ 4 C 277/16f-64, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Synsynfurt-Finanzen GmbH` | `Synsynfurt-Finanzen GmbH` |

**Missed by this rule (FN):**

- `Tanja Thielike` (person)
- `Roberta Reumschüssel, Bakk. phil.` (person)

**Example 18** (doc_id: `deanon_TRAIN/1Ob51_11y`) (sent_id: `deanon_TRAIN/1Ob51_11y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei mj Kurt Schwenckel, vertreten durch Mag. Erich Frenner, Rechtsanwalt in Saalfelden, gegen die beklagte Partei Condon Planung GmbH, Corvin Heidtmeyer, vertreten durch Dr. Harald Schwendinger und Dr. Brigitte Piber Rechtsanwälte in Salzburg, wegen 5.100 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 30. Dezember 2010, GZ 53 R 273/10v-12, mit dem über die Berufung der beklagten Partei das Zwischenurteil des Bezirksgerichts Saalfelden vom 23. Juni 2010, GZ 2 C 454/10z-7, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Condon Planung GmbH` | `Condon Planung GmbH` |

**Missed by this rule (FN):**

- `Kurt Schwenckel` (person)
- `Corvin Heidtmeyer` (person)

**Example 19** (doc_id: `deanon_TRAIN/1Ob51_14b`) (sent_id: `deanon_TRAIN/1Ob51_14b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Landwirtschaft Glanzlemglanz GmbH, Erhard Blaufuß, vertreten durch Dr. Arno Kempf, Rechtsanwalt in Spittal an der Drau, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Landwirtschaft Glanzlemglanz GmbH` | `Landwirtschaft Glanzlemglanz GmbH` |

**Missed by this rule (FN):**

- `Erhard Blaufuß` (person)

**Example 20** (doc_id: `deanon_TRAIN/1Ob82_18t`) (sent_id: `deanon_TRAIN/1Ob82_18t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei MurUmwelt GmbH, Oskar Stelzel, vertreten durch die KRONBERGER Rechtsanwälte Gesellschaft mbH, Wien, gegen die beklagte Partei Brian Hüpsch, vertreten durch Dr. Werner Loos, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 14. März 2018, GZ 38 R 303/17s-48, mit dem das Urteil des Bezirksgerichts Fünfhaus vom 4. August 2017, GZ 22 C 163/16w-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `MurUmwelt GmbH` | `MurUmwelt GmbH` |

**Missed by this rule (FN):**

- `Oskar Stelzel` (person)
- `Brian Hüpsch` (person)

**Example 21** (doc_id: `deanon_TRAIN/2Ob178_18t`) (sent_id: `deanon_TRAIN/2Ob178_18t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Veith als Vorsitzenden, den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé sowie die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Garttri Sicherheit -GesmbH, Alpendorfsiedlung 14, 4209 Linzerberg, Österreich, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, wider die beklagte Partei Vogelsanger Marine GmbH, Juri Büttgens, vertreten durch Mag. Dr. Dirk Just, Rechtsanwalt in Wien, wegen (restlich) 30.000 EUR sA, über die „außerordentliche Revision“ der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Juli 2018, GZ 4 R 79/18v-157, mit welchem das Endurteil des Handelsgerichts Wien vom 9. April 2018, GZ 40 Cg 12/11g-153, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

| Predicted | Gold |
|---|---|
| `Vogelsanger Marine GmbH` | `Vogelsanger Marine GmbH` |

**Missed by this rule (FN):**

- `Garttri Sicherheit` (organisation)
- `Alpendorfsiedlung 14, 4209 Linzerberg, Österreich` (address)
- `Juri Büttgens` (person)

**Example 22** (doc_id: `deanon_TRAIN/2Ob256_12d`) (sent_id: `deanon_TRAIN/2Ob256_12d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Stallbauer Telekom Aktiengesellschaft, Poysdorfer Straße 5, 9341 Dobersberg, Österreich, vertreten durch Dr. Manfred Steininger, Rechtsanwalt in Wien, gegen die beklagte Partei DDr. Viktor Junkmanns, Bakk. iur., vertreten durch die ANWALTGMBH Rinner Teuchtmann in Linz, wegen 50.932,89 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2012, GZ 4 R 158/12a-20, womit das Urteil des Landesgerichts Linz vom 14. Juni 2012, GZ 5 Cg 119/11m-14, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Stallbauer Telekom Aktiengesellschaft` | `Stallbauer Telekom Aktiengesellschaft` |

**Missed by this rule (FN):**

- `Poysdorfer Straße 5, 9341 Dobersberg, Österreich` (address)
- `DDr. Viktor Junkmanns, Bakk. iur.` (person)

**Example 23** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden, die Hofräte Dr. Veith und Dr. Musger sowie die Hofrätinnen Dr. E. Solé und Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Luigi Neimeier, vertreten durch Rechtsanwälte Estermann & Partner OG in Mattighofen, gegen die beklagte Partei LNC KI Solutions GmbH, Kordelia Grauel, vertreten durch Dr. Herbert Harlander und Mag. Wolfgang Harlander, Rechtsanwälte in Salzburg, wegen 33.251,85 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. März 2015, GZ 2 R 1/15b-37, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Salzburg vom 23. Oktober 2014, GZ 4 Cg 27/13d-33, bestätigt wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `LNC KI Solutions GmbH` | `LNC KI Solutions GmbH` |

**Missed by this rule (FN):**

- `Luigi Neimeier` (person)
- `Kordelia Grauel` (person)

**Example 24** (doc_id: `deanon_TRAIN/3Nc39_24a`) (sent_id: `deanon_TRAIN/3Nc39_24a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn und die Hofrätin Dr. Kodek als weitere Richter in der Ordinationssache der betreibenden Partei Wendy Janacek, vertreten durch Dr. Florian Johann Ernst Knaipp, Rechtsanwalt in Wien, gegen die verpflichtete Partei Siege KI Limited, Edgar Dölle, wegen 47.126,91 EUR sA, über den Antrag auf Ordination nach § 28 JN, den Beschluss gefasst:  Spruch Für die Bewilligung und den Vollzug der von der betreibenden Partei beabsichtigten Rechteexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

| Predicted | Gold |
|---|---|
| `Siege KI Limited` | `Siege KI Limited` |

**Missed by this rule (FN):**

- `Wendy Janacek` (person)
- `Edgar Dölle` (person)

**Example 25** (doc_id: `deanon_TRAIN/3Ob147_20v`) (sent_id: `deanon_TRAIN/3Ob147_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Kraftnorost Wind GmbH, Roderich Holtze, vertreten durch Mag. Andreas Kleiber, Rechtsanwalt in Wien, gegen die beklagte Partei Annette Fiss verein Ing. Kirstin Movcan, vertreten durch Pflaum Karlberger Wiener Opetnik, Rechtsanwälte in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 22. Juli 2020, GZ 40 R 37/20t-27, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Kraftnorost Wind GmbH` | `Kraftnorost Wind GmbH` |

**Missed by this rule (FN):**

- `Roderich Holtze` (person)
- `Annette Fiss` (person)
- `Ing. Kirstin Movcan` (person)

**Example 26** (doc_id: `deanon_TRAIN/3Ob150_16d`) (sent_id: `deanon_TRAIN/3Ob150_16d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Jensik und Dr. Roch und die Hofrätin Dr. Kodek als weitere Richter in der Exekutionssache der betreibenden Partei SGQ Versand GmbH, Hon.-Prof.in Dr.in Silvana Früboes, vertreten durch Dr. Andrea Gesinger, Rechtsanwältin in Salzburg, gegen die verpflichtete Partei Talseemon GmbH, Finn Auctor, vertreten durch Doschek Rechtsanwalts GmbH in Wien, wegen 9.718,32 EUR sA, über den Revisionsrekurs und Rekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 24. Mai 2016, GZ 22 R 132/16i, 133/16m-21, womit der Beschluss des Bezirksgerichts St. Johann im Pongau vom 17. März 2016, GZ 22 E 1592/15d-14, abgeändert und der Beschluss des Bezirksgerichts St. Johann im Pongau vom 6. April 2016, GZ 22 E 1592/15d-13, aufgehoben wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs und der Rekurs werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `SGQ Versand GmbH` | `SGQ Versand GmbH` |
| `Talseemon GmbH` | `Talseemon GmbH` |

**Missed by this rule (FN):**

- `Hon.-Prof.in Dr.in Silvana Früboes` (person)
- `Finn Auctor` (person)

**Example 27** (doc_id: `deanon_TRAIN/3Ob164_20v`) (sent_id: `deanon_TRAIN/3Ob164_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Bruckgartver GmbH, MedR StR René Titz, vertreten durch Dr. Reinhard Schanda, Rechtsanwalt in Wien, gegen die beklagte Partei Ofczarczik Planung AG, Dipl.

| Predicted | Gold |
|---|---|
| `Bruckgartver GmbH` | `Bruckgartver GmbH` |
| `Ofczarczik Planung AG` | `Ofczarczik Planung AG` |

**Missed by this rule (FN):**

- `MedR StR René Titz` (person)

**Example 28** (doc_id: `deanon_TRAIN/3Ob17_20a`) (sent_id: `deanon_TRAIN/3Ob17_20a_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie die Hofräte Priv.-Doz. Dr. Rassi und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Exekutionssache betreibenden Partei Heizung Werkuni Aktiengesellschaft, P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich, vertreten durch Dr. Roland Grilc ua, Rechtsanwälte in Klagenfurt am Wörthersee, gegen die verpflichtete Partei Dorothea Eiken Bank, Peter Eitenmüller, vertreten durch Diwok Hermann Petsche Rechtsanwälte LLP Co KG in Wien, wegen 12.602.980,92 EUR sA, über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. November 2019, GZ 46 R 293/19g-18, mit dem der Beschluss des Bezirksgerichts Favoriten vom 17. April 2019, GZ 17 E 1298/19z-2, bestätigt wurde, den Beschluss gefasst:  Spruch I. Der Revisionsrekurs wird, soweit er sich gegen die Bestätigung der Exekutionsbewilligung richtet, als jedenfalls unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Heizung Werkuni Aktiengesellschaft` | `Heizung Werkuni Aktiengesellschaft` |

**Missed by this rule (FN):**

- `P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich` (address)
- `Dorothea Eiken` (person)
- `Peter Eitenmüller` (person)

**Example 29** (doc_id: `deanon_TRAIN/3Ob185_22k`) (sent_id: `deanon_TRAIN/3Ob185_22k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn und die Hofrätinnen Dr. Weixelbraun-Mohr, Dr. Kodek und Mag. Wessely-Kristöfel als weitere Richter in der Exekutionssache der betreibenden Partei Dr. Brian Adamska, vertreten durch Dr. Martin Neuwirth, Dr. Alexander Neurauter, Rechtsanwälte in Wien, gegen die verpflichtete Partei Kelglanzver-Software GmbH, Egon Libert, vertreten durch Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH in Wien, wegen zwangsweiser Räumung, über den Revisionsrekurs der betreibenden Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 12. August 2022, GZ 40 R 104/22y-20, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 8. April 2022, GZ 49 E 11/22w-3, abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Kelglanzver-Software GmbH` | `Kelglanzver-Software GmbH` |

**Missed by this rule (FN):**

- `Dr. Brian Adamska` (person)
- `Egon Libert` (person)

**Example 30** (doc_id: `deanon_TRAIN/3Ob209_21p`) (sent_id: `deanon_TRAIN/3Ob209_21p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Nexostlem GmbH & Co KG, Rehlackenweg 5G, 8451 Pernitsch, Österreich, vertreten durch DDr. Heinz Dietmar Schimanko, Rechtsanwalt in Wien, gegen die beklagte Partei RheinLandwirtschaft Vertrieb GmbH, Klaus Dissler, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH & Co KG in Wien, wegen 7.906,82 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 7. Juni 2021, GZ 38 R 66/21v-16, mit dem das Urteil des Bezirksgerichts Favoriten vom 19. Jänner 2021, GZ 3 C 503/20f-12, abgeändert wurde, zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `RheinLandwirtschaft Vertrieb GmbH` | `RheinLandwirtschaft Vertrieb GmbH` |

**Missed by this rule (FN):**

- `Nexostlem GmbH` (organisation)
- `Rehlackenweg 5G, 8451 Pernitsch, Österreich` (address)
- `Klaus Dissler` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Karin Meiwaldt, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Katharina Tomandl, MA, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Karin Meiwaldt` — type mismatch — same span as gold: `Karin Meiwaldt`
- `Katharina Tomandl` — partial — pred is substring of gold: `Katharina Tomandl, MA`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Karin Meiwaldt`(person)
- `Katharina Tomandl, MA`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc22_13m`) (sent_id: `deanon_TRAIN/10Nc22_13m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Exekutionssache der betreibenden Partei Catharina Frielinghausen, Russische Föderation, gegen die verpflichtete Partei Gartcondon-Bildung GmbH, Alan Looß, wegen 1.553,569,52 EUR sA, den Beschluss gefasst:  Spruch Der Antrag der betreibenden Partei auf „Anerkennung und Genehmigung einer Vollstreckung“ vom 6. 9. 2013 wird an das Bezirksgericht Innere Stadt Wien überwiesen.

**False Positives:**

- `Catharina Frielinghausen` — type mismatch — same span as gold: `Catharina Frielinghausen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Catharina Frielinghausen`(person)
- `Gartcondon-Bildung GmbH`(organisation)
- `Alan Looß`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Nc24_22v`) (sent_id: `deanon_TRAIN/10Nc24_22v_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofräte Mag. Ziegelbauer und Mag. Schober als weitere Richter in der Rechtssache der klagenden Partei Yorick Nosczyk, vertreten durch die Skribe Rechtsanwaelte GmbH in Wien, gegen die beklagte Partei Dipl.

**False Positives:**

- `Yorick Nosczyk` — type mismatch — same span as gold: `Yorick Nosczyk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Yorick Nosczyk`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei C. Dersudheim Digital GmbH, Taxlbergstraße 247, 8151 Rohrbach, Österreich, vertreten durch Dr. Carl Benkhofer, Rechtsanwalt in Wien, gegen die beklagte Partei Ingolf Grimpe, vertreten durch Greiml & Horwath Rechtsanwaltspartnerschaft in Graz, wegen 5.232 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 14 C 1302/11a des Bezirksgerichts Graz-West in nichtöffentlicher Sitzung, den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Graz-West das Bezirksgericht Fünfhaus bestimmt.

**False Positives:**

- `C. Dersudheim Digital GmbH` — partial — gold is substring of pred: `Dersudheim Digital GmbH`
- `Ingolf Grimpe` — type mismatch — same span as gold: `Ingolf Grimpe`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dersudheim Digital GmbH`(organisation)
- `Taxlbergstraße 247, 8151 Rohrbach, Österreich`(address)
- `Ingolf Grimpe`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob102_18z`) (sent_id: `deanon_TRAIN/10Ob102_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG, Adelheid Lochmaier, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Ursula Antoniadis, vertreten durch Knirsch – Braun – Fellner Rechtsanwälte in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 5. September 2018, GZ 40 R 39/18h-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Ursula Antoniadis` — type mismatch — same span as gold: `Ursula Antoniadis`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Skrzypczik + Duchscherer Digital AG`(organisation)
- `Adelheid Lochmaier`(person)
- `Ursula Antoniadis`(person)

**Example 5** (doc_id: `deanon_TRAIN/10Ob105_15m`) (sent_id: `deanon_TRAIN/10Ob105_15m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Alsteinost GmbH, Anna Kisaoglu, Bakk. iur., vertreten durch Dr. Erich Kafka und Dr. Manfred Palkovits, Rechtsanwälte in Wien, gegen die beklagte Partei Ing. Mag. Adam Kratki, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 11. Juni 2015, GZ 39 R 41/15s-29, in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch

**False Positives:**

- `Ing. Mag. Adam Kratki` — partial — gold is substring of pred: `Mag. Adam Kratki`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alsteinost GmbH`(organisation)
- `Anna Kisaoglu, Bakk. iur.`(person)
- `Mag. Adam Kratki`(person)

**Example 6** (doc_id: `deanon_TRAIN/10Ob10_18w`) (sent_id: `deanon_TRAIN/10Ob10_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Jonasgasse 71, 4760 Weeg, Österreich, vertreten durch Dr. Alois Schneider, Rechtsanwalt in Rattenberg, wider die beklagte Partei Corinna Elfe, vertreten durch Dr. Walter Hausberger, Dr. Katharina Moritz und Dr. Alfred Schmidt, Rechtsanwälte in Wörgl, wegen Entfernung und Unterlassung (Revisionsinteresse 10.000 EUR), infolge Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 3. November 2017, GZ 3 R 172/17s-22, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Rattenberg vom 17. Mai 2017, GZ 3 C 401/15k-18, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Corinna Elfe` — type mismatch — same span as gold: `Corinna Elfe`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jonasgasse 71, 4760 Weeg, Österreich`(address)
- `Corinna Elfe`(person)

**Example 7** (doc_id: `deanon_TRAIN/10Ob13_20i`) (sent_id: `deanon_TRAIN/10Ob13_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Miranda Klagemann, vertreten durch Dr. Andreas Ladstätter, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. DI Adolf Kowallek, und 2. Ing. Janis Grottian, beide vertreten durch Dr. Walter Schuhmeister und Mag. Franz Haydn, Rechtsanwälte in Schwechat, wegen 15.000 EUR sA, infolge Revision der beklagten Parteien (Revisionsinteresse 6.250 EUR) gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 30. Jänner 2019, GZ 34 R 66/18k-27, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Innere Stadt Wien vom 23. März 2018, GZ 37 C 780/16f-18, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Miranda Klagemann` — type mismatch — same span as gold: `Miranda Klagemann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Miranda Klagemann`(person)
- `DI Adolf Kowallek`(person)
- `Ing. Janis Grottian`(person)

**Example 8** (doc_id: `deanon_TRAIN/10Ob16_16z`) (sent_id: `deanon_TRAIN/10Ob16_16z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Josepha Mikolajetz, vertreten durch Dr. Clemens Lintschinger, Rechtsanwalt in Wien, gegen die beklagte Partei Erhard Arslanboga, vertreten durch Mag. Dr. Georg Backhausen, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 27. Jänner 2016, GZ 38 R 265/15z-45, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Josepha Mikolajetz` — type mismatch — same span as gold: `Josepha Mikolajetz`
- `Erhard Arslanboga` — type mismatch — same span as gold: `Erhard Arslanboga`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Josepha Mikolajetz`(person)
- `Erhard Arslanboga`(person)

**Example 9** (doc_id: `deanon_TRAIN/10Ob18_25g`) (sent_id: `deanon_TRAIN/10Ob18_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Steger und Dr. Annerl und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der gefährdeten Partei Stanley Plogmeyer, vertreten durch Mag. Franz Eckl, Rechtsanwalt in Zwettl, gegen die Gegnerin der gefährdeten Partei Tal-Daten GmbH, Karlheinz Hornschuck, vertreten durch die Skribe Rechtsanwälte GmbH in Wien, wegen Erlassung einer einstweiligen Verfügung, über den Revisionsrekurs der Gegnerin der gefährdeten Partei gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 31. Jänner 2025, GZ 1 R 202/24x-16, mit dem der Beschluss des Bezirksgerichts Zwettl vom 5. November 2024, GZ 1 C 847/24t-5, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Stanley Plogmeyer` — type mismatch — same span as gold: `Stanley Plogmeyer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stanley Plogmeyer`(person)
- `Tal-Daten GmbH`(organisation)
- `Karlheinz Hornschuck`(person)

**Example 10** (doc_id: `deanon_TRAIN/10Ob19_25d`) (sent_id: `deanon_TRAIN/10Ob19_25d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober, Dr. Annerl, Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Ernestine Feifel, vertreten durch die Salburg Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Jean Kandziora, vertreten durch die BEURLE Rechtsanwälte GmbH & Co KG in Linz, wegen Feststellung (Streitwert 5.100 EUR), über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 19. Dezember 2024, GZ 1 R 255/24f-28, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 31. Mai 2024, GZ 15 C 939/23d-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Ernestine Feifel` — type mismatch — same span as gold: `Ernestine Feifel`
- `Jean Kandziora` — type mismatch — same span as gold: `Jean Kandziora`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Ernestine Feifel`(person)
- `Jean Kandziora`(person)

**Example 11** (doc_id: `deanon_TRAIN/10Ob22_22s`) (sent_id: `deanon_TRAIN/10Ob22_22s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber, und die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Ludger Radek, vertreten durch Dr. Sven Rudolf Thorstensen, Rechtsanwalt in Wien, gegen die beklagte Partei Solar Fenwerk Limited, Amanda Ziergöbel Malta, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 57.761,81 EUR und 6.000 USD sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. März 2022, GZ 12 R 26/22i-49, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. Jänner 2022, GZ 11 Cg 65/20i-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Ludger Radek` — type mismatch — same span as gold: `Ludger Radek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ludger Radek`(person)
- `Solar Fenwerk Limited`(organisation)
- `Amanda Ziergöbel`(person)

**Example 12** (doc_id: `deanon_TRAIN/10Ob23_15b`) (sent_id: `deanon_TRAIN/10Ob23_15b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Bruno Altevogt, BA MBA, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, gegen die beklagten Parteien 1.

**False Positives:**

- `Bruno Altevogt` — partial — pred is substring of gold: `Bruno Altevogt, BA MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bruno Altevogt, BA MBA`(person)

**Example 13** (doc_id: `deanon_TRAIN/10Ob26_14t`) (sent_id: `deanon_TRAIN/10Ob26_14t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Massimo Juderjahn, vertreten durch Dr. Klaus Schiller, Rechtsanwalt in Schwanenstadt, gegen die beklagten Parteien 1.

**False Positives:**

- `Massimo Juderjahn` — type mismatch — same span as gold: `Massimo Juderjahn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Massimo Juderjahn`(person)

**Example 14** (doc_id: `deanon_TRAIN/10Ob2_20x`) (sent_id: `deanon_TRAIN/10Ob2_20x_4`)


Matzka und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Ignaz Jungmichel, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei TalAlvalRobotik AG, Delila Leiteritz, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 25.617,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 29. Oktober 2019, GZ 2 R 151/19t-23, mit dem das Urteil des Landesgerichts Linz vom 21. August 2019, GZ 5 Cg 118/18z-19, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

**False Positives:**

- `Ignaz Jungmichel` — type mismatch — same span as gold: `Ignaz Jungmichel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ignaz Jungmichel`(person)
- `TalAlvalRobotik AG`(organisation)
- `Delila Leiteritz`(person)

**Example 15** (doc_id: `deanon_TRAIN/10Ob2_22z`) (sent_id: `deanon_TRAIN/10Ob2_22z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Calvin Amorelli, vertreten durch Dr. Martin Hembach, Rechtsanwalt in Wiener Neustadt, gegen die beklagte Partei Strathewerd u. Niemetz Metall GmbH, Dolores Chatzakis, vertreten durch Mag. Martin Trapichler, Rechtsanwalt in Wien, wegen 13.639,20 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 25. Oktober 2021, GZ 18 R 67/21p-16, mit dem das Urteil des Bezirksgerichts Wiener Neustadt vom 7. Juni 2021, GZ 7 C 117/21b-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Calvin Amorelli` — type mismatch — same span as gold: `Calvin Amorelli`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Calvin Amorelli`(person)
- `Strathewerd u. Niemetz Metall GmbH`(organisation)
- `Dolores Chatzakis`(person)

**Example 16** (doc_id: `deanon_TRAIN/10Ob38_25y`) (sent_id: `deanon_TRAIN/10Ob38_25y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Arielle Schallmair, gegen die beklagte Partei Dr. Daisy Nagelkrämer, vertreten durch Ing. Dr. Stefan Krall und Dr. Oliver Kühnl, Rechtsanwälte in Innsbruck, wegen 9.456 EUR sA (Revisionsinteresse 9.268,50 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 25. Februar 2025, GZ 21 R 434/24f-29, mit dem das Urteil des Bezirksgerichts Seekirchen am Wallersee vom 5. September 2024, GZ 2 C 1107/23d-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Arielle Schallmair` — type mismatch — same span as gold: `Arielle Schallmair`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Arielle Schallmair`(person)
- `Dr. Daisy Nagelkrämer`(person)

**Example 17** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Dr. Marlon Richel, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Freimut & Assenov Sicherheit GmbH in Liqu, Spazgasse 41, 8524 Greim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 31.596,47 EUR und Feststellung (6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 18. Juni 2019, GZ 129 R 50/19z-21, mit dem das Urteil des Handelsgerichts Wien vom 28. März 2019, GZ 54 Cg 71/18x-17, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Marlon Richel` — type mismatch — same span as gold: `Dr. Marlon Richel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Marlon Richel`(person)
- `Freimut & Assenov Sicherheit GmbH`(organisation)
- `Spazgasse 41, 8524 Greim, Österreich`(address)

**Example 18** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Daniel Wiegand, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei West-Medien Manufaktur GmbH in Liqu, Kanzelweg 32, 4850 Oberthalheim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `DI Daniel Wiegand` — type mismatch — same span as gold: `DI Daniel Wiegand`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DI Daniel Wiegand`(person)
- `West-Medien Manufaktur GmbH`(organisation)
- `Kanzelweg 32, 4850 Oberthalheim, Österreich`(address)

**Example 19** (doc_id: `deanon_TRAIN/10Ob88_19t`) (sent_id: `deanon_TRAIN/10Ob88_19t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Fatima Berlin, BSc, vertreten durch Frysak & Frysak Rechtsanwalts-Partnerschaft in Wien, gegen die beklagte Partei Otto Cesar, MSc, vertreten durch Maraszto Milisits Rechtsanwälte OG in Wien, wegen 18.800 EUR sA und Feststellung (Streitwert 5.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 14. Oktober 2019, GZ 11 R 145/19b-16, womit das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 28. Mai 2019, GZ 27 Cg 6/19d-11, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Fatima Berlin` — partial — pred is substring of gold: `Fatima Berlin, BSc`
- `Otto Cesar` — partial — pred is substring of gold: `Otto Cesar, MSc`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Fatima Berlin, BSc`(person)
- `Otto Cesar, MSc`(person)

**Example 20** (doc_id: `deanon_TRAIN/10ObS21_10a`) (sent_id: `deanon_TRAIN/10ObS21_10a_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Schinko als Vorsitzenden, die Hofräte Dr. Fellinger und Dr. Hoch sowie die fachkundigen Laienrichter Mag. Irene Kienzl (aus dem Kreis der Arbeitgeber) und Eva-Maria Florianschütz (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Gertrud Johanna Ostrovska, gegen die beklagte Partei Steiermärkische Gebietskrankenkasse, 8011 Graz, Josef-Pongratz-Platz 1, vertreten durch Das Haus des Rechts Rechtsanwälte Destaller-Mader in Graz, wegen Kostenübernahme, infolge Rekurses der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 19. November 2009, GZ 8 Rs 73/09f-10, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 1. September 2009, GZ 29 Cgs 90/09s-6, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Gertrud Johanna Ostrovska` — partial — gold is substring of pred: `Ostrovska`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ostrovska`(person)

**Example 21** (doc_id: `deanon_TRAIN/10ObS49_15a`) (sent_id: `deanon_TRAIN/10ObS49_15a_4`)


Brigitte Augustin (aus dem Kreis der Arbeitgeber) und Peter Schönhofer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Samantha Neunteufl, Deutschland, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Vorarlberger Gebietskrankenkasse, Jahngasse 4, 6850 Dornbirn, vertreten durch Hoffmann & Brandstätter Rechtsanwälte KG in Innsbruck, wegen Kinderbetreuungsgeld, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 12. Februar 2015, GZ 11 Rs 4/15k-10, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 28. Oktober 2014, GZ 20 Cgs 71/14k-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Samantha Neunteufl` — type mismatch — same span as gold: `Samantha Neunteufl`
- `Vorarlberger Gebietskrankenkasse` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Samantha Neunteufl`(person)

**Example 22** (doc_id: `deanon_TRAIN/10ObS7_10t`) (sent_id: `deanon_TRAIN/10ObS7_10t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Schinko als Vorsitzenden, die Hofräte Dr. Fellinger und Hon.-Prof. Dr. Neumayr sowie die fachkundigen Laienrichter Dr. Thomas Neumann (aus dem Kreis der Arbeitgeber) und KR Mag. Michaela Haydter (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Wilhelm Peter Perlt, vertreten durch Wukovits & Eppelein Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Pensionsversicherungsanstalt, Friedrich Hillegeist-Straße 1, 1021 Wien, wegen Feststellung der Versicherungszeiten, infolge außerordentlicher Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 19. Dezember 2008, GZ 9 Rs 160/08b-19, den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Wilhelm Peter Perlt` — partial — gold is substring of pred: `Perlt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Perlt`(person)

**Example 23** (doc_id: `deanon_TRAIN/10ObS92_17b`) (sent_id: `deanon_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Dr.in Gerlinde Saltzmann, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Dr.in Gerlinde Saltzmann` — type mismatch — same span as gold: `Dr.in Gerlinde Saltzmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Gerlinde Saltzmann`(person)

**Example 24** (doc_id: `deanon_TRAIN/17Ob17_10i`) (sent_id: `deanon_TRAIN/17Ob17_10i_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Griss als Vorsitzende und durch die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei VRDN Versand GmbH, David Tanzler, vertreten durch Held Berdnik Astner & Partner Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Dr. Livia Zinkel, vertreten durch Dr. Johannes Dörner und Dr. Alexander Singer, Rechtsanwälte in Graz, wegen Unterlassung, Beseitigung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 18.000 EUR), infolge „außerordentlichen“ Revisionsrekurses der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 28. September 2010, GZ 1 R 3/10h-23, womit infolge Rekurses der beklagten Partei der Beschluss des Handelsgerichts Wien vom 25. Oktober 2009, GZ 10 Cg 126/09y-10, bestätigt wurde, folgenden Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.

**False Positives:**

- `Dr. Livia Zinkel` — type mismatch — same span as gold: `Dr. Livia Zinkel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VRDN Versand GmbH`(organisation)
- `David Tanzler`(person)
- `Dr. Livia Zinkel`(person)

**Example 25** (doc_id: `deanon_TRAIN/18OCg12_19t`) (sent_id: `deanon_TRAIN/18OCg12_19t_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Veith und die Hofräte Dr. Höllwerth, Priv.-Doz. Dr. Rassi und Mag. Painsi als weitere Richter in der Schiedsrechtssache der klagenden Partei Trabruckgart Holding GmbH, Jean Nellner, vertreten durch die SRG Stock Rafaseder Gruszkiewicz Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Lydia Astorre, Bulgarien, wegen Aufhebung eines Schiedsspruchs (Streitwert 257.397,45 EUR), in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Klage wird als nicht zur Bestimmung einer Tagsatzung zur mündlichen Verhandlung geeignet zurückgewiesen.

**False Positives:**

- `Lydia Astorre` — type mismatch — same span as gold: `Lydia Astorre`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Trabruckgart Holding GmbH`(organisation)
- `Jean Nellner`(person)
- `Lydia Astorre`(person)

**Example 26** (doc_id: `deanon_TRAIN/1Nc2_20i`) (sent_id: `deanon_TRAIN/1Nc2_20i_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie den Hofrat Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei KommR Franz Kubank, vertreten durch Dr. Michael Wukoschitz, Rechtsanwalt in Wien, gegen die beklagte Partei Laurin Aichhorn a.d., Timothy Schulmeister, Serbien, wegen 600 EUR sA, über den Ordinationsantrag nach § 28 JN den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `KommR Franz Kubank` — type mismatch — same span as gold: `KommR Franz Kubank`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `KommR Franz Kubank`(person)
- `Laurin Aichhorn`(person)
- `Timothy Schulmeister`(person)

**Example 27** (doc_id: `deanon_TRAIN/1Ob103_17d`) (sent_id: `deanon_TRAIN/1Ob103_17d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Laura Overbeeke, BA, vertreten durch Dr. Gerhard Ebenbichler, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. Janis Marxmeyer, und 2.

**False Positives:**

- `Laura Overbeeke` — partial — pred is substring of gold: `Laura Overbeeke, BA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Laura Overbeeke, BA`(person)
- `Janis Marxmeyer`(person)

**Example 28** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Dr. Alice Wickertsheimer, gegen die beklagten Parteien 1.

**False Positives:**

- `Dr. Alice Wickertsheimer` — type mismatch — same span as gold: `Dr. Alice Wickertsheimer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Alice Wickertsheimer`(person)

**Example 29** (doc_id: `deanon_TRAIN/1Ob152_24w`) (sent_id: `deanon_TRAIN/1Ob152_24w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Musger als Vorsitzenden sowie die Hofrätin und die Hofräte Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei VetR Volkmar Acar KG, FN FN823951l, vertreten durch Dr. Eva-Maria Bachmann-Lang, Dr. Christian Bachmann, Rechtsanwälte in Wien, gegen die beklagte Partei „ Nemtschok Touristik “ Wilnorlex Werke gmbH, FN FN545761v, vertreten durch die GRAF ISOLA Rechtsanwälte GmbH in Wien, wegen 51.843,91 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 3. Juli 2024, GZ 1 R 17/24p-39, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `VetR Volkmar Acar KG` — partial — gold is substring of pred: `VetR Volkmar Acar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VetR Volkmar Acar`(person)
- `FN823951l`(business_register_number)
- `Nemtschok Touristik`(organisation)
- `Wilnorlex Werke gmbH`(organisation)
- `FN545761v`(business_register_number)

**Example 30** (doc_id: `deanon_TRAIN/1Ob16_20i`) (sent_id: `deanon_TRAIN/1Ob16_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Stadt Christina Schorer, vertreten durch die Benn-Ibler Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Donsteinlex AG, Natalie Gieseking, MSc, vertreten durch die Weber Rechtsanwälte GmbH & Co KG, Wien, wegen 312.706,88 EUR sowie Feststellung (Streitwert 80.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Oktober 2019, GZ 6 R 71/19g-17, mit dem das Urteil des Landesgerichts Steyr vom 29. März 2019, GZ 9 Cg 39/18g-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Stadt Christina Schorer` — partial — gold is substring of pred: `Christina Schorer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Christina Schorer`(person)
- `Donsteinlex AG`(organisation)
- `Natalie Gieseking, MSc`(person)

**Example 31** (doc_id: `deanon_TRAIN/1Ob171_22m`) (sent_id: `deanon_TRAIN/1Ob171_22m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Musger als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Leonie Dommke, vertreten durch Mag. Klaus Mayer, Rechtsanwalt in Premstätten, gegen die beklagte Partei Grashuber+Kovatchev Immobilien Limited, Elisabeth Hallmanns, vertreten durch Dr. Fabian Maschke, Rechtsanwalt in Wien, wegen 36.070 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 3. August 2022, GZ 4 R 98/22x-24, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Leonie Dommke` — type mismatch — same span as gold: `Leonie Dommke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Leonie Dommke`(person)
- `Grashuber+Kovatchev Immobilien Limited`(organisation)
- `Elisabeth Hallmanns`(person)

**Example 32** (doc_id: `deanon_TRAIN/1Ob174_19y`) (sent_id: `deanon_TRAIN/1Ob174_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei KzlR Babette Maile, vertreten durch Dr. Hannes Paulweber, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Willibald Jonasius, vertreten durch die Heiss & Heiss Rechtsanwälte OG, Innsbruck, wegen 137.664,28 EUR sA sowie Feststellung (Streitwert 15.000 EUR), über die außerordentliche Revision der beklagten Partei gegen das (richtig) Teilzwischenurteil des Oberlandesgerichts Innsbruck vom 18. Juli 2019, GZ 1 R 76/19i-74, mit dem das Urteil des Landesgerichts Innsbruck vom 21. Februar 2019, GZ 8 Cg 119/16z-68, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `KzlR Babette Maile` — type mismatch — same span as gold: `KzlR Babette Maile`
- `Willibald Jonasius` — type mismatch — same span as gold: `Willibald Jonasius`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `KzlR Babette Maile`(person)
- `Willibald Jonasius`(person)

**Example 33** (doc_id: `deanon_TRAIN/1Ob178_19m`) (sent_id: `deanon_TRAIN/1Ob178_19m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Manfred Dietmayr, vertreten durch die Korn und Gärtner Rechtsanwälte OG, Salzburg, gegen die beklagte Partei Sakura Assmacher, MSc, vertreten durch die Ferner Hornung & Partner Rechtsanwälte GmbH, Salzburg, wegen Wiederaufnahme des Verfahrens AZ 17 C 1538/16p des Bezirksgerichts Salzburg, über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 12. Juni 2019, GZ 22 R 163/19b-7, mit dem der Beschluss des Bezirksgerichts Salzburg vom 25. Jänner 2019, GZ 17 C 80/19f-2, mit einer Maßgabe bestätigt wurde, den Beschluss gefasst:  Spruch Dem außerordentlichen Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Manfred Dietmayr` — type mismatch — same span as gold: `Manfred Dietmayr`
- `Sakura Assmacher` — partial — pred is substring of gold: `Sakura Assmacher, MSc`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Manfred Dietmayr`(person)
- `Sakura Assmacher, MSc`(person)

**Example 34** (doc_id: `deanon_TRAIN/1Ob184_15p`) (sent_id: `deanon_TRAIN/1Ob184_15p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tamara Schweinfurth, vertreten durch Dr. Wolfgang Maurer, Rechtsanwalt in Golling, gegen die beklagte Partei Noah Vlatten, BEd, vertreten durch Dr. Peter Perner, Rechtsanwalt in Salzburg, wegen 10.895,18 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 19. Mai 2015, GZ 22 R 126/15f-21, mit dem das Urteil des Bezirksgerichts Salzburg vom 5. März 2015, GZ 32 C 407/14x-17, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Tamara Schweinfurth` — type mismatch — same span as gold: `Tamara Schweinfurth`
- `Noah Vlatten` — partial — pred is substring of gold: `Noah Vlatten, BEd`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Tamara Schweinfurth`(person)
- `Noah Vlatten, BEd`(person)

**Example 35** (doc_id: `deanon_TRAIN/1Ob186_16h`) (sent_id: `deanon_TRAIN/1Ob186_16h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Anton Luehne, Deutschland, vertreten durch die Dr. Paul Kreuzberger, Mag. Markus Stranimaier & Mag. Manuel Vogler – Rechtsanwälte & Strafverteidiger OG, Bischofshofen, gegen die beklagten Parteien 1. OMedR Angelina Badenius und 2. Hon.-Prof. Miroslav Roelle, vertreten durch Dr. Raimund Danner, Rechtsanwalt in Salzburg, wegen 18.383,81 EUR sA und Feststellung (Streitwert 5.000 EUR), über die Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 11. August 2016, GZ 4 R 107/16g-45, mit dem das Teilzwischenurteil des Landesgerichts Salzburg vom 8. Juni 2016, GZ 5 Cg 125/14z-41, mit einer Maßgabe bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Anton Luehne` — type mismatch — same span as gold: `Anton Luehne`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Anton Luehne`(person)
- `OMedR Angelina Badenius`(person)
- `Hon.-Prof. Miroslav Roelle`(person)

**Example 36** (doc_id: `deanon_TRAIN/1Ob216_15v`) (sent_id: `deanon_TRAIN/1Ob216_15v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Ashley Meinering, vertreten durch Hon.-Prof. Dr. Michel Walter, Rechtsanwalt in Wien, gegen die beklagte Partei Walddon GmbH, Linn Voegelein, vertreten durch die Schlösser & Partner Rechtsanwälte OG, Graz, wegen 33.930 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 19. August 2015, GZ 13 R 74/15w-55, mit dem das Endurteil des Landesgerichts Korneuburg vom 26. Februar 2015, GZ 3 Cg 15/13h-50, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Ashley Meinering` — type mismatch — same span as gold: `Ashley Meinering`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ashley Meinering`(person)
- `Walddon GmbH`(organisation)
- `Linn Voegelein`(person)

**Example 37** (doc_id: `deanon_TRAIN/1Ob216_19z`) (sent_id: `deanon_TRAIN/1Ob216_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat des Obersten Gerichtshofs Mag. Wurzer als Vorsitzenden sowie die Hofräte und Hofrätinnen Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer, Dr. Parzmayr und Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Fabienne Arndsmeier, MMSc, Kassandra Orak, vertreten durch Dr. Michael Pallauf, LL.M., und andere, Rechtsanwälte in Salzburg, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 41.978,49 EUR sA sowie Feststellung (Streitwert 40.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. September 2019, GZ 14 R 75/19f-18, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 24. April 2019, GZ 33 Cg 26/18p-14, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Fabienne Arndsmeier` — type mismatch — same span as gold: `Fabienne Arndsmeier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fabienne Arndsmeier`(person)
- `Kassandra Orak`(person)

**Example 38** (doc_id: `deanon_TRAIN/1Ob221_17g`) (sent_id: `deanon_TRAIN/1Ob221_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und Hofrätinnen Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Boothe u. Sandmeier IT GmbH (früher OberTelekom GmbH), Ewaldgasse 28, 4084 Mitterberg, Österreich, vormals vertreten durch Dr. Wolfgang Poleschinski, Rechtsanwalt in Hartberg, gegen die beklagte Partei Yelec Dangelmeier, vertreten durch die Dr. Farhad Paya Rechtsanwalt GmbH, Klagenfurt am Wörthersee, wegen 7.583,60 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 24. August 2017, GZ 1 R 127/17x-69, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 28. März 2017, GZ 16 C 1333/14i-65, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

**False Positives:**

- `Yelec Dangelmeier` — type mismatch — same span as gold: `Yelec Dangelmeier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Boothe u. Sandmeier IT GmbH`(organisation)
- `OberTelekom GmbH`(organisation)
- `Ewaldgasse 28, 4084 Mitterberg, Österreich`(address)
- `Yelec Dangelmeier`(person)

**Example 39** (doc_id: `deanon_TRAIN/1Ob226_20x`) (sent_id: `deanon_TRAIN/1Ob226_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Ibrahim Gerlicher GmbH, Gabriel van Straaten, vertreten durch Dr. Martin Leitner und andere, Rechtsanwälte in Wien, gegen die beklagte Partei Stadt Olaf Doerrien, vertreten durch die Estermann Pock Rechtsanwälte GmbH, Wien, wegen 19.002,01 EUR, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 7. September 2020, GZ 14 R 61/20y-27, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 28. Jänner 2020, GZ 31 Cg 1/19y-22, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Ibrahim Gerlicher GmbH` — partial — gold is substring of pred: `Ibrahim Gerlicher`
- `Stadt Olaf Doerrien` — partial — gold is substring of pred: `Olaf Doerrien`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Ibrahim Gerlicher`(person)
- `Gabriel van Straaten`(person)
- `Olaf Doerrien`(person)

**Example 40** (doc_id: `deanon_TRAIN/1Ob234_19x`) (sent_id: `deanon_TRAIN/1Ob234_19x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr in der Rechtssache der gefährdeten Partei VetR RgR Janet Wichtler, vertreten durch die Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG, Wien, gegen die gefährdende Partei Charles Gutbrot, vertreten durch Dr. Alexander Haas, Rechtsanwalt in Seiersberg, wegen Erlassung einer einstweiligen Verfügung nach § 382 Z 8 lit c zweiter Fall EO, über den außerordentlichen Revisionsrekurs der gefährdenden Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 5. November 2019, GZ 1 R 191/19v-326, mit dem der Beschluss des Bezirksgerichts Fürstenfeld vom 24. Juli 2019, GZ 23 Fam 27/15p-297, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß den §§ 402 Abs 4, 78 EO iVm § 526 Abs 2 erster Satz ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `VetR RgR Janet Wichtler` — type mismatch — same span as gold: `VetR RgR Janet Wichtler`
- `Charles Gutbrot` — type mismatch — same span as gold: `Charles Gutbrot`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `VetR RgR Janet Wichtler`(person)
- `Charles Gutbrot`(person)

**Example 41** (doc_id: `deanon_TRAIN/1Ob53_25p`) (sent_id: `deanon_TRAIN/1Ob53_25p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Dr. Wurdinger als Vorsitzenden sowie die Hofrätin und die Hofräte Dr. Steger, Mag. Wessely-Kristöfel, Dr. Parzmayr und Dr. Vollmaier als weitere Richter in der Rechtssache der klagenden Partei Ariadne Ludger, vertreten durch die ANWALTGMBH Rinner Teuchtmann in Linz, gegen die beklagte Partei Ing. Siegbert Fräde, vertreten durch die Wintersberger Rechtsanwälte GmbH in Ried im Innkreis, wegen 200.500 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 30. Jänner 2025, GZ 1 R 2/25g-86, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Ariadne Ludger` — type mismatch — same span as gold: `Ariadne Ludger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ariadne Ludger`(person)
- `Ing. Siegbert Fräde`(person)

**Example 42** (doc_id: `deanon_TRAIN/1Ob57_16p`) (sent_id: `deanon_TRAIN/1Ob57_16p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der außerstreitigen Familienrechtssache der Antragstellerin und gefährdeten Partei Tatjana Skowroneck, vertreten durch Mag. Nikolaus Vasak, Rechtsanwalt in Wien, gegen den Antragsgegner und Gegner der gefährdeten Partei Emmerich Smolin, vertreten durch Dr. Josef Lindlbauer, Rechtsanwalt in Enns, wegen (einstweiligen) Unterhalts, über den Revisionsrekurs des Antragsgegners gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 17. September 2015, GZ 16 R 271/15i-77, mit dem der Beschluss des Bezirksgerichts Mödling vom 29. Juni 2015, GZ 2 Fam 68/14f-58, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Tatjana Skowroneck` — type mismatch — same span as gold: `Tatjana Skowroneck`
- `Emmerich Smolin` — type mismatch — same span as gold: `Emmerich Smolin`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Tatjana Skowroneck`(person)
- `Emmerich Smolin`(person)

**Example 43** (doc_id: `deanon_TRAIN/1Ob66_13g_1Ob67_13d_`) (sent_id: `deanon_TRAIN/1Ob66_13g_1Ob67_13d__3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohman, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Dr. James Oforiwah, gegen die beklagten Parteien 1.

**False Positives:**

- `Dr. James Oforiwah` — type mismatch — same span as gold: `Dr. James Oforiwah`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. James Oforiwah`(person)

**Example 44** (doc_id: `deanon_TRAIN/1Ob6_23y`) (sent_id: `deanon_TRAIN/1Ob6_23y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Musger als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Sebastian de Joncheere, vertreten durch die Peissl & Partner Rechtsanwälte OG in Köflach, gegen die beklagte Partei Hemma Ambrose, vertreten durch Dr. Peter Schaden und Mag. Werner Thurner, Rechtsanwälte in Graz, wegen 4.681,98 EUR sowie Feststellung (Streitwert 5.000 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 29. September 2020, GZ 1 R 98/22x-74, sowie über den Rekurs der klagenden Partei gegen den in dieses Urteil aufgenommenen Beschluss, mit dem der Rekurs der klagenden Partei gegen das Urteil des Bezirksgerichts Graz-West vom 19. Jänner 2022, GZ 2 C 444/18x-67, zurückgewiesen wurde, den Beschluss gefasst:  Spruch I. Dem Rekurs des Klägers wird nicht Folge gegeben.

**False Positives:**

- `Hemma Ambrose` — type mismatch — same span as gold: `Hemma Ambrose`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Sebastian de Joncheere`(person)
- `Hemma Ambrose`(person)

**Example 45** (doc_id: `deanon_TRAIN/1Ob7_20s`) (sent_id: `deanon_TRAIN/1Ob7_20s_5`)


Francois Klingsoehr, vertreten durch die Dr. Schartner Rechtsanwalt GmbH, Altenmarkt im Pongau, gegen die beklagte Partei Egon Lammprecht, vertreten durch Dr. Reinfried Eberl und andere Rechtsanwälte in Salzburg, wegen Wiederherstellung, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 20. November 2019, GZ 22 R 322/19k-13, mit dem das Urteil des Bezirksgerichts St. Johann im Pongau vom 12. September 2019, GZ 2 C 152/19t-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Entscheidungen der Vorinstanzen werden aus Anlass der Revision einschließlich des durchgeführten Verfahrens als nichtig aufgehoben.

**False Positives:**

- `Egon Lammprecht` — type mismatch — same span as gold: `Egon Lammprecht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Francois Klingsoehr`(person)
- `Egon Lammprecht`(person)

**Example 46** (doc_id: `deanon_TRAIN/1Ob84_13d`) (sent_id: `deanon_TRAIN/1Ob84_13d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der gefährdeten Partei Dr. Miklos Ostheim, vertreten durch Dr. Christoph Brandweiner und Dr. Gabriela Brandweiner-Reiter, Rechtsanwälte in Salzburg, gegen den Gegner der gefährdeten Partei Karim Markel DDr. Maximilian Damrau, vertreten durch Dr. Petra Patzelt, Rechtsanwältin in Salzburg, wegen Erlassung einer einstweiligen Verfügung, über den vom Gegner der gefährdeten Partei gestellten Antrag auf Wiedereinsetzung in den vorigen Stand gegen die Versäumung der Frist zur Erhebung eines außerordentlichen Revisionsrekurses gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 26. März 2013, GZ 21 R 359/12h-16, mit dem der Beschluss des Bezirksgerichts Salzburg vom 8. August 2012, GZ 20 C 11/12w-6, mit einer Maßgabe bestätigt wurde, den Beschluss gefasst:  Spruch Der Wiedereinsetzungsantrag wird zurückgewiesen.

**False Positives:**

- `Dr. Miklos Ostheim` — type mismatch — same span as gold: `Dr. Miklos Ostheim`
- `Karim Markel DDr. Maximilian Damrau` — partial — gold is substring of pred: `Karim Markel`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Miklos Ostheim`(person)
- `Karim Markel`(person)
- `DDr. Maximilian Damrau`(person)

**Example 47** (doc_id: `deanon_TRAIN/1Ob85_16f`) (sent_id: `deanon_TRAIN/1Ob85_16f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Emanuela Hagener, MSc, Deutschland, vertreten durch Dr. Günther Klepp und andere, Rechtsanwälte in Linz, gegen die beklagte Partei Dr. Kira Trillhaase, vertreten durch Mag. Dagmar Hoppstädter, Rechtsanwältin in Weißkirchen an der Traun, wegen 39.000 EUR und Vertragsaufhebung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 31. März 2016, GZ 4 R 169/15y-28, mit dem das Urteil des Landesgerichts Linz vom 19. August 2015, GZ 5 Cg 79/14h-24, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

**False Positives:**

- `Emanuela Hagener` — partial — pred is substring of gold: `Emanuela Hagener, MSc`
- `Dr. Kira Trillhaase` — type mismatch — same span as gold: `Dr. Kira Trillhaase`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Emanuela Hagener, MSc`(person)
- `Dr. Kira Trillhaase`(person)

**Example 48** (doc_id: `deanon_TRAIN/2Ob114_24i`) (sent_id: `deanon_TRAIN/2Ob114_24i_4`)


Sloboda, Dr. Thunhart, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Edith Wischnewsky, vertreten durch Metzler & Partner Rechtsanwälte GmbH in Linz, gegen die beklagte Partei KzlR Techn R Quirin Erler, vertreten durch Nenning & Tockner, Rechtsanwälte in Steyr, wegen Herstellung, Ausfolgung und Unterlassung über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Steyr als Berufungsgericht vom 21. Dezember 2023, GZ 1 R 116/23m-12, mit dem einer Berufung der beklagten Partei gegen das Urteil des Bezirksgerichts Kirchdorf an der Krems vom 26. Juli 2023, GZ 1 C 132/23y-7, Folge gegeben wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Edith Wischnewsky` — type mismatch — same span as gold: `Edith Wischnewsky`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Edith Wischnewsky`(person)
- `KzlR Techn R Quirin Erler`(person)

**Example 49** (doc_id: `deanon_TRAIN/2Ob159_18y`) (sent_id: `deanon_TRAIN/2Ob159_18y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden, den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé sowie die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Edgar Arnts, vertreten durch Dr. Heinrich Oppitz, Rechtsanwalt in Wels, wider die beklagten Parteien 1.

**False Positives:**

- `Edgar Arnts` — type mismatch — same span as gold: `Edgar Arnts`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Edgar Arnts`(person)

**Example 50** (doc_id: `deanon_TRAIN/2Ob162_23x`) (sent_id: `deanon_TRAIN/2Ob162_23x_4`)


Sloboda und Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Vivian Juenger, vertreten durch Lirk Spielbüchler Hirtzberger Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Tobias Gancarz, wegen Feststellung, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 18. Juli 2023, GZ 21 R 75/23k-7, mit dem der Beschluss des Bezirksgerichts St. Johann im Pongau vom 28. Februar 2023, GZ 305 C 9/23x-3, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Vivian Juenger` — type mismatch — same span as gold: `Vivian Juenger`
- `Tobias Gancarz` — type mismatch — same span as gold: `Tobias Gancarz`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Vivian Juenger`(person)
- `Tobias Gancarz`(person)

**Example 51** (doc_id: `deanon_TRAIN/2Ob180_21s`) (sent_id: `deanon_TRAIN/2Ob180_21s_4`)


Sloboda als weitere Richter in der Rechtssache der klagenden Partei Ing. Constanze Kronawitt, vertreten durch Dr. Alexander Bosio, Rechtsanwalt in Zell am See, gegen die beklagten Parteien 1. DDr. Leif Eralp, und 2. Lothar Schwänke, beide vertreten durch Kinberger-Schuberth-Fischer Rechtsanwälte-GmbH in Zell am See, wegen 21.376,95 EUR sA und Feststellung (Streitwert: 10.000 EUR), über die Revisionen der klagenden und der zweitbeklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 6. August 2021, GZ 53 R 110/21i-23, womit das Teil- und Teilzwischenurteil des Bezirksgerichts Zell am See vom 6. April 2021, GZ 18 C 892/20z-17, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revisionen der klagenden und der zweitbeklagten Partei werden zurückgewiesen.

**False Positives:**

- `Ing. Constanze Kronawitt` — type mismatch — same span as gold: `Ing. Constanze Kronawitt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Constanze Kronawitt`(person)
- `DDr. Leif Eralp`(person)
- `Lothar Schwänke`(person)

**Example 52** (doc_id: `deanon_TRAIN/2Ob182_24i`) (sent_id: `deanon_TRAIN/2Ob182_24i_4`)


Sloboda, Dr. Thunhart und Dr. Kikinger sowie die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden und gefährdeten Partei Theresa Ziebold, vertreten durch Mag. Mahmut Sahinol, Rechtsanwalt in Wien, gegen die beklagten Parteien und Gegner der gefährdeten Parteien 1.

**False Positives:**

- `Theresa Ziebold` — type mismatch — same span as gold: `Theresa Ziebold`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Theresa Ziebold`(person)

**Example 53** (doc_id: `deanon_TRAIN/2Ob193_23f`) (sent_id: `deanon_TRAIN/2Ob193_23f_5`)


Kff. Magdalena Münsterberg, vertreten durch Weber Rechtsanwälte GmbH & Co KG in Wien 1, gegen die beklagte Partei Gisela Ammenn, vertreten durch BEURLE Rechtsanwälte GmbH & Co KG in Linz, wegen Herausgabe (Streitwert 1.525.000 EUR), über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2023, GZ 2 R 87/23m-32, mit dem das Urteil des Landesgerichts Salzburg vom 5. April 2023, GZ 8 Cg 9/23a-22, aufgehoben wurde zu Recht erkannt:  Spruch

**False Positives:**

- `Gisela Ammenn` — type mismatch — same span as gold: `Gisela Ammenn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Gisela Ammenn`(person)

**Example 54** (doc_id: `deanon_TRAIN/2Ob194_24d`) (sent_id: `deanon_TRAIN/2Ob194_24d_4`)


Sloboda, Dr. Thunhart, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Rut Dolff, vertreten durch Gottgeisl Leinsmer Weber Rechtsanwälte GmbH in Wien, wider die beklagte Partei Samuel Nachtwei, Malta, vertreten durch Mag. Simon Wallner Rechtsanwalt GmbH in Wien, wegen 30.895 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 1. Oktober 2024, GZ 12 R 72/24g-21, den Beschluss gefasst:  Spruch I. Der Antrag auf Unterbrechung des Revisionsverfahrens bis zur Entscheidung des Europäischen Gerichtshofs zu C-683/24 wird abgewiesen.

**False Positives:**

- `Rut Dolff` — type mismatch — same span as gold: `Rut Dolff`
- `Samuel Nachtwei` — type mismatch — same span as gold: `Samuel Nachtwei`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Rut Dolff`(person)
- `Samuel Nachtwei`(person)

**Example 55** (doc_id: `deanon_TRAIN/2Ob256_12d`) (sent_id: `deanon_TRAIN/2Ob256_12d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Stallbauer Telekom Aktiengesellschaft, Poysdorfer Straße 5, 9341 Dobersberg, Österreich, vertreten durch Dr. Manfred Steininger, Rechtsanwalt in Wien, gegen die beklagte Partei DDr. Viktor Junkmanns, Bakk. iur., vertreten durch die ANWALTGMBH Rinner Teuchtmann in Linz, wegen 50.932,89 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2012, GZ 4 R 158/12a-20, womit das Urteil des Landesgerichts Linz vom 14. Juni 2012, GZ 5 Cg 119/11m-14, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `DDr. Viktor Junkmanns` — partial — pred is substring of gold: `DDr. Viktor Junkmanns, Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stallbauer Telekom Aktiengesellschaft`(organisation)
- `Poysdorfer Straße 5, 9341 Dobersberg, Österreich`(address)
- `DDr. Viktor Junkmanns, Bakk. iur.`(person)

**Example 56** (doc_id: `deanon_TRAIN/2Ob27_22t`) (sent_id: `deanon_TRAIN/2Ob27_22t_4`)


Sloboda und Dr. Kikinger als weitere Richter in der Rechtssache der klagenden Partei Mag. Dr. Rosamunde Wolfschmidt, vertreten durch Pfletschinger Renzl Rechtsanwaltspartnerschaft in Wien, gegen die beklagte Partei Mag. Wieland Engelmair, vertreten durch Mag. Dr. Ralf Heinrich Höfer, Rechtsanwalt in Wien, wegen 214.114,51 EUR sA und Rechnungslegung (Streitwert 50.000 EUR), über die Revision der beklagten Partei (Revisionsinteresse 131.423,61 EUR) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 19. November 2021, GZ 16 R 148/21h-59, mit welchem das Teilurteil des Landesgerichts für Zivilrechtssachen Wien vom 25. Juli 2021, GZ 6 Cg 26/19s-55, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Mag. Dr. Rosamunde Wolfschmidt` — partial — gold is substring of pred: `Dr. Rosamunde Wolfschmidt`
- `Mag. Wieland Engelmair` — type mismatch — same span as gold: `Mag. Wieland Engelmair`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Rosamunde Wolfschmidt`(person)
- `Mag. Wieland Engelmair`(person)

**Example 57** (doc_id: `deanon_TRAIN/2Ob28_14b`) (sent_id: `deanon_TRAIN/2Ob28_14b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Gerald Schantze, vertreten durch Dr. Karl-Heinz Götz und Dr. Rudolf Tobler jun., Rechtsanwälte in Neusiedl am See, gegen die beklagte Partei Simon Lukac, vertreten durch Dr. Peter Böck, Rechtsanwalt in Neusiedl am See, wegen 34.860,66 EUR sA, über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 14. November 2013, GZ 16 R 156/13y-12, womit das Urteil des Landesgerichts Eisenstadt vom 15. Mai 2013, GZ 27 Cg 17/13p-8, aufgehoben wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Gerald Schantze` — partial — gold is substring of pred: `Schantze`
- `Simon Lukac` — partial — gold is substring of pred: `Lukac`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Schantze`(person)
- `Lukac`(person)

**Example 58** (doc_id: `deanon_TRAIN/2Ob37_17f`) (sent_id: `deanon_TRAIN/2Ob37_17f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé und den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Florentin Uffenwasser, vertreten durch Dr. Armin Exner, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Stadtgemeinde Naomi Mertensmeyer, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, wegen 29.461,04 EUR sA und Feststellung (Streitwert 10.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse 22.377,04 EUR) gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 15. Dezember 2016, GZ 2 R 141/16a-47, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Florentin Uffenwasser` — type mismatch — same span as gold: `Florentin Uffenwasser`
- `Stadtgemeinde Naomi Mertensmeyer` — partial — gold is substring of pred: `Naomi Mertensmeyer`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Florentin Uffenwasser`(person)
- `Naomi Mertensmeyer`(person)

**Example 59** (doc_id: `deanon_TRAIN/2Ob60_15k`) (sent_id: `deanon_TRAIN/2Ob60_15k_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé und den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Ariadne Schmalfuhs, vertreten durch Dr. Ingrid Stöger und Dr. Roger Reyman, Rechtsanwälte in Salzburg, gegen die beklagte Partei DDr.in Lukas Goncharova, vertreten durch Mag. Paul Wolf, Rechtsanwalt in St. Veit/Glan, wegen 4.862,43 EUR sA und Feststellung (Streitwert 2.000 EUR), über den „Revisionsrekurs“ (richtig: Rekurs) der beklagten Partei gegen den Beschluss des Landesgerichts Klagenfurt als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 408/14p-60, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Klagenfurt vom 17. Oktober 2014, GZ 40 C 1129/12p-53, aufgehoben und dem Erstgericht die neuerliche Entscheidung nach Verfahrensergänzung aufgetragen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Ariadne Schmalfuhs` — type mismatch — same span as gold: `Ariadne Schmalfuhs`
- `DDr.in Lukas Goncharova` — type mismatch — same span as gold: `DDr.in Lukas Goncharova`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Ariadne Schmalfuhs`(person)
- `DDr.in Lukas Goncharova`(person)

**Example 60** (doc_id: `deanon_TRAIN/2Ob63_11w`) (sent_id: `deanon_TRAIN/2Ob63_11w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Thomas Papakonstantinou, vertreten durch Kinberger-Schuberth-Fischer Rechtsanwälte-GmbH in Zell am See, gegen die beklagten Parteien 1. Matthias Graafmann, und 2.

**False Positives:**

- `Thomas Papakonstantinou` — partial — gold is substring of pred: `Papakonstantinou`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Papakonstantinou`(person)
- `Graafmann`(person)

**Example 61** (doc_id: `deanon_TRAIN/2Ob67_24b`) (sent_id: `deanon_TRAIN/2Ob67_24b_4`)


Sloboda, Dr. Thunhart, Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Joachim Arcularius, MSc LLB, vertreten durch Mag. Mehmet Munar, Rechtsanwalt in Wien, wider die beklagten Parteien 1. Diethard Wencke, und 2. Lara Splettstößer, beide vertreten durch Rechtsanwaltspartnerschaft Kolarz – Augustin – Mayer in Stockerau, wegen zuletzt 14.950 EUR sA und Feststellung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 22. Jänner 2024, GZ 12 R 111/23s-57, mit dem einer Berufung der beklagten Parteien gegen das Urteil des Landesgerichts Korneuburg vom 24. Mai 2023, GZ 6 Cg 8/22i-45, teilweise Folge gegeben wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Joachim Arcularius` — partial — pred is substring of gold: `Joachim Arcularius, MSc LLB`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Joachim Arcularius, MSc LLB`(person)
- `Diethard Wencke`(person)
- `Lara Splettstößer`(person)

**Example 62** (doc_id: `deanon_TRAIN/2Ob71_23i`) (sent_id: `deanon_TRAIN/2Ob71_23i_4`)


Sloboda und Dr. Kikinger als weitere Richter in der Rechtssache der klagenden Partei Moses Malkomes, vertreten durch Klepp Nöbauer Hintringer Primetshofer Rechtsanwälte (GbR) in Linz, gegen die beklagte Partei Carmen Reinoldsmann, vertreten durch Dr. Christoph Arbeithuber, Rechtsanwalt in Linz, wegen 26.843,50 EUR sA und Feststellung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 27. Februar 2023, GZ 4 R 17/23g-28, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Moses Malkomes` — type mismatch — same span as gold: `Moses Malkomes`
- `Carmen Reinoldsmann` — type mismatch — same span as gold: `Carmen Reinoldsmann`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Moses Malkomes`(person)
- `Carmen Reinoldsmann`(person)

**Example 63** (doc_id: `deanon_TRAIN/2Ob73_15x`) (sent_id: `deanon_TRAIN/2Ob73_15x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden, die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé sowie den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Dragan Karp, vertreten durch Mag. Bernd Trappmaier, Rechtsanwalt in Korneuburg, gegen die beklagte Partei Marlene Diderichs, vertreten durch Mag. Claus Marchl, Rechtsanwalt in Wien, wegen 25.396,03 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 22. Jänner 2015, GZ 11 R 239/14v-26, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 30. September 2014, GZ 57 Cg 30/14x-22, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dragan Karp` — type mismatch — same span as gold: `Dragan Karp`
- `Marlene Diderichs` — type mismatch — same span as gold: `Marlene Diderichs`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dragan Karp`(person)
- `Marlene Diderichs`(person)

**Example 64** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden, die Hofräte Dr. Veith und Dr. Musger sowie die Hofrätinnen Dr. E. Solé und Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Luigi Neimeier, vertreten durch Rechtsanwälte Estermann & Partner OG in Mattighofen, gegen die beklagte Partei LNC KI Solutions GmbH, Kordelia Grauel, vertreten durch Dr. Herbert Harlander und Mag. Wolfgang Harlander, Rechtsanwälte in Salzburg, wegen 33.251,85 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. März 2015, GZ 2 R 1/15b-37, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Salzburg vom 23. Oktober 2014, GZ 4 Cg 27/13d-33, bestätigt wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Luigi Neimeier` — type mismatch — same span as gold: `Luigi Neimeier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Luigi Neimeier`(person)
- `LNC KI Solutions GmbH`(organisation)
- `Kordelia Grauel`(person)

**Example 65** (doc_id: `deanon_TRAIN/2Ob79_11y`) (sent_id: `deanon_TRAIN/2Ob79_11y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Angelika Ebendorff, vertreten durch Hengstschläger Lindner und Partner Rechtsanwälte GmbH in Linz, gegen die beklagte Partei Sabine Landgraff, vertreten durch Mag. Gerlach Bachinger, Rechtsanwalt in Traun, wegen 14.957,31 EUR sA und Feststellung (Streitinteresse: 7.500 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 15. März 2011, GZ 3 R 34/11g-24, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts Linz vom 22. Dezember 2010, GZ 1 Cg 210/09m-20, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Angelika Ebendorff` — partial — gold is substring of pred: `Ebendorff`
- `Sabine Landgraff` — partial — gold is substring of pred: `Landgraff`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Ebendorff`(person)
- `Landgraff`(person)

**Example 66** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei OMedR Eleonore Wunderling, 9020 Klagenfurt, vertreten durch Mag. Michael Hirm, Rechtsanwalt in Klagenfurt, sowie der Nebenintervenientin auf Seiten der klagenden Partei Fildhaut & Claeser Forschung AG, Amanda Deutschlender, vertreten durch Dr. Martin Wuelz, Rechtsanwalt in Innsbruck, gegen die beklagten Parteien 1.

**False Positives:**

- `OMedR Eleonore Wunderling` — type mismatch — same span as gold: `OMedR Eleonore Wunderling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OMedR Eleonore Wunderling`(person)
- `Fildhaut & Claeser Forschung AG`(organisation)
- `Amanda Deutschlender`(person)

**Example 67** (doc_id: `deanon_TRAIN/2Ob89_17b`) (sent_id: `deanon_TRAIN/2Ob89_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende, die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé sowie den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Aron Dawideit, vertreten durch Posch, Schausberger & Lutz Rechtsanwälte GmbH in Wels, gegen die beklagten Parteien 1. PhD Irvin Kindschuh, 2. Theodor Hermus, und 3.

**False Positives:**

- `Aron Dawideit` — type mismatch — same span as gold: `Aron Dawideit`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Aron Dawideit`(person)
- `PhD Irvin Kindschuh`(person)
- `Theodor Hermus`(person)

**Example 68** (doc_id: `deanon_TRAIN/2Ob91_22d`) (sent_id: `deanon_TRAIN/2Ob91_22d_4`)


Sloboda und Dr. Kikinger als weitere Richter in der Rechtssache der klagenden Partei Farina Dirker, vertreten durch Dr. Sven Rudolf Thorstensen, LL.M., Rechtsanwalt in Wien, gegen die beklagte Partei Lüttge Chemie Limited, René Luidthard, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 40.150,26 EUR sA, im Verfahren über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. Februar 2022, GZ 15 R 171/21h-33, den Beschluss gefasst:  Spruch Die Zurücknahme der Revision wird zur Kenntnis genommen.

**False Positives:**

- `Farina Dirker` — type mismatch — same span as gold: `Farina Dirker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Farina Dirker`(person)
- `Lüttge Chemie Limited`(organisation)
- `René Luidthard`(person)

**Example 69** (doc_id: `deanon_TRAIN/3Nc32_19i`) (sent_id: `deanon_TRAIN/3Nc32_19i_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie die Hofräte Dr. Roch und Priv.-Doz. Dr. Rassi als weitere Richter in der Rechtssache der betreibenden Partei Ingolf Domagalik, vertreten durch Dr. Marco Rovagnati, Rechtsanwalt in Innsbruck, wider die verpflichtete Partei Lee Peickert, Malta, wegen Erwirkung von Unterlassungen (§ 355 EO), infolge Vorlage nach § 28 JN, den Beschluss gefasst:  Spruch Die Bestimmung eines zuständigen Gerichts nach § 28 JN für die beabsichtigte Exekution wird abgelehnt.

**False Positives:**

- `Ingolf Domagalik` — type mismatch — same span as gold: `Ingolf Domagalik`
- `Lee Peickert` — type mismatch — same span as gold: `Lee Peickert`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Ingolf Domagalik`(person)
- `Lee Peickert`(person)

**Example 70** (doc_id: `deanon_TRAIN/3Nc39_24a`) (sent_id: `deanon_TRAIN/3Nc39_24a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn und die Hofrätin Dr. Kodek als weitere Richter in der Ordinationssache der betreibenden Partei Wendy Janacek, vertreten durch Dr. Florian Johann Ernst Knaipp, Rechtsanwalt in Wien, gegen die verpflichtete Partei Siege KI Limited, Edgar Dölle, wegen 47.126,91 EUR sA, über den Antrag auf Ordination nach § 28 JN, den Beschluss gefasst:  Spruch Für die Bewilligung und den Vollzug der von der betreibenden Partei beabsichtigten Rechteexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Wendy Janacek` — type mismatch — same span as gold: `Wendy Janacek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wendy Janacek`(person)
- `Siege KI Limited`(organisation)
- `Edgar Dölle`(person)

**Example 71** (doc_id: `deanon_TRAIN/3Ob108_18f`) (sent_id: `deanon_TRAIN/3Ob108_18f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Hofräte Dr. Roch und Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Dr. Lorena Arzet, vertreten durch Scherbaum Seebacher Rechtsanwälte GmbH in Graz, wider die beklagte Partei Priv.-Doz.in Rafaela Flamang, vertreten durch Dr. Destaller ua, Rechtsanwälte in Graz, wegen (eingeschränkt) Räumung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 23. Februar 2018, GZ 7 R 137/17v-19, mit dem das Urteil des Bezirksgerichts Graz-Ost vom 29. September 2017, GZ 213 C 131/16m-15, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Lorena Arzet` — type mismatch — same span as gold: `Dr. Lorena Arzet`
- `Priv.-Doz.in Rafaela Flamang` — type mismatch — same span as gold: `Priv.-Doz.in Rafaela Flamang`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Lorena Arzet`(person)
- `Priv.-Doz.in Rafaela Flamang`(person)

**Example 72** (doc_id: `deanon_TRAIN/3Ob116_23i_3Ob117_23m_`) (sent_id: `deanon_TRAIN/3Ob116_23i_3Ob117_23m__3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Exekutionssache der betreibenden Partei Gemeinde Florian Endrikat, vertreten durch Muhri & Werschitz Partnerschaft von Rechtsanwälten GmbH in Graz, gegen die verpflichtete Partei Pablo Kroiss, wegen 377,45 EUR sA, über den Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 20. Dezember 2022, GZ 4 R 257/22a-34, womit der Rekurs der verpflichteten Partei gegen den Beschluss des Bezirksgerichts Feldbach vom 20. September 2022, GZ 3 E 3781/21p-30, zurückgewiesen wurde, den Beschluss gefasst:  Spruch I.Der als Revisionsrekurs zu wertende „Einspruch“ des Verpflichteten wird zurückgewiesen.

**False Positives:**

- `Gemeinde Florian Endrikat` — partial — gold is substring of pred: `Florian Endrikat`
- `Pablo Kroiss` — type mismatch — same span as gold: `Pablo Kroiss`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Florian Endrikat`(person)
- `Pablo Kroiss`(person)

**Example 73** (doc_id: `deanon_TRAIN/3Ob128_10k`) (sent_id: `deanon_TRAIN/3Ob128_10k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie die Hofräte und Hofrätinnen Hon.-Prof. Dr. Sailer, Dr. Lovrek, Dr. Jensik und Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Nadja Spangler, vertreten durch Kinberger-Schuberth-Fischer Rechtsanwälte-GmbH in Zell am See, gegen die beklagte Partei Sascha Heckert, vertreten durch Dr. Andreas König, Dr. Andreas Ermacora und Dr. Barbara Lässer, Rechtsanwälte in Innsbruck, wegen 137.146,60 EUR sA und Feststellung (Gesamtstreitwert 157.146,60 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 31. März 2010, GZ 6 R 28/10w-44, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Salzburg vom 30. Oktober 2009, GZ 7 Cg 117/07b-40, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Nadja Spangler` — partial — gold is substring of pred: `Spangler`
- `Sascha Heckert` — type mismatch — same span as gold: `Sascha Heckert`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Spangler`(person)
- `Sascha Heckert`(person)

**Example 74** (doc_id: `deanon_TRAIN/3Ob12_11b`) (sent_id: `deanon_TRAIN/3Ob12_11b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Amber Zeunert, LLB, vertreten durch Hopmeier & Wagner Rechtsanwälte OG in Wien, gegen die beklagte Partei Peter Chrysander, vertreten durch Kaufmann & Thurnher Rechtsanwälte GmbH in Dornbirn, wegen Einwendungen gegen den Anspruch (§ 35 EO), über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts Feldkirch als Berufungsgericht vom 9. November 2010, GZ 3 R 354/10x-15, womit über Berufung der klagenden Partei das Urteil des Bezirksgerichts Bludenz vom 9. August 2010, GZ 4 C 516/10z-11, abgeändert wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Amber Zeunert` — partial — pred is substring of gold: `Amber Zeunert, LLB`
- `Peter Chrysander` — partial — gold is substring of pred: `Chrysander`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Amber Zeunert, LLB`(person)
- `Chrysander`(person)

**Example 75** (doc_id: `deanon_TRAIN/3Ob147_16p`) (sent_id: `deanon_TRAIN/3Ob147_16p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Jensik und Dr. Roch und die Hofrätin Dr. Kodek als weitere Richter in der Exekutionssache der betreibenden Partei Melissa Edtmeier, vertreten durch Mag. Ute Svinger, Rechtsanwältin in Wien, wider die verpflichtete Partei Estelle Gschwendberger, vertreten durch Dr. Helmut Krenn, Rechtsanwalt in Wien, wegen 100.000 EUR sA, über den Revisionsrekurs der betreibenden Partei gegen den Beschluss des Landesgerichts Korneuburg als Rekursgericht vom 24. Mai 2016, GZ 22 R 56/16i-18, mit dem der Beschluss des Bezirksgerichts Schwechat vom 22. März 2016, GZ 2 E 689/16x-4, in der Fassung des Berichtigungsbeschlusses vom 15. April 2016, GZ 2 E 689/16x-10, abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Melissa Edtmeier` — type mismatch — same span as gold: `Melissa Edtmeier`
- `Estelle Gschwendberger` — type mismatch — same span as gold: `Estelle Gschwendberger`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Melissa Edtmeier`(person)
- `Estelle Gschwendberger`(person)

**Example 76** (doc_id: `deanon_TRAIN/3Ob14_24s`) (sent_id: `deanon_TRAIN/3Ob14_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Exekutionssache der betreibenden Partei Daniela Sklenar SE, Kimberly Hurrelmeyer, vertreten durch Cerha Hempel Rechtsanwälte GmbH in Wien, gegen die verpflichtete Partei Staat Libyen, StR Violetta Stegemeyer, Libyen, vertreten durch Binder Grösswang Rechtsanwälte GmbH in Wien, wegen 10 Mio EUR sA, über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Oktober 2023, GZ 47 R 228/23m-107, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 78 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Daniela Sklenar SE` — partial — gold is substring of pred: `Daniela Sklenar`
- `Staat Libyen` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Daniela Sklenar`(person)
- `Kimberly Hurrelmeyer`(person)
- `StR Violetta Stegemeyer`(person)

**Example 77** (doc_id: `deanon_TRAIN/3Ob156_12f`) (sent_id: `deanon_TRAIN/3Ob156_12f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in den verbundenen Rechtssachen der klagenden Partei Severin Ilek, vertreten durch die Sachwalterin Mag. Roswitha Ferl-Pailer, Rechtsanwältin in Hartberg, gegen die beklagte Partei Dipl.

**False Positives:**

- `Severin Ilek` — type mismatch — same span as gold: `Severin Ilek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Severin Ilek`(person)

**Example 78** (doc_id: `deanon_TRAIN/3Ob17_20a`) (sent_id: `deanon_TRAIN/3Ob17_20a_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie die Hofräte Priv.-Doz. Dr. Rassi und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Exekutionssache betreibenden Partei Heizung Werkuni Aktiengesellschaft, P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich, vertreten durch Dr. Roland Grilc ua, Rechtsanwälte in Klagenfurt am Wörthersee, gegen die verpflichtete Partei Dorothea Eiken Bank, Peter Eitenmüller, vertreten durch Diwok Hermann Petsche Rechtsanwälte LLP Co KG in Wien, wegen 12.602.980,92 EUR sA, über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. November 2019, GZ 46 R 293/19g-18, mit dem der Beschluss des Bezirksgerichts Favoriten vom 17. April 2019, GZ 17 E 1298/19z-2, bestätigt wurde, den Beschluss gefasst:  Spruch I. Der Revisionsrekurs wird, soweit er sich gegen die Bestätigung der Exekutionsbewilligung richtet, als jedenfalls unzulässig zurückgewiesen.

**False Positives:**

- `Dorothea Eiken Bank` — partial — gold is substring of pred: `Dorothea Eiken`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Heizung Werkuni Aktiengesellschaft`(organisation)
- `P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich`(address)
- `Dorothea Eiken`(person)
- `Peter Eitenmüller`(person)

**Example 79** (doc_id: `deanon_TRAIN/3Ob185_22k`) (sent_id: `deanon_TRAIN/3Ob185_22k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn und die Hofrätinnen Dr. Weixelbraun-Mohr, Dr. Kodek und Mag. Wessely-Kristöfel als weitere Richter in der Exekutionssache der betreibenden Partei Dr. Brian Adamska, vertreten durch Dr. Martin Neuwirth, Dr. Alexander Neurauter, Rechtsanwälte in Wien, gegen die verpflichtete Partei Kelglanzver-Software GmbH, Egon Libert, vertreten durch Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH in Wien, wegen zwangsweiser Räumung, über den Revisionsrekurs der betreibenden Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 12. August 2022, GZ 40 R 104/22y-20, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 8. April 2022, GZ 49 E 11/22w-3, abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Dr. Brian Adamska` — type mismatch — same span as gold: `Dr. Brian Adamska`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Brian Adamska`(person)
- `Kelglanzver-Software GmbH`(organisation)
- `Egon Libert`(person)

**Example 80** (doc_id: `deanon_TRAIN/3Ob192_11y`) (sent_id: `deanon_TRAIN/3Ob192_11y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Dr. Bartholomäus Nijboer, vertreten durch Hochsteger, Perz, Wallner & Warga Rechtsanwälte in Hallein, gegen die beklagte Partei Hon.-Prof. Dirk Edlich, vertreten durch Mag. Johann Meisthuber, Rechtsanwalt in Salzburg, wegen Einwendungen gegen den Anspruch (§ 35 EO), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 26. August 2011, GZ 21 R 31/11x-32, womit über Berufung der beklagten Partei das Urteil des Bezirksgerichts Salzburg vom 25. November 2010, GZ 31 C 86/09a-24, abgeändert wurde, den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

**False Positives:**

- `Hon.-Prof. Dirk Edlich` — type mismatch — same span as gold: `Hon.-Prof. Dirk Edlich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Bartholomäus Nijboer`(person)
- `Hon.-Prof. Dirk Edlich`(person)

**Example 81** (doc_id: `deanon_TRAIN/3Ob204_13s`) (sent_id: `deanon_TRAIN/3Ob204_13s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Univ.-Prof. DDr. Aurelia Wichera, vertreten durch Dr. Petra Patzelt, Rechtsanwältin in Salzburg, gegen die beklagte Partei Dr. Otto Furtwängler, wegen 62.769,86 EUR sA, über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz vom 28. August 2013, GZ 4 Nc 18/13b-3, mit welchem der Delegierungsantrag der klagenden Partei abgewiesen wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Univ.-Prof. DDr. Aurelia Wichera` — partial — gold is substring of pred: `DDr. Aurelia Wichera`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DDr. Aurelia Wichera`(person)
- `Dr. Otto Furtwängler`(person)

**Example 82** (doc_id: `deanon_TRAIN/3Ob204_19z`) (sent_id: `deanon_TRAIN/3Ob204_19z_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Roch als Vorsitzenden sowie die Hofräte Priv.-Doz. Dr. Rassi und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Exekutionssache der betreibenden Partei Dr. Karsten Elsayed, vertreten durch Dr. Hartmut Ramsauer, Rechtsanwalt in Salzburg, gegen die verpflichtete Partei DDr. Valentin Schwand, vertreten durch Lansky, Ganzger & Partner Rechtsanwälte GmbH in Wien, wegen Exekution nach § 354 EO, über den Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 12. September 2019, GZ 53 R 172/19d-165, womit der Beschluss des Bezirksgerichts Salzburg vom 24. Juni 2019, GZ 6 E 1184/18g-124, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Dr. Karsten Elsayed` — type mismatch — same span as gold: `Dr. Karsten Elsayed`
- `DDr. Valentin Schwand` — type mismatch — same span as gold: `DDr. Valentin Schwand`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Karsten Elsayed`(person)
- `DDr. Valentin Schwand`(person)

</details>

---

## `German Legal Organisation AG`

**F1:** 0.043 | **Precision:** 0.085 | **Recall:** 0.029  

**Format:** `regex`  
**Description:**
Matches German company names ending in AG (Aktiengesellschaft), handling hyphens and spaces in the name part. Tightened to exclude 'Partei' and 'Antragsgegnerin' prefixes.

**Content:**
```
(?<!\w)([A-Z][A-Za-z0-9\-\s&+\.]+(?:\s+[A-Z][A-Za-z0-9\-\s&+\.]+)*\s+AG)(?!\s+der\s+AG|\s+Partei|\s+Antragsgegnerin|\s+Antragstellerin)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.085 | 0.029 | 0.043 | 117 | 10 | 107 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 10 | 107 | 333 |

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

**Example 1** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_117`)


Außerdem wird die Valwalduni-Handel AG eine Gegenüberstellung über die von der Änderung betroffenen Bestimmungen sowie die vollständige Fassung der neuen Bedingungen auf ihrer Internetseite veröffentlichen und die Gegenüberstellung dem Kunden auf sein Verlangen zur Verfügung stellen;

| Predicted | Gold |
|---|---|
| `Valwalduni-Handel AG` | `Valwalduni-Handel AG` |

**Example 2** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_118`)


auch darauf wird die Landwerlin&Plumke Versand AG in derMitteilung hinweisen.

| Predicted | Gold |
|---|---|
| `Landwerlin&Plumke Versand AG` | `Landwerlin&Plumke Versand AG` |

**Example 3** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_12`)


Unkenntnis des Disziplinarbeschuldigten von den Gründen der Daten Unizorstein AG für die beantragte Fortsetzung der Zwangsversteigerungsverfahren;

| Predicted | Gold |
|---|---|
| `Daten Unizorstein AG` | `Daten Unizorstein AG` |

**Example 4** (doc_id: `deanon_TRAIN/2Ob63_11w`) (sent_id: `deanon_TRAIN/2Ob63_11w_4`)


Holz Seewald AG, Kaiserbrunnengasse 6, 5122 Lindach, Österreich, beide vertreten durch Dr. Leopold Hirsch, Rechtsanwalt in Salzburg, wegen 38.967,48 EUR sA und Feststellung (Streitinteresse 20.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 10. Februar 2011, GZ 4 R 206/10g-29, womit das Urteil des Landesgerichts Salzburg vom 17. August 2010, GZ 7 Cg 49/09f-25, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Holz Seewald AG` | `Holz Seewald AG` |

**Missed by this rule (FN):**

- `Kaiserbrunnengasse 6, 5122 Lindach, Österreich` (address)

**Example 5** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_5`)


RheinPharma Services AG, Unterhillinglah 5, 9853 Dornbach, Österreich, vertreten durch Dr. Harald Burmann und andere Rechtsanwälte in Innsbruck, und 3.

| Predicted | Gold |
|---|---|
| `RheinPharma Services AG` | `RheinPharma Services AG` |

**Missed by this rule (FN):**

- `Unterhillinglah 5, 9853 Dornbach, Österreich` (address)

**Example 6** (doc_id: `deanon_TRAIN/4Nc4_17a`) (sent_id: `deanon_TRAIN/4Nc4_17a_4`)


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

**Example 7** (doc_id: `deanon_TRAIN/4Ob9_20g`) (sent_id: `deanon_TRAIN/4Ob9_20g_4`)


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

- `Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG` — partial — gold is substring of pred: `Skrzypczik + Duchscherer Digital AG`

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

**Example 3** (doc_id: `deanon_TRAIN/10Ob31_16f`) (sent_id: `deanon_TRAIN/10Ob31_16f_24`)


DasBerufungsgerichtgab der Berufung der beklagten Partei nur insoweit Folge, als die Leistungsfrist mit vier (statt mit drei) Monaten festgesetzt wurde, und ließ die Revision mit der Begründung zu, dass es an höchstgerichtlicher Rechtsprechung zur Auslegung der hier beanstandeten AGB-Klauseln fehle.

**False Positives:**

- `Rechtsprechung zur Auslegung der hier beanstandeten AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Ob31_16f`) (sent_id: `deanon_TRAIN/10Ob31_16f_37`)


Ein Verweis auf die in den AGB der beklagten Partei enthaltene Definition des Begriffs „Terminsverlust“ hätte genügt, ohne dass die Gefahr gegeben gewesen wäre, dass die Kommunikationsfähigkeit der gesamten Branche zum Erliegen komme.

**False Positives:**

- `Ein Verweis auf die in den AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/10Ob31_16f`) (sent_id: `deanon_TRAIN/10Ob31_16f_52`)


Den Revisionsausführungen ist Folgendes entgegenzuhalten: 1.7.1 Nach § 6 Abs 3 KSchG ist eine in AGB oder Vertragsformblättern enthaltene Vertragsbestimmung unwirksam, wenn sie unklar oder unverständlich abgefasst ist.

**False Positives:**

- `Abs 3 KSchG ist eine in AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/10Ob31_16f`) (sent_id: `deanon_TRAIN/10Ob31_16f_92`)


2.5.3 Der Oberste Gerichtshof hatte bereits mehrfach Klauseln in den AGB einer Bank unter dem Gesichtspunkt des § 6 Abs 2 Z 1 KSchG zu beurteilen, mit denen sich die Bank das Recht zur Fälligstellung von Krediten einräumen ließ.

**False Positives:**

- `Der Oberste Gerichtshof hatte bereits mehrfach Klauseln in den AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/10Ob33_15y`) (sent_id: `deanon_TRAIN/10Ob33_15y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Inn Sudconkraft AG, Elisabeth Breitschwerdt, vertreten durch Poinstingl & Partner Rechtsanwälte OG in Wien, gegen die beklagte Partei Mazik Heizung GmbH, Hemma Rahn, vertreten durch Mag. Johannes Bügler, Rechtsanwalt in Wien, wegen 17.273,39 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 30. Jänner 2015, GZ 2 R 227/14p-70, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts Wiener Neustadt vom 7. Oktober 2014, GZ 24 Cg 232/10y-66, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Inn Sudconkraft AG` — partial — gold is substring of pred: `Inn Sudconkraft AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Sudconkraft AG`(organisation)
- `Elisabeth Breitschwerdt`(person)
- `Mazik Heizung GmbH`(organisation)
- `Hemma Rahn`(person)

**Example 8** (doc_id: `deanon_TRAIN/1Ob106_20z`) (sent_id: `deanon_TRAIN/1Ob106_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Kodek, Mag. Wurzer, Mag. Dr. Wurdinger und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei IGK Bau Consulting AG, Ariadne Seebalt, vertreten durch Dr. Manfred Angerer und andere Rechtsanwälte in Klagenfurt am Wörthersee, gegen die beklagte Partei DI Roxana Pöll, vertreten durch Mag. Claudia Egarter, Rechtsanwältin in Klagenfurt am Wörthersee, wegen 5.457.559,15 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 28. Februar 2020, GZ 2 R 9/20s-150, mit dem das Urteil des Landesgerichts Klagenfurt vom 20. Februar 2017, GZ 21 Cg 24/13h-102, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mag. Dr. Wurdinger und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei IGK Bau Consulting AG` — partial — gold is substring of pred: `IGK Bau Consulting AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `IGK Bau Consulting AG`(organisation)
- `Ariadne Seebalt`(person)
- `DI Roxana Pöll`(person)

**Example 9** (doc_id: `deanon_TRAIN/1Ob16_20i`) (sent_id: `deanon_TRAIN/1Ob16_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Stadt Christina Schorer, vertreten durch die Benn-Ibler Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Donsteinlex AG, Natalie Gieseking, MSc, vertreten durch die Weber Rechtsanwälte GmbH & Co KG, Wien, wegen 312.706,88 EUR sowie Feststellung (Streitwert 80.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. Oktober 2019, GZ 6 R 71/19g-17, mit dem das Urteil des Landesgerichts Steyr vom 29. März 2019, GZ 9 Cg 39/18g-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Donsteinlex AG` — partial — gold is substring of pred: `Donsteinlex AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Christina Schorer`(person)
- `Donsteinlex AG`(organisation)
- `Natalie Gieseking, MSc`(person)

**Example 10** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Dr. Wurdinger als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Steger, Mag. Wessely-Kristöfel, Dr. Parzmayr und Dr. Pfurtscheller als weitere Richterinnen und Richter in der Rechtssache der klagenden Partei Bundeskammer für Arbeiter und Angestellte, Wien 4, Prinz-Eugen-Straße 20–22, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Alsynwald-Recycling AG, RgR Mag. Dr. Evelyn Steinkröger, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH in Wien, wegen Unterlassung und Urteilsveröffentlichung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. Juli 2024, GZ 2 R 77/24v-15, mit dem das Urteil des Handelsgerichts Wien vom 28. Februar 2024, GZ 57 Cg 36/23d-8, bestätigt wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Alsynwald-Recycling AG` — partial — gold is substring of pred: `Alsynwald-Recycling AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alsynwald-Recycling AG`(organisation)
- `RgR Mag. Dr. Evelyn Steinkröger`(person)

**Example 11** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_33`)


[14]2.Eine in AGB oder Vertragsformblättern enthaltene Vertragsbestimmung, die nicht eine der beiderseitigen Hauptleistungen festlegt, ist nach § 879 Abs 3 ABGB nichtig, wenn sie unter Berücksichtigung aller Umstände des Falls einen Teil gröblich benachteiligt.

**False Positives:**

- `Eine in AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_43`)


[17]3.Nach § 6 Abs 3 KSchG ist eine in AGB oder Vertragsformblättern enthaltene Vertragsbestimmung unwirksam, wenn sie unklar oder unverständlich abgefasst ist.

**False Positives:**

- `Abs 3 KSchG ist eine in AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_57`)


Das der Klausel vom Verwender der AGB beigelegte Verständnis ist im Verbandsprozess nicht maßgeblich (RS0016590 [T23]).

**False Positives:**

- `Das der Klausel vom Verwender der AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_79`)


[32] So muss nach der Rechtsprechung des Obersten Gerichtshofs eine Zustimmungsfiktion in AGB nicht nur den formalen Voraussetzungen des § 6 Abs 1 Z 2 KSchG entsprechen, sondern auch einer Zulässigkeitsprüfung nach § 879 Abs 3 ABGB standhalten (1 Ob 210/12g [Punkt 2.15.] = RS0128865;

**False Positives:**

- `So muss nach der Rechtsprechung des Obersten Gerichtshofs eine Zustimmungsfiktion in AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_84`)


Vielmehr kann ein in AGB enthaltener Haftungsausschluss für leichte Fahrlässigkeit grob benachteiligend im Sinn des § 879 Abs 3 ABGB sein (ErläutRV 744 BlgNR 14.

**False Positives:**

- `Vielmehr kann ein in AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_90`)


Entgegen der Rechtsansicht der Beklagten kann daraus aber nicht der Umkehrschluss gezogen werden, dass Verzugszinsen in AGB, die den für den Fall der vertragsgemäßen Zahlung vereinbarten Sollzinssatz nicht um mehr als 5 % übersteigen, jedenfalls zulässig sind.

**False Positives:**

- `Verzugszinsen in AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_95`)


Wenngleich § 1333 Abs 1 ABGB dispositiv ist und für die Vereinbarung höherer als 4%iger vertraglicher Verzugszinsen in AGB in der Rechtsprechung mitunter kein schuldhafter Verzug gefordert wird (vgl 10 Ob 14/18h [Punkt 2.4.1]), handelt es sich nur bei den gesetzlichen Verzugszinsen in Höhe von 4 % um eine Mindestpauschale, die der Gläubiger unabhängig vom Nachweis eines konkreten Schadens verlangen kann (vgl RS0109502).

**False Positives:**

- `Verzugszinsen in AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_104`)


[40]2.3.Die Beklagte hält dem in derRevisionentgegen, die Klausel sei zulässig, weil die Bearbeitungsgebühr Teil der Hauptleistung sei, daher nicht der Kontrolle nach § 879 Abs 3 AGB unterliege und den Verbraucher ohnedies nicht gröblich benachteilige.

**False Positives:**

- `Abs 3 AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_115`)


3. Klausel 5: „2. Änderungen Z 2. (1) Änderungen dieser zwischen dem Kunden und dem Kreditinstitut vereinbarten Bedingungen gelten nach Ablauf von zwei Monaten ab Zugang der Mitteilung der angebotenen Änderungen an den Kunden als vereinbart, sofern bis dahin kein schriftlicher Widerspruch des Kunden bei der DFA Planung AG einlangt.

**False Positives:**

- `Widerspruch des Kunden bei der DFA Planung AG` — partial — gold is substring of pred: `DFA Planung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DFA Planung AG`(organisation)

**Example 20** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_116`)


Die Nieder Norber AG wird den Kunden in der Mitteilung auf die Änderungen hinweisen und darauf aufmerksam machen, dass sein Stillschweigen nach Ablauf der zwei Monate ab Zugang der Mitteilung durch das Unterlassen eines Widerspruchs in Schriftform als Zustimmung zu den Änderungen gilt.

**False Positives:**

- `Die Nieder Norber AG` — partial — gold is substring of pred: `Nieder Norber AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nieder Norber AG`(organisation)

**Example 21** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_141`)


Dies gilt vor allem dann, wenn die Klausel eine Änderung wesentlicher Pflichten der Parteien (Leistung und Gegenleistung) zu Gunsten des Verwenders der AGB in nahezu jede Richtung und in unbeschränktem Ausmaß zulässt (RS0128865).

**False Positives:**

- `Gunsten des Verwenders der AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_169`)


[55] Dass auch AGB-Änderungsklauseln, die Zustimmungsfiktionen enthalten, gesetzwidrig sein können, wenn die künftigen Änderungsmöglichkeiten nicht ausreichend bestimmt sind, entspricht der ständigen Rechtsprechung (vgl 5 Ob 160/15p [Punkt 2];

**False Positives:**

- `Dass auch AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_265`)


[88]8.5.In AGB enthaltene Entgeltklauseln, die ein Zusatzentgelt nicht zur Abgeltung einer nur aufgrund von Besonderheiten im Einzelfall erforderlichen Mehrleistung, sondern zur Abgeltung einer im Regelfall mit der Erfüllung der vertraglichen Pflichten verbundenen Leistung vorsehen, schränken das eigentliche Leistungsversprechen ein, verändern es oder höhlen es aus und unterliegen der Inhaltskontrolle nach § 879 Abs 3 ABGB (RS0016908 [T5, T6]).

**False Positives:**

- `In AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_267`)


Die Verrechnung von zusätzlichen Entgelten in AGB, denen keine konkreten Zusatzleistungen oder konkrete Kosten gegenüberstehen, die also bloß eine in die AGB „verschobene“ Entgeltverrechnung für ohnehin mit der Erfüllung der Hauptleistung üblicherweise verbundenen Aufwendungen darstellt, ist gröblich benachteiligend im Sinn des § 879 Abs 3 ABGB (vgl RS0123253 [T4, T6];

**False Positives:**

- `Entgelten in AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_TRAIN/1Ob226_20x`) (sent_id: `deanon_TRAIN/1Ob226_20x_54`)


C-620/17,Hochtief Solutions AG, Rn 35, jeweils mwN).

**False Positives:**

- `Hochtief Solutions AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_6`)


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

**Example 27** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_9`)


Die Besetzungsrüge (Z 1) zeigt zwar keine Tatsachengrundlage für die reklamierte Ausgeschlossenheit des Vorsitzenden des Disziplinarrats wegen Befangenheit (§ 43 Abs 1 Z 3 StPO iVm § 77 Abs 3 DSt) auf, weil aufgrund der Mitteilung des Genannten vom 5. Dezember 2014, wonach er keine Veranlassung sehe, seine „rechtsgeschäftlichen Kontakte“ dem Disziplinarbeschuldigten gegenüber offenzulegen, entgegen dem rein spekulativen Berufungsstandpunkt nicht „anzunehmen ist, dass ein berufsbedingtes Naheverhältnis“ des Vorsitzenden des Disziplinarrats zur Traun Lemalnor AG (Prozessgegnerin der vom Disziplinarbeschuldigten vertretenen Mandanten)“ besteht (vgl RIS-Justiz RS0125768, RS0097054).

**False Positives:**

- `Vorsitzenden des Disziplinarrats zur Traun Lemalnor AG` — partial — gold is substring of pred: `Traun Lemalnor AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Traun Lemalnor AG`(organisation)

**Example 28** (doc_id: `deanon_TRAIN/23Os1_15t`) (sent_id: `deanon_TRAIN/23Os1_15t_11`)


Denn die Beweisthemen (Geschäftsgrundlage der eingangs genannten Vereinbarung vom 11. Dezember 2012 mit der Süd-Immobilien AG; von derselben intendierte Verwertung der Liegenschaften in Draskovichgasse 12, 8240 Friedberg, Österreich durch Zwangsversteigerung ungeachtet eines allfälligen Abverkaufs von Liegenschaften in Steghof 15, 4891 Höhenwarth, Österreich ; Auftrag der Mandanten des Disziplinarbeschuldigten zur Zurückziehung des Antrags auf Aufhebung der Höfeeigenschaft;

**False Positives:**

- `Immobilien AG` — partial — pred is substring of gold: `Süd-Immobilien AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Süd-Immobilien AG`(organisation)
- `Draskovichgasse 12, 8240 Friedberg, Österreich`(address)
- `Steghof 15, 4891 Höhenwarth, Österreich`(address)

**Example 29** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei OMedR Eleonore Wunderling, 9020 Klagenfurt, vertreten durch Mag. Michael Hirm, Rechtsanwalt in Klagenfurt, sowie der Nebenintervenientin auf Seiten der klagenden Partei Fildhaut & Claeser Forschung AG, Amanda Deutschlender, vertreten durch Dr. Martin Wuelz, Rechtsanwalt in Innsbruck, gegen die beklagten Parteien 1.

**False Positives:**

- `Nebenintervenientin auf Seiten der klagenden Partei Fildhaut & Claeser Forschung AG` — partial — gold is substring of pred: `Fildhaut & Claeser Forschung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OMedR Eleonore Wunderling`(person)
- `Fildhaut & Claeser Forschung AG`(organisation)
- `Amanda Deutschlender`(person)

**Example 30** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_6`)


Glöckler Daten AG, Arbeiterstrandbadstraße 492, 8680 Pernreit, Österreich, vertreten durch Dr. Walter Heel, Rechtsanwalt in Innsbruck, wegen 62.404,99 EUR sA und Feststellung (Streitinteresse: 10.000 EUR), über die Revisionen der klagenden, der erstbeklagten und der zweitbeklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Jänner 2011, GZ 4 R 250/10m-85, womit infolge der Berufungen der klagenden, der erstbeklagten und der zweitbeklagten Partei das Urteil des Landesgerichts Innsbruck vom 25. August 2010, GZ 5 Cg 160/08w-74, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Sämtliche Revisionen werden zurückgewiesen.

**False Positives:**

- `Daten AG` — partial — pred is substring of gold: `Glöckler Daten AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Glöckler Daten AG`(organisation)
- `Arbeiterstrandbadstraße 492, 8680 Pernreit, Österreich`(address)

**Example 31** (doc_id: `deanon_TRAIN/3Ob164_20v`) (sent_id: `deanon_TRAIN/3Ob164_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Bruckgartver GmbH, MedR StR René Titz, vertreten durch Dr. Reinhard Schanda, Rechtsanwalt in Wien, gegen die beklagte Partei Ofczarczik Planung AG, Dipl.

**False Positives:**

- `Partei Ofczarczik Planung AG` — partial — gold is substring of pred: `Ofczarczik Planung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bruckgartver GmbH`(organisation)
- `MedR StR René Titz`(person)
- `Ofczarczik Planung AG`(organisation)

**Example 32** (doc_id: `deanon_TRAIN/3Ob215_19t`) (sent_id: `deanon_TRAIN/3Ob215_19t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie die Hofräte Dr. Roch und Priv.-Doz. Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Bartholomäus Kurth, vertreten durch die Torggler Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Traberval AG, Vera Lindenstruth, vertreten durch Dr. Manfred Angerer ua, Rechtsanwälte in Klagenfurt am Wörthersee, wegen 300.000 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 10. September 2019, GZ 5 R 68/19p-19, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Traberval AG` — partial — gold is substring of pred: `Traberval AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bartholomäus Kurth`(person)
- `Traberval AG`(organisation)
- `Vera Lindenstruth`(person)

**Example 33** (doc_id: `deanon_TRAIN/4Ob165_09g`) (sent_id: `deanon_TRAIN/4Ob165_09g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Schenk als Vorsitzende sowie die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Donostzor-Software AG, Florian Gretenkordt, vertreten durch Ewald Weninger Rechtsanwalts GmbH in Wien, gegen die beklagte Partei WienDigital Planung AG, KzlR Volker Chang, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Feststellung und Anfechtung (Streitwert: 101.000.000 EUR), im Verfahren über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Juni 2009, GZ 5 R 44/09s-15, womit das Urteil des Handelsgerichts Wien vom 26. Jänner 2008, GZ 19 Cg 98/08w-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Zurückziehung der außerordentlichen Revision der klagenden Partei dient zur Kenntnis.

**False Positives:**

- `Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Donostzor-Software AG` — partial — gold is substring of pred: `Donostzor-Software AG`
- `Partei WienDigital Planung AG` — partial — gold is substring of pred: `WienDigital Planung AG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Donostzor-Software AG`(organisation)
- `Florian Gretenkordt`(person)
- `WienDigital Planung AG`(organisation)
- `KzlR Volker Chang`(person)

**Example 34** (doc_id: `deanon_TRAIN/4Ob188_14x`) (sent_id: `deanon_TRAIN/4Ob188_14x_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Bachkelwerk Pflege AG, Eva Selcuk, vertreten durch Ebert Huber Swoboda Oswald & Partner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Christiane Rechenauer e.U., Dossenweg 6, 4924 Dundeck, Österreich, vertreten durch Dr. Patrick Ruth, Rechtsanwalt in Innsbruck, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 34.900 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz vom 5. August 2014, GZ 2 R 139/14w-13, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Bachkelwerk Pflege AG` — partial — gold is substring of pred: `Bachkelwerk Pflege AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bachkelwerk Pflege AG`(organisation)
- `Eva Selcuk`(person)
- `Christiane Rechenauer`(person)
- `Dossenweg 6, 4924 Dundeck, Österreich`(address)

**Example 35** (doc_id: `deanon_TRAIN/4Ob19_10p`) (sent_id: `deanon_TRAIN/4Ob19_10p_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Traun-Sanitär gesellschaft mbH,*****, vertreten durch Prof. Haslinger & Partner, Rechtsanwälte in Linz, gegen die beklagte Partei NWJ KI Dienstleistungen AG,*****, vertreten durch Rechtsanwälte Konrad & Schröttner OG in Graz, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 65.000 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 25. November 2009, GZ 6 R 169/09h-37, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei NWJ KI Dienstleistungen AG` — partial — gold is substring of pred: `NWJ KI Dienstleistungen AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Traun-Sanitär gesellschaft mbH`(organisation)
- `NWJ KI Dienstleistungen AG`(organisation)

**Example 36** (doc_id: `deanon_TRAIN/4Ob90_16p`) (sent_id: `deanon_TRAIN/4Ob90_16p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Vogel als Vorsitzenden und die Hofräte Dr. Jensik, Dr. Musger, Dr. Schwarzenbacher und Dr. Rassi als weitere Richter in der Rechtssache der klagenden Partei Lebensmittel Glanzconuni AG, Immanuel Gspan, vertreten durch Fellner Wratzfeld & Partner Rechtsanwälte GmbH in Wien, gegen die beklagten Parteien 1. Fridolin Braunhold, 2. Mag. Frauke Steinweg, und 3. DonauLexlogbruckPlanung GmbH, Felberbachstraße 4, 3631 Jungschlag, Österreich, alle vertreten durch Dr. Peter Zöchbauer, Rechtsanwalt in Wien, wegen Unterlassung (Streitwert 102.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Februar 2016, GZ 2 R 93/15h-25, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Schwarzenbacher und Dr. Rassi als weitere Richter in der Rechtssache der klagenden Partei Lebensmittel Glanzconuni AG` — partial — gold is substring of pred: `Lebensmittel Glanzconuni AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lebensmittel Glanzconuni AG`(organisation)
- `Immanuel Gspan`(person)
- `Fridolin Braunhold`(person)
- `Mag. Frauke Steinweg`(person)
- `DonauLexlogbruckPlanung GmbH`(organisation)
- `Felberbachstraße 4, 3631 Jungschlag, Österreich`(address)

**Example 37** (doc_id: `deanon_TRAIN/5Ob102_24x`) (sent_id: `deanon_TRAIN/5Ob102_24x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei OSR Wolfram Dag, MA, wider die beklagte Partei MLUD Pharma Planung AG, Leila Wildvang, Deutschland vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 13.607,40 EUR sA und Feststellung über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Ried im Innkreis als Berufungsgericht vom 13. März 2024, GZ 18 R 2/24k-29, mit dem das Urteil des Bezirksgerichts Schärding vom 6. November 2023, GZ 2 C 478/20g-24, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei MLUD Pharma Planung AG` — partial — gold is substring of pred: `MLUD Pharma Planung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OSR Wolfram Dag, MA`(person)
- `MLUD Pharma Planung AG`(organisation)
- `Leila Wildvang`(person)

**Example 38** (doc_id: `deanon_TRAIN/5Ob141_23f`) (sent_id: `deanon_TRAIN/5Ob141_23f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofräte Mag. Wurzer und Mag. Painsi, die Hofrätin Dr. Weixelbraun-Mohr und den Hofrat Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei OMedR Univ.-Prof.in Eugenia Breitenfelder, vertreten durch Poduschka Partner AnwaltsGmbH in Linz, gegen die beklagte Partei Werkfurtval-Lebensmittel AG, Meinrad Birkenmeyer, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 19.600 EUR sA über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 22. Mai 2023, GZ 12 R 6/23y-34, mit dem das Urteil des Landesgerichts Wels vom 11. Jänner 2023, GZ 8 Cg 29/20s-29, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Partei Werkfurtval-Lebensmittel AG` — partial — gold is substring of pred: `Werkfurtval-Lebensmittel AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OMedR Univ.-Prof.in Eugenia Breitenfelder`(person)
- `Werkfurtval-Lebensmittel AG`(organisation)
- `Meinrad Birkenmeyer`(person)

**Example 39** (doc_id: `deanon_TRAIN/5Ob141_23f`) (sent_id: `deanon_TRAIN/5Ob141_23f_17`)


Ende des Jahres 2018 schloss er sich der deutschen Musterfeststellungsklage gegen die Conkraftnor-Event AG an.

**False Positives:**

- `Ende des Jahres 2018 schloss er sich der deutschen Musterfeststellungsklage gegen die Conkraftnor-Event AG` — partial — gold is substring of pred: `Conkraftnor-Event AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Conkraftnor-Event AG`(organisation)

**Example 40** (doc_id: `deanon_TRAIN/6Ob10_22x`) (sent_id: `deanon_TRAIN/6Ob10_22x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Nowotny, Dr. Hofer-Zeni-Rennhofer, Dr. Faber und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Mozar und Kuebler Daten Versicherungs AG, Grindelstraße 99, 4723 Tal, Österreich, vertreten durch Musey Rechtsanwalt GmbH in Salzburg, gegen die beklagte Partei Maschinenbau Ostlogber GmbH, Richarda Vetterer, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 7.246.839 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 1. Dezember 2021, GZ 2 R 165/21d-49, womit das Teil- und Zwischenurteil des Landesgerichts Salzburg vom 6. September 2021, GZ 6 Cg 16/20m-45, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Faber und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Mozar und Kuebler Daten Versicherungs AG` — partial — gold is substring of pred: `Mozar und Kuebler Daten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mozar und Kuebler Daten`(organisation)
- `Grindelstraße 99, 4723 Tal, Österreich`(address)
- `Maschinenbau Ostlogber GmbH`(organisation)
- `Richarda Vetterer`(person)

**Example 41** (doc_id: `deanon_TRAIN/6Ob123_19k`) (sent_id: `deanon_TRAIN/6Ob123_19k_58`)


Dies ist hier mit Punkt 32 der AGB der Klägerin auch erfolgt.

**False Positives:**

- `Dies ist hier mit Punkt 32 der AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_TRAIN/6Ob123_19k`) (sent_id: `deanon_TRAIN/6Ob123_19k_75`)


Punkt 32 der AGB betrifft ja gerade den Netzzutritt, bis zu dessen Herstellung oder zumindest Abschluss einer verbindlichen Vereinbarung über die Herstellung nie ein Vertragsverhältnis bestehen wird;

**False Positives:**

- `Punkt 32 der AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_TRAIN/6Ob231_24z`) (sent_id: `deanon_TRAIN/6Ob231_24z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Hofer-Zeni-Rennhofer als Vorsitzende sowie die Hofrätinnen und Hofräte Hon.-Prof. Dr. Faber, Mag. Pertmayr, Dr. Weber und Mag. Nigl LL.M. als weitere Richter in der Rechtssache der klagenden Partei Ing. Egon Jurguttis, vertreten durch Poduschka Partner Anwaltsgesellschaft mbH in Linz, wider die beklagte Partei UnterFinanzen AG, Silvius Haagmans, Deutschland, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 9.600 EUR sA, im Verfahren über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Linz als Berufungsgericht vom 7. Oktober 2024, GZ 6 R 57/24b-31, womit das Urteil des Bezirksgerichts Traun vom 16. Februar 2024, GZ 2 C 198/23z-22, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei vom 9. Dezember 2025 auf Fortsetzung des Verfahrens wird abgewiesen.

**False Positives:**

- `Partei UnterFinanzen AG` — partial — gold is substring of pred: `UnterFinanzen AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Egon Jurguttis`(person)
- `UnterFinanzen AG`(organisation)
- `Silvius Haagmans`(person)

**Example 44** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_31`)


Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG wäre hinsichtlich § 14 Abs 3 FBG sachlich nicht gerechtfertigt.

**False Positives:**

- `Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_33`)


Diese Gesetzeslücke sei durch eine analoge Anwendung des § 14 Abs 3 FBG auf gemeinnützige Bauvereinigungen in sämtlichen möglichen Rechtsformen (also auch in der Rechtsform einer GmbH oder AG) anzuwenden.

**False Positives:**

- `Rechtsform einer GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_52`)


Auch wenn die Prüfpflichten des Revisionsverbands gemäß § 28 Abs 4 WGG die Genehmigungspflicht durch die Landesregierung beim Erwerb von Anteilen an Unternehmungen mit dem überwiegenden Geschäftszweck des (un-)mittelbaren Erwerbs/Haltens/Verwaltens von Anteilen an Bauvereinigungen nach § 10a WGG erfassten, sei nicht anzunehmen, der Gesetzgeber habe in § 14 Abs 3 FBG die Möglichkeit, gemeinnützige Bauvereinigungen auch in der Rechtsform der GmbH oder der AG zu betreiben, vergessen.

**False Positives:**

- `Bauvereinigungen auch in der Rechtsform der GmbH oder der AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_64`)


Eine Unterscheidung dahingehend, dass § 14 Abs 3 FBG dem Revisionsverband Parteistellung nur bei gemeinnützigen Bauvereinigungen in der Rechtsform einer Genossenschaft, nicht aber auch einer GmbH oder AG zuerkenne, wäre sachlich nicht gerechtfertigt.

**False Positives:**

- `GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_66`)


Die Bestimmung sei daher analog auch auf gemeinnützige Bauvereinigungen in der Rechtsform der GmbH oder AG anzuwenden.

**False Positives:**

- `Bauvereinigungen in der Rechtsform der GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_107`)


Wenn nun kraft ausdrücklicher gesetzlicher Vorschrift gemeinnützige Bauvereinigungen auch in den Rechtsformen einer GmbH oder AG erlaubt sind (§ 1 Abs 1 WGG) und gleichzeitig auch für diese die Pflicht statuiert wird, einem Revisionsverband anzugehören (§ 5 Abs 1 WGG), so ist auch für eine in der Rechtsform einer GmbH oder AG bestehende Bauvereinigung der Revisionsverband als „zuständig“ im Sinn von § 14 Abs 3 FBG und demgemäß insoweit als Amtspartei anzusehen.

**False Positives:**

- `Bauvereinigungen auch in den Rechtsformen einer GmbH oder AG` — no gold match — likely missing annotation
- `Rechtsform einer GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 50** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_111`)


Es muss daher davon ausgegangen werden, dass sowohl der Gesetzgeber des FBG als auch der mehrfache (Novellen-)Gesetzgeber des WGG die Zuständigkeit des Revisionsverbands für Bauvereinigungen in der Rechtsform einer GmbH oder AG übersehen hat.

**False Positives:**

- `Bauvereinigungen in der Rechtsform einer GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_112`)


Es liegt nach Ansicht des Senats daher insoweit eine durch Analogie zu füllende Gesetzeslücke dahingehend vor, dass der für eine gemeinnützige Bauvereinigung zuständige Revisionsverband auch dann Amtspartei im Sinne des § 14 Abs 3 FBG ist, wenn die Bauvereinigung nicht in der Rechtsform einer Erwerbs- und Wirtschaftsgenossenschaft, sondern einer GmbH oder AG besteht (in diesem Sinn auchSchwetz/Gahler, Wohnungsgemeinnützigkeit und Firmenbuch – Wechselwirkung und Spannungsbogen?

**False Positives:**

- `GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_TRAIN/6Ob36_20t`) (sent_id: `deanon_TRAIN/6Ob36_20t_140`)


Der EuGH teilte die von einigen Mitgliedstaaten (darunter auch Österreich) geäußerte Rechtsansicht, eine Befristung des Widerrufsrechts sei aus Gründen der Rechtssicherheit unerlässlich, nicht (EuGH C-481/99 [Georg und Helga Heininger/Bayerische Hypo- und Vereinsbank AG]).

**False Positives:**

- `Bayerische Hypo- und Vereinsbank AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_TRAIN/6Ob47_25t`) (sent_id: `deanon_TRAIN/6Ob47_25t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Hofer-Zeni-Rennhofer als Vorsitzende sowie die Hofrätinnen und Hofräte Dr. Faber, Mag. Pertmayr, Dr. Weber und Mag. Nigl LL.M. als weitere Richter in der Rechtssache der klagenden Partei Timothy Scheppan, vertreten durch Dr. Alexander Amann LL.M., Rechtsanwalt in Gamprin-Bendern, Liechtenstein, wider die beklagte Partei Nord-Luftfahrt AG, Niklas Kühlewind, Deutschland, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 71.888,75 EUR sA Zug um Zug gegen die Rückstellung eines Fahrzeugs, in eventu wegen 17.972,19 EUR sA und Feststellung, im Verfahren über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Jänner 2025, GZ 11 R 7/25t-63, den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Partei Nord-Luftfahrt AG` — partial — gold is substring of pred: `Nord-Luftfahrt AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Timothy Scheppan`(person)
- `Nord-Luftfahrt AG`(organisation)
- `Niklas Kühlewind`(person)

**Example 54** (doc_id: `deanon_TRAIN/6Ob51_21z`) (sent_id: `deanon_TRAIN/6Ob51_21z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Univ.-Prof. Dr. Kodek, Dr. Nowotny, Dr. Faber und Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei Mag. Frank Mahrhold, vertreten durch Dr. Wolfgang Haslinger, LL.M., Rechtsanwalt in Wien, gegen die beklagte Partei PKLA Textil Bank Verwilnex Betriebe AG, Valerie Kallweidt, vertreten durch Dr. Anton Ehm und Mag. Thomas Mödlagl, Rechtsanwälte in Wien, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Jänner 2021, GZ 3 R 63/20m-18, mit dem das Urteil des Handelsgerichts Wien vom 7. September 2020, GZ 56 Cg 9/20x-14, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revision wirdFolge gegeben.

**False Positives:**

- `Partei PKLA Textil Bank Verwilnex Betriebe AG` — partial — gold is substring of pred: `PKLA Textil`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Frank Mahrhold`(person)
- `PKLA Textil`(organisation)
- `Verwilnex Betriebe AG`(organisation)
- `Valerie Kallweidt`(person)

**Example 55** (doc_id: `deanon_TRAIN/6Ob51_21z`) (sent_id: `deanon_TRAIN/6Ob51_21z_64`)


[15]2.2.Die Beklagte beruft sich alternativ auf Z 75 ihrer AGB, aus der sie das Bestehen einer effektiven Fremdwährungsschuld in Schweizer Franken ableitet:„Fremdwährungskredite sind effektiv, das heißt in der Währung zurückzuzahlen, in der sie das Kreditinstitut gegeben hat.“ [16]

**False Positives:**

- `Die Beklagte beruft sich alternativ auf Z 75 ihrer AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_TRAIN/6Ob51_21z`) (sent_id: `deanon_TRAIN/6Ob51_21z_65`)


Der Kläger bestritt zwar in erster Instanz noch, dass die Parteien die Geltung der AGB der Beklagten vereinbart hätten, stellte dies aber in weiterer Folge in seiner Berufung außer Streit.

**False Positives:**

- `Parteien die Geltung der AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_TRAIN/6Ob51_21z`) (sent_id: `deanon_TRAIN/6Ob51_21z_69`)


[17]2.3.Der Beklagten ist zwar beizupflichten, dass der Oberste Gerichtshof Z 75 ihrer AGB in einem Verbandsprozess als„weder intransparent noch gröblich benachteiligend“bezeichnete (6 Ob 228/16x [Pkt 2.17.]).

**False Positives:**

- `Oberste Gerichtshof Z 75 ihrer AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_TRAIN/6Ob51_21z`) (sent_id: `deanon_TRAIN/6Ob51_21z_123`)


Z 75 der AGB der Beklagten spricht daher auch gegen eine (analoge) Anwendung der Norm.

**False Positives:**

- `Z 75 der AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_TRAIN/6Ob51_21z`) (sent_id: `deanon_TRAIN/6Ob51_21z_133`)


Der EuGH bestätigte, dass eine solche Umrechnungsregelung der Missbrauchskontrolle unterliegt (C-26/13,KáslerRn 25, 53, 59; vgl dazu auchGraf, Neue EuGH-E: Ausnahmsweise doch kein ersatzloser Wegfall nichtiger AGB-Klauseln?

**False Positives:**

- `Ausnahmsweise doch kein ersatzloser Wegfall nichtiger AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_67`)


Ein Widerspruch zu Punkt III.4. der AGB liege nicht vor, weil sich die Beklagte lediglich für den Fall des Scheiterns der Übermittlung per E-Mail die Wahl anderer Übermittlungsarten vorbehalte.

**False Positives:**

- `Ein Widerspruch zu Punkt III.4. der AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_100`)


es können vielmehr auch zwei unabhängige Regelungen in einem Punkt oder sogar in einem Satz der AGB enthalten sein.

**False Positives:**

- `Regelungen in einem Punkt oder sogar in einem Satz der AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_108`)


Die Bestimmung soll verhindern, dass der Unternehmer dem Verbraucher mündliche Zusagen macht, deren Gültigkeit er nachträglich unter Berufung auf eine Klausel in seinen AGB in Abrede stellt (RS0121954).

**False Positives:**

- `Berufung auf eine Klausel in seinen AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_131`)


Dient eine Klausel in AGB bloß der Aufklärung des Verbrauchers, ist sie grundsätzlich nur dann intransparent nach § 6 Abs 3 KSchG, wenn sie dabei dem Verbraucher ein unrichtiges Bild der Rechtslage vermittelt und geeignet ist, ihn von der Durchsetzung seiner Rechte abzuhalten (RS0121951 [T4] = 5 Ob 217/16x).

**False Positives:**

- `Dient eine Klausel in AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_152`)


Dadurch widerspreche die Klausel den rechtlichen Vorgaben zum Geltungsgrund von AGB und sei gröblich benachteiligend im Sinn des § 879 Abs 3 ABGB.

**False Positives:**

- `Dadurch widerspreche die Klausel den rechtlichen Vorgaben zum Geltungsgrund von AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_159`)


DieBeklagtehält dem entgegen, die Gültigkeitsdauer der Gutscheine werde vom jeweiligen Tourismusunternehmen festgelegt und sei ihren AGB deshalb zwangsläufig nicht zu entnehmen.

**False Positives:**

- `Gutscheine werde vom jeweiligen Tourismusunternehmen festgelegt und sei ihren AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_172`)


sie ist aber gemäß Punkt II.4. ihrer AGB gegenüber dem Erwerber verpflichtet, den Gutschein, in dem die Dienstleistung, die durch den Gutschein bezahlt werden kann, dokumentiert ist, zu übermitteln (Klausel 1).

**False Positives:**

- `Punkt II.4. ihrer AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_250`)


Der Verbraucher wird vielmehr auf eine Rechtsfolge seines Zahlungsverzugs hingewiesen, mit der er auch ohne die Aufnahme der beanstandeten Klausel in die AGB der Beklagten konfrontiert wäre;

**False Positives:**

- `Aufnahme der beanstandeten Klausel in die AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_286`)


Auch wenn der Adressat des Transparenzgebots nicht der Gesetzgeber, sondern ein mit Verbrauchern kontrahierender Unternehmer ist (4 Ob 58/18k), können an den Unternehmer, der zum Zweck der Aufklärung der Verbraucher die dispositive Rechtslage dem Gesetzeswortlaut entsprechend und im Gesamtzusammenhang seiner AGB in nicht irreführender Weise wiedergibt, keiner darüber hinausgehenden Anforderungen an die Textverständlichkeit gestellt werden.

**False Positives:**

- `Verbraucher die dispositive Rechtslage dem Gesetzeswortlaut entsprechend und im Gesamtzusammenhang seiner AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_428`)


Sie sei als von der Beklagten formulierter standardisierter Vertragstext als Klausel in AGB oder Vertragsformblättern zu qualifizieren;

**False Positives:**

- `Sie sei als von der Beklagten formulierter standardisierter Vertragstext als Klausel in AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_433`)


DieBeklagteentgegnete, die beanstandete Klausel sei nicht Bestandteil ihrer AGB, sondern sei Angeboten entnommen, für die ausschließlich der jeweilige Anbieter verantwortlich sei, ohne dass sie darauf Einfluss habe.

**False Positives:**

- `Klausel sei nicht Bestandteil ihrer AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_446`)


Daraus sei aber für die Beklagte nichts gewonnen, weil § 28 Abs 1 KSchG die Verwendung gesetz- oder sittenwidriger AGB deren Empfehlung oder Vorschreibung für den geschäftlichen Verkehr gleichstelle.

**False Positives:**

- `Abs 1 KSchG die Verwendung gesetz- oder sittenwidriger AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_449`)


Die Beklagte hält dem in ihrerRevisionentgegen, die beanstandete Klausel finde sich nicht in ihren AGB;

**False Positives:**

- `Klausel finde sich nicht in ihren AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_459`)


Verwender der AGB ist grundsätzlich nur derjenige, der Partei des Vertrags ist oder werden soll (RS0124305;ApathyinSchwimann/Kodek, Praxiskommentar4§ 28 KSchG Rz 6), nicht sein Stellvertreter, Gehilfe oder Organwalter (KrejciinRummel, ABGB³ §§ 28–30 KSchG Rz 19;EccherinKlang³ § 28 KSchG Rz 4) oder der bloße Abschlussmittler (Kühnberg, Die konsumentenschutzrechtliche Verbandsklage [2006] 78).

**False Positives:**

- `Verwender der AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_465`)


Zu 7 Ob 78/06f wurde eine Hausverwalterin als Verwenderin der dort strittigen AGB beurteilt, die Mietverträge zwar im Namen und auf Rechnung der Kunden schloss, für diese Verträge aber die von ihr selbst entwickelten Textbausteine verwendete, über Rechtsfragen im Zusammenhang mit Änderungswünschen selbst entschied, von den Vermietern zum Abschluss und zur Auflösung aller die Liegenschaft betreffenden Verträge, insbesondere von Mietverträgen bevollmächtigt war, und letztlich in fast allen Angelegenheiten selbständig entschied, sodass sie im Ergebnis den Mietern gegenüber wie der Vermieter auftrat.

**False Positives:**

- `Hausverwalterin als Verwenderin der dort strittigen AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_466`)


Aufgrund dieser umfassenden Verwalterstellung sowie aufgrund des Umstands, dass die von der Beklagten entworfenen Vertragsformblätter der (vermeintlichen) Erleichterung ihrer eigenen Verwaltungstätigkeit dienten, qualifizierte der Oberste Gerichtshof die Beklagte – obgleich sie nur Vertreterin der Vertragspartnerin war – ausnahmsweise als Verwenderin der AGB.

**False Positives:**

- `Verwenderin der AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_468`)


In der Entscheidung 8 Ob 110/08x wurde die Muttergesellschaft als Verwenderin der in den AGB der Tochtergesellschaft enthaltenen Klauseln angesehen, weil ihr aus den von der Tochtergesellschaft abgeschlossenen Verträgen die Rechte einer Vertragspartnerin zukamen und sie maßgeblich in die „Vertragsgestion“ eingebunden war.

**False Positives:**

- `Muttergesellschaft als Verwenderin der in den AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_470`)


Zu 10 Ob 28/14m wurde klargestellt, dass auch Inkassounternehmen als AGB-Verwender zu beurteilen sind, wenn sie zwar formal als Vertreter der Gläubiger handeln, dabei aber AGB oder Vertragsformblätter zum Abschluss von Vereinbarungen über die Einbringung der offenen Forderungen und der von ihnen beanspruchten Kosten und Gebühren sowie ihres Aufwandsersatzes verwenden.

**False Positives:**

- `Inkassounternehmen als AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_472`)


Der Oberste Gerichtshof befasste sich bereits mehrfach mit AGB, die dem Vertrieb von Gutscheinen für touristische Leistungen im Internet zugrunde gelegt wurden.

**False Positives:**

- `Der Oberste Gerichtshof befasste sich bereits mehrfach mit AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_487`)


Es liegt aber auch kein den Entscheidungen 7 Ob 78/06f und 10 Ob 28/14m vergleichbarer Sachverhalt vor, in dem der Vertreter des Vertragspartners selbst als AGB-Verwender zu qualifizieren wäre.

**False Positives:**

- `Vertreter des Vertragspartners selbst als AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_488`)


In den genannten Entscheidungen waren jeweils Fälle zu beurteilen, in denen der Vertreter offenkundig Einfluss auf den Inhalt der AGB des Vertretenen nehmen konnte und diese auch der Gestaltung seiner eigenen (Vertretungs-)Tätigkeit (als Hausverwalter oder Inkassobüro) dienten.

**False Positives:**

- `Vertreter offenkundig Einfluss auf den Inhalt der AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_501`)


Daraus kann die Passivlegitimation der Beklagten für den hier geltend gemachten Anspruch auf Unterlassung der Verwendung und des Sich-Berufens auf die AGB aber nicht abgeleitet werden.

**False Positives:**

- `Anspruch auf Unterlassung der Verwendung und des Sich-Berufens auf die AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_TRAIN/6Ob56_19g`) (sent_id: `deanon_TRAIN/6Ob56_19g_502`)


Der Empfehler unwirksamer AGB kann vielmehr nur verhalten werden, die Empfehlung zu unterlassen (vglWittinUlmer/Brandner/Hensen, AGB-Recht12§ 1 UklaG Rz 40).

**False Positives:**

- `Der Empfehler unwirksamer AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_TRAIN/7Nc6_13m`) (sent_id: `deanon_TRAIN/7Nc6_13m_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Huber als Vorsitzende und die Hofrätinnen und Hofräte Dr. Hoch, Dr. Kalivoda, Mag. Dr. Wurdinger und Mag. Malesich als weitere Richter in der Arbeitsrechtssache der klagenden Partei Dr. Norbert Overdick, vertreten durch Dr. Clemens Gärner, Rechtsanwalt in Wien, gegen die beklagte Partei Daten Lexunilog AG, Marlon Jerabeck, vertreten durch Dr. Helmut Engelbrecht und andere Rechtsanwälte in Wien, wegen 4.868,07 EUR sA und Feststellung, über die Befangenheitsanzeige des Hofrats des Obersten Gerichtshofs Dr. Richard Hargassner im Verfahren 9 ObA 29/13z den Beschluss gefasst:  Spruch Der Hofrat des Obersten Gerichtshofs Dr. Richard Hargassner ist ausgeschlossen.

**False Positives:**

- `Partei Daten Lexunilog AG` — partial — gold is substring of pred: `Daten Lexunilog AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Norbert Overdick`(person)
- `Daten Lexunilog AG`(organisation)
- `Marlon Jerabeck`(person)

**Example 84** (doc_id: `deanon_TRAIN/7Ob162_20d`) (sent_id: `deanon_TRAIN/7Ob162_20d_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei DDr.in Gisela Loy, vertreten durch Mag. Marco und Mag. Amelie Kunczicky, Rechtsanwälte in Mayrhofen, gegen die beklagte Partei Helferich & Zeitler Marine AG, Jessica Seebald, vertreten durch Mag. Thomas Anker und DI Mag. Nikolaus Gratl, Rechtsanwäte in Innsbruck, wegen Urkundeneinsicht, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 19. Juni 2020, GZ 4 R 55/20z-18, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Helferich & Zeitler Marine AG` — partial — gold is substring of pred: `Helferich & Zeitler Marine AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DDr.in Gisela Loy`(person)
- `Helferich & Zeitler Marine AG`(organisation)
- `Jessica Seebald`(person)

**Example 85** (doc_id: `deanon_TRAIN/7Ob165_23z`) (sent_id: `deanon_TRAIN/7Ob165_23z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und die Hofräte Mag. Dr. Wurdinger, Mag. Malesich, Dr. Weber und Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei Mag. Norbert Faulwasser, vertreten durch Mag. Alexandra Schwarz, Rechtsanwältin in Wien, gegen die beklagte Partei AlpenMaschinenbau AG, Sibylle von Wachtendonk, vertreten durch Dr. Günter Niebauer, Rechtsanwalt in Wien, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Juli 2023, GZ 3 R 74/23h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei AlpenMaschinenbau AG` — partial — gold is substring of pred: `AlpenMaschinenbau AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Norbert Faulwasser`(person)
- `AlpenMaschinenbau AG`(organisation)
- `Sibylle von Wachtendonk`(person)

**Example 86** (doc_id: `deanon_TRAIN/7Ob55_25a`) (sent_id: `deanon_TRAIN/7Ob55_25a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Malesich, Dr. Weber, Mag. Fitz und Mag. Jelinek als weitere Richter in der Rechtssache der klagenden Partei Laurin Tieltges, vertreten durch die Poduschka Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Guender Medien AG, Lothar Sax, vertreten durch die CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 6.090 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 13. Dezember 2024, GZ 2 R 125/24g-42, mit dem das Urteil des Bezirksgerichts Innsbruck vom 28. Mai 2024, GZ 26 C 450/20h-37, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei Guender Medien AG` — partial — gold is substring of pred: `Guender Medien AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Laurin Tieltges`(person)
- `Guender Medien AG`(organisation)
- `Lothar Sax`(person)

**Example 87** (doc_id: `deanon_TRAIN/7Ob85_15y`) (sent_id: `deanon_TRAIN/7Ob85_15y_4`)


Cynthia Martchenko AG, Schmidhuberstraße 73, 4792 Landertsberg, Österreich, vertreten durch Jank Weiler Operenyi Rechtsanwälte OG in Wien, 2. Reisch + Weißert Getränke AG und 3.

**False Positives:**

- `Cynthia Martchenko AG` — partial — gold is substring of pred: `Cynthia Martchenko`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Cynthia Martchenko`(person)
- `Schmidhuberstraße 73, 4792 Landertsberg, Österreich`(address)
- `Reisch + Weißert Getränke AG`(organisation)

**Example 88** (doc_id: `deanon_TRAIN/7Ob92_19h`) (sent_id: `deanon_TRAIN/7Ob92_19h_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Tosca Janetscheck, vertreten durch Dr. Herwig Ernst, Rechtsanwalt in Korneuburg, gegen die beklagte Partei Domingo + Sinner Robotik AG Liliana Böbe, vertreten durch Dr. Herbert Laimböck, Rechtsanwalt in Wien, wegen 521.151,28 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. April 2019, GZ 5 R 32/19s-29, womit das Urteil des Handelsgerichts Wien vom 14. Jänner 2019, GZ 10 Cg 70/17z-25, bestätigt wurde, beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Partei Domingo + Sinner Robotik AG` — partial — gold is substring of pred: `Domingo + Sinner Robotik AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tosca Janetscheck`(person)
- `Domingo + Sinner Robotik AG`(organisation)
- `Liliana Böbe`(person)

**Example 89** (doc_id: `deanon_TRAIN/7Ob94_20d`) (sent_id: `deanon_TRAIN/7Ob94_20d_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Mag. Bernhard Siegloch, vertreten durch Brand Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Aspleiter Forschung AG, Chen Karime, vertreten durch Dorda Rechtsanwälte GmbH in Wien, wegen 16.354,47 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 31. Jänner 2020, GZ 1 R 120/19b-21, womit das Urteil des Handelsgerichts Wien vom 22. Juli 2019, GZ 16 Cg 50/18d-9, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Partei Aspleiter Forschung AG` — partial — gold is substring of pred: `Aspleiter Forschung AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Bernhard Siegloch`(person)
- `Aspleiter Forschung AG`(organisation)
- `Chen Karime`(person)

**Example 90** (doc_id: `deanon_TRAIN/7Ob97_18t`) (sent_id: `deanon_TRAIN/7Ob97_18t_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Dr. Leila Werntz, vertreten durch Dr. Peter Gregorich, Rechtsanwalt in Wien, gegen die beklagte Partei Valber Solar AG, Alexander Lukoszek, vertreten durch Dr. Matthias Bacher, Rechtsanwalt in Wien, wegen 1.057.200 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. März 2018, GZ 1 R 160/17g-116, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Valber Solar AG` — partial — gold is substring of pred: `Valber Solar AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Leila Werntz`(person)
- `Valber Solar AG`(organisation)
- `Alexander Lukoszek`(person)

**Example 91** (doc_id: `deanon_TRAIN/8Ob11_11t`) (sent_id: `deanon_TRAIN/8Ob11_11t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner sowie die Hofräte Mag. Ziegelbauer und Dr. Brenn als weitere Richter in der Rechtssache der klagenden Partei, Guggeis Automotive Bank InnBildung Betriebe AG, Olga Wohlbrück-Gasse 5, 3482 Gösing am Wagram, Österreich, vertreten durch Dr. Mag. Günther Riess, Mag. Christine Schneider, Rechtsanwälte in Innsbruck, gegen die beklagte Partei Doris Froemmel, vertreten durch Czernich Hofstädter Guggenberger & Partner, Rechtsanwälte in Innsbruck, wegen 2.278.895,88 EUR sA, über die Rekurse beider Parteien gegen den Beschluss des Oberlandesgerichts Innsbruck als Berufungsgericht vom 11. Oktober 2010, GZ 4 R 168/10b-76, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Feldkirch vom 20. Mai 2010, GZ 6 Cg 71/08s-71, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch 1.

**False Positives:**

- `Guggeis Automotive Bank InnBildung Betriebe AG` — partial — gold is substring of pred: `Guggeis Automotive`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Guggeis Automotive`(organisation)
- `InnBildung Betriebe AG`(organisation)
- `Olga Wohlbrück-Gasse 5, 3482 Gösing am Wagram, Österreich`(address)
- `Doris Froemmel`(person)

</details>

---

## `German Legal Organisation GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches German company names ending in GmbH, including those with & Co KG suffixes. Tightened to exclude 'Partei' and 'Antragsgegnerin' prefixes.

**Content:**
```
(?<!\w)([A-Z][A-Za-z0-9\-\s&+\.]+(?:\s+[A-Z][A-Za-z0-9\-\s&+\.]+)*\s+GmbH(?:\s*&\s*Co\.?(?:\s*KG)?))(?!\s+Partei|\s+Antragsgegnerin|\s+Antragstellerin)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 12 | 0 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 12 | 315 |

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

**Example 3** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_5`)


Text Begründung: Der Kläger erwarb als Verbraucher im Juni 2003 über Vermittlung eines selbständigen Vermögensberaters Kommanditanteile an der Bestelmeyer+Keßelheim Software GmbH & Co KG im Nominale von 17.000 EUR zuzüglich 850 EUR Agio.

**False Positives:**

- `Software GmbH & Co KG` — positional overlap with gold: `Bestelmeyer+Keßelheim Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bestelmeyer+Keßelheim Software GmbH`(organisation)

**Example 4** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/1Ob197_18d`) (sent_id: `deanon_TRAIN/1Ob197_18d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Volze KI GmbH & Co KG, Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich, vertreten durch Dr. Klaus-Dieter Strobach und andere Rechtsanwälte, Grieskirchen, gegen die beklagte Partei Land Oberösterreich, Linz, Landhausplatz 1, vertreten durch Dr. Thomas J. A. Langer, LL.M., Rechtsanwalt in Linz, wegen 475.550,18 EUR sA, über die (außerordentliche) Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2018, GZ 4 R 56/18k-17, mit dem das Urteil des Landesgerichts Wels vom 1. März 2018, GZ 3 Cg 3/16z-13, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Volze KI GmbH & Co KG` — partial — gold is substring of pred: `Volze KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Volze KI GmbH`(organisation)
- `Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich`(address)

**Example 6** (doc_id: `deanon_TRAIN/3Ob209_21p`) (sent_id: `deanon_TRAIN/3Ob209_21p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Nexostlem GmbH & Co KG, Rehlackenweg 5G, 8451 Pernitsch, Österreich, vertreten durch DDr. Heinz Dietmar Schimanko, Rechtsanwalt in Wien, gegen die beklagte Partei RheinLandwirtschaft Vertrieb GmbH, Klaus Dissler, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH & Co KG in Wien, wegen 7.906,82 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 7. Juni 2021, GZ 38 R 66/21v-16, mit dem das Urteil des Bezirksgerichts Favoriten vom 19. Jänner 2021, GZ 3 C 503/20f-12, abgeändert wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Nexostlem GmbH & Co KG` — partial — gold is substring of pred: `Nexostlem GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nexostlem GmbH`(organisation)
- `Rehlackenweg 5G, 8451 Pernitsch, Österreich`(address)
- `RheinLandwirtschaft Vertrieb GmbH`(organisation)
- `Klaus Dissler`(person)

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

- `Antragsgegnerin Talgart-Chemie GmbH & Co KG` — partial — gold is substring of pred: `Talgart-Chemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Niels Mueter`(person)
- `Talgart-Chemie GmbH`(organisation)
- `Tiefe Gasse 5, 2061 Obritz, Österreich`(address)

**Example 9** (doc_id: `deanon_TRAIN/8Ob60_12z`) (sent_id: `deanon_TRAIN/8Ob60_12z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner sowie die Hofräte Mag. Ziegelbauer und Dr. Brenn als weitere Richter in der Rechtssache der klagenden Partei Arabella Witkopf, vertreten durch Mag. Renate Aigner, Rechtsanwältin in Kallham, gegen die beklagte Partei Abramczyk & Krollpfeifer Wind GmbH & Co KG, Pühra 22, 8010 Edelsbach bei Graz, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen (Revisionsinteresse) 10.000 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 15. März 2012, GZ 3 R 42/12k-38, womit das Urteil des Landesgerichts Linz vom 28. Dezember 2011, GZ 1 Cg 167/10i-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Partei Abramczyk & Krollpfeifer Wind GmbH & Co KG` — partial — gold is substring of pred: `Abramczyk & Krollpfeifer Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Arabella Witkopf`(person)
- `Abramczyk & Krollpfeifer Wind GmbH`(organisation)
- `Pühra 22, 8010 Edelsbach bei Graz, Österreich`(address)

**Example 10** (doc_id: `deanon_TRAIN/8ObA21_11p`) (sent_id: `deanon_TRAIN/8ObA21_11p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn sowie die fachkundigen Laienrichter Dr. Manfred Engelmann und Alfred Klair als weitere Richter in der Arbeitsrechtssache der klagenden Partei Wilost Garten Werke GmbH & Co OG, Heinickegasse 3x, 4984 Klingersberg, Österreich, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Ing. Waltraud Seckl, vertreten durch Dr. Friedrich Schubert, Rechtsanwalt in Wien, wegen 19.335,55 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 31. Jänner 2011, GZ 7 Ra 121/10f-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO iVm § 2 Abs 1 ASGG).

**False Positives:**

- `Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn sowie die fachkundigen Laienrichter Dr. Manfred Engelmann und Alfred Klair als weitere Richter in der Arbeitsrechtssache der klagenden Partei Wilost Garten Werke GmbH & Co` — partial — gold is substring of pred: `Wilost Garten Werke GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wilost Garten Werke GmbH`(organisation)
- `Heinickegasse 3x, 4984 Klingersberg, Österreich`(address)
- `Ing. Waltraud Seckl`(person)

**Example 11** (doc_id: `deanon_TRAIN/9Ob58_20z`) (sent_id: `deanon_TRAIN/9Ob58_20z_48`)


Nach den Feststellungen sollte sich der Kläger als Treugeber über die Beklagte an einer GmbH & Co KG beteiligen, welche wiederum bis zu 90 % der Anteile an einer Kapitalgesellschaft in den VAE erwerben sollte.

**False Positives:**

- `Beklagte an einer GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `German Legal Organisation Limited`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches English-style Limited entities which may appear in German legal texts. Tightened to exclude 'Partei' prefix.

**Content:**
```
(?<!\w)([A-Z][A-Za-z0-9\-\s&+\.]+(?:\s+[A-Z][A-Za-z0-9\-\s&+\.]+)*\s+Limited)(?!\s+Partei)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 6 | 0 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 6 | 318 |

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

- `Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Hamberg Marine Limited` — partial — gold is substring of pred: `Hamberg Marine Limited`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hamberg Marine Limited`(organisation)
- `Kapellergasse 9, 4925 Lungdorf, Österreich`(address)

**Example 3** (doc_id: `deanon_TRAIN/2Ob91_22d`) (sent_id: `deanon_TRAIN/2Ob91_22d_4`)


Sloboda und Dr. Kikinger als weitere Richter in der Rechtssache der klagenden Partei Farina Dirker, vertreten durch Dr. Sven Rudolf Thorstensen, LL.M., Rechtsanwalt in Wien, gegen die beklagte Partei Lüttge Chemie Limited, René Luidthard, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 40.150,26 EUR sA, im Verfahren über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. Februar 2022, GZ 15 R 171/21h-33, den Beschluss gefasst:  Spruch Die Zurücknahme der Revision wird zur Kenntnis genommen.

**False Positives:**

- `Chemie Limited` — partial — pred is substring of gold: `Lüttge Chemie Limited`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Farina Dirker`(person)
- `Lüttge Chemie Limited`(organisation)
- `René Luidthard`(person)

**Example 4** (doc_id: `deanon_TRAIN/3Nc39_24a`) (sent_id: `deanon_TRAIN/3Nc39_24a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn und die Hofrätin Dr. Kodek als weitere Richter in der Ordinationssache der betreibenden Partei Wendy Janacek, vertreten durch Dr. Florian Johann Ernst Knaipp, Rechtsanwalt in Wien, gegen die verpflichtete Partei Siege KI Limited, Edgar Dölle, wegen 47.126,91 EUR sA, über den Antrag auf Ordination nach § 28 JN, den Beschluss gefasst:  Spruch Für die Bewilligung und den Vollzug der von der betreibenden Partei beabsichtigten Rechteexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Partei Siege KI Limited` — partial — gold is substring of pred: `Siege KI Limited`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wendy Janacek`(person)
- `Siege KI Limited`(organisation)
- `Edgar Dölle`(person)

**Example 5** (doc_id: `deanon_TRAIN/8Ob31_24b`) (sent_id: `deanon_TRAIN/8Ob31_24b_4`)


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

## `German Legal Organisation e.U.`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Einzelunternehmer (e.U.) entities.

**Content:**
```
\b([A-Z][A-Za-z0-9\-\.]+(?:\s+[A-Z][A-Za-z0-9\-\.]+)*\s+e\.U\.)(?!\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 3 | 187 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/4Ob188_14x`) (sent_id: `deanon_TRAIN/4Ob188_14x_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Bachkelwerk Pflege AG, Eva Selcuk, vertreten durch Ebert Huber Swoboda Oswald & Partner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Christiane Rechenauer e.U., Dossenweg 6, 4924 Dundeck, Österreich, vertreten durch Dr. Patrick Ruth, Rechtsanwalt in Innsbruck, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 34.900 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz vom 5. August 2014, GZ 2 R 139/14w-13, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Christiane Rechenauer e.U.` — partial — gold is substring of pred: `Christiane Rechenauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bachkelwerk Pflege AG`(organisation)
- `Eva Selcuk`(person)
- `Christiane Rechenauer`(person)
- `Dossenweg 6, 4924 Dundeck, Österreich`(address)

**Example 1** (doc_id: `deanon_TRAIN/6Ob69_23z`) (sent_id: `deanon_TRAIN/6Ob69_23z_25`)


Johanna Pfeiffenschneider e.U.“ bezahlt wurden und welche Rechnungen noch offen sind.

**False Positives:**

- `Johanna Pfeiffenschneider e.U.` — partial — gold is substring of pred: `Johanna Pfeiffenschneider`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Johanna Pfeiffenschneider`(person)

**Example 2** (doc_id: `deanon_TRAIN/6Ob69_23z`) (sent_id: `deanon_TRAIN/6Ob69_23z_63`)


Auch wenn der Beklagte in der Berufungsbeantwortung eingeräumt hat, „Rechtsnachfolger des Einzelunternehmens Willem Ing. Florentine Rohne e.U.“ gewesen zu sein (was die Haftung des Beklagten für auf dem Unternehmen lastenden Verbindlichkeiten nach § 38 UGB, § 1409 ABGB begründen könnte), wird mit den Parteien die Grundlage dieser Rechtsnachfolge und einer daraus etwa folgenden Haftung zu erörtern sein.

**False Positives:**

- `Einzelunternehmens Willem Ing. Florentine Rohne e.U.` — partial — gold is substring of pred: `Willem`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Willem`(organisation)
- `Florentine Rohne`(person)

</details>

---

## `German Legal Organisation GmbH & Co KG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specifically targets the complex GmbH & Co KG structure.

**Content:**
```
(?<!\w)([A-Z][A-Za-z0-9\-\s&+\.]+(?:\s+[A-Z][A-Za-z0-9\-\s&+\.]+)*\s+GmbH\s*&\s*Co\.?\s*KG)(?!\s+Partei|\s+der|\s+des)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 11 | 0 | 11 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 11 | 315 |

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

**Example 3** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_5`)


Text Begründung: Der Kläger erwarb als Verbraucher im Juni 2003 über Vermittlung eines selbständigen Vermögensberaters Kommanditanteile an der Bestelmeyer+Keßelheim Software GmbH & Co KG im Nominale von 17.000 EUR zuzüglich 850 EUR Agio.

**False Positives:**

- `Software GmbH & Co KG` — positional overlap with gold: `Bestelmeyer+Keßelheim Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bestelmeyer+Keßelheim Software GmbH`(organisation)

**Example 4** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_6`)


Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG, die eine oder mehrere Immobilien erwirbt.

**False Positives:**

- `Bei dieser Veranlagung beteiligen sich die Anleger als Kommanditisten an einer GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/1Ob197_18d`) (sent_id: `deanon_TRAIN/1Ob197_18d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Volze KI GmbH & Co KG, Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich, vertreten durch Dr. Klaus-Dieter Strobach und andere Rechtsanwälte, Grieskirchen, gegen die beklagte Partei Land Oberösterreich, Linz, Landhausplatz 1, vertreten durch Dr. Thomas J. A. Langer, LL.M., Rechtsanwalt in Linz, wegen 475.550,18 EUR sA, über die (außerordentliche) Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. Juli 2018, GZ 4 R 56/18k-17, mit dem das Urteil des Landesgerichts Wels vom 1. März 2018, GZ 3 Cg 3/16z-13, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Volze KI GmbH & Co KG` — partial — gold is substring of pred: `Volze KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Volze KI GmbH`(organisation)
- `Ekkehard-Hauer-Straße 42, 3830 Hollenbach, Österreich`(address)

**Example 6** (doc_id: `deanon_TRAIN/3Ob209_21p`) (sent_id: `deanon_TRAIN/3Ob209_21p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Nexostlem GmbH & Co KG, Rehlackenweg 5G, 8451 Pernitsch, Österreich, vertreten durch DDr. Heinz Dietmar Schimanko, Rechtsanwalt in Wien, gegen die beklagte Partei RheinLandwirtschaft Vertrieb GmbH, Klaus Dissler, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH & Co KG in Wien, wegen 7.906,82 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 7. Juni 2021, GZ 38 R 66/21v-16, mit dem das Urteil des Bezirksgerichts Favoriten vom 19. Jänner 2021, GZ 3 C 503/20f-12, abgeändert wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Nexostlem GmbH & Co KG` — partial — gold is substring of pred: `Nexostlem GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nexostlem GmbH`(organisation)
- `Rehlackenweg 5G, 8451 Pernitsch, Österreich`(address)
- `RheinLandwirtschaft Vertrieb GmbH`(organisation)
- `Klaus Dissler`(person)

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

- `Antragsgegnerin Talgart-Chemie GmbH & Co KG` — partial — gold is substring of pred: `Talgart-Chemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Niels Mueter`(person)
- `Talgart-Chemie GmbH`(organisation)
- `Tiefe Gasse 5, 2061 Obritz, Österreich`(address)

**Example 9** (doc_id: `deanon_TRAIN/8Ob60_12z`) (sent_id: `deanon_TRAIN/8Ob60_12z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner sowie die Hofräte Mag. Ziegelbauer und Dr. Brenn als weitere Richter in der Rechtssache der klagenden Partei Arabella Witkopf, vertreten durch Mag. Renate Aigner, Rechtsanwältin in Kallham, gegen die beklagte Partei Abramczyk & Krollpfeifer Wind GmbH & Co KG, Pühra 22, 8010 Edelsbach bei Graz, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen (Revisionsinteresse) 10.000 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 15. März 2012, GZ 3 R 42/12k-38, womit das Urteil des Landesgerichts Linz vom 28. Dezember 2011, GZ 1 Cg 167/10i-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Partei Abramczyk & Krollpfeifer Wind GmbH & Co KG` — partial — gold is substring of pred: `Abramczyk & Krollpfeifer Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Arabella Witkopf`(person)
- `Abramczyk & Krollpfeifer Wind GmbH`(organisation)
- `Pühra 22, 8010 Edelsbach bei Graz, Österreich`(address)

**Example 10** (doc_id: `deanon_TRAIN/9Ob58_20z`) (sent_id: `deanon_TRAIN/9Ob58_20z_48`)


Nach den Feststellungen sollte sich der Kläger als Treugeber über die Beklagte an einer GmbH & Co KG beteiligen, welche wiederum bis zu 90 % der Anteile an einer Kapitalgesellschaft in den VAE erwerben sollte.

**False Positives:**

- `Beklagte an einer GmbH & Co KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `German Legal Organisation Aktiengesellschaft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the full word Aktiengesellschaft instead of just AG.

**Content:**
```
(?<!\w)([A-Z][A-Za-z0-9\-\s&+\.]+(?:\s+[A-Z][A-Za-z0-9\-\s&+\.]+)*\s+Aktiengesellschaft)(?!\s+Partei)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 13 | 0 | 13 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 13 | 345 |

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

- `Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft` — partial — gold is substring of pred: `Tracondon Aktiengesellschaft`

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

**Example 4** (doc_id: `deanon_TRAIN/2Ob256_12d`) (sent_id: `deanon_TRAIN/2Ob256_12d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Stallbauer Telekom Aktiengesellschaft, Poysdorfer Straße 5, 9341 Dobersberg, Österreich, vertreten durch Dr. Manfred Steininger, Rechtsanwalt in Wien, gegen die beklagte Partei DDr. Viktor Junkmanns, Bakk. iur., vertreten durch die ANWALTGMBH Rinner Teuchtmann in Linz, wegen 50.932,89 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2012, GZ 4 R 158/12a-20, womit das Urteil des Landesgerichts Linz vom 14. Juni 2012, GZ 5 Cg 119/11m-14, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Stallbauer Telekom Aktiengesellschaft` — partial — gold is substring of pred: `Stallbauer Telekom Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stallbauer Telekom Aktiengesellschaft`(organisation)
- `Poysdorfer Straße 5, 9341 Dobersberg, Österreich`(address)
- `DDr. Viktor Junkmanns, Bakk. iur.`(person)

**Example 5** (doc_id: `deanon_TRAIN/3Ob17_20a`) (sent_id: `deanon_TRAIN/3Ob17_20a_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie die Hofräte Priv.-Doz. Dr. Rassi und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Exekutionssache betreibenden Partei Heizung Werkuni Aktiengesellschaft, P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich, vertreten durch Dr. Roland Grilc ua, Rechtsanwälte in Klagenfurt am Wörthersee, gegen die verpflichtete Partei Dorothea Eiken Bank, Peter Eitenmüller, vertreten durch Diwok Hermann Petsche Rechtsanwälte LLP Co KG in Wien, wegen 12.602.980,92 EUR sA, über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. November 2019, GZ 46 R 293/19g-18, mit dem der Beschluss des Bezirksgerichts Favoriten vom 17. April 2019, GZ 17 E 1298/19z-2, bestätigt wurde, den Beschluss gefasst:  Spruch I. Der Revisionsrekurs wird, soweit er sich gegen die Bestätigung der Exekutionsbewilligung richtet, als jedenfalls unzulässig zurückgewiesen.

**False Positives:**

- `Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Exekutionssache betreibenden Partei Heizung Werkuni Aktiengesellschaft` — partial — gold is substring of pred: `Heizung Werkuni Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Heizung Werkuni Aktiengesellschaft`(organisation)
- `P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich`(address)
- `Dorothea Eiken`(person)
- `Peter Eitenmüller`(person)

**Example 6** (doc_id: `deanon_TRAIN/4Ob13_17s`) (sent_id: `deanon_TRAIN/4Ob13_17s_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Daten Steinlem Aktiengesellschaft, Inderstadt 17, 2564 Furth, Österreich, vertreten durch die Huber Swoboda Oswald Aixberger Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Muran Fass, vertreten durch Dr. Fabian Maschke, Rechtsanwalt in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert 35.000 EUR), über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Dezember 2016, GZ 2 R 74/16i-24, womit das Urteil des Landesgerichts Ried im Innkreis vom 25. Februar 2016, GZ 5 Cg 191/14m-14, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei Daten Steinlem Aktiengesellschaft` — partial — gold is substring of pred: `Daten Steinlem Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Daten Steinlem Aktiengesellschaft`(organisation)
- `Inderstadt 17, 2564 Furth, Österreich`(address)
- `Muran Fass`(person)

**Example 7** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_78`)


WGG „§ 1 (1) Bauvereinigungen in den Rechtsformen einer Genossenschaft, einer Gesellschaft mit beschränkter Haftung und einer Aktiengesellschaft, die ihren Sitz im Inland haben, sind von der Landesregierung als gemeinnützig anzuerkennen, wenn sie die in den Bestimmungen dieses Bundesgesetzes vorgesehenen Bedingungen erfüllen.

**False Positives:**

- `Haftung und einer Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_82`)


Bei sonstiger Rechtsunwirksamkeit bedürfen der Zustimmung der Landesregierung Vereinbarungen über: a) den Erwerb von Anteilen an einer Bauvereinigung in der Rechtsform einer Gesellschaft mit beschränkter Haftung oder Aktiengesellschaft, […] (1a)

**False Positives:**

- `Haftung oder Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_86`)


Auch bei Bauvereinigungen in der Rechtsform der Gesellschaft mit beschränkter Haftung oder der Aktiengesellschaft hat die Prüfung diesen Vorschriften zu entsprechen.

**False Positives:**

- `Haftung oder der Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_164`)


[39]4.Die Ergebnisse dieser Entscheidung werden wie folgt zusammengefasst: [40]4.1.Dem für gemeinnützige Bauvereinigungen zuständigen Revisionsverband kommt im Firmenbuchverfahren, das eine gemeinnützige Bauvereinigung betrifft, die Parteistellung nach § 14 Abs 3 FBG auch dann zu, wenn die gemeinnützige Bauvereinigung die Rechtsform einer Gesellschaft mit beschränkter Haftung oder einer Aktiengesellschaft hat.

**False Positives:**

- `Haftung oder einer Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_TRAIN/7Ob141_16k`) (sent_id: `deanon_TRAIN/7Ob141_16k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und die Hofräte Dr. Höllwerth, Mag. Dr. Wurdinger, Mag. Malesich und Dr. Singer als weitere Richter in der Rechtssache der klagenden Partei Seedorf Vertrieb GmbH, Felix Bernloehr, vertreten durch Dr. Helmut Fetz und andere, Rechtsanwälte in Leoben, gegen die beklagte Partei Mlynarik Handel Aktiengesellschaft, Veropastraße 16, 2413 Edelstal, Österreich, vertreten durch Dr. Heimo Jilek und Dr. Martin Sommer, Rechtsanwälte in Leoben, wegen 61.848,15 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 25. Mai 2016, GZ 5 R 9/16g-32, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Partei Mlynarik Handel Aktiengesellschaft` — partial — gold is substring of pred: `Mlynarik Handel Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Seedorf Vertrieb GmbH`(organisation)
- `Felix Bernloehr`(person)
- `Mlynarik Handel Aktiengesellschaft`(organisation)
- `Veropastraße 16, 2413 Edelstal, Österreich`(address)

**Example 12** (doc_id: `deanon_TRAIN/8ObA41_17p`) (sent_id: `deanon_TRAIN/8ObA41_17p_3`)


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

## `German Legal Organisation Specific Entities List`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known entities from training data to ensure high precision for rare names. Added missing entities like 'Buth Analyse GmbH', 'Inn Synmon GmbH', 'Donau Wilverlog', 'KRV Technik', 'Beratung Valtal GmbH', 'Nexberkraft AG', 'Werkber-Garten AG', 'Klüs Event AG'.

**Content:**
```
\b(Buth Analyse GmbH|Inn Synmon GmbH|Donau Wilverlog|KRV Technik|Beratung Valtal GmbH|Nexberkraft AG|Werkber-Garten AG|Klüs Event AG|Tal Kelfurtzor Betriebe GmbH|Hamrosi Garten AG|SKSP Immobilien GmbH|Scherg und Kintzli Holz GmbH|Wagenlöhner Versand GmbH|SKRV IT Vertrieb|Medien Gartheim|WestGarten|Norglanz|Gruetze Handel Limited|RheinLogistik GmbH|Maschinenbau Waldtra GmbH|Bersud-Technik GmbH|JUPL Sicherheit GmbH|Mur Dorfheim GmbH)\b
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

