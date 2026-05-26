# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-05-25T14:11:57.834566

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-05-25/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 76 |
| Validation documents | 20 |
| Test documents | 476 |
| Train sentences | 185 |
| Validation sentences | 45 |
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

**Transfer Learning**

| Property | Value |
|---|---|
| Best Batch Idx | 1 |
| Best Batch F1 | 0.05811450710288419 |
| Best Rules Serialized | [{'id': 'cfc661f1', 'name': "Person after 'Schriftführer' (Court Clerk)", 'description': 'Captures the name of the court clerk mentioned after the title.', 'format': 'regex', 'content': '(?:Schriftführer)\\s+([A-Z][a-z]+(?:\\s+[A-Z][a-z]+)*)', 'priority': 6, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '6e3cfc1d', 'name': "Person after 'fachkundiger Laienrichter'", 'description': 'Captures lay judges mentioned with their specific title.', 'format': 'regex', 'content': '(?:fachkundiger\\s+Laienrichter|fachkundige\\s+Laienrichterin)\\s+([A-Z][a-z]+(?:\\s+[A-Z][a-z]+)*)', 'priority': 5, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '4677ce2b', 'name': 'Person with Academic/Professional Titles', 'description': "Captures names preceded by German academic/professional titles, handling repeated titles and optional 'in' suffixes.", 'format': 'regex', 'content': '\\b(?:Dr\\.(?:in)?|Mag\\.(?:Dr\\.)?|Univ\\.-Prof\\.(?:in)?|Priv\\.-Doz\\.(?:in)?|Hon\\.-Prof\\.(?:in)?|Ing\\.(?:Mag\\.)?|PhD|LL\\.M\\.|Bakk\\. rer\\. nat\\.|OStR|MR|ÖkR|KommR|VetR|PhD OMedR)(?:\\s+(?:Dr\\.(?:in)?|Mag\\.(?:Dr\\.)?|Univ\\.-Prof\\.(?:in)?|Priv\\.-Doz\\.(?:in)?|Hon\\.-Prof\\.(?:in)?|Ing\\.(?:Mag\\.)?|PhD|LL\\.M\\.|Bakk\\. rer\\. nat\\.|OStR|MR|ÖkR|KommR|VetR|PhD OMedR))?\\s+[A-Z][a-z]+(?:\\s+[A-Z][a-z]+)+', 'priority': 10, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '9b474dd4', 'name': 'Person after Judicial Role', 'description': 'Captures the full name (including title) appearing immediately after judicial role indicators, excluding the role text.', 'format': 'regex', 'content': '(?:die\\s+Richterin|der\\s+Richter|die\\s+Senatsvorsitzende)\\s+(?:Dr\\.(?:in)?|Mag\\.(?:Dr\\.)?|Univ\\.-Prof\\.(?:in)?|Priv\\.-Doz\\.(?:in)?|Hon\\.-Prof\\.(?:in)?|Ing\\.(?:Mag\\.)?|PhD|LL\\.M\\.|Bakk\\. rer\\. nat\\.|OStR|MR|ÖkR|KommR|VetR|PhD OMedR)?\\s+([A-Z][a-z]+(?:\\s+[A-Z][a-z]+)+)', 'priority': 9, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'dd884f7b', 'name': 'Person in Legal Case Context', 'description': "Captures names appearing after 'Beschwerdesache' or similar case introductions, ensuring full name is captured.", 'format': 'regex', 'content': '(?:in\\s+der\\s+Beschwerdesache|der\\s+Beschwerdesache|in\\s+der\\s+Verwaltungsstrafsache|gegen\\s+Herrn|gegen\\s+Frau|gegen\\s+die)\\s+([A-Z][a-z]+(?:\\s+[A-Z][a-z]+)+)', 'priority': 8, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '4499bf7e', 'name': "Person after 'vertreten durch' (represented by)", 'description': "Captures names of legal representatives following 'vertreten durch', ensuring full name is captured.", 'format': 'regex', 'content': '(?:vertreten\\s+durch)\\s+([A-Z][a-z]+(?:\\s+[A-Z][a-z]+)+)', 'priority': 7, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '78d78435', 'name': 'Standalone Person Name in Legal Context', 'description': 'Captures standalone capitalized names in legal contexts where no title or specific role precedes them.', 'format': 'regex', 'content': '(?:eingetragenen|für\\s+seine\\s+Kinder|für\\s+das\\s+Kind|der\\s+Beschwerdeführerin|der\\s+Beschwerdeführer|der\\s+Beschuldigte|der\\s+Abgabepflichtige|der\\s+Bf\\.)\\s+([A-Z][a-z]+(?:\\s+[A-Z][a-z]+)+)', 'priority': 5, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '79232d4e', 'name': "Person after 'Herrn' or 'Frau'", 'description': "Captures names preceded by 'Herrn' or 'Frau' in legal texts.", 'format': 'regex', 'content': '(?:Herrn|Frau)\\s+([A-Z][a-z]+(?:\\s+[A-Z][a-z]+)+)', 'priority': 4, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '23bbc7f9', 'name': "Person after 'Gattin' or 'Kinder'", 'description': 'Captures names of spouses or children mentioned in legal contexts.', 'format': 'regex', 'content': '(?:und\\s+dessen\\s+Gattin|und\\s+deren\\s+Gattin|für\\s+seine\\s+Kinder|für\\s+das\\s+Kind|für\\s+ihre\\s+Tochter|für\\s+seinen\\s+Sohn)\\s+([A-Z][a-z]+(?:\\s+[A-Z][a-z]+)+)', 'priority': 6, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}] |

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 96.1% |
| True Positives | 149 |
| False Positives | 756 |
| False Negatives | 1226 |
| Total Gold Entities | 1375 |
| Micro Precision | 16.5% |
| Micro Recall | 10.8% |
| Micro F1 | 13.1% |
| Macro F1 | 13.1% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Person with Academic/Professional Titles` | 13.8% | 18.8% | 10.8% | 791 | 149 | 642 |
| `Person after 'Schriftführer' (Court Clerk)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Person after 'fachkundiger Laienrichter'` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Person after Judicial Role` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Person in Legal Case Context` | 0.0% | 0.0% | 0.0% | 19 | 0 | 19 |
| `Person after 'vertreten durch' (represented by)` | 0.0% | 0.0% | 0.0% | 99 | 0 | 99 |
| `Standalone Person Name in Legal Context` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Person after 'Herrn' or 'Frau'` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Person after 'Gattin' or 'Kinder'` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `Person with Academic/Professional Titles`

**F1:** 0.138 | **Precision:** 0.188 | **Recall:** 0.108  

**Format:** `regex`  
**Rule ID:** `4677ce2b`  
**Description:**
Captures names preceded by German academic/professional titles, handling repeated titles and optional 'in' suffixes.

**Content:**
```
\b(?:Dr\.(?:in)?|Mag\.(?:Dr\.)?|Univ\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Hon\.-Prof\.(?:in)?|Ing\.(?:Mag\.)?|PhD|LL\.M\.|Bakk\. rer\. nat\.|OStR|MR|ÖkR|KommR|VetR|PhD OMedR)(?:\s+(?:Dr\.(?:in)?|Mag\.(?:Dr\.)?|Univ\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Hon\.-Prof\.(?:in)?|Ing\.(?:Mag\.)?|PhD|LL\.M\.|Bakk\. rer\. nat\.|OStR|MR|ÖkR|KommR|VetR|PhD OMedR))?\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.188 | 0.108 | 0.138 | 791 | 149 | 642 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 149 | 642 | 1226 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc22_25d`) (sent_id: `deanon_TRAIN/10Nc22_25d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hargassner als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi und den Hofrat Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Juri Petraschk, Bakk. iur., gegen die beklagte Partei Mag. Dominik Riewert, wegen Feststellung, über den Delegierungsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an ein Gericht außerhalb des Sprengels des Oberlandesgerichts Wien wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dominik Riewert` | `Mag. Dominik Riewert` |

**Missed by this rule (FN):**

- `Juri Petraschk, Bakk. iur.` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen ÖkR Priv.-Doz. Sven Egerth, geboren 3. Mai 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt.

| Predicted | Gold |
|---|---|
| `ÖkR Priv.-Doz. Sven Egerth` | `ÖkR Priv.-Doz. Sven Egerth` |

**Missed by this rule (FN):**

- `3. Mai` (date)
- `Bezirksgericht Graz` (organisation)

**Example 2** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Sten und Stöwer Wind GmbH, OMedR Torsten Münchmeyer, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei OStR Gregor Ruemmel, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `OStR Gregor Ruemmel` | `OStR Gregor Ruemmel` |

**Missed by this rule (FN):**

- `Sten und Stöwer Wind GmbH` (organisation)
- `OMedR Torsten Münchmeyer` (person)

**Example 3** (doc_id: `deanon_TRAIN/10Nc6_22x`) (sent_id: `deanon_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei PhD Ignaz Nardelli, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Diethard Eisenlöffel, Bakk. phil., Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `PhD Ignaz Nardelli` | `PhD Ignaz Nardelli` |

**Missed by this rule (FN):**

- `Diethard Eisenlöffel, Bakk. phil.` (person)
- `Bezirksgericht Schwechat` (organisation)

**Example 4** (doc_id: `deanon_TRAIN/10Ob11_11g`) (sent_id: `deanon_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Mag. Elmar Janaschek, geboren am 8. Mai 1999, und der minderjährigen VetR Charlotte Eissenmann, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Elmar Janaschek` | `Mag. Elmar Janaschek` |
| `VetR Charlotte Eissenmann` | `VetR Charlotte Eissenmann` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Karin Meiwaldt, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Katharina Tomandl, MA, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Mag. Ernst Michael Lang` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Karin Meiwaldt`(person)
- `Katharina Tomandl, MA`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Chen Mestwerdt, Slowenien, vertreten durch Mag. Erich Hierz, Rechtsanwalt in Graz, gegen die beklagte Partei Roman Eschenweck, Deutschland, vertreten durch Salleck + Partner Rechtsanwälte in Deutschland, wegen 5.856 EUR sA, 1.342 EUR sA und 915 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag, die Rechtssache gemäß § 28 JN einem österreichischem Gericht zuzuweisen, wird zurückgewiesen.

**False Positives:**

- `Mag. Erich Hierz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Chen Mestwerdt`(person)
- `Roman Eschenweck`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Sten und Stöwer Wind GmbH, OMedR Torsten Münchmeyer, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei OStR Gregor Ruemmel, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Mag. Alexander Rimser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Sten und Stöwer Wind GmbH`(organisation)
- `OMedR Torsten Münchmeyer`(person)
- `OStR Gregor Ruemmel`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei C. Dersudheim Digital GmbH, Taxlbergstraße 247, 8151 Rohrbach, Österreich, vertreten durch Dr. Carl Benkhofer, Rechtsanwalt in Wien, gegen die beklagte Partei Ingolf Grimpe, vertreten durch Greiml & Horwath Rechtsanwaltspartnerschaft in Graz, wegen 5.232 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 14 C 1302/11a des Bezirksgerichts Graz-West in nichtöffentlicher Sitzung, den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Graz-West das Bezirksgericht Fünfhaus bestimmt.

**False Positives:**

- `Dr. Carl Benkhofer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dersudheim Digital GmbH`(organisation)
- `Taxlbergstraße 247, 8151 Rohrbach, Österreich`(address)
- `Ingolf Grimpe`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Nc7_10a`) (sent_id: `deanon_TRAIN/10Nc7_10a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger und Hon.-Prof. Dr. Neumayr als weitere Richter in der Verlassenschaftssache nach dem am 9. September 2009 verstorbenen, zuletzt in Tschiggfreystraße 46, 3240 Loitsdorf, Österreich, wohnhaft gewesenen Manfred Johann Pingert, AZ 1 A 349/09w des Bezirksgerichts Kitzbühel, über den Delegierungsantrag der Karin Czychy, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, den B e s c h l u s s gefasst:  Spruch Dem Delegierungsantrag wird stattgegeben.

**False Positives:**

- `Mag. Maximilian Kocher` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Tschiggfreystraße 46, 3240 Loitsdorf, Österreich`(address)
- `Pingert`(person)
- `Czychy`(person)

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `Person after 'vertreten durch' (represented by)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4499bf7e`  
**Description:**
Captures names of legal representatives following 'vertreten durch', ensuring full name is captured.

**Content:**
```
(?:vertreten\s+durch)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 99 | 0 | 99 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 99 | 1357 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc6_22x`) (sent_id: `deanon_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei PhD Ignaz Nardelli, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Diethard Eisenlöffel, Bakk. phil., Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Skribe Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `PhD Ignaz Nardelli`(person)
- `Diethard Eisenlöffel, Bakk. phil.`(person)
- `Bezirksgericht Schwechat`(organisation)

**Example 1** (doc_id: `deanon_TRAIN/10Ob12_24y`) (sent_id: `deanon_TRAIN/10Ob12_24y_5`)


Isidor Janofske, beide vertreten durch Ghendler Ruvinskij Rechtsanwaltsgesellschaft mbH in Wien, gegen die beklagte Partei Wolfram Fritzsche S.p.A., VetR Lukas Dickhaus, vertreten durch bpv Hügel Rechtsanwälte GmbH in Wien, wegen 71.425,56 EUR sA, aus Anlass der Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 20. Dezember 2023, GZ 6 R 68/23a-41, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 21. August 2023, GZ 19 Cg 10/22f-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die gemeinsame Anzeige der Parteien über das vereinbarte „ewige“ Ruhen des Verfahrens wird zur Kenntnis genommen.

**False Positives:**

- `Ghendler Ruvinskij Rechtsanwaltsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Isidor Janofske`(person)
- `Wolfram Fritzsche`(person)
- `VetR Lukas Dickhaus`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob13_15g`) (sent_id: `deanon_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Zoltan Alfermann, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei DonauFurtostBildung GmbH, KzlR Noah Christansen, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Lederer Rechtsanwalt Gmb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zoltan Alfermann`(person)
- `DonauFurtostBildung GmbH`(organisation)
- `KzlR Noah Christansen`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob21_15h`) (sent_id: `deanon_TRAIN/10Ob21_15h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Kotschenreuther u. Abele Planung GmbH, Janis Krentzel, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, gegen die beklagte Partei Mittel Keltal GmbH, Julian Grebener, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, wegen 7.731,06 EUR und Feststellung (Streitwert 20.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse insgesamt 11.597,42 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 216/14h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Vavrovsky Heine Marth Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Kotschenreuther u. Abele Planung GmbH`(organisation)
- `Janis Krentzel`(person)
- `Mittel Keltal GmbH`(organisation)
- `Julian Grebener`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob23_18g`) (sent_id: `deanon_TRAIN/10Ob23_18g_4`)


Severin Simaitis, geboren 20. November 2002, 2. 8. Juli 1967, geboren 17. November 2004, und 3. Nepomuk Sprinzl, geboren 11. September 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Miklos Stiening, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Doschek Rechtsanwalts Gmb` — no gold match — likely missing annotation

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

## `Person in Legal Case Context`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `dd884f7b`  
**Description:**
Captures names appearing after 'Beschwerdesache' or similar case introductions, ensuring full name is captured.

**Content:**
```
(?:in\s+der\s+Beschwerdesache|der\s+Beschwerdesache|in\s+der\s+Verwaltungsstrafsache|gegen\s+Herrn|gegen\s+Frau|gegen\s+die)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 19 | 0 | 19 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 19 | 918 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/15Os133_11i_15Os134_11m_`) (sent_id: `deanon_TRAIN/15Os133_11i_15Os134_11m__3`)


Kopf Der Oberste Gerichtshof hat am 16. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Danek als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Dr. Michel-Kwapinski als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Kopinits als Schriftführer in der Medienrechtssache des Antragstellers Siegfried Klimczuk gegen die Antragsgegnerin Reifner Medien GmbH wegen §§ 6 Abs 1, 8a Abs 6 MedienG, AZ 91 Hv 72/05g des Landesgerichts für Strafsachen Wien, über die von der Generalprokuratur gegen die Beschlüsse des Landesgerichts für Strafsachen Wien vom 28. April 2009, GZ 91 Hv 72/05g-75, und des Oberlandesgerichts Wien als Beschwerdegericht vom 6. Juli 2009, AZ 18 Bs 218/09d, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Knibbe, des Vertreters des Antragstellers Dr. Rami sowie jenes der Antragsgegnerin Mag. Renzl zu Recht erkannt:  Spruch

**False Positives:**

- `Antragsgegnerin Reifner Medien Gmb` — positional overlap with gold: `Reifner Medien GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Klimczuk`(person)
- `Reifner Medien GmbH`(organisation)

**Example 1** (doc_id: `deanon_TRAIN/15Os133_11i_15Os134_11m_`) (sent_id: `deanon_TRAIN/15Os133_11i_15Os134_11m__5`)


Text Gründe: In der Medienrechtssache des Antragstellers Siegfried Knechtlein gegen die Antragsgegnerin Traglanz Software GmbH wegen §§ 6 Abs 1, 8a Abs 6 MedienG, AZ 91 Hv 72/05g des Landesgerichts für Strafsachen Wien, wurde mit Urteil vom 18. November 2005 (ON 17) mit Beziehung auf eine in der in der periodischen Druckschrift „ Ida Parakeninks “ Nr 18 vom 2. Mai 2005 erschienenen Veröffentlichung enthaltene, dem Antragsteller zugeschriebene Äußerung („Wehrmachtsdeserteure sind Kameradenmörder“) der Antragsgegnerin gemäß § 6 Abs 1 MedienG die Zahlung einer Entschädigung von 4.000 Euro an den Antragsteller sowie gemäß § 8a Abs 1 MedienG iVm § 389 Abs 1 StPO der Ersatz der Verfahrenskosten auferlegt und sie gemäß § 8a Abs 6 MedienG zur Urteilsveröffentlichung verpflichtet.

**False Positives:**

- `Antragsgegnerin Traglanz Software Gmb` — positional overlap with gold: `Traglanz Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Knechtlein`(person)
- `Traglanz Software GmbH`(organisation)
- `Ida Parakeninks`(person)

**Example 2** (doc_id: `deanon_TRAIN/1Ob105_18z`) (sent_id: `deanon_TRAIN/1Ob105_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Familienrechtssache des Antragstellers Ilona Hoerhold, vertreten durch die Korp Rechtsanwalts GmbH, Andorf, gegen die Antragsgegnerin Farina Prokofyev, vertreten durch die Puttinger Vogl Rechtsanwälte GmbH, Ried im Innkreis, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts Wels als Rekursgericht vom 2. Mai 2018, GZ 21 R 50/18d-32, mit dem der Rekurs des Antragstellers gegen den Beschluss des Bezirksgerichts Grieskirchen vom 8. Jänner 2018, GZ 8 Fam 37/16i-26, zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

**False Positives:**

- `Antragsgegnerin Farina Prokofyev` — partial — gold is substring of pred: `Farina Prokofyev`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ilona Hoerhold`(person)
- `Farina Prokofyev`(person)

**Example 3** (doc_id: `deanon_TRAIN/1Ob128_17f`) (sent_id: `deanon_TRAIN/1Ob128_17f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Familienrechtssache des Antragstellers Mag. Jeannette Scherl, vertreten durch die Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG, Wien, gegen die Antragsgegnerin Selina Dorfmeyer, vertreten durch Mag. Anna-Maria Freiberger, Rechtsanwältin in Wien, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 24. April 2017, GZ 45 R 66/17i, 67/17m-19, mit dem die Beschlüsse des Bezirksgerichts Liesing vom 4. Jänner 2017, GZ 7 Fam 30/16m-12, und vom 17. Jänner 2017, GZ 7 Fam 30/16m-14, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Antragsgegnerin Selina Dorfmeyer` — partial — gold is substring of pred: `Selina Dorfmeyer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Jeannette Scherl`(person)
- `Selina Dorfmeyer`(person)

**Example 4** (doc_id: `deanon_TRAIN/1Ob205_10v`) (sent_id: `deanon_TRAIN/1Ob205_10v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Dr. E. Solé und Mag. Wurzer als weitere Richter in der Rechtssache des Antragstellers Hans Päulgen, vertreten durch Mag. Matthias Kucera, Rechtsanwalt in Hard, gegen die Antragsgegnerin Herta Polaschegg, vertreten durch Dr. Wolf Heistinger, Rechtsanwalt in Mödling, wegen Anerkennung eines ausländischen Scheidungsurteils, über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 13. Oktober 2010, GZ 16 R 384/10z-11, mit dem der Beschluss des Bezirksgerichts Mödling vom 1. September 2010, GZ 13 Nc 14/10w-5, bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

**False Positives:**

- `Antragsgegnerin Herta Polaschegg` — partial — gold is substring of pred: `Polaschegg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Päulgen`(person)
- `Polaschegg`(person)

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `Person after 'Schriftführer' (Court Clerk)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `cfc661f1`  
**Description:**
Captures the name of the court clerk mentioned after the title.

**Content:**
```
(?:Schriftführer)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Person after 'fachkundiger Laienrichter'`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6e3cfc1d`  
**Description:**
Captures lay judges mentioned with their specific title.

**Content:**
```
(?:fachkundiger\s+Laienrichter|fachkundige\s+Laienrichterin)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Person after 'Herrn' or 'Frau'`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `79232d4e`  
**Description:**
Captures names preceded by 'Herrn' or 'Frau' in legal texts.

**Content:**
```
(?:Herrn|Frau)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Person after 'Gattin' or 'Kinder'`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `23bbc7f9`  
**Description:**
Captures names of spouses or children mentioned in legal contexts.

**Content:**
```
(?:und\s+dessen\s+Gattin|und\s+deren\s+Gattin|für\s+seine\s+Kinder|für\s+das\s+Kind|für\s+ihre\s+Tochter|für\s+seinen\s+Sohn)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
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

## `Person with Academic/Professional Titles`

**F1:** 0.138 | **Precision:** 0.188 | **Recall:** 0.108  

**Format:** `regex`  
**Rule ID:** `4677ce2b`  
**Description:**
Captures names preceded by German academic/professional titles, handling repeated titles and optional 'in' suffixes.

**Content:**
```
\b(?:Dr\.(?:in)?|Mag\.(?:Dr\.)?|Univ\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Hon\.-Prof\.(?:in)?|Ing\.(?:Mag\.)?|PhD|LL\.M\.|Bakk\. rer\. nat\.|OStR|MR|ÖkR|KommR|VetR|PhD OMedR)(?:\s+(?:Dr\.(?:in)?|Mag\.(?:Dr\.)?|Univ\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Hon\.-Prof\.(?:in)?|Ing\.(?:Mag\.)?|PhD|LL\.M\.|Bakk\. rer\. nat\.|OStR|MR|ÖkR|KommR|VetR|PhD OMedR))?\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.188 | 0.108 | 0.138 | 791 | 149 | 642 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 149 | 642 | 1226 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc22_25d`) (sent_id: `deanon_TRAIN/10Nc22_25d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hargassner als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi und den Hofrat Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Juri Petraschk, Bakk. iur., gegen die beklagte Partei Mag. Dominik Riewert, wegen Feststellung, über den Delegierungsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an ein Gericht außerhalb des Sprengels des Oberlandesgerichts Wien wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dominik Riewert` | `Mag. Dominik Riewert` |

**Missed by this rule (FN):**

- `Juri Petraschk, Bakk. iur.` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen ÖkR Priv.-Doz. Sven Egerth, geboren 3. Mai 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt.

| Predicted | Gold |
|---|---|
| `ÖkR Priv.-Doz. Sven Egerth` | `ÖkR Priv.-Doz. Sven Egerth` |

**Missed by this rule (FN):**

- `3. Mai` (date)
- `Bezirksgericht Graz` (organisation)

**Example 2** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Sten und Stöwer Wind GmbH, OMedR Torsten Münchmeyer, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei OStR Gregor Ruemmel, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `OStR Gregor Ruemmel` | `OStR Gregor Ruemmel` |

**Missed by this rule (FN):**

- `Sten und Stöwer Wind GmbH` (organisation)
- `OMedR Torsten Münchmeyer` (person)

**Example 3** (doc_id: `deanon_TRAIN/10Nc6_22x`) (sent_id: `deanon_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei PhD Ignaz Nardelli, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Diethard Eisenlöffel, Bakk. phil., Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `PhD Ignaz Nardelli` | `PhD Ignaz Nardelli` |

**Missed by this rule (FN):**

- `Diethard Eisenlöffel, Bakk. phil.` (person)
- `Bezirksgericht Schwechat` (organisation)

**Example 4** (doc_id: `deanon_TRAIN/10Ob11_11g`) (sent_id: `deanon_TRAIN/10Ob11_11g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Mag. Elmar Janaschek, geboren am 8. Mai 1999, und der minderjährigen VetR Charlotte Eissenmann, geboren am 28. November 2000, beide vertreten durch den Jugendwohlfahrtsträger Land Wien (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung, Bezirk 10, Van-der-Nüll-Gasse 20), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. September 2010, GZ 48 R 259/10h, 48 R 260/10f-42, womit die Beschlüsse des Bezirksgerichts Favoriten vom 25. März 2010, GZ 8 PU 327/09z-26 und -27, abgeändert wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Elmar Janaschek` | `Mag. Elmar Janaschek` |
| `VetR Charlotte Eissenmann` | `VetR Charlotte Eissenmann` |

**Example 5** (doc_id: `deanon_TRAIN/10Ob12_24y`) (sent_id: `deanon_TRAIN/10Ob12_24y_5`)


Isidor Janofske, beide vertreten durch Ghendler Ruvinskij Rechtsanwaltsgesellschaft mbH in Wien, gegen die beklagte Partei Wolfram Fritzsche S.p.A., VetR Lukas Dickhaus, vertreten durch bpv Hügel Rechtsanwälte GmbH in Wien, wegen 71.425,56 EUR sA, aus Anlass der Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 20. Dezember 2023, GZ 6 R 68/23a-41, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 21. August 2023, GZ 19 Cg 10/22f-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die gemeinsame Anzeige der Parteien über das vereinbarte „ewige“ Ruhen des Verfahrens wird zur Kenntnis genommen.

| Predicted | Gold |
|---|---|
| `VetR Lukas Dickhaus` | `VetR Lukas Dickhaus` |

**Missed by this rule (FN):**

- `Isidor Janofske` (person)
- `Wolfram Fritzsche` (person)

**Example 6** (doc_id: `deanon_TRAIN/10Ob13_15g`) (sent_id: `deanon_TRAIN/10Ob13_15g_6`)


Text Entscheidungsgründe: Über Vermittlung der Beklagten und nach Beratung durch deren Mitarbeiter Ing. Vivian Wenz erwarb die Klägerin im Mai 2007 um 20.000 EUR Immofinanz- und Immoeast-Aktien.

| Predicted | Gold |
|---|---|
| `Ing. Vivian Wenz` | `Ing. Vivian Wenz` |

**Example 7** (doc_id: `deanon_TRAIN/10Ob13_15g`) (sent_id: `deanon_TRAIN/10Ob13_15g_7`)


Als sie einen Kursverfall dieser Aktien 2008/2009 zu einem nicht mehr näher feststellbaren Zeitpunkt wahrnahm, stellte sie erstmals fest, dass sie mit diesen Aktien ein Finanzprodukt erworben hatte, das weder dem Inhalt der Beratung des Ing. Dietrich Worell noch vom Risiko und der Risikostreuung im „Portfolio“ her dem entsprach, was sie 2007 hatte erwerben wollen.

| Predicted | Gold |
|---|---|
| `Ing. Dietrich Worell` | `Ing. Dietrich Worell` |

**Example 8** (doc_id: `deanon_TRAIN/10Ob13_15g`) (sent_id: `deanon_TRAIN/10Ob13_15g_9`)


Mit der am 30. 8. 2010 eingebrachten Klage begehrte die Klägerin von der Beklagten Zahlung von 20.000 EUR sA wegen fehlerhafter Anlageberatung durch deren Mitarbeiter Ing. Miklos Wiederaenders im Zusammenhang mit dem Erwerb von Immofinanz- und Immoeast-Aktien.

| Predicted | Gold |
|---|---|
| `Ing. Miklos Wiederaenders` | `Ing. Miklos Wiederaenders` |

**Example 9** (doc_id: `deanon_TRAIN/10Ob13_20i`) (sent_id: `deanon_TRAIN/10Ob13_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Miranda Klagemann, vertreten durch Dr. Andreas Ladstätter, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. DI Adolf Kowallek, und 2. Ing. Janis Grottian, beide vertreten durch Dr. Walter Schuhmeister und Mag. Franz Haydn, Rechtsanwälte in Schwechat, wegen 15.000 EUR sA, infolge Revision der beklagten Parteien (Revisionsinteresse 6.250 EUR) gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 30. Jänner 2019, GZ 34 R 66/18k-27, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Innere Stadt Wien vom 23. März 2018, GZ 37 C 780/16f-18, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `Ing. Janis Grottian` | `Ing. Janis Grottian` |

**Missed by this rule (FN):**

- `Miranda Klagemann` (person)
- `DI Adolf Kowallek` (person)

**Example 10** (doc_id: `deanon_TRAIN/10Ob15_12x`) (sent_id: `deanon_TRAIN/10Ob15_12x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Egon Luckow, geboren am 1. August 2011, und des mj Priv.-Doz. Samuel Prestle, geboren am 14. November 2003, beide vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie, Rechtsvertretung, Bezirk 22, 1220 Wien, Kapellenweg 35), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Jänner 2012, GZ 45 R 29/12s, 45 R 30/12p-16, womit infolge Rekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien, die Beschlüsse des Bezirksgerichts Donaustadt jeweils vom 25. Oktober 2011, GZ 17 PU 193/11k-4 und -5, abgeändert wurden, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Samuel Prestle` | `Priv.-Doz. Samuel Prestle` |

**Missed by this rule (FN):**

- `Egon Luckow` (person)

**Example 11** (doc_id: `deanon_TRAIN/10Ob16_14x`) (sent_id: `deanon_TRAIN/10Ob16_14x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Walter Gritzmacher, vertreten durch Dr. Birgit Lajtai-Nagl, Rechtsanwältin in Villach, gegen die beklagte Partei Dr. Ariadne Graspointner, vertreten durch Dr. Robert Kugler, Rechtsanwalt in Klagenfurt, wegen Unterhalts, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 27. November 2013, GZ 2 R 234/13h-116, womit das Urteil des Bezirksgerichts Villach vom 27. August 2013, GZ 3 C 144/06w-109, abgeändert wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `Dr. Ariadne Graspointner` | `Dr. Ariadne Graspointner` |

**Missed by this rule (FN):**

- `Walter Gritzmacher` (person)

**Example 12** (doc_id: `deanon_TRAIN/10Ob18_13i`) (sent_id: `deanon_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Monsud-Textil GmbH, VetR Herbert Dedert, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

| Predicted | Gold |
|---|---|
| `VetR Herbert Dedert` | `VetR Herbert Dedert` |

**Missed by this rule (FN):**

- `Monsud-Textil GmbH` (organisation)

**Example 13** (doc_id: `deanon_TRAIN/10Ob23_14a`) (sent_id: `deanon_TRAIN/10Ob23_14a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Aurelia von der Lei, geboren am 10. September 1997, in Pflege und Erziehung der Mutter Univ.-Prof.in Marceline Siladji, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Gmunden, 4810 Gmunden, Esplanade 10), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Linz, gegen den Beschluss des Landesgerichts Wels als Rekursgericht vom 15. Jänner 2014, GZ 21 R 298/13t-38, womit der Beschluss des Bezirksgerichts Gmunden vom 18. Oktober 2013, GZ 1 Pu 223/09k-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Marceline Siladji` | `Univ.-Prof.in Marceline Siladji` |

**Missed by this rule (FN):**

- `Aurelia von der Lei` (person)

**Example 14** (doc_id: `deanon_TRAIN/10Ob23_18g`) (sent_id: `deanon_TRAIN/10Ob23_18g_4`)


Severin Simaitis, geboren 20. November 2002, 2. 8. Juli 1967, geboren 17. November 2004, und 3. Nepomuk Sprinzl, geboren 11. September 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Miklos Stiening, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Miklos Stiening` | `Mag. Miklos Stiening` |

**Missed by this rule (FN):**

- `Severin Simaitis` (person)
- `20. November` (date)
- `8. Juli 1967` (date)
- `17. November` (date)
- `Nepomuk Sprinzl` (person)
- `11. September` (date)

**Example 15** (doc_id: `deanon_TRAIN/10Ob28_17s`) (sent_id: `deanon_TRAIN/10Ob28_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Schramm, Dr. Fichtenau, Dr. Grohmann und Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Kindes Jaroslaw Mlynarik, geboren am 1. Juli 2009, wegen Kontaktrechts des Vaters Dr. Eckard Tschernig, vertreten durch Rechtsanwälte Pieler & Pieler & Partner KG in Wien, infolge des außerordentlichen Revisionsrekurses der Mutter Dr. Bettina Makswietat, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wiener Neustadt, gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 31. Jänner 2017, GZ 16 R 12/17d-129, mit dem der Beschluss des Bezirksgerichts Wiener Neustadt vom 2. Dezember 2016, GZ 6 Ps 67/16s-122, teilweise bestätigt, teilweise abgeändert und teilweise aufgehoben wurde, den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 13. Juni 2017, AZ 10 Ob 28/17s, wird dahingehend berichtigt, dass die Wortfolge „einschließlich des Auftrags zur Erziehungsberatung“ in Spruchpunkt 2 zweiter Satz sowie auf S 5 dritter Absatz zu entfallen hat.

| Predicted | Gold |
|---|---|
| `Dr. Eckard Tschernig` | `Dr. Eckard Tschernig` |
| `Dr. Bettina Makswietat` | `Dr. Bettina Makswietat` |

**Missed by this rule (FN):**

- `Jaroslaw Mlynarik` (person)
- `1. Juli 2009` (date)
- `Partner KG` (organisation)

**Example 16** (doc_id: `deanon_TRAIN/10Ob2_14p`) (sent_id: `deanon_TRAIN/10Ob2_14p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Calvin Mützlaff, geboren am Volker Scheffski, Jaden Jurkutaitis, geboren am 8. Dezember 1982 und PhD Karim Trieber, geboren am 11. Januar 1975, in Pflege und Erziehung der Mutter StR Lara Jungnikl, vertreten durch das Land Vorarlberg als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Feldkirch, Schlossgraben 1, 6800 Feldkirch), wegen Gewährung von Unterhaltsvorschuss, über den Revisionsrekurs des Vaters RgR Dipl.-Ing. Quirin Bagemühl, vertreten durch Mag. Hans-Christian Obernberger, Rechtsanwalt in Feldkirch, gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 12. Juli 2011, GZ 3 R 198/11g, 3 R 199/11d, 3 R 200/11a-18, womit die Beschlüsse des Bezirksgerichts Feldkirch vom 18. Mai 2011, GZ 12 Pu 141/11f-4 bis 6, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `PhD Karim Trieber` | `PhD Karim Trieber` |

**Missed by this rule (FN):**

- `Calvin Mützlaff` (person)
- `Volker Scheffski` (person)
- `Jaden Jurkutaitis` (person)
- `8. Dezember 1982` (date)
- `11. Januar 1975` (date)
- `StR Lara Jungnikl` (person)
- `RgR Dipl.-Ing. Quirin Bagemühl` (person)

**Example 17** (doc_id: `deanon_TRAIN/10Ob2_14p`) (sent_id: `deanon_TRAIN/10Ob2_14p_83`)


Nach dem Unterhaltsherabsetzungsantrag des Vaters vom 20. 12. 2011 (Band I, ON 29 und ON 30) wurde mit der Vorschussgewährung ohnehin bereits teilweise innegehalten, sodass anstatt der ursprünglich gewährten 791,50 EUR monatlich pro Kind nunmehr - wie der Vater beantragte - nur noch monatliche Unterhaltsvorschüsse von 300 EUR für Cassandra Mustapha, 340 EUR für Jeannine Janowska und 330 EUR für PhD Zdenko Tomayer zur Auszahlung gelangen (Band I, ON 31, vgl auch Band II, ON 75, womit das Rekursgericht dem Erstgericht die Fortsetzung des Unterhaltsherabsetzungsverfahrens auftrug).

| Predicted | Gold |
|---|---|
| `PhD Zdenko Tomayer` | `PhD Zdenko Tomayer` |

**Missed by this rule (FN):**

- `Cassandra Mustapha` (person)
- `Jeannine Janowska` (person)

**Example 18** (doc_id: `deanon_TRAIN/10Ob3_12g`) (sent_id: `deanon_TRAIN/10Ob3_12g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Helge Monhemius, Bakk. techn., vertreten durch Dr. Georg Gorton und DDr. Birgit Gorton, Rechtsanwälte in Klagenfurt, gegen die beklagte Partei Ing. Eugenia Welze, vertreten durch Dr. Gottfried Kassin, Rechtsanwalt in St. Veit an der Glan, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 26. Mai 2011, GZ 2 R 83/11z-49, mit dem das Urteil des Bezirksgerichts St. Veit an der Glan vom 29. Oktober 2010, GZ 3 C 333/09h-34, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ing. Eugenia Welze` | `Ing. Eugenia Welze` |

**Missed by this rule (FN):**

- `Helge Monhemius, Bakk. techn.` (person)

**Example 19** (doc_id: `deanon_TRAIN/10Ob41_20g`) (sent_id: `deanon_TRAIN/10Ob41_20g_4`)


Dr. Emmerich Schrammen, Niederlande, und 3.)

| Predicted | Gold |
|---|---|
| `Dr. Emmerich Schrammen` | `Dr. Emmerich Schrammen` |

**Example 20** (doc_id: `deanon_TRAIN/10Ob41_20g`) (sent_id: `deanon_TRAIN/10Ob41_20g_5`)


Dr. Torsten Classe, Niederlande, beide vertreten durch Tramposch & Partner, Rechtsanwälte KG in Innsbruck, gegen die beklagte Partei Jaqueline Ratzenböck, vertreten durch König Ermacora Klotz & Partner, Rechtsanwälte in Innsbruck, wegen je 15.000 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 1. Juli 2020, GZ 10 R 16/20h-49, mit dem das Urteil des Landesgerichts Innsbruck vom 6. Februar 2020, GZ 41 Cg 11/19i-42, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Torsten Classe` | `Dr. Torsten Classe` |

**Missed by this rule (FN):**

- `Jaqueline Ratzenböck` (person)

**Example 21** (doc_id: `deanon_TRAIN/10Ob42_15x`) (sent_id: `deanon_TRAIN/10Ob42_15x_5`)


Text Begründung: Mit Beschluss vom 14. 3. 2013, GZ 3 Pu 61/12x-40, verpflichtete das Erstgericht den Vater der minderjährigen Mathias Weinschrod und des minderjährigen PhD Regina Milbradt, ab 1. 3. 2012 einen monatlichen Unterhaltsbeitrag von 75 EUR für Enrico Weffers und von 55 EUR für Veit Mazzei zu leisten;

| Predicted | Gold |
|---|---|
| `PhD Regina Milbradt` | `PhD Regina Milbradt` |

**Missed by this rule (FN):**

- `Mathias Weinschrod` (person)
- `Enrico Weffers` (person)
- `Veit Mazzei` (person)

**Example 22** (doc_id: `deanon_TRAIN/10Ob57_13z`) (sent_id: `deanon_TRAIN/10Ob57_13z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der Kinder Pablo Ebling, geboren am 9. August 1991, Hugo Stegemann, geboren am 30. September 1992, mj Delila Ringsdorff, geboren am 22. Dezember 1998 und mj Nigel Conrades, Bakk. techn. BEd, geboren am 18. Jänner 2001, wegen Unterhaltsvorschuss, infolge Revisionsrekurses des Vaters Mag. Vivian Hadamzick, vertreten durch Mag. Roland Marko, Rechtsanwalt in Wien, dieser vertreten durch Dr. Francisco Rumpf, Rechtsanwalt in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 7. Juni 2013, GZ 43 R 391/08f ua -U-458, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 12. November 2007, GZ 2 P 88/07t-U-238, abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Vivian Hadamzick` | `Mag. Vivian Hadamzick` |

**Missed by this rule (FN):**

- `Pablo Ebling` (person)
- `Hugo Stegemann` (person)
- `Delila Ringsdorff` (person)
- `Nigel Conrades, Bakk. techn. BEd` (person)

**Example 23** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Dr. Marlon Richel, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Freimut & Assenov Sicherheit GmbH in Liqu, Spazgasse 41, 8524 Greim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 31.596,47 EUR und Feststellung (6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 18. Juni 2019, GZ 129 R 50/19z-21, mit dem das Urteil des Handelsgerichts Wien vom 28. März 2019, GZ 54 Cg 71/18x-17, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Marlon Richel` | `Dr. Marlon Richel` |

**Missed by this rule (FN):**

- `Freimut & Assenov Sicherheit GmbH` (organisation)
- `Spazgasse 41, 8524 Greim, Österreich` (address)

**Example 24** (doc_id: `deanon_TRAIN/10ObS150_17g`) (sent_id: `deanon_TRAIN/10ObS150_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Ing. Christian Stangl-Brachnik, MA BA und Mag. Claudia Gründel (beide aus dem Kreis der Arbeitgeber) als weitere Richter in der Sozialrechtssache der klagenden Partei OStR Esra Jakubait, vertreten durch Dr. Thomas Stampfer und Dr. Christoph Orgler, Rechtsanwälte in Graz, gegen die beklagte Partei Sozialversicherungsanstalt der Bauern, 1031 Wien, Ghegastraße 1, vertreten durch Dr. Michael Stögerer, Rechtsanwalt in Wien, wegen Ausgleichszulage, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2017, GZ 7 Rs 37/17s-11, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. April 2017, GZ 43 Cgs 113/17p-7, teils bestätigt und teils abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

| Predicted | Gold |
|---|---|
| `OStR Esra Jakubait` | `OStR Esra Jakubait` |

**Example 25** (doc_id: `deanon_TRAIN/10ObS92_17b`) (sent_id: `deanon_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Dr.in Gerlinde Saltzmann, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Gerlinde Saltzmann` | `Dr.in Gerlinde Saltzmann` |

**Example 26** (doc_id: `deanon_TRAIN/17Ob10_20z`) (sent_id: `deanon_TRAIN/17Ob10_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätinnen Mag. Malesich und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Levi Adelwart, vertreten durch Stephan Briem Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Dr. Penelope Piephans als Treuhänder der Insolvenzgläubiger der Valkraftfen-Analyse Aktiengesellschaft, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH in Linz, wegen Feststellung (Streitwert 18.335,66 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. März 2020, GZ 1 R 31/20i-13, womit das Urteil des Landesgerichts Linz vom 9. Dezember 2019, GZ 4 Cg 73/18z-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Penelope Piephans` | `Dr. Penelope Piephans` |

**Missed by this rule (FN):**

- `Levi Adelwart` (person)
- `Valkraftfen-Analyse Aktiengesellschaft` (organisation)

**Example 27** (doc_id: `deanon_TRAIN/18ONc1_21y`) (sent_id: `deanon_TRAIN/18ONc1_21y_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Senatspräsidenten Dr. Veith, die Hofräte Hon.-Prof. Dr. Höllwerth, Hon.-Prof. PD Dr. Rassi und Mag. Painsi als weitere Richter in der Schiedsrechtssache der Antragstellerin (schiedsbeklagte Partei) See-Versand Werke GmbH, Robert Leis, gegen die Antragsgegnerin (schiedsklagende Partei) Dargatz+Boedewig Telekom GmbH, ÖkR Nikolaus Buksbaum, vertreten durch Dr. Horst Pechar, Rechtsanwalt in Weiz, wegen § 602 ZPO, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der an den Obersten Gerichtshof gerichtete Antrag vom 7. 1. 2021 wird, soweit er sich an den Obersten Gerichtshof richtet, zurückgewiesen.

| Predicted | Gold |
|---|---|
| `ÖkR Nikolaus Buksbaum` | `ÖkR Nikolaus Buksbaum` |

**Missed by this rule (FN):**

- `See-Versand Werke GmbH` (organisation)
- `Robert Leis` (person)
- `Dargatz+Boedewig Telekom GmbH` (organisation)

**Example 28** (doc_id: `deanon_TRAIN/18ONc1_21y`) (sent_id: `deanon_TRAIN/18ONc1_21y_5`)


Daneben besteht das Schiedsgericht aus Mag. Verena Mikolassek als Vorsitzendem und Dr. Ingrid Enzensperger als weiterer Schiedsrichterin.

| Predicted | Gold |
|---|---|
| `Mag. Verena Mikolassek` | `Mag. Verena Mikolassek` |
| `Dr. Ingrid Enzensperger` | `Dr. Ingrid Enzensperger` |

**Example 29** (doc_id: `deanon_TRAIN/1Nc2_20i`) (sent_id: `deanon_TRAIN/1Nc2_20i_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie den Hofrat Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei KommR Franz Kubank, vertreten durch Dr. Michael Wukoschitz, Rechtsanwalt in Wien, gegen die beklagte Partei Laurin Aichhorn a.d., Timothy Schulmeister, Serbien, wegen 600 EUR sA, über den Ordinationsantrag nach § 28 JN den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

| Predicted | Gold |
|---|---|
| `KommR Franz Kubank` | `KommR Franz Kubank` |

**Missed by this rule (FN):**

- `Laurin Aichhorn` (person)
- `Timothy Schulmeister` (person)
- `Bezirksgericht Schwechat` (organisation)

**Example 30** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Dr. Alice Wickertsheimer, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Dr. Alice Wickertsheimer` | `Dr. Alice Wickertsheimer` |

**Example 31** (doc_id: `deanon_TRAIN/1Ob128_17f`) (sent_id: `deanon_TRAIN/1Ob128_17f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Familienrechtssache des Antragstellers Mag. Jeannette Scherl, vertreten durch die Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG, Wien, gegen die Antragsgegnerin Selina Dorfmeyer, vertreten durch Mag. Anna-Maria Freiberger, Rechtsanwältin in Wien, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 24. April 2017, GZ 45 R 66/17i, 67/17m-19, mit dem die Beschlüsse des Bezirksgerichts Liesing vom 4. Jänner 2017, GZ 7 Fam 30/16m-12, und vom 17. Jänner 2017, GZ 7 Fam 30/16m-14, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Jeannette Scherl` | `Mag. Jeannette Scherl` |

**Missed by this rule (FN):**

- `Selina Dorfmeyer` (person)

**Example 32** (doc_id: `deanon_TRAIN/1Ob12_21b`) (sent_id: `deanon_TRAIN/1Ob12_21b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Mag. Franziska Gonschorek, vertreten durch die Huber & Partner Rechtsanwälte GmbH, Linz, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `Mag. Franziska Gonschorek` | `Mag. Franziska Gonschorek` |

**Example 33** (doc_id: `deanon_TRAIN/1Ob142_19t`) (sent_id: `deanon_TRAIN/1Ob142_19t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der Antragstellerin Mag. Liu Cingöz, vertreten Dr. Brigitte Birnbaum und Dr. Rainer Toperczer, Rechtsanwälte in Wien, gegen den Antragsgegner Dr. Torsten Erlautzki, vertreten durch die Anwaltssocietät Sattlegger Dorninger Steiner & Partner OG, Linz, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse gemäß §§ 81 ff EheG, über die außerordentlichen Revisionsrekurse beider Parteien gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 9. Juli 2019, GZ 45 R 554/18f-162, mit dem der Beschluss des Bezirksgerichts Fünfhaus vom 25. Oktober 2018, GZ 4 Fam 68/14k-156, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Der Revisionsrekurs des Antragsgegners wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Torsten Erlautzki` | `Dr. Torsten Erlautzki` |

**Missed by this rule (FN):**

- `Mag. Liu Cingöz` (person)

**Example 34** (doc_id: `deanon_TRAIN/1Ob14_20w`) (sent_id: `deanon_TRAIN/1Ob14_20w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei VetR Amber Baraniak, Hong Kong, vertreten durch die Oblin Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Mag. Liliana Bößer, vertreten durch Dr. Karl Heinz Kramer M.A.S., Rechtsanwalt in Villach, wegen Aufhebung eines Kaufvertrags, 213.819,01 USD sA und 9.950,39 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 30. Oktober 2019, GZ 5 R 94/19m-210, mit dem das Urteil des Landesgerichts Klagenfurt vom 2. April 2019, GZ 25 Cg 122/12y-207, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `VetR Amber Baraniak` | `VetR Amber Baraniak` |

**Missed by this rule (FN):**

- `Mag. Liliana Bößer` (person)

**Example 35** (doc_id: `deanon_TRAIN/1Ob152_24w`) (sent_id: `deanon_TRAIN/1Ob152_24w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Musger als Vorsitzenden sowie die Hofrätin und die Hofräte Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei VetR Volkmar Acar KG, FN FN823951l, vertreten durch Dr. Eva-Maria Bachmann-Lang, Dr. Christian Bachmann, Rechtsanwälte in Wien, gegen die beklagte Partei „ Nemtschok Touristik “ Wilnorlex Werke gmbH, FN FN545761v, vertreten durch die GRAF ISOLA Rechtsanwälte GmbH in Wien, wegen 51.843,91 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 3. Juli 2024, GZ 1 R 17/24p-39, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `VetR Volkmar Acar` | `VetR Volkmar Acar` |

**Missed by this rule (FN):**

- `FN823951l` (business_register_number)
- `Nemtschok Touristik` (organisation)
- `Wilnorlex Werke gmbH` (organisation)
- `FN545761v` (business_register_number)

**Example 36** (doc_id: `deanon_TRAIN/1Ob179_12y`) (sent_id: `deanon_TRAIN/1Ob179_12y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Pflegschaftssache des mj Roy Boner, geboren am 13. Juli 2006, vertreten durch Mag. Heinz Wolfbauer, Rechtsanwalt in Wien, wegen Unterhalts, über den Revisionsrekurs des Vaters Dr. Jaroslaw Kellenbrink, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 29. Mai 2012, GZ 43 R 254/12i-106, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Döbling vom 28. März 2012, GZ 10 Pu 131/09b-100, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Jaroslaw Kellenbrink` | `Dr. Jaroslaw Kellenbrink` |

**Missed by this rule (FN):**

- `Roy Boner` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Karin Meiwaldt, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Katharina Tomandl, MA, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Mag. Ernst Michael Lang` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Karin Meiwaldt`(person)
- `Katharina Tomandl, MA`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Chen Mestwerdt, Slowenien, vertreten durch Mag. Erich Hierz, Rechtsanwalt in Graz, gegen die beklagte Partei Roman Eschenweck, Deutschland, vertreten durch Salleck + Partner Rechtsanwälte in Deutschland, wegen 5.856 EUR sA, 1.342 EUR sA und 915 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag, die Rechtssache gemäß § 28 JN einem österreichischem Gericht zuzuweisen, wird zurückgewiesen.

**False Positives:**

- `Mag. Erich Hierz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Chen Mestwerdt`(person)
- `Roman Eschenweck`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Sten und Stöwer Wind GmbH, OMedR Torsten Münchmeyer, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei OStR Gregor Ruemmel, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Mag. Alexander Rimser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Sten und Stöwer Wind GmbH`(organisation)
- `OMedR Torsten Münchmeyer`(person)
- `OStR Gregor Ruemmel`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei C. Dersudheim Digital GmbH, Taxlbergstraße 247, 8151 Rohrbach, Österreich, vertreten durch Dr. Carl Benkhofer, Rechtsanwalt in Wien, gegen die beklagte Partei Ingolf Grimpe, vertreten durch Greiml & Horwath Rechtsanwaltspartnerschaft in Graz, wegen 5.232 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 14 C 1302/11a des Bezirksgerichts Graz-West in nichtöffentlicher Sitzung, den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Graz-West das Bezirksgericht Fünfhaus bestimmt.

**False Positives:**

- `Dr. Carl Benkhofer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dersudheim Digital GmbH`(organisation)
- `Taxlbergstraße 247, 8151 Rohrbach, Österreich`(address)
- `Ingolf Grimpe`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Nc7_10a`) (sent_id: `deanon_TRAIN/10Nc7_10a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger und Hon.-Prof. Dr. Neumayr als weitere Richter in der Verlassenschaftssache nach dem am 9. September 2009 verstorbenen, zuletzt in Tschiggfreystraße 46, 3240 Loitsdorf, Österreich, wohnhaft gewesenen Manfred Johann Pingert, AZ 1 A 349/09w des Bezirksgerichts Kitzbühel, über den Delegierungsantrag der Karin Czychy, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, den B e s c h l u s s gefasst:  Spruch Dem Delegierungsantrag wird stattgegeben.

**False Positives:**

- `Mag. Maximilian Kocher` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Tschiggfreystraße 46, 3240 Loitsdorf, Österreich`(address)
- `Pingert`(person)
- `Czychy`(person)

**Example 5** (doc_id: `deanon_TRAIN/10Nc9_15b`) (sent_id: `deanon_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Mur Kraftalheim Holding GmbH, Gerald Zacharie, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Nexstein Textil GmbH, Dipl.-Ing. Lynn Forkarth, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

**False Positives:**

- `Dr. Roland Kassowitz` — no gold match — likely missing annotation
- `Ing. Lynn Forkarth` — partial — pred is substring of gold: `Dipl.-Ing. Lynn Forkarth`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgericht Linz`(organisation)
- `Mur Kraftalheim Holding GmbH`(organisation)
- `Gerald Zacharie`(person)
- `Nexstein Textil GmbH`(organisation)
- `Dipl.-Ing. Lynn Forkarth`(person)

**Example 6** (doc_id: `deanon_TRAIN/10Ob102_18z`) (sent_id: `deanon_TRAIN/10Ob102_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG, Adelheid Lochmaier, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Ursula Antoniadis, vertreten durch Knirsch – Braun – Fellner Rechtsanwälte in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 5. September 2018, GZ 40 R 39/18h-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mag. Franz Podovsovnik` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Skrzypczik + Duchscherer Digital AG`(organisation)
- `Adelheid Lochmaier`(person)
- `Ursula Antoniadis`(person)

**Example 7** (doc_id: `deanon_TRAIN/10Ob105_15m`) (sent_id: `deanon_TRAIN/10Ob105_15m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Alsteinost GmbH, Anna Kisaoglu, Bakk. iur., vertreten durch Dr. Erich Kafka und Dr. Manfred Palkovits, Rechtsanwälte in Wien, gegen die beklagte Partei Ing. Mag. Adam Kratki, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 11. Juni 2015, GZ 39 R 41/15s-29, in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch

**False Positives:**

- `Dr. Erich Kafka` — no gold match — likely missing annotation
- `Dr. Manfred Palkovits` — no gold match — likely missing annotation
- `Ing. Mag. Adam Kratki` — partial — gold is substring of pred: `Mag. Adam Kratki`

> overlaps gold: 1  |  likely missing annotation: 2

**Gold Entities:**

- `Alsteinost GmbH`(organisation)
- `Anna Kisaoglu, Bakk. iur.`(person)
- `Mag. Adam Kratki`(person)

**Example 8** (doc_id: `deanon_TRAIN/10Ob10_16t`) (sent_id: `deanon_TRAIN/10Ob10_16t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei DI Fabian Reifrath, vertreten durch Dr. Wilhelm Schlein Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Elina Woyte, vertreten durch Dr. Werner Goeritz, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 2. Dezember 2015, GZ 40 R 205/15s-34, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Wilhelm Schlein Rechtsanwalt Gmb` — no gold match — likely missing annotation
- `Dr. Werner Goeritz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `DI Fabian Reifrath`(person)
- `Elina Woyte`(person)

**Example 9** (doc_id: `deanon_TRAIN/10Ob10_18w`) (sent_id: `deanon_TRAIN/10Ob10_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Jonasgasse 71, 4760 Weeg, Österreich, vertreten durch Dr. Alois Schneider, Rechtsanwalt in Rattenberg, wider die beklagte Partei Corinna Elfe, vertreten durch Dr. Walter Hausberger, Dr. Katharina Moritz und Dr. Alfred Schmidt, Rechtsanwälte in Wörgl, wegen Entfernung und Unterlassung (Revisionsinteresse 10.000 EUR), infolge Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 3. November 2017, GZ 3 R 172/17s-22, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Rattenberg vom 17. Mai 2017, GZ 3 C 401/15k-18, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Alois Schneider` — no gold match — likely missing annotation
- `Dr. Walter Hausberger` — no gold match — likely missing annotation
- `Dr. Katharina Moritz` — no gold match — likely missing annotation
- `Dr. Alfred Schmidt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 4

**Gold Entities:**

- `Jonasgasse 71, 4760 Weeg, Österreich`(address)
- `Corinna Elfe`(person)

**Example 10** (doc_id: `deanon_TRAIN/10Ob11_15p`) (sent_id: `deanon_TRAIN/10Ob11_15p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte und Hofrätinnen Univ.-Prof. Dr. Neumayr, Dr. Schramm, Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Viktoria Hornburg, vertreten durch Dr. Walter Vasoll und Mag. Marion Vasoll, Rechtsanwälte in Hermagor, gegen die beklagte Partei Mercedes Jungschlaeger, vertreten durch Dr. Thomas Romauch, Rechtsanwalt in Wien, wegen Feststellung und Einwilligung (6.000 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 4. Dezember 2014, GZ 3 R 169/14h-14, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Hermagor vom 9. August 2014, GZ 1 C 563/13b-10, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision der beklagten Partei wird zurückgewiesen.

**False Positives:**

- `Dr. Walter Vasoll` — no gold match — likely missing annotation
- `Mag. Marion Vasoll` — no gold match — likely missing annotation
- `Dr. Thomas Romauch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Gold Entities:**

- `Viktoria Hornburg`(person)
- `Mercedes Jungschlaeger`(person)

**Example 11** (doc_id: `deanon_TRAIN/10Ob13_20i`) (sent_id: `deanon_TRAIN/10Ob13_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Miranda Klagemann, vertreten durch Dr. Andreas Ladstätter, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. DI Adolf Kowallek, und 2. Ing. Janis Grottian, beide vertreten durch Dr. Walter Schuhmeister und Mag. Franz Haydn, Rechtsanwälte in Schwechat, wegen 15.000 EUR sA, infolge Revision der beklagten Parteien (Revisionsinteresse 6.250 EUR) gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 30. Jänner 2019, GZ 34 R 66/18k-27, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Innere Stadt Wien vom 23. März 2018, GZ 37 C 780/16f-18, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Andreas Ladst` — no gold match — likely missing annotation
- `Dr. Walter Schuhmeister` — no gold match — likely missing annotation
- `Mag. Franz Haydn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Gold Entities:**

- `Miranda Klagemann`(person)
- `DI Adolf Kowallek`(person)
- `Ing. Janis Grottian`(person)

**Example 12** (doc_id: `deanon_TRAIN/10Ob16_14x`) (sent_id: `deanon_TRAIN/10Ob16_14x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Walter Gritzmacher, vertreten durch Dr. Birgit Lajtai-Nagl, Rechtsanwältin in Villach, gegen die beklagte Partei Dr. Ariadne Graspointner, vertreten durch Dr. Robert Kugler, Rechtsanwalt in Klagenfurt, wegen Unterhalts, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 27. November 2013, GZ 2 R 234/13h-116, womit das Urteil des Bezirksgerichts Villach vom 27. August 2013, GZ 3 C 144/06w-109, abgeändert wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Dr. Birgit Lajtai` — no gold match — likely missing annotation
- `Dr. Robert Kugler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Walter Gritzmacher`(person)
- `Dr. Ariadne Graspointner`(person)

**Example 13** (doc_id: `deanon_TRAIN/10Ob16_16z`) (sent_id: `deanon_TRAIN/10Ob16_16z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Josepha Mikolajetz, vertreten durch Dr. Clemens Lintschinger, Rechtsanwalt in Wien, gegen die beklagte Partei Erhard Arslanboga, vertreten durch Mag. Dr. Georg Backhausen, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 27. Jänner 2016, GZ 38 R 265/15z-45, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Clemens Lintschinger` — no gold match — likely missing annotation
- `Mag. Dr. Georg Backhausen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Josepha Mikolajetz`(person)
- `Erhard Arslanboga`(person)

**Example 14** (doc_id: `deanon_TRAIN/10Ob18_13i`) (sent_id: `deanon_TRAIN/10Ob18_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Verein für Konsumenteninformation, 1061 Wien, Linke Wienzeile 18, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Monsud-Textil GmbH, VetR Herbert Dedert, vertreten durch Kraft & Winternitz Rechtsanwälte GmbH in Wien, wegen (restlichen) 1.479,20 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 15. Jänner 2013, GZ 1 R 270/12w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Dr. Walter Reichholf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Monsud-Textil GmbH`(organisation)
- `VetR Herbert Dedert`(person)

**Example 15** (doc_id: `deanon_TRAIN/10Ob23_15b`) (sent_id: `deanon_TRAIN/10Ob23_15b_4`)


Steintra Solar GmbH, Kospachstraße 35, 3162 Rainfeld, Österreich, vertreten durch Dr. Paul Vavrovsky und Mag. Christian Schrott, Rechtsanwälte in Salzburg, 2. Umwelt Dorfwald ges.m.b.H., Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich, vertreten durch Dr. Katharina Sedlazeck-Gschaider, Rechtsanwältin in Salzburg, wegen 11.921,56 EUR sA und Feststellung (Streitwert 5.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 27. Jänner 2015, GZ 11 R 14/14d-34, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Paul Vavrovsky` — no gold match — likely missing annotation
- `Mag. Christian Schrott` — no gold match — likely missing annotation
- `Dr. Katharina Sedlazeck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Gold Entities:**

- `Steintra Solar GmbH`(organisation)
- `Kospachstraße 35, 3162 Rainfeld, Österreich`(address)
- `Umwelt Dorfwald ges.m.b.H.`(organisation)
- `Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich`(address)

**Example 16** (doc_id: `deanon_TRAIN/10Ob23_18g`) (sent_id: `deanon_TRAIN/10Ob23_18g_4`)


Severin Simaitis, geboren 20. November 2002, 2. 8. Juli 1967, geboren 17. November 2004, und 3. Nepomuk Sprinzl, geboren 11. September 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Miklos Stiening, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Mag. Florian Kucera` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Severin Simaitis`(person)
- `20. November`(date)
- `8. Juli 1967`(date)
- `17. November`(date)
- `Nepomuk Sprinzl`(person)
- `11. September`(date)
- `Mag. Miklos Stiening`(person)

**Example 17** (doc_id: `deanon_TRAIN/10Ob26_10m`) (sent_id: `deanon_TRAIN/10Ob26_10m_4`)


Silvester Boetefuer, geboren am 12. Juli 1994, 2.) Annika Blumenstock, geboren am 28. Dezember 1998, und 3.) Lars Betschel, geboren am 3. Juli 2003, alle vertreten durch das Land Wien als Jugendwohlfahrtsträger (Amt für Jugend und Familie - Rechtsfürsorge Bezirke 17., 18. und 19., 1190 Wien, Gatterburggasse 12-14), wegen Unterhaltsvorschuss, über den „außerordentlichen Revisionsrekurs“ des Vaters Mag. Anton Brockschnieder, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. April 2009, GZ 44 R 193/08w-U140, womit der als Zulassungsvorstellung zu wertende „außerordentliche Revisionsrekurs“ des Vaters zurückgewiesen wurde, den Beschluss gefasst:  Spruch Der „außerordentliche Revisionsrekurs“ wird zurückgewiesen.

**False Positives:**

- `Mag. Anton Brockschnieder` — partial — gold is substring of pred: `Brockschnieder`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Boetefuer`(person)
- `Blumenstock`(person)
- `Betschel`(person)
- `Brockschnieder`(person)

**Example 18** (doc_id: `deanon_TRAIN/10Ob2_14p`) (sent_id: `deanon_TRAIN/10Ob2_14p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der mj Calvin Mützlaff, geboren am Volker Scheffski, Jaden Jurkutaitis, geboren am 8. Dezember 1982 und PhD Karim Trieber, geboren am 11. Januar 1975, in Pflege und Erziehung der Mutter StR Lara Jungnikl, vertreten durch das Land Vorarlberg als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Feldkirch, Schlossgraben 1, 6800 Feldkirch), wegen Gewährung von Unterhaltsvorschuss, über den Revisionsrekurs des Vaters RgR Dipl.-Ing. Quirin Bagemühl, vertreten durch Mag. Hans-Christian Obernberger, Rechtsanwalt in Feldkirch, gegen den Beschluss des Landesgerichts Feldkirch als Rekursgericht vom 12. Juli 2011, GZ 3 R 198/11g, 3 R 199/11d, 3 R 200/11a-18, womit die Beschlüsse des Bezirksgerichts Feldkirch vom 18. Mai 2011, GZ 12 Pu 141/11f-4 bis 6, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Ing. Quirin Bagem` — partial — pred is substring of gold: `RgR Dipl.-Ing. Quirin Bagemühl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Calvin Mützlaff`(person)
- `Volker Scheffski`(person)
- `Jaden Jurkutaitis`(person)
- `8. Dezember 1982`(date)
- `PhD Karim Trieber`(person)
- `11. Januar 1975`(date)
- `StR Lara Jungnikl`(person)
- `RgR Dipl.-Ing. Quirin Bagemühl`(person)

**Example 19** (doc_id: `deanon_TRAIN/10Ob2_22z`) (sent_id: `deanon_TRAIN/10Ob2_22z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Calvin Amorelli, vertreten durch Dr. Martin Hembach, Rechtsanwalt in Wiener Neustadt, gegen die beklagte Partei Strathewerd u. Niemetz Metall GmbH, Dolores Chatzakis, vertreten durch Mag. Martin Trapichler, Rechtsanwalt in Wien, wegen 13.639,20 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 25. Oktober 2021, GZ 18 R 67/21p-16, mit dem das Urteil des Bezirksgerichts Wiener Neustadt vom 7. Juni 2021, GZ 7 C 117/21b-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Martin Hembach` — no gold match — likely missing annotation
- `Mag. Martin Trapichler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Calvin Amorelli`(person)
- `Strathewerd u. Niemetz Metall GmbH`(organisation)
- `Dolores Chatzakis`(person)

**Example 20** (doc_id: `deanon_TRAIN/10Ob38_25y`) (sent_id: `deanon_TRAIN/10Ob38_25y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofräte Dr. Annerl und Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Rechtssache der klagenden Partei Arielle Schallmair, gegen die beklagte Partei Dr. Daisy Nagelkrämer, vertreten durch Ing. Dr. Stefan Krall und Dr. Oliver Kühnl, Rechtsanwälte in Innsbruck, wegen 9.456 EUR sA (Revisionsinteresse 9.268,50 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 25. Februar 2025, GZ 21 R 434/24f-29, mit dem das Urteil des Bezirksgerichts Seekirchen am Wallersee vom 5. September 2024, GZ 2 C 1107/23d-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Dr. Daisy Nagelkr` — partial — pred is substring of gold: `Dr. Daisy Nagelkrämer`
- `Ing. Dr. Stefan Krall` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Arielle Schallmair`(person)
- `Dr. Daisy Nagelkrämer`(person)

**Example 21** (doc_id: `deanon_TRAIN/10Ob3_12g`) (sent_id: `deanon_TRAIN/10Ob3_12g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Helge Monhemius, Bakk. techn., vertreten durch Dr. Georg Gorton und DDr. Birgit Gorton, Rechtsanwälte in Klagenfurt, gegen die beklagte Partei Ing. Eugenia Welze, vertreten durch Dr. Gottfried Kassin, Rechtsanwalt in St. Veit an der Glan, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 26. Mai 2011, GZ 2 R 83/11z-49, mit dem das Urteil des Bezirksgerichts St. Veit an der Glan vom 29. Oktober 2010, GZ 3 C 333/09h-34, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Georg Gorton` — no gold match — likely missing annotation
- `Dr. Gottfried Kassin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Helge Monhemius, Bakk. techn.`(person)
- `Ing. Eugenia Welze`(person)

**Example 22** (doc_id: `deanon_TRAIN/10Ob41_14y`) (sent_id: `deanon_TRAIN/10Ob41_14y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in den verbundenen Familienrechtssachen des Antragstellers DI Dr. Jakob Krägeloh, geboren am 9. Juli 2019, vertreten durch Mag. Werner Thurner, Rechtsanwalt in Graz, gegen die Antragsgegnerinnen 1.

**False Positives:**

- `Dr. Jakob Kr` — partial — pred is substring of gold: `Dr. Jakob Krägeloh`
- `Mag. Werner Thurner` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Jakob Krägeloh`(person)
- `9. Juli 2019`(date)

**Example 23** (doc_id: `deanon_TRAIN/10Ob57_13z`) (sent_id: `deanon_TRAIN/10Ob57_13z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der Kinder Pablo Ebling, geboren am 9. August 1991, Hugo Stegemann, geboren am 30. September 1992, mj Delila Ringsdorff, geboren am 22. Dezember 1998 und mj Nigel Conrades, Bakk. techn. BEd, geboren am 18. Jänner 2001, wegen Unterhaltsvorschuss, infolge Revisionsrekurses des Vaters Mag. Vivian Hadamzick, vertreten durch Mag. Roland Marko, Rechtsanwalt in Wien, dieser vertreten durch Dr. Francisco Rumpf, Rechtsanwalt in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 7. Juni 2013, GZ 43 R 391/08f ua -U-458, womit der Beschluss des Bezirksgerichts Innere Stadt Wien vom 12. November 2007, GZ 2 P 88/07t-U-238, abgeändert wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Mag. Roland Marko` — no gold match — likely missing annotation
- `Dr. Francisco Rumpf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Pablo Ebling`(person)
- `Hugo Stegemann`(person)
- `Delila Ringsdorff`(person)
- `Nigel Conrades, Bakk. techn. BEd`(person)
- `Mag. Vivian Hadamzick`(person)

**Example 24** (doc_id: `deanon_TRAIN/10Ob57_13z`) (sent_id: `deanon_TRAIN/10Ob57_13z_10`)


8. 2009 zuerkannte, und zwar in Höhe von (jeweils) 80 EUR monatlich für MedR Ing. Anneliese Eberschulz und Tristan Swirbul, von 70 EUR monatlich für Wendy Remmy und von 60 EUR für Serena Christodoulidou.

**False Positives:**

- `Ing. Anneliese Eberschulz` — partial — pred is substring of gold: `MedR Ing. Anneliese Eberschulz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MedR Ing. Anneliese Eberschulz`(person)
- `Tristan Swirbul`(person)
- `Wendy Remmy`(person)
- `Serena Christodoulidou`(person)

**Example 25** (doc_id: `deanon_TRAIN/10ObS150_17g`) (sent_id: `deanon_TRAIN/10ObS150_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Ing. Christian Stangl-Brachnik, MA BA und Mag. Claudia Gründel (beide aus dem Kreis der Arbeitgeber) als weitere Richter in der Sozialrechtssache der klagenden Partei OStR Esra Jakubait, vertreten durch Dr. Thomas Stampfer und Dr. Christoph Orgler, Rechtsanwälte in Graz, gegen die beklagte Partei Sozialversicherungsanstalt der Bauern, 1031 Wien, Ghegastraße 1, vertreten durch Dr. Michael Stögerer, Rechtsanwalt in Wien, wegen Ausgleichszulage, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2017, GZ 7 Rs 37/17s-11, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. April 2017, GZ 43 Cgs 113/17p-7, teils bestätigt und teils abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Ing. Christian Stangl` — no gold match — likely missing annotation
- `Mag. Claudia Gr` — no gold match — likely missing annotation
- `Dr. Thomas Stampfer` — no gold match — likely missing annotation
- `Dr. Christoph Orgler` — no gold match — likely missing annotation
- `Dr. Michael St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 5

**Gold Entities:**

- `OStR Esra Jakubait`(person)

**Example 26** (doc_id: `deanon_TRAIN/10ObS21_10a`) (sent_id: `deanon_TRAIN/10ObS21_10a_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Schinko als Vorsitzenden, die Hofräte Dr. Fellinger und Dr. Hoch sowie die fachkundigen Laienrichter Mag. Irene Kienzl (aus dem Kreis der Arbeitgeber) und Eva-Maria Florianschütz (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Gertrud Johanna Ostrovska, gegen die beklagte Partei Steiermärkische Gebietskrankenkasse, 8011 Graz, Josef-Pongratz-Platz 1, vertreten durch Das Haus des Rechts Rechtsanwälte Destaller-Mader in Graz, wegen Kostenübernahme, infolge Rekurses der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 19. November 2009, GZ 8 Rs 73/09f-10, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 1. September 2009, GZ 29 Cgs 90/09s-6, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Mag. Irene Kienzl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ostrovska`(person)

**Example 27** (doc_id: `deanon_TRAIN/10ObS21_10a`) (sent_id: `deanon_TRAIN/10ObS21_10a_6`)


Sie suchte Dr. Thomas Poettgen, Facharzt für Orthopädie in Graz, auf, der ihr das Medikament Voltaren sowie eine Physiotherapie verschrieb.

**False Positives:**

- `Dr. Thomas Poettgen` — partial — gold is substring of pred: `Poettgen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Poettgen`(person)

**Example 28** (doc_id: `deanon_TRAIN/10ObS21_10a`) (sent_id: `deanon_TRAIN/10ObS21_10a_11`)


2. 2009 von Dr. Thomas Pawlowitsch, Facharzt für Orthopädie in Graz, verordnete Präparat „Hyalgan SprAmp 2 ml 5 St“ habe.

**False Positives:**

- `Dr. Thomas Pawlowitsch` — partial — gold is substring of pred: `Pawlowitsch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Pawlowitsch`(person)

**Example 29** (doc_id: `deanon_TRAIN/10ObS21_10a`) (sent_id: `deanon_TRAIN/10ObS21_10a_137`)


2. 2009 von Dr. Thomas Pavelec, Facharzt für Orthopädie in Graz, verordnete Präparat „Hyalgan SprAmp 2 ml 5 St“ zu Recht bestehe.

**False Positives:**

- `Dr. Thomas Pavelec` — partial — gold is substring of pred: `Pavelec`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Pavelec`(person)

**Example 30** (doc_id: `deanon_TRAIN/10ObS92_17b`) (sent_id: `deanon_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Dr.in Gerlinde Saltzmann, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Dr. Gabriele Griehsel` — no gold match — likely missing annotation
- `Dr. Wolfgang Kozak` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Dr.in Gerlinde Saltzmann`(person)

**Example 31** (doc_id: `deanon_TRAIN/10ObS92_17b`) (sent_id: `deanon_TRAIN/10ObS92_17b_28`)


11. 2015 im Herz Jesu Heim in Dr. Rudolf Haberleitner-Straße 13, 4230 Pregarten, Österreich als „Hilfsarbeiterin“ beschäftigt gewesen sei, sei Ergebnis einer unbedenklichen Beweiswürdigung.

**False Positives:**

- `Dr. Rudolf Haberleitner` — partial — pred is substring of gold: `Dr. Rudolf Haberleitner-Straße 13, 4230 Pregarten, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Rudolf Haberleitner-Straße 13, 4230 Pregarten, Österreich`(address)

**Example 32** (doc_id: `deanon_TRAIN/11Ns41_20y`) (sent_id: `deanon_TRAIN/11Ns41_20y_3`)


Kopf Der Oberste Gerichtshof hat am 24. Februar 2021 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie die Vizepräsidentin des Obersten Gerichtshofs Mag. Marek, den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer, die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski und den Hofrat des Obersten Gerichtshofs Dr. Oberressl als weitere Richter im Verfahren zur Unterbringung des Mag. Herwig Beerbohm in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB, AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, über den Antrag des Genannten auf Gewährung von Verfahrenshilfe nach Einsichtnahme der Generalprokuratur in die Akten nichtöffentlich (§ 62 Abs 1 zweiter Satz OGH-Geo 2019) den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Mag. Herwig Beerbohm` — partial — gold is substring of pred: `Beerbohm`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Beerbohm`(person)

**Example 33** (doc_id: `deanon_TRAIN/11Ns41_20y`) (sent_id: `deanon_TRAIN/11Ns41_20y_4`)


Text Gründe: [1] Mit Beschluss des Obersten Gerichtshofs vom 8. Mai 2020, AZ 11 Os 18/20m, wurde ein auf das Verfahren AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien bezogener Antrag des Mag. Herwig Balnuß auf Erneuerung des Strafverfahrens zurückgewiesen.

**False Positives:**

- `Mag. Herwig Balnu` — positional overlap with gold: `Balnuß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Balnuß`(person)

**Example 34** (doc_id: `deanon_TRAIN/12Ns17_13s`) (sent_id: `deanon_TRAIN/12Ns17_13s_3`)


Kopf Der Oberste Gerichtshof hat am 11. April 2013 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Viktorin als Schriftführer in der Strafsache gegen Andre Raszka und weitere Angeklagte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 2 zweiter Fall StGB und anderer strafbarer Handlungen, AZ 49 Hv 69/09f des Landesgerichts Wiener Neustadt, über die Anzeige der möglichen Ausgeschlossenheit der Hofrätin des Obersten Gerichtshofs Mag. Michel in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Hofrätin des Obersten Gerichtshofs Mag. Michel ist von der Entscheidung über die Nichtigkeitsbeschwerden und die Berufungen der Angeklagten Andre Rautenkrantz, Mag. Johann Klössel, Mag. Kurt Stoliarov und Dr. Bernhard Holtzhäuser sowie über den Antrag des Angeklagten Mag. Kurt Schromm auf Wiedereinsetzung in den vorigen Stand nicht ausgeschlossen.

**False Positives:**

- `Mag. Johann Kl` — positional overlap with gold: `Klössel`
- `Mag. Kurt Stoliarov` — partial — gold is substring of pred: `Stoliarov`
- `Dr. Bernhard Holtzh` — positional overlap with gold: `Holtzhäuser`
- `Mag. Kurt Schromm` — partial — gold is substring of pred: `Schromm`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Raszka`(person)
- `Rautenkrantz`(person)
- `Klössel`(person)
- `Stoliarov`(person)
- `Holtzhäuser`(person)
- `Schromm`(person)

**Example 35** (doc_id: `deanon_TRAIN/12Ns17_13s`) (sent_id: `deanon_TRAIN/12Ns17_13s_4`)


Text Gründe: Der Oberste Gerichtshof hat zu AZ 12 Os 117/12s, 12 Os 118/12p über den Antrag des Angeklagten Mag. Kurt Schelm auf Wiedereinsetzung in den vorigen Stand gegen die Versäumung der Frist zur Ausführung eines Rechtsmittels sowie über die Nichtigkeitsbeschwerden und die Berufungen der Angeklagten Andre Rogger, Mag. Johann Kiesler, Mag. Kurt Schwamm und Dr. Bernhard Havkost gegen das Urteil des Landesgerichts Wiener Neustadt als Schöffengericht vom 21. Juni 2011, GZ 49 Hv 69/09f-938, zu entscheiden.

**False Positives:**

- `Mag. Kurt Schelm` — partial — gold is substring of pred: `Schelm`
- `Mag. Johann Kiesler` — partial — gold is substring of pred: `Kiesler`
- `Mag. Kurt Schwamm` — partial — gold is substring of pred: `Schwamm`
- `Dr. Bernhard Havkost` — partial — gold is substring of pred: `Havkost`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Schelm`(person)
- `Rogger`(person)
- `Kiesler`(person)
- `Schwamm`(person)
- `Havkost`(person)

**Example 36** (doc_id: `deanon_TRAIN/12Ns17_13s`) (sent_id: `deanon_TRAIN/12Ns17_13s_7`)


Diese zeigte ihre allfällige Ausgeschlossenheit an, weil sie mit dem (nach Einstellung des gegen ihn geführten Ermittlungsverfahrens) in der Hauptverhandlung als Zeugen vernommenen Dr. Gottwald Kr Valerian Hrabal eng befreundet sei.

**False Positives:**

- `Dr. Gottwald Kr Valerian Hrabal` — partial — gold is substring of pred: `Valerian Hrabal`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Valerian Hrabal`(person)

**Example 37** (doc_id: `deanon_TRAIN/12Ns17_13s`) (sent_id: `deanon_TRAIN/12Ns17_13s_9`)


Zwar können aus dieser Generalklausel persönliche Beziehungen des Richters zu einer Beweisperson beachtlich sein, doch ist vom Obersten Gerichtshof die Glaubwürdigkeit des Zeugen Dr. Kr Svenja Siliacks nicht zu beurteilen, weshalb die Freundschaft der Hofrätin des Obersten Gerichtshofs Mag. Michel mit dem Zeugen nicht geeignet ist, bei einem verständig würdigenden objektiven Beurteiler naheliegende Zweifel an der unvoreingenommenen und unparteilichen Dienstverrichtung zu wecken (vglLässig, WK-StPO § 43 Rz 10 f; RIS-Justiz RS0045935).

**False Positives:**

- `Dr. Kr Svenja Siliacks` — partial — gold is substring of pred: `Svenja Siliacks`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Svenja Siliacks`(person)

**Example 38** (doc_id: `deanon_TRAIN/12Ns18_20y`) (sent_id: `deanon_TRAIN/12Ns18_20y_3`)


Kopf Der Oberste Gerichtshof hat am 18. März 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski im Verfahren zur Unterbringung des Mag. Herwig Bellingrath in einer Anstalt für geistig abnorme Rechtsbrecher nach § 21 Abs 1 StGB, AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit des Senatspräsidenten des Obersten Gerichtshofs Dr. Schwab und der Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Mag. Fürnkranz gemäß § 62 Abs 1 zweiter Satz OGH-Geo 2019 den Beschluss gefasst:  Spruch Senatspräsident des Obersten Gerichtshofs Dr. Schwab und die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger sowie Mag. Fürnkranz sind von der Entscheidung über die Anträge des Mag. Herwig Birnstiel auf Erneuerung des Strafverfahrens AZ 22 Hv 7/18k des Landesgerichts für Strafsachen Wien, ausgeschlossen.

**False Positives:**

- `Mag. Herwig Bellingrath` — partial — gold is substring of pred: `Bellingrath`
- `Mag. Herwig Birnstiel` — partial — gold is substring of pred: `Birnstiel`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bellingrath`(person)
- `Birnstiel`(person)

**Example 39** (doc_id: `deanon_TRAIN/12Ns18_20y`) (sent_id: `deanon_TRAIN/12Ns18_20y_8`)


Der vorliegende Antrag des Mag. Herwig Busskamp bezieht sich auf das Urteil des Oberlandesgerichts Wien vom 21. August 2019, AZ 17 Bs 168/19h, mit dem der Berufung des Betroffenen gegen das Urteil des Landesgerichts für Strafsachen Wien vom 14. November 2018, GZ 22 Hv 7/18k-350, nicht Folge gegeben wurde.

**False Positives:**

- `Mag. Herwig Busskamp` — partial — gold is substring of pred: `Busskamp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Busskamp`(person)

**Example 40** (doc_id: `deanon_TRAIN/12Ns22_16f`) (sent_id: `deanon_TRAIN/12Ns22_16f_9`)


An der angefochtenen Entscheidung des Oberlandesgerichts Wien hat die mit ihm in einem Angehörigenverhältnis im Sinne des § 72 StGB stehende Senatspräsidentin des Oberlandesgerichts Dr. Christine Schwab als Richterin mitgewirkt.

**False Positives:**

- `Dr. Christine Schwab` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_TRAIN/12Ns34_18y`) (sent_id: `deanon_TRAIN/12Ns34_18y_4`)


2005 den Beschluss gefasst:  Spruch Vizepräsidentin des Obersten Gerichtshofs Mag. Marek ist von der Entscheidung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Dr. Tilo Bräutigam sowie über die Berufungen der Staatsanwaltschaft und der Privatbeteiligten Hoch Seefurtlem GmbH gegen das Urteil des Landesgerichts Klagenfurt als Schöffengericht vom 30. Juni 2017, GZ 72 Hv 8/17g-80, ausgeschlossen.

**False Positives:**

- `Dr. Tilo Br` — positional overlap with gold: `Bräutigam`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bräutigam`(person)
- `Hoch Seefurtlem GmbH`(organisation)

**Example 42** (doc_id: `deanon_TRAIN/12Ns4_15g`) (sent_id: `deanon_TRAIN/12Ns4_15g_9`)


1. Senatspräsident des Obersten Gerichtshofs Dr. Schwab zeigt seine Ausgeschlossenheit unter Hinweis auf die (Vor-)Entscheidung des Obersten Gerichtshofs vom 8. August 2013, GZ 12 Ns 48/13z-3, sowie den Umstand an, dass er mit Senatspräsidentin des Oberlandesgerichts Wien Dr. Christine Schwab, die an mehreren (vom Anzeiger im einzelnen bezeichneten) früheren Entscheidungen dieses Gerichts in dieser Sache mit Bezug auf die Prüfung des Tatverdachts teilgenommen hat, im Angehörigenverhältnis des § 72 StGB stehe.

**False Positives:**

- `Dr. Christine Schwab` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_TRAIN/12Ns61_19w`) (sent_id: `deanon_TRAIN/12Ns61_19w_3`)


Kopf Der Oberste Gerichtshof hat am 24. September 2019 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari und die Hofrätin des Obersten Gerichtshofs Dr. Michel-Kwapinski in der Strafsache gegen Dr. Harald Weichard und einen anderen Angeklagten wegen des Verbrechens der Untreue nach § 153 Abs 1 und 3 zweiter Fall StGB, AZ 121 Hv 19/16z des Landesgerichts für Strafsachen Wien, über die Anzeige der Ausgeschlossenheit der Vizepräsidentin des Obersten Gerichtshofs Mag. Marek gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Dr. Harald Weichard` — partial — gold is substring of pred: `Weichard`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Weichard`(person)

**Example 44** (doc_id: `deanon_TRAIN/12Ns61_19w`) (sent_id: `deanon_TRAIN/12Ns61_19w_4`)


2005 den Beschluss gefasst:  Spruch Vizepräsidentin des Obersten Gerichtshofs Mag. Marek ist von der Entscheidung über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten Dr. Harald Wallbrecht gegen das Urteil des Landesgerichts für Strafsachen Wien als Schöffengericht vom 1. August 2018, GZ 121 Hv 19/16z-857, ausgeschlossen.

**False Positives:**

- `Dr. Harald Wallbrecht` — partial — gold is substring of pred: `Wallbrecht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wallbrecht`(person)

**Example 45** (doc_id: `deanon_TRAIN/12Os202_10p`) (sent_id: `deanon_TRAIN/12Os202_10p_3`)


Kopf Der Oberste Gerichtshof hat am 3. Februar 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Schroll als Vorsitzenden sowie durch den Hofrat des Obersten Gerichtshofs Dr. T. Solé und die Hofrätin des Obersten Gerichtshofs Dr. Bachner-Foregger als weitere Richter in Gegenwart der Richteramtsanwärterin Mag. Bergmann als Schriftführerin in der Strafsache gegen Mag. Herwig Botzong wegen der Verbrechen der Verleumdung nach § 297 Abs 1 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 24 Hv 46/10k des Landesgerichts Linz, über die Grundrechtsbeschwerden des Genannten gegen den Beschluss des Oberlandesgerichts Linz vom 29. November 2010, AZ 8 Bs 402/10i, nach Einsichtnahme durch die Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Grundrechtsbeschwerden werden zurückgewiesen.

**False Positives:**

- `Mag. Herwig Botzong` — partial — gold is substring of pred: `Botzong`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Botzong`(person)

**Example 46** (doc_id: `deanon_TRAIN/12Os202_10p`) (sent_id: `deanon_TRAIN/12Os202_10p_4`)


Text Gründe: In dem gegen Mag. Herwig Booth wegen der Verbrechen der Verleumdung nach § 297 Abs 1 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 24 Hv 46/10k des Landesgerichts Linz, geführten Strafverfahren befindet sich der Genannte seit 5. November 2009 in Untersuchungshaft.

**False Positives:**

- `Mag. Herwig Booth` — partial — gold is substring of pred: `Booth`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Booth`(person)

**Example 47** (doc_id: `deanon_TRAIN/12Os202_10p`) (sent_id: `deanon_TRAIN/12Os202_10p_6`)


Mit dem angefochtenen Beschluss gab das Oberlandesgericht Linz einer Beschwerde von Mag. Herwig Brückbauer gegen die am 11. November 2010 beschlossene Fortsetzung (ON 1134) der Untersuchungshaft nicht Folge und setzte diese aus dem Haftgrund der Tatbegehungsgefahr nach § 173 Abs 2 Z 3 lit a, lit b und lit c StPO fort.

**False Positives:**

- `Mag. Herwig Br` — positional overlap with gold: `Brückbauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Brückbauer`(person)

**Example 48** (doc_id: `deanon_TRAIN/12Os202_10p`) (sent_id: `deanon_TRAIN/12Os202_10p_7`)


Rechtliche Beurteilung Gegen diese Entscheidung richten sich die rechtzeitig erhobenen, von Mag. Thobias Boßer handschriftlich in überwiegend grob unsachlicher Diktion verfassten Grundrechtsbeschwerden vom 15. Dezember 2010, die fristgerecht mit Schriftsatz seines Verteidigers gemeinsam eingebracht wurden.

**False Positives:**

- `Mag. Thobias Bo` — partial — pred is substring of gold: `Mag. Thobias Boßer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Thobias Boßer`(person)

**Example 49** (doc_id: `deanon_TRAIN/12Os34_19w`) (sent_id: `deanon_TRAIN/12Os34_19w_3`)


Kopf Der Oberste Gerichtshof hat am 20. Jänner 2020 durch den Hofrat des Obersten Gerichtshofs Dr. Oshidari als Vorsitzenden, den Senatspräsidenten des Obersten Gerichtshofs Dr. Solé und durch die Hofrätinnen des Obersten Gerichtshofs Dr. Michel-Kwapinski, Dr. Brenner und Dr. Setz-Hummel in Gegenwart des Schriftführers Mag. Hauer in der Strafsache gegen Viktor Mattheiß und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und Abs 3 zweiter Fall StGB, AZ 352 HR 214/11x des Landesgerichts für Strafsachen Wien, über den Antrag des Dr. Stefan Tiepoldt auf Erneuerung des Strafverfahrens gemäß § 363a StPO in Ansehung des Beschlusses des Oberlandesgerichts Wien vom 28. August 2018, AZ 20 Bs 199/18p, nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Dr. Stefan Tiepoldt` — partial — gold is substring of pred: `Tiepoldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mattheiß`(person)
- `Tiepoldt`(person)

**Example 50** (doc_id: `deanon_TRAIN/12Os34_19w`) (sent_id: `deanon_TRAIN/12Os34_19w_4`)


Text Gründe: Im Ermittlungsverfahren gegen Viktor Mittermair und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und 3 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 703 St 3/11t (nunmehr AZ 713 St 24/18i) der Staatsanwaltschaft Wien, stellte der Beschuldigte Dr. Stefan Tolmin mit Schriftsatz vom 29. November 2017 – soweit im Folgenden von Relevanz – den Antrag auf Einstellung des Ermittlungsverfahrens „gemäß § 108 StPO“ (ON 558), welchen das Landesgericht für Strafsachen Wien mit Beschluss vom 22. Juni 2018, AZ 352 HR 214/11x, abwies (ON 644).

**False Positives:**

- `Dr. Stefan Tolmin` — partial — gold is substring of pred: `Tolmin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mittermair`(person)
- `Tolmin`(person)

**Example 51** (doc_id: `deanon_TRAIN/12Os34_19w`) (sent_id: `deanon_TRAIN/12Os34_19w_6`)


Rechtliche Beurteilung Gegen diesen Beschluss des Oberlandesgerichts Wien richtet sich der – nicht auf ein Erkenntnis des Europäischen Gerichtshofs für Menschenrechte (EGMR) gestützte – (rechtzeitige) Antrag des Beschuldigten Dr. Stefan Tokarski auf Erneuerung des Strafverfahrens gemäß § 363a StPO per analogiam, mit welchem dieser einen „Verstoß gegen Art 6 und 8 EMRK, Art 1 1.

**False Positives:**

- `Dr. Stefan Tokarski` — partial — gold is substring of pred: `Tokarski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tokarski`(person)

**Example 52** (doc_id: `deanon_TRAIN/13Fss3_19y`) (sent_id: `deanon_TRAIN/13Fss3_19y_3`)


Kopf Der Oberste Gerichtshof hat am 21. Jänner 2020 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Lässig als Vorsitzenden sowie den Hofrat des Obersten Gerichtshofs Dr. Nordmeyer und die Hofrätin des Obersten Gerichtshofs Dr. Brenner über den von Ing. Sebastian Nedler im Verfahren AZ 5 Bl 6/19v des Landesgerichts für Strafsachen Graz gestellten Fristsetzungsantrag nach Einsichtnahme der Generalprokuratur in die Akten und Abstimmung gemäß § 62 Abs 1 zweiter Satz OGH-Geo 2019 den Beschluss gefasst:  Spruch Der Antrag wird zurückgewiesen.

**False Positives:**

- `Ing. Sebastian Nedler` — partial — gold is substring of pred: `Nedler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nedler`(person)

**Example 53** (doc_id: `deanon_TRAIN/13Fss3_19y`) (sent_id: `deanon_TRAIN/13Fss3_19y_4`)


Gründe:  Rechtliche Beurteilung Mit seinem Fristsetzungsantrag vom 23. Dezember 2019 behauptet Ing. Sebastian Nattler Säumnis des Obersten Gerichtshofs mit „der Vornahme einer Verfahrenshandlung und Ausfertigung einer Entscheidung“ in Ansehung seines am 20. August 2019 beim Obersten Gerichtshof eingebrachten, gegen den Beschluss des Landesgerichts für Strafsachen Graz vom 1. Juli 2019, AZ 5 Bl 6/19v gerichteten Antrags auf Erneuerung des Strafverfahrens.

**False Positives:**

- `Ing. Sebastian Nattler` — partial — gold is substring of pred: `Nattler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nattler`(person)

**Example 54** (doc_id: `deanon_TRAIN/13Fss3_19y`) (sent_id: `deanon_TRAIN/13Fss3_19y_7`)


Eine Ausfertigung dieser Entscheidung wurde der Vertreterin des Ing. Sebastian Naesemann am 18. Oktober 2019 zugestellt.

**False Positives:**

- `Ing. Sebastian Naesemann` — partial — gold is substring of pred: `Naesemann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Naesemann`(person)

**Example 55** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__4`)


Abs 1 fünfter Fall, Abs 2 Z 1 SMG und weiterer strafbarer Handlungen über die Nichtigkeitsbeschwerde und die Berufung des Angeklagten gegen das Urteil des Landesgerichts für Strafsachen Graz als Schöffengericht vom 20. Jänner 2012, GZ 8 Hv 83/11m-49, sowie die von der Generalprokuratur gegen den Vorgang der schriftlichen Ausfertigung dieses Urteils erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit der Vertreterin der Generalprokuratur, Generalanwältin Dr. Brenner, sowie des Angeklagten und seines Verteidigers Mag. Heinz Russold nach Anhörung der Generalprokuratur zu Recht erkannt:  Spruch

**False Positives:**

- `Mag. Heinz Russold` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_TRAIN/14Os16_15g`) (sent_id: `deanon_TRAIN/14Os16_15g_9`)


Dem Einwand der Verfahrensrüge (Z 5) zuwider wurden durch die Abweisung des - zum Beweis dafür, dass beim Angeklagten zum Tatzeitpunkt ein die Zurechnungsfähigkeit ausschließender Rauschzustand bestanden hat, gestellten - Antrags auf „Einholung eines weiteren Gutachtens aus dem Fachbereich der Medizin“ (ON 35 S 14) wegen behaupteter unvollständiger Befundaufnahme und inhaltlicher Mangelhaftigkeit der Expertise des psychiatrischen und neurologischen Sachverständigen Dr. Bertha Westerhoven Verteidigungsrechte nicht verletzt.

**False Positives:**

- `Dr. Bertha Westerhoven Verteidigungsrechte` — partial — gold is substring of pred: `Dr. Bertha Westerhoven`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Bertha Westerhoven`(person)

**Example 57** (doc_id: `deanon_TRAIN/14Os19_16z`) (sent_id: `deanon_TRAIN/14Os19_16z_6`)


Danach hat er in Feldleitengasse 127u, 4132 Steining, Österreich und StR HR Dr.in Danielle Besmer unter dem Einfluss eines die Zurechnungsfähigkeit ausschließenden Zustands (§ 11 StGB), der auf einer geistigen und seelischen Abartigkeit von höherem Grad beruht, nämlich einer Polytoxikomanie, eines hirnorganischen Psychosyndroms und einer emotional instabilen Persönlichkeitsstörung (1) am 11. August 2015 Sabine Sulcke mit Gewalt zur Duldung des Beischlafs oder einer dem Beischlaf gleichzusetzenden geschlechtlichen Handlung zu nötigen versucht, indem er ihren Oberkörper mit beiden Armen umschlang, sie nachfolgend an ihrer Bekleidung festhielt und ihre Hose und Unterhose mit einer Hand gewaltsam bis zu den Knien herunterriss;

**False Positives:**

- `Dr.in Danielle Besmer` — partial — pred is substring of gold: `StR HR Dr.in Danielle Besmer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Feldleitengasse 127u, 4132 Steining, Österreich`(address)
- `StR HR Dr.in Danielle Besmer`(person)
- `Sulcke`(person)

**Example 58** (doc_id: `deanon_TRAIN/15Os177_13p`) (sent_id: `deanon_TRAIN/15Os177_13p_7`)


Mit Beschluss der Vorsitzenden des Schöffengerichts vom 22. Februar 2013, GZ 33 Hv 70/12x-220, wurden der Antrag des Dr. Rakhart Kirstin Achard auf Zuerkennung der Stellung als Opfer gemäß § 65 Abs 1 lit c StPO in diesem Verfahren zurückgewiesen und der Antrag auf Akteneinsicht abgewiesen.

**False Positives:**

- `Dr. Rakhart Kirstin Achard` — partial — gold is substring of pred: `Kirstin Achard`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Kirstin Achard`(person)

**Example 59** (doc_id: `deanon_TRAIN/15Os177_13p`) (sent_id: `deanon_TRAIN/15Os177_13p_10`)


Dagegen richtet sich der nicht auf eine Entscheidung des EGMR gestützte Antrag auf Erneuerung des Verfahrens gemäß § 363a StPO (RIS-Justiz RS0122228) des Dr. Rakhart Karsten Abbas.

**False Positives:**

- `Dr. Rakhart Karsten Abbas` — partial — gold is substring of pred: `Karsten Abbas`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Karsten Abbas`(person)

**Example 60** (doc_id: `deanon_TRAIN/15Os178_15p`) (sent_id: `deanon_TRAIN/15Os178_15p_3`)


Kopf Der Oberste Gerichtshof hat am 1. Juli 2016 durch den Senatspräsidenten des Obersten Gerichtshofs Prof. Dr. Danek als Vorsitzenden in der Strafsache des Privatanklägers Mag. Ralph Korsmeier gegen Martin Rühmekorb wegen des Vergehens der üblen Nachrede nach § 111 Abs 1 und Abs 2 StGB, AZ 91 Hv 75/09d des Landesgerichts für Strafsachen Wien über den Antrag des Privatanklägers auf Verlängerung der Frist zur Äußerung zur Stellungnahme der Generalprokuratur den Beschluss gefasst:  Spruch Der Antrag des Privatanklägers Mag. Ralph Klingspohr vom 27. Juni 2016 auf Verlängerung der Frist zur Äußerung zur Stellungnahme der Generalprokuratur wird abgewiesen.

**False Positives:**

- `Mag. Ralph Korsmeier` — partial — gold is substring of pred: `Korsmeier`
- `Mag. Ralph Klingspohr` — partial — gold is substring of pred: `Klingspohr`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Korsmeier`(person)
- `Rühmekorb`(person)
- `Klingspohr`(person)

**Example 61** (doc_id: `deanon_TRAIN/17Ob19_23b`) (sent_id: `deanon_TRAIN/17Ob19_23b_5`)


Zeno Thulcke, 2. Christine Adomadt, erstklagende Partei vertreten durch die Erwachsenenvertreterin Mag. Elfriede Melichar, Rechtsanwältin in Mödling, wider die beklagte Partei Dr. Benjamin Görmar, wegen Schadenersatz, hier wegen Verfahrenshilfe, über den „Rekurs“ (richtig: Revisionsrekurs) der zweitklagenden Partei gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 21. Juli 2023, GZ 18 R 96/23f, 97/23b, 98/23z-31, womit der Beschluss des Bezirksgerichts Mödling vom 10. Mai 2023, GZ 3 C 1057/21v-25, hinsichtlich der erstklagenden Partei bestätigt und der von der zweitklagenden Partei dagegen erhobene Rekurs zurückgewiesen wurde, sowie der Rekurs der klagenden Parteien gegen den Beschluss des Bezirksgerichts Mödling vom 28. März 2023, GZ 3 C 1057/21v-20, zurückgewiesen wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Mag. Elfriede Melichar` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zeno Thulcke`(person)
- `Christine Adomadt`(person)
- `Dr. Benjamin Görmar`(person)

**Example 62** (doc_id: `deanon_TRAIN/18ONc1_21y`) (sent_id: `deanon_TRAIN/18ONc1_21y_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Senatspräsidenten Dr. Veith, die Hofräte Hon.-Prof. Dr. Höllwerth, Hon.-Prof. PD Dr. Rassi und Mag. Painsi als weitere Richter in der Schiedsrechtssache der Antragstellerin (schiedsbeklagte Partei) See-Versand Werke GmbH, Robert Leis, gegen die Antragsgegnerin (schiedsklagende Partei) Dargatz+Boedewig Telekom GmbH, ÖkR Nikolaus Buksbaum, vertreten durch Dr. Horst Pechar, Rechtsanwalt in Weiz, wegen § 602 ZPO, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der an den Obersten Gerichtshof gerichtete Antrag vom 7. 1. 2021 wird, soweit er sich an den Obersten Gerichtshof richtet, zurückgewiesen.

**False Positives:**

- `Dr. Horst Pechar` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `See-Versand Werke GmbH`(organisation)
- `Robert Leis`(person)
- `Dargatz+Boedewig Telekom GmbH`(organisation)
- `ÖkR Nikolaus Buksbaum`(person)

**Example 63** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Herbes&Vißers Heizung GmbH, Waldemar Lokämper, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Traun-Luftfahrt GmbH, VetR DDr. Walter Stuehrmann, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

**False Positives:**

- `Dr. Andreas Oberbichler` — no gold match — likely missing annotation
- `Dr. Michael Kramer` — no gold match — likely missing annotation
- `Mag. Maximilian Kocher` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Gold Entities:**

- `Landesgericht Wiener Neustadt`(organisation)
- `Herbes&Vißers Heizung GmbH`(organisation)
- `Waldemar Lokämper`(person)
- `Traun-Luftfahrt GmbH`(organisation)
- `VetR DDr. Walter Stuehrmann`(person)
- `Landesgericht Feldkirch`(organisation)

**Example 64** (doc_id: `deanon_TRAIN/1Nc2_20i`) (sent_id: `deanon_TRAIN/1Nc2_20i_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie den Hofrat Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei KommR Franz Kubank, vertreten durch Dr. Michael Wukoschitz, Rechtsanwalt in Wien, gegen die beklagte Partei Laurin Aichhorn a.d., Timothy Schulmeister, Serbien, wegen 600 EUR sA, über den Ordinationsantrag nach § 28 JN den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Dr. Michael Wukoschitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `KommR Franz Kubank`(person)
- `Laurin Aichhorn`(person)
- `Timothy Schulmeister`(person)
- `Bezirksgericht Schwechat`(organisation)

**Example 65** (doc_id: `deanon_TRAIN/1Ob103_17d`) (sent_id: `deanon_TRAIN/1Ob103_17d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Laura Overbeeke, BA, vertreten durch Dr. Gerhard Ebenbichler, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. Janis Marxmeyer, und 2.

**False Positives:**

- `Dr. Gerhard Ebenbichler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Laura Overbeeke, BA`(person)
- `Janis Marxmeyer`(person)

**Example 66** (doc_id: `deanon_TRAIN/1Ob103_17d`) (sent_id: `deanon_TRAIN/1Ob103_17d_4`)


Chantal Maxein, vertreten durch Dr. Eric Agstner, Rechtsanwalt in Wien, wegen Unterlassung, Zahlung, Feststellung und Beseitigung, über die Revision der beklagten Parteien gegen das Teilurteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 27. Februar 2017, GZ 58 R 128/16w-38a, in der Fassung des Berichtigungsbeschlusses vom 29. März 2017, GZ 58 R 128/16w-40, mit dem das Urteil des Bezirksgerichts Neunkirchen vom 18. November 2016, GZ 23 C 249/16x-33, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Eric Agstner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Chantal Maxein`(person)

**Example 67** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_4`)


Republik Österreich, vertreten durch die Finanzprokuratur in Wien, 2. Dr. Ralph Kreidenweiß, und 3. Donau-Automotive GmbH, Ebersreith 11, 8761 Götzendorf, Österreich, beide vertreten durch Dr. Hubert Simon, Rechtsanwalt in Wien, wegen Leistung und Feststellung, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. April 2014, GZ 7 R 21/14h-7, mit dem der Beschluss des Landesgerichts Leoben vom 30. Jänner 2014, GZ 2 Nc 2/14y-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Dr. Ralph Kreidenwei` — partial — pred is substring of gold: `Dr. Ralph Kreidenweiß`
- `Dr. Hubert Simon` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Ralph Kreidenweiß`(person)
- `Donau-Automotive GmbH`(organisation)
- `Ebersreith 11, 8761 Götzendorf, Österreich`(address)

**Example 68** (doc_id: `deanon_TRAIN/1Ob128_17f`) (sent_id: `deanon_TRAIN/1Ob128_17f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Familienrechtssache des Antragstellers Mag. Jeannette Scherl, vertreten durch die Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG, Wien, gegen die Antragsgegnerin Selina Dorfmeyer, vertreten durch Mag. Anna-Maria Freiberger, Rechtsanwältin in Wien, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 24. April 2017, GZ 45 R 66/17i, 67/17m-19, mit dem die Beschlüsse des Bezirksgerichts Liesing vom 4. Jänner 2017, GZ 7 Fam 30/16m-12, und vom 17. Jänner 2017, GZ 7 Fam 30/16m-14, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Dr. Helene Klaar Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Jeannette Scherl`(person)
- `Selina Dorfmeyer`(person)

**Example 69** (doc_id: `deanon_TRAIN/1Ob139_18z`) (sent_id: `deanon_TRAIN/1Ob139_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Angelina Töpker Inc., Ronja Straßgschwandtner, vertreten durch Mag. Ralph Kilches, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Lilia Anderßon, als Insolvenzverwalter im Insolvenzverfahren über das Vermögen der Vanek und Eloy Analyse GmbH, Kanischaberg 21, 4742 Kornrödt, Österreich, vertreten durch die Haslinger/Nagele & Partner Rechtsanwälte GmbH, Linz, wegen Feststellung einer Insolvenzforderung (Streitwert 447.352,05 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 28. Juni 2018, GZ 1 R 83/18h-8, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mag. Ralph Kilches` — no gold match — likely missing annotation
- `Mag. Lilia Ander` — partial — pred is substring of gold: `Mag. Lilia Anderßon`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Angelina Töpker`(person)
- `Ronja Straßgschwandtner`(person)
- `Mag. Lilia Anderßon`(person)
- `Vanek und Eloy Analyse GmbH`(organisation)
- `Kanischaberg 21, 4742 Kornrödt, Österreich`(address)

**Example 70** (doc_id: `deanon_TRAIN/1Ob142_19t`) (sent_id: `deanon_TRAIN/1Ob142_19t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der Antragstellerin Mag. Liu Cingöz, vertreten Dr. Brigitte Birnbaum und Dr. Rainer Toperczer, Rechtsanwälte in Wien, gegen den Antragsgegner Dr. Torsten Erlautzki, vertreten durch die Anwaltssocietät Sattlegger Dorninger Steiner & Partner OG, Linz, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse gemäß §§ 81 ff EheG, über die außerordentlichen Revisionsrekurse beider Parteien gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 9. Juli 2019, GZ 45 R 554/18f-162, mit dem der Beschluss des Bezirksgerichts Fünfhaus vom 25. Oktober 2018, GZ 4 Fam 68/14k-156, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Der Revisionsrekurs des Antragsgegners wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

**False Positives:**

- `Mag. Liu Cing` — partial — pred is substring of gold: `Mag. Liu Cingöz`
- `Dr. Brigitte Birnbaum` — no gold match — likely missing annotation
- `Dr. Rainer Toperczer` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 2

**Gold Entities:**

- `Mag. Liu Cingöz`(person)
- `Dr. Torsten Erlautzki`(person)

**Example 71** (doc_id: `deanon_TRAIN/1Ob14_20w`) (sent_id: `deanon_TRAIN/1Ob14_20w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei VetR Amber Baraniak, Hong Kong, vertreten durch die Oblin Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Mag. Liliana Bößer, vertreten durch Dr. Karl Heinz Kramer M.A.S., Rechtsanwalt in Villach, wegen Aufhebung eines Kaufvertrags, 213.819,01 USD sA und 9.950,39 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 30. Oktober 2019, GZ 5 R 94/19m-210, mit dem das Urteil des Landesgerichts Klagenfurt vom 2. April 2019, GZ 25 Cg 122/12y-207, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Karl Heinz Kramer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `VetR Amber Baraniak`(person)
- `Mag. Liliana Bößer`(person)

**Example 72** (doc_id: `deanon_TRAIN/1Ob152_24w`) (sent_id: `deanon_TRAIN/1Ob152_24w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Musger als Vorsitzenden sowie die Hofrätin und die Hofräte Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei VetR Volkmar Acar KG, FN FN823951l, vertreten durch Dr. Eva-Maria Bachmann-Lang, Dr. Christian Bachmann, Rechtsanwälte in Wien, gegen die beklagte Partei „ Nemtschok Touristik “ Wilnorlex Werke gmbH, FN FN545761v, vertreten durch die GRAF ISOLA Rechtsanwälte GmbH in Wien, wegen 51.843,91 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 3. Juli 2024, GZ 1 R 17/24p-39, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Christian Bachmann` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `VetR Volkmar Acar`(person)
- `FN823951l`(business_register_number)
- `Nemtschok Touristik`(organisation)
- `Wilnorlex Werke gmbH`(organisation)
- `FN545761v`(business_register_number)

**Example 73** (doc_id: `deanon_TRAIN/1Ob160_12d`) (sent_id: `deanon_TRAIN/1Ob160_12d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der außerstreitigen Rechtssache der Antragstellerin Svenja Meierarnd, vertreten durch Dr. Karl-Peter Hasch, Rechtsanwalt in Villach, gegen den Antragsgegner Othmar Eidenmueller, vertreten durch Mag. Hanno Stromberger, Rechtsanwalt in Villach, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse über den Revisionsrekurs der Antragstellerin gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 31. Mai 2012, GZ 2 R 85/12w-11, mit dem der Beschluss des Bezirksgerichts Villach vom 13. März 2012, GZ 38 Fam 98/11s-7, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Mag. Hanno Stromberger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Svenja Meierarnd`(person)
- `Othmar Eidenmueller`(person)

**Example 74** (doc_id: `deanon_TRAIN/1Ob163_21h`) (sent_id: `deanon_TRAIN/1Ob163_21h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Manfred Nordkamp, vertreten durch Mag. Dieter Koch und Mag. Natascha Jilek, Rechtsanwälte in Bruck an der Mur, gegen die beklagte Partei Belohlawek KI Bank AG, Denis Nakonzer, vertreten durch Mag. Martina Hosp ua, Rechtsanwälte in Salzburg, wegen Feststellung (Streitwert 103.488,18 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 21. Juni 2021, GZ 2 R 70/21h-19, mit dem das Urteil des Landesgerichts Salzburg vom 12. März 2021, GZ 10 Cg 52/20k-15, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mag. Dieter Koch` — no gold match — likely missing annotation
- `Mag. Natascha Jilek` — no gold match — likely missing annotation
- `Mag. Martina Hosp` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Gold Entities:**

- `Manfred Nordkamp`(person)
- `Belohlawek KI`(organisation)
- `Denis Nakonzer`(person)

**Example 75** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Dr. Wurdinger als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Steger, Mag. Wessely-Kristöfel, Dr. Parzmayr und Dr. Pfurtscheller als weitere Richterinnen und Richter in der Rechtssache der klagenden Partei Bundeskammer für Arbeiter und Angestellte, Wien 4, Prinz-Eugen-Straße 20–22, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Alsynwald-Recycling AG, RgR Mag. Dr. Evelyn Steinkröger, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH in Wien, wegen Unterlassung und Urteilsveröffentlichung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. Juli 2024, GZ 2 R 77/24v-15, mit dem das Urteil des Handelsgerichts Wien vom 28. Februar 2024, GZ 57 Cg 36/23d-8, bestätigt wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Walter Reichholf` — no gold match — likely missing annotation
- `Mag. Dr. Evelyn Steinkr` — partial — pred is substring of gold: `RgR Mag. Dr. Evelyn Steinkröger`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Alsynwald-Recycling AG`(organisation)
- `RgR Mag. Dr. Evelyn Steinkröger`(person)

**Example 76** (doc_id: `deanon_TRAIN/1Ob179_12y`) (sent_id: `deanon_TRAIN/1Ob179_12y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Pflegschaftssache des mj Roy Boner, geboren am 13. Juli 2006, vertreten durch Mag. Heinz Wolfbauer, Rechtsanwalt in Wien, wegen Unterhalts, über den Revisionsrekurs des Vaters Dr. Jaroslaw Kellenbrink, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 29. Mai 2012, GZ 43 R 254/12i-106, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Döbling vom 28. März 2012, GZ 10 Pu 131/09b-100, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Mag. Heinz Wolfbauer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Roy Boner`(person)
- `Dr. Jaroslaw Kellenbrink`(person)

**Example 77** (doc_id: `deanon_TRAIN/1Ob182_17x`) (sent_id: `deanon_TRAIN/1Ob182_17x_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Dr. Wurdinger, und die Hofrätinnen Dr. Hofer-Zeni-Rennhofer und Dr. Kodek in der Rechtssache der gefährdeten Partei Prof. Virgil Pahlow, vertreten durch die Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG, Wien, gegen die gefährdete Partei Dominika Föcks, vertreten durch Dr. Alexander Haas, Rechtsanwalt in Seiersberg-Pirka, wegen Erlassung einer einstweiligen Verfügung nach § 382 Z 8 lit c zweiter Fall EO, über den außerordentlichen Revisionsrekurs der gefährdeten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 11. September 2017, GZ 1 R 213/17a-221, mit dem der Beschluss des Bezirksgerichts Fürstenfeld vom 25. Juli 2017, GZ 23 Fam 27/15p-207, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Dr. Helene Klaar Dr` — no gold match — likely missing annotation
- `Dr. Alexander Haas` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Prof. Virgil Pahlow`(person)
- `Dominika Föcks`(person)

**Example 78** (doc_id: `deanon_TRAIN/1Ob184_15p`) (sent_id: `deanon_TRAIN/1Ob184_15p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tamara Schweinfurth, vertreten durch Dr. Wolfgang Maurer, Rechtsanwalt in Golling, gegen die beklagte Partei Noah Vlatten, BEd, vertreten durch Dr. Peter Perner, Rechtsanwalt in Salzburg, wegen 10.895,18 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 19. Mai 2015, GZ 22 R 126/15f-21, mit dem das Urteil des Bezirksgerichts Salzburg vom 5. März 2015, GZ 32 C 407/14x-17, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Wolfgang Maurer` — no gold match — likely missing annotation
- `Dr. Peter Perner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Tamara Schweinfurth`(person)
- `Noah Vlatten, BEd`(person)

**Example 79** (doc_id: `deanon_TRAIN/1Ob186_12b`) (sent_id: `deanon_TRAIN/1Ob186_12b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Thomas Pasqualini, vertreten durch Kammler & Koll Rechtsanwälte OG in Freistadt, gegen die beklagte Partei Patrick Denzlein, vertreten durch Mag. Klaus Burgholzer, Rechtsanwalt in Linz, wegen 100.000 EUR sA und Feststellung (Streitwert: 5.000 EUR), über die außerordentliche Revision der klagenden Partei (Revisionsinteresse: 70.000 EUR sA) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. Juli 2012, GZ 2 R 79/12v-22, mit dem das Urteil des Landesgerichts Linz vom 27. Februar 2012, GZ 5 Cg 61/11d-18, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Mag. Klaus Burgholzer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Pasqualini`(person)
- `Denzlein`(person)

</details>

---

## `Person after 'Schriftführer' (Court Clerk)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `cfc661f1`  
**Description:**
Captures the name of the court clerk mentioned after the title.

**Content:**
```
(?:Schriftführer)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Person after 'fachkundiger Laienrichter'`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6e3cfc1d`  
**Description:**
Captures lay judges mentioned with their specific title.

**Content:**
```
(?:fachkundiger\s+Laienrichter|fachkundige\s+Laienrichterin)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Person after Judicial Role`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9b474dd4`  
**Description:**
Captures the full name (including title) appearing immediately after judicial role indicators, excluding the role text.

**Content:**
```
(?:die\s+Richterin|der\s+Richter|die\s+Senatsvorsitzende)\s+(?:Dr\.(?:in)?|Mag\.(?:Dr\.)?|Univ\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Hon\.-Prof\.(?:in)?|Ing\.(?:Mag\.)?|PhD|LL\.M\.|Bakk\. rer\. nat\.|OStR|MR|ÖkR|KommR|VetR|PhD OMedR)?\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 229 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/7Ob58_15b`) (sent_id: `deanon_TRAIN/7Ob58_15b_4`)


Text Begründung: Das Bezirksgericht Vöcklabruck gab dem vom Antragsteller gegen die Richterin Dr. Nikolai Hopfstock erhobenen Ablehnungsantrag nicht Folge.

**False Positives:**

- `Nikolai Hopfstock` — partial — pred is substring of gold: `Dr. Nikolai Hopfstock`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Nikolai Hopfstock`(person)

</details>

---

## `Person in Legal Case Context`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `dd884f7b`  
**Description:**
Captures names appearing after 'Beschwerdesache' or similar case introductions, ensuring full name is captured.

**Content:**
```
(?:in\s+der\s+Beschwerdesache|der\s+Beschwerdesache|in\s+der\s+Verwaltungsstrafsache|gegen\s+Herrn|gegen\s+Frau|gegen\s+die)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 19 | 0 | 19 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 19 | 918 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/15Os133_11i_15Os134_11m_`) (sent_id: `deanon_TRAIN/15Os133_11i_15Os134_11m__3`)


Kopf Der Oberste Gerichtshof hat am 16. November 2011 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Danek als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Dr. T. Solé und Mag. Lendl sowie die Hofrätinnen des Obersten Gerichtshofs Dr. Bachner-Foregger und Dr. Michel-Kwapinski als weitere Richter in Gegenwart des Richteramtsanwärters Mag. Kopinits als Schriftführer in der Medienrechtssache des Antragstellers Siegfried Klimczuk gegen die Antragsgegnerin Reifner Medien GmbH wegen §§ 6 Abs 1, 8a Abs 6 MedienG, AZ 91 Hv 72/05g des Landesgerichts für Strafsachen Wien, über die von der Generalprokuratur gegen die Beschlüsse des Landesgerichts für Strafsachen Wien vom 28. April 2009, GZ 91 Hv 72/05g-75, und des Oberlandesgerichts Wien als Beschwerdegericht vom 6. Juli 2009, AZ 18 Bs 218/09d, erhobene Nichtigkeitsbeschwerde zur Wahrung des Gesetzes nach öffentlicher Verhandlung in Anwesenheit des Vertreters der Generalprokuratur, Generalanwalt Mag. Knibbe, des Vertreters des Antragstellers Dr. Rami sowie jenes der Antragsgegnerin Mag. Renzl zu Recht erkannt:  Spruch

**False Positives:**

- `Antragsgegnerin Reifner Medien Gmb` — positional overlap with gold: `Reifner Medien GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Klimczuk`(person)
- `Reifner Medien GmbH`(organisation)

**Example 1** (doc_id: `deanon_TRAIN/15Os133_11i_15Os134_11m_`) (sent_id: `deanon_TRAIN/15Os133_11i_15Os134_11m__5`)


Text Gründe: In der Medienrechtssache des Antragstellers Siegfried Knechtlein gegen die Antragsgegnerin Traglanz Software GmbH wegen §§ 6 Abs 1, 8a Abs 6 MedienG, AZ 91 Hv 72/05g des Landesgerichts für Strafsachen Wien, wurde mit Urteil vom 18. November 2005 (ON 17) mit Beziehung auf eine in der in der periodischen Druckschrift „ Ida Parakeninks “ Nr 18 vom 2. Mai 2005 erschienenen Veröffentlichung enthaltene, dem Antragsteller zugeschriebene Äußerung („Wehrmachtsdeserteure sind Kameradenmörder“) der Antragsgegnerin gemäß § 6 Abs 1 MedienG die Zahlung einer Entschädigung von 4.000 Euro an den Antragsteller sowie gemäß § 8a Abs 1 MedienG iVm § 389 Abs 1 StPO der Ersatz der Verfahrenskosten auferlegt und sie gemäß § 8a Abs 6 MedienG zur Urteilsveröffentlichung verpflichtet.

**False Positives:**

- `Antragsgegnerin Traglanz Software Gmb` — positional overlap with gold: `Traglanz Software GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Knechtlein`(person)
- `Traglanz Software GmbH`(organisation)
- `Ida Parakeninks`(person)

**Example 2** (doc_id: `deanon_TRAIN/1Ob105_18z`) (sent_id: `deanon_TRAIN/1Ob105_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Familienrechtssache des Antragstellers Ilona Hoerhold, vertreten durch die Korp Rechtsanwalts GmbH, Andorf, gegen die Antragsgegnerin Farina Prokofyev, vertreten durch die Puttinger Vogl Rechtsanwälte GmbH, Ried im Innkreis, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts Wels als Rekursgericht vom 2. Mai 2018, GZ 21 R 50/18d-32, mit dem der Rekurs des Antragstellers gegen den Beschluss des Bezirksgerichts Grieskirchen vom 8. Jänner 2018, GZ 8 Fam 37/16i-26, zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

**False Positives:**

- `Antragsgegnerin Farina Prokofyev` — partial — gold is substring of pred: `Farina Prokofyev`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ilona Hoerhold`(person)
- `Farina Prokofyev`(person)

**Example 3** (doc_id: `deanon_TRAIN/1Ob128_17f`) (sent_id: `deanon_TRAIN/1Ob128_17f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Familienrechtssache des Antragstellers Mag. Jeannette Scherl, vertreten durch die Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG, Wien, gegen die Antragsgegnerin Selina Dorfmeyer, vertreten durch Mag. Anna-Maria Freiberger, Rechtsanwältin in Wien, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 24. April 2017, GZ 45 R 66/17i, 67/17m-19, mit dem die Beschlüsse des Bezirksgerichts Liesing vom 4. Jänner 2017, GZ 7 Fam 30/16m-12, und vom 17. Jänner 2017, GZ 7 Fam 30/16m-14, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Antragsgegnerin Selina Dorfmeyer` — partial — gold is substring of pred: `Selina Dorfmeyer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Jeannette Scherl`(person)
- `Selina Dorfmeyer`(person)

**Example 4** (doc_id: `deanon_TRAIN/1Ob205_10v`) (sent_id: `deanon_TRAIN/1Ob205_10v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Dr. E. Solé und Mag. Wurzer als weitere Richter in der Rechtssache des Antragstellers Hans Päulgen, vertreten durch Mag. Matthias Kucera, Rechtsanwalt in Hard, gegen die Antragsgegnerin Herta Polaschegg, vertreten durch Dr. Wolf Heistinger, Rechtsanwalt in Mödling, wegen Anerkennung eines ausländischen Scheidungsurteils, über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 13. Oktober 2010, GZ 16 R 384/10z-11, mit dem der Beschluss des Bezirksgerichts Mödling vom 1. September 2010, GZ 13 Nc 14/10w-5, bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

**False Positives:**

- `Antragsgegnerin Herta Polaschegg` — partial — gold is substring of pred: `Polaschegg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Päulgen`(person)
- `Polaschegg`(person)

**Example 5** (doc_id: `deanon_TRAIN/1Ob35_21k`) (sent_id: `deanon_TRAIN/1Ob35_21k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Familienrechtssache des Antragstellers DI Sandra Foglar, vertreten durch Dr. Walter Mardetschläger und andere Rechtsanwälte in Wien, gegen die Antragsgegnerin Mag. Christine Scherfling, vertreten durch Mag. Sonja Fragner, Rechtsanwältin in Krems, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 28. Jänner 2021, GZ 2 R 91/20z-49, mit dem der Beschluss des Bezirksgerichts Krems an der Donau vom 29. Juli 2020, GZ 7 Fam 10/18a-43, mit einer Maßgabe bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Antragsgegnerin Mag` — positional overlap with gold: `Mag. Christine Scherfling`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DI Sandra Foglar`(person)
- `Mag. Christine Scherfling`(person)

**Example 6** (doc_id: `deanon_TRAIN/1Ob78_22k`) (sent_id: `deanon_TRAIN/1Ob78_22k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. HR Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Familienrechtssache des Antragstellers Dr. Mehmet Herschlein, vertreten durch den Erwachsenenvertreter Dr. Dagobert Hammer, Rechtsanwalt in Wien, gegen die Antragsgegnerin Lucia Ignatzy, vertreten durch Dr. Karl Newole, Rechtsanwalt in Wien, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. Dezember 2021, GZ 44 R 449/21m-15, mit dem der Beschluss des Bezirksgerichts Josefstadt vom 29. November 2021, GZ 25 Fam 3/21k-10, bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

**False Positives:**

- `Antragsgegnerin Lucia Ignatzy` — partial — gold is substring of pred: `Lucia Ignatzy`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Mehmet Herschlein`(person)
- `Dr. Dagobert Hammer`(person)
- `Lucia Ignatzy`(person)

**Example 7** (doc_id: `deanon_TRAIN/1Ob7_18p`) (sent_id: `deanon_TRAIN/1Ob7_18p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Familienrechtssache des Antragstellers Charlotte Zanker, vertreten durch die GKP Gabl Kogler Leitner Stöglehner Bodingbauer Rechtsanwälte OG, Linz, gegen die Antragsgegnerin Elvira Mohamad, vertreten durch die ANWALTGMBH Rinner Teuchtmann, Linz, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse nach den §§ 81 ff EheG, über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts Linz als Rekursgericht vom 15. November 2017, GZ 15 R 484/17b-10, mit dem der Beschluss des Bezirksgerichts Urfahr vom 28. September 2017, GZ 13 Fam 22/17v-5, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Antragsgegnerin Elvira Mohamad` — partial — gold is substring of pred: `Elvira Mohamad`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Charlotte Zanker`(person)
- `Elvira Mohamad`(person)

**Example 8** (doc_id: `deanon_TRAIN/3Nc11_13t`) (sent_id: `deanon_TRAIN/3Nc11_13t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie die Hofräte Univ.-Prof Dr. Neumayr und Dr. Jensik als weitere Richter in der Ordinationssache der Antragstellerin Waldzorval Technologien GmbH, Dr.-Kühne-Gasse 29, 9560 Albern, Österreich, vertreten durch Dr. Clemens Thiele, Rechtsanwalt in Salzburg, gegen die Antragsgegnerin Pflege Allemkraft GmbH, Schirmerstraße 61, 8967 Oberhausberg, Österreich, wegen Exekutionsführung nach § 355 EO, infolge Antrags gemäß § 28 JN den Beschluss gefasst:  Spruch Für die Bewilligung und die Vollziehung der beabsichtigten Unterlassungsexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Antragsgegnerin Pflege Allemkraft Gmb` — positional overlap with gold: `Pflege Allemkraft GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Waldzorval Technologien GmbH`(organisation)
- `Dr.-Kühne-Gasse 29, 9560 Albern, Österreich`(address)
- `Pflege Allemkraft GmbH`(organisation)
- `Schirmerstraße 61, 8967 Oberhausberg, Österreich`(address)
- `Bezirksgericht Salzburg`(organisation)

**Example 9** (doc_id: `deanon_TRAIN/3Nc19_22g`) (sent_id: `deanon_TRAIN/3Nc19_22g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek sowie den Hofrat Dr. Stefula als weitere Richter in der Ordinationssache der Antragstellerin Stadt-Robotik GmbH, Hum 65, 9241 Kantnig, Österreich, vertreten durch Specht & Partner Rechtsanwalt GmbH in Wien, gegen die Antragsgegnerin Ing. Verona Obersteiner, Russische Föderation, wegen § 355 EO, über den Ordinationsantrag der Antragstellerin, den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Antragsgegnerin Ing` — positional overlap with gold: `Ing. Verona Obersteiner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stadt-Robotik GmbH`(organisation)
- `Hum 65, 9241 Kantnig, Österreich`(address)
- `Ing. Verona Obersteiner`(person)

**Example 10** (doc_id: `deanon_TRAIN/3Ob112_23a`) (sent_id: `deanon_TRAIN/3Ob112_23a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der außerstreitigen Rechtssache der Antragstellerin Amalia Lupprich, vertreten durch Dr. Walter Fleissner, Rechtsanwalt in Wien, gegen die Antragsgegnerin Zarin Terzi, vertreten durch Mag. Werner Hauser Rechtsanwalt in Wien, über den außerordentlichen Revisionsrekurs der Antragstellerin gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 27. Februar 2023, GZ 43 R 331/22b-65, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

**False Positives:**

- `Antragsgegnerin Zarin Terzi` — partial — gold is substring of pred: `Zarin Terzi`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Amalia Lupprich`(person)
- `Zarin Terzi`(person)

**Example 11** (doc_id: `deanon_TRAIN/5Ob146_16f`) (sent_id: `deanon_TRAIN/5Ob146_16f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie den Hofrat Dr. Höllwerth, die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer und Mag. Painsi als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers Mag. Niels Mueter, vertreten durch Dr. Anke Reisch, Rechtsanwältin in Kitzbühel, gegen die Antragsgegnerin Talgart-Chemie GmbH & Co KG, Tiefe Gasse 5, 2061 Obritz, Österreich, vertreten durch Dr. Lisbeth Lass und Dr. Hans Christian Lass, Rechtsanwälte in Innsbruck, wegen § 52 Abs 1 Z 6 iVm § 20 Abs 3 WEG 2002, infolge des „außerordentlichen“ Revisionsrekurses des Antragstellers gegen den (richtig) Sachbeschluss des Landesgerichts Innsbruck vom 24. Mai 2016, GZ 4 R 128/16a-50, mit dem der Sachbeschluss des Bezirksgerichts Kitzbühel vom 14. März 2016, GZ 4 Msch 7/14x-36, abgeändert wurde, den Beschluss gefasst:  Spruch Der Akt wird dem Erstgericht zurückgestellt.

**False Positives:**

- `Antragsgegnerin Talgart` — positional overlap with gold: `Talgart-Chemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Niels Mueter`(person)
- `Talgart-Chemie GmbH`(organisation)
- `Co KG`(organisation)
- `Tiefe Gasse 5, 2061 Obritz, Österreich`(address)

**Example 12** (doc_id: `deanon_TRAIN/5Ob184_21a`) (sent_id: `deanon_TRAIN/5Ob184_21a_4`)


Techn R Jaden Damcke, 2. Florian Adatepe, ebenda, beide vertreten durch Schlösser & Partner Rechtsanwälte OG in Wien, gegen die Antragsgegnerin Xenia Droeßler, vertreten durch Mag. Michael Operschal Rechtsanwalt GmbH in Wien, wegen § 37 Abs 1 Z 8 iVm § 16 MRG, über den Revisionsrekurs der Antragsteller gegen den Sachbeschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 19. Mai 2021, GZ 40 R 2/21x-15, mit dem der Sachbeschluss des Bezirksgerichts Floridsdorf vom 30. Oktober 2020, GZ 28 Msch 9/19g-11, abgeändert wurde, den Sachbeschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Antragsgegnerin Xenia Droe` — positional overlap with gold: `Xenia Droeßler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Techn R Jaden Damcke`(person)
- `Florian Adatepe`(person)
- `Xenia Droeßler`(person)

**Example 13** (doc_id: `deanon_TRAIN/5Ob189_19h`) (sent_id: `deanon_TRAIN/5Ob189_19h_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer, Mag. Painsi und Dr. Steger als weitere Richter in der Rechtssache der klagenden Partei James Chowdhury, vertreten durch Mag. Dr. Wolfgang Schlegl, Rechtsanwalt in Graz, gegen die Beklagte Mag. Ilhan Poele, vertreten durch MMag.Dr. Christopher Engel, Rechtsanwalt in Graz, wegen 37.052,50 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 16. September 2019, GZ 2 R 129/19m-21, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Beklagte Mag` — positional overlap with gold: `Mag. Ilhan Poele`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `James Chowdhury`(person)
- `Mag. Ilhan Poele`(person)

**Example 14** (doc_id: `deanon_TRAIN/5Ob206_24s`) (sent_id: `deanon_TRAIN/5Ob206_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Painsi, Dr. Weixelbraun-Mohr, Dr. Steger und Dr. Pfurtscheller als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers OMedR Louisa Dutzke, vertreten durch Mag. Wolfgang Doppelhofer LL.M. LL.M., Rechtsanwalt in Wien, gegen die Antragsgegnerin Alsud-Pflege GmbH, Kirchenwaldweg 10, 3104 St. Pölten, Österreich, vertreten durch Weishaupt Horak Georgiev Rechtsanwälte GmbH & Co KG in Wien, wegen Feststellung der Ausstattungskategorie nach § 15a MRG, über den Revisionsrekurs der Antragsgegnerin gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 26. August 2024, GZ 39 R 144/24a-22, mit dem der Sachbeschluss des Bezirksgerichts Hietzing vom 29. Mai 2024, GZ 9 MSch 18/23k-18, aufgehoben wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Antragsgegnerin Alsud` — positional overlap with gold: `Alsud-Pflege GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OMedR Louisa Dutzke`(person)
- `Alsud-Pflege GmbH`(organisation)
- `Kirchenwaldweg 10, 3104 St. Pölten, Österreich`(address)
- `Co KG`(organisation)

**Example 15** (doc_id: `deanon_TRAIN/5Ob20_21h`) (sent_id: `deanon_TRAIN/5Ob20_21h_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer, Mag. Painsi und Dr. Steger als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers Paolo Hermens, vertreten durch Mag. Norbert Tanzer, Rechtsanwalt in Telfs, gegen die Antragsgegnerin Heidrun Imgrundt, vertreten durch Dr. Bernhard Waldhof, Rechtsanwalt in Innsbruck, wegen §§ 3, 37 Abs 1 Z 2 sowie §§ 21 f, 37 Abs 1 Z 11 MRG, über den Revisionsrekurs der Antragsgegnerin gegen den Sachbeschluss des Landesgerichts Innsbruck vom 5. November 2020, GZ 4 R 122/20z-25, mit dem der Zwischensachbeschluss des Bezirksgerichts Silz vom 29. Juni 2020, GZ 2 Msch 4/19i-20, bestätigt wurde, den Beschluss gefasst:  Spruch Aus Anlass des Revisionsrekurses werden die Entscheidungen der Vorinstanzen über den Zwischenantrag auf Feststellung aufgehoben.

**False Positives:**

- `Antragsgegnerin Heidrun Imgrundt` — partial — gold is substring of pred: `Heidrun Imgrundt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Paolo Hermens`(person)
- `Heidrun Imgrundt`(person)

**Example 16** (doc_id: `deanon_TRAIN/6Ob161_10k`) (sent_id: `deanon_TRAIN/6Ob161_10k_5`)


Nigel Frömmke, vertreten durch Dr. Josef Olischar und Dr. Johannes Olischar, Rechtsanwälte in Wien, gegen die Antragsgegnerin Republik Österreich, vertreten durch WienEvent GmbH, Oweges C 64, 4115 Apfelsbach, Österreich, vertreten durch Fellner Wratzfeld & Partner Rechtsanwälte GmbH in Wien, wegen Festsetzung einer Enteignungsentschädigung, über den Revisionsrekurs der Antragsgegnerin gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 27. Mai 2010, GZ 14 R 59/10i-54, womit der Beschluss des Landesgerichts Korneuburg vom 2. Februar 2010, GZ 26 Nc 3/08x-44, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Antragsgegnerin Republik` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Nigel Frömmke`(person)
- `WienEvent GmbH`(organisation)
- `Oweges C 64, 4115 Apfelsbach, Österreich`(address)

**Example 17** (doc_id: `deanon_TRAIN/7Ob58_15b`) (sent_id: `deanon_TRAIN/7Ob58_15b_4`)


Text Begründung: Das Bezirksgericht Vöcklabruck gab dem vom Antragsteller gegen die Richterin Dr. Nikolai Hopfstock erhobenen Ablehnungsantrag nicht Folge.

**False Positives:**

- `Richterin Dr` — positional overlap with gold: `Dr. Nikolai Hopfstock`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Nikolai Hopfstock`(person)

**Example 18** (doc_id: `deanon_TRAIN/9Nc65_19m`) (sent_id: `deanon_TRAIN/9Nc65_19m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätinnen des Obersten Gerichtshofs Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der Antragstellerin RgR Sonja Vormschlag, vertreten durch Dr. Wallentin-Hermann, Rechtsanwältin Wien, gegen die Antragsgegnerin Bianca Urbscheit, Russische Föderation, wegen 400 EUR sA, über den Ordinationsantrag nach § 28 JN, den Beschluss gefasst:  Spruch Dem Ordinationsantrag wird stattgegeben.

**False Positives:**

- `Antragsgegnerin Bianca Urbscheit` — partial — gold is substring of pred: `Bianca Urbscheit`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RgR Sonja Vormschlag`(person)
- `Bianca Urbscheit`(person)

</details>

---

## `Person after 'vertreten durch' (represented by)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4499bf7e`  
**Description:**
Captures names of legal representatives following 'vertreten durch', ensuring full name is captured.

**Content:**
```
(?:vertreten\s+durch)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 99 | 0 | 99 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 99 | 1357 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc6_22x`) (sent_id: `deanon_TRAIN/10Nc6_22x_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei PhD Ignaz Nardelli, vertreten durch Skribe Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Diethard Eisenlöffel, Bakk. phil., Vereinigtes Königreich, wegen 82,39 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Skribe Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `PhD Ignaz Nardelli`(person)
- `Diethard Eisenlöffel, Bakk. phil.`(person)
- `Bezirksgericht Schwechat`(organisation)

**Example 1** (doc_id: `deanon_TRAIN/10Ob12_24y`) (sent_id: `deanon_TRAIN/10Ob12_24y_5`)


Isidor Janofske, beide vertreten durch Ghendler Ruvinskij Rechtsanwaltsgesellschaft mbH in Wien, gegen die beklagte Partei Wolfram Fritzsche S.p.A., VetR Lukas Dickhaus, vertreten durch bpv Hügel Rechtsanwälte GmbH in Wien, wegen 71.425,56 EUR sA, aus Anlass der Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 20. Dezember 2023, GZ 6 R 68/23a-41, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 21. August 2023, GZ 19 Cg 10/22f-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die gemeinsame Anzeige der Parteien über das vereinbarte „ewige“ Ruhen des Verfahrens wird zur Kenntnis genommen.

**False Positives:**

- `Ghendler Ruvinskij Rechtsanwaltsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Isidor Janofske`(person)
- `Wolfram Fritzsche`(person)
- `VetR Lukas Dickhaus`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Ob13_15g`) (sent_id: `deanon_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Zoltan Alfermann, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei DonauFurtostBildung GmbH, KzlR Noah Christansen, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Lederer Rechtsanwalt Gmb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zoltan Alfermann`(person)
- `DonauFurtostBildung GmbH`(organisation)
- `KzlR Noah Christansen`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob21_15h`) (sent_id: `deanon_TRAIN/10Ob21_15h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Kotschenreuther u. Abele Planung GmbH, Janis Krentzel, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, gegen die beklagte Partei Mittel Keltal GmbH, Julian Grebener, vertreten durch Stolz & Schartner Rechtsanwälte GmbH in Radstadt, wegen 7.731,06 EUR und Feststellung (Streitwert 20.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse insgesamt 11.597,42 EUR) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 14. Jänner 2015, GZ 4 R 216/14h-36, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Vavrovsky Heine Marth Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Kotschenreuther u. Abele Planung GmbH`(organisation)
- `Janis Krentzel`(person)
- `Mittel Keltal GmbH`(organisation)
- `Julian Grebener`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob23_18g`) (sent_id: `deanon_TRAIN/10Ob23_18g_4`)


Severin Simaitis, geboren 20. November 2002, 2. 8. Juli 1967, geboren 17. November 2004, und 3. Nepomuk Sprinzl, geboren 11. September 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Miklos Stiening, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Doschek Rechtsanwalts Gmb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Severin Simaitis`(person)
- `20. November`(date)
- `8. Juli 1967`(date)
- `17. November`(date)
- `Nepomuk Sprinzl`(person)
- `11. September`(date)
- `Mag. Miklos Stiening`(person)

**Example 5** (doc_id: `deanon_TRAIN/10Ob2_20x`) (sent_id: `deanon_TRAIN/10Ob2_20x_4`)


Matzka und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Ignaz Jungmichel, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei TalAlvalRobotik AG, Delila Leiteritz, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 25.617,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 29. Oktober 2019, GZ 2 R 151/19t-23, mit dem das Urteil des Landesgerichts Linz vom 21. August 2019, GZ 5 Cg 118/18z-19, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

**False Positives:**

- `Poduschka Anwaltsgesellschaft` — no gold match — likely missing annotation
- `Pressl Endl Heinrich Bamberger Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Ignaz Jungmichel`(person)
- `TalAlvalRobotik AG`(organisation)
- `Delila Leiteritz`(person)

**Example 6** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Dr. Marlon Richel, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Freimut & Assenov Sicherheit GmbH in Liqu, Spazgasse 41, 8524 Greim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 31.596,47 EUR und Feststellung (6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 18. Juni 2019, GZ 129 R 50/19z-21, mit dem das Urteil des Handelsgerichts Wien vom 28. März 2019, GZ 54 Cg 71/18x-17, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Vogl Rechtsanwalt Gmb` — no gold match — likely missing annotation
- `Wess Kux Kispert` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Dr. Marlon Richel`(person)
- `Freimut & Assenov Sicherheit GmbH`(organisation)
- `Spazgasse 41, 8524 Greim, Österreich`(address)

**Example 7** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Daniel Wiegand, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei West-Medien Manufaktur GmbH in Liqu, Kanzelweg 32, 4850 Oberthalheim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Vogl Rechtsanwalt Gmb` — no gold match — likely missing annotation
- `Wess Kux Kispert` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `DI Daniel Wiegand`(person)
- `West-Medien Manufaktur GmbH`(organisation)
- `Kanzelweg 32, 4850 Oberthalheim, Österreich`(address)

**Example 8** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_4`)


Matzka und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Techn R Heidrun Imai, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1.

**False Positives:**

- `Poduschka Anwaltsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Techn R Heidrun Imai`(person)

**Example 9** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_6`)


OberTratraSoftware Dienstleistungen AG, Prägrader Weg 43, 8616 Gasen, Österreich, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung (5.000 EUR) und 11.561,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2019, GZ 2 R 140/19z-30, mit dem das Urteil des Landesgerichts Wels vom 22. Juli 2019, GZ 26 Cg 66/18m-26, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

**False Positives:**

- `Pressl Endl Heinrich Bamberger Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OberTratraSoftware Dienstleistungen AG`(organisation)
- `Prägrader Weg 43, 8616 Gasen, Österreich`(address)

**Example 10** (doc_id: `deanon_TRAIN/10Ob88_19t`) (sent_id: `deanon_TRAIN/10Ob88_19t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Fatima Berlin, BSc, vertreten durch Frysak & Frysak Rechtsanwalts-Partnerschaft in Wien, gegen die beklagte Partei Otto Cesar, MSc, vertreten durch Maraszto Milisits Rechtsanwälte OG in Wien, wegen 18.800 EUR sA und Feststellung (Streitwert 5.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 14. Oktober 2019, GZ 11 R 145/19b-16, womit das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 28. Mai 2019, GZ 27 Cg 6/19d-11, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Maraszto Milisits Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Fatima Berlin, BSc`(person)
- `Otto Cesar, MSc`(person)

**Example 11** (doc_id: `deanon_TRAIN/10ObS21_10a`) (sent_id: `deanon_TRAIN/10ObS21_10a_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Schinko als Vorsitzenden, die Hofräte Dr. Fellinger und Dr. Hoch sowie die fachkundigen Laienrichter Mag. Irene Kienzl (aus dem Kreis der Arbeitgeber) und Eva-Maria Florianschütz (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Gertrud Johanna Ostrovska, gegen die beklagte Partei Steiermärkische Gebietskrankenkasse, 8011 Graz, Josef-Pongratz-Platz 1, vertreten durch Das Haus des Rechts Rechtsanwälte Destaller-Mader in Graz, wegen Kostenübernahme, infolge Rekurses der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 19. November 2009, GZ 8 Rs 73/09f-10, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 1. September 2009, GZ 29 Cgs 90/09s-6, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Das Haus` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ostrovska`(person)

**Example 12** (doc_id: `deanon_TRAIN/10ObS49_15a`) (sent_id: `deanon_TRAIN/10ObS49_15a_4`)


Brigitte Augustin (aus dem Kreis der Arbeitgeber) und Peter Schönhofer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Samantha Neunteufl, Deutschland, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Vorarlberger Gebietskrankenkasse, Jahngasse 4, 6850 Dornbirn, vertreten durch Hoffmann & Brandstätter Rechtsanwälte KG in Innsbruck, wegen Kinderbetreuungsgeld, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 12. Februar 2015, GZ 11 Rs 4/15k-10, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 28. Oktober 2014, GZ 20 Cgs 71/14k-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Mahringer Steinwender Bestebner Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Samantha Neunteufl`(person)

**Example 13** (doc_id: `deanon_TRAIN/10ObS92_17b`) (sent_id: `deanon_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Dr.in Gerlinde Saltzmann, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Mahringer Steinwender Bestebner Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr.in Gerlinde Saltzmann`(person)

**Example 14** (doc_id: `deanon_TRAIN/17Ob10_20z`) (sent_id: `deanon_TRAIN/17Ob10_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätinnen Mag. Malesich und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Levi Adelwart, vertreten durch Stephan Briem Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Dr. Penelope Piephans als Treuhänder der Insolvenzgläubiger der Valkraftfen-Analyse Aktiengesellschaft, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH in Linz, wegen Feststellung (Streitwert 18.335,66 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. März 2020, GZ 1 R 31/20i-13, womit das Urteil des Landesgerichts Linz vom 9. Dezember 2019, GZ 4 Cg 73/18z-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Stephan Briem Rechtsanwalt Gmb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Levi Adelwart`(person)
- `Dr. Penelope Piephans`(person)
- `Valkraftfen-Analyse Aktiengesellschaft`(organisation)

**Example 15** (doc_id: `deanon_TRAIN/1Ob192_11h`) (sent_id: `deanon_TRAIN/1Ob192_11h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Hamberg Marine Limited, London, Kapellergasse 9, 4925 Lungdorf, Österreich, vertreten durch Thum Weinreich Schwarz Fuchsbauer Rechtsanwälte OG in St. Pölten, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 1,8 Mio EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Juni 2011, GZ 14 R 214/10h-39, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 3. September 2010, GZ 33 Cg 3/09t-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Thum Weinreich Schwarz Fuchsbauer Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hamberg Marine Limited`(organisation)
- `Kapellergasse 9, 4925 Lungdorf, Österreich`(address)

**Example 16** (doc_id: `deanon_TRAIN/2Ob91_22d`) (sent_id: `deanon_TRAIN/2Ob91_22d_4`)


Sloboda und Dr. Kikinger als weitere Richter in der Rechtssache der klagenden Partei Farina Dirker, vertreten durch Dr. Sven Rudolf Thorstensen, LL.M., Rechtsanwalt in Wien, gegen die beklagte Partei Lüttge Chemie Limited, René Luidthard, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 40.150,26 EUR sA, im Verfahren über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. Februar 2022, GZ 15 R 171/21h-33, den Beschluss gefasst:  Spruch Die Zurücknahme der Revision wird zur Kenntnis genommen.

**False Positives:**

- `Brandl Talos Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Farina Dirker`(person)
- `Lüttge Chemie Limited`(organisation)
- `René Luidthard`(person)

**Example 17** (doc_id: `deanon_TRAIN/2Ob99_18z`) (sent_id: `deanon_TRAIN/2Ob99_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden, den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé sowie die Hofräte Dr. Nowotny und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Stadt-Textil GmbH & Co KG, Kreuzlandstraße 52, 9462 Kalchberg, Österreich, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Kazlowski + Röttjer Automotive GmbH, Clarissa Lenschau, vertreten durch Keschmann Rechtsanwalts-GmbH in Wien, sowie die Nebenintervenientinnen 1. Ost-Chemie GmbH, M.-Klieber-Gasse 22, 3611 Himberg, Österreich, vertreten durch Dr. Dirk Just, Rechtsanwalt in Wien, 2.

**False Positives:**

- `Keschmann Rechtsanwalts` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stadt-Textil GmbH`(organisation)
- `Co KG`(organisation)
- `Kreuzlandstraße 52, 9462 Kalchberg, Österreich`(address)
- `Kazlowski + Röttjer Automotive GmbH`(organisation)
- `Clarissa Lenschau`(person)
- `Ost-Chemie GmbH`(organisation)
- `M.-Klieber-Gasse 22, 3611 Himberg, Österreich`(address)

**Example 18** (doc_id: `deanon_TRAIN/3Ob137_17v`) (sent_id: `deanon_TRAIN/3Ob137_17v_4`)


Siegfried Littwinsky, geboren am 20. Februar 2007, 2. Ada Damien, geboren am 2. Februar 2009, beide wohnhaft beim Vater Mag. Nepomuk Chimenti, dieser vertreten durch Dr. Johann Etienne Korab, Rechtsanwalt in Wien, über den außerordentlichen Revisionsrekurs der Mutter Mag. Floriane Platvoet, vertreten durch Hornek Hubacek Lichtenstrasser Rechtsanwälte OG in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 15. Mai 2017, GZ 48 R 101/17b-137, womit Punkt 1. und 2. des Beschlusses des Bezirksgerichts Döbling vom 9. Jänner 2017, GZ 1 Ps 119/13b-90, bestätigt wurde, den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Hornek Hubacek Lichtenstrasser Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Siegfried Littwinsky`(person)
- `20. Februar`(date)
- `Ada Damien`(person)
- `2. Februar`(date)
- `Mag. Nepomuk Chimenti`(person)
- `Mag. Floriane Platvoet`(person)

**Example 19** (doc_id: `deanon_TRAIN/3Ob147_20v`) (sent_id: `deanon_TRAIN/3Ob147_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Kraftnorost Wind GmbH, Roderich Holtze, vertreten durch Mag. Andreas Kleiber, Rechtsanwalt in Wien, gegen die beklagte Partei Annette Fiss verein Ing. Kirstin Movcan, vertreten durch Pflaum Karlberger Wiener Opetnik, Rechtsanwälte in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 22. Juli 2020, GZ 40 R 37/20t-27, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Pflaum Karlberger Wiener Opetnik` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Kraftnorost Wind GmbH`(organisation)
- `Roderich Holtze`(person)
- `Annette Fiss`(person)
- `Ing. Kirstin Movcan`(person)

**Example 20** (doc_id: `deanon_TRAIN/3Ob14_24s`) (sent_id: `deanon_TRAIN/3Ob14_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Exekutionssache der betreibenden Partei Daniela Sklenar SE, Kimberly Hurrelmeyer, vertreten durch Cerha Hempel Rechtsanwälte GmbH in Wien, gegen die verpflichtete Partei Staat Libyen, StR Violetta Stegemeyer, Libyen, vertreten durch Binder Grösswang Rechtsanwälte GmbH in Wien, wegen 10 Mio EUR sA, über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 20. Oktober 2023, GZ 47 R 228/23m-107, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 78 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Cerha Hempel Rechtsanw` — no gold match — likely missing annotation
- `Binder Gr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Daniela Sklenar`(person)
- `Kimberly Hurrelmeyer`(person)
- `StR Violetta Stegemeyer`(person)

**Example 21** (doc_id: `deanon_TRAIN/3Ob178_15w`) (sent_id: `deanon_TRAIN/3Ob178_15w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Jensik als Vorsitzenden, die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Schwarzenbacher und Dr. Roch sowie die Hofrätin Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Nikolai Castelli, vertreten durch Divitschek Sieder Sauer Peter Rechtsanwälte GesBR in Deutschlandsberg, gegen die beklagte Partei Dohmgoergen Bau GmbH, Oswald Schubert, vertreten durch Dr. Johannes Liebmann, Rechtsanwalt in Gleisdorf, wegen 82.977,52 EUR sA und Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 27. Juli 2015, GZ 3 R 54/15h-145, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Divitschek Sieder Sauer Peter Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Nikolai Castelli`(person)
- `Dohmgoergen Bau GmbH`(organisation)
- `Oswald Schubert`(person)

**Example 22** (doc_id: `deanon_TRAIN/3Ob17_20a`) (sent_id: `deanon_TRAIN/3Ob17_20a_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie die Hofräte Priv.-Doz. Dr. Rassi und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Exekutionssache betreibenden Partei Heizung Werkuni Aktiengesellschaft, P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich, vertreten durch Dr. Roland Grilc ua, Rechtsanwälte in Klagenfurt am Wörthersee, gegen die verpflichtete Partei Dorothea Eiken Bank, Peter Eitenmüller, vertreten durch Diwok Hermann Petsche Rechtsanwälte LLP Co KG in Wien, wegen 12.602.980,92 EUR sA, über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. November 2019, GZ 46 R 293/19g-18, mit dem der Beschluss des Bezirksgerichts Favoriten vom 17. April 2019, GZ 17 E 1298/19z-2, bestätigt wurde, den Beschluss gefasst:  Spruch I. Der Revisionsrekurs wird, soweit er sich gegen die Bestätigung der Exekutionsbewilligung richtet, als jedenfalls unzulässig zurückgewiesen.

**False Positives:**

- `Diwok Hermann Petsche Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Heizung Werkuni Aktiengesellschaft`(organisation)
- `P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich`(address)
- `Dorothea Eiken`(person)
- `Peter Eitenmüller`(person)
- `LLP Co KG`(organisation)

**Example 23** (doc_id: `deanon_TRAIN/3Ob1_20y`) (sent_id: `deanon_TRAIN/3Ob1_20y_4`)


Erna Wodarsch, 2. Philippa Weikl, beide vertreten durch Dr. Stefan Gloß und andere Rechtsanwälte in St. Pölten, gegen die beklagten Parteien 1. Ing. Felizia Astfalck, 2. Matthäus Adelwart, beide vertreten durch Hintermeier Pfleger Brandstätter Rechtsanwälte GesRB in St. Pölten, wegen Titelergänzung nach § 10 EO, über die Revision der klagenden Parteien gegen das Urteil des Landesgerichts St. Pölten als Berufungsgericht vom 10. September 2019, GZ 21 R 127/19p-20, womit das Urteil des Bezirksgerichts Melk vom 9. April 2019, GZ 12 C 852/18z-15, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Hintermeier Pfleger Brandst` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Erna Wodarsch`(person)
- `Philippa Weikl`(person)
- `Ing. Felizia Astfalck`(person)
- `Matthäus Adelwart`(person)

**Example 24** (doc_id: `deanon_TRAIN/3Ob26_23d`) (sent_id: `deanon_TRAIN/3Ob26_23d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Florentin Rosskämmer, vertreten durch Mag. Christopher Schmied, Rechtsanwalt in Salzburg, gegen die beklagte Partei Marktgemeinde ÖkR Priv.-Doz. Björn Gustloff, vertreten durch Ebner Aichinger Guggenberger Rechtsanwälte GmbH in Salzburg, wegen Feststellung einer Dienstbarkeit und Beseitigung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 7. Dezember 2022, GZ 3 R 142/22f-17, womit das Urteil des Landesgerichts Salzburg vom 29. September 2022, GZ 9 Cg 47/22w-12, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Ebner Aichinger Guggenberger Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Florentin Rosskämmer`(person)
- `ÖkR Priv.-Doz. Björn Gustloff`(person)

**Example 25** (doc_id: `deanon_TRAIN/3Ob32_17b`) (sent_id: `deanon_TRAIN/3Ob32_17b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hoch als Vorsitzenden sowie die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Jensik und Dr. Roch und die Hofrätin Dr. Kodek als weitere Richter in der Exekutionssache der betreibenden Partei HR Dr.in RgR Johanna Drestomark, Italien, vertreten durch Oberhammer Rechtsanwälte GmbH in Wien, wider die verpflichtete Partei Prosten und Kreutzinger Bau gesellschaft mbH, Dr.Viktor-Kaplan-Straße 8, 4920 Weiketsedt, Österreich, vertreten durch Dr. Daniel Charim und Mag. Jakob Charim, Rechtsanwälte in Wien, wegen (restlich) 347.093,53 EUR sA über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 7. Dezember 2016, GZ 46 R 323/16i-61, womit der Beschluss des Bezirksgerichts Josefstadt vom 24. Juni 2016, GZ 11 E 2966/11p-56, bestätigt wurde, den Beschluss gefasst:  Spruch I.Der Revisionsrekurs der verpflichteten Partei wird, soweit er die Bestätigung der Exekutionsbewilligung bekämpft, als jedenfalls unzulässig zurückgewiesen.

**False Positives:**

- `Oberhammer Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `HR Dr.in RgR Johanna Drestomark`(person)
- `Prosten und Kreutzinger Bau gesellschaft mbH`(organisation)
- `Dr.Viktor-Kaplan-Straße 8, 4920 Weiketsedt, Österreich`(address)

**Example 26** (doc_id: `deanon_TRAIN/4Ob100_13d`) (sent_id: `deanon_TRAIN/4Ob100_13d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Verein Erwin Sieferer, vertreten durch Kosesnik-Wehrle & Langer Rechtsanwälte KG in Wien, gegen die beklagte Partei Lebensmittel Seeder -Aktiengesellschaft, Knechtswies 63, 4692 Niederau, Österreich, vertreten durch Raits Bleiziffer Rechtsanwälte GmbH in Salzburg, und die Nebenintervenientin auf Seiten der beklagten Partei „ StR Thobias Broß ” Viola Hüßkes, vertreten durch Dr. Peter Zöchbauer und andere Rechtsanwälte in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert 36.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz vom 19. April 2013, GZ 1 R 192/12d-14, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Raits Bleiziffer Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Erwin Sieferer`(person)
- `Lebensmittel Seeder`(organisation)
- `Knechtswies 63, 4692 Niederau, Österreich`(address)
- `StR Thobias Broß`(person)
- `Viola Hüßkes`(person)

**Example 27** (doc_id: `deanon_TRAIN/4Ob113_24g`) (sent_id: `deanon_TRAIN/4Ob113_24g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schwarzenbacher als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Mag. Istjan, LL.M., und Mag. Waldstätten und den Hofrat Dr. Stiefsohn als weitere Richter in der Rechtssache der klagenden Partei Vierziger u. Tewald Wind GmbH, Claire Lüdermann, Bakk. rer. nat., vertreten durch Grassner Rechtsanwalts GmbH in Linz, gegen die beklagte Partei Milena Buchmayr, vertreten durch Dr. Manfred Palkovits, Mag. Martin Sohm, Rechtsanwälte in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 24. April 2024, GZ 38 R 247/23i-46, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Grassner Rechtsanwalts Gmb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Vierziger u. Tewald Wind GmbH`(organisation)
- `Claire Lüdermann, Bakk. rer. nat.`(person)
- `Milena Buchmayr`(person)

**Example 28** (doc_id: `deanon_TRAIN/4Ob114_14i`) (sent_id: `deanon_TRAIN/4Ob114_14i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei OMedR Prof.in Agatha Schöbeck, vertreten durch Dr. Riedl & Dr. Ludwig Rechtsanwälte GmbH in Haag, gegen die beklagte Partei Mag. Gerald Robker, vertreten durch Gloss Pucher Leitner Schweinzer Burger Gloss, Rechtsanwälte in St. Pölten, wegen Ehescheidung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts St. Pölten als Berufungsgericht vom 9. April 2014, GZ 23 R 121/14p-43, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Gloss Pucher Leitner Schweinzer Burger Gloss` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OMedR Prof.in Agatha Schöbeck`(person)
- `Mag. Gerald Robker`(person)

**Example 29** (doc_id: `deanon_TRAIN/4Ob136_11w`) (sent_id: `deanon_TRAIN/4Ob136_11w_5`)


Lee Tinnemeyer, 2. Mag. Romana Weisbrodt, beide vertreten durch Mag. Ulrich Salburg, Rechtsanwalt in Wien, gegen die beklagte Partei Nexbach-Marine AG, StR Hon.-Prof.in Linda Tarak, vertreten durch Kunz Schima Wallentin Rechtsanwälte OEG in Wien, wegen 60.626,11 EUR sA, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. November 2011, GZ 1 R 242/10f-21, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Kunz Schima Wallentin Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Lee Tinnemeyer`(person)
- `Mag. Romana Weisbrodt`(person)
- `Nexbach-Marine AG`(organisation)
- `StR Hon.-Prof.in Linda Tarak`(person)

**Example 30** (doc_id: `deanon_TRAIN/4Ob162_18d`) (sent_id: `deanon_TRAIN/4Ob162_18d_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei XDC Druck GmbH, Scarlett Augustus, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Wien, gegen die beklagte Partei UBER B.V., Larissa Ebele, Niederlande, vertreten durch Schönherr Rechtsanwälte GmbH in Wien, wegen Unterlassung, Veröffentlichung und Feststellung (Streitwert im Sicherungsverfahren 70.000 EUR), über den Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 4. Juli 2018, GZ 3 R 32/18z-14, mit dem der Beschluss des Handelsgerichts Wien vom 24. April 2018, GZ 58 Cg 10/18f-6, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird teilweise Folge gegeben.

**False Positives:**

- `Vavrovsky Heine Marth Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `XDC Druck GmbH`(organisation)
- `Scarlett Augustus`(person)
- `Larissa Ebele`(person)

**Example 31** (doc_id: `deanon_TRAIN/4Ob188_14x`) (sent_id: `deanon_TRAIN/4Ob188_14x_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Bachkelwerk Pflege AG, Eva Selcuk, vertreten durch Ebert Huber Swoboda Oswald & Partner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Christiane Rechenauer e.U., Dossenweg 6, 4924 Dundeck, Österreich, vertreten durch Dr. Patrick Ruth, Rechtsanwalt in Innsbruck, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 34.900 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz vom 5. August 2014, GZ 2 R 139/14w-13, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Ebert Huber Swoboda Oswald` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bachkelwerk Pflege AG`(organisation)
- `Eva Selcuk`(person)
- `Christiane Rechenauer`(person)
- `Dossenweg 6, 4924 Dundeck, Österreich`(address)

**Example 32** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_4`)


Kff. Marion Hemmke, vertreten durch Berger Saurer Zöchbauer, Rechtsanwälte in Wien, gegen die beklagten Parteien 1.

**False Positives:**

- `Berger Saurer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_TRAIN/4Ob196_10t`) (sent_id: `deanon_TRAIN/4Ob196_10t_6`)


JQV Finanzen Gruppe GmbH, Innovationsplatz 79, 9751 Nigglai, Österreich, beide vertreten durch Ruggenthaler Rechtsanwalts KG in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 62.000 EUR) über den außerordentlichen Revisionsrekurs der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Wien vom 20. September 2010, GZ 30 R 29/10w-9, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Ruggenthaler Rechtsanwalts` — partial — pred is substring of gold: `Ruggenthaler Rechtsanwalts KG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `JQV Finanzen Gruppe GmbH`(organisation)
- `Innovationsplatz 79, 9751 Nigglai, Österreich`(address)
- `Ruggenthaler Rechtsanwalts KG`(organisation)

**Example 34** (doc_id: `deanon_TRAIN/4Ob201_10b`) (sent_id: `deanon_TRAIN/4Ob201_10b_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Wendelin Wetekamp OEG, KzlR Ibrahim Kocaslan, vertreten durch Dr. Martin Leitner und Dr. Ralph Trischler, Rechtsanwälte in Wien, gegen die beklagte Partei Feddes KI GmbH, KommR Waldemar Holzhaider, vertreten durch Bichler Zrzavy Rechtsanwälte GmbH in Wien, wegen Unterlassung, Beseitigung, Rechnungslegung, Schadenersatz und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 36.000 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 27. September 2010, GZ 1 R 192/10b-13, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß Der Antrag auf Zuspruch der Kosten der Revisionsrekursbeantwortung wird gemäß § 508a Abs 2 Satz 2 und § 521a Abs 2 ZPO abgewiesen.

**False Positives:**

- `Bichler Zrzavy Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wendelin Wetekamp`(person)
- `KzlR Ibrahim Kocaslan`(person)
- `Feddes KI GmbH`(organisation)
- `KommR Waldemar Holzhaider`(person)

**Example 35** (doc_id: `deanon_TRAIN/4Ob24_11z`) (sent_id: `deanon_TRAIN/4Ob24_11z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei DI Gundula Vielmäder, vertreten durch Proksch & Fritzsche Rechtsanwälte OG in Wien, gegen die beklagte Partei Dr. Theodor Huetter, vertreten durch Ploil Krepp & Partner Rechtsanwälte GmbH in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 24. November 2010, GZ 39 R 292/10w-31, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Ploil Krepp` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `DI Gundula Vielmäder`(person)
- `Dr. Theodor Huetter`(person)

**Example 36** (doc_id: `deanon_TRAIN/4Ob69_14x`) (sent_id: `deanon_TRAIN/4Ob69_14x_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Schenk als Vorsitzende und die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Univ.-Prof. Dr. Anita Christöphler, vertreten durch Riesemann Rechtsanwalts GmbH in Graz, gegen die beklagte Partei Husein E‑Commerce GmbH, Dolores Linse, Deutschland, vertreten durch Dr. Peter Schlösser, Rechtsanwalt in Graz, wegen Unterlassung, Beseitigung, Urteilsveröffentlichung, Rechnungslegung und Zahlung (Streitwert im Sicherungsverfahren 50.000 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz vom 5. März 2014, GZ 5 R 20/14x-21, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Riesemann Rechtsanwalts Gmb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Anita Christöphler`(person)
- `Husein E‑Commerce GmbH`(organisation)
- `Dolores Linse`(person)

**Example 37** (doc_id: `deanon_TRAIN/4Ob90_16p`) (sent_id: `deanon_TRAIN/4Ob90_16p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Vogel als Vorsitzenden und die Hofräte Dr. Jensik, Dr. Musger, Dr. Schwarzenbacher und Dr. Rassi als weitere Richter in der Rechtssache der klagenden Partei Lebensmittel Glanzconuni AG, Immanuel Gspan, vertreten durch Fellner Wratzfeld & Partner Rechtsanwälte GmbH in Wien, gegen die beklagten Parteien 1. Fridolin Braunhold, 2. Mag. Frauke Steinweg, und 3. DonauLexlogbruckPlanung GmbH, Felberbachstraße 4, 3631 Jungschlag, Österreich, alle vertreten durch Dr. Peter Zöchbauer, Rechtsanwalt in Wien, wegen Unterlassung (Streitwert 102.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Februar 2016, GZ 2 R 93/15h-25, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Fellner Wratzfeld` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Lebensmittel Glanzconuni AG`(organisation)
- `Immanuel Gspan`(person)
- `Fridolin Braunhold`(person)
- `Mag. Frauke Steinweg`(person)
- `DonauLexlogbruckPlanung GmbH`(organisation)
- `Felberbachstraße 4, 3631 Jungschlag, Österreich`(address)

**Example 38** (doc_id: `deanon_TRAIN/4Ob98_20w`) (sent_id: `deanon_TRAIN/4Ob98_20w_4`)


Matzka als weitere Richter in der Rechtssache der Klägerin Dr. Imre Grosse-Budde, vertreten durch Huber Swoboda Oswald Aixberger Rechtsanwälte GmbH in Wien, gegen die Beklagte IFS Telekom Technologien GmbH, Großtaxen 13, 6345 Kössen, Österreich, vertreten durch Wiedenbauer Mutz Winkler & Partner Rechtsanwälte GmbH in Wien, und die Nebenintervenienten auf Seiten der Beklagten 1.

**False Positives:**

- `Huber Swoboda Oswald Aixberger Rechtsanw` — no gold match — likely missing annotation
- `Wiedenbauer Mutz Winkler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Dr. Imre Grosse-Budde`(person)
- `IFS Telekom Technologien GmbH`(organisation)
- `Großtaxen 13, 6345 Kössen, Österreich`(address)

**Example 39** (doc_id: `deanon_TRAIN/4Ob9_20g`) (sent_id: `deanon_TRAIN/4Ob9_20g_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Ing. KzlR MedR Brunhild Syndikus, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1) Böhnstedt+Bittlmeier Verlag GmbH, Wien Traalmon Betriebe, und 2) TraunBau AG, Schneeballenweg 6, 4232 Penzendorf, Österreich, beide vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 11.091,23 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 6. November 2019, GZ 2 R 158/19x-27, mit dem das Urteil des Landesgerichts Linz vom 29. August 2019, GZ 36 Cg 14/18h-22, bestätigt wurde, den Beschluss gefasst:  Spruch I. Das Revisionsverfahren zu 4 Ob 9/20g wird bis zur Vorabentscheidung des Gerichtshofs der Europäischen Union über das Vorabentscheidungsersuchen des Obersten Gerichtshofs vom 17.

**False Positives:**

- `Poduschka Anwaltsgesellschaft` — no gold match — likely missing annotation
- `Pressl Endl Heinrich Bamberger Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Ing. KzlR MedR Brunhild Syndikus`(person)
- `Böhnstedt+Bittlmeier Verlag GmbH`(organisation)
- `Wien Traalmon Betriebe`(organisation)
- `TraunBau AG`(organisation)
- `Schneeballenweg 6, 4232 Penzendorf, Österreich`(address)

**Example 40** (doc_id: `deanon_TRAIN/5Ob18_11z`) (sent_id: `deanon_TRAIN/5Ob18_11z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und die Hofrätinnen Dr. Hurch und Dr. Lovrek sowie die Hofräte Dr. Höllwerth und Mag. Wurzer als weitere Richter in der Rechtssache der klagenden Partei DI Borislav Viskorf, vertreten durch Dr. Günter Niebauer, Rechtsanwalt in Wien, und der Nebenintervenientin auf Seiten der klagenden Partei Mittel Waldheim Betriebe AG, Samantha Althöfer, vertreten durch Mayer & Herrmann, Rechtsanwälte in Wien, gegen die beklagte Partei Weckebrod Immobilien Aktiengesellschaft, Graf Geroldstraße 2, 8181 Dörfl an der Raab, Österreich, vertreten durch Kunz Schima Wallentin Rechtsanwälte OG in Wien, wegen 96.882,93 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Oktober 2010, GZ 2 R 213/09x, 2 R 216/09p-27, mit dem infolge Berufung der beklagten Partei das Urteil des Handelsgerichts Wien vom 24. Juli 2009, GZ 19 Cg 167/08t-19, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Kunz Schima Wallentin Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Viskorf`(person)
- `Mittel Waldheim Betriebe AG`(organisation)
- `Samantha Althöfer`(person)
- `Weckebrod Immobilien Aktiengesellschaft`(organisation)
- `Graf Geroldstraße 2, 8181 Dörfl an der Raab, Österreich`(address)

**Example 41** (doc_id: `deanon_TRAIN/5Ob206_24s`) (sent_id: `deanon_TRAIN/5Ob206_24s_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Painsi, Dr. Weixelbraun-Mohr, Dr. Steger und Dr. Pfurtscheller als weitere Richter in der wohnrechtlichen Außerstreitsache des Antragstellers OMedR Louisa Dutzke, vertreten durch Mag. Wolfgang Doppelhofer LL.M. LL.M., Rechtsanwalt in Wien, gegen die Antragsgegnerin Alsud-Pflege GmbH, Kirchenwaldweg 10, 3104 St. Pölten, Österreich, vertreten durch Weishaupt Horak Georgiev Rechtsanwälte GmbH & Co KG in Wien, wegen Feststellung der Ausstattungskategorie nach § 15a MRG, über den Revisionsrekurs der Antragsgegnerin gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 26. August 2024, GZ 39 R 144/24a-22, mit dem der Sachbeschluss des Bezirksgerichts Hietzing vom 29. Mai 2024, GZ 9 MSch 18/23k-18, aufgehoben wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Weishaupt Horak Georgiev Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OMedR Louisa Dutzke`(person)
- `Alsud-Pflege GmbH`(organisation)
- `Kirchenwaldweg 10, 3104 St. Pölten, Österreich`(address)
- `Co KG`(organisation)

**Example 42** (doc_id: `deanon_TRAIN/6Ob10_22x`) (sent_id: `deanon_TRAIN/6Ob10_22x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Nowotny, Dr. Hofer-Zeni-Rennhofer, Dr. Faber und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Mozar und Kuebler Daten Versicherungs AG, Grindelstraße 99, 4723 Tal, Österreich, vertreten durch Musey Rechtsanwalt GmbH in Salzburg, gegen die beklagte Partei Maschinenbau Ostlogber GmbH, Richarda Vetterer, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 7.246.839 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 1. Dezember 2021, GZ 2 R 165/21d-49, womit das Teil- und Zwischenurteil des Landesgerichts Salzburg vom 6. September 2021, GZ 6 Cg 16/20m-45, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Musey Rechtsanwalt Gmb` — no gold match — likely missing annotation
- `Pressl Endl Heinrich Bamberger Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Mozar und Kuebler Daten`(organisation)
- `Grindelstraße 99, 4723 Tal, Österreich`(address)
- `Maschinenbau Ostlogber GmbH`(organisation)
- `Richarda Vetterer`(person)

**Example 43** (doc_id: `deanon_TRAIN/6Ob118_16w`) (sent_id: `deanon_TRAIN/6Ob118_16w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden und durch die Hofräte Dr. Schramm, Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Ing. Melinda Jastrembski, vertreten durch Dr. Wolfgang Leitner, Priv.-Doz. Dr. Max Leitner, Dr. Mara-Sophie Häusler, Rechtsanwälte in Wien, gegen die beklagte Partei Heiko Radziwil, vertreten durch Lederer Rechtsanwalt GmbH in Wien, und der Nebenintervenienten auf Seite der beklagten Partei 1.

**False Positives:**

- `Lederer Rechtsanwalt Gmb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ing. Melinda Jastrembski`(person)
- `Heiko Radziwil`(person)

**Example 44** (doc_id: `deanon_TRAIN/6Ob118_16w`) (sent_id: `deanon_TRAIN/6Ob118_16w_4`)


SeeAlheimsudMedien Institut GmbH in Liquidation, LNMT Cloud, 2. WEA Robotik GmbH, Selpritscher Weg 52, 4951 Polling im Innkreis, Österreich, Deutschland, beide vertreten durch Wess Kispert Rechtsanwalts GmbH in Wien, wegen 103.578,16 EUR sA und Feststellung, über die Rekurse der beklagten Partei und der Nebenintervenienten gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 13. April 2016, GZ 14 R 173/16m-39, womit das Urteil des Landesgerichts Eisenstadt vom 31. August 2015, GZ 3 Cg 166/13y-34, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Den Rekursen wird nicht Folge gegeben.

**False Positives:**

- `Wess Kispert Rechtsanwalts Gmb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `SeeAlheimsudMedien Institut GmbH`(organisation)
- `LNMT Cloud`(organisation)
- `WEA Robotik GmbH`(organisation)
- `Selpritscher Weg 52, 4951 Polling im Innkreis, Österreich`(address)

**Example 45** (doc_id: `deanon_TRAIN/6Ob123_19k`) (sent_id: `deanon_TRAIN/6Ob123_19k_5`)


Li Krautsch, alle vertreten durch Saxinger Chalupsky & Partner Rechtsanwälte GmbH in Wien, wegen Feststellung, über die Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. März 2019, GZ 11 R 28/19x-17, womit über Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 3. Dezember 2018, GZ 58 Cg 33/18a-13, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Saxinger Chalupsky` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Li Krautsch`(person)

**Example 46** (doc_id: `deanon_TRAIN/6Ob139_19p`) (sent_id: `deanon_TRAIN/6Ob139_19p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Priv.-Doz. Florian Thiesbonenkamp, LLM, vertreten durch Höhne, In der Maur & Partner Rechtsanwälte GmbH & Co KG in Wien, gegen die beklagte Partei Prof. Dr. Maximiliane Cekal, vertreten durch Brauneis Klauser Prändl Rechtsanwälte GmbH in Wien, wegen Rechnungslegung und Zahlung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 22. April 2019, GZ 14 R 152/18b-16, womit das Teilurteil des Landesgerichts für Zivilrechtssachen Wien vom 27. September 2018, GZ 4 Cg 50/17b-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Brauneis Klauser Pr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz. Florian Thiesbonenkamp, LLM`(person)
- `Co KG`(organisation)
- `Dr. Maximiliane Cekal`(person)

**Example 47** (doc_id: `deanon_TRAIN/6Ob161_10k`) (sent_id: `deanon_TRAIN/6Ob161_10k_5`)


Nigel Frömmke, vertreten durch Dr. Josef Olischar und Dr. Johannes Olischar, Rechtsanwälte in Wien, gegen die Antragsgegnerin Republik Österreich, vertreten durch WienEvent GmbH, Oweges C 64, 4115 Apfelsbach, Österreich, vertreten durch Fellner Wratzfeld & Partner Rechtsanwälte GmbH in Wien, wegen Festsetzung einer Enteignungsentschädigung, über den Revisionsrekurs der Antragsgegnerin gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 27. Mai 2010, GZ 14 R 59/10i-54, womit der Beschluss des Landesgerichts Korneuburg vom 2. Februar 2010, GZ 26 Nc 3/08x-44, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Fellner Wratzfeld` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Nigel Frömmke`(person)
- `WienEvent GmbH`(organisation)
- `Oweges C 64, 4115 Apfelsbach, Österreich`(address)

**Example 48** (doc_id: `deanon_TRAIN/6Ob169_12i`) (sent_id: `deanon_TRAIN/6Ob169_12i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Pimmer als Vorsitzenden und durch die Hofräte des Obersten Gerichtshofs Dr. Schramm, Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Unlandherm KI GmbH, Ilona Hoernle, vertreten durch List Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Wickl Logistik GmbH, Vitus Glassbrenner, vertreten durch Dr. Christoph Brenner - Mag. Severin Perschl Rechtsanwälte OG in Krems, wegen 7.641,30 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Korneuburg als Berufungsgericht vom 16. Februar 2012, GZ 21 R 262/11v-50, womit das Urteil des Bezirksgerichts Gänserndorf vom 2. August 2011, GZ 12 C 1036/10h-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `List Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Unlandherm KI GmbH`(organisation)
- `Ilona Hoernle`(person)
- `Wickl Logistik GmbH`(organisation)
- `Vitus Glassbrenner`(person)

**Example 49** (doc_id: `deanon_TRAIN/6Ob18_20w`) (sent_id: `deanon_TRAIN/6Ob18_20w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Schramm als Vorsitzenden, durch die Hofräte Dr. Gitschthaler, Univ.-Prof. Dr. Kodek und Dr. Nowotny sowie durch die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Nepomuk Birkenmeier, vertreten durch Dorda Rechtsanwälte GmbH in Wien, wider die beklagte Partei Dr. Flora Lyttwin, vertreten durch Dr. Thomas Weber, Rechtsanwalt in Baden, und den Nebenintervenienten auf Seiten der beklagten Partei Dr. Lukas Riemenschneider, vertreten durch Prettenhofer Raimann Pérez Rechtsanwaltspartnerschaft in Wien, wegen Löschung und Unterlassung, über die außerordentlichen Revisionen der beklagten Partei und des Nebenintervenienten gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 19. November 2019, GZ 58 R 58/19f-36, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentlichen Revisionen werden gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dorda Rechtsanw` — no gold match — likely missing annotation
- `Prettenhofer Raimann` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Nepomuk Birkenmeier`(person)
- `Dr. Flora Lyttwin`(person)
- `Dr. Lukas Riemenschneider`(person)

**Example 50** (doc_id: `deanon_TRAIN/6Ob86_20w`) (sent_id: `deanon_TRAIN/6Ob86_20w_5`)


Juri Schlösiger, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagten Parteien 1.

**False Positives:**

- `Poduschka Anwaltsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Juri Schlösiger`(person)

**Example 51** (doc_id: `deanon_TRAIN/6Ob86_20w`) (sent_id: `deanon_TRAIN/6Ob86_20w_6`)


Solar Bruckstein GmbH, Scherrers Getränke, 2. SüdDerveruniMaschinenbau AG, Untere Hofäcker 14, 5771 Sinning, Österreich, beide vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 27.758,24 EUR sA, über die Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 5. März 2020, GZ 1 R 4/20w-44, mit dem das Urteil des Landesgerichts St. Pölten vom 28. Oktober 2019, GZ 3 Cg 62/17m-40, bestätigt wurde, den Beschluss gefasst:  Spruch Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

**False Positives:**

- `Pressl Endl Heinrich Bamberger Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Solar Bruckstein GmbH`(organisation)
- `Scherrers Getränke`(organisation)
- `SüdDerveruniMaschinenbau AG`(organisation)
- `Untere Hofäcker 14, 5771 Sinning, Österreich`(address)

**Example 52** (doc_id: `deanon_TRAIN/7Ob110_13x`) (sent_id: `deanon_TRAIN/7Ob110_13x_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin Dr. Huber als Vorsitzende und die Hofrätinnen und Hofräte Dr. Hoch, Dr. Kalivoda, Mag. Dr. Wurdinger und Mag. Malesich als weitere Richter in der Rechtssache der klagenden Partei Sudconzor-Landwirtschaft AG, Juliette Ossipenko, vertreten durch Kunz Schima Wallentin Rechtsanwälte OG in Wien, gegen die beklagte Partei Mag. (FH) Markus Voerman, vertreten durch Binder Grösswang Rechtsanwälte OG in Wien, wegen Erteilung von Auskünften, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. April 2013, GZ 11 R 75/13z-12, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Kunz Schima Wallentin Rechtsanw` — no gold match — likely missing annotation
- `Binder Gr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Sudconzor-Landwirtschaft AG`(organisation)
- `Juliette Ossipenko`(person)
- `Mag. (FH) Markus Voerman`(person)

**Example 53** (doc_id: `deanon_TRAIN/7Ob165_18t`) (sent_id: `deanon_TRAIN/7Ob165_18t_4`)


Matzka als weitere Richter in der Pflegschaftssache der mj StR Jürgen Meistermann, geboren am 15. Juli 2012, vertreten durch ihre Mutter Janis Lafflör, diese vertreten durch Maus Riedherr Rechtsanwälte OG in Salzburg, wegen Unterhalts, über den Revisionsrekurs des Vaters Mag. Ing. Bruno Chatziapostolou, vertreten durch Sattlegger, Dorninger, Steiner & Partner, Rechtsanwälte in Linz, gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 11. Juli 2018, GZ 21 R 134/18d-77, mit dem der Beschluss des Bezirksgerichts Salzburg vom 20. April 2016, GZ 4 Pu 110/15x-43, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Maus Riedherr Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `StR Jürgen Meistermann`(person)
- `15. Juli`(date)
- `Janis Lafflör`(person)
- `Ing. Bruno Chatziapostolou`(person)

**Example 54** (doc_id: `deanon_TRAIN/7Ob205_19a`) (sent_id: `deanon_TRAIN/7Ob205_19a_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Florentin Herboldt, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Wolenk und Ukininks Planung -Aktiengesellschaft, Mayr-Melnhof-Weg 66, 9842 Auen, Österreich, vertreten durch Dr. Andreas A. Lintl, Rechtsanwalt in Wien, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 11. September 2019, GZ 22 R 243/19t-11, womit das Urteil des Bezirksgerichts Salzburg vom 29. Mai 2019, GZ 16 C 627/18p-7, bestätigt wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Poduschka Anwaltsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Florentin Herboldt`(person)
- `Wolenk und Ukininks Planung`(organisation)
- `Mayr-Melnhof-Weg 66, 9842 Auen, Österreich`(address)

**Example 55** (doc_id: `deanon_TRAIN/7Ob254_18f`) (sent_id: `deanon_TRAIN/7Ob254_18f_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Svenja Nareyek, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Ost-Pflege AG, Lorena Blanknagel, vertreten durch Themmer, Toth & Partner Rechtsanwälte GmbH in Wien, wegen Feststellung, über die Revision der beklagten Partei gegen das Urteil des Handelsgerichts Wien als Berufungsgericht vom 19. Februar 2018, GZ 50 R 131/17x-10, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 29. September 2017, GZ 18 C 304/17p-6, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Poduschka Anwaltsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Svenja Nareyek`(person)
- `Ost-Pflege AG`(organisation)
- `Lorena Blanknagel`(person)

**Example 56** (doc_id: `deanon_TRAIN/7Ob48_17k`) (sent_id: `deanon_TRAIN/7Ob48_17k_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Vertra-Elektro GmbH, Camilla Niemetschek, vertreten durch Aigner Rechtsanwalts GmbH in Wien, gegen die beklagte Partei Schmerschneider Transport AG, René Weisspfenning, vertreten durch Dr. Josef Milchram, Dr. Anton Ehm und Mag. Thomas Mödlagl, Rechtsanwälte in Wien, wegen 1.373.171,48 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 20. Jänner 2017, GZ 1 R 160/16d-52, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Aigner Rechtsanwalts Gmb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Vertra-Elektro GmbH`(organisation)
- `Camilla Niemetschek`(person)
- `Schmerschneider Transport AG`(organisation)
- `René Weisspfenning`(person)

**Example 57** (doc_id: `deanon_TRAIN/7Ob85_15y`) (sent_id: `deanon_TRAIN/7Ob85_15y_4`)


Cynthia Martchenko AG, Schmidhuberstraße 73, 4792 Landertsberg, Österreich, vertreten durch Jank Weiler Operenyi Rechtsanwälte OG in Wien, 2. Reisch + Weißert Getränke AG und 3.

**False Positives:**

- `Jank Weiler Operenyi Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Cynthia Martchenko`(person)
- `Schmidhuberstraße 73, 4792 Landertsberg, Österreich`(address)
- `Reisch + Weißert Getränke AG`(organisation)

**Example 58** (doc_id: `deanon_TRAIN/7Ob85_15y`) (sent_id: `deanon_TRAIN/7Ob85_15y_5`)


Schefuss Forschung GmbH, beide Raidenstraße 62, 8354 Aigen, Österreich, vertreten durch Dorda Brugger Jordis Rechtsanwälte GmbH in Wien, wegen 7.523,16 EUR sA, über den Rekurs der erstbeklagten Partei gegen den Beschluss des Handelsgerichts Wien als Berufungsgericht vom 19. Februar 2015, GZ 1 R 6/15a-49, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 29. September 2014, GZ 13 C 134/10s-45, hinsichtlich der erstbeklagten Partei aufgehoben wurde, den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Dorda Brugger Jordis Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Schefuss Forschung GmbH`(organisation)
- `Raidenstraße 62, 8354 Aigen, Österreich`(address)

**Example 59** (doc_id: `deanon_TRAIN/8Nc31_13w`) (sent_id: `deanon_TRAIN/8Nc31_13w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn als weitere Richter in der beim Landesgericht Salzburg als Arbeits- und Sozialgericht anhängigen Rechtssache der klagenden Partei Buth Analyse GmbH, Anabel Traudtmann, vertreten durch Dr. Ernst Kohlbacher, Rechtsanwalt in Salzburg, gegen die beklagte Partei Christine Schwemmer, vertreten durch Plankel Mayrhofer & Partner, Rechtsanwälte in Dornbirn, wegen 213,52 EUR sA, über den Delegierungsantrag der beklagten Partei den Beschluss gefasst:  Spruch Der Antrag der beklagten Partei, die Rechtssache an das Arbeits- und Sozialgericht Wien zu delegieren, wird abgewiesen.

**False Positives:**

- `Plankel Mayrhofer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgericht Salzburg`(organisation)
- `Buth Analyse GmbH`(organisation)
- `Anabel Traudtmann`(person)
- `Christine Schwemmer`(person)

**Example 60** (doc_id: `deanon_TRAIN/8Ob100_19t`) (sent_id: `deanon_TRAIN/8Ob100_19t_4`)


Kraftzorstein-Telekom GmbH Karsten Öllinger, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, und 2. Univ.-Prof.in Rebecca Obermeyr GmbH Klöcklstraße 57, 9111 Berg ob Attendorf, Österreich, vertreten durch Lederer Hoff & Apfelbacher Rechtsanwälte GmbH in Wien, wegen 11.388,49 EUR sA und Feststellung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. Juni 2019, GZ 5 R 60/19h-33, mit dem das Urteil des Handelsgerichts Wien vom 12. März 2019, GZ 51 Cg 62/17z-28, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Wess Kux Kispert` — no gold match — likely missing annotation
- `Lederer Hoff` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Kraftzorstein-Telekom GmbH`(organisation)
- `Karsten Öllinger`(person)
- `Univ.-Prof.in Rebecca Obermeyr`(person)
- `Klöcklstraße 57, 9111 Berg ob Attendorf, Österreich`(address)

**Example 61** (doc_id: `deanon_TRAIN/8Ob11_11t`) (sent_id: `deanon_TRAIN/8Ob11_11t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner sowie die Hofräte Mag. Ziegelbauer und Dr. Brenn als weitere Richter in der Rechtssache der klagenden Partei, Guggeis Automotive Bank InnBildung Betriebe AG, Olga Wohlbrück-Gasse 5, 3482 Gösing am Wagram, Österreich, vertreten durch Dr. Mag. Günther Riess, Mag. Christine Schneider, Rechtsanwälte in Innsbruck, gegen die beklagte Partei Doris Froemmel, vertreten durch Czernich Hofstädter Guggenberger & Partner, Rechtsanwälte in Innsbruck, wegen 2.278.895,88 EUR sA, über die Rekurse beider Parteien gegen den Beschluss des Oberlandesgerichts Innsbruck als Berufungsgericht vom 11. Oktober 2010, GZ 4 R 168/10b-76, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Feldkirch vom 20. Mai 2010, GZ 6 Cg 71/08s-71, aufgehoben wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch 1.

**False Positives:**

- `Czernich Hofst` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Guggeis Automotive`(organisation)
- `InnBildung Betriebe AG`(organisation)
- `Olga Wohlbrück-Gasse 5, 3482 Gösing am Wagram, Österreich`(address)
- `Doris Froemmel`(person)

**Example 62** (doc_id: `deanon_TRAIN/8Ob134_19t`) (sent_id: `deanon_TRAIN/8Ob134_19t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn, den Hofrat Dr. Stefula und die Hofrätin Mag. Wessely-Kristöfel als weitere Richter in den verbundenen Rechtssachen der klagenden und widerbeklagten Parteien 1. Mag. Wendy Hoffbuhr, und 2. Dr. Janina Brüster, vertreten durch Gerlach Rechtsanwälte in Wien, gegen die beklagte und widerklagende Partei Henriette Junkherr, vertreten durch Gloß Pucher Leitner Gloß Enzenhofer Rechtsanwälte in St. Pölten, wegen Unterlassung (AZ 6 C 313/17i) und Feststellung, Einwilligung, Beseitigung und Unterlassung (AZ 6 C 342/17d), über die Revision der beklagten und widerklagenden Partei gegen das Urteil des Landesgerichts St. Pölten als Berufungsgericht vom 8. August 2019, GZ 21 R 106/19z-41, womit das Urteil des Bezirksgerichts St. Pölten vom 25. Februar 2019, GZ 6 C 313/17i-37, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Gerlach Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Wendy Hoffbuhr`(person)
- `Dr. Janina Brüster`(person)
- `Henriette Junkherr`(person)

**Example 63** (doc_id: `deanon_TRAIN/8Ob29_19a`) (sent_id: `deanon_TRAIN/8Ob29_19a_5`)


Wald Lemwald - Lemlogber Metall GmbH, Argenotstraße 81, 4871 Tiefenbach, Österreich, vertreten durch Dr. Wilfried Plattner, Rechtsanwalt in Innsbruck, 4. Bachconval-Automotive GmbH in Liqu., Förolach 3, 4952 Appersting, Österreich, vertreten durch Mag. Martin Corazza, Rechtsanwalt in Innsbruck, 5. Waltemathe KI GmbH & Co OG, Springsfield 4, 9112 Untergreutschach, Österreich, vertreten durch Wolf Theiss Rechtsanwälte GmbH & Co KG in Wien und Prader, Ortner, Fuchs, Wenzel Rechtsanwälte GesbR in Innsbruck, wegen Hinterlegung nach § 1425 ABGB, über den außerordentlichen Revisionsrekurs der Fünfterlagsgegnerin gegen den Beschluss des Landesgerichts Innsbruck als Rekursgericht vom 2. Oktober 2018, GZ 52 R 50/18m-30, den Beschluss gefasst:  Spruch I. Die Bezeichnung der Fünfterlagsgegnerin wird berichtigt auf: „ Lexder-Finanzen GmbH & Co OG“.

**False Positives:**

- `Wolf Theiss Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wald Lemwald`(organisation)
- `Lemlogber Metall GmbH`(organisation)
- `Argenotstraße 81, 4871 Tiefenbach, Österreich`(address)
- `Bachconval-Automotive GmbH`(organisation)
- `Förolach 3, 4952 Appersting, Österreich`(address)
- `Waltemathe KI GmbH`(organisation)
- `Springsfield 4, 9112 Untergreutschach, Österreich`(address)
- `Co KG`(organisation)
- `Lexder-Finanzen GmbH`(organisation)

**Example 64** (doc_id: `deanon_TRAIN/8Ob60_12z`) (sent_id: `deanon_TRAIN/8Ob60_12z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner sowie die Hofräte Mag. Ziegelbauer und Dr. Brenn als weitere Richter in der Rechtssache der klagenden Partei Arabella Witkopf, vertreten durch Mag. Renate Aigner, Rechtsanwältin in Kallham, gegen die beklagte Partei Abramczyk & Krollpfeifer Wind GmbH & Co KG, Pühra 22, 8010 Edelsbach bei Graz, Österreich, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen (Revisionsinteresse) 10.000 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 15. März 2012, GZ 3 R 42/12k-38, womit das Urteil des Landesgerichts Linz vom 28. Dezember 2011, GZ 1 Cg 167/10i-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Pressl Endl Heinrich Bamberger Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Arabella Witkopf`(person)
- `Abramczyk & Krollpfeifer Wind GmbH`(organisation)
- `Co KG`(organisation)
- `Pühra 22, 8010 Edelsbach bei Graz, Österreich`(address)

**Example 65** (doc_id: `deanon_TRAIN/8Ob7_10b`) (sent_id: `deanon_TRAIN/8Ob7_10b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Spenling als Vorsitzenden, durch den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner sowie die Hofräte Mag. Ziegelbauer und Dr. Brenn als weitere Richter in der Rechtssache der klagenden Partei DI Dr. Valerie Haesevoets, vertreten durch Kaan Cronenberg & Partner, Rechtsanwälte in Graz, gegen die beklagten Parteien 1. Ashley Völkmer, 2. Marlene Fritzer und 3. Karsten Dalkiran, alle vertreten durch Dr. Thomas Stampfer, Dr. Christoph Orgler, Rechtsanwälte in Graz, wegen 49.620 EUR sA und Feststellung (Streitwert 15.000 EUR), über die Revision der beklagten Parteien (Revisionsinteresse: 49.620 EUR) gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 19. November 2009, GZ 4 R 142/09y-38, womit über Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 19. Juni 2009, GZ 39 Cg 102/08m-32 teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Kaan Cronenberg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Valerie Haesevoets`(person)
- `Ashley Völkmer`(person)
- `Marlene Fritzer`(person)
- `Karsten Dalkiran`(person)

**Example 66** (doc_id: `deanon_TRAIN/8Ob97_16x`) (sent_id: `deanon_TRAIN/8Ob97_16x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner, den Hofrat Dr. Brenn sowie die Hofrätinnen Mag. Korn und Dr. Weixelbraun-Mohr als weitere Richter in der Rechtssache der klagenden Partei VetR Dr.in Zarin Österhellweg, vertreten durch Wiedenbauer Mutz Winkler Pramberger Rechtsanwälte GmbH in Klagenfurt, gegen die beklagte Partei APEA Solar Systeme Aktiengesellschaft, Vorderer Sonnberg 7, 2752 Wöllersdorf, Österreich, vertreten durch Dr. Ludwig Beurle, Dr. Rudolf Mitterlehner und andere, Rechtsanwälte in Linz, wegen 6.073,15 EUR sA, über die Revison der klagenden Partei gegen das Urteil des Landesgerichts Linz als Berufungsgericht vom 10. Mai 2016, GZ 32 R 127/15z-56, mit dem das Urteil des Bezirksgerichts Linz vom 7. August 2015, GZ 8 C 1185/13y-50, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Wiedenbauer Mutz Winkler Pramberger Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `VetR Dr.in Zarin Österhellweg`(person)
- `APEA Solar Systeme Aktiengesellschaft`(organisation)
- `Vorderer Sonnberg 7, 2752 Wöllersdorf, Österreich`(address)

**Example 67** (doc_id: `deanon_TRAIN/8Ob99_16s`) (sent_id: `deanon_TRAIN/8Ob99_16s_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden, die Hofrätin Dr. Tarmann-Prentner, den Hofrat Dr. Brenn sowie die Hofrätinnen Mag. Korn und Dr. Weixelbraun-Mohr als weitere Richter in der Rechtssache der klagenden Partei Wien Wilzor AG, Chiara Hellfritsch, vertreten durch Dr. Amhof & Dr. Damian GmbH Rechtsanwälte in Wien, gegen die beklagte Partei Ostfurttal-Touristik GmbH, Elias Stellmaszyk, vertreten durch Hochedlinger Luschin Marenzi Kapsch Rechtsanwälte GmbH in Wien, wegen 6.396.663,36 EUR sA, infolge Rekurses der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 25. August 2016, GZ 1 R 60/16z-14, mit dem festgestellt wurde, dass das Urteil des Landesgerichts Eisenstadt vom 18. Jänner 2014, GZ 27 Cg 47/15b-10, als nicht gefällt anzusehen sei und die Berufung sowie die Berufungsbeantwortung zurückgewiesen wurden, den Beschluss gefasst:  Spruch Der angefochtene Beschluss wird aufgehoben, die Rechtssache an das Berufungsgericht zurückverwiesen und diesem die Fortsetzung des Berufungsverfahrens aufgetragen.

**False Positives:**

- `Hochedlinger Luschin Marenzi Kapsch Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wien Wilzor AG`(organisation)
- `Chiara Hellfritsch`(person)
- `Ostfurttal-Touristik GmbH`(organisation)
- `Elias Stellmaszyk`(person)

**Example 68** (doc_id: `deanon_TRAIN/8ObA31_23a`) (sent_id: `deanon_TRAIN/8ObA31_23a_4`)


Dr. Andreas Schlegel (aus dem Kreis der Arbeitgeber) und Anton Starecek (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Ing. Zacharias Kloße, vertreten durch Doschek Rechtsanwalts GmbH in Wien, gegen die beklagte Partei EEH Landwirtschaft GmbH Gwendolin Raffelsiefer, vertreten durch Barnert Egermann Illigasch Rechtsanwälte GmbH in Wien, wegen Entlassungsanfechtung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. März 2023, GZ 8 Ra 61/22g-97, mit dem das Urteil des Landesgerichts Korneuburg vom 30. März 2022, GZ 9 Cga 43/19z-88, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Doschek Rechtsanwalts Gmb` — no gold match — likely missing annotation
- `Barnert Egermann Illigasch Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Ing. Zacharias Kloße`(person)
- `EEH Landwirtschaft GmbH`(organisation)
- `Gwendolin Raffelsiefer`(person)

**Example 69** (doc_id: `deanon_TRAIN/8ObA56_10h`) (sent_id: `deanon_TRAIN/8ObA56_10h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras und die Hofrätin Dr. Tarmann-Prentner sowie die fachkundigen Laienrichter Prof. Mag. Dr. Thomas Keppert und Franz Kisling als weitere Richter in der Arbeitsrechtssache der klagenden Partei Ing. Francois Zindl, vertreten durch Achammer und Mennel Rechtsanwälte OG in Feldkirch, wider die beklagte Partei Marktgemeinde Tatjana Nußhardt, vertreten durch Amman Jehle Juen Rechtsanwälte GmbH in Rankweil, wegen Feststellung des aufrechten Dienstverhältnisses, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 10. Juni 2010, GZ 15 Ra 2/10x-43, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Amman Jehle Juen Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ing. Francois Zindl`(person)
- `Tatjana Nußhardt`(person)

**Example 70** (doc_id: `deanon_TRAIN/9Ob10_19i`) (sent_id: `deanon_TRAIN/9Ob10_19i_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Dehn, Dr. Hargassner, Mag. Korn und Dr. Stefula in der Rechtssache der klagenden Partei See-Automotive Entwicklung GmbH, Alva Scherper, vertreten durch Partnerschaft Schuppich Sporn & Winischhofer, Rechtsanwälte in Wien, gegen die beklagte Partei DrauSuddonPharma GmbH, Gloria Rennicke, vertreten durch Vavrovsky Heine Marth Rechtsanwälte GmbH in Salzburg, wegen 6.265 EUR sA, über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts Salzburg als Berufungsgericht vom 29. November 2018, GZ 53 R 212/18k-19, mit dem der Berufung der klagenden Partei gegen das Urteil des Bezirksgerichts Salzburg vom 25. Juni 2018, GZ 17 C 965/17a-15, Folge gegeben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Partnerschaft Schuppich Sporn` — no gold match — likely missing annotation
- `Vavrovsky Heine Marth Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `See-Automotive Entwicklung GmbH`(organisation)
- `Alva Scherper`(person)
- `DrauSuddonPharma GmbH`(organisation)
- `Gloria Rennicke`(person)

**Example 71** (doc_id: `deanon_TRAIN/9Ob10_21t`) (sent_id: `deanon_TRAIN/9Ob10_21t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätinnen und Hofräte Dr. Fichtenau, Hon.-Prof. Dr. Dehn, Dr. Hargassner, und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Schnake Robotik gmbh, Jeanne Großkopf, vertreten durch Forcher-Mayr & Kantner Rechtsanwälte Partnerschaft in Innsbruck, gegen die beklagte Partei Volkmar Kapelner GmbH, Reinberg-Litschau 11, 9343 Aich, Österreich, vertreten durch Advokatur Dr. Herbert Schöpf, LL.M., Rechtsanwalt-GmbH in Innsbruck, sowie die Nebenintervenientin auf Seiten der beklagten Partei EKFS Landwirtschaft AG & Co KG, Burgstallerstraße 10, 4892 Röth, Österreich, vertreten durch Hämmerle & Hübner Rechtsanwälte OG in Innsbruck, wegen 115.062,53 EUR sA, über die außerordentliche Revision der beklagten Partei (Revisionsinteresse 104.999,62 EUR sA) gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 11. Jänner 2021, GZ 3 R 76/20f-144, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Advokatur Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Schnake Robotik gmbh`(organisation)
- `Jeanne Großkopf`(person)
- `Volkmar Kapelner`(person)
- `Reinberg-Litschau 11, 9343 Aich, Österreich`(address)
- `EKFS Landwirtschaft AG`(organisation)
- `Co KG`(organisation)
- `Burgstallerstraße 10, 4892 Röth, Österreich`(address)

**Example 72** (doc_id: `deanon_TRAIN/9Ob28_23t`) (sent_id: `deanon_TRAIN/9Ob28_23t_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende, die Hofrätinnen und Hofräte des Obersten Gerichtshofs Mag. Ziegelbauer, Dr. Hargassner, Mag. Korn und Dr. Annerl in der Rechtssache der klagenden Partei Dr. Alessia Anwar, vertreten durch Held Berdnik Astner & Partner Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Dr.inM Li Mavromatidis, vertreten durch Mag. Markus Lechner, Rechtsanwalt in Lochau, wegen 247.483,60 EUR sA, über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 10. Mai 2023, GZ 4 R 28/23d-16, mit dem aus Anlass der Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 16. Dezember 2022, GZ 20 Cg 86/22i-10, und das vorangegangene Verfahren als nichtig aufgehoben und die Klage wegen Unzulässigkeit des Rechtswegs zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Beschluss des Obersten Gerichtshofs vom 26. Juli 2023 wird in seinem Spruch wie folgt berichtigt: Die Kostenentscheidung hat anstelle der Wortfolge „Die klagende Partei ist schuldig, der beklagten Partei ...“ richtig mit den Worten „DiebeklagtePartei ist schuldig, derklagendenPartei ...“ zu beginnen.

**False Positives:**

- `Held Berdnik Astner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Alessia Anwar`(person)
- `Li Mavromatidis`(person)

**Example 73** (doc_id: `deanon_TRAIN/9Ob49_19z`) (sent_id: `deanon_TRAIN/9Ob49_19z_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Dehn, Dr. Hargassner, Mag. Korn und Dr. Stefula in der Rechtssache der klagenden Partei Hartmut Dehn, vertreten durch Dr. Harald Schwendinger und Dr. Brigitte Piber, Rechtsanwälte in Salzburg, gegen die beklagte Partei Rosalinde Rover, vertreten durch Fahrner Unterrainer Rechtsanwälte OG in Zell am See, wegen Wiederaufnahme des Verfahrens AZ 17 C 29/13w des Bezirksgerichts Zell am See (wegen 11.658,48 EUR sA und Feststellung), über den Rekurs der klagenden Partei gegen den Beschluss des Landesgerichts Salzburg als Berufungsgericht vom 13. Juni 2019, GZ 53 R 71/19a-12, mit dem der Antrag auf Abänderung des Unzulässigkeitsausspruchs gemäß § 508 Abs 1 ZPO zurückgewiesen wurde, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Fahrner Unterrainer Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hartmut Dehn`(person)
- `Rosalinde Rover`(person)

**Example 74** (doc_id: `deanon_TRAIN/9Ob68_22y`) (sent_id: `deanon_TRAIN/9Ob68_22y_4`)


Sloboda und Dr. Annerl in der Rechtssache der klagenden Partei Angelika Blochinger, vertreten durch Neubauer Fähnrich Rechtsanwälte GmbH & Co KG in Graz, gegen die beklagte Partei Laurence Klüs Gesellschaft m.b.H. (FN FN026367d ), FN434768w, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung und 19.490 EUR sA (Gesamtstreitwert: 19.490 EUR), über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 10. September 2019, GZ 4 R 89/19v-59, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 27. März 2019, GZ 20 Cg 15/18t-54, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Revisionsverfahren wird fortgesetzt.

**False Positives:**

- `Pressl Endl Heinrich Bamberger Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Angelika Blochinger`(person)
- `Co KG`(organisation)
- `Laurence Klüs`(person)
- `FN026367d`(business_register_number)
- `FN434768w`(business_register_number)

**Example 75** (doc_id: `deanon_TRAIN/9Ob72_18f`) (sent_id: `deanon_TRAIN/9Ob72_18f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Dehn, Dr. Hargassner, Mag. Korn und Dr. Stefula in der Rechtssache der klagenden Partei Beilmaier&Herpolsheimer Daten GmbH, Dipl.-Ing. Ramon Neess, vertreten durch Knirsch Gschaider & Cerha Rechtsanwälte OG in Wien, sowie des Nebenintervenienten auf Seiten der klagenden Partei Dr. Hilde Gemperl, gegen die beklagte Partei Kirci & Issakov Sicherheit GesmbH, Stowassergasse 117, 2840 Hütten, Österreich, vertreten durch Partnerschaft Schuppich Sporn & Winischhofer, Rechtsanwälte in Wien, wegen 159.824,87 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Juli 2018, GZ 129 R 55/18h-40, mit dem der Berufung der klagenden Partei gegen das Urteil des Handelsgerichts Wien vom 6. April 2018, GZ 21 Cg 23/15s-36, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt und beschlossen:  Spruch

**False Positives:**

- `Knirsch Gschaider` — no gold match — likely missing annotation
- `Partnerschaft Schuppich Sporn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Beilmaier&Herpolsheimer Daten GmbH`(organisation)
- `Dipl.-Ing. Ramon Neess`(person)
- `Dr. Hilde Gemperl`(person)
- `Kirci & Issakov Sicherheit GesmbH`(organisation)
- `Stowassergasse 117, 2840 Hütten, Österreich`(address)

**Example 76** (doc_id: `deanon_TRAIN/9ObA109_13i`) (sent_id: `deanon_TRAIN/9ObA109_13i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras, die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner und Mag. Thomas Kallab als weitere Richter in der Arbeitsrechtssache der klagenden Partei Klaus Sowacki, gegen die beklagte Partei Mag. Gerlinde Klobucar, vertreten durch Hochleitner Rechtsanwälte GmbH in Linz, wegen 3.674,41 EUR brutto abzüglich 181,96 EUR netto sA (Revisionsinteresse 1.572,49 EUR brutto sA), über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 23. Mai 2013, GZ 8 Ra 36/13t-44, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Hochleitner Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Klaus Sowacki`(person)
- `Mag. Gerlinde Klobucar`(person)

**Example 77** (doc_id: `deanon_TRAIN/9ObA118_19x`) (sent_id: `deanon_TRAIN/9ObA118_19x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau und den Hofrat des Obersten Gerichtshofs Dr. Hargassner (Senat nach § 11a ASGG) in der Arbeitsrechtssache der klagenden Partei Thilo Weijer, gegen die beklagte Partei UWK Chemie GmbH, Emma Finzel, vertreten durch Dumfarth Klausberger Rechtsanwälte GmbH & CO KG in Linz, wegen Nichtigkeit und Wiederaufnahme des Verfahrens zu 9 ObA 41/19y, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das beim Obersten Gerichtshof anhängige Verfahren 9 ObA 118/19x wird bis zur Mitteilung des Pflegschaftsgerichts, ob für den Kläger ein (einstweiliger) Erwachsenenvertreter bestellt oder eine sonstige Maßnahme getroffen wird, unterbrochen.

**False Positives:**

- `Dumfarth Klausberger Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Thilo Weijer`(person)
- `UWK Chemie GmbH`(organisation)
- `Emma Finzel`(person)
- `CO KG`(organisation)

**Example 78** (doc_id: `deanon_TRAIN/9ObA120_22w`) (sent_id: `deanon_TRAIN/9ObA120_22w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Fichtenau als Vorsitzende, den Hofrat Dr. Hargassner und die Hofrätin Mag. Korn sowie die fachkundigen Laienrichter Dr. Martina Michor (aus dem Kreis der Arbeitgeber) und Dr. Andrea Eisler (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Larissa Prestianni, vertreten durch AHP Rechtsanwälte OG in Klagenfurt am Wörthersee, gegen die beklagte Partei RgR KzlR Lieselotte Mühlenbrock, vertreten durch Moser Mutz, Rechtsanwälte GesbR in Klagenfurt am Wörthersee, wegen Einwilligung in die Auflösung eines Dienstverhältnisses, in eventu Feststellung (Streitwert 94.891,52 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. September 2022, GZ 7 Ra 23/22i-24, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Moser Mutz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Larissa Prestianni`(person)
- `RgR KzlR Lieselotte Mühlenbrock`(person)

**Example 79** (doc_id: `deanon_TRAIN/9ObA129_19i`) (sent_id: `deanon_TRAIN/9ObA129_19i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden sowie die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau, den Hofrat des Obersten Gerichtshofs Dr. Stefula und die fachkundigen Laienrichter KR Mag. Paul Kunsky (aus dem Kreis der Arbeitgeber) und Harald Kohlruss (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Regina Drahtschmidt, LLB, vertreten durch Klein, Wuntschek & Partner Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Anselm Staeblein, vertreten durch Leitner Hirth Rechtsanwälte GmbH in Graz, wegen 3.461,72 EUR brutto sA (Revisionsinteresse 971,31 EUR brutto sA), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 12. September 2019, GZ 6 Ra 57/19b-13, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Leitner Hirth Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Regina Drahtschmidt, LLB`(person)
- `Anselm Staeblein`(person)

**Example 80** (doc_id: `deanon_TRAIN/9ObA33_20y`) (sent_id: `deanon_TRAIN/9ObA33_20y_4`)


Gabriele Svirak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Jürgen Fußgänger, vertreten durch Dr. Herbert Holzinger, Rechtsanwalt in Wien, gegen die beklagte Partei UnterImmobilien GmbH, Ing. Virgil Feketics, vertreten durch Salzborn Rechtsanwaltsgesellschaft mbH in Wien, wegen 1.152,44 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 27. Februar 2020, GZ 7 Ra 7/20f-23, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Salzborn Rechtsanwaltsgesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jürgen Fußgänger`(person)
- `UnterImmobilien GmbH`(organisation)
- `Ing. Virgil Feketics`(person)

**Example 81** (doc_id: `deanon_TRAIN/9ObA41_14s`) (sent_id: `deanon_TRAIN/9ObA41_14s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras, die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Mag. Gerald Fuchs und Peter Schönhofer als weitere Richter in der Arbeitsrechtssache der klagenden Partei Gwendolin Schmeerbauch, vertreten durch Dr. Remo Sacherer, Rechtsanwalt in Wien, gegen die beklagte Partei Uniglanz Bildung Solutions AG, PhD Martina Gesänger, vertreten durch Korn Rechtsanwälte OG in Wien, wegen Kündigungsanfechtung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Februar 2014, GZ 7 Ra 4/14f-29, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Korn Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Gwendolin Schmeerbauch`(person)
- `Uniglanz Bildung Solutions AG`(organisation)
- `PhD Martina Gesänger`(person)

**Example 82** (doc_id: `deanon_TRAIN/9ObA41_16v`) (sent_id: `deanon_TRAIN/9ObA41_16v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätinnen des Obersten Gerichtshofs Hon.-Prof. Dr. Dehn und Mag. Korn sowie die fachkundigen Laienrichter Dr. Johannes Pflug und Mag. Robert Brunner als weitere Richter in der Arbeitsrechtssache der klagenden Partei Mag. Joseph Mehl, vertreten durch Dr. Stephan Rainer und Dr. Andreas Ruetz, Rechtsanwälte in Innsbruck, gegen die beklagte Partei Heiko Ayna, vertreten durch Korn Rechtsanwälte OG in Wien, wegen 40.647,29 EUR brutto sA über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. Jänner 2016, GZ 15 Ra 16/16i-31, mit dem der Berufung der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 11. November 2015, GZ 43 Cga 118/14b-26, nicht Folge gegeben wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Korn Rechtsanw` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Joseph Mehl`(person)
- `Heiko Ayna`(person)

**Example 83** (doc_id: `deanon_TRAIN/9ObA4_13y`) (sent_id: `deanon_TRAIN/9ObA4_13y_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, den Hofrat des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und die Hofrätin des Obersten Gerichtshofs Dr. Dehn sowie die fachkundigen Laienrichter Werner Rodlauer und Mag. Robert Brunner als weitere Richter in der Arbeitsrechtssache der klagenden Partei Maria Maritz, vertreten durch Dr. Susanne Kuen, Rechtsanwältin in Wien, gegen die beklagte Partei PHG Möbel Dienstleistungen GmbH, Zeno Speckl, vertreten durch Fellner Wratzfeld & Partner Rechtsanwälte GmbH in Wien, wegen 125.731,44 EUR sA, über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 30. Oktober 2012, GZ 11 Ra 82/12a-74, mit dem das Urteil des Landesgerichts Steyr als Arbeits- und Sozialgericht vom 31. Juli 2012, GZ 9 Cga 245/08g-70, aufgehoben und die Rechtssache an das Erstgericht zurückverwiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Fellner Wratzfeld` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maria Maritz`(person)
- `PHG Möbel Dienstleistungen GmbH`(organisation)
- `Zeno Speckl`(person)

**Example 84** (doc_id: `deanon_TRAIN/9ObA8_20x`) (sent_id: `deanon_TRAIN/9ObA8_20x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau und den Hofrat des Obersten Gerichtshofs Dr. Hargassner sowie die fachkundigen Laienrichter Dr. Ingomar Stupar (aus dem Kreis der Arbeitgeber) und Mag. Werner Pletzenauer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Mag. Dr. Cornelius Jannes, vertreten durch Moser Mutz Rechtsanwälte GesbR in Klagenfurt am Wörthersee, gegen die beklagte Partei Stubertz & Fortschnieder Daten AG, VetR Zeno Dornedden, vertreten durch Wiedenbauer Mutz Winkler & Partner Rechtsanwälte GmbH in Klagenfurt am Wörthersee, wegen Kündigungsanfechtung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 18. Dezember 2019, GZ 7 Ra 70/19x-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision der klagenden Partei wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Moser Mutz Rechtsanw` — no gold match — likely missing annotation
- `Wiedenbauer Mutz Winkler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Dr. Cornelius Jannes`(person)
- `Stubertz & Fortschnieder Daten AG`(organisation)
- `VetR Zeno Dornedden`(person)

</details>

---

## `Standalone Person Name in Legal Context`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `78d78435`  
**Description:**
Captures standalone capitalized names in legal contexts where no title or specific role precedes them.

**Content:**
```
(?:eingetragenen|für\s+seine\s+Kinder|für\s+das\s+Kind|der\s+Beschwerdeführerin|der\s+Beschwerdeführer|der\s+Beschuldigte|der\s+Abgabepflichtige|der\s+Bf\.)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 328 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/6Ob240_20t`) (sent_id: `deanon_TRAIN/6Ob240_20t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schramm als Vorsitzenden sowie durch die Hofräte Hon.-Prof. Dr. Gitschthaler, Univ.-Prof. Dr. Kodek, Dr. Nowotny und die Hofrätin Dr. Faber als weitere Richter in der Firmenbuchsache der zu FN FN912691n beim Landesgericht Landesgericht Klagenfurt eingetragenen Holtschmidt Versicherung GmbH mit Sitz in der politischen Gemeinde LG Wels, über den Revisionsrekurs der Lohneis Pflege gesellschaft mbH, Auf der Werzer Leitn 27, 9560 Klausen, Österreich, vertreten durch Dr. Robert Mogy, Rechtsanwalt in Klagenfurt, gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. Oktober 2020, GZ 4 R 153/20g-8, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen (§ 71 Abs 3 AußStrG iVm § 15 Abs 2 FBG).

**False Positives:**

- `Holtschmidt Versicherung Gmb` — partial — pred is substring of gold: `Holtschmidt Versicherung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FN912691n`(business_register_number)
- `Landesgericht Klagenfurt`(organisation)
- `Holtschmidt Versicherung GmbH`(organisation)
- `LG Wels`(organisation)
- `Lohneis Pflege gesellschaft mbH`(organisation)
- `Auf der Werzer Leitn 27, 9560 Klausen, Österreich`(address)

</details>

---

## `Person after 'Herrn' or 'Frau'`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `79232d4e`  
**Description:**
Captures names preceded by 'Herrn' or 'Frau' in legal texts.

**Content:**
```
(?:Herrn|Frau)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Person after 'Gattin' or 'Kinder'`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `23bbc7f9`  
**Description:**
Captures names of spouses or children mentioned in legal contexts.

**Content:**
```
(?:und\s+dessen\s+Gattin|und\s+deren\s+Gattin|für\s+seine\s+Kinder|für\s+das\s+Kind|für\s+ihre\s+Tochter|für\s+seinen\s+Sohn)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
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

