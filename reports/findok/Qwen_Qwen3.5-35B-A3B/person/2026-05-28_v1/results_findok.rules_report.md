# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-05-28T12:24:45.458862

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-05-28_v1/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 2473 |
| Validation documents | 619 |
| Test documents | 476 |
| Train sentences | 3896 |
| Validation sentences | 1147 |
| Test sentences | 21234 |
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
| Batch size | 100 |
| Refine per batch | 1 |
| Manually annotated examples | 0 |
| First batch with manual data | None |

</details>

---

**Transfer Learning**

| Property | Value |
|---|---|
| Best Batch Idx | 1 |
| Best Batch F1 | 0.050867210529923906 |
| Best Rules Serialized | [{'id': '219eb9e0', 'name': 'Judge_Richter', 'description': 'Captures the name of a judge (Richter/Richterin/Vorsitzende) including complex titles and suffixes.', 'format': 'regex', 'content': '(?:durch\\s+(?:den\\s+)?(?:Richter|Richterin|Vorsitzende)\\s+)([A-Z][a-zA-Z\\.\\s,]+?(?:\\s+(?:LL\\.M\\.|M\\.B\\.L\\.|B\\.Ed\\.|B\\.Sc\\.|MA|Bakk\\.|Dipl\\.-|Dipl\\.\\s+Kfm\\.|Ing\\.|MedR|VetR|Techn|ÖkR|OStR|Univ\\.-|Priv\\.-|Hon\\.-|Dr\\.in|Mag\\.in|Mag\\.a|PhD|LLB|Dr\\.\\s+Univ\\.-Prof\\.in?|Univ\\.-Prof\\.in?|Priv\\.-Doz\\.in?|Hon\\.-Prof\\.in?)?)?)(?:\\s+(?:in der|über die|in der Verwaltungsstrafsache))', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '9c38bec4', 'name': 'Party_Beschwerdesache', 'description': "Captures the name of a party in a complaint case (Beschwerdesache/Rechtssache), handling 'der' prefix and complex suffixes.", 'format': 'regex', 'content': '(?:in der\\s+(?:Beschwerdesache|Rechtssache|Verwaltungsstrafsache)\\s+(?:der\\s+)?)([A-Z][a-zA-Z\\.\\s,]+?(?:\\s+(?:LL\\.M\\.|M\\.B\\.L\\.|B\\.Ed\\.|B\\.Sc\\.|MA|Bakk\\.|Dipl\\.-|Dipl\\.\\s+Kfm\\.|Ing\\.|MedR|VetR|Techn|ÖkR|OStR|Univ\\.-|Priv\\.-|Hon\\.-|Dr\\.in|Mag\\.in|Mag\\.a|PhD|LLB)?)?)(?:,\\s+[A-Z]|\\s+vertreten|\\s+\\(|\\s+\\))', 'priority': 9, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '03afec1a', 'name': 'Representative_vertreten_durch', 'description': "Captures the name of a representative (lawyer/tax advisor) introduced by 'vertreten durch'.", 'format': 'regex', 'content': '(?:vertreten\\s+durch\\s+)([A-Z][a-zA-Z\\.\\s,]+?(?:\\s+(?:LL\\.M\\.|M\\.B\\.L\\.|B\\.Ed\\.|B\\.Sc\\.|MA|Bakk\\.|Dipl\\.-|Dipl\\.\\s+Kfm\\.|Ing\\.|MedR|VetR|Techn|ÖkR|OStR|Univ\\.-|Priv\\.-|Hon\\.-|Dr\\.in|Mag\\.in|Mag\\.a|PhD|LLB)?)?)(?:,\\s+[A-Z]|\\s+GmbH|\\s+Steuerberatung)', 'priority': 8, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '214b5905', 'name': 'Herr_Name', 'description': "Captures full names following 'Herr' or 'Herrn'.", 'format': 'regex', 'content': '(?:Herrn?\\s+)([A-Z][a-zA-Z]+(?:\\s+[A-Z][a-zA-Z]+)+)', 'priority': 7, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'ae51c48f', 'name': 'Frau_Name', 'description': "Captures full names following 'Frau'.", 'format': 'regex', 'content': '(?:Frau\\s+)([A-Z][a-zA-Z]+(?:\\s+[A-Z][a-zA-Z]+)+)', 'priority': 7, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '9a5bee62', 'name': 'Title_Name_Context', 'description': 'Captures names with titles (Dr., Mag., Ing., etc.) in general contexts, ensuring at least a first and last name.', 'format': 'regex', 'content': '(?:^|\\s)([A-Z][a-zA-Z]+(?:\\s+[A-Z][a-zA-Z]+)+)(?:\\s+(?:Dr\\.in?|Mag\\.in?|Ing\\.in?|Prof\\.in?|Univ\\.-Prof\\.in?|Priv\\.-Doz\\.in?|Hon\\.-Prof\\.in?|MedR|VetR|Techn|Ri|Ri2|Ri3|R\\.in?|[A-Z]\\.)?)?(?:\\s|$|,|\\.|\\))', 'priority': 5, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}] |

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 61.7% |
| True Positives | 371 |
| False Positives | 12831 |
| False Negatives | 1014 |
| Total Gold Entities | 1385 |
| Micro Precision | 2.8% |
| Micro Recall | 26.8% |
| Micro F1 | 5.1% |
| Macro F1 | 5.1% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Title_Name_Context` | 5.0% | 2.8% | 26.4% | 13210 | 365 | 12845 |
| `Representative_vertreten_durch` | 0.7% | 1.6% | 0.4% | 379 | 6 | 373 |
| `Judge_Richter` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Party_Beschwerdesache` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Herr_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Frau_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `Title_Name_Context`

**F1:** 0.050 | **Precision:** 0.028 | **Recall:** 0.264  

**Format:** `regex`  
**Rule ID:** `9a5bee62`  
**Description:**
Captures names with titles (Dr., Mag., Ing., etc.) in general contexts, ensuring at least a first and last name.

**Content:**
```
(?:^|\s)([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)+)(?:\s+(?:Dr\.in?|Mag\.in?|Ing\.in?|Prof\.in?|Univ\.-Prof\.in?|Priv\.-Doz\.in?|Hon\.-Prof\.in?|MedR|VetR|Techn|Ri|Ri2|Ri3|R\.in?|[A-Z]\.)?)?(?:\s|$|,|\.|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.028 | 0.264 | 0.050 | 13210 | 365 | 12845 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 365 | 12845 | 1020 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Schramm als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Ivan Dimitroff, geboren am 19. Mai 1960, AZ 7 P 203/15g des Bezirksgerichts Mödling, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Mödling zurückgestellt.

| Predicted | Gold |
|---|---|
| `Ivan Dimitroff` | `Ivan Dimitroff` |

**Missed by this rule (FN):**

- `19. Mai 1960` (date)
- `Bezirksgerichts Mödling` (organisation)
- `Bezirksgericht Mödling` (organisation)

**Example 1** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und die Hofräte Dr. Fellinger und Dr. Schramm als weitere Richter in der Pflegschaftssache der Minderjährigen Delia Truepschuch, geboren am 1. Februar 2026, und Aloisa Eckmaier, geboren am 28. Februar 1976, AZ 2 PS 117/09t des Bezirksgerichts Feldkirchen, infolge Vorlage zur Genehmigung der Übertragung gemäß § 111 JN an das Bezirksgericht Neunkirchen, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Übertragung der Zuständigkeit zur Besorgung dieser Pflegschaftssache an das Bezirksgericht Neunkirchen wird genehmigt.

| Predicted | Gold |
|---|---|
| `Delia Truepschuch` | `Delia Truepschuch` |
| `Aloisa Eckmaier` | `Aloisa Eckmaier` |

**Missed by this rule (FN):**

- `1. Februar 2026` (date)
- `28. Februar 1976` (date)
- `Bezirksgericht Neunkirchen` (organisation)
- `Bezirksgericht Neunkirchen` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_0`)


Gericht OGH

**False Positives:**

- `Gericht OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Karin Meiwaldt, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Katharina Tomandl, MA, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Kopf Der Oberste Gerichtshof` — no gold match — likely missing annotation
- `Partei Karin Meiwaldt` — partial — gold is substring of pred: `Karin Meiwaldt`
- `Partei Katharina Tomandl` — positional overlap with gold: `Katharina Tomandl, MA`
- `Ernst Michael Lang` — partial — pred is substring of gold: `Mag. Ernst Michael Lang`
- `Spruch Der Ordinationsantrag` — no gold match — likely missing annotation

> overlaps gold: 3  |  likely missing annotation: 2

**Gold Entities:**

- `Karin Meiwaldt`(person)
- `Katharina Tomandl, MA`(person)
- `Mag. Ernst Michael Lang`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_4`)


Text Begründung: Die Klägerin begehrt mit der am 4. 8. 2017 beim Bezirksgericht Steyr eingebrachten Klage von dem in der Schweiz ansässigen Beklagten 4.660 EUR sA.

**False Positives:**

- `Bezirksgericht Steyr` — type mismatch — same span as gold: `Bezirksgericht Steyr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Steyr`(organisation)

**Example 3** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_6`)


Die Aktiengesellschaft habe damit geworben, mit den eingezahlten Beträgen Edelmetalle zu marktüblichen Preisen zu erwerben, zu lagern und zu verwalten und habe dem Beklagten in dessen Funktion als Rechtsanwalt und öffentlicher Notar den Auftrag erteilt, jährliche Prüfberichte über den vollständigen Bestand zu erstellen.

**False Positives:**

- `Die Aktiengesellschaft` — type mismatch — same span as gold: `Die Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Die Aktiengesellschaft`(organisation)

**Example 4** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_7`)


Der Beklagte habe seine Aufsichts- und Prüfpflichten jedoch verletzt, rechtswidrig gehandelt und arglistig einen wesentlichen Irrtum verursacht.

**False Positives:**

- `Der Beklagte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_9`)


Der Beklagte erhob die Einrede der internationalen Unzuständigkeit, hilfsweise die Einrede der internationalen Streitanhängigkeit sowie die Einrede der örtlichen Unzuständigkeit des angerufenen Gerichts.

**False Positives:**

- `Der Beklagte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_10`)


Mit Beschluss vom 8. 10.

**False Positives:**

- `Mit Beschluss` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_11`)


2018 erklärte sich dasBezirksgericht Steyrfür örtlich unzuständig und überwies (antragsgemäß) die Rechtssache an das nicht offenbar unzuständige Bezirksgericht Salzburg.

**False Positives:**

- `Bezirksgericht Salzburg` — type mismatch — same span as gold: `Bezirksgericht Salzburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Salzburg`(organisation)

**Example 8** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_12`)


DasBezirksgericht Salzburgwies mit Beschluss vom 12. 11. 2018 die Klage wegen internationaler und örtlicher Unzuständigkeit zurück (ON 31).

**False Positives:**

- `DasBezirksgericht Salzburgwies` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_13`)


In ihrem gegen diesen Beschluss erhobenenRekursbeantragte die Klägerin hilfsweise (für den Fall, dass ihrem Rekurs nicht stattgegeben werden sollte) die Ordination gemäß § 28 JN an ein vom Obersten Gerichtshof zu benennendes Bezirksgericht (ON 34).

**False Positives:**

- `Obersten Gerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_14`)


DasLandesgericht Salzburgals Rekursgericht gab dem Rekurs nicht Folge und erachtete den Revisionsrekurs im Hinblick auf § 528 Abs 2 Z 1 ZPO (Entscheidungsgegenstand 5.000 EUR nicht übersteigend) als jedenfalls unzulässig (ON 38).

**False Positives:**

- `DasLandesgericht Salzburgals Rekursgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_15`)


Dieser Beschluss ist rechtskräftig.

**False Positives:**

- `Dieser Beschluss` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_16`)


Rechtliche Beurteilung Der Ordinationsantrag ist nicht berechtigt.

**False Positives:**

- `Rechtliche Beurteilung Der Ordinationsantrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_17`)


1. Die Ordination nach § 28 Abs 1 Z 1 JN setzt die internationale Zuständigkeit Österreichs voraus (RIS-Justiz RS0118239;

**False Positives:**

- `Die Ordination` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_18`)


RS0053178 [T10];GarberinFasching/Konecny3§ 28 JN Rz 22).

**False Positives:**

- `JN Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_19`)


Ist über die internationale Zuständigkeit bereits eine rechtskräftige Entscheidung ergangen, ist der Oberste Gerichtshof an diese Entscheidung gebunden (Garberin Fasching/Konecny3§ 28 JN Rz 25;

**False Positives:**

- `Oberste Gerichtshof` — no gold match — likely missing annotation
- `JN Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 16** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_22`)


Da das Bezirksgericht Salzburg die internationale Zuständigkeit Österreichs zur Erledigung der Klage rechtskräftig verneint hat, kann eine Ordination nicht mehr erfolgreich auf § 28 Abs 1 Z 1 JN gestützt werden.

**False Positives:**

- `Bezirksgericht Salzburg` — type mismatch — same span as gold: `Bezirksgericht Salzburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Salzburg`(organisation)

**Example 17** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_23`)


2.1 Als Grundlage für eine Ordination kommt daher nur der Fall des § 28 Abs 1 Z 2 JN in Betracht, wonach die Bestimmung eines örtlich zuständigen Gerichts durch den Obersten Gerichtshof dann zulässig ist, wenn der Antragsteller seinen Wohnsitz im Inland hat und im Einzelfall die Rechtsverfolgung im Ausland nicht möglich oder unzumutbar wäre (RIS-Justiz RS0112108).

**False Positives:**

- `Als Grundlage` — no gold match — likely missing annotation
- `Obersten Gerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 18** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_26`)


3. Der Ordinationsantrag war daher abzuweisen (ebenso 3 Nc 3/19z, 6 Nc 25/18f, 9 Nc 24/18f, 9 Nc 2/19x, 9 Nc 6/19k und 2 Nc 8/19b).

**False Positives:**

- `Der Ordinationsantrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_27`)


European Case Law Identifier ECLI:AT:OGH0002:2019:0100NC00011.19B.0321.000

**False Positives:**

- `European Case Law Identifier` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_0`)


Gericht OGH

**False Positives:**

- `Gericht OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Schramm als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Ivan Dimitroff, geboren am 19. Mai 1960, AZ 7 P 203/15g des Bezirksgerichts Mödling, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Mödling zurückgestellt.

**False Positives:**

- `Kopf Der Oberste Gerichtshof` — no gold match — likely missing annotation
- `Hofrat Dr` — no gold match — likely missing annotation
- `Hofrat Univ` — no gold match — likely missing annotation
- `Spruch Der Akt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 4

**Gold Entities:**

- `Ivan Dimitroff`(person)
- `19. Mai 1960`(date)
- `Bezirksgerichts Mödling`(organisation)
- `Bezirksgericht Mödling`(organisation)

**Example 22** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_4`)


Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

**False Positives:**

- `Mit Beschluss` — no gold match — likely missing annotation
- `Bezirksgericht Judenburg` — type mismatch — same span as gold: `Bezirksgericht Judenburg`
- `Bezirksgerichts Judenburg` — type mismatch — same span as gold: `Bezirksgerichts Judenburg`

> overlaps gold: 2  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Mödling`(organisation)
- `Bezirksgericht Judenburg`(organisation)
- `Bezirksgerichts Judenburg`(organisation)

**Example 23** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_5`)


Das Bezirksgericht Mödling legte den Akt zur Entscheidung gemäß § 111 Abs 2 JN dem Obersten Gerichtshof vor (ON 8), ohne den Übertragungsbeschluss an die Parteien zuzustellen.

**False Positives:**

- `Das Bezirksgericht` — positional overlap with gold: `Bezirksgericht Mödling`
- `Obersten Gerichtshof` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Mödling`(organisation)

**Example 24** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_6`)


Rechtliche Beurteilung Die Vorlage ist verfrüht.

**False Positives:**

- `Rechtliche Beurteilung Die Vorlage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_9`)


Andernfalls könnte eine Verschiebung der funktionellen Zuständigkeit eintreten, weil mangels Bestätigung des Übertragungsbeschlusses durch das Rekursgericht gar keine Grundlage für die Genehmigung einer Zuständigkeitsübertragung durch den Obersten Gerichtshof bestünde (9 Nc 15/14a;

**False Positives:**

- `Obersten Gerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_12`)


Der Akt ist daher dem übertragenden Gericht zurückzustellen, das den Übertragungsbeschluss den Verfahrensbeteiligten zuzustellen haben wird.

**False Positives:**

- `Der Akt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_14`)


European Case Law Identifier ECLI:AT:OGH0002:2016:0100NC00018.16B.1004.000

**False Positives:**

- `European Case Law Identifier` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_0`)


Gericht OGH

**False Positives:**

- `Gericht OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Chen Mestwerdt, Slowenien, vertreten durch Mag. Erich Hierz, Rechtsanwalt in Graz, gegen die beklagte Partei Roman Eschenweck, Deutschland, vertreten durch Salleck + Partner Rechtsanwälte in Deutschland, wegen 5.856 EUR sA, 1.342 EUR sA und 915 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag, die Rechtssache gemäß § 28 JN einem österreichischem Gericht zuzuweisen, wird zurückgewiesen.

**False Positives:**

- `Kopf Der Oberste Gerichtshof` — no gold match — likely missing annotation
- `Partei Chen Mestwerdt` — partial — gold is substring of pred: `Chen Mestwerdt`
- `Erich Hierz` — partial — pred is substring of gold: `Mag. Erich Hierz`
- `Partei Roman Eschenweck` — partial — gold is substring of pred: `Roman Eschenweck`
- `Spruch Der Antrag` — no gold match — likely missing annotation

> overlaps gold: 3  |  likely missing annotation: 2

**Gold Entities:**

- `Chen Mestwerdt`(person)
- `Mag. Erich Hierz`(person)
- `Roman Eschenweck`(person)

</details>

---

## `Representative_vertreten_durch`

**F1:** 0.007 | **Precision:** 0.016 | **Recall:** 0.004  

**Format:** `regex`  
**Rule ID:** `03afec1a`  
**Description:**
Captures the name of a representative (lawyer/tax advisor) introduced by 'vertreten durch'.

**Content:**
```
(?:vertreten\s+durch\s+)([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|ÖkR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB)?)?)(?:,\s+[A-Z]|\s+GmbH|\s+Steuerberatung)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.016 | 0.004 | 0.007 | 379 | 6 | 373 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 6 | 373 | 1379 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Karin Meiwaldt, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Katharina Tomandl, MA, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Ernst Michael Lang` | `Mag. Ernst Michael Lang` |

**Missed by this rule (FN):**

- `Karin Meiwaldt` (person)
- `Katharina Tomandl, MA` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Chen Mestwerdt, Slowenien, vertreten durch Mag. Erich Hierz, Rechtsanwalt in Graz, gegen die beklagte Partei Roman Eschenweck, Deutschland, vertreten durch Salleck + Partner Rechtsanwälte in Deutschland, wegen 5.856 EUR sA, 1.342 EUR sA und 915 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag, die Rechtssache gemäß § 28 JN einem österreichischem Gericht zuzuweisen, wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Erich Hierz` | `Mag. Erich Hierz` |

**Missed by this rule (FN):**

- `Chen Mestwerdt` (person)
- `Roman Eschenweck` (person)

**Example 2** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Sten und Stöwer Wind GmbH, OMedR Torsten Münchmeyer, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei OStR Gregor Ruemmel, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Alexander Rimser` | `Mag. Alexander Rimser` |

**Missed by this rule (FN):**

- `Sten und Stöwer Wind GmbH` (organisation)
- `OMedR Torsten Münchmeyer` (person)
- `OStR Gregor Ruemmel` (person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob10_16t`) (sent_id: `deanon_TRAIN/10Ob10_16t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei DI Fabian Reifrath, vertreten durch Dr. Wilhelm Schlein Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Elina Woyte, vertreten durch Dr. Werner Goeritz, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 2. Dezember 2015, GZ 40 R 205/15s-34, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Werner Goeritz` | `Dr. Werner Goeritz` |

**Missed by this rule (FN):**

- `DI Fabian Reifrath` (person)
- `Wilhelm Schlein Rechtsanwalt GmbH` (organisation)
- `Elina Woyte` (person)

**Example 4** (doc_id: `deanon_TRAIN/3Ob152_10i`) (sent_id: `deanon_TRAIN/3Ob152_10i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Exekutionssache der betreibenden Partei KMN Versicherung Werke AG, Corbinian Pichlmaier, vertreten durch Dr. Erich Kafka, Dr. Manfred Palkovits, Rechtsanwälte in Wien, gegen die verpflichtete Partei Severin Wellenbrink, vertreten durch Dr. Philipp Jessich, Rechtsanwalt in Wien, wegen Aufschiebung einer Räumungsexekution, über den Revisionsrekurs der betreibenden Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 12. Mai 2010, GZ 39 R 44/10z-22, womit der Beschluss des Bezirksgerichts Fünfhaus vom 14. Jänner 2010, GZ 10 E 171/09d-6, abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Erich Kafka` | `Dr. Erich Kafka` |

**Missed by this rule (FN):**

- `KMN Versicherung Werke AG` (organisation)
- `Corbinian Pichlmaier` (person)
- `Dr. Manfred Palkovits` (person)
- `Severin Wellenbrink` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Karin Meiwaldt, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Katharina Tomandl, MA, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Neumayer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Karin Meiwaldt`(person)
- `Katharina Tomandl, MA`(person)
- `Mag. Ernst Michael Lang`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei C. Dersudheim Digital GmbH, Taxlbergstraße 247, 8151 Rohrbach, Österreich, vertreten durch Dr. Carl Benkhofer, Rechtsanwalt in Wien, gegen die beklagte Partei Ingolf Grimpe, vertreten durch Greiml & Horwath Rechtsanwaltspartnerschaft in Graz, wegen 5.232 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 14 C 1302/11a des Bezirksgerichts Graz-West in nichtöffentlicher Sitzung, den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Graz-West das Bezirksgericht Fünfhaus bestimmt.

**False Positives:**

- `Dr. Carl Benkhofer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dersudheim Digital GmbH`(organisation)
- `Taxlbergstraße 247, 8151 Rohrbach, Österreich`(address)
- `Ingolf Grimpe`(person)
- `Bezirksgericht Fünfhaus`(organisation)

**Example 2** (doc_id: `deanon_TRAIN/10Nc7_10a`) (sent_id: `deanon_TRAIN/10Nc7_10a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger und Hon.-Prof. Dr. Neumayr als weitere Richter in der Verlassenschaftssache nach dem am 9. September 2009 verstorbenen, zuletzt in Tschiggfreystraße 46, 3240 Loitsdorf, Österreich, wohnhaft gewesenen Manfred Johann Pingert, AZ 1 A 349/09w des Bezirksgerichts Kitzbühel, über den Delegierungsantrag der Karin Czychy, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, den B e s c h l u s s gefasst:  Spruch Dem Delegierungsantrag wird stattgegeben.

**False Positives:**

- `Mag. Maximilian Kocher` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Tschiggfreystraße 46, 3240 Loitsdorf, Österreich`(address)
- `Pingert`(person)
- `Czychy`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Nc9_15b`) (sent_id: `deanon_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Mur Kraftalheim Holding GmbH, Gerald Zacharie, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Nexstein Textil GmbH, Dipl.-Ing. Lynn Forkarth, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

**False Positives:**

- `Dr. Roland Kassowitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgericht Linz`(organisation)
- `Mur Kraftalheim Holding GmbH`(organisation)
- `Gerald Zacharie`(person)
- `Nexstein Textil GmbH`(organisation)
- `Dipl.-Ing. Lynn Forkarth`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob102_18z`) (sent_id: `deanon_TRAIN/10Ob102_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG, Adelheid Lochmaier, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Ursula Antoniadis, vertreten durch Knirsch – Braun – Fellner Rechtsanwälte in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 5. September 2018, GZ 40 R 39/18h-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mag. Franz Podovsovnik` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Skrzypczik + Duchscherer Digital AG`(organisation)
- `Adelheid Lochmaier`(person)
- `Ursula Antoniadis`(person)

**Example 5** (doc_id: `deanon_TRAIN/10Ob105_15m`) (sent_id: `deanon_TRAIN/10Ob105_15m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Alsteinost GmbH, Anna Kisaoglu, Bakk. iur., vertreten durch Dr. Erich Kafka und Dr. Manfred Palkovits, Rechtsanwälte in Wien, gegen die beklagte Partei Ing. Mag. Adam Kratki, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 11. Juni 2015, GZ 39 R 41/15s-29, in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch

**False Positives:**

- `Dr. Erich Kafka und Dr. Manfred Palkovits` — partial — gold is substring of pred: `Dr. Erich Kafka`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alsteinost GmbH`(organisation)
- `Anna Kisaoglu, Bakk. iur.`(person)
- `Dr. Erich Kafka`(person)
- `Dr. Manfred Palkovits`(person)
- `Mag. Adam Kratki`(person)

**Example 6** (doc_id: `deanon_TRAIN/10Ob10_16t`) (sent_id: `deanon_TRAIN/10Ob10_16t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei DI Fabian Reifrath, vertreten durch Dr. Wilhelm Schlein Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Elina Woyte, vertreten durch Dr. Werner Goeritz, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 2. Dezember 2015, GZ 40 R 205/15s-34, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Wilhelm Schlein Rechtsanwalt` — positional overlap with gold: `Wilhelm Schlein Rechtsanwalt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DI Fabian Reifrath`(person)
- `Wilhelm Schlein Rechtsanwalt GmbH`(organisation)
- `Elina Woyte`(person)
- `Dr. Werner Goeritz`(person)

**Example 7** (doc_id: `deanon_TRAIN/10Ob10_18w`) (sent_id: `deanon_TRAIN/10Ob10_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Jonasgasse 71, 4760 Weeg, Österreich, vertreten durch Dr. Alois Schneider, Rechtsanwalt in Rattenberg, wider die beklagte Partei Corinna Elfe, vertreten durch Dr. Walter Hausberger, Dr. Katharina Moritz und Dr. Alfred Schmidt, Rechtsanwälte in Wörgl, wegen Entfernung und Unterlassung (Revisionsinteresse 10.000 EUR), infolge Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 3. November 2017, GZ 3 R 172/17s-22, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Rattenberg vom 17. Mai 2017, GZ 3 C 401/15k-18, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Alois Schneider` — no gold match — likely missing annotation
- `Dr. Walter Hausberger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Jonasgasse 71, 4760 Weeg, Österreich`(address)
- `Corinna Elfe`(person)

**Example 8** (doc_id: `deanon_TRAIN/10Ob11_15p`) (sent_id: `deanon_TRAIN/10Ob11_15p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte und Hofrätinnen Univ.-Prof. Dr. Neumayr, Dr. Schramm, Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Viktoria Hornburg, vertreten durch Dr. Walter Vasoll und Mag. Marion Vasoll, Rechtsanwälte in Hermagor, gegen die beklagte Partei Mercedes Jungschlaeger, vertreten durch Dr. Thomas Romauch, Rechtsanwalt in Wien, wegen Feststellung und Einwilligung (6.000 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 4. Dezember 2014, GZ 3 R 169/14h-14, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Hermagor vom 9. August 2014, GZ 1 C 563/13b-10, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision der beklagten Partei wird zurückgewiesen.

**False Positives:**

- `Dr. Walter Vasoll und Mag. Marion Vasoll` — no gold match — likely missing annotation
- `Dr. Thomas Romauch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Viktoria Hornburg`(person)
- `Mercedes Jungschlaeger`(person)

**Example 9** (doc_id: `deanon_TRAIN/10Ob12_24y`) (sent_id: `deanon_TRAIN/10Ob12_24y_5`)


Isidor Janofske, beide vertreten durch Ghendler Ruvinskij Rechtsanwaltsgesellschaft mbH in Wien, gegen die beklagte Partei Wolfram Fritzsche S.p.A., VetR Lukas Dickhaus, vertreten durch bpv Hügel Rechtsanwälte GmbH in Wien, wegen 71.425,56 EUR sA, aus Anlass der Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 20. Dezember 2023, GZ 6 R 68/23a-41, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 21. August 2023, GZ 19 Cg 10/22f-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die gemeinsame Anzeige der Parteien über das vereinbarte „ewige“ Ruhen des Verfahrens wird zur Kenntnis genommen.

**False Positives:**

- `Ghendler Ruvinskij Rechtsanwaltsgesellschaft mbH in Wien, gegen die beklagte Partei Wolfram Fritzsche S.p.A.` — partial — gold is substring of pred: `Wolfram Fritzsche`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Isidor Janofske`(person)
- `Wolfram Fritzsche`(person)
- `VetR Lukas Dickhaus`(person)

**Example 10** (doc_id: `deanon_TRAIN/10Ob13_15g`) (sent_id: `deanon_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Zoltan Alfermann, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei DonauFurtostBildung GmbH, KzlR Noah Christansen, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Lederer Rechtsanwalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zoltan Alfermann`(person)
- `DonauFurtostBildung GmbH`(organisation)
- `KzlR Noah Christansen`(person)

**Example 11** (doc_id: `deanon_TRAIN/10Ob13_20i`) (sent_id: `deanon_TRAIN/10Ob13_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Miranda Klagemann, vertreten durch Dr. Andreas Ladstätter, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. DI Adolf Kowallek, und 2. Ing. Janis Grottian, beide vertreten durch Dr. Walter Schuhmeister und Mag. Franz Haydn, Rechtsanwälte in Schwechat, wegen 15.000 EUR sA, infolge Revision der beklagten Parteien (Revisionsinteresse 6.250 EUR) gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 30. Jänner 2019, GZ 34 R 66/18k-27, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Innere Stadt Wien vom 23. März 2018, GZ 37 C 780/16f-18, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Walter Schuhmeister und Mag. Franz Haydn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Miranda Klagemann`(person)
- `DI Adolf Kowallek`(person)
- `Ing. Janis Grottian`(person)

**Example 12** (doc_id: `deanon_TRAIN/10Ob16_14x`) (sent_id: `deanon_TRAIN/10Ob16_14x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Walter Gritzmacher, vertreten durch Dr. Birgit Lajtai-Nagl, Rechtsanwältin in Villach, gegen die beklagte Partei Dr. Ariadne Graspointner, vertreten durch Dr. Robert Kugler, Rechtsanwalt in Klagenfurt, wegen Unterhalts, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 27. November 2013, GZ 2 R 234/13h-116, womit das Urteil des Bezirksgerichts Villach vom 27. August 2013, GZ 3 C 144/06w-109, abgeändert wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Dr. Robert Kugler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

- `Dr. Paul Vavrovsky und Mag. Christian Schrott` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Steintra Solar GmbH`(organisation)
- `Kospachstraße 35, 3162 Rainfeld, Österreich`(address)
- `Umwelt Dorfwald ges.m.b.H.`(organisation)
- `Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich`(address)

**Example 16** (doc_id: `deanon_TRAIN/10Ob23_18g`) (sent_id: `deanon_TRAIN/10Ob23_18g_4`)


Severin Simaitis, geboren 20. November 2002, 2. 8. Juli 1967, geboren 17. November 2004, und 3. Nepomuk Sprinzl, geboren 11. September 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Miklos Stiening, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Mag. Florian Kucera` — no gold match — likely missing annotation
- `Doschek Rechtsanwalts` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Severin Simaitis`(person)
- `20. November`(date)
- `8. Juli 1967`(date)
- `17. November`(date)
- `Nepomuk Sprinzl`(person)
- `11. September`(date)
- `Mag. Miklos Stiening`(person)

**Example 17** (doc_id: `deanon_TRAIN/10Ob2_20x`) (sent_id: `deanon_TRAIN/10Ob2_20x_4`)


Matzka und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Ignaz Jungmichel, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei TalAlvalRobotik AG, Delila Leiteritz, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 25.617,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 29. Oktober 2019, GZ 2 R 151/19t-23, mit dem das Urteil des Landesgerichts Linz vom 21. August 2019, GZ 5 Cg 118/18z-19, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

**False Positives:**

- `Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei TalAlvalRobotik AG` — partial — gold is substring of pred: `TalAlvalRobotik AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ignaz Jungmichel`(person)
- `TalAlvalRobotik AG`(organisation)
- `Delila Leiteritz`(person)

**Example 18** (doc_id: `deanon_TRAIN/10Ob2_22z`) (sent_id: `deanon_TRAIN/10Ob2_22z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Calvin Amorelli, vertreten durch Dr. Martin Hembach, Rechtsanwalt in Wiener Neustadt, gegen die beklagte Partei Strathewerd u. Niemetz Metall GmbH, Dolores Chatzakis, vertreten durch Mag. Martin Trapichler, Rechtsanwalt in Wien, wegen 13.639,20 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 25. Oktober 2021, GZ 18 R 67/21p-16, mit dem das Urteil des Bezirksgerichts Wiener Neustadt vom 7. Juni 2021, GZ 7 C 117/21b-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Martin Hembach` — no gold match — likely missing annotation
- `Mag. Martin Trapichler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Calvin Amorelli`(person)
- `Strathewerd u. Niemetz Metall GmbH`(organisation)
- `Dolores Chatzakis`(person)

**Example 19** (doc_id: `deanon_TRAIN/10Ob3_12g`) (sent_id: `deanon_TRAIN/10Ob3_12g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Helge Monhemius, Bakk. techn., vertreten durch Dr. Georg Gorton und DDr. Birgit Gorton, Rechtsanwälte in Klagenfurt, gegen die beklagte Partei Ing. Eugenia Welze, vertreten durch Dr. Gottfried Kassin, Rechtsanwalt in St. Veit an der Glan, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 26. Mai 2011, GZ 2 R 83/11z-49, mit dem das Urteil des Bezirksgerichts St. Veit an der Glan vom 29. Oktober 2010, GZ 3 C 333/09h-34, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Georg Gorton und DDr. Birgit Gorton` — no gold match — likely missing annotation
- `Dr. Gottfried Kassin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Helge Monhemius, Bakk. techn.`(person)
- `Ing. Eugenia Welze`(person)

**Example 20** (doc_id: `deanon_TRAIN/10Ob41_14y`) (sent_id: `deanon_TRAIN/10Ob41_14y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in den verbundenen Familienrechtssachen des Antragstellers DI Dr. Jakob Krägeloh, geboren am 9. Juli 2019, vertreten durch Mag. Werner Thurner, Rechtsanwalt in Graz, gegen die Antragsgegnerinnen 1.

**False Positives:**

- `Mag. Werner Thurner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Jakob Krägeloh`(person)
- `9. Juli 2019`(date)

**Example 21** (doc_id: `deanon_TRAIN/10Ob57_13z`) (sent_id: `deanon_TRAIN/10Ob57_13z_3`)


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

**Example 22** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Dr. Marlon Richel, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Freimut & Assenov Sicherheit GmbH in Liqu, Spazgasse 41, 8524 Greim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 31.596,47 EUR und Feststellung (6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 18. Juni 2019, GZ 129 R 50/19z-21, mit dem das Urteil des Handelsgerichts Wien vom 28. März 2019, GZ 54 Cg 71/18x-17, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Vogl Rechtsanwalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Marlon Richel`(person)
- `Freimut & Assenov Sicherheit GmbH`(organisation)
- `Spazgasse 41, 8524 Greim, Österreich`(address)
- `Eckert Rechtsanwalts GmbH`(organisation)

**Example 23** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Daniel Wiegand, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei West-Medien Manufaktur GmbH in Liqu, Kanzelweg 32, 4850 Oberthalheim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Vogl Rechtsanwalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `DI Daniel Wiegand`(person)
- `West-Medien Manufaktur GmbH`(organisation)
- `Kanzelweg 32, 4850 Oberthalheim, Österreich`(address)
- `Eckert Rechtsanwalts GmbH`(organisation)

**Example 24** (doc_id: `deanon_TRAIN/10ObS150_17g`) (sent_id: `deanon_TRAIN/10ObS150_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Ing. Christian Stangl-Brachnik, MA BA und Mag. Claudia Gründel (beide aus dem Kreis der Arbeitgeber) als weitere Richter in der Sozialrechtssache der klagenden Partei OStR Esra Jakubait, vertreten durch Dr. Thomas Stampfer und Dr. Christoph Orgler, Rechtsanwälte in Graz, gegen die beklagte Partei Sozialversicherungsanstalt der Bauern, 1031 Wien, Ghegastraße 1, vertreten durch Dr. Michael Stögerer, Rechtsanwalt in Wien, wegen Ausgleichszulage, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2017, GZ 7 Rs 37/17s-11, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. April 2017, GZ 43 Cgs 113/17p-7, teils bestätigt und teils abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Thomas Stampfer und Dr. Christoph Orgler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OStR Esra Jakubait`(person)
- `Arbeits- und Sozialgericht`(organisation)

**Example 25** (doc_id: `deanon_TRAIN/17Ob10_20z`) (sent_id: `deanon_TRAIN/17Ob10_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätinnen Mag. Malesich und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Levi Adelwart, vertreten durch Stephan Briem Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Dr. Penelope Piephans als Treuhänder der Insolvenzgläubiger der Valkraftfen-Analyse Aktiengesellschaft, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH in Linz, wegen Feststellung (Streitwert 18.335,66 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. März 2020, GZ 1 R 31/20i-13, womit das Urteil des Landesgerichts Linz vom 9. Dezember 2019, GZ 4 Cg 73/18z-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Stephan Briem Rechtsanwalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Levi Adelwart`(person)
- `Dr. Penelope Piephans`(person)
- `Valkraftfen-Analyse Aktiengesellschaft`(organisation)

**Example 26** (doc_id: `deanon_TRAIN/18ONc1_21y`) (sent_id: `deanon_TRAIN/18ONc1_21y_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Senatspräsidenten Dr. Veith, die Hofräte Hon.-Prof. Dr. Höllwerth, Hon.-Prof. PD Dr. Rassi und Mag. Painsi als weitere Richter in der Schiedsrechtssache der Antragstellerin (schiedsbeklagte Partei) See-Versand Werke GmbH, Robert Leis, gegen die Antragsgegnerin (schiedsklagende Partei) Dargatz+Boedewig Telekom GmbH, ÖkR Nikolaus Buksbaum, vertreten durch Dr. Horst Pechar, Rechtsanwalt in Weiz, wegen § 602 ZPO, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der an den Obersten Gerichtshof gerichtete Antrag vom 7. 1. 2021 wird, soweit er sich an den Obersten Gerichtshof richtet, zurückgewiesen.

**False Positives:**

- `Dr. Horst Pechar` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `See-Versand Werke GmbH`(organisation)
- `Robert Leis`(person)
- `Dargatz+Boedewig Telekom GmbH`(organisation)
- `ÖkR Nikolaus Buksbaum`(person)

**Example 27** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Herbes&Vißers Heizung GmbH, Waldemar Lokämper, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Traun-Luftfahrt GmbH, VetR DDr. Walter Stuehrmann, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

**False Positives:**

- `Dr. Andreas Oberbichler und Dr. Michael Kramer` — no gold match — likely missing annotation
- `Mag. Maximilian Kocher` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Landesgericht Wiener Neustadt`(organisation)
- `Herbes&Vißers Heizung GmbH`(organisation)
- `Waldemar Lokämper`(person)
- `Traun-Luftfahrt GmbH`(organisation)
- `VetR DDr. Walter Stuehrmann`(person)
- `Landesgericht Feldkirch`(organisation)

**Example 28** (doc_id: `deanon_TRAIN/1Nc2_20i`) (sent_id: `deanon_TRAIN/1Nc2_20i_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie den Hofrat Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei KommR Franz Kubank, vertreten durch Dr. Michael Wukoschitz, Rechtsanwalt in Wien, gegen die beklagte Partei Laurin Aichhorn a.d., Timothy Schulmeister, Serbien, wegen 600 EUR sA, über den Ordinationsantrag nach § 28 JN den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Dr. Michael Wukoschitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `KommR Franz Kubank`(person)
- `Laurin Aichhorn`(person)
- `Timothy Schulmeister`(person)
- `Bezirksgericht Schwechat`(organisation)

**Example 29** (doc_id: `deanon_TRAIN/1Ob103_17d`) (sent_id: `deanon_TRAIN/1Ob103_17d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Laura Overbeeke, BA, vertreten durch Dr. Gerhard Ebenbichler, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. Janis Marxmeyer, und 2.

**False Positives:**

- `Dr. Gerhard Ebenbichler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Laura Overbeeke, BA`(person)
- `Janis Marxmeyer`(person)

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `Judge_Richter`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `219eb9e0`  
**Description:**
Captures the name of a judge (Richter/Richterin/Vorsitzende) including complex titles and suffixes.

**Content:**
```
(?:durch\s+(?:den\s+)?(?:Richter|Richterin|Vorsitzende)\s+)([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|ÖkR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|Dr\.\s+Univ\.-Prof\.in?|Univ\.-Prof\.in?|Priv\.-Doz\.in?|Hon\.-Prof\.in?)?)?)(?:\s+(?:in der|über die|in der Verwaltungsstrafsache))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Herr_Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `214b5905`  
**Description:**
Captures full names following 'Herr' or 'Herrn'.

**Content:**
```
(?:Herrn?\s+)([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Frau_Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ae51c48f`  
**Description:**
Captures full names following 'Frau'.

**Content:**
```
(?:Frau\s+)([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)+)
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

## `Title_Name_Context`

**F1:** 0.050 | **Precision:** 0.028 | **Recall:** 0.264  

**Format:** `regex`  
**Rule ID:** `9a5bee62`  
**Description:**
Captures names with titles (Dr., Mag., Ing., etc.) in general contexts, ensuring at least a first and last name.

**Content:**
```
(?:^|\s)([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)+)(?:\s+(?:Dr\.in?|Mag\.in?|Ing\.in?|Prof\.in?|Univ\.-Prof\.in?|Priv\.-Doz\.in?|Hon\.-Prof\.in?|MedR|VetR|Techn|Ri|Ri2|Ri3|R\.in?|[A-Z]\.)?)?(?:\s|$|,|\.|\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.028 | 0.264 | 0.050 | 13210 | 365 | 12845 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 365 | 12845 | 1020 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Schramm als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Ivan Dimitroff, geboren am 19. Mai 1960, AZ 7 P 203/15g des Bezirksgerichts Mödling, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Mödling zurückgestellt.

| Predicted | Gold |
|---|---|
| `Ivan Dimitroff` | `Ivan Dimitroff` |

**Missed by this rule (FN):**

- `19. Mai 1960` (date)
- `Bezirksgerichts Mödling` (organisation)
- `Bezirksgericht Mödling` (organisation)

**Example 1** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und die Hofräte Dr. Fellinger und Dr. Schramm als weitere Richter in der Pflegschaftssache der Minderjährigen Delia Truepschuch, geboren am 1. Februar 2026, und Aloisa Eckmaier, geboren am 28. Februar 1976, AZ 2 PS 117/09t des Bezirksgerichts Feldkirchen, infolge Vorlage zur Genehmigung der Übertragung gemäß § 111 JN an das Bezirksgericht Neunkirchen, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Übertragung der Zuständigkeit zur Besorgung dieser Pflegschaftssache an das Bezirksgericht Neunkirchen wird genehmigt.

| Predicted | Gold |
|---|---|
| `Delia Truepschuch` | `Delia Truepschuch` |
| `Aloisa Eckmaier` | `Aloisa Eckmaier` |

**Missed by this rule (FN):**

- `1. Februar 2026` (date)
- `28. Februar 1976` (date)
- `Bezirksgericht Neunkirchen` (organisation)
- `Bezirksgericht Neunkirchen` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_0`)


Gericht OGH

**False Positives:**

- `Gericht OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Karin Meiwaldt, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Katharina Tomandl, MA, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Kopf Der Oberste Gerichtshof` — no gold match — likely missing annotation
- `Partei Karin Meiwaldt` — partial — gold is substring of pred: `Karin Meiwaldt`
- `Partei Katharina Tomandl` — positional overlap with gold: `Katharina Tomandl, MA`
- `Ernst Michael Lang` — partial — pred is substring of gold: `Mag. Ernst Michael Lang`
- `Spruch Der Ordinationsantrag` — no gold match — likely missing annotation

> overlaps gold: 3  |  likely missing annotation: 2

**Gold Entities:**

- `Karin Meiwaldt`(person)
- `Katharina Tomandl, MA`(person)
- `Mag. Ernst Michael Lang`(person)

**Example 2** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_4`)


Text Begründung: Die Klägerin begehrt mit der am 4. 8. 2017 beim Bezirksgericht Steyr eingebrachten Klage von dem in der Schweiz ansässigen Beklagten 4.660 EUR sA.

**False Positives:**

- `Bezirksgericht Steyr` — type mismatch — same span as gold: `Bezirksgericht Steyr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Steyr`(organisation)

**Example 3** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_6`)


Die Aktiengesellschaft habe damit geworben, mit den eingezahlten Beträgen Edelmetalle zu marktüblichen Preisen zu erwerben, zu lagern und zu verwalten und habe dem Beklagten in dessen Funktion als Rechtsanwalt und öffentlicher Notar den Auftrag erteilt, jährliche Prüfberichte über den vollständigen Bestand zu erstellen.

**False Positives:**

- `Die Aktiengesellschaft` — type mismatch — same span as gold: `Die Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Die Aktiengesellschaft`(organisation)

**Example 4** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_7`)


Der Beklagte habe seine Aufsichts- und Prüfpflichten jedoch verletzt, rechtswidrig gehandelt und arglistig einen wesentlichen Irrtum verursacht.

**False Positives:**

- `Der Beklagte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_9`)


Der Beklagte erhob die Einrede der internationalen Unzuständigkeit, hilfsweise die Einrede der internationalen Streitanhängigkeit sowie die Einrede der örtlichen Unzuständigkeit des angerufenen Gerichts.

**False Positives:**

- `Der Beklagte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_10`)


Mit Beschluss vom 8. 10.

**False Positives:**

- `Mit Beschluss` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_11`)


2018 erklärte sich dasBezirksgericht Steyrfür örtlich unzuständig und überwies (antragsgemäß) die Rechtssache an das nicht offenbar unzuständige Bezirksgericht Salzburg.

**False Positives:**

- `Bezirksgericht Salzburg` — type mismatch — same span as gold: `Bezirksgericht Salzburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Salzburg`(organisation)

**Example 8** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_12`)


DasBezirksgericht Salzburgwies mit Beschluss vom 12. 11. 2018 die Klage wegen internationaler und örtlicher Unzuständigkeit zurück (ON 31).

**False Positives:**

- `DasBezirksgericht Salzburgwies` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_13`)


In ihrem gegen diesen Beschluss erhobenenRekursbeantragte die Klägerin hilfsweise (für den Fall, dass ihrem Rekurs nicht stattgegeben werden sollte) die Ordination gemäß § 28 JN an ein vom Obersten Gerichtshof zu benennendes Bezirksgericht (ON 34).

**False Positives:**

- `Obersten Gerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_14`)


DasLandesgericht Salzburgals Rekursgericht gab dem Rekurs nicht Folge und erachtete den Revisionsrekurs im Hinblick auf § 528 Abs 2 Z 1 ZPO (Entscheidungsgegenstand 5.000 EUR nicht übersteigend) als jedenfalls unzulässig (ON 38).

**False Positives:**

- `DasLandesgericht Salzburgals Rekursgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_15`)


Dieser Beschluss ist rechtskräftig.

**False Positives:**

- `Dieser Beschluss` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_16`)


Rechtliche Beurteilung Der Ordinationsantrag ist nicht berechtigt.

**False Positives:**

- `Rechtliche Beurteilung Der Ordinationsantrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_17`)


1. Die Ordination nach § 28 Abs 1 Z 1 JN setzt die internationale Zuständigkeit Österreichs voraus (RIS-Justiz RS0118239;

**False Positives:**

- `Die Ordination` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_18`)


RS0053178 [T10];GarberinFasching/Konecny3§ 28 JN Rz 22).

**False Positives:**

- `JN Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_19`)


Ist über die internationale Zuständigkeit bereits eine rechtskräftige Entscheidung ergangen, ist der Oberste Gerichtshof an diese Entscheidung gebunden (Garberin Fasching/Konecny3§ 28 JN Rz 25;

**False Positives:**

- `Oberste Gerichtshof` — no gold match — likely missing annotation
- `JN Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 16** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_22`)


Da das Bezirksgericht Salzburg die internationale Zuständigkeit Österreichs zur Erledigung der Klage rechtskräftig verneint hat, kann eine Ordination nicht mehr erfolgreich auf § 28 Abs 1 Z 1 JN gestützt werden.

**False Positives:**

- `Bezirksgericht Salzburg` — type mismatch — same span as gold: `Bezirksgericht Salzburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Salzburg`(organisation)

**Example 17** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_23`)


2.1 Als Grundlage für eine Ordination kommt daher nur der Fall des § 28 Abs 1 Z 2 JN in Betracht, wonach die Bestimmung eines örtlich zuständigen Gerichts durch den Obersten Gerichtshof dann zulässig ist, wenn der Antragsteller seinen Wohnsitz im Inland hat und im Einzelfall die Rechtsverfolgung im Ausland nicht möglich oder unzumutbar wäre (RIS-Justiz RS0112108).

**False Positives:**

- `Als Grundlage` — no gold match — likely missing annotation
- `Obersten Gerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 18** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_26`)


3. Der Ordinationsantrag war daher abzuweisen (ebenso 3 Nc 3/19z, 6 Nc 25/18f, 9 Nc 24/18f, 9 Nc 2/19x, 9 Nc 6/19k und 2 Nc 8/19b).

**False Positives:**

- `Der Ordinationsantrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_27`)


European Case Law Identifier ECLI:AT:OGH0002:2019:0100NC00011.19B.0321.000

**False Positives:**

- `European Case Law Identifier` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_0`)


Gericht OGH

**False Positives:**

- `Gericht OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Schramm als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Ivan Dimitroff, geboren am 19. Mai 1960, AZ 7 P 203/15g des Bezirksgerichts Mödling, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Mödling zurückgestellt.

**False Positives:**

- `Kopf Der Oberste Gerichtshof` — no gold match — likely missing annotation
- `Hofrat Dr` — no gold match — likely missing annotation
- `Hofrat Univ` — no gold match — likely missing annotation
- `Spruch Der Akt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 4

**Gold Entities:**

- `Ivan Dimitroff`(person)
- `19. Mai 1960`(date)
- `Bezirksgerichts Mödling`(organisation)
- `Bezirksgericht Mödling`(organisation)

**Example 22** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_4`)


Text Begründung: Mit Beschluss vom 5. September 2016 (ON 6) übertrug das Bezirksgericht Mödling die Zuständigkeit zur Führung der Pflegschaftssache – im Hinblick auf einen Aufenthaltswechsel des Minderjährigen, einem aus Syrien stammenden unbegleiteten Flüchtling – dem Bezirksgericht Judenburg, das die Übernahme mit dem kurzen Hinweis darauf ablehnte, dass der Minderjährige im Sprengel des Bezirksgerichts Judenburg keine aufrechte Meldeadresse habe (ON 7).

**False Positives:**

- `Mit Beschluss` — no gold match — likely missing annotation
- `Bezirksgericht Judenburg` — type mismatch — same span as gold: `Bezirksgericht Judenburg`
- `Bezirksgerichts Judenburg` — type mismatch — same span as gold: `Bezirksgerichts Judenburg`

> overlaps gold: 2  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Mödling`(organisation)
- `Bezirksgericht Judenburg`(organisation)
- `Bezirksgerichts Judenburg`(organisation)

**Example 23** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_5`)


Das Bezirksgericht Mödling legte den Akt zur Entscheidung gemäß § 111 Abs 2 JN dem Obersten Gerichtshof vor (ON 8), ohne den Übertragungsbeschluss an die Parteien zuzustellen.

**False Positives:**

- `Das Bezirksgericht` — positional overlap with gold: `Bezirksgericht Mödling`
- `Obersten Gerichtshof` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Mödling`(organisation)

**Example 24** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_6`)


Rechtliche Beurteilung Die Vorlage ist verfrüht.

**False Positives:**

- `Rechtliche Beurteilung Die Vorlage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_9`)


Andernfalls könnte eine Verschiebung der funktionellen Zuständigkeit eintreten, weil mangels Bestätigung des Übertragungsbeschlusses durch das Rekursgericht gar keine Grundlage für die Genehmigung einer Zuständigkeitsübertragung durch den Obersten Gerichtshof bestünde (9 Nc 15/14a;

**False Positives:**

- `Obersten Gerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_12`)


Der Akt ist daher dem übertragenden Gericht zurückzustellen, das den Übertragungsbeschluss den Verfahrensbeteiligten zuzustellen haben wird.

**False Positives:**

- `Der Akt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_TRAIN/10Nc18_16b`) (sent_id: `deanon_TRAIN/10Nc18_16b_14`)


European Case Law Identifier ECLI:AT:OGH0002:2016:0100NC00018.16B.1004.000

**False Positives:**

- `European Case Law Identifier` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_0`)


Gericht OGH

**False Positives:**

- `Gericht OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Chen Mestwerdt, Slowenien, vertreten durch Mag. Erich Hierz, Rechtsanwalt in Graz, gegen die beklagte Partei Roman Eschenweck, Deutschland, vertreten durch Salleck + Partner Rechtsanwälte in Deutschland, wegen 5.856 EUR sA, 1.342 EUR sA und 915 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag, die Rechtssache gemäß § 28 JN einem österreichischem Gericht zuzuweisen, wird zurückgewiesen.

**False Positives:**

- `Kopf Der Oberste Gerichtshof` — no gold match — likely missing annotation
- `Partei Chen Mestwerdt` — partial — gold is substring of pred: `Chen Mestwerdt`
- `Erich Hierz` — partial — pred is substring of gold: `Mag. Erich Hierz`
- `Partei Roman Eschenweck` — partial — gold is substring of pred: `Roman Eschenweck`
- `Spruch Der Antrag` — no gold match — likely missing annotation

> overlaps gold: 3  |  likely missing annotation: 2

**Gold Entities:**

- `Chen Mestwerdt`(person)
- `Mag. Erich Hierz`(person)
- `Roman Eschenweck`(person)

**Example 30** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_6`)


12. 2006 zur Einführung eines Europäischen Mahnverfahrens (EuMahnVO) vor dem Bezirksgericht für Handelssachen Wien die Zahlung von Forderungen aus in den Jahren 2018 und 2019 geschlossenen Werkverträgen.

**False Positives:**

- `Handelssachen Wien` — partial — pred is substring of gold: `Bezirksgericht für Handelssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht für Handelssachen Wien`(organisation)

**Example 31** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_7`)


[2] Das Bezirksgericht für Handelssachen Wien erließ – nach Verbesserung des Antrags – den Europäischen Zahlungsbefehl, gegen den die Beklagte fristgerecht Einspruch erhob.

**False Positives:**

- `Das Bezirksgericht` — positional overlap with gold: `Bezirksgericht für Handelssachen Wien`
- `Handelssachen Wien` — partial — pred is substring of gold: `Bezirksgericht für Handelssachen Wien`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht für Handelssachen Wien`(organisation)

**Example 32** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_9`)


Nach Aufforderung im Sinn des § 252 Abs 3 ZPO benannte die Klägerin fristgerecht das Bezirksgericht Graz-Ost als das für die Durchführung des ordentlichen Verfahrens zuständige Gericht.

**False Positives:**

- `Nach Aufforderung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Graz`(organisation)

**Example 33** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_10`)


Das Bezirksgericht für Handelssachen Wien überwies die Rechtssache an dieses Gericht.

**False Positives:**

- `Das Bezirksgericht` — positional overlap with gold: `Bezirksgericht für Handelssachen Wien`
- `Handelssachen Wien` — partial — pred is substring of gold: `Bezirksgericht für Handelssachen Wien`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht für Handelssachen Wien`(organisation)

**Example 34** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_11`)


[3] Vor dem Bezirksgericht Graz-Ost beantragte sie die Vorlage der Rechtssache an den Obersten Gerichtshof zur Ordination nach § 28 Abs 1 Z 3 JN sowie die Unterbrechung des Verfahrens bis zur Entscheidung des Obersten Gerichtshofs (ON 18).

**False Positives:**

- `Obersten Gerichtshof` — no gold match — likely missing annotation
- `Obersten Gerichtshofs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Bezirksgericht Graz`(organisation)

**Example 35** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_15`)


[4] Die Beklagte trat diesem Antrag auf Unterbrechung bei.

**False Positives:**

- `Die Beklagte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_16`)


[5] Das Bezirksgericht Graz-Ost unterbrach das Verfahren bis zur Entscheidung des Obersten Gerichtshofs, „ein örtlich zuständiges Gericht gemäß § 98 Abs 1 Z 3 JN für die Geltendmachung der Forderungen der klagenden Partei gegenüber der Beklagten aus der gegenständlichen Geschäftsbeziehung zu bestimmen“, und sprach aus, dass das Verfahren nur über Antrag der Parteien fortgesetzt werde.

**False Positives:**

- `Das Bezirksgericht` — positional overlap with gold: `Bezirksgericht Graz`
- `Obersten Gerichtshofs` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Graz`(organisation)

**Example 37** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_17`)


Die Parteien verzichteten auf Beschlussausfertigung und Rechtsmittel (ON 19).

**False Positives:**

- `Die Parteien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_19`)


Das Bezirksgericht Graz-Ost legte den Akt dem Obersten Gerichtshof zur Entscheidung nach § 28 Abs 1 Z 3 JN vor.

**False Positives:**

- `Das Bezirksgericht` — positional overlap with gold: `Bezirksgericht Graz`
- `Obersten Gerichtshof` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Graz`(organisation)

**Example 39** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_20`)


Rechtliche Beurteilung [7]

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_21`)


Die Voraussetzungen für eine Ordination durch den Obersten Gerichtshof liegen nicht vor.

**False Positives:**

- `Die Voraussetzungen` — no gold match — likely missing annotation
- `Obersten Gerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 41** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_22`)


[8] 1.1 Für das Verfahren nach der Europäischen Mahnverfahrensverordnung ist in Österreich nach § 252 Abs 2 ZPO ausschließlich das Bezirksgericht für Handelssachen Wien zuständig.

**False Positives:**

- `Handelssachen Wien` — partial — pred is substring of gold: `Bezirksgericht für Handelssachen Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht für Handelssachen Wien`(organisation)

**Example 42** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_24`)


Bei Vorliegen dieser Voraussetzungen hat das Gericht einen Europäischen Zahlungsbefehl zu erlassen (Art 12 EuMahnVO).

**False Positives:**

- `Bei Vorliegen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_29`)


[11] 2.1 Diese Vorgangsweise wurde im vorliegenden Fall eingehalten.

**False Positives:**

- `Diese Vorgangsweise` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_30`)


Die Rechtssache wurde an das von der Klägerin namhafte gemachte Bezirksgericht Graz-Ost überwiesen.

**False Positives:**

- `Die Rechtssache` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Graz`(organisation)

**Example 45** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_33`)


[12] 2.3 Solange das Bezirksgericht Graz-Ost seine sich aus § 252 Abs 3 ZPO ergebende Zuständigkeit nicht rechtskräftig verneint hat, ist der Oberste Gerichtshof nicht zur Bestimmung eines örtlich zuständigen Gerichts nach § 28 Abs 1 Z 3 JN berufen (RS0046450;

**False Positives:**

- `Oberste Gerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Graz`(organisation)

**Example 46** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_35`)


Die rechtskräftige Unterbrechung des Verfahrens bis zur Entscheidung des Obersten Gerichtshofs über den Ordinationsantrag ändert an diesem Ergebnis nichts.

**False Positives:**

- `Obersten Gerichtshofs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_36`)


Wenn die internationale Zuständigkeit eines österreichischen Gerichts zu verneinen ist, weil keine wirksame Gerichtsstandsvereinbarung vorliegt, scheidet eine Ordination durch den Obersten Gerichtshof nach § 28 Abs 1 Z 3 JN jedenfalls aus.

**False Positives:**

- `Obersten Gerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_37`)


European Case Law Identifier ECLI:AT:OGH0002:2021:0100NC00021.21A.1115.000

**False Positives:**

- `European Case Law Identifier` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_TRAIN/10Nc22_25d`) (sent_id: `deanon_TRAIN/10Nc22_25d_0`)


Gericht OGH

**False Positives:**

- `Gericht OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_TRAIN/10Nc22_25d`) (sent_id: `deanon_TRAIN/10Nc22_25d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hargassner als Vorsitzenden sowie den Vizepräsidenten Hon.-Prof. PD Dr. Rassi und den Hofrat Dr. Annerl als weitere Richter in der Rechtssache der klagenden Partei Juri Petraschk, Bakk. iur., gegen die beklagte Partei Mag. Dominik Riewert, wegen Feststellung, über den Delegierungsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an ein Gericht außerhalb des Sprengels des Oberlandesgerichts Wien wird abgewiesen.

**False Positives:**

- `Kopf Der Oberste Gerichtshof` — no gold match — likely missing annotation
- `PD Dr` — no gold match — likely missing annotation
- `Hofrat Dr` — no gold match — likely missing annotation
- `Partei Juri Petraschk` — positional overlap with gold: `Juri Petraschk, Bakk. iur.`
- `Partei Mag` — positional overlap with gold: `Mag. Dominik Riewert`
- `Dominik Riewert` — partial — pred is substring of gold: `Mag. Dominik Riewert`
- `Spruch Der Antrag` — no gold match — likely missing annotation
- `Oberlandesgerichts Wien` — no gold match — likely missing annotation

> overlaps gold: 3  |  likely missing annotation: 5

**Gold Entities:**

- `Juri Petraschk, Bakk. iur.`(person)
- `Mag. Dominik Riewert`(person)

**Example 51** (doc_id: `deanon_TRAIN/10Nc22_25d`) (sent_id: `deanon_TRAIN/10Nc22_25d_5`)


Der nach eigenen Angaben keinen „festen Wohnsitz“ habende Kläger erhob vor dem Bezirksgericht Neusiedl am See eine Klage auf Feststellung, dass der Beklagte nicht berechtigt sei, Daten in eine Datenanwendung einzufügen „bzw“ dass der Beklagte für die Entfernung solcher Daten aus der Anwendung „zuständig“ sei.

**False Positives:**

- `Bezirksgericht Neusiedl` — type mismatch — same span as gold: `Bezirksgericht Neusiedl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Neusiedl`(organisation)

**Example 52** (doc_id: `deanon_TRAIN/10Nc22_25d`) (sent_id: `deanon_TRAIN/10Nc22_25d_6`)


[2] Das Bezirksgericht Neusiedl am See und der Beklagte äußerten sich dahingehend, dass sie die Delegierung für nicht zweckmäßig erachteten.

**False Positives:**

- `Das Bezirksgericht Neusiedl` — partial — gold is substring of pred: `Bezirksgericht Neusiedl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Neusiedl`(organisation)

**Example 53** (doc_id: `deanon_TRAIN/10Nc22_25d`) (sent_id: `deanon_TRAIN/10Nc22_25d_7`)


Rechtliche Beurteilung [3]

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_TRAIN/10Nc22_25d`) (sent_id: `deanon_TRAIN/10Nc22_25d_8`)


Der Delegierungsantrag ist nicht berechtigt.

**False Positives:**

- `Der Delegierungsantrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_TRAIN/10Nc22_25d`) (sent_id: `deanon_TRAIN/10Nc22_25d_11`)


Ein Delegierungsantrag ist nur dann zweckmäßig, wenn die Rechtssache von einem anderen als dem zuständigen Gericht aller Voraussicht nach rascher und mit geringerem Kostenaufwand zu Ende geführt werden kann (RS0053169).

**False Positives:**

- `Ein Delegierungsantrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_TRAIN/10Nc22_25d`) (sent_id: `deanon_TRAIN/10Nc22_25d_13`)


Ein Delegierungsantrag nach § 31 JN kann jedoch nicht auf Gründe gestützt werden, die für eine Ablehnung von Richtern und anderen Gerichtsorganen in Betracht kommen (RS0046074).

**False Positives:**

- `Ein Delegierungsantrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_TRAIN/10Nc22_25d`) (sent_id: `deanon_TRAIN/10Nc22_25d_16`)


[7] Der Delegierungsantrag ist daher abzuweisen.

**False Positives:**

- `Der Delegierungsantrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_TRAIN/10Nc22_25d`) (sent_id: `deanon_TRAIN/10Nc22_25d_17`)


European Case Law Identifier ECLI:AT:OGH0002:2025:0100NC00022.25D.0903.000

**False Positives:**

- `European Case Law Identifier` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_0`)


Gericht OGH

**False Positives:**

- `Gericht OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und die Hofräte Dr. Fellinger und Dr. Schramm als weitere Richter in der Pflegschaftssache der Minderjährigen Delia Truepschuch, geboren am 1. Februar 2026, und Aloisa Eckmaier, geboren am 28. Februar 1976, AZ 2 PS 117/09t des Bezirksgerichts Feldkirchen, infolge Vorlage zur Genehmigung der Übertragung gemäß § 111 JN an das Bezirksgericht Neunkirchen, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Übertragung der Zuständigkeit zur Besorgung dieser Pflegschaftssache an das Bezirksgericht Neunkirchen wird genehmigt.

**False Positives:**

- `Kopf Der Oberste Gerichtshof` — no gold match — likely missing annotation
- `Bezirksgerichts Feldkirchen` — no gold match — likely missing annotation
- `Bezirksgericht Neunkirchen` — type mismatch — same span as gold: `Bezirksgericht Neunkirchen`
- `Spruch Die` — no gold match — likely missing annotation
- `Bezirksgericht Neunkirchen` — similar text (different position): `Bezirksgericht Neunkirchen`

> overlaps gold: 2  |  likely missing annotation: 3

**Gold Entities:**

- `Delia Truepschuch`(person)
- `1. Februar 2026`(date)
- `Aloisa Eckmaier`(person)
- `28. Februar 1976`(date)
- `Bezirksgericht Neunkirchen`(organisation)
- `Bezirksgericht Neunkirchen`(organisation)

**Example 61** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_4`)


Begründung:  Rechtliche Beurteilung Das bisher zuständige Bezirksgericht Feldkirchen übertrug mit seinem - den Verfahrensbeteiligten zugestellten und nicht bekämpften - Beschluss vom 7. 10.

**False Positives:**

- `Rechtliche Beurteilung Das` — no gold match — likely missing annotation
- `Bezirksgericht Feldkirchen` — type mismatch — same span as gold: `Bezirksgericht Feldkirchen`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Feldkirchen`(organisation)

**Example 62** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_5`)


2009 die Zuständigkeit zur Führung der Pflegschaftssache an das Bezirksgericht Neunkirchen, weil die beiden Minderjährigen und ihre obsorgeberechtigte Mutter, in deren Haushalt sich die Kinder nach dem pflegschaftsgerichtlich genehmigten Scheidungsvergleich hauptsächlich aufhalten sollen, sich nunmehr ständig im Sprengel dieses Gerichts aufhielten.

**False Positives:**

- `Bezirksgericht Neunkirchen` — type mismatch — same span as gold: `Bezirksgericht Neunkirchen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Neunkirchen`(organisation)

**Example 63** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_6`)


Das Bezirksgericht Neunkirchen verweigerte die Übernahme der Zuständigkeit, weil das übertragende Gericht den Antrag vom 24.

**False Positives:**

- `Das Bezirksgericht Neunkirchen` — partial — gold is substring of pred: `Bezirksgericht Neunkirchen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Neunkirchen`(organisation)

**Example 64** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_7`)


8. 2009 schon zu bearbeiten begonnen habe, ihm die verfahrensbeteiligten Personen bekannt, dem Bezirksgericht Neunkirchen aber gänzlich unbekannt seien.

**False Positives:**

- `Bezirksgericht Neunkirchen` — type mismatch — same span as gold: `Bezirksgericht Neunkirchen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Neunkirchen`(organisation)

**Example 65** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_9`)


Das übertragende Gericht legte aufgrund dieser Weigerung den Akt dem Obersten Gerichtshof als gemeinsam übergeordnetem Gericht zur Entscheidung gemäß § 111 Abs 2 JN vor.

**False Positives:**

- `Obersten Gerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_10`)


Die Übertragung ist zu genehmigen: Die Genehmigung einer Übertragung der Zuständigkeit nach § 111 Abs 2 JN hat nur zu erfolgen, wenn dies im Interesse des Pflegebefohlenen zweckmäßig erscheint.

**False Positives:**

- `Die Genehmigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_12`)


Ausschlaggebendes Kriterium für die Übertragung der Zuständigkeit zur Führung einer Pflegschaftssache ist stets das Wohl des Kindes (RIS-Justiz RS0047074; RS0046908).

**False Positives:**

- `Ausschlaggebendes Kriterium` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_TRAIN/10Nc25_09x`) (sent_id: `deanon_TRAIN/10Nc25_09x_13`)


Die Bestimmung nimmt darauf bedacht, dass ein (örtliches) Naheverhältnis zwischen dem Pflegschaftsgericht und dem Minderjährigen regelmäßig zweckmäßig und von wesentlicher Bedeutung ist.

**False Positives:**

- `Die Bestimmung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_0`)


Gericht OGH

**False Positives:**

- `Gericht OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Nowotny als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache des minderjährigen ÖkR Priv.-Doz. Sven Egerth, geboren 3. Mai 2012, AZ 36 Pu 45/23h des Bezirksgerichts Graz-West, wegen Genehmigung der Übertragung der Zuständigkeit in Pflegschaftssachen nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Graz-West zurückgestellt.

**False Positives:**

- `Kopf Der Oberste Gerichtshof` — no gold match — likely missing annotation
- `Hofrat Dr` — no gold match — likely missing annotation
- `Hofrat Mag` — no gold match — likely missing annotation
- `Sven Egerth` — partial — pred is substring of gold: `ÖkR Priv.-Doz. Sven Egerth`
- `Spruch Der Akt` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 4

**Gold Entities:**

- `ÖkR Priv.-Doz. Sven Egerth`(person)
- `3. Mai`(date)
- `Bezirksgericht Graz`(organisation)

**Example 71** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_4`)


Begründung:  Rechtliche Beurteilung [1] Mit Beschluss vom 12.

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation
- `Mit Beschluss` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 72** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_5`)


9. 2023 übertrug das Bezirksgericht Graz-West die Zuständigkeit zur Führung der Pflegschaftssache dem Bezirksgericht Braunau am Inn, das die Übernahme jedoch ablehnte.

**False Positives:**

- `Bezirksgericht Braunau` — type mismatch — same span as gold: `Bezirksgericht Braunau`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Graz`(organisation)
- `Bezirksgericht Braunau`(organisation)

**Example 73** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_6`)


[2] Das Bezirksgericht Graz-West legte den Akt daraufhin dem Obersten Gerichtshof zur Entscheidung gemäß § 111 Abs 2 JN vor, ohne den Übertragungsbeschluss den Parteien zuzustellen.

**False Positives:**

- `Das Bezirksgericht` — positional overlap with gold: `Bezirksgericht Graz`
- `Obersten Gerichtshof` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Graz`(organisation)

**Example 74** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_7`)


[3] Die Vorlage ist verfrüht.

**False Positives:**

- `Die Vorlage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_12`)


[5] Der Akt ist daher dem übertragenden Gericht zur Zustellung des Beschlusses an die Parteien zurückzustellen.

**False Positives:**

- `Der Akt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_14`)


Den Parteien steht gegen den Übertragungsbeschluss nach § 111 JN ein Rechtsmittel zu (3 Nc 1/23m;

**False Positives:**

- `Den Parteien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_TRAIN/10Nc27_23m`) (sent_id: `deanon_TRAIN/10Nc27_23m_18`)


European Case Law Identifier ECLI:AT:OGH0002:2023:0100NC00027.23M.1027.000

**False Positives:**

- `European Case Law Identifier` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_0`)


Gericht OGH

**False Positives:**

- `Gericht OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Sten und Stöwer Wind GmbH, OMedR Torsten Münchmeyer, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei OStR Gregor Ruemmel, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Kopf Der Oberste Gerichtshof` — no gold match — likely missing annotation
- `Partei Sten` — positional overlap with gold: `Sten und Stöwer Wind GmbH`
- `Wind GmbH` — partial — pred is substring of gold: `Sten und Stöwer Wind GmbH`
- `OMedR Torsten` — partial — pred is substring of gold: `OMedR Torsten Münchmeyer`
- `Alexander Rimser` — partial — pred is substring of gold: `Mag. Alexander Rimser`
- `Partei OStR Gregor Ruemmel` — partial — gold is substring of pred: `OStR Gregor Ruemmel`
- `Spruch Der Ordinationsantrag` — no gold match — likely missing annotation

> overlaps gold: 5  |  likely missing annotation: 2

**Gold Entities:**

- `Sten und Stöwer Wind GmbH`(organisation)
- `OMedR Torsten Münchmeyer`(person)
- `Mag. Alexander Rimser`(person)
- `OStR Gregor Ruemmel`(person)

**Example 80** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_4`)


Text Begründung: Das klagende Unternehmen mit Sitz in Österreich begehrt gegenüber der in Hongkong ansässigen beklagten Partei die Feststellung, dass zwischen den Parteien weder ein Data Transfer Agreement noch ein Collaboration Agreement abgeschlossen worden sei oder diese wirksam zustande gekommen seien.

**False Positives:**

- `Data Transfer Agreement` — no gold match — likely missing annotation
- `Collaboration Agreement` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 81** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_7`)


Diese Verhandlungen seien weit gediehen, es sei jedoch zu keinem schriftlichen Vertragsabschluss gekommen, da die Klägerin das ihr von der Beklagten übersandte schriftliche Vertragsanbot nicht unterfertigt habe.

**False Positives:**

- `Diese Verhandlungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_8`)


Auch ein Collaboration Agreement sei nie geschlossen worden.

**False Positives:**

- `Collaboration Agreement` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_10`)


Die Klägerin stützte die Zuständigkeit des von ihr angerufenen Landesgerichts Wr. Neustadt als Handelsgericht auf § 88 Abs 1 und 2 JN.

**False Positives:**

- `Landesgerichts Wr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_11`)


Für den Fall der örtlichen Unzuständigkeit des angerufenen Gerichts beantragte die Klägerin gemäß § 28 JN die Bestimmung des Landesgerichts Wr. Neustadt als Handelsgericht als für den gegenständlichen Rechtsstreit örtlich zuständiges Gericht.

**False Positives:**

- `Landesgerichts Wr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_14`)


Die Unzumutbarkeit der Rechtsverfolgung im Ausland ergebe sich daraus, dass eine ausländische Entscheidung in Österreich nicht anerkannt und vollstreckt werden würde, eine dringende Entscheidung nicht erreicht werden könne und eine Prozessführung im Ausland äußerst kostspielig wäre.

**False Positives:**

- `Die Unzumutbarkeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_15`)


Das Erstgericht wies die Klage wegen Fehlens eines inländischen Gerichtsstands und somit der österreichischen internationalen Zuständigkeit rechtskräftig zurück und legte daraufhin den Akt dem Obersten Gerichtshof zur Entscheidung über den hilfsweise gestellten Ordinationsantrag vor.

**False Positives:**

- `Das Erstgericht` — no gold match — likely missing annotation
- `Obersten Gerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 87** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_16`)


Rechtliche Beurteilung Der Ordinationsantrag ist nicht berechtigt.

**False Positives:**

- `Rechtliche Beurteilung Der Ordinationsantrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_18`)


Gemäß § 28 Abs 4 zweiter Satz JN hat der Kläger in streitigen bürgerlichen Rechtssachen das Vorliegen der Voraussetzungen nach Abs 1 Z 2 oder 3 zu behaupten und zu bescheinigen.

**False Positives:**

- `Satz JN` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_19`)


2. § 28 Abs 1 Z 2 JN soll die Fälle abdecken, in denen trotz Fehlens eines Gerichtsstands im Inland ein Bedürfnis nach Gewährung inländischen Rechtsschutzes vorhanden ist, weil ein Naheverhältnis zum Inland besteht und im Einzelfall keine effektive Klagemöglichkeit im Ausland gegeben ist (vglGarberinFasching/Konecny3I § 28 JN Rz 54;

**False Positives:**

- `JN Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 90** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_22`)


Das Vorliegen der zweiten Voraussetzung (nämlich die Unmöglichkeit oder Unzumutbarkeit der Rechtsverfolgung im Ausland) wird in der Rechtsprechung insbesondere dann bejaht, wenn die ausländische Entscheidung in Österreich nicht anerkannt oder vollstreckt wird (unter der weiteren Voraussetzung, dass eine Exekutionsführung im Inland überhaupt geplant ist - RIS-Justiz RS0046148 [T10]), eine dringende Entscheidung im Ausland nicht rechtzeitig erreicht werden kann, eine Prozessführung im Ausland wenigstens eine der Parteien politischer Verfolgung aussetzen würde oder wenn die Prozessführung im Ausland äußerst kostspielig wäre (MayrinRechberger, ZPO4§ 28 JN Rz 4 mwN; RIS-Justiz RS0046148).

**False Positives:**

- `Das Vorliegen` — no gold match — likely missing annotation
- `JN Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 91** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_23`)


3.1 Auch wenn die früher vorgenommene Ausdehnung des Vertrags zwischen dem Vereinigten Königreich von Großbritannien und Nordirland und der Republik Österreich über die gegenseitige Anerkennung und Vollstreckung gerichtlicher Entscheidungen in Zivil- und Handelssachen (BGBl 1962/224) auf Hongkong (BGBl 1978/90) - seit Beendigung des Britischen Hoheitsrechts - keine Geltung mehr für Hongkong hat (BGBl III 1999/51) und zwischen Österreich und China die Gegenseitigkeit im Verhältnis beider Staaten, was die Anerkennung und Vollstreckbarkeit gerichtlicher Exekutionstitel in jeweils anderen Staaten anlangt, fehlt (vgl 3 Nc 15/14g), kann die mangelnde Vollstreckbarkeit ausländischer Entscheidungen ein besonderes Rechtsschutzbedürfnis für die Inanspruchnahme inländischer Gerichte nur dann begründen, wenn die Entscheidungen des an sich berufenen Staats in Österreich vollstreckt werden müssten (4 Nd 507/96;

**False Positives:**

- `Britischen Hoheitsrechts` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 92** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_25`)


Dabei ist im vorliegenden Fall im Hinblick auf das von der Klägerin ausschließlich erhobene Feststellungsbegehren zu berücksichtigen, dass ein Feststellungsurteil eines ausländischen Gerichts, das eine vermögensrechtliche Angelegenheit zum Gegenstand hat, auf Antrag einer der Parteien gemäß den §§ 79, 85 EO im Inland zwar anerkannt werden kann, Feststellungsurteile aber nur deklarative Wirkung haben, also keinen Leistungsanspruch schaffen, und daher - abgesehen von einem in das Urteil aufgenommenen Leistungsausspruch über den Prozesskostenersatz - nicht vollstreckbar sind (vglFaschinginFasching/Konecny2III § 228 ZPO Rz 145).

**False Positives:**

- `ZPO Rz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_26`)


Den Angaben der Klägerin ist nicht zu entnehmen, dass die Beklagte über irgendein Vermögen im Inland verfügt.

**False Positives:**

- `Den Angaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 94** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_32`)


Im Regelfall stellt sich nämlich die Kostenfrage bei Distanzprozessen für beide Parteien jeweils mit umgekehrten Vorzeichen und geht daher zu Lasten des Klägers (RIS-Justiz RS0046420).

**False Positives:**

- `Im Regelfall` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 95** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_35`)


Der Antrag war daher abzuweisen.

**False Positives:**

- `Der Antrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 96** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_36`)


European Case Law Identifier ECLI:AT:OGH0002:2014:0100NC00028.14W.1204.000

**False Positives:**

- `European Case Law Identifier` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 97** (doc_id: `deanon_TRAIN/10Nc2_10s`) (sent_id: `deanon_TRAIN/10Nc2_10s_0`)


Gericht OGH

**False Positives:**

- `Gericht OGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 98** (doc_id: `deanon_TRAIN/10Nc2_10s`) (sent_id: `deanon_TRAIN/10Nc2_10s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Pflegschaftssache des mj Andreas Wolfgang Spinner, geboren am 8. Juli 2004, und der mj Herta Vanessa Schlichtcroll, geboren am 4. April 2007, wegen Übertragung der Zuständigkeit nach § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Die mit Beschluss des Bezirksgerichts Salzburg vom 9. 9. 2009, AZ 42 PS 56/09a, verfügte Übertragung der Zuständigkeit zur Führung der Pflegschaftssache an das Bezirksgericht Mödling wird genehmigt.

**False Positives:**

- `Kopf Der Oberste Gerichtshof` — no gold match — likely missing annotation
- `Andreas Wolfgang Spinner` — partial — gold is substring of pred: `Spinner`
- `Herta Vanessa Schlichtcroll` — partial — gold is substring of pred: `Schlichtcroll`
- `Spruch Die` — no gold match — likely missing annotation
- `Bezirksgerichts Salzburg` — no gold match — likely missing annotation

> overlaps gold: 2  |  likely missing annotation: 3

**Gold Entities:**

- `Spinner`(person)
- `Schlichtcroll`(person)
- `Bezirksgericht Mödling`(organisation)

**Example 99** (doc_id: `deanon_TRAIN/10Nc2_10s`) (sent_id: `deanon_TRAIN/10Nc2_10s_4`)


Begründung:  Rechtliche Beurteilung Die Zuständigkeit in der früher beim Bezirksgericht Steyr und beim Bezirksgericht Mattighofen anhängig gewesenen Pflegschaftssache wurde mit Beschluss des Bezirksgerichts Salzburg vom 26.

**False Positives:**

- `Rechtliche Beurteilung Die` — no gold match — likely missing annotation
- `Bezirksgericht Steyr` — type mismatch — same span as gold: `Bezirksgericht Steyr`
- `Bezirksgericht Mattighofen` — type mismatch — same span as gold: `Bezirksgericht Mattighofen`
- `Bezirksgerichts Salzburg` — no gold match — likely missing annotation

> overlaps gold: 2  |  likely missing annotation: 2

**Gold Entities:**

- `Bezirksgericht Steyr`(organisation)
- `Bezirksgericht Mattighofen`(organisation)

</details>

---

## `Representative_vertreten_durch`

**F1:** 0.007 | **Precision:** 0.016 | **Recall:** 0.004  

**Format:** `regex`  
**Rule ID:** `03afec1a`  
**Description:**
Captures the name of a representative (lawyer/tax advisor) introduced by 'vertreten durch'.

**Content:**
```
(?:vertreten\s+durch\s+)([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|ÖkR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB)?)?)(?:,\s+[A-Z]|\s+GmbH|\s+Steuerberatung)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.016 | 0.004 | 0.007 | 379 | 6 | 373 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 6 | 373 | 1379 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Karin Meiwaldt, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Katharina Tomandl, MA, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Ernst Michael Lang` | `Mag. Ernst Michael Lang` |

**Missed by this rule (FN):**

- `Karin Meiwaldt` (person)
- `Katharina Tomandl, MA` (person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc21_21a`) (sent_id: `deanon_TRAIN/10Nc21_21a_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Chen Mestwerdt, Slowenien, vertreten durch Mag. Erich Hierz, Rechtsanwalt in Graz, gegen die beklagte Partei Roman Eschenweck, Deutschland, vertreten durch Salleck + Partner Rechtsanwälte in Deutschland, wegen 5.856 EUR sA, 1.342 EUR sA und 915 EUR sA, über den Ordinationsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag, die Rechtssache gemäß § 28 JN einem österreichischem Gericht zuzuweisen, wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Erich Hierz` | `Mag. Erich Hierz` |

**Missed by this rule (FN):**

- `Chen Mestwerdt` (person)
- `Roman Eschenweck` (person)

**Example 2** (doc_id: `deanon_TRAIN/10Nc28_14w`) (sent_id: `deanon_TRAIN/10Nc28_14w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Sten und Stöwer Wind GmbH, OMedR Torsten Münchmeyer, vertreten durch Mag. Alexander Rimser, Rechtsanwalt in Wien, gegen die beklagte Partei OStR Gregor Ruemmel, Hongkong, wegen Feststellung (Streitwert: 31.000 EUR sA), über den Antrag der klagenden Partei nach § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Alexander Rimser` | `Mag. Alexander Rimser` |

**Missed by this rule (FN):**

- `Sten und Stöwer Wind GmbH` (organisation)
- `OMedR Torsten Münchmeyer` (person)
- `OStR Gregor Ruemmel` (person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob10_16t`) (sent_id: `deanon_TRAIN/10Ob10_16t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei DI Fabian Reifrath, vertreten durch Dr. Wilhelm Schlein Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Elina Woyte, vertreten durch Dr. Werner Goeritz, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 2. Dezember 2015, GZ 40 R 205/15s-34, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Werner Goeritz` | `Dr. Werner Goeritz` |

**Missed by this rule (FN):**

- `DI Fabian Reifrath` (person)
- `Wilhelm Schlein Rechtsanwalt GmbH` (organisation)
- `Elina Woyte` (person)

**Example 4** (doc_id: `deanon_TRAIN/3Ob152_10i`) (sent_id: `deanon_TRAIN/3Ob152_10i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Exekutionssache der betreibenden Partei KMN Versicherung Werke AG, Corbinian Pichlmaier, vertreten durch Dr. Erich Kafka, Dr. Manfred Palkovits, Rechtsanwälte in Wien, gegen die verpflichtete Partei Severin Wellenbrink, vertreten durch Dr. Philipp Jessich, Rechtsanwalt in Wien, wegen Aufschiebung einer Räumungsexekution, über den Revisionsrekurs der betreibenden Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 12. Mai 2010, GZ 39 R 44/10z-22, womit der Beschluss des Bezirksgerichts Fünfhaus vom 14. Jänner 2010, GZ 10 E 171/09d-6, abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Erich Kafka` | `Dr. Erich Kafka` |

**Missed by this rule (FN):**

- `KMN Versicherung Werke AG` (organisation)
- `Corbinian Pichlmaier` (person)
- `Dr. Manfred Palkovits` (person)
- `Severin Wellenbrink` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Nc11_19b`) (sent_id: `deanon_TRAIN/10Nc11_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann als weitere Richter in der Rechtssache der klagenden Partei Karin Meiwaldt, vertreten durch Neumayer, Walter & Haslinger Rechtsanwälte-Partnerschaft (OG) in Wien, gegen die beklagte Partei Katharina Tomandl, MA, Schweiz, vertreten durch Mag. Ernst Michael Lang, Rechtsanwalt in Hohenems, wegen 4.660 EUR sA, über den Antrag der Klägerin auf Ordination gemäß § 28 JN den Beschluss gefasst:  Spruch Der Ordinationsantrag wird abgewiesen.

**False Positives:**

- `Neumayer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Karin Meiwaldt`(person)
- `Katharina Tomandl, MA`(person)
- `Mag. Ernst Michael Lang`(person)

**Example 1** (doc_id: `deanon_TRAIN/10Nc2_12v`) (sent_id: `deanon_TRAIN/10Nc2_12v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei C. Dersudheim Digital GmbH, Taxlbergstraße 247, 8151 Rohrbach, Österreich, vertreten durch Dr. Carl Benkhofer, Rechtsanwalt in Wien, gegen die beklagte Partei Ingolf Grimpe, vertreten durch Greiml & Horwath Rechtsanwaltspartnerschaft in Graz, wegen 5.232 EUR sA, über den Delegierungsantrag der klagenden Partei im Verfahren AZ 14 C 1302/11a des Bezirksgerichts Graz-West in nichtöffentlicher Sitzung, den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Graz-West das Bezirksgericht Fünfhaus bestimmt.

**False Positives:**

- `Dr. Carl Benkhofer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dersudheim Digital GmbH`(organisation)
- `Taxlbergstraße 247, 8151 Rohrbach, Österreich`(address)
- `Ingolf Grimpe`(person)
- `Bezirksgericht Fünfhaus`(organisation)

**Example 2** (doc_id: `deanon_TRAIN/10Nc7_10a`) (sent_id: `deanon_TRAIN/10Nc7_10a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger und Hon.-Prof. Dr. Neumayr als weitere Richter in der Verlassenschaftssache nach dem am 9. September 2009 verstorbenen, zuletzt in Tschiggfreystraße 46, 3240 Loitsdorf, Österreich, wohnhaft gewesenen Manfred Johann Pingert, AZ 1 A 349/09w des Bezirksgerichts Kitzbühel, über den Delegierungsantrag der Karin Czychy, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, den B e s c h l u s s gefasst:  Spruch Dem Delegierungsantrag wird stattgegeben.

**False Positives:**

- `Mag. Maximilian Kocher` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Tschiggfreystraße 46, 3240 Loitsdorf, Österreich`(address)
- `Pingert`(person)
- `Czychy`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Nc9_15b`) (sent_id: `deanon_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Mur Kraftalheim Holding GmbH, Gerald Zacharie, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Nexstein Textil GmbH, Dipl.-Ing. Lynn Forkarth, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

**False Positives:**

- `Dr. Roland Kassowitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgericht Linz`(organisation)
- `Mur Kraftalheim Holding GmbH`(organisation)
- `Gerald Zacharie`(person)
- `Nexstein Textil GmbH`(organisation)
- `Dipl.-Ing. Lynn Forkarth`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob102_18z`) (sent_id: `deanon_TRAIN/10Ob102_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Skrzypczik + Duchscherer Digital AG, Adelheid Lochmaier, vertreten durch Mag. Franz Podovsovnik, Rechtsanwalt in Wien, gegen die beklagte Partei Ursula Antoniadis, vertreten durch Knirsch – Braun – Fellner Rechtsanwälte in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 5. September 2018, GZ 40 R 39/18h-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mag. Franz Podovsovnik` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Skrzypczik + Duchscherer Digital AG`(organisation)
- `Adelheid Lochmaier`(person)
- `Ursula Antoniadis`(person)

**Example 5** (doc_id: `deanon_TRAIN/10Ob105_15m`) (sent_id: `deanon_TRAIN/10Ob105_15m_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei Alsteinost GmbH, Anna Kisaoglu, Bakk. iur., vertreten durch Dr. Erich Kafka und Dr. Manfred Palkovits, Rechtsanwälte in Wien, gegen die beklagte Partei Ing. Mag. Adam Kratki, vertreten durch Gheneff - Rami - Sommer Rechtsanwälte OG in Wien, wegen Aufkündigung, infolge außerordentlicher Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 11. Juni 2015, GZ 39 R 41/15s-29, in nichtöffentlicher Sitzung den B e s c h l u s s gefasst:  Spruch

**False Positives:**

- `Dr. Erich Kafka und Dr. Manfred Palkovits` — partial — gold is substring of pred: `Dr. Erich Kafka`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alsteinost GmbH`(organisation)
- `Anna Kisaoglu, Bakk. iur.`(person)
- `Dr. Erich Kafka`(person)
- `Dr. Manfred Palkovits`(person)
- `Mag. Adam Kratki`(person)

**Example 6** (doc_id: `deanon_TRAIN/10Ob10_16t`) (sent_id: `deanon_TRAIN/10Ob10_16t_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm, die Hofrätin Dr. Fichtenau und den Hofrat Mag. Ziegelbauer als weitere Richter in der Rechtssache der klagenden Partei DI Fabian Reifrath, vertreten durch Dr. Wilhelm Schlein Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Elina Woyte, vertreten durch Dr. Werner Goeritz, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 2. Dezember 2015, GZ 40 R 205/15s-34, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Wilhelm Schlein Rechtsanwalt` — positional overlap with gold: `Wilhelm Schlein Rechtsanwalt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DI Fabian Reifrath`(person)
- `Wilhelm Schlein Rechtsanwalt GmbH`(organisation)
- `Elina Woyte`(person)
- `Dr. Werner Goeritz`(person)

**Example 7** (doc_id: `deanon_TRAIN/10Ob10_18w`) (sent_id: `deanon_TRAIN/10Ob10_18w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Agrargemeinschaft Jonasgasse 71, 4760 Weeg, Österreich, vertreten durch Dr. Alois Schneider, Rechtsanwalt in Rattenberg, wider die beklagte Partei Corinna Elfe, vertreten durch Dr. Walter Hausberger, Dr. Katharina Moritz und Dr. Alfred Schmidt, Rechtsanwälte in Wörgl, wegen Entfernung und Unterlassung (Revisionsinteresse 10.000 EUR), infolge Revision der klagenden Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 3. November 2017, GZ 3 R 172/17s-22, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Rattenberg vom 17. Mai 2017, GZ 3 C 401/15k-18, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Alois Schneider` — no gold match — likely missing annotation
- `Dr. Walter Hausberger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Jonasgasse 71, 4760 Weeg, Österreich`(address)
- `Corinna Elfe`(person)

**Example 8** (doc_id: `deanon_TRAIN/10Ob11_15p`) (sent_id: `deanon_TRAIN/10Ob11_15p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden sowie durch die Hofräte und Hofrätinnen Univ.-Prof. Dr. Neumayr, Dr. Schramm, Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Viktoria Hornburg, vertreten durch Dr. Walter Vasoll und Mag. Marion Vasoll, Rechtsanwälte in Hermagor, gegen die beklagte Partei Mercedes Jungschlaeger, vertreten durch Dr. Thomas Romauch, Rechtsanwalt in Wien, wegen Feststellung und Einwilligung (6.000 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 4. Dezember 2014, GZ 3 R 169/14h-14, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Hermagor vom 9. August 2014, GZ 1 C 563/13b-10, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision der beklagten Partei wird zurückgewiesen.

**False Positives:**

- `Dr. Walter Vasoll und Mag. Marion Vasoll` — no gold match — likely missing annotation
- `Dr. Thomas Romauch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Viktoria Hornburg`(person)
- `Mercedes Jungschlaeger`(person)

**Example 9** (doc_id: `deanon_TRAIN/10Ob12_24y`) (sent_id: `deanon_TRAIN/10Ob12_24y_5`)


Isidor Janofske, beide vertreten durch Ghendler Ruvinskij Rechtsanwaltsgesellschaft mbH in Wien, gegen die beklagte Partei Wolfram Fritzsche S.p.A., VetR Lukas Dickhaus, vertreten durch bpv Hügel Rechtsanwälte GmbH in Wien, wegen 71.425,56 EUR sA, aus Anlass der Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 20. Dezember 2023, GZ 6 R 68/23a-41, mit dem über Berufung der beklagten Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 21. August 2023, GZ 19 Cg 10/22f-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die gemeinsame Anzeige der Parteien über das vereinbarte „ewige“ Ruhen des Verfahrens wird zur Kenntnis genommen.

**False Positives:**

- `Ghendler Ruvinskij Rechtsanwaltsgesellschaft mbH in Wien, gegen die beklagte Partei Wolfram Fritzsche S.p.A.` — partial — gold is substring of pred: `Wolfram Fritzsche`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Isidor Janofske`(person)
- `Wolfram Fritzsche`(person)
- `VetR Lukas Dickhaus`(person)

**Example 10** (doc_id: `deanon_TRAIN/10Ob13_15g`) (sent_id: `deanon_TRAIN/10Ob13_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die Hofrätinnen Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Zoltan Alfermann, vertreten durch Dr. Karl-Heinz Plankel und andere Rechtsanwälte in Dornbirn, gegen die beklagte Partei DonauFurtostBildung GmbH, KzlR Noah Christansen, vertreten durch Lederer Rechtsanwalt GmbH in Wien, wegen 19.151,17 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. November 2014, GZ 4 R 106/14h-21, womit das Urteil des Handelsgerichts Wien vom 24. März 2014, GZ 23 Cg 183/10b-17, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Lederer Rechtsanwalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zoltan Alfermann`(person)
- `DonauFurtostBildung GmbH`(organisation)
- `KzlR Noah Christansen`(person)

**Example 11** (doc_id: `deanon_TRAIN/10Ob13_20i`) (sent_id: `deanon_TRAIN/10Ob13_20i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Miranda Klagemann, vertreten durch Dr. Andreas Ladstätter, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. DI Adolf Kowallek, und 2. Ing. Janis Grottian, beide vertreten durch Dr. Walter Schuhmeister und Mag. Franz Haydn, Rechtsanwälte in Schwechat, wegen 15.000 EUR sA, infolge Revision der beklagten Parteien (Revisionsinteresse 6.250 EUR) gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 30. Jänner 2019, GZ 34 R 66/18k-27, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Innere Stadt Wien vom 23. März 2018, GZ 37 C 780/16f-18, teilweise abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Walter Schuhmeister und Mag. Franz Haydn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Miranda Klagemann`(person)
- `DI Adolf Kowallek`(person)
- `Ing. Janis Grottian`(person)

**Example 12** (doc_id: `deanon_TRAIN/10Ob16_14x`) (sent_id: `deanon_TRAIN/10Ob16_14x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm sowie die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Walter Gritzmacher, vertreten durch Dr. Birgit Lajtai-Nagl, Rechtsanwältin in Villach, gegen die beklagte Partei Dr. Ariadne Graspointner, vertreten durch Dr. Robert Kugler, Rechtsanwalt in Klagenfurt, wegen Unterhalts, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 27. November 2013, GZ 2 R 234/13h-116, womit das Urteil des Bezirksgerichts Villach vom 27. August 2013, GZ 3 C 144/06w-109, abgeändert wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Dr. Robert Kugler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

- `Dr. Paul Vavrovsky und Mag. Christian Schrott` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Steintra Solar GmbH`(organisation)
- `Kospachstraße 35, 3162 Rainfeld, Österreich`(address)
- `Umwelt Dorfwald ges.m.b.H.`(organisation)
- `Bäckenbrünnlgasse 38, 2571 Thenneberg, Österreich`(address)

**Example 16** (doc_id: `deanon_TRAIN/10Ob23_18g`) (sent_id: `deanon_TRAIN/10Ob23_18g_4`)


Severin Simaitis, geboren 20. November 2002, 2. 8. Juli 1967, geboren 17. November 2004, und 3. Nepomuk Sprinzl, geboren 11. September 2006, vertreten durch Mag. Florian Kucera, Rechtsanwalt in Wien, wegen Unterhaltsverpflichtung des Vaters Mag. Miklos Stiening, vertreten durch Doschek Rechtsanwalts GmbH in Wien, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 4. Oktober 2017, GZ 42 R 164/17d-65 in der Fassung des Berichtigungsbeschlusses vom 17. Jänner 2018, GZ 42 R 164/17d-67, mit dem der Beschluss des Bezirksgerichts Döbling vom 3. März 2017, GZ 2 Pu 132/15z-58, infolge Rekurses des Vaters teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Mag. Florian Kucera` — no gold match — likely missing annotation
- `Doschek Rechtsanwalts` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Severin Simaitis`(person)
- `20. November`(date)
- `8. Juli 1967`(date)
- `17. November`(date)
- `Nepomuk Sprinzl`(person)
- `11. September`(date)
- `Mag. Miklos Stiening`(person)

**Example 17** (doc_id: `deanon_TRAIN/10Ob2_20x`) (sent_id: `deanon_TRAIN/10Ob2_20x_4`)


Matzka und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Ignaz Jungmichel, vertreten durch Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei TalAlvalRobotik AG, Delila Leiteritz, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 25.617,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 29. Oktober 2019, GZ 2 R 151/19t-23, mit dem das Urteil des Landesgerichts Linz vom 21. August 2019, GZ 5 Cg 118/18z-19, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

**False Positives:**

- `Poduschka Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei TalAlvalRobotik AG` — partial — gold is substring of pred: `TalAlvalRobotik AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ignaz Jungmichel`(person)
- `TalAlvalRobotik AG`(organisation)
- `Delila Leiteritz`(person)

**Example 18** (doc_id: `deanon_TRAIN/10Ob2_22z`) (sent_id: `deanon_TRAIN/10Ob2_22z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Hofrat Mag. Ziegelbauer, die Hofrätin Dr. Faber und die Hofräte Mag. Schober und Dr. Thunhart als weitere Richter in der Rechtssache der klagenden Partei Calvin Amorelli, vertreten durch Dr. Martin Hembach, Rechtsanwalt in Wiener Neustadt, gegen die beklagte Partei Strathewerd u. Niemetz Metall GmbH, Dolores Chatzakis, vertreten durch Mag. Martin Trapichler, Rechtsanwalt in Wien, wegen 13.639,20 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 25. Oktober 2021, GZ 18 R 67/21p-16, mit dem das Urteil des Bezirksgerichts Wiener Neustadt vom 7. Juni 2021, GZ 7 C 117/21b-12, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Martin Hembach` — no gold match — likely missing annotation
- `Mag. Martin Trapichler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Calvin Amorelli`(person)
- `Strathewerd u. Niemetz Metall GmbH`(organisation)
- `Dolores Chatzakis`(person)

**Example 19** (doc_id: `deanon_TRAIN/10Ob3_12g`) (sent_id: `deanon_TRAIN/10Ob3_12g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Rechtssache der klagenden Partei Helge Monhemius, Bakk. techn., vertreten durch Dr. Georg Gorton und DDr. Birgit Gorton, Rechtsanwälte in Klagenfurt, gegen die beklagte Partei Ing. Eugenia Welze, vertreten durch Dr. Gottfried Kassin, Rechtsanwalt in St. Veit an der Glan, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 26. Mai 2011, GZ 2 R 83/11z-49, mit dem das Urteil des Bezirksgerichts St. Veit an der Glan vom 29. Oktober 2010, GZ 3 C 333/09h-34, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Georg Gorton und DDr. Birgit Gorton` — no gold match — likely missing annotation
- `Dr. Gottfried Kassin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Helge Monhemius, Bakk. techn.`(person)
- `Ing. Eugenia Welze`(person)

**Example 20** (doc_id: `deanon_TRAIN/10Ob41_14y`) (sent_id: `deanon_TRAIN/10Ob41_14y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in den verbundenen Familienrechtssachen des Antragstellers DI Dr. Jakob Krägeloh, geboren am 9. Juli 2019, vertreten durch Mag. Werner Thurner, Rechtsanwalt in Graz, gegen die Antragsgegnerinnen 1.

**False Positives:**

- `Mag. Werner Thurner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Jakob Krägeloh`(person)
- `9. Juli 2019`(date)

**Example 21** (doc_id: `deanon_TRAIN/10Ob57_13z`) (sent_id: `deanon_TRAIN/10Ob57_13z_3`)


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

**Example 22** (doc_id: `deanon_TRAIN/10Ob64_19p`) (sent_id: `deanon_TRAIN/10Ob64_19p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei Dr. Marlon Richel, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei Freimut & Assenov Sicherheit GmbH in Liqu, Spazgasse 41, 8524 Greim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 31.596,47 EUR und Feststellung (6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 18. Juni 2019, GZ 129 R 50/19z-21, mit dem das Urteil des Handelsgerichts Wien vom 28. März 2019, GZ 54 Cg 71/18x-17, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Vogl Rechtsanwalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Marlon Richel`(person)
- `Freimut & Assenov Sicherheit GmbH`(organisation)
- `Spazgasse 41, 8524 Greim, Österreich`(address)
- `Eckert Rechtsanwalts GmbH`(organisation)

**Example 23** (doc_id: `deanon_TRAIN/10Ob69_19y`) (sent_id: `deanon_TRAIN/10Ob69_19y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Rechtssache der klagenden Partei DI Daniel Wiegand, vertreten durch Vogl Rechtsanwalt GmbH in Feldkirch, gegen die beklagte Partei West-Medien Manufaktur GmbH in Liqu, Kanzelweg 32, 4850 Oberthalheim, Österreich, vertreten durch Wess Kux Kispert & Eckert Rechtsanwalts GmbH in Wien, wegen 21.231,42 EUR sA und Feststellung (Streitwert: 6.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. August 2019, GZ 5 R 49/19s-17, mit dem das Urteil des Handelsgerichts Wien vom 21. Februar 2019, GZ 52 Cg 43/18i-13, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Vogl Rechtsanwalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `DI Daniel Wiegand`(person)
- `West-Medien Manufaktur GmbH`(organisation)
- `Kanzelweg 32, 4850 Oberthalheim, Österreich`(address)
- `Eckert Rechtsanwalts GmbH`(organisation)

**Example 24** (doc_id: `deanon_TRAIN/10ObS150_17g`) (sent_id: `deanon_TRAIN/10ObS150_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Senatspräsidenten Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Ing. Christian Stangl-Brachnik, MA BA und Mag. Claudia Gründel (beide aus dem Kreis der Arbeitgeber) als weitere Richter in der Sozialrechtssache der klagenden Partei OStR Esra Jakubait, vertreten durch Dr. Thomas Stampfer und Dr. Christoph Orgler, Rechtsanwälte in Graz, gegen die beklagte Partei Sozialversicherungsanstalt der Bauern, 1031 Wien, Ghegastraße 1, vertreten durch Dr. Michael Stögerer, Rechtsanwalt in Wien, wegen Ausgleichszulage, infolge Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 20. September 2017, GZ 7 Rs 37/17s-11, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 27. April 2017, GZ 43 Cgs 113/17p-7, teils bestätigt und teils abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Thomas Stampfer und Dr. Christoph Orgler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OStR Esra Jakubait`(person)
- `Arbeits- und Sozialgericht`(organisation)

**Example 25** (doc_id: `deanon_TRAIN/17Ob10_20z`) (sent_id: `deanon_TRAIN/17Ob10_20z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Dr. Musger, die Hofrätinnen Mag. Malesich und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Levi Adelwart, vertreten durch Stephan Briem Rechtsanwalt GmbH in Wien, gegen die beklagte Partei Dr. Penelope Piephans als Treuhänder der Insolvenzgläubiger der Valkraftfen-Analyse Aktiengesellschaft, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH in Linz, wegen Feststellung (Streitwert 18.335,66 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. März 2020, GZ 1 R 31/20i-13, womit das Urteil des Landesgerichts Linz vom 9. Dezember 2019, GZ 4 Cg 73/18z-8, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Stephan Briem Rechtsanwalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Levi Adelwart`(person)
- `Dr. Penelope Piephans`(person)
- `Valkraftfen-Analyse Aktiengesellschaft`(organisation)

**Example 26** (doc_id: `deanon_TRAIN/18ONc1_21y`) (sent_id: `deanon_TRAIN/18ONc1_21y_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Senatspräsidenten Dr. Veith, die Hofräte Hon.-Prof. Dr. Höllwerth, Hon.-Prof. PD Dr. Rassi und Mag. Painsi als weitere Richter in der Schiedsrechtssache der Antragstellerin (schiedsbeklagte Partei) See-Versand Werke GmbH, Robert Leis, gegen die Antragsgegnerin (schiedsklagende Partei) Dargatz+Boedewig Telekom GmbH, ÖkR Nikolaus Buksbaum, vertreten durch Dr. Horst Pechar, Rechtsanwalt in Weiz, wegen § 602 ZPO, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der an den Obersten Gerichtshof gerichtete Antrag vom 7. 1. 2021 wird, soweit er sich an den Obersten Gerichtshof richtet, zurückgewiesen.

**False Positives:**

- `Dr. Horst Pechar` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `See-Versand Werke GmbH`(organisation)
- `Robert Leis`(person)
- `Dargatz+Boedewig Telekom GmbH`(organisation)
- `ÖkR Nikolaus Buksbaum`(person)

**Example 27** (doc_id: `deanon_TRAIN/1Nc1_15k`) (sent_id: `deanon_TRAIN/1Nc1_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski und Mag. Wurzer als weitere Richter in der beim Landesgericht Wiener Neustadt zu AZ 56 Cg 36/14s anhängigen Rechtssache der klagenden Partei Herbes&Vißers Heizung GmbH, Waldemar Lokämper, vertreten durch Dr. Andreas Oberbichler und Dr. Michael Kramer, Rechtsanwälte in Feldkirch, gegen die beklagte Partei Traun-Luftfahrt GmbH, VetR DDr. Walter Stuehrmann, vertreten durch Mag. Maximilian Kocher, Rechtsanwalt in Brunn am Gebirge, wegen 36.000 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der vorliegenden Rechtssache wird das Landesgericht Feldkirch als zuständig bestimmt.

**False Positives:**

- `Dr. Andreas Oberbichler und Dr. Michael Kramer` — no gold match — likely missing annotation
- `Mag. Maximilian Kocher` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Landesgericht Wiener Neustadt`(organisation)
- `Herbes&Vißers Heizung GmbH`(organisation)
- `Waldemar Lokämper`(person)
- `Traun-Luftfahrt GmbH`(organisation)
- `VetR DDr. Walter Stuehrmann`(person)
- `Landesgericht Feldkirch`(organisation)

**Example 28** (doc_id: `deanon_TRAIN/1Nc2_20i`) (sent_id: `deanon_TRAIN/1Nc2_20i_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie den Hofrat Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei KommR Franz Kubank, vertreten durch Dr. Michael Wukoschitz, Rechtsanwalt in Wien, gegen die beklagte Partei Laurin Aichhorn a.d., Timothy Schulmeister, Serbien, wegen 600 EUR sA, über den Ordinationsantrag nach § 28 JN den Beschluss gefasst:  Spruch Als örtlich zuständiges Gericht wird das Bezirksgericht Schwechat bestimmt.

**False Positives:**

- `Dr. Michael Wukoschitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `KommR Franz Kubank`(person)
- `Laurin Aichhorn`(person)
- `Timothy Schulmeister`(person)
- `Bezirksgericht Schwechat`(organisation)

**Example 29** (doc_id: `deanon_TRAIN/1Ob103_17d`) (sent_id: `deanon_TRAIN/1Ob103_17d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Laura Overbeeke, BA, vertreten durch Dr. Gerhard Ebenbichler, Rechtsanwalt in Wien, gegen die beklagten Parteien 1. Janis Marxmeyer, und 2.

**False Positives:**

- `Dr. Gerhard Ebenbichler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Laura Overbeeke, BA`(person)
- `Janis Marxmeyer`(person)

**Example 30** (doc_id: `deanon_TRAIN/1Ob103_17d`) (sent_id: `deanon_TRAIN/1Ob103_17d_4`)


Chantal Maxein, vertreten durch Dr. Eric Agstner, Rechtsanwalt in Wien, wegen Unterlassung, Zahlung, Feststellung und Beseitigung, über die Revision der beklagten Parteien gegen das Teilurteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 27. Februar 2017, GZ 58 R 128/16w-38a, in der Fassung des Berichtigungsbeschlusses vom 29. März 2017, GZ 58 R 128/16w-40, mit dem das Urteil des Bezirksgerichts Neunkirchen vom 18. November 2016, GZ 23 C 249/16x-33, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Eric Agstner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Chantal Maxein`(person)

**Example 31** (doc_id: `deanon_TRAIN/1Ob127_14d`) (sent_id: `deanon_TRAIN/1Ob127_14d_4`)


Republik Österreich, vertreten durch die Finanzprokuratur in Wien, 2. Dr. Ralph Kreidenweiß, und 3. Donau-Automotive GmbH, Ebersreith 11, 8761 Götzendorf, Österreich, beide vertreten durch Dr. Hubert Simon, Rechtsanwalt in Wien, wegen Leistung und Feststellung, über den Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Graz als Rekursgericht vom 28. April 2014, GZ 7 R 21/14h-7, mit dem der Beschluss des Landesgerichts Leoben vom 30. Jänner 2014, GZ 2 Nc 2/14y-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Dr. Hubert Simon` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Ralph Kreidenweiß`(person)
- `Donau-Automotive GmbH`(organisation)
- `Ebersreith 11, 8761 Götzendorf, Österreich`(address)

**Example 32** (doc_id: `deanon_TRAIN/1Ob139_18z`) (sent_id: `deanon_TRAIN/1Ob139_18z_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Angelina Töpker Inc., Ronja Straßgschwandtner, vertreten durch Mag. Ralph Kilches, Rechtsanwalt in Wien, gegen die beklagte Partei Mag. Lilia Anderßon, als Insolvenzverwalter im Insolvenzverfahren über das Vermögen der Vanek und Eloy Analyse GmbH, Kanischaberg 21, 4742 Kornrödt, Österreich, vertreten durch die Haslinger/Nagele & Partner Rechtsanwälte GmbH, Linz, wegen Feststellung einer Insolvenzforderung (Streitwert 447.352,05 EUR), über den außerordentlichen Revisionsrekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 28. Juni 2018, GZ 1 R 83/18h-8, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mag. Ralph Kilches` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Angelina Töpker`(person)
- `Ronja Straßgschwandtner`(person)
- `Mag. Lilia Anderßon`(person)
- `Vanek und Eloy Analyse GmbH`(organisation)
- `Kanischaberg 21, 4742 Kornrödt, Österreich`(address)
- `Haslinger/Nagele & Partner Rechtsanwälte GmbH`(organisation)

**Example 33** (doc_id: `deanon_TRAIN/1Ob14_20w`) (sent_id: `deanon_TRAIN/1Ob14_20w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei VetR Amber Baraniak, Hong Kong, vertreten durch die Oblin Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Mag. Liliana Bößer, vertreten durch Dr. Karl Heinz Kramer M.A.S., Rechtsanwalt in Villach, wegen Aufhebung eines Kaufvertrags, 213.819,01 USD sA und 9.950,39 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 30. Oktober 2019, GZ 5 R 94/19m-210, mit dem das Urteil des Landesgerichts Klagenfurt vom 2. April 2019, GZ 25 Cg 122/12y-207, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Karl Heinz Kramer M.A.S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `VetR Amber Baraniak`(person)
- `Mag. Liliana Bößer`(person)

**Example 34** (doc_id: `deanon_TRAIN/1Ob160_12d`) (sent_id: `deanon_TRAIN/1Ob160_12d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der außerstreitigen Rechtssache der Antragstellerin Svenja Meierarnd, vertreten durch Dr. Karl-Peter Hasch, Rechtsanwalt in Villach, gegen den Antragsgegner Othmar Eidenmueller, vertreten durch Mag. Hanno Stromberger, Rechtsanwalt in Villach, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse über den Revisionsrekurs der Antragstellerin gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 31. Mai 2012, GZ 2 R 85/12w-11, mit dem der Beschluss des Bezirksgerichts Villach vom 13. März 2012, GZ 38 Fam 98/11s-7, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Mag. Hanno Stromberger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Svenja Meierarnd`(person)
- `Othmar Eidenmueller`(person)

**Example 35** (doc_id: `deanon_TRAIN/1Ob163_21h`) (sent_id: `deanon_TRAIN/1Ob163_21h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Manfred Nordkamp, vertreten durch Mag. Dieter Koch und Mag. Natascha Jilek, Rechtsanwälte in Bruck an der Mur, gegen die beklagte Partei Belohlawek KI Bank AG, Denis Nakonzer, vertreten durch Mag. Martina Hosp ua, Rechtsanwälte in Salzburg, wegen Feststellung (Streitwert 103.488,18 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 21. Juni 2021, GZ 2 R 70/21h-19, mit dem das Urteil des Landesgerichts Salzburg vom 12. März 2021, GZ 10 Cg 52/20k-15, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mag. Dieter Koch und Mag. Natascha Jilek` — no gold match — likely missing annotation
- `Mag. Martina Hosp ua` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Manfred Nordkamp`(person)
- `Belohlawek KI`(organisation)
- `Denis Nakonzer`(person)

**Example 36** (doc_id: `deanon_TRAIN/1Ob177_24x`) (sent_id: `deanon_TRAIN/1Ob177_24x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Dr. Wurdinger als Vorsitzenden sowie die Hofrätinnen und Hofräte Dr. Steger, Mag. Wessely-Kristöfel, Dr. Parzmayr und Dr. Pfurtscheller als weitere Richterinnen und Richter in der Rechtssache der klagenden Partei Bundeskammer für Arbeiter und Angestellte, Wien 4, Prinz-Eugen-Straße 20–22, vertreten durch Dr. Walter Reichholf, Rechtsanwalt in Wien, gegen die beklagte Partei Alsynwald-Recycling AG, RgR Mag. Dr. Evelyn Steinkröger, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH in Wien, wegen Unterlassung und Urteilsveröffentlichung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. Juli 2024, GZ 2 R 77/24v-15, mit dem das Urteil des Handelsgerichts Wien vom 28. Februar 2024, GZ 57 Cg 36/23d-8, bestätigt wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Walter Reichholf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Alsynwald-Recycling AG`(organisation)
- `RgR Mag. Dr. Evelyn Steinkröger`(person)

**Example 37** (doc_id: `deanon_TRAIN/1Ob179_12y`) (sent_id: `deanon_TRAIN/1Ob179_12y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Pflegschaftssache des mj Roy Boner, geboren am 13. Juli 2006, vertreten durch Mag. Heinz Wolfbauer, Rechtsanwalt in Wien, wegen Unterhalts, über den Revisionsrekurs des Vaters Dr. Jaroslaw Kellenbrink, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 29. Mai 2012, GZ 43 R 254/12i-106, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Döbling vom 28. März 2012, GZ 10 Pu 131/09b-100, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Mag. Heinz Wolfbauer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Roy Boner`(person)
- `Dr. Jaroslaw Kellenbrink`(person)

**Example 38** (doc_id: `deanon_TRAIN/1Ob182_17x`) (sent_id: `deanon_TRAIN/1Ob182_17x_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Mag. Wurzer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Dr. Wurdinger, und die Hofrätinnen Dr. Hofer-Zeni-Rennhofer und Dr. Kodek in der Rechtssache der gefährdeten Partei Prof. Virgil Pahlow, vertreten durch die Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG, Wien, gegen die gefährdete Partei Dominika Föcks, vertreten durch Dr. Alexander Haas, Rechtsanwalt in Seiersberg-Pirka, wegen Erlassung einer einstweiligen Verfügung nach § 382 Z 8 lit c zweiter Fall EO, über den außerordentlichen Revisionsrekurs der gefährdeten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 11. September 2017, GZ 1 R 213/17a-221, mit dem der Beschluss des Bezirksgerichts Fürstenfeld vom 25. Juli 2017, GZ 23 Fam 27/15p-207, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Dr. Alexander Haas` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Prof. Virgil Pahlow`(person)
- `Dominika Föcks`(person)

**Example 39** (doc_id: `deanon_TRAIN/1Ob184_15p`) (sent_id: `deanon_TRAIN/1Ob184_15p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tamara Schweinfurth, vertreten durch Dr. Wolfgang Maurer, Rechtsanwalt in Golling, gegen die beklagte Partei Noah Vlatten, BEd, vertreten durch Dr. Peter Perner, Rechtsanwalt in Salzburg, wegen 10.895,18 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 19. Mai 2015, GZ 22 R 126/15f-21, mit dem das Urteil des Bezirksgerichts Salzburg vom 5. März 2015, GZ 32 C 407/14x-17, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Wolfgang Maurer` — no gold match — likely missing annotation
- `Dr. Peter Perner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Tamara Schweinfurth`(person)
- `Noah Vlatten, BEd`(person)

**Example 40** (doc_id: `deanon_TRAIN/1Ob186_12b`) (sent_id: `deanon_TRAIN/1Ob186_12b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei Thomas Pasqualini, vertreten durch Kammler & Koll Rechtsanwälte OG in Freistadt, gegen die beklagte Partei Patrick Denzlein, vertreten durch Mag. Klaus Burgholzer, Rechtsanwalt in Linz, wegen 100.000 EUR sA und Feststellung (Streitwert: 5.000 EUR), über die außerordentliche Revision der klagenden Partei (Revisionsinteresse: 70.000 EUR sA) gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. Juli 2012, GZ 2 R 79/12v-22, mit dem das Urteil des Landesgerichts Linz vom 27. Februar 2012, GZ 5 Cg 61/11d-18, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Mag. Klaus Burgholzer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Pasqualini`(person)
- `Denzlein`(person)

**Example 41** (doc_id: `deanon_TRAIN/1Ob186_16h`) (sent_id: `deanon_TRAIN/1Ob186_16h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Anton Luehne, Deutschland, vertreten durch die Dr. Paul Kreuzberger, Mag. Markus Stranimaier & Mag. Manuel Vogler – Rechtsanwälte & Strafverteidiger OG, Bischofshofen, gegen die beklagten Parteien 1. OMedR Angelina Badenius und 2. Hon.-Prof. Miroslav Roelle, vertreten durch Dr. Raimund Danner, Rechtsanwalt in Salzburg, wegen 18.383,81 EUR sA und Feststellung (Streitwert 5.000 EUR), über die Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 11. August 2016, GZ 4 R 107/16g-45, mit dem das Teilzwischenurteil des Landesgerichts Salzburg vom 8. Juni 2016, GZ 5 Cg 125/14z-41, mit einer Maßgabe bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Raimund Danner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Anton Luehne`(person)
- `OMedR Angelina Badenius`(person)
- `Hon.-Prof. Miroslav Roelle`(person)

**Example 42** (doc_id: `deanon_TRAIN/1Ob187_14b`) (sent_id: `deanon_TRAIN/1Ob187_14b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der außerstreitigen Rechtssache der Antragstellerin Juliana Enssle, vertreten durch Dr. Albert Heiss, Rechtsanwalt in Innsbruck, gegen den Antragsgegner PhD MedR Oskar Sträßer, vertreten durch Dr. Christian Fuchs Rechtsanwalt GmbH, Innsbruck, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse nach den §§ 81 ff EheG, über die außerordentlichen Revisionsrekurse beider Parteien gegen den Beschluss des Landesgerichts Innsbruck als Rekursgericht vom 30. Mai 2014, GZ 52 R 76/13b-174, womit dem Rekurs des Antragsgegners nicht Folge gegeben und über Rekurs der Antragstellerin der Beschluss des Bezirksgerichts Innsbruck vom 30. November 2012, GZ 1 C 8/07f-163, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Der Beschluss vom 19. März 2015 wird dahin berichtigt, dass es im zweiten Absatz des Spruchs „Dem außerordentlichen Revisionsrekurs des Antragsgegners [anstelle von Antragstellers] wird teilweise Folge gegeben“ und auf Seite 5 der Begründung „Das Erstgericht verpflichtete […] den Antragsgegner zur Leistung […] lautet.

**False Positives:**

- `Dr. Albert Heiss` — no gold match — likely missing annotation
- `Dr. Christian Fuchs Rechtsanwalt` — positional overlap with gold: `Christian Fuchs Rechtsanwalt GmbH`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Juliana Enssle`(person)
- `PhD MedR Oskar Sträßer`(person)
- `Christian Fuchs Rechtsanwalt GmbH`(organisation)

**Example 43** (doc_id: `deanon_TRAIN/1Ob205_10v`) (sent_id: `deanon_TRAIN/1Ob205_10v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Dr. E. Solé und Mag. Wurzer als weitere Richter in der Rechtssache des Antragstellers Hans Päulgen, vertreten durch Mag. Matthias Kucera, Rechtsanwalt in Hard, gegen die Antragsgegnerin Herta Polaschegg, vertreten durch Dr. Wolf Heistinger, Rechtsanwalt in Mödling, wegen Anerkennung eines ausländischen Scheidungsurteils, über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 13. Oktober 2010, GZ 16 R 384/10z-11, mit dem der Beschluss des Bezirksgerichts Mödling vom 1. September 2010, GZ 13 Nc 14/10w-5, bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

**False Positives:**

- `Mag. Matthias Kucera` — no gold match — likely missing annotation
- `Dr. Wolf Heistinger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Päulgen`(person)
- `Polaschegg`(person)
- `Bezirksgerichts Mödling`(organisation)

**Example 44** (doc_id: `deanon_TRAIN/1Ob221_17g`) (sent_id: `deanon_TRAIN/1Ob221_17g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und Hofrätinnen Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Mag. Korn als weitere Richter in der Rechtssache der klagenden Partei Boothe u. Sandmeier IT GmbH (früher OberTelekom GmbH), Ewaldgasse 28, 4084 Mitterberg, Österreich, vormals vertreten durch Dr. Wolfgang Poleschinski, Rechtsanwalt in Hartberg, gegen die beklagte Partei Yelec Dangelmeier, vertreten durch die Dr. Farhad Paya Rechtsanwalt GmbH, Klagenfurt am Wörthersee, wegen 7.583,60 EUR sA, infolge Revision der beklagten Partei gegen das Urteil des Landesgerichts Klagenfurt als Berufungsgericht vom 24. August 2017, GZ 1 R 127/17x-69, mit dem das Urteil des Bezirksgerichts Klagenfurt vom 28. März 2017, GZ 16 C 1333/14i-65, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

**False Positives:**

- `Dr. Wolfgang Poleschinski` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Boothe u. Sandmeier IT GmbH`(organisation)
- `OberTelekom GmbH`(organisation)
- `Ewaldgasse 28, 4084 Mitterberg, Österreich`(address)
- `Yelec Dangelmeier`(person)
- `Farhad Paya Rechtsanwalt GmbH`(organisation)

**Example 45** (doc_id: `deanon_TRAIN/1Ob22_24b`) (sent_id: `deanon_TRAIN/1Ob22_24b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Musger als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der gefährdeten Partei Ida Theocharaki, vertreten durch Mag. Stefan Hotz, Rechtsanwalt in Wien, gegen den Gegner der gefährdeten Partei Mag. Bianca Orzegowski, vertreten durch Dr. Kristina Venturini, Rechtsanwältin in Wien, wegen Ehescheidung, hier wegen vorläufigen Unterhalts, über den außerordentlichen Revisionsrekurs der gefährdeten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 13. Dezember 2023, GZ 44 R 314/23m-203, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionrekurs wird mangels der Voraussetzungen des § 528 Abs 1 ZPO (iVm §§ 78, 402 Abs 4 EO) zurückgewiesen.

**False Positives:**

- `Mag. Stefan Hotz` — no gold match — likely missing annotation
- `Dr. Kristina Venturini` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Ida Theocharaki`(person)
- `Mag. Bianca Orzegowski`(person)

**Example 46** (doc_id: `deanon_TRAIN/1Ob234_19x`) (sent_id: `deanon_TRAIN/1Ob234_19x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr in der Rechtssache der gefährdeten Partei VetR RgR Janet Wichtler, vertreten durch die Dr. Helene Klaar Dr. Norbert Marschall Rechtsanwälte OG, Wien, gegen die gefährdende Partei Charles Gutbrot, vertreten durch Dr. Alexander Haas, Rechtsanwalt in Seiersberg, wegen Erlassung einer einstweiligen Verfügung nach § 382 Z 8 lit c zweiter Fall EO, über den außerordentlichen Revisionsrekurs der gefährdenden Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 5. November 2019, GZ 1 R 191/19v-326, mit dem der Beschluss des Bezirksgerichts Fürstenfeld vom 24. Juli 2019, GZ 23 Fam 27/15p-297, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß den §§ 402 Abs 4, 78 EO iVm § 526 Abs 2 erster Satz ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Alexander Haas` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `VetR RgR Janet Wichtler`(person)
- `Charles Gutbrot`(person)

**Example 47** (doc_id: `deanon_TRAIN/1Ob26_20k`) (sent_id: `deanon_TRAIN/1Ob26_20k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Synsynfurt-Finanzen GmbH, Tanja Thielike, vertreten durch die Draxler Rexeis Sozietät von Rechtsanwälten OG, Graz, gegen die beklagte Partei Roberta Reumschüssel, Bakk. phil., vertreten durch Mag. Dr. Alfred Wansch, Rechtsanwalt in Wien, wegen Räumung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtsachen Wien als Berufungsgericht vom 13. November 2019, GZ 39 R 228/19x-70, mit dem das Urteil des Bezirksgerichts Hernals vom 30. April 2019, GZ 4 C 277/16f-64, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mag. Dr. Alfred Wansch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Synsynfurt-Finanzen GmbH`(organisation)
- `Tanja Thielike`(person)
- `Roberta Reumschüssel, Bakk. phil.`(person)

**Example 48** (doc_id: `deanon_TRAIN/1Ob35_21k`) (sent_id: `deanon_TRAIN/1Ob35_21k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Familienrechtssache des Antragstellers DI Sandra Foglar, vertreten durch Dr. Walter Mardetschläger und andere Rechtsanwälte in Wien, gegen die Antragsgegnerin Mag. Christine Scherfling, vertreten durch Mag. Sonja Fragner, Rechtsanwältin in Krems, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts Krems an der Donau als Rekursgericht vom 28. Jänner 2021, GZ 2 R 91/20z-49, mit dem der Beschluss des Bezirksgerichts Krems an der Donau vom 29. Juli 2020, GZ 7 Fam 10/18a-43, mit einer Maßgabe bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Mag. Sonja Fragner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `DI Sandra Foglar`(person)
- `Mag. Christine Scherfling`(person)

**Example 49** (doc_id: `deanon_TRAIN/1Ob51_11y`) (sent_id: `deanon_TRAIN/1Ob51_11y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei mj Kurt Schwenckel, vertreten durch Mag. Erich Frenner, Rechtsanwalt in Saalfelden, gegen die beklagte Partei Condon Planung GmbH, Corvin Heidtmeyer, vertreten durch Dr. Harald Schwendinger und Dr. Brigitte Piber Rechtsanwälte in Salzburg, wegen 5.100 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 30. Dezember 2010, GZ 53 R 273/10v-12, mit dem über die Berufung der beklagten Partei das Zwischenurteil des Bezirksgerichts Saalfelden vom 23. Juni 2010, GZ 2 C 454/10z-7, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Mag. Erich Frenner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Kurt Schwenckel`(person)
- `Condon Planung GmbH`(organisation)
- `Corvin Heidtmeyer`(person)

**Example 50** (doc_id: `deanon_TRAIN/1Ob55_13i`) (sent_id: `deanon_TRAIN/1Ob55_13i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Pflegschaftssache des mj Kevin Hüpgen, geboren am 5. November 2000, vertreten durch die Mutter Bernarda Albold, vertreten durch Mag. Herbert Premur, Rechtsanwalt in Klagenfurt, wegen pflegschaftsgerichtlicher Genehmigung einer Klage, über den außerordentlichen Revisionsrekurs des Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 12. Februar 2013, GZ 44 R 61/13s-101, mit dem der Beschluss des Bezirksgerichts Döbling vom 6. Dezember 2012, GZ 2 Ps 94/11f-98, bestätigt wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Mag. Herbert Premur` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Kevin Hüpgen`(person)
- `5. November`(date)
- `Bernarda Albold`(person)

**Example 51** (doc_id: `deanon_TRAIN/1Ob56_21y`) (sent_id: `deanon_TRAIN/1Ob56_21y_4`)


Ali Haarnacke und 2. Li Baselt, vertreten durch Dr. Serpil Dogan, Rechtsanwältin in Feldkirch, gegen die beklagte Partei Republik Österreich (Bund), vertreten durch die Finanzprokuratur in Wien, und den Nebenintervenienten auf Seite der beklagten Partei KzlR Florian Schlimm, vertreten durch Dr. Bertram Grass und Mag. Christoph Dorner, Rechtsanwälte in Bregenz, wegen 60.300 EUR sA und Feststellung (Erstklägerin) und 66.300 EUR sA und Feststellung (Zweitkläger), über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 27. Jänner 2021, GZ 4 R 171/20h-41, mit dem das Urteil des Landesgerichts Feldkirch vom 2. Oktober 2020, GZ 4 Cg 14/19k-35, bestätigt wurde, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Serpil Dogan` — no gold match — likely missing annotation
- `Dr. Bertram Grass und Mag. Christoph Dorner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Ali Haarnacke`(person)
- `Li Baselt`(person)
- `KzlR Florian Schlimm`(person)

**Example 52** (doc_id: `deanon_TRAIN/1Ob57_16p`) (sent_id: `deanon_TRAIN/1Ob57_16p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der außerstreitigen Familienrechtssache der Antragstellerin und gefährdeten Partei Tatjana Skowroneck, vertreten durch Mag. Nikolaus Vasak, Rechtsanwalt in Wien, gegen den Antragsgegner und Gegner der gefährdeten Partei Emmerich Smolin, vertreten durch Dr. Josef Lindlbauer, Rechtsanwalt in Enns, wegen (einstweiligen) Unterhalts, über den Revisionsrekurs des Antragsgegners gegen den Beschluss des Landesgerichts Wiener Neustadt als Rekursgericht vom 17. September 2015, GZ 16 R 271/15i-77, mit dem der Beschluss des Bezirksgerichts Mödling vom 29. Juni 2015, GZ 2 Fam 68/14f-58, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Mag. Nikolaus Vasak` — no gold match — likely missing annotation
- `Dr. Josef Lindlbauer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Tatjana Skowroneck`(person)
- `Emmerich Smolin`(person)
- `Bezirksgerichts Mödling`(organisation)

**Example 53** (doc_id: `deanon_TRAIN/1Ob60_22p`) (sent_id: `deanon_TRAIN/1Ob60_22p_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Pflegschaftssache des mj Dorothea Sachtleber, geboren am 8. März 2011, über den außerordentlichen Revisionsrekurs der Mutter Scarlett Jähnel, vertreten durch Mag. Elisabeth Mace, Rechtsanwältin in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 11. Jänner 2022, GZ 48 R 263/21p-80, mit dem der Beschluss des Bezirksgerichts Floridsdorf vom 25. Oktober 2021, GZ 1 Ps 110/18i-71, bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

**False Positives:**

- `Mag. Elisabeth Mace` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dorothea Sachtleber`(person)
- `8. März`(date)
- `Scarlett Jähnel`(person)

**Example 54** (doc_id: `deanon_TRAIN/1Ob78_22k`) (sent_id: `deanon_TRAIN/1Ob78_22k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. HR Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Familienrechtssache des Antragstellers Dr. Mehmet Herschlein, vertreten durch den Erwachsenenvertreter Dr. Dagobert Hammer, Rechtsanwalt in Wien, gegen die Antragsgegnerin Lucia Ignatzy, vertreten durch Dr. Karl Newole, Rechtsanwalt in Wien, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den außerordentlichen Revisionsrekurs des Antragstellers gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 21. Dezember 2021, GZ 44 R 449/21m-15, mit dem der Beschluss des Bezirksgerichts Josefstadt vom 29. November 2021, GZ 25 Fam 3/21k-10, bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

**False Positives:**

- `Dr. Karl Newole` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Mehmet Herschlein`(person)
- `Dr. Dagobert Hammer`(person)
- `Lucia Ignatzy`(person)

**Example 55** (doc_id: `deanon_TRAIN/1Ob7_11b`) (sent_id: `deanon_TRAIN/1Ob7_11b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache des Antragstellers Ing. Jörg Wesemeyer, vertreten durch Dr. Christian Widl, Rechtsanwalt in Wien, gegen die Antragsgegnerin OSR Fabienne Hudetschek, vertreten durch Dr. Alfred Feitsch, Rechtsanwalt in Wien, wegen Aufteilung des ehelichen Gebrauchsvermögens und der ehelichen Ersparnisse, über den „außerordentlichen“ Revisionsrekurs der Antragsgegnerin gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 8. November 2010, GZ 43 R 466/10p-8, mit dem der Beschluss des Bezirksgerichts Favoriten vom 7. Juli 2010, GZ 6 FAM 49/10v-2, aufgehoben wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Dr. Christian Widl` — no gold match — likely missing annotation
- `Dr. Alfred Feitsch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Ing. Jörg Wesemeyer`(person)
- `OSR Fabienne Hudetschek`(person)

**Example 56** (doc_id: `deanon_TRAIN/1Ob84_13d`) (sent_id: `deanon_TRAIN/1Ob84_13d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Dr. Grohmann, Mag. Wurzer und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der gefährdeten Partei Dr. Miklos Ostheim, vertreten durch Dr. Christoph Brandweiner und Dr. Gabriela Brandweiner-Reiter, Rechtsanwälte in Salzburg, gegen den Gegner der gefährdeten Partei Karim Markel DDr. Maximilian Damrau, vertreten durch Dr. Petra Patzelt, Rechtsanwältin in Salzburg, wegen Erlassung einer einstweiligen Verfügung, über den vom Gegner der gefährdeten Partei gestellten Antrag auf Wiedereinsetzung in den vorigen Stand gegen die Versäumung der Frist zur Erhebung eines außerordentlichen Revisionsrekurses gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 26. März 2013, GZ 21 R 359/12h-16, mit dem der Beschluss des Bezirksgerichts Salzburg vom 8. August 2012, GZ 20 C 11/12w-6, mit einer Maßgabe bestätigt wurde, den Beschluss gefasst:  Spruch Der Wiedereinsetzungsantrag wird zurückgewiesen.

**False Positives:**

- `Dr. Petra Patzelt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Miklos Ostheim`(person)
- `Karim Markel`(person)
- `DDr. Maximilian Damrau`(person)

**Example 57** (doc_id: `deanon_TRAIN/2Nc17_17y`) (sent_id: `deanon_TRAIN/2Nc17_17y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und durch die Hofräte Dr. Veith und Dr. Musger als weitere Richter in der Rechtssache der klagenden Partei Glanzbruckkraft-Recycling -Aktiengesellschaft, Steindläcker 26, 4183 Obertraberg, Österreich, vertreten durch THUM WEINREICH SCHWARZ CHYBA REITER Rechtsanwälte OG in St. Pölten, gegen die beklagte Partei Verband der Versicherungsunternehmen Österreichs, Schwarzenbergplatz 7, 1030 Wien, vertreten durch Mag. Georg E. Thalhammer, Rechtsanwalt in Wien, wegen 11.550 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Innere Stadt Wien das Bezirksgericht Kitzbühel bestimmt.

**False Positives:**

- `Mag. Georg E. Thalhammer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Glanzbruckkraft-Recycling`(organisation)
- `Steindläcker 26, 4183 Obertraberg, Österreich`(address)
- `Bezirksgericht Kitzbühel`(organisation)

**Example 58** (doc_id: `deanon_TRAIN/2Nc24_12w`) (sent_id: `deanon_TRAIN/2Nc24_12w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith und Dr. E. Solé als weitere Richter in der Rechtssache der klagenden Partei Thaddäus Gerzabek, LLM, vertreten durch Dr. Hanspeter Egger, Rechtsanwalt in Wien, gegen die beklagte Partei Pietruszak Recycling -AG, Rainer Chochola, vertreten durch Dr. Norbert Bergmüller, Rechtsanwalt in Schladming, wegen 1.505,25 EUR sA, über den Delegierungsantrag der beklagten Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Bezirksgerichts Hietzing das Bezirksgericht Irdning bestimmt.

**False Positives:**

- `Dr. Hanspeter Egger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Thaddäus Gerzabek, LLM`(person)
- `Pietruszak Recycling`(organisation)
- `Rainer Chochola`(person)
- `Bezirksgericht Irdning`(organisation)

**Example 59** (doc_id: `deanon_TRAIN/2Ob159_18y`) (sent_id: `deanon_TRAIN/2Ob159_18y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden, den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé sowie die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Edgar Arnts, vertreten durch Dr. Heinrich Oppitz, Rechtsanwalt in Wels, wider die beklagten Parteien 1.

**False Positives:**

- `Dr. Heinrich Oppitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Edgar Arnts`(person)

**Example 60** (doc_id: `deanon_TRAIN/2Ob159_18y`) (sent_id: `deanon_TRAIN/2Ob159_18y_4`)


Henriette Daxlberger, 2. Thassilo Debus, und 3. ÖkR Claudia Göttken, alle vertreten durch Dr. Wolfgang Muchitsch, Rechtsanwalt in Graz, wegen 32.086 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 21. Juni 2018, GZ 6 R 21/18b-59, womit infolge Berufung der beklagten Parteien das Urteil des Landesgerichts Wels vom 15. Dezember 2017, GZ 36 Cg 34/16a-55, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

**False Positives:**

- `Dr. Wolfgang Muchitsch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Henriette Daxlberger`(person)
- `Thassilo Debus`(person)
- `ÖkR Claudia Göttken`(person)

**Example 61** (doc_id: `deanon_TRAIN/2Ob175_21f`) (sent_id: `deanon_TRAIN/2Ob175_21f_4`)


Sloboda als weitere Richter in der Rechtssache der klagenden Partei Shoshana Etl, vertreten durch Mag. Axel Bauer, Rechtsanwalt in Wien, gegen die beklagte Partei Manuel van der Willik, vertreten durch Dr. Manfred Sommerbauer ua, Rechtsanwälte in Wiener Neustadt, wegen 44.903,84 EUR sA, über die Revision der beklagten Partei gegen das Zwischenurteil des Oberlandesgerichts Wien als Berufungsgericht vom 17. Juni 2021, GZ 11 R 79/21z-66, womit das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 10. März 2021, GZ 5 Cg 105/19a-50 in der Fassung des Berichtigungsbeschlusses vom 16. März 2021, GZ 5 Cg 105/19a-51, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision der beklagten Partei wird zurückgewiesen.

**False Positives:**

- `Mag. Axel Bauer` — no gold match — likely missing annotation
- `Dr. Manfred Sommerbauer ua` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Shoshana Etl`(person)
- `Manuel van der Willik`(person)

**Example 62** (doc_id: `deanon_TRAIN/2Ob176_25h`) (sent_id: `deanon_TRAIN/2Ob176_25h_4`)


Sloboda, Dr. Thunhart und Dr. Kikinger und die Hofrätin Mag. Fitz als weitere Richterin und weitere Richter in der Rechtssache der klagenden Partei Alva Wittwer, vertreten durch Dr. Friedrich Schulz, Rechtsanwalt in Wien, gegen die beklagte Partei Leopold Eggerichs, vertreten durch Grgic & Partneri Rechtsanwaltsgesellschaft mbH in Wien, wegen zuletzt 31.718 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 6. September 2025, GZ 11 R 40/25w-47, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Friedrich Schulz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Alva Wittwer`(person)
- `Leopold Eggerichs`(person)

**Example 63** (doc_id: `deanon_TRAIN/2Ob177_20y`) (sent_id: `deanon_TRAIN/2Ob177_20y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden und den Hofrat Dr. Musger, die Hofrätin Dr. Solé sowie die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Jörg von Bockel, vertreten durch Mag. Stefan Danzinger, Rechtsanwalt in Wiener Neustadt, gegen die beklagte Partei Gareise Energie AG, Ada Krol, vertreten durch Grgić & Partneri Rechtsanwaltsgesellschaft mbH, Zweigniederlassung Wien, wegen 11.266,39 EUR sA, über die Revision der beklagten Partei (Revisionsinteresse: 6.646,20 EUR) gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 17. Juli 2020, GZ 18 R 38/20x-32, womit infolge Berufung der beklagten Partei das Urteil des Bezirksgerichts Wiener Neustadt vom 31. Jänner 2020, GZ 14 C 1015/18h-27, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Mag. Stefan Danzinger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jörg von Bockel`(person)
- `Gareise Energie AG`(organisation)
- `Ada Krol`(person)

**Example 64** (doc_id: `deanon_TRAIN/2Ob178_18t`) (sent_id: `deanon_TRAIN/2Ob178_18t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Veith als Vorsitzenden, den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé sowie die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Garttri Sicherheit -GesmbH, Alpendorfsiedlung 14, 4209 Linzerberg, Österreich, vertreten durch Dr. Bernhard Birek, Rechtsanwalt in Schlüßlberg, wider die beklagte Partei Vogelsanger Marine GmbH, Juri Büttgens, vertreten durch Mag. Dr. Dirk Just, Rechtsanwalt in Wien, wegen (restlich) 30.000 EUR sA, über die „außerordentliche Revision“ der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Juli 2018, GZ 4 R 79/18v-157, mit welchem das Endurteil des Handelsgerichts Wien vom 9. April 2018, GZ 40 Cg 12/11g-153, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

**False Positives:**

- `Dr. Bernhard Birek` — no gold match — likely missing annotation
- `Mag. Dr. Dirk Just` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Garttri Sicherheit`(organisation)
- `Alpendorfsiedlung 14, 4209 Linzerberg, Österreich`(address)
- `Vogelsanger Marine GmbH`(organisation)
- `Juri Büttgens`(person)

**Example 65** (doc_id: `deanon_TRAIN/2Ob179_15k`) (sent_id: `deanon_TRAIN/2Ob179_15k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden, die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé sowie den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Franz Wagenschwanz, vertreten durch Dr. Klaus Estl, Rechtsanwalt in Salzburg, gegen die beklagten Parteien 1. Hartmut Willekes, und 2. KommR Roswitha Allgoewer, vertreten durch Dr. Roland Reichl, Rechtsanwalt in Salzburg, wegen 10.000 EUR sA und Feststellung (Streitinteresse 5.000 EUR), über den Rekurs der zweitbeklagten Partei gegen den Beschluss des Landesgerichts Salzburg als Berufungsgericht vom 22. Juli 2015, GZ 22 R 169/15d-52, womit infolge Berufung der klagenden Partei das Urteil des Bezirksgerichts Salzburg vom 2. April 2015, GZ 32 C 896/12f-47, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Dr. Klaus Estl` — no gold match — likely missing annotation
- `Dr. Roland Reichl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Franz Wagenschwanz`(person)
- `Hartmut Willekes`(person)
- `KommR Roswitha Allgoewer`(person)

**Example 66** (doc_id: `deanon_TRAIN/2Ob180_21s`) (sent_id: `deanon_TRAIN/2Ob180_21s_4`)


Sloboda als weitere Richter in der Rechtssache der klagenden Partei Ing. Constanze Kronawitt, vertreten durch Dr. Alexander Bosio, Rechtsanwalt in Zell am See, gegen die beklagten Parteien 1. DDr. Leif Eralp, und 2. Lothar Schwänke, beide vertreten durch Kinberger-Schuberth-Fischer Rechtsanwälte-GmbH in Zell am See, wegen 21.376,95 EUR sA und Feststellung (Streitwert: 10.000 EUR), über die Revisionen der klagenden und der zweitbeklagten Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 6. August 2021, GZ 53 R 110/21i-23, womit das Teil- und Teilzwischenurteil des Bezirksgerichts Zell am See vom 6. April 2021, GZ 18 C 892/20z-17, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revisionen der klagenden und der zweitbeklagten Partei werden zurückgewiesen.

**False Positives:**

- `Dr. Alexander Bosio` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ing. Constanze Kronawitt`(person)
- `DDr. Leif Eralp`(person)
- `Lothar Schwänke`(person)

**Example 67** (doc_id: `deanon_TRAIN/2Ob181_10x`) (sent_id: `deanon_TRAIN/2Ob181_10x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Gertrude Ptak, vertreten durch Dr. Bertram Broesigke und Dr. Wolfgang Broesigke, Rechtsanwälte in Wien, gegen die beklagte Partei Josef Schindelmeißer, vertreten durch den Sachwalter Dr. Helmut Heiger, Rechtsanwalt in Wien, wegen Aufkündigung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 15. Juni 2010, GZ 41 R 130/10m-26, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Dr. Bertram Broesigke und Dr. Wolfgang Broesigke` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ptak`(person)
- `Schindelmeißer`(person)

**Example 68** (doc_id: `deanon_TRAIN/2Ob182_24i`) (sent_id: `deanon_TRAIN/2Ob182_24i_4`)


Sloboda, Dr. Thunhart und Dr. Kikinger sowie die Hofrätin Mag. Fitz als weitere Richter in der Rechtssache der klagenden und gefährdeten Partei Theresa Ziebold, vertreten durch Mag. Mahmut Sahinol, Rechtsanwalt in Wien, gegen die beklagten Parteien und Gegner der gefährdeten Parteien 1.

**False Positives:**

- `Mag. Mahmut Sahinol` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Theresa Ziebold`(person)

**Example 69** (doc_id: `deanon_TRAIN/2Ob182_24i`) (sent_id: `deanon_TRAIN/2Ob182_24i_5`)


Vivian Canzler, 2. Viola Raudzus, und 3. Livia Baumbach, alle vertreten durch Dr. Alexander Hofmann, Rechtsanwalt in Wien, wegen Einwilligung in eine Einverleibung (140.000 EUR), über den außerordentlichen Revisionsrekurs der gefährdeten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 30. September 2024, GZ 11 R 147/24d-12, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß § 78 EO, § 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Alexander Hofmann` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Vivian Canzler`(person)
- `Viola Raudzus`(person)
- `Livia Baumbach`(person)

**Example 70** (doc_id: `deanon_TRAIN/2Ob216_18f`) (sent_id: `deanon_TRAIN/2Ob216_18f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden und den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé und die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Hon.-Prof. Ewald Schwietale, vertreten durch Mag. Martin Paar und Mag. Hermann Zwanzger, Rechtsanwälte in Wien, gegen die beklagte Partei Lütkemöller Digital AG, Karl Deppermann, vertreten durch Dr. Helmut Weinzettl, Rechtsanwalt in Wiener Neustadt, wegen 14.817,50 EUR sA, über die Revisionen beider Parteien gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 27. Juni 2018, GZ 18 R 11/18y-64, mit welchem das Urteil des Bezirksgerichts Baden vom 28. Dezember 2017, GZ 7 C 1010/15x-58, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revisionen werden zurückgewiesen.

**False Positives:**

- `Mag. Martin Paar und Mag. Hermann Zwanzger` — no gold match — likely missing annotation
- `Dr. Helmut Weinzettl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Hon.-Prof. Ewald Schwietale`(person)
- `Lütkemöller Digital AG`(organisation)
- `Karl Deppermann`(person)

**Example 71** (doc_id: `deanon_TRAIN/2Ob224_21m`) (sent_id: `deanon_TRAIN/2Ob224_21m_5`)


Dr. Konstantin Haas, Rechtsanwalt in Leonding, gegen die beklagte Partei Annette Provost, vertreten durch Posch, Schausberger & Lutz Rechtsanwälte GmbH in Wels, wegen 25.650,07 EUR sA sowie Herausgabe (Streitwert 1.000 EUR) über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 1. Oktober 2021, GZ 2 R 119/21i-48, mit dem das Urteil des Landesgerichts Ried im Innkreis vom 28. Juni 2021, GZ 5 Cg 60/18b-44, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Posch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Annette Provost`(person)

**Example 72** (doc_id: `deanon_TRAIN/2Ob226_19b`) (sent_id: `deanon_TRAIN/2Ob226_19b_4`)


Roswitha Buchmueller, vertreten durch Mag. Nikolaus Rast, Rechtsanwalt in Wien, wegen 21.485,09 EUR sA (erstbeklagte Partei) und 7.333,11 EUR sA (zweitklagende Partei), über den Rekurs der beklagten Parteien (Rekursinteresse der erstbeklagten Partei 15.833,25 EUR, der zweitbeklagten Partei 7.113,49 EUR) gegen den Beschluss des Oberlandesgerichts Wien als Berufungsgericht vom 21. Oktober 2019, GZ 12 R 20/19b-18, womit infolge Berufung der beklagten Parteien das Urteil des Landesgerichts Eisenstadt vom 28. November 2018, GZ 27 Cg 22/18f-14, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Mag. Nikolaus Rast` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Roswitha Buchmueller`(person)

**Example 73** (doc_id: `deanon_TRAIN/2Ob256_12d`) (sent_id: `deanon_TRAIN/2Ob256_12d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und durch die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Stallbauer Telekom Aktiengesellschaft, Poysdorfer Straße 5, 9341 Dobersberg, Österreich, vertreten durch Dr. Manfred Steininger, Rechtsanwalt in Wien, gegen die beklagte Partei DDr. Viktor Junkmanns, Bakk. iur., vertreten durch die ANWALTGMBH Rinner Teuchtmann in Linz, wegen 50.932,89 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2012, GZ 4 R 158/12a-20, womit das Urteil des Landesgerichts Linz vom 14. Juni 2012, GZ 5 Cg 119/11m-14, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Manfred Steininger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stallbauer Telekom Aktiengesellschaft`(organisation)
- `Poysdorfer Straße 5, 9341 Dobersberg, Österreich`(address)
- `DDr. Viktor Junkmanns, Bakk. iur.`(person)

**Example 74** (doc_id: `deanon_TRAIN/2Ob37_17f`) (sent_id: `deanon_TRAIN/2Ob37_17f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé und den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Florentin Uffenwasser, vertreten durch Dr. Armin Exner, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Stadtgemeinde Naomi Mertensmeyer, vertreten durch Dr. Thomas Girardi, Rechtsanwalt in Innsbruck, wegen 29.461,04 EUR sA und Feststellung (Streitwert 10.000 EUR), über die außerordentliche Revision der beklagten Partei (Revisionsinteresse 22.377,04 EUR) gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 15. Dezember 2016, GZ 2 R 141/16a-47, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Armin Exner` — no gold match — likely missing annotation
- `Dr. Thomas Girardi` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Florentin Uffenwasser`(person)
- `Naomi Mertensmeyer`(person)

**Example 75** (doc_id: `deanon_TRAIN/2Ob63_11w`) (sent_id: `deanon_TRAIN/2Ob63_11w_4`)


Holz Seewald AG, Kaiserbrunnengasse 6, 5122 Lindach, Österreich, beide vertreten durch Dr. Leopold Hirsch, Rechtsanwalt in Salzburg, wegen 38.967,48 EUR sA und Feststellung (Streitinteresse 20.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 10. Februar 2011, GZ 4 R 206/10g-29, womit das Urteil des Landesgerichts Salzburg vom 17. August 2010, GZ 7 Cg 49/09f-25, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Leopold Hirsch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Holz Seewald AG`(organisation)
- `Kaiserbrunnengasse 6, 5122 Lindach, Österreich`(address)

**Example 76** (doc_id: `deanon_TRAIN/2Ob71_23i`) (sent_id: `deanon_TRAIN/2Ob71_23i_4`)


Sloboda und Dr. Kikinger als weitere Richter in der Rechtssache der klagenden Partei Moses Malkomes, vertreten durch Klepp Nöbauer Hintringer Primetshofer Rechtsanwälte (GbR) in Linz, gegen die beklagte Partei Carmen Reinoldsmann, vertreten durch Dr. Christoph Arbeithuber, Rechtsanwalt in Linz, wegen 26.843,50 EUR sA und Feststellung, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 27. Februar 2023, GZ 4 R 17/23g-28, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Christoph Arbeithuber` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Moses Malkomes`(person)
- `Carmen Reinoldsmann`(person)

**Example 77** (doc_id: `deanon_TRAIN/2Ob73_15x`) (sent_id: `deanon_TRAIN/2Ob73_15x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden, die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé sowie den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Dragan Karp, vertreten durch Mag. Bernd Trappmaier, Rechtsanwalt in Korneuburg, gegen die beklagte Partei Marlene Diderichs, vertreten durch Mag. Claus Marchl, Rechtsanwalt in Wien, wegen 25.396,03 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 22. Jänner 2015, GZ 11 R 239/14v-26, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Wien vom 30. September 2014, GZ 57 Cg 30/14x-22, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Mag. Bernd Trappmaier` — no gold match — likely missing annotation
- `Mag. Claus Marchl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Dragan Karp`(person)
- `Marlene Diderichs`(person)

**Example 78** (doc_id: `deanon_TRAIN/2Ob78_15g`) (sent_id: `deanon_TRAIN/2Ob78_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden, die Hofräte Dr. Veith und Dr. Musger sowie die Hofrätinnen Dr. E. Solé und Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Luigi Neimeier, vertreten durch Rechtsanwälte Estermann & Partner OG in Mattighofen, gegen die beklagte Partei LNC KI Solutions GmbH, Kordelia Grauel, vertreten durch Dr. Herbert Harlander und Mag. Wolfgang Harlander, Rechtsanwälte in Salzburg, wegen 33.251,85 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 5. März 2015, GZ 2 R 1/15b-37, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Salzburg vom 23. Oktober 2014, GZ 4 Cg 27/13d-33, bestätigt wurde, in nichtöffentlicher Sitzung beschlossen und zu Recht erkannt:  Spruch

**False Positives:**

- `Dr. Herbert Harlander und Mag. Wolfgang Harlander` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Luigi Neimeier`(person)
- `LNC KI Solutions GmbH`(organisation)
- `Kordelia Grauel`(person)

**Example 79** (doc_id: `deanon_TRAIN/2Ob86_12d`) (sent_id: `deanon_TRAIN/2Ob86_12d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Baumann als Vorsitzenden und die Hofräte Dr. Veith, Dr. E. Solé, Dr. Schwarzenbacher und Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Constanze Hoefelmann, MSc, vertreten durch Gruböck & Lentschig Rechtsanwälte OG in Baden, wider die beklagte Partei „ Herbert Sippert “ Ada Roselius, vertreten durch Themmer, Toth & Partner Rechtsanwälte OG in Wien, wegen 144.329,55 EUR sA (Revisionsinteresse 54.717 EUR sA), infolge der außerordentlichen Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. Februar 2012, GZ 4 R 598/11g-25, den Beschluss gefasst:  Spruch Das Revisionsverfahren wird bis zur rechtskräftigen Erledigung des Verfahrens über den Ablehnungsantrag der beklagten Partei gegen die Erstrichterin unterbrochen.

**False Positives:**

- `Themmer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Constanze Hoefelmann, MSc`(person)
- `Herbert Sippert`(person)
- `Ada Roselius`(person)

**Example 80** (doc_id: `deanon_TRAIN/2Ob89_17b`) (sent_id: `deanon_TRAIN/2Ob89_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Vizepräsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende, die Hofräte Dr. Veith und Dr. Musger, die Hofrätin Dr. E. Solé sowie den Hofrat Dr. Nowotny als weitere Richter in der Rechtssache der klagenden Partei Aron Dawideit, vertreten durch Posch, Schausberger & Lutz Rechtsanwälte GmbH in Wels, gegen die beklagten Parteien 1. PhD Irvin Kindschuh, 2. Theodor Hermus, und 3.

**False Positives:**

- `Posch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Aron Dawideit`(person)
- `PhD Irvin Kindschuh`(person)
- `Theodor Hermus`(person)

**Example 81** (doc_id: `deanon_TRAIN/2Ob89_17b`) (sent_id: `deanon_TRAIN/2Ob89_17b_4`)


AlpenOstunitalWind Versicherungs-AG, Kirchenstiege 6, 6353 Reith bei Kitzbühel, Österreich, alle vertreten durch Mag. Dr. A. Michael Dallinger, Rechtsanwalt in Wels, wegen 187.040,19 EUR sA und Feststellung (Streitinteresse: 5.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 1. März 2017, GZ 6 R 30/17z-42, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mag. Dr. A. Michael Dallinger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `AlpenOstunitalWind`(organisation)
- `Kirchenstiege 6, 6353 Reith bei Kitzbühel, Österreich`(address)

**Example 82** (doc_id: `deanon_TRAIN/2Ob91_22d`) (sent_id: `deanon_TRAIN/2Ob91_22d_4`)


Sloboda und Dr. Kikinger als weitere Richter in der Rechtssache der klagenden Partei Farina Dirker, vertreten durch Dr. Sven Rudolf Thorstensen, LL.M., Rechtsanwalt in Wien, gegen die beklagte Partei Lüttge Chemie Limited, René Luidthard, vertreten durch Brandl Talos Rechtsanwälte GmbH in Wien, wegen 40.150,26 EUR sA, im Verfahren über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. Februar 2022, GZ 15 R 171/21h-33, den Beschluss gefasst:  Spruch Die Zurücknahme der Revision wird zur Kenntnis genommen.

**False Positives:**

- `Dr. Sven Rudolf Thorstensen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Farina Dirker`(person)
- `Lüttge Chemie Limited`(organisation)
- `René Luidthard`(person)

**Example 83** (doc_id: `deanon_TRAIN/2Ob99_18z`) (sent_id: `deanon_TRAIN/2Ob99_18z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden, den Hofrat Dr. Musger, die Hofrätin Dr. E. Solé sowie die Hofräte Dr. Nowotny und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Stadt-Textil GmbH & Co KG, Kreuzlandstraße 52, 9462 Kalchberg, Österreich, vertreten durch die DSC Doralt Seist Csoklich Rechtsanwälte GmbH, Wien, gegen die beklagte Partei Kazlowski + Röttjer Automotive GmbH, Clarissa Lenschau, vertreten durch Keschmann Rechtsanwalts-GmbH in Wien, sowie die Nebenintervenientinnen 1. Ost-Chemie GmbH, M.-Klieber-Gasse 22, 3611 Himberg, Österreich, vertreten durch Dr. Dirk Just, Rechtsanwalt in Wien, 2.

**False Positives:**

- `Dr. Dirk Just` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stadt-Textil GmbH`(organisation)
- `Kreuzlandstraße 52, 9462 Kalchberg, Österreich`(address)
- `Kazlowski + Röttjer Automotive GmbH`(organisation)
- `Clarissa Lenschau`(person)
- `Ost-Chemie GmbH`(organisation)
- `M.-Klieber-Gasse 22, 3611 Himberg, Österreich`(address)

**Example 84** (doc_id: `deanon_TRAIN/2Ob99_18z`) (sent_id: `deanon_TRAIN/2Ob99_18z_4`)


Oßmer KI GmbH, Dr.H.Pirchegger-Weg 23, 4154 Lengau, Österreich, vertreten durch Mag. Martina Hackl, Rechtsanwältin in Mödling, und 3. Pistor Pflege GmbH, Maierlweg 58, 4776 Kobledt, Österreich, vertreten durch Dr. Klaus Rainer, Rechtsanwalt in Graz, wegen 308.539,34 EUR sA und Feststellung (Streitwert 10.000 EUR), über die außerordentliche Revision der klagenden Partei (Revisionsinteresse 92.942,15 EUR) gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. März 2018, GZ 1 R 140/17s-101, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mag. Martina Hackl` — no gold match — likely missing annotation
- `Dr. Klaus Rainer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Oßmer KI GmbH`(organisation)
- `Dr.H.Pirchegger-Weg 23, 4154 Lengau, Österreich`(address)
- `Pistor Pflege GmbH`(organisation)
- `Maierlweg 58, 4776 Kobledt, Österreich`(address)

**Example 85** (doc_id: `deanon_TRAIN/3Nc11_13t`) (sent_id: `deanon_TRAIN/3Nc11_13t_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie die Hofräte Univ.-Prof Dr. Neumayr und Dr. Jensik als weitere Richter in der Ordinationssache der Antragstellerin Waldzorval Technologien GmbH, Dr.-Kühne-Gasse 29, 9560 Albern, Österreich, vertreten durch Dr. Clemens Thiele, Rechtsanwalt in Salzburg, gegen die Antragsgegnerin Pflege Allemkraft GmbH, Schirmerstraße 61, 8967 Oberhausberg, Österreich, wegen Exekutionsführung nach § 355 EO, infolge Antrags gemäß § 28 JN den Beschluss gefasst:  Spruch Für die Bewilligung und die Vollziehung der beabsichtigten Unterlassungsexekution wird das Bezirksgericht Salzburg als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Dr. Clemens Thiele` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Waldzorval Technologien GmbH`(organisation)
- `Dr.-Kühne-Gasse 29, 9560 Albern, Österreich`(address)
- `Pflege Allemkraft GmbH`(organisation)
- `Schirmerstraße 61, 8967 Oberhausberg, Österreich`(address)
- `Bezirksgericht Salzburg`(organisation)

**Example 86** (doc_id: `deanon_TRAIN/3Ob105_13g`) (sent_id: `deanon_TRAIN/3Ob105_13g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei ÖkR Malik Sutmöller OEG, Leila Nieboer, vertreten durch Dr. Heinz-Wilhelm Stenzl, Rechtsanwalt in Wien, gegen die beklagte Partei Mittel Bachlemsee GmbH, Erwin Klefass, BSc, vertreten durch Dr. Johann Gelbmann, Rechtsanwalt in Wien, wegen (restlich) 12.536,14 EUR sA, über die Revision der beklagten Partei (Revisionsinteresse 6.909 EUR sA) gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 19. Dezember 2012, GZ 38 R 173/12s-139, womit über die Berufungen beider Parteien das Urteil des Bezirksgerichts Fünfhaus vom 10. April 2012, GZ 12 C 1045/05m-131, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Dr. Johann Gelbmann` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `ÖkR Malik Sutmöller`(person)
- `Leila Nieboer`(person)
- `Mittel Bachlemsee GmbH`(organisation)
- `Erwin Klefass, BSc`(person)

**Example 87** (doc_id: `deanon_TRAIN/3Ob112_23a`) (sent_id: `deanon_TRAIN/3Ob112_23a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Höllwerth als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Brenn, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der außerstreitigen Rechtssache der Antragstellerin Amalia Lupprich, vertreten durch Dr. Walter Fleissner, Rechtsanwalt in Wien, gegen die Antragsgegnerin Zarin Terzi, vertreten durch Mag. Werner Hauser Rechtsanwalt in Wien, über den außerordentlichen Revisionsrekurs der Antragstellerin gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 27. Februar 2023, GZ 43 R 331/22b-65, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

**False Positives:**

- `Dr. Walter Fleissner` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Amalia Lupprich`(person)
- `Zarin Terzi`(person)

**Example 88** (doc_id: `deanon_TRAIN/3Ob137_17v`) (sent_id: `deanon_TRAIN/3Ob137_17v_4`)


Siegfried Littwinsky, geboren am 20. Februar 2007, 2. Ada Damien, geboren am 2. Februar 2009, beide wohnhaft beim Vater Mag. Nepomuk Chimenti, dieser vertreten durch Dr. Johann Etienne Korab, Rechtsanwalt in Wien, über den außerordentlichen Revisionsrekurs der Mutter Mag. Floriane Platvoet, vertreten durch Hornek Hubacek Lichtenstrasser Rechtsanwälte OG in Wien, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 15. Mai 2017, GZ 48 R 101/17b-137, womit Punkt 1. und 2. des Beschlusses des Bezirksgerichts Döbling vom 9. Jänner 2017, GZ 1 Ps 119/13b-90, bestätigt wurde, den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Dr. Johann Etienne Korab` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Siegfried Littwinsky`(person)
- `20. Februar`(date)
- `Ada Damien`(person)
- `2. Februar`(date)
- `Mag. Nepomuk Chimenti`(person)
- `Mag. Floriane Platvoet`(person)

**Example 89** (doc_id: `deanon_TRAIN/3Ob147_20v`) (sent_id: `deanon_TRAIN/3Ob147_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Kraftnorost Wind GmbH, Roderich Holtze, vertreten durch Mag. Andreas Kleiber, Rechtsanwalt in Wien, gegen die beklagte Partei Annette Fiss verein Ing. Kirstin Movcan, vertreten durch Pflaum Karlberger Wiener Opetnik, Rechtsanwälte in Wien, wegen Aufkündigung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 22. Juli 2020, GZ 40 R 37/20t-27, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Mag. Andreas Kleiber` — no gold match — likely missing annotation
- `Pflaum Karlberger Wiener Opetnik` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Kraftnorost Wind GmbH`(organisation)
- `Roderich Holtze`(person)
- `Annette Fiss`(person)
- `Ing. Kirstin Movcan`(person)

**Example 90** (doc_id: `deanon_TRAIN/3Ob152_10i`) (sent_id: `deanon_TRAIN/3Ob152_10i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Exekutionssache der betreibenden Partei KMN Versicherung Werke AG, Corbinian Pichlmaier, vertreten durch Dr. Erich Kafka, Dr. Manfred Palkovits, Rechtsanwälte in Wien, gegen die verpflichtete Partei Severin Wellenbrink, vertreten durch Dr. Philipp Jessich, Rechtsanwalt in Wien, wegen Aufschiebung einer Räumungsexekution, über den Revisionsrekurs der betreibenden Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 12. Mai 2010, GZ 39 R 44/10z-22, womit der Beschluss des Bezirksgerichts Fünfhaus vom 14. Jänner 2010, GZ 10 E 171/09d-6, abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Dr. Philipp Jessich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `KMN Versicherung Werke AG`(organisation)
- `Corbinian Pichlmaier`(person)
- `Dr. Erich Kafka`(person)
- `Dr. Manfred Palkovits`(person)
- `Severin Wellenbrink`(person)

**Example 91** (doc_id: `deanon_TRAIN/3Ob155_13k`) (sent_id: `deanon_TRAIN/3Ob155_13k_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Univ.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Exekutionssache der betreibenden Partei Dr. Ingolf Durur, vertreten durch Dr. Lucas Lorenz, Rechtsanwalt in Innsbruck, gegen die verpflichtete Partei Imre Viße, vertreten durch Dr. Robert Eiter, Rechtsanwalt in Landeck, wegen Einverleibung des Eigentumsrechts sowie Lastenfreistellung (§§ 350, 353 EO), über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts Innsbruck als Rekursgericht vom 4. Juni 2013, GZ 1 R 10/13x-22, womit die Exekutionsbewilligung des Bezirksgerichts Imst vom 13. November 2012, GZ 5 E 2224/12y-2, bestätigt wurde, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Lucas Lorenz` — no gold match — likely missing annotation
- `Dr. Robert Eiter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Dr. Ingolf Durur`(person)
- `Imre Viße`(person)

**Example 92** (doc_id: `deanon_TRAIN/3Ob156_12f`) (sent_id: `deanon_TRAIN/3Ob156_12f_5`)


Engelbert Johanns, vertreten durch Dr. Wolfgang Poleschinski, Rechtsanwalt in Hartberg, wegen Einwendungen gegen Strafbeschlüsse (§ 36 EO), über den Rekurs der beklagten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 6. Juli 2012, GZ 4 R 73/12b-28, womit über Berufung der klagenden Partei das Urteil des Bezirksgerichts Hartberg vom 24. Jänner 2012, GZ 2 C 321/11w (2 C 258/11f)-23, aufgehoben wurde, den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Dr. Wolfgang Poleschinski` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `deanon_TRAIN/3Ob164_20v`) (sent_id: `deanon_TRAIN/3Ob164_20v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei Bruckgartver GmbH, MedR StR René Titz, vertreten durch Dr. Reinhard Schanda, Rechtsanwalt in Wien, gegen die beklagte Partei Ofczarczik Planung AG, Dipl.

**False Positives:**

- `Dr. Reinhard Schanda` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bruckgartver GmbH`(organisation)
- `MedR StR René Titz`(person)
- `Ofczarczik Planung AG`(organisation)

**Example 94** (doc_id: `deanon_TRAIN/3Ob178_15w`) (sent_id: `deanon_TRAIN/3Ob178_15w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Jensik als Vorsitzenden, die Vizepräsidentin Dr. Lovrek, die Hofräte Dr. Schwarzenbacher und Dr. Roch sowie die Hofrätin Dr. Kodek als weitere Richter in der Rechtssache der klagenden Partei Nikolai Castelli, vertreten durch Divitschek Sieder Sauer Peter Rechtsanwälte GesBR in Deutschlandsberg, gegen die beklagte Partei Dohmgoergen Bau GmbH, Oswald Schubert, vertreten durch Dr. Johannes Liebmann, Rechtsanwalt in Gleisdorf, wegen 82.977,52 EUR sA und Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 27. Juli 2015, GZ 3 R 54/15h-145, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Dr. Johannes Liebmann` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Nikolai Castelli`(person)
- `Dohmgoergen Bau GmbH`(organisation)
- `Oswald Schubert`(person)

**Example 95** (doc_id: `deanon_TRAIN/3Ob17_20a`) (sent_id: `deanon_TRAIN/3Ob17_20a_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie die Hofräte Priv.-Doz. Dr. Rassi und Mag. Painsi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Exekutionssache betreibenden Partei Heizung Werkuni Aktiengesellschaft, P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich, vertreten durch Dr. Roland Grilc ua, Rechtsanwälte in Klagenfurt am Wörthersee, gegen die verpflichtete Partei Dorothea Eiken Bank, Peter Eitenmüller, vertreten durch Diwok Hermann Petsche Rechtsanwälte LLP Co KG in Wien, wegen 12.602.980,92 EUR sA, über den außerordentlichen Revisionsrekurs der verpflichteten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. November 2019, GZ 46 R 293/19g-18, mit dem der Beschluss des Bezirksgerichts Favoriten vom 17. April 2019, GZ 17 E 1298/19z-2, bestätigt wurde, den Beschluss gefasst:  Spruch I. Der Revisionsrekurs wird, soweit er sich gegen die Bestätigung der Exekutionsbewilligung richtet, als jedenfalls unzulässig zurückgewiesen.

**False Positives:**

- `Dr. Roland Grilc ua` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Heizung Werkuni Aktiengesellschaft`(organisation)
- `P.-B.-Rodlberger-Straße 78, 8672 Kirchenviertel, Österreich`(address)
- `Dorothea Eiken`(person)
- `Peter Eitenmüller`(person)

**Example 96** (doc_id: `deanon_TRAIN/3Ob192_11y`) (sent_id: `deanon_TRAIN/3Ob192_11y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Dr. Bartholomäus Nijboer, vertreten durch Hochsteger, Perz, Wallner & Warga Rechtsanwälte in Hallein, gegen die beklagte Partei Hon.-Prof. Dirk Edlich, vertreten durch Mag. Johann Meisthuber, Rechtsanwalt in Salzburg, wegen Einwendungen gegen den Anspruch (§ 35 EO), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Salzburg als Berufungsgericht vom 26. August 2011, GZ 21 R 31/11x-32, womit über Berufung der beklagten Partei das Urteil des Bezirksgerichts Salzburg vom 25. November 2010, GZ 31 C 86/09a-24, abgeändert wurde, den Beschluss gefasst:  Spruch Der außerordentlichen Revision wird Folge gegeben.

**False Positives:**

- `Hochsteger` — no gold match — likely missing annotation
- `Mag. Johann Meisthuber` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Dr. Bartholomäus Nijboer`(person)
- `Hon.-Prof. Dirk Edlich`(person)

**Example 97** (doc_id: `deanon_TRAIN/3Ob19_20w`) (sent_id: `deanon_TRAIN/3Ob19_20w_3`)


Kopf Der Oberste Gerichtshof hat durch die Präsidentin Hon.-Prof. Dr. Lovrek als Vorsitzende sowie die Hofräte Dr. Roch und Priv.-Doz. Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in den verbundenen Rechtssachen der klagenden Partei Rinaldo Isaac, vertreten durch Mag. Gerhard Walzl, Rechtsanwalt in Wien, wider die beklagte Partei Felizia Mascheck, vertreten durch Dr. Alexandra Sedelmayer-Pammesberger, Rechtsanwältin in Wien, wegen Unterhaltsherabsetzung (AZ 8 C 22/16k) und Einwendungen gegen den Anspruch nach § 35 EO (AZ 8 C 4/18s), über die „außerordentliche“ Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 20. August 2019, GZ 44 R 338/19k-67, mit dem das Urteil des Bezirksgerichts Hernals vom 23. Mai 2019, GZ 8 C 22/16k-60, bestätigt wurde, den Beschluss gefasst:  Spruch Die Akten werden neuerlich dem Erstgericht zurückgestellt.

**False Positives:**

- `Mag. Gerhard Walzl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Rinaldo Isaac`(person)
- `Felizia Mascheck`(person)

</details>

---

## `Judge_Richter`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `219eb9e0`  
**Description:**
Captures the name of a judge (Richter/Richterin/Vorsitzende) including complex titles and suffixes.

**Content:**
```
(?:durch\s+(?:den\s+)?(?:Richter|Richterin|Vorsitzende)\s+)([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|ÖkR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|Dr\.\s+Univ\.-Prof\.in?|Univ\.-Prof\.in?|Priv\.-Doz\.in?|Hon\.-Prof\.in?)?)?)(?:\s+(?:in der|über die|in der Verwaltungsstrafsache))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Party_Beschwerdesache`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9c38bec4`  
**Description:**
Captures the name of a party in a complaint case (Beschwerdesache/Rechtssache), handling 'der' prefix and complex suffixes.

**Content:**
```
(?:in der\s+(?:Beschwerdesache|Rechtssache|Verwaltungsstrafsache)\s+(?:der\s+)?)([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|ÖkR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB)?)?)(?:,\s+[A-Z]|\s+vertreten|\s+\(|\s+\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 2 | 100 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/9Nc65_19m`) (sent_id: `deanon_TRAIN/9Nc65_19m_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätinnen des Obersten Gerichtshofs Dr. Fichtenau und Mag. Korn als weitere Richter in der Rechtssache der Antragstellerin RgR Sonja Vormschlag, vertreten durch Dr. Wallentin-Hermann, Rechtsanwältin Wien, gegen die Antragsgegnerin Bianca Urbscheit, Russische Föderation, wegen 400 EUR sA, über den Ordinationsantrag nach § 28 JN, den Beschluss gefasst:  Spruch Dem Ordinationsantrag wird stattgegeben.

**False Positives:**

- `Antragstellerin RgR Sonja Vormschlag,` — partial — gold is substring of pred: `RgR Sonja Vormschlag`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RgR Sonja Vormschlag`(person)
- `Bianca Urbscheit`(person)

**Example 1** (doc_id: `deanon_TRAIN/9Ob55_17d`) (sent_id: `deanon_TRAIN/9Ob55_17d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsrekursgericht durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden sowie die Hofrätinnen und Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Dehn, Dr. Hargassner, Mag. Korn und Dr. Stefula in der Rechtssache der Antragstellerin Marlies Kroenert, gegen den Antragsgegner Calvin Behrbaum, vertreten durch Dr. Christian Branczik, Mag. Clemens Zehentleitner, Rechtsanwälte in Bad Aussee, wegen Unterhalt, über den Revisionsrekurs des Antragsgegners gegen den Beschluss des Landesgerichts Leoben als Rekursgericht vom 18. Juli 2017, GZ 2 R 152/17b-35, mit dem dem Rekurs des Antragsgegners gegen den Beschluss des Bezirksgerichts Liezen vom 16. Mai 2017, GZ 1 FAM 41/16f-30, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs des Antragsgegners wird zurückgewiesen.

**False Positives:**

- `Antragstellerin Marlies Kroenert, gegen den Antragsgegner Calvin Behrbaum,` — partial — gold is substring of pred: `Marlies Kroenert`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Marlies Kroenert`(person)
- `Calvin Behrbaum`(person)

</details>

---

## `Herr_Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `214b5905`  
**Description:**
Captures full names following 'Herr' or 'Herrn'.

**Content:**
```
(?:Herrn?\s+)([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Frau_Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ae51c48f`  
**Description:**
Captures full names following 'Frau'.

**Content:**
```
(?:Frau\s+)([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)+)
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

