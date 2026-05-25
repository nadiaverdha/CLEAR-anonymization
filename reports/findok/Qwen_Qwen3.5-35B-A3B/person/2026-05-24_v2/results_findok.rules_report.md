# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-05-24T15:12:36.978392

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-05-24_v2/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 2473 |
| Validation documents | 619 |
| Test documents | 96 |
| Train sentences | 3896 |
| Validation sentences | 1147 |
| Test sentences | 10026 |
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
| Best Batch Idx | 4 |
| Best Batch F1 | 0.40983606557377056 |
| Best Rules Serialized | [{'id': 'b11b6b1a', 'name': 'Judge_Richter', 'description': 'Captures the name of a judge (Richter/Richterin/Vorsitzende) including complex titles and suffixes.', 'format': 'regex', 'content': '(?:durch\\s+(?:den\\s+)?(?:Richter|Richterin|Vorsitzende)\\s+)([A-Z][a-zA-Z\\.\\s,]+?(?:\\s+(?:LL\\.M\\.|M\\.B\\.L\\.|B\\.Ed\\.|B\\.Sc\\.|MA|Bakk\\.|Dipl\\.-|Dipl\\.\\s+Kfm\\.|Ing\\.|MedR|VetR|Techn|\\u00d6kR|OStR|Univ\\.-|Priv\\.-|Hon\\.-|Dr\\.in|Mag\\.in|Mag\\.a|PhD|LLB|Dr\\.\\s+Univ\\.-Prof\\.in?|Univ\\.-Prof\\.in?|Priv\\.-Doz\\.in?|Hon\\.-Prof\\.in?)?)?)(?:\\s+(?:in der|\\u00fcber die|in der Verwaltungsstrafsache)|$)', 'priority': 10, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'ee477b11', 'name': 'Party_Beschwerdesache', 'description': "Captures the name of a party in a complaint case (Beschwerdesache/Rechtssache), handling 'der/des' prefix and complex suffixes.", 'format': 'regex', 'content': '(?:in der\\s+(?:Beschwerdesache|Rechtssache|Verwaltungsstrafsache|Revisionssache)\\s+(?:der\\s+|des\\s+)?)([A-Z][a-zA-Z\\.\\s,]+?(?:\\s+(?:LL\\.M\\.|M\\.B\\.L\\.|B\\.Ed\\.|B\\.Sc\\.|MA|Bakk\\.|Dipl\\.-|Dipl\\.\\s+Kfm\\.|Ing\\.|MedR|VetR|Techn|\\u00d6kR|OStR|Univ\\.-|Priv\\.-|Hon\\.-|Dr\\.in|Mag\\.in|Mag\\.a|PhD|LLB|BEd|BA|BSc|Mag\\.a|Mag\\.in|DDr\\.|R\\.in?|R\\.))?(?=,\\s+[A-Z]|\\s+vertreten|\\s+\\(|\\s+\\)|$|\\s+\\d{4}\\s+\\w+))', 'priority': 9, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '4913d14d', 'name': 'Representative_vertreten_durch', 'description': "Captures the name of a representative (lawyer/tax advisor) introduced by 'vertreten durch'.", 'format': 'regex', 'content': '(?:vertreten\\s+durch\\s+)([A-Z][a-zA-Z\\.\\s,]+?(?:\\s+(?:LL\\.M\\.|M\\.B\\.L\\.|B\\.Ed\\.|B\\.Sc\\.|MA|Bakk\\.|Dipl\\.-|Dipl\\.\\s+Kfm\\.|Ing\\.|MedR|VetR|Techn|\\u00d6kR|OStR|Univ\\.-|Priv\\.-|Hon\\.-|Dr\\.in|Mag\\.in|Mag\\.a|PhD|LLB|BEd|BA|BSc|DDr\\.|R\\.in?|R\\.)?)(?=,\\s+[A-Z]|\\s+GmbH|\\s+Steuerberatung|\\s+OG|\\s+KG|\\s+Rechtsanwalts|\\s+PartG|\\s+StbG|\\s+\\(|$))', 'priority': 6, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '4bee6298', 'name': 'Herr_Name', 'description': "Captures full names following 'Herr' or 'Herrn', ensuring the full name is extracted.", 'format': 'regex', 'content': '(?:Herr|Herrn)\\s+([A-Z][a-zA-Z\\u00e4\\u00f6\\u00fc\\u00df]+(?:\\s+[A-Z][a-zA-Z\\u00e4\\u00f6\\u00fc\\u00df]+)+)', 'priority': 7, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'b07361b5', 'name': 'Frau_Name', 'description': "Captures full names following 'Frau'.", 'format': 'regex', 'content': '(?:Frau|Frauen)\\s+([A-Z][a-zA-Z\\u00e4\\u00f6\\u00fc\\u00df]+(?:\\s+[A-Z][a-zA-Z\\u00e4\\u00f6\\u00fc\\u00df]+)+)(?=\\s+(?:in|von|der|des|\\(|$|\\d{4}|\\s+\\d))', 'priority': 5, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '98f92f79', 'name': 'Herr_Name_Corrected', 'description': "Captures full names following 'Herr' or 'Herrn', ensuring it matches a name (not a title) and handles German characters.", 'format': 'regex', 'content': '(?:Herr|Herrn)\\s+([A-Z][a-zA-Z\\u00e4\\u00f6\\u00fc\\u00df]+(?:\\s+[A-Z][a-zA-Z\\u00e4\\u00f6\\u00fc\\u00df]+)+)(?=\\s+(?:in|von|der|des|\\(|$|\\d{4}|\\s+\\d))', 'priority': 7, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}] |

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 98.0% |
| True Positives | 100 |
| False Positives | 34 |
| False Negatives | 254 |
| Total Gold Entities | 354 |
| Micro Precision | 74.6% |
| Micro Recall | 28.2% |
| Micro F1 | 41.0% |
| Macro F1 | 41.0% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Frau_Name` | 0.6% | 100.0% | 0.3% | 1 | 1 | 0 |
| `Herr_Name_Corrected` | 0.6% | 100.0% | 0.3% | 1 | 1 | 0 |
| `Party_Beschwerdesache` | 28.0% | 86.8% | 16.7% | 68 | 59 | 9 |
| `Herr_Name` | 9.0% | 68.0% | 4.8% | 25 | 17 | 8 |
| `Judge_Richter` | 11.7% | 57.5% | 6.5% | 40 | 23 | 17 |
| `Representative_vertreten_durch` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `Party_Beschwerdesache`

**F1:** 0.280 | **Precision:** 0.868 | **Recall:** 0.167  

**Format:** `regex`  
**Rule ID:** `ee477b11`  
**Description:**
Captures the name of a party in a complaint case (Beschwerdesache/Rechtssache), handling 'der/des' prefix and complex suffixes.

**Content:**
```
(?:in der\s+(?:Beschwerdesache|Rechtssache|Verwaltungsstrafsache|Revisionssache)\s+(?:der\s+|des\s+)?)([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|\u00d6kR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|BEd|BA|BSc|Mag\.a|Mag\.in|DDr\.|R\.in?|R\.))?(?=,\s+[A-Z]|\s+vertreten|\s+\(|\s+\)|$|\s+\d{4}\s+\w+))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.868 | 0.167 | 0.280 | 68 | 59 | 9 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 59 | 9 | 295 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/132828.1`) (sent_id: `findok-manually-annotated_TRAIN/132828.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Michaela Okyay, Franz-Wagner-Weg 6, 4973 Forsthub, Österreich, betreffend Beschwerde vom 30. September 2020 gegen den  Bescheid des Finanzamtes Hollabrunn Korneuburg Tulln (nunmehr Finanzamt Österreich) vom  1. September 2020 betreffend Abweisung des Antrages auf Gewährung von Familienbeihilfe  01.01.2019 in Höhe des in § 33 Abs. 3 erster Satz des Einkommensteuergesetzes 1988  festgelegten Betrages beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Michaela Okyay` | `Michaela Okyay` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Franz-Wagner-Weg 6, 4973 Forsthub, Österreich` (address)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/133563.1`) (sent_id: `findok-manually-annotated_TRAIN/133563.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Priv.-Doz. Pascal Knörle  in der Beschwerdesache  DDr. Rocco Fortmaier, Farbstraße 30, 5232 Angelberg, Österreich, über die Beschwerde vom 27. März 2015 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr zuständig: Finanzamt Österreich) vom 9. März 2015  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2013, Steuernummer 10-725/1788,  zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `DDr. Rocco Fortmaier` | `DDr. Rocco Fortmaier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Pascal Knörle` (person)
- `Farbstraße 30, 5232 Angelberg, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `Finanzamt Österreich` (organisation)
- `10-725/1788` (tax_number)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/132504.1`) (sent_id: `findok-manually-annotated_TRAIN/132504.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Maximilian Karrer  in der Beschwerdesache VetR Tosca Buecher,  Obere Amtshausgasse 26, 4591 Rosenau am Hengstpaß, Österreich, vertreten durch Grazer Treuhand Steuerberatung GmbH & Partner KG,  Petersgasse 128a, 8010 Graz, über die Beschwerde vom 14.11.2016 gegen den Bescheid des  Finanzamts Graz-Stadt vom 12.10.2016 betreffend Abweisung des Antrages gemäß § 299 BAO  vom 9.7.2015 auf Aufhebung des Einkommensteuerbescheides 2014 des Finanzamts Graz- Stadt vom 20.5.2015 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `VetR Tosca Buecher` | `VetR Tosca Buecher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Maximilian Karrer` (person)
- `Obere Amtshausgasse 26, 4591 Rosenau am Hengstpaß, Österreich` (address)
- `Grazer Treuhand Steuerberatung GmbH & Partner KG` (organisation)
- `Petersgasse 128a, 8010 Graz` (address)
- `Finanzamts Graz-Stadt` (organisation)
- `Finanzamts Graz- Stadt` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/136623.1`) (sent_id: `findok-manually-annotated_TRAIN/136623.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Leya Gern  in der Beschwerdesache Ronja Hebestreit,  Fisching 29, 4083 Untergschwendt, Österreich, über die Beschwerde vom 27.06.2021 gegen den Bescheid des Finanzamtes  Österreich vom 9. Juni 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer 14-107/0761  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ronja Hebestreit` | `Ronja Hebestreit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Leya Gern` (person)
- `Fisching 29, 4083 Untergschwendt, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `14-107/0761` (tax_number)

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/135536.1`) (sent_id: `findok-manually-annotated_TRAIN/135536.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Florentine Beumers, Krischgasse 309, 4113 Windischberg, Österreich, über die Beschwerde vom 20. Februar 2020 gegen den Bescheid  des Finanzamtes Österreich vom 16. Jänner 2020 betreffend Familienbeihilfe 01.2020  Steuernummer 58-742/0765, SVNR 8800 110262, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Florentine Beumers` | `Florentine Beumers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Krischgasse 309, 4113 Windischberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `58-742/0765` (tax_number)
- `8800 110262` (social_security_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/138410.1`) (sent_id: `findok-manually-annotated_TRAIN/138410.1_2`)


Gerald Erwin Ehgartner in der  Beschwerdesache Prof.in Klara Dolejsch, vertreten durch die Prof.in Tamara Simanek, über die Beschwerde vom 2.  November 2020 gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg (nunmehr  zuständig: Finanzamt Österreich) vom 9. September 2020 betreffend Abweisung des Antrags  auf Wiedereinsetzung in den vorigen Stand gemäß § 308 BAO zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Prof.in Klara Dolejsch,` — partial — gold is substring of pred: `Prof.in Klara Dolejsch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof.in Klara Dolejsch`(person)
- `Prof.in Tamara Simanek`(person)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_2`)


Gerald Erwin Ehgartner in der  Beschwerdesache Ronald Leinberger, vertreten durch Ernst & Young Steuerberatungsgesellschaft m.b.H.,  Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 6. Dezember 2019 gegen die  Bescheide des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr  zuständig: Finanzamt Österreich) vom 31. Oktober 2019 betreffend Gebühren 2010 bis 2012 zu  Recht:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ronald Leinberger,` — partial — gold is substring of pred: `Ronald Leinberger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ronald Leinberger`(person)
- `Ernst & Young Steuerberatungsgesellschaft m.b.H.`(organisation)
- `Wagramer Straße 19, 1220 Wien`(address)
- `Finanzamt Österreich`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/140526.1`) (sent_id: `findok-manually-annotated_TRAIN/140526.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Alois Ahl  in der Beschwerdesache Romana van Straaten, MBA,  Seeanlage Straße V 4p, 9335 St. Johann am Pressen, Österreich, vertreten durch Dr. Anna Schlosser-Péter, Kurrentgasse 6/3, 1010  Wien, über die Beschwerden vom 23. März 2015 gegen die Bescheide des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf (heute zuständig: Finanzamt Österreich) vom 17. März 2015  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2011 und 2012, Steuernummer  38-795/8528, zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Romana van Straaten` — partial — pred is substring of gold: `Romana van Straaten, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Alois Ahl`(person)
- `Romana van Straaten, MBA`(person)
- `Seeanlage Straße V 4p, 9335 St. Johann am Pressen, Österreich`(address)
- `Dr. Anna Schlosser-Péter`(person)
- `Kurrentgasse 6/3, 1010  Wien`(address)
- `Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `Finanzamt Österreich`(organisation)
- `38-795/8528`(tax_number)

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/144052.1`) (sent_id: `findok-manually-annotated_TRAIN/144052.1_2`)


Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Mag. Janosch Moehrle, Bakk. rer. nat., Neue Frauengasse 2, 3180 Hintereben, Österreich  vertreten durch Tschurtschenthaler, Walder,  Fister Rechtsanwälte GmbH, Dr. Arthur Lemisch Platz 7, 9020 Klagenfurt, über die Beschwerde  vom 3. Juni 2022 gegen den Bescheid des Finanzamtes Österreich vom 4. Mai 2022 betreffend  Einkommensteuer 2020 (Steuernummer 71-848/5765) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Janosch Moehrle` — partial — pred is substring of gold: `Mag. Janosch Moehrle, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Janosch Moehrle, Bakk. rer. nat.`(person)
- `Neue Frauengasse 2, 3180 Hintereben, Österreich`(address)
- `Tschurtschenthaler, Walder,  Fister Rechtsanwälte GmbH`(organisation)
- `Dr. Arthur Lemisch Platz 7, 9020 Klagenfurt`(address)
- `Finanzamtes Österreich`(organisation)
- `71-848/5765`(tax_number)

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149456.1`) (sent_id: `findok-manually-annotated_TRAIN/149456.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Eva Rauber  in der Beschwerdesache der  Henken, Dr.Walter-Hochsteiner-Straße 39, 4730 Röckendorferholz, Österreich, über die Beschwerde vom 2. September 2025 gegen den Bescheid  des Finanzamt Schwechat Gerasdorf  vom 28. August 2025 betreffend Abweisung eines Antrages auf Änderung des  Einkommensteuerbescheides 2024 gemäß § 295a BAO zu Steuernummer 69-427/7795  zu  Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Henken` — type mismatch — same span as gold: `Henken`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Eva Rauber`(person)
- `Henken`(organisation)
- `Dr.Walter-Hochsteiner-Straße 39, 4730 Röckendorferholz, Österreich`(address)
- `Finanzamt Schwechat Gerasdorf`(organisation)
- `69-427/7795`(tax_number)

</details>

---

## `Herr_Name`

**F1:** 0.090 | **Precision:** 0.680 | **Recall:** 0.048  

**Format:** `regex`  
**Rule ID:** `4bee6298`  
**Description:**
Captures full names following 'Herr' or 'Herrn', ensuring the full name is extracted.

**Content:**
```
(?:Herr|Herrn)\s+([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.680 | 0.048 | 0.090 | 25 | 17 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 17 | 8 | 253 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/139698.1`) (sent_id: `findok-manually-annotated_TRAIN/139698.1_1`)


IM NAMEN DER REPUBLI K  Gekürzte Ausfertigung des Erkenntnisses gemäß § 29 Abs. 5 VwGVG  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Verwaltungsstrafsache gegen Herrn Valentina Riehmers, Julius-Wagner-Jauregg-Gasse 1, 6232 Münster, Österreich, vertreten durch Huber  Swoboda Oswald Aixberger Rechtsanwälte GmbH, Tuchlauben 11/18, 1010 Wien, wegen der  Verwaltungsübertretungen gemäß § 1 Abs. 1 in Verbindung mit § 16 Abs. 1 und Tarifen D Post  1 und D Post 4 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBl. für Wien Nr. 20, in  der derzeit geltenden Fassung über die Beschwerde des Beschuldigten vom 4. März 2022  gegen   I. das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen  vom 3. Februar 2022, GZ. MA6/206000003074/2020,   II. das Straferkenntnis des Magistrates der Stadt Wien vom 21. Februar 2022, GZ.  MA6/206000003065/2020,   nach Durchführung einer mündlichen Verhandlung am 15. Dezember 2022 in Abwesenheit des  Beschuldigten, jedoch in Anwesenheit der Verteidigerin, auch als Vertreterin der haftenden  GmbH, der Behördenvertreterin und der Schriftführerin zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als bei  unverändert bleibenden Schuldsprüchen die Höhe der Strafen und der Kosten wie folgt  geändert werden:  II. Wegen der Verwaltungsübertretungen laut Erkenntnis vom 3. Februar 2022, GZ.  MA6/206000003074/2020, werden über den Beschuldigten folgende Strafen jeweils gemäß  § 16 Abs. 1 GAG LGBl. für Wien Nr. 20, in der derzeit geltenden Fassung verhängt:   1. – 5. Geldstrafen in Höhe von je € 330,00, falls diese uneinbringlich sind,   5 Ersatzfreiheitsstrafen von je 11 Stunden,   1 von 11 Seite 2 von 11

| Predicted | Gold |
|---|---|
| `Valentina Riehmers` | `Valentina Riehmers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gerhard Groschedl` (person)
- `Julius-Wagner-Jauregg-Gasse 1, 6232 Münster, Österreich` (address)
- `Huber  Swoboda Oswald Aixberger Rechtsanwälte GmbH` (organisation)
- `Tuchlauben 11/18, 1010 Wien` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/139698.1`) (sent_id: `findok-manually-annotated_TRAIN/139698.1_36`)


Die UnterRecycling Services GMBH  hafte für die mit diesem Bescheid über den zur Vertretung nach außen  Berufenen, Herrn Valentina Riehmers, verhängten Geldstrafen von 5 x je € 510,00 und 2 x je € 520,00  und die Verfahrenskosten in der Höhe von € 359,00 sowie für sonstige in Geld bemessene  Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.

| Predicted | Gold |
|---|---|
| `Valentina Riehmers` | `Valentina Riehmers` |

**Missed by this rule (FN):**

- `UnterRecycling Services GMBH` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/139698.1`) (sent_id: `findok-manually-annotated_TRAIN/139698.1_37`)


II. Mit Straferkenntnis des Magistrates der Stadt Wien vom 21. Februar 2022, GZ.  MA6/206000003065/2020, wurde Herr Valentina Riehmers, (in weiterer Folge: Beschuldigter) als  handelsrechtlicher Geschäftsführer der Firma UnterRecycling Services GMBH  mit Sitz in Mosletzberg 2, 4084 Dörfledt, Österreich,  schuldig erkannt,   1. er habe als handelsrechtlicher Geschäftsführer der Firma UnterRecycling Services GMBH  im Juni 2020 vor  der Liegenschaft in Rodelsbach 3, 4800 Lehen, Österreich, den öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, durch eine Baustofflagerung im Ausmaß von 57,50 m² genutzt, wobei er hiefür  bis zum 13.08.2020 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe  entrichtet habe.

| Predicted | Gold |
|---|---|
| `Valentina Riehmers` | `Valentina Riehmers` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)
- `UnterRecycling Services GMBH` (organisation)
- `Mosletzberg 2, 4084 Dörfledt, Österreich` (address)
- `UnterRecycling Services GMBH` (organisation)
- `Rodelsbach 3, 4800 Lehen, Österreich` (address)

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/139698.1`) (sent_id: `findok-manually-annotated_TRAIN/139698.1_62`)


Die UnterRecycling Services GMBH  hafte für die mit diesem Bescheid über den zur Vertretung nach außen  Berufenen, Herrn Valentina Riehmers, verhängten Geldstrafen von 3 x je € 520,00, 3 x je € 320,00 und 2  x je € 700,00 und die Verfahrenskosten in der Höhe von € 392,00 sowie für sonstige in Geld  bemessene Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.“

| Predicted | Gold |
|---|---|
| `Valentina Riehmers` | `Valentina Riehmers` |

**Missed by this rule (FN):**

- `UnterRecycling Services GMBH` (organisation)

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/148648.1`) (sent_id: `findok-manually-annotated_TRAIN/148648.1_6`)


Entscheidungsgründe  I. Verfahrensgang  Mit Einkommensteuerbescheid (Arbeitnehmerveranlagung) vom 1. März 2024 wurde die  Einkommensteuer von Herrn Bernhard Siegmundt (im Folgenden auch Beschwerdeführer oder Bf.) für das  Jahr 2023 mit einer Gutschrift in Höhe von EUR 29,- festgesetzt.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_2`)


Herrn OSR Jan Passerschroer, MA, geb. am 1960, Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich  2. Reinemut + Smoch Handel, Zachariasweg 4K, 3250 Wieselburg, Österreich   beide vertreten durch HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH, Triesterstraße  14, 2351 Wiener Neudorf,   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und Abs. 2 lit. a und 49 Abs. 1 lit. a FinStrG des Finanzstrafgesetzes  (FinStrG) über die Beschwerden des Beschuldigten und des belangten Verbandes jeweils vom  7. August 2024 gegen das Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als  Finanzstrafbehörde vom 28. Mai 2024, Geschäftszahl SpS-1, in der Sitzung am 10. Dezember  2024 in Anwesenheit der Schriftführerin zu Recht erkannt:  1.

**False Positives:**

- `OSR Jan Passerschroer` — partial — pred is substring of gold: `OSR Jan Passerschroer, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OSR Jan Passerschroer, MA`(person)
- `1960`(date)
- `Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich`(address)
- `Reinemut + Smoch Handel`(organisation)
- `Zachariasweg 4K, 3250 Wieselburg, Österreich`(address)
- `HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH`(organisation)
- `Triesterstraße  14, 2351 Wiener Neudorf`(address)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_15`)


Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22

**False Positives:**

- `OSR Jan Passerschroer` — partial — pred is substring of gold: `OSR Jan Passerschroer, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Amtes für Betrugsbekämpfung als Finanzstrafbehörde`(organisation)
- `OSR Jan Passerschroer, MA`(person)
- `Finanzamts Österreich`(organisation)
- `Reinemut + Smoch Handel`(organisation)
- `72-531/2688`(tax_number)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_86`)


Dieser Bescheid wurde von  Herrn OSR Jan Passerschroer, MA  nicht bekämpft und die Zahllasten wurden am Finanzamtskonto verbucht.

**False Positives:**

- `OSR Jan Passerschroer` — partial — pred is substring of gold: `OSR Jan Passerschroer, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OSR Jan Passerschroer, MA`(person)

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_89`)


3. Feststellungen des Vorsatzes nach § 33 (1) sowie des Vorsatzes und der Wissentlichkeit nach  § 33 (2) a und b FinStrG  Aus den Ausführungen unserer Mandantschaft, insbesondere des Schreibens vom 17.05.2024  an das Amt für Betrugsbekämpfung, geht hervor, dass Herr OSR Jan Passerschroer, MA  zu den Tatzeitpunkten  in einem psychisch instabilen Zustand war.

**False Positives:**

- `OSR Jan Passerschroer` — partial — pred is substring of gold: `OSR Jan Passerschroer, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OSR Jan Passerschroer, MA`(person)

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_92`)


Herr OSR Jan Passerschroer, MA  hat aufgrund seiner  psychischen Instabilität seine Sorgfalt außer Acht gelassen und eine verspätete  Abgabenentrichtung herbeigeführt.

**False Positives:**

- `OSR Jan Passerschroer` — partial — pred is substring of gold: `OSR Jan Passerschroer, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OSR Jan Passerschroer, MA`(person)

</details>

---

## `Judge_Richter`

**F1:** 0.117 | **Precision:** 0.575 | **Recall:** 0.065  

**Format:** `regex`  
**Rule ID:** `b11b6b1a`  
**Description:**
Captures the name of a judge (Richter/Richterin/Vorsitzende) including complex titles and suffixes.

**Content:**
```
(?:durch\s+(?:den\s+)?(?:Richter|Richterin|Vorsitzende)\s+)([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|\u00d6kR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|Dr\.\s+Univ\.-Prof\.in?|Univ\.-Prof\.in?|Priv\.-Doz\.in?|Hon\.-Prof\.in?)?)?)(?:\s+(?:in der|\u00fcber die|in der Verwaltungsstrafsache)|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.575 | 0.065 | 0.117 | 40 | 23 | 17 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 23 | 17 | 331 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/132828.1`) (sent_id: `findok-manually-annotated_TRAIN/132828.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Michaela Okyay, Franz-Wagner-Weg 6, 4973 Forsthub, Österreich, betreffend Beschwerde vom 30. September 2020 gegen den  Bescheid des Finanzamtes Hollabrunn Korneuburg Tulln (nunmehr Finanzamt Österreich) vom  1. September 2020 betreffend Abweisung des Antrages auf Gewährung von Familienbeihilfe  01.01.2019 in Höhe des in § 33 Abs. 3 erster Satz des Einkommensteuergesetzes 1988  festgelegten Betrages beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Michaela Okyay` (person)
- `Franz-Wagner-Weg 6, 4973 Forsthub, Österreich` (address)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)

| Predicted | Gold |
|---|---|
| `Mag.Dr. Wolfgang Pagitsch` | `Mag.Dr. Wolfgang Pagitsch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Brunhild Katschmareck` (person)
- `Oberwinden 3, 4553 Hausmanning, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Wien` (city)
- `Wien` (city)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/135661.1`) (sent_id: `findok-manually-annotated_TRAIN/135661.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht über die Beschwerden der  Reinhold Moellenkamp, Höllererweg 4, 2852 Maltern, Österreich, vertreten durch die Achammer & Mennel Rechtsanwälte OG,  Schloßgraben 10, 6800 Feldkirch, gegen die Bescheide des Finanzamtes Feldkirch vom  7. Jänner 2020 betreffend Festsetzung der Kraftfahrzeugsteuer für den Zeitraum 8-10/2019  und Festsetzung der Normverbrauchsabgabe für den Zeitraum 07/2019, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Reinhold Moellenkamp` (person)
- `Höllererweg 4, 2852 Maltern, Österreich` (address)
- `Achammer & Mennel Rechtsanwälte OG` (organisation)
- `Schloßgraben 10, 6800 Feldkirch` (address)
- `Finanzamtes Feldkirch` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/135536.1`) (sent_id: `findok-manually-annotated_TRAIN/135536.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Florentine Beumers, Krischgasse 309, 4113 Windischberg, Österreich, über die Beschwerde vom 20. Februar 2020 gegen den Bescheid  des Finanzamtes Österreich vom 16. Jänner 2020 betreffend Familienbeihilfe 01.2020  Steuernummer 58-742/0765, SVNR 8800 110262, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Florentine Beumers` (person)
- `Krischgasse 309, 4113 Windischberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `58-742/0765` (tax_number)
- `8800 110262` (social_security_number)

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/139698.1`) (sent_id: `findok-manually-annotated_TRAIN/139698.1_1`)


IM NAMEN DER REPUBLI K  Gekürzte Ausfertigung des Erkenntnisses gemäß § 29 Abs. 5 VwGVG  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Verwaltungsstrafsache gegen Herrn Valentina Riehmers, Julius-Wagner-Jauregg-Gasse 1, 6232 Münster, Österreich, vertreten durch Huber  Swoboda Oswald Aixberger Rechtsanwälte GmbH, Tuchlauben 11/18, 1010 Wien, wegen der  Verwaltungsübertretungen gemäß § 1 Abs. 1 in Verbindung mit § 16 Abs. 1 und Tarifen D Post  1 und D Post 4 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBl. für Wien Nr. 20, in  der derzeit geltenden Fassung über die Beschwerde des Beschuldigten vom 4. März 2022  gegen   I. das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen  vom 3. Februar 2022, GZ. MA6/206000003074/2020,   II. das Straferkenntnis des Magistrates der Stadt Wien vom 21. Februar 2022, GZ.  MA6/206000003065/2020,   nach Durchführung einer mündlichen Verhandlung am 15. Dezember 2022 in Abwesenheit des  Beschuldigten, jedoch in Anwesenheit der Verteidigerin, auch als Vertreterin der haftenden  GmbH, der Behördenvertreterin und der Schriftführerin zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als bei  unverändert bleibenden Schuldsprüchen die Höhe der Strafen und der Kosten wie folgt  geändert werden:  II. Wegen der Verwaltungsübertretungen laut Erkenntnis vom 3. Februar 2022, GZ.  MA6/206000003074/2020, werden über den Beschuldigten folgende Strafen jeweils gemäß  § 16 Abs. 1 GAG LGBl. für Wien Nr. 20, in der derzeit geltenden Fassung verhängt:   1. – 5. Geldstrafen in Höhe von je € 330,00, falls diese uneinbringlich sind,   5 Ersatzfreiheitsstrafen von je 11 Stunden,   1 von 11 Seite 2 von 11

| Predicted | Gold |
|---|---|
| `Mag. Gerhard Groschedl` | `Mag. Gerhard Groschedl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Valentina Riehmers` (person)
- `Julius-Wagner-Jauregg-Gasse 1, 6232 Münster, Österreich` (address)
- `Huber  Swoboda Oswald Aixberger Rechtsanwälte GmbH` (organisation)
- `Tuchlauben 11/18, 1010 Wien` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Magistrates der Stadt Wien` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/138410.1`) (sent_id: `findok-manually-annotated_TRAIN/138410.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter MMag.

**False Positives:**

- `MMag.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/140056.1`) (sent_id: `findok-manually-annotated_TRAIN/140056.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache   Emanuela Wilgen, Kölnhofsiedlung 12, 5622 Mitterstein, Österreich, über die Beschwerde vom 1. Juni 2022 gegen den Bescheid des  Finanzamtes Österreich vom 5. Mai 2022 betreffend Rückforderung von für Hademar Peschek  für  den Zeitraum Oktober 2021 bis Februar 2022 bezogener Beträge an Familienbeihilfe und  Kinderabsetzbetrag, Steuernummer 06-892/6489 (7083181213) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Emanuela Wilgen`(person)
- `Kölnhofsiedlung 12, 5622 Mitterstein, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Hademar Peschek`(person)
- `06-892/6489`(tax_number)
- `7083181213`(social_security_number)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter MMag.

**False Positives:**

- `MMag.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/140853.1`) (sent_id: `findok-manually-annotated_TRAIN/140853.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Juri Jonkhans  in der Beschwerdesache KommR Ulrich Maader,  Prangergasse 2, 5323 Hinterebenau, Österreich, vertreten durch Dr. Anton Herbert Pochieser, Schottenfeldgasse 2-4 Tür 23,  Wien 1070, betreffend die Beschwerde vom 29.09.2021 gegen den Bescheid des  Finanzamtes  Österreich vom 27. August 2021, mit welchem die Aussetzung der Entscheidung gem. § 271  BAO betreffend die Beschwerde vom 18.01.2021 gegen den Abweisungsbescheid vom  10.12.2020 (Ausgleichszahlung) verfügt wurde, zu SVNr.

**False Positives:**

- `Mag. Juri Jonkhans ` — partial — gold is substring of pred: `Mag. Juri Jonkhans`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Juri Jonkhans`(person)
- `KommR Ulrich Maader`(person)
- `Prangergasse 2, 5323 Hinterebenau, Österreich`(address)
- `Dr. Anton Herbert Pochieser`(person)
- `Schottenfeldgasse 2-4 Tür 23,  Wien 1070`(address)
- `Finanzamtes  Österreich`(organisation)

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/143368.1`) (sent_id: `findok-manually-annotated_TRAIN/143368.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Karlheinz Parlak  in der Beschwerdesache  Melinda Krebsz, Zauchmühle 136, 2463 Gallbrunn, Österreich, über die Beschwerde vom 8. Mai 2023 gegen den Bescheid des  Finanzamtes Österreich vom 27. April 2023 betreffend Einkommensteuer 2022 zur  Steuernummer 60-281/5380  zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Karlheinz Parlak ` — partial — gold is substring of pred: `Mag. Karlheinz Parlak`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Karlheinz Parlak`(person)
- `Melinda Krebsz`(person)
- `Zauchmühle 136, 2463 Gallbrunn, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `60-281/5380`(tax_number)

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

## `Representative_vertreten_durch`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4913d14d`  
**Description:**
Captures the name of a representative (lawyer/tax advisor) introduced by 'vertreten durch'.

**Content:**
```
(?:vertreten\s+durch\s+)([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|\u00d6kR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|BEd|BA|BSc|DDr\.|R\.in?|R\.)?)(?=,\s+[A-Z]|\s+GmbH|\s+Steuerberatung|\s+OG|\s+KG|\s+Rechtsanwalts|\s+PartG|\s+StbG|\s+\(|$))
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

## `Party_Beschwerdesache`

**F1:** 0.280 | **Precision:** 0.868 | **Recall:** 0.167  

**Format:** `regex`  
**Rule ID:** `ee477b11`  
**Description:**
Captures the name of a party in a complaint case (Beschwerdesache/Rechtssache), handling 'der/des' prefix and complex suffixes.

**Content:**
```
(?:in der\s+(?:Beschwerdesache|Rechtssache|Verwaltungsstrafsache|Revisionssache)\s+(?:der\s+|des\s+)?)([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|\u00d6kR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|BEd|BA|BSc|Mag\.a|Mag\.in|DDr\.|R\.in?|R\.))?(?=,\s+[A-Z]|\s+vertreten|\s+\(|\s+\)|$|\s+\d{4}\s+\w+))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.868 | 0.167 | 0.280 | 68 | 59 | 9 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 59 | 9 | 295 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/132828.1`) (sent_id: `findok-manually-annotated_TRAIN/132828.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Michaela Okyay, Franz-Wagner-Weg 6, 4973 Forsthub, Österreich, betreffend Beschwerde vom 30. September 2020 gegen den  Bescheid des Finanzamtes Hollabrunn Korneuburg Tulln (nunmehr Finanzamt Österreich) vom  1. September 2020 betreffend Abweisung des Antrages auf Gewährung von Familienbeihilfe  01.01.2019 in Höhe des in § 33 Abs. 3 erster Satz des Einkommensteuergesetzes 1988  festgelegten Betrages beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Michaela Okyay` | `Michaela Okyay` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Franz-Wagner-Weg 6, 4973 Forsthub, Österreich` (address)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/133563.1`) (sent_id: `findok-manually-annotated_TRAIN/133563.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Priv.-Doz. Pascal Knörle  in der Beschwerdesache  DDr. Rocco Fortmaier, Farbstraße 30, 5232 Angelberg, Österreich, über die Beschwerde vom 27. März 2015 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr zuständig: Finanzamt Österreich) vom 9. März 2015  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2013, Steuernummer 10-725/1788,  zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `DDr. Rocco Fortmaier` | `DDr. Rocco Fortmaier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Pascal Knörle` (person)
- `Farbstraße 30, 5232 Angelberg, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `Finanzamt Österreich` (organisation)
- `10-725/1788` (tax_number)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/132504.1`) (sent_id: `findok-manually-annotated_TRAIN/132504.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Maximilian Karrer  in der Beschwerdesache VetR Tosca Buecher,  Obere Amtshausgasse 26, 4591 Rosenau am Hengstpaß, Österreich, vertreten durch Grazer Treuhand Steuerberatung GmbH & Partner KG,  Petersgasse 128a, 8010 Graz, über die Beschwerde vom 14.11.2016 gegen den Bescheid des  Finanzamts Graz-Stadt vom 12.10.2016 betreffend Abweisung des Antrages gemäß § 299 BAO  vom 9.7.2015 auf Aufhebung des Einkommensteuerbescheides 2014 des Finanzamts Graz- Stadt vom 20.5.2015 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `VetR Tosca Buecher` | `VetR Tosca Buecher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Maximilian Karrer` (person)
- `Obere Amtshausgasse 26, 4591 Rosenau am Hengstpaß, Österreich` (address)
- `Grazer Treuhand Steuerberatung GmbH & Partner KG` (organisation)
- `Petersgasse 128a, 8010 Graz` (address)
- `Finanzamts Graz-Stadt` (organisation)
- `Finanzamts Graz- Stadt` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/136623.1`) (sent_id: `findok-manually-annotated_TRAIN/136623.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Leya Gern  in der Beschwerdesache Ronja Hebestreit,  Fisching 29, 4083 Untergschwendt, Österreich, über die Beschwerde vom 27.06.2021 gegen den Bescheid des Finanzamtes  Österreich vom 9. Juni 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer 14-107/0761  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ronja Hebestreit` | `Ronja Hebestreit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Leya Gern` (person)
- `Fisching 29, 4083 Untergschwendt, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `14-107/0761` (tax_number)

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/135536.1`) (sent_id: `findok-manually-annotated_TRAIN/135536.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Florentine Beumers, Krischgasse 309, 4113 Windischberg, Österreich, über die Beschwerde vom 20. Februar 2020 gegen den Bescheid  des Finanzamtes Österreich vom 16. Jänner 2020 betreffend Familienbeihilfe 01.2020  Steuernummer 58-742/0765, SVNR 8800 110262, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Florentine Beumers` | `Florentine Beumers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Krischgasse 309, 4113 Windischberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `58-742/0765` (tax_number)
- `8800 110262` (social_security_number)

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/138550.1`) (sent_id: `findok-manually-annotated_TRAIN/138550.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Eberhard Kreislmeier  in der Beschwerdesache Vera Soldtwedel,  Gaas 20, 3494 Schlickendorf, Österreich, betreffend Beschwerde vom 15. April 2022 gegen den Bescheid des  Finanzamtes Österreich vom 1. April 2022 betreffend Mehrkindzuschlag 2021 zur  Steuernummer 39-381/5653  beschlossen:  I. Die Parteien werden gemäß § 281a BAO formlos darüber verständigt, dass nach Auffassung  des Bundesfinanzgerichtes ein Vorlageantrag nicht eingebracht wurde.

| Predicted | Gold |
|---|---|
| `Vera Soldtwedel` | `Vera Soldtwedel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Eberhard Kreislmeier` (person)
- `Gaas 20, 3494 Schlickendorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `39-381/5653` (tax_number)
- `Bundesfinanzgerichtes` (organisation)

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/138550.1`) (sent_id: `findok-manually-annotated_TRAIN/138550.1_48`)


IV. Formlose Verständigung gemäß § 281a BAO:  Das Bundesfinanzgericht ist in der Beschwerdesache Vera Soldtwedel (Gaas 20, 3494 Schlickendorf, Österreich) zur Beschwerde  vom 15. April 2022 gegen den Bescheid des Finanzamtes Österreich vom 1. April 2022  4 von 6 Seite 5 von 6

| Predicted | Gold |
|---|---|
| `Vera Soldtwedel` | `Vera Soldtwedel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gaas 20, 3494 Schlickendorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/138586.1`) (sent_id: `findok-manually-annotated_TRAIN/138586.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Verena Gephardt  in der Beschwerdesache Laurentia Ahrendtz,  Gschwendt 7, 2640 Wörth, Österreich, betreffend Beschwerde vom 15. März 2021 gegen den Bescheid des  Finanzamtes Österreich vom 27. Februar 2017 hinsichtlich Einkommensteuer  (Arbeitnehmerveranlagung) 2016, Steuernummer 21-921/6236, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Laurentia Ahrendtz` | `Laurentia Ahrendtz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Verena Gephardt` (person)
- `Gschwendt 7, 2640 Wörth, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `21-921/6236` (tax_number)

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/138587.1`) (sent_id: `findok-manually-annotated_TRAIN/138587.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Laurentia Siemes  in der Beschwerdesache Ada Pawelski,  Erich-Kandel-Straße 101, 3564 Oberplank, Österreich, betreffend Beschwerde vom 15. März 2021 gegen die Bescheide des  Finanzamtes Österreich vom 8. März 2018 und 18. November 2019 hinsichtlich  Einkommensteuer (Arbeitnehmerveranlagung) 2017  und Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Steuernummer 32-400/6426, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ada Pawelski` | `Ada Pawelski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Laurentia Siemes` (person)
- `Erich-Kandel-Straße 101, 3564 Oberplank, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `32-400/6426` (tax_number)

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) (sent_id: `findok-manually-annotated_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Konstanze Bertling` | `Konstanze Bertling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Jacqueline Bruemmer` (person)
- `Pabstbergstraße 45, 9135 Unterort, Österreich` (address)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `Finanzamt Österreich` (organisation)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `Finanzamt Österreich` (organisation)
- `88-575/7122` (tax_number)

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/140056.1`) (sent_id: `findok-manually-annotated_TRAIN/140056.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache   Emanuela Wilgen, Kölnhofsiedlung 12, 5622 Mitterstein, Österreich, über die Beschwerde vom 1. Juni 2022 gegen den Bescheid des  Finanzamtes Österreich vom 5. Mai 2022 betreffend Rückforderung von für Hademar Peschek  für  den Zeitraum Oktober 2021 bis Februar 2022 bezogener Beträge an Familienbeihilfe und  Kinderabsetzbetrag, Steuernummer 06-892/6489 (7083181213) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Emanuela Wilgen` | `Emanuela Wilgen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kölnhofsiedlung 12, 5622 Mitterstein, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Hademar Peschek` (person)
- `06-892/6489` (tax_number)
- `7083181213` (social_security_number)

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/140853.1`) (sent_id: `findok-manually-annotated_TRAIN/140853.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Juri Jonkhans  in der Beschwerdesache KommR Ulrich Maader,  Prangergasse 2, 5323 Hinterebenau, Österreich, vertreten durch Dr. Anton Herbert Pochieser, Schottenfeldgasse 2-4 Tür 23,  Wien 1070, betreffend die Beschwerde vom 29.09.2021 gegen den Bescheid des  Finanzamtes  Österreich vom 27. August 2021, mit welchem die Aussetzung der Entscheidung gem. § 271  BAO betreffend die Beschwerde vom 18.01.2021 gegen den Abweisungsbescheid vom  10.12.2020 (Ausgleichszahlung) verfügt wurde, zu SVNr.

| Predicted | Gold |
|---|---|
| `KommR Ulrich Maader` | `KommR Ulrich Maader` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Juri Jonkhans` (person)
- `Prangergasse 2, 5323 Hinterebenau, Österreich` (address)
- `Dr. Anton Herbert Pochieser` (person)
- `Schottenfeldgasse 2-4 Tür 23,  Wien 1070` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/143368.1`) (sent_id: `findok-manually-annotated_TRAIN/143368.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Karlheinz Parlak  in der Beschwerdesache  Melinda Krebsz, Zauchmühle 136, 2463 Gallbrunn, Österreich, über die Beschwerde vom 8. Mai 2023 gegen den Bescheid des  Finanzamtes Österreich vom 27. April 2023 betreffend Einkommensteuer 2022 zur  Steuernummer 60-281/5380  zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Melinda Krebsz` | `Melinda Krebsz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Karlheinz Parlak` (person)
- `Zauchmühle 136, 2463 Gallbrunn, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `60-281/5380` (tax_number)

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/144169.1`) (sent_id: `findok-manually-annotated_TRAIN/144169.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache   Felizia Ponsong, Georg-von-Trapp-Straße 66, 8243 Sparberegg, Österreich, über die Beschwerde vom 29. Juli 2023 gegen den Bescheid des  Finanzamtes Österreich vom 6. Juli 2023 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbetrag für den Zeitraum Oktober 2022 bis Juni 2023, Steuernummer  68-038/3701 (SVNR 8332180970), zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Felizia Ponsong` | `Felizia Ponsong` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Georg-von-Trapp-Straße 66, 8243 Sparberegg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `68-038/3701` (tax_number)
- `8332180970` (social_security_number)

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/145534.1`) (sent_id: `findok-manually-annotated_TRAIN/145534.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Juliana Kleppel  in der Beschwerdesache des  HR Christian Styrnal, Babenbergersee I 18, 5524 Hallseiten, Österreich  vertreten durch TPA STB Wien GmbH Wien, Wiedner Gürtel 13,  Turm 24, 1100 Wien, über die Beschwerde vom 23. Jänner 2012 gegen die Bescheide des FA  Wien 9/18/19 Klosterneuburg (nunmehr Finanzamt Österreich) vom 21. Dezember 2011  betreffend Einkommensteuer 2001 bis 2003, Steuernummer 60-008/3417, zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `HR Christian Styrnal` | `HR Christian Styrnal` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Juliana Kleppel` (person)
- `Babenbergersee I 18, 5524 Hallseiten, Österreich` (address)
- `TPA STB Wien GmbH` (organisation)
- `Wiedner Gürtel 13,  Turm 24, 1100 Wien` (address)
- `FA  Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamt Österreich` (organisation)
- `60-008/3417` (tax_number)

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/146072.1`) (sent_id: `findok-manually-annotated_TRAIN/146072.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Univ.-Prof. Hartwig Boehler  in der Beschwerdesache DDr.in Josepha de Haan,  Oisching 129, 3071 Wiesen, Österreich, vertreten durch Merkur Treuhand Steuerberatung GmbH, St.-Veit-Gasse 50,  1130 Wien, über die Beschwerde vom 16. Mai 2024 gegen den Bescheid des Finanzamtes  Österreich vom 13. Mai 2024 betreffend Abrechnung gem. § 216 BAO Steuernummer  01-186/7053  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und festgestellt, dass die  Umbuchung des per 3.4.2024 auf dem Abgabenkonto der Beschwerdeführerin bestehenden  Guthabens i.H.v. € 166.146,40 auf Finanzverwahrnisse unrichtig war.

| Predicted | Gold |
|---|---|
| `DDr.in Josepha de Haan` | `DDr.in Josepha de Haan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Univ.-Prof. Hartwig Boehler` (person)
- `Oisching 129, 3071 Wiesen, Österreich` (address)
- `Merkur Treuhand Steuerberatung GmbH` (organisation)
- `St.-Veit-Gasse 50,  1130 Wien` (address)
- `Finanzamtes  Österreich` (organisation)
- `01-186/7053` (tax_number)

**Example 16** (doc_id: `findok-manually-annotated_TRAIN/146878.1`) (sent_id: `findok-manually-annotated_TRAIN/146878.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Dr. Wiebke Peperkorn in der  Beschwerdesache Sophie Zekalla, Benedikt-Stampfl-Weg 17, 8122 Waldstein, Österreich, über die Beschwerde vom 29. April 2024 gegen  den Bescheid des Finanzamtes Österreich vom 24. April 2024 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2023 Steuernummer 71-479/6461  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Sophie Zekalla` | `Sophie Zekalla` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dr. Wiebke Peperkorn` (person)
- `Benedikt-Stampfl-Weg 17, 8122 Waldstein, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `71-479/6461` (tax_number)

**Example 17** (doc_id: `findok-manually-annotated_TRAIN/146849.1`) (sent_id: `findok-manually-annotated_TRAIN/146849.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Evelyn Sedlmayr, Ebener Straße 25, 5201 Seewalchen, Österreich, über die Beschwerde vom 2. April 2024 gegen den Bescheid des Finanzamtes  Österreich vom 20. März 2024 betreffend Rückforderung von für die Kinder Evelyn Boediker  und  Merlin Leutholdt  für den Zeitraum Juni 2022 bis Juli 2023 bezogenen Beträgen an Familienbeihilfe  (Differenz-/Ausgleichszahlungen), Steuernummer 50-831/8746 (SVNR 2154030383) zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Evelyn Sedlmayr` | `Evelyn Sedlmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ebener Straße 25, 5201 Seewalchen, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `Evelyn Boediker` (person)
- `Merlin Leutholdt` (person)
- `50-831/8746` (tax_number)
- `2154030383` (social_security_number)

**Example 18** (doc_id: `findok-manually-annotated_TRAIN/148615.1`) (sent_id: `findok-manually-annotated_TRAIN/148615.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache   Nicola Happl, Unterfarracher Straße 34, 9542 Berg ob Afritz, Österreich, über die Beschwerde vom 18. November 2024 gegen den Bescheid  des Finanzamtes Österreich vom 21. Oktober 2024 betreffend Abweisung des Antrages auf  Familienbeihilfe vom 10. September 2024 für Delila Hofsäß  ab September 2024,  Steuernummer 20-702/2840 (SVNR 8634 041244), zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Nicola Happl` | `Nicola Happl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Unterfarracher Straße 34, 9542 Berg ob Afritz, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Delila Hofsäß` (person)
- `20-702/2840` (tax_number)
- `8634 041244` (social_security_number)

**Example 19** (doc_id: `findok-manually-annotated_TRAIN/148648.1`) (sent_id: `findok-manually-annotated_TRAIN/148648.1_2`)


Alexander Beißer in der  Beschwerdesache Bernhard Siegmundt, Grabental 83, 9300 Goggerwenig, Österreich, über die Beschwerde vom 4. März 2024  gegen den Bescheid des Finanzamtes Österreich vom 1. März 2024 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2023 Steuernummer 61-582/6966  zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

**Missed by this rule (FN):**

- `Grabental 83, 9300 Goggerwenig, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `61-582/6966` (tax_number)

**Example 20** (doc_id: `findok-manually-annotated_TRAIN/148650.1`) (sent_id: `findok-manually-annotated_TRAIN/148650.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache   Agatha Vesper, Albersdorfweg 21, 4973 Rabenfurt, Österreich, betreffend Beschwerde vom 9. Juli 2024 gegen den Bescheid des  Finanzamtes Österreich vom 17. Juni 2024 betreffend Abweisung des Antrages vom  31. Jänner 2024 auf den Erhöhungsbetrag zur Familienbeihilfe ab Jänner 2024, Steuernummer  58-042/7990 (SVNR 6155 130467), beschlossen:   Der Vorlageantrag vom 20. November 2024 wird gemäß § 260 Abs. 1 lit. b  Bundesabgabenordnung (BAO) iVm § 264 Abs. 4 lit. e BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Agatha Vesper` | `Agatha Vesper` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Albersdorfweg 21, 4973 Rabenfurt, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `58-042/7990` (tax_number)
- `6155 130467` (social_security_number)

**Example 21** (doc_id: `findok-manually-annotated_TRAIN/149270.1`) (sent_id: `findok-manually-annotated_TRAIN/149270.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Univ.-Prof.in Lynn Tscherwenka  in der Beschwerdesache Lydia Alexandridis,  Major-Trojer-Weg 132, 8345 Straden, Österreich, über die Beschwerde vom 28. März 2025 gegen den Bescheid des FA Klosterneuburg  vom 13. März 2025 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2024,  Steuernummer 67-606/3958, zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Lydia Alexandridis` | `Lydia Alexandridis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Univ.-Prof.in Lynn Tscherwenka` (person)
- `Major-Trojer-Weg 132, 8345 Straden, Österreich` (address)
- `FA Klosterneuburg` (organisation)
- `67-606/3958` (tax_number)

**Example 22** (doc_id: `findok-manually-annotated_TRAIN/149284.1`) (sent_id: `findok-manually-annotated_TRAIN/149284.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Bartholomäus Ficke  in der Beschwerdesache Ophelia Hinnemann,  Weizerstraße 8, 9615 Görtschach, Österreich, vertreten durch Paugger Steuerberatung GmbH, Wollzeile 18 Tür 16, 1010  Wien, wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Österreich  betreffend Untätigkeit bei der Erledigung der Außenprüfung für die 2020 bis 2022 den  Beschluss:  I. Die Beschwerde gilt hinsichtlich der Jahre 2020 bis 2022 gemäß § 85 Abs. 2 BAO als  zurückgenommen.

| Predicted | Gold |
|---|---|
| `Ophelia Hinnemann` | `Ophelia Hinnemann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Bartholomäus Ficke` (person)
- `Weizerstraße 8, 9615 Görtschach, Österreich` (address)
- `Paugger Steuerberatung GmbH` (organisation)
- `Wollzeile 18 Tür 16, 1010  Wien` (address)
- `Finanzamt Österreich` (organisation)

**Example 23** (doc_id: `findok-manually-annotated_TRAIN/149301.1`) (sent_id: `findok-manually-annotated_TRAIN/149301.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Annalena Spatzier, Bahnhof Krottenbachstraße 4, 3130 Unterwinden, Österreich, über die Beschwerde vom 21. März 2024 gegen  den Bescheid des Finanzamtes Österreich vom 22. Februar 2024 betreffend Einkommensteuer  2018, Steuernummer 78-848/2763, zu Recht erkannt:   I. Der angefochtene Bescheid wird ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Annalena Spatzier` | `Annalena Spatzier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ansgar Unterberger` (person)
- `Bahnhof Krottenbachstraße 4, 3130 Unterwinden, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `78-848/2763` (tax_number)

**Example 24** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) (sent_id: `findok-manually-annotated_TRAIN/149280.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Zwilling in der Beschwerdesache  Ferdinand Mielnickel, Viertelweg 16, 3720 Gaindorf, Österreich, vertreten durch Hallas & Partner Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG, Praterstraße 38, 1020 Wien, über die Beschwerde vom  30. November 2017 gegen die Bescheide des Finanzamtes Baden Mödling (nunmehr Finanzamt  Österreich) vom 31. Oktober 2017 betreffend Festsetzung eines Verspätungszuschlages  betreffend Einkommensteuer 2015 und 2016 und Umsatzsteuer 2015 und 2016,  Steuernummer 86-167/7419  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ferdinand Mielnickel` | `Ferdinand Mielnickel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Zwilling` (person)
- `Viertelweg 16, 3720 Gaindorf, Österreich` (address)
- `Hallas & Partner Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG` (organisation)
- `Praterstraße 38, 1020 Wien` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `Finanzamt  Österreich` (organisation)
- `86-167/7419` (tax_number)

**Example 25** (doc_id: `findok-manually-annotated_TRAIN/149322.1`) (sent_id: `findok-manually-annotated_TRAIN/149322.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache HR KzlR Stephanie Ganssloser, Schwemmgasse 16, 8992 Fischerndorf, Österreich, betreffend Beschwerde vom 8. April 2025 gegen  den Bescheid des Finanzamtes Österreich vom 10. März 2025 betreffend Säumniszuschlag  10.03.2025 zur Steuernummer 16-527/7844  beschlossen:   Die Beschwerde vom 8. April 2025 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `HR KzlR Stephanie Ganssloser` | `HR KzlR Stephanie Ganssloser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Schwemmgasse 16, 8992 Fischerndorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `16-527/7844` (tax_number)

**Example 26** (doc_id: `findok-manually-annotated_TRAIN/149309.1`) (sent_id: `findok-manually-annotated_TRAIN/149309.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Julia Terbofen, Treidlerstraße 2, 3820 Reith, Österreich, Steuernummer 31-441/2585, über die Beschwerde vom  9. Dezember 2024 gegen den Bescheid des Finanzamtes Österreich vom 22. November 2024  betreffend Festsetzung von Anspruchszinsen 2023 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Julia Terbofen` | `Julia Terbofen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Peter Bilger` (person)
- `Treidlerstraße 2, 3820 Reith, Österreich` (address)
- `31-441/2585` (tax_number)
- `Finanzamtes Österreich` (organisation)

**Example 27** (doc_id: `findok-manually-annotated_TRAIN/149316.1`) (sent_id: `findok-manually-annotated_TRAIN/149316.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Siegbert Höweltewes  in der Beschwerdesache Xenia Lukoszek,  Nußbaumallee 23, 9556 Sörg, Österreich, über die Beschwerde vom 22. Dezember 2017 gegen die Bescheide des  Finanzamt Innsbruck  vom 5. Dezember 2017 betreffend Festsetzung der   Normverbrauchsabgabe für April 2014 (4.338,82 €) und Kraftfahrzeugsteuer für die  Zeiträume 4 - 12/2014 (608,26 €) und 1 - 9/2015 (684,29 €) sowie    Normverbrauchsabgabe für September 2015 (11.193,28 €) und Kraftfahrzeugsteuer für  die Zeiträume 10 - 12/2015 (574,60 €), 1 - 12/2016 (2.298,38) und 1 - 9/2017 (1.723,79  €)   Normverbrauchsabgabe für Oktober 2017 (20.414,12 €) und Kraftfahrzeugsteuer für die  Zeiträume 10 - 12/2017 (240 €), 1 - 12/2018 (960 €) und 1 - 8/2019 (640 €),  zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Xenia Lukoszek` | `Xenia Lukoszek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Siegbert Höweltewes` (person)
- `Nußbaumallee 23, 9556 Sörg, Österreich` (address)
- `Finanzamt Innsbruck` (organisation)

**Example 28** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) (sent_id: `findok-manually-annotated_TRAIN/149418.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hartwig Daxlberger  in der Beschwerdesache Arnd Ehrlein,  Schloßwiesen 332, 5651 Heuberg, Österreich  vertreten durch Ernst & Young Steuerberatungs-GmbH, Wagramer Straße 19,  1220 Wien über die Beschwerde vom 1. Oktober 2025 gegen den Bescheid des Finanzamtes für  Großbetriebe vom 2. September 2025 betreffend Stabilitätsabgabe 2024 Steuernummer  44-182/2731  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Arnd Ehrlein` | `Arnd Ehrlein` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hartwig Daxlberger` (person)
- `Schloßwiesen 332, 5651 Heuberg, Österreich` (address)
- `Ernst & Young Steuerberatungs-GmbH` (organisation)
- `Wagramer Straße 19,  1220 Wien` (address)
- `44-182/2731` (tax_number)

**Example 29** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) (sent_id: `findok-manually-annotated_TRAIN/149404.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johann Fischerlehner in der  Beschwerdesache Veronika Ogrissek, Weißeneggerberg 160, 3631 Kienings, Österreich, über die Beschwerde vom 23. September 2024  gegen die Bescheide des Finanzamtes Österreich vom 16. September 2024 betreffend  Pfändung einer Geldforderung und Verfügungsverbot zu Steuernummer 48-541/5488  zu  Recht erkannt:   I. Die Beschwerde gegen den Bescheid betreffend Pfändung einer Geldforderung wird  als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Veronika Ogrissek` | `Veronika Ogrissek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Johann Fischerlehner` (person)
- `Weißeneggerberg 160, 3631 Kienings, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `48-541/5488` (tax_number)

**Example 30** (doc_id: `findok-manually-annotated_TRAIN/149424.1`) (sent_id: `findok-manually-annotated_TRAIN/149424.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Franka Bartolomey, Feisterweg 11, 8321 St. Margarethen an der Raab, Österreich, über die Beschwerde vom 13. Mai 2024 gegen den Bescheid des  Finanzamtes Österreich vom 29. April 2024 betreffend Einkommensteuer 2023, 82-102/0439,  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Franka Bartolomey` | `Franka Bartolomey` |

**Missed by this rule (FN):**

- `Dr. Peter Steurer` (person)
- `Feisterweg 11, 8321 St. Margarethen an der Raab, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `82-102/0439` (tax_number)

**Example 31** (doc_id: `findok-manually-annotated_TRAIN/149430.1`) (sent_id: `findok-manually-annotated_TRAIN/149430.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Lisa Pucher in der Beschwerdesache  Sebastian Nathansen, Neuhofenstraße 10, 8970 Preunegg, Österreich, vertreten durch Michael Walter Nierla, Annagasse 5/2/15, 1010  Wien, über die Beschwerde vom 7. September 2023 gegen den Bescheid des Finanzamtes  Österreich vom 7. August 2023, mit dem ein Antrag auf Aufschiebung der Vollstreckung gemäß  § 18 Z 1 AbgEO abgewiesen wurde, zu Steuernummer 46-406/1806, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Sebastian Nathansen` | `Sebastian Nathansen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Lisa Pucher` (person)
- `Neuhofenstraße 10, 8970 Preunegg, Österreich` (address)
- `Michael Walter Nierla` (person)
- `Annagasse 5/2/15, 1010  Wien` (address)
- `Finanzamtes  Österreich` (organisation)
- `46-406/1806` (tax_number)

**Example 32** (doc_id: `findok-manually-annotated_TRAIN/149445.1`) (sent_id: `findok-manually-annotated_TRAIN/149445.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Mag. Gertraud Hausherr in der  Beschwerdesache Ottfried Herbener, Am See VI 5, 5441 Lindenthal, Österreich, vertreten durch BKS Steuerberatung GmbH & Co  KG, Handelsstraße 8/Stiege 2/Top 2, 3130 Herzogenburg, betreffend Beschwerde vom  24. Oktober 2023 gegen den Bescheid des Finanzamtes Österreich vom 28. September 2023  betreffend Einkommensteuer 2021 Steuernummer 04-621/0728  beschlossen:   Die Beschwerde vom 24. Oktober 2023 wird gemäß § 256 Abs. 3 BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Ottfried Herbener` | `Ottfried Herbener` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gertraud Hausherr` (person)
- `Am See VI 5, 5441 Lindenthal, Österreich` (address)
- `BKS Steuerberatung GmbH & Co  KG` (organisation)
- `Handelsstraße 8/Stiege 2/Top 2, 3130 Herzogenburg` (address)
- `Finanzamtes Österreich` (organisation)
- `04-621/0728` (tax_number)

**Example 33** (doc_id: `findok-manually-annotated_TRAIN/149390.1`) (sent_id: `findok-manually-annotated_TRAIN/149390.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Priv.-Doz. Timon Jestrzemski  in der Beschwerdesache Othmar Arvanitidis,  Schrödlgasse 19, 4924 Höschmühl, Österreich, über die Beschwerde vom 23. Mai 2017 gegen den Bescheid -  Sicherstellungsauftrag des Finanzamtes FA (nunmehr FA Braunau Ried Schärding) vom 18. April 2017,  Steuernummer 71-450/0461, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Othmar Arvanitidis` | `Othmar Arvanitidis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Priv.-Doz. Timon Jestrzemski` (person)
- `Schrödlgasse 19, 4924 Höschmühl, Österreich` (address)
- `FA Braunau Ried Schärding` (organisation)
- `71-450/0461` (tax_number)

**Example 34** (doc_id: `findok-manually-annotated_TRAIN/149497.1`) (sent_id: `findok-manually-annotated_TRAIN/149497.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  James Grentz, Katharine-Drexel-Straße 5, 3661 Lohsdorf, Österreich, vertreten durch T & M TRAUNSTEINER U. MITTERER KG,  Schubertviertel 38, 4300 St.Valentin, betreffend Beschwerde vom 16. Mai 2024 gegen den  Bescheid des Finanzamtes Österreich vom 7. Mai 2024 betreffend Anspruchszinsen (§ 205  BAO) 2022 (Einkommensteuer) Steuernummer 90-523/9682  beschlossen:  Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO für gegenstandlos erklärt.

| Predicted | Gold |
|---|---|
| `James Grentz` | `James Grentz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Katharine-Drexel-Straße 5, 3661 Lohsdorf, Österreich` (address)
- `T & M TRAUNSTEINER U. MITTERER KG` (organisation)
- `Schubertviertel 38, 4300 St.Valentin` (address)
- `Finanzamtes Österreich` (organisation)
- `90-523/9682` (tax_number)

**Example 35** (doc_id: `findok-manually-annotated_TRAIN/149462.1`) (sent_id: `findok-manually-annotated_TRAIN/149462.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Ashley Ditges  in der Beschwerdesache Willibald Urbanowicz,  Caritasstraße 286, 3920 Heinreichs, Österreich, vertreten durch Lenfeld/Leys/Sonderegger Rechtsanwälte, Malserstraße 19,  6500 Landeck, über die Beschwerde vom 14. Dezember 2023 gegen den Bescheid des  Finanzamtes Österreich vom 14. November 2023 betreffend Rückforderung von  Familienbeihilfe und Kinderabsetzbeträgen für die Monate Oktober 2021 bis Jänner 2022,  Steuernummer 83-447/1877,  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Willibald Urbanowicz` | `Willibald Urbanowicz` |

**Missed by this rule (FN):**

- `Priv.-Doz. Ashley Ditges` (person)
- `Caritasstraße 286, 3920 Heinreichs, Österreich` (address)
- `Lenfeld/Leys/Sonderegger Rechtsanwälte` (organisation)
- `Malserstraße 19,  6500 Landeck` (address)
- `Finanzamtes Österreich` (organisation)
- `83-447/1877` (tax_number)

**Example 36** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) (sent_id: `findok-manually-annotated_TRAIN/149473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Pawel Heldt  in der Beschwerdesache  Samir Krahnepuhl, Webersberg 40, 7331 Kalkgruben, Österreich, über die Beschwerde vom 18. September 2023 gegen den  Bescheid des Finanzamtes Österreich vom 7. September 2023 betreffend Abweisung des  Antrags auf Wiedereinsetzung in den vorigen Stand vom 5. August 2023, Steuernummer  88-903/5443, zu Recht:   I. Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Samir Krahnepuhl` | `Samir Krahnepuhl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Pawel Heldt` (person)
- `Webersberg 40, 7331 Kalkgruben, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `88-903/5443` (tax_number)

**Example 37** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) (sent_id: `findok-manually-annotated_TRAIN/149505.1_2`)


Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Fabienne Jostl, Aufschließungsweg Löx Gründe Tschierweg 3, 9862 Vorderkrems, Österreich  vertreten durch Deloitte Tax Wirtschaftsprüfungs  GmbH, Renngasse/Freyung 1, 1013 Wien, über die Beschwerden gegen die Bescheide des  Finanzamtes Österreich vom 5.11.2024 und 26.5.2025 betreffend Umsatzsteuer 2022 und 2023  zu Recht erkannt (Steuernummer 81-450/8995):   I. Die Beschwerdevorentscheidungen des Finanzamtes Österreich vom 17.7.2025, mit  welchen über die Beschwerden gegen die Bescheide des Finanzamtes für Großbetriebe  vom 5.11.2024 (USt 2022) und 26.5.2025 (USt 2023) abgesprochen wurde, werden  wegen Unzuständigkeit der bescheiderlassenden Behörde aufgehoben.

| Predicted | Gold |
|---|---|
| `Fabienne Jostl` | `Fabienne Jostl` |

**Missed by this rule (FN):**

- `Aufschließungsweg Löx Gründe Tschierweg 3, 9862 Vorderkrems, Österreich` (address)
- `Deloitte Tax Wirtschaftsprüfungs  GmbH` (organisation)
- `Renngasse/Freyung 1, 1013 Wien` (address)
- `Finanzamtes Österreich` (organisation)
- `81-450/8995` (tax_number)
- `Finanzamtes Österreich` (organisation)

**Example 38** (doc_id: `findok-manually-annotated_TRAIN/149682.1`) (sent_id: `findok-manually-annotated_TRAIN/149682.1_1`)


BESCHLUSS  Das Bundesfinanzgericht beschließt durch den Richter Mag. David Hell LL.B. LL.M. in der  Beschwerdesache Ingolf Johannisbauer, Hochtregister Straße 44, 9560 Weit, Österreich, vertreten durch Dr. Michael Kotschnigg,  Stadlauer Straße 39/I/12, 1220 Wien, betreffend Beschwerde vom 16. Mai 2023 (eingebracht  am 1. September 2025) gegen den Bescheid des Finanzamtes Österreich vom 21. April 2023  betreffend Zurückweisung eines Antrages auf Festsetzung von Umsatzsteuerzinsen gemäß  § 205c BAO, Steuernummer 08-788/8579:  I. Die Beschwerde wird als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ingolf Johannisbauer` | `Ingolf Johannisbauer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. David Hell LL.B. LL.M.` (person)
- `Hochtregister Straße 44, 9560 Weit, Österreich` (address)
- `Dr. Michael Kotschnigg` (person)
- `Stadlauer Straße 39/I/12, 1220 Wien` (address)
- `Finanzamtes Österreich` (organisation)
- `08-788/8579` (tax_number)

**Example 39** (doc_id: `findok-manually-annotated_TRAIN/149687.1`) (sent_id: `findok-manually-annotated_TRAIN/149687.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Delia Fürniß  in der Beschwerdesache PhD OMedR Ada Segert,  Gschlößlgasse 2, 5542 Flachau, Österreich, vertreten durch Vertreter, Adresse Vertreter, über die Säumnisbeschwerde der  beschwerdeführenden Partei vom 4. September 2025 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Österreich betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für das Jahr 2023, Steuernummer xx-xxx/xxxx, beschlossen:  Das Säumnisbeschwerdeverfahren wird eingestellt.

| Predicted | Gold |
|---|---|
| `PhD OMedR Ada Segert` | `PhD OMedR Ada Segert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Delia Fürniß` (person)
- `Gschlößlgasse 2, 5542 Flachau, Österreich` (address)
- `Finanzamt Österreich` (organisation)

**Example 40** (doc_id: `findok-manually-annotated_TRAIN/149708.1`) (sent_id: `findok-manually-annotated_TRAIN/149708.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht fasst durch die Richterin Mag. Lisa Fries in der Revisionssache  Donald Kurun, Röcklbrunnstraße 21, 5222 Valentinhaft, Österreich, vertreten durch Eckhardt SteuerberatungsgmbH, Hauptstraße 58,  7033 Pöttsching, über den Antrag der Revisionswerberin der Revision vom 13. November 2025  gegen das Erkenntnis des Bundesfinanzgerichtes vom 29. September 2025, RV/7103756/2024,  betreffend Abweisung einer Nachsicht, die aufschiebende Wirkung zuzuerkennen, den  Beschluss:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

| Predicted | Gold |
|---|---|
| `Donald Kurun` | `Donald Kurun` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Lisa Fries` (person)
- `Röcklbrunnstraße 21, 5222 Valentinhaft, Österreich` (address)
- `Eckhardt SteuerberatungsgmbH` (organisation)
- `Hauptstraße 58,  7033 Pöttsching` (address)
- `Bundesfinanzgerichtes` (organisation)

**Example 41** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) (sent_id: `findok-manually-annotated_TRAIN/149683.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Univ.-Prof.in Marion Bomarius  in der Beschwerdesache Norbert Ribarczik,  Zufahrt Felbermayr 68, 9241 Neudorf, Österreich, vertreten durch Dr. Roland Gabl Rechtsanwalts- Kommandit-Partnerschaft,  Museumstraße 31a, 4020 Linz, über die Beschwerde vom 3. Jänner 2024 gegen den  Einkommensteuerbescheid des Finanzamtes Österreich vom 23. November 2023 betreffend  Berichtigung gem. § 293b BAO zu Bescheid vom 21.11.2023 Steuernummer 71-595/2950  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Norbert Ribarczik` | `Norbert Ribarczik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Univ.-Prof.in Marion Bomarius` (person)
- `Zufahrt Felbermayr 68, 9241 Neudorf, Österreich` (address)
- `Dr. Roland Gabl Rechtsanwalts- Kommandit-Partnerschaft` (organisation)
- `Museumstraße 31a, 4020 Linz` (address)
- `Finanzamtes Österreich` (organisation)
- `71-595/2950` (tax_number)

**Example 42** (doc_id: `findok-manually-annotated_TRAIN/149741.1`) (sent_id: `findok-manually-annotated_TRAIN/149741.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Lisa Fries in der Beschwerdesache  Corvin Diebald, Pitzelstätten 4, 2490 Ebenfurth, Österreich, vertreten durch Dr. Ronald Rödler, Lagerstraße 5/1/20, 2460  Bruck/Leitha über die Beschwerde vom 11. Oktober 2019 gegen den Bescheid des Finanzamtes  Neunkirchen Wr. Neustadt (nunmehr Finanzamt Österreich) vom 11. September 2019  betreffend Aussetzung gemäß § 212a BAO zu Recht:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Corvin Diebald` | `Corvin Diebald` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Lisa Fries` (person)
- `Pitzelstätten 4, 2490 Ebenfurth, Österreich` (address)
- `Dr. Ronald Rödler` (person)
- `Lagerstraße 5/1/20, 2460  Bruck/Leitha` (address)
- `Finanzamtes  Neunkirchen Wr. Neustadt` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 43** (doc_id: `findok-manually-annotated_TRAIN/149711.1`) (sent_id: `findok-manually-annotated_TRAIN/149711.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  Joseph Kramors, Planseestraße 8, 9833 Lamnitz, Österreich, über dessen Beschwerde vom 7. Februar 2025 gegen den Bescheid  des Finanzamtes Österreich vom 15. Jänner 2025 betreffend Anspruchszinsen (§ 205 BAO)  2022, Steuernummer 27-377/4888, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Joseph Kramors` | `Joseph Kramors` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andreas Stanek` (person)
- `Planseestraße 8, 9833 Lamnitz, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `27-377/4888` (tax_number)

**Example 44** (doc_id: `findok-manually-annotated_TRAIN/149749.1`) (sent_id: `findok-manually-annotated_TRAIN/149749.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Heidemarie Zangel, Furtmüllerstraße 66, 5142 Hehenberg, Österreich  vertreten durch die Mag. Ghesla Steuerberater GmbH, Kirchstraße 32,  6923 Lauterach, über die Beschwerden gegen die Bescheide des Finanzamtes Österreich  betreffend Einkommensteuer 2019 und 2020, 08-156/6554, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Heidemarie Zangel` | `Heidemarie Zangel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Furtmüllerstraße 66, 5142 Hehenberg, Österreich` (address)
- `Mag. Ghesla Steuerberater GmbH` (organisation)
- `Kirchstraße 32,  6923 Lauterach` (address)
- `Finanzamtes Österreich` (organisation)
- `08-156/6554` (tax_number)

**Example 45** (doc_id: `findok-manually-annotated_TRAIN/149765.1`) (sent_id: `findok-manually-annotated_TRAIN/149765.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Monika Ahorn in der Beschwerdesache  Irvin Altbauer, Kreuzfeldweg 69, 5272 Himmelschlag, Österreich, vertreten durch Dr. Thomas Krankl, Lerchenfelder Straße  120/2/28, 1080 Wien, über die Beschwerde vom 22. Jänner 2021 gegen den Bescheid des  Finanzamtes Österreich vom 13. Jänner 2021 Einkommensteuer (Arbeitnehmerveranlagung)  2019 (Steuernummer 18-845/4090 ) nach Durchführung einer mündlichen Verhandlung am  07.11.2025 in Anwesenheit des Schriftführers Dietmar Gratz  I. beschlossen:  Der Vorlageantrag vom 23.11.2022 wird als gegenstandslos erklärt (§ 85 Abs. 2 iVm § 256 Abs.  3 iVm § 264 Abs. 4 lit. d BAO).

| Predicted | Gold |
|---|---|
| `Irvin Altbauer` | `Irvin Altbauer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Monika Ahorn` (person)
- `Kreuzfeldweg 69, 5272 Himmelschlag, Österreich` (address)
- `Dr. Thomas Krankl` (person)
- `Lerchenfelder Straße  120/2/28, 1080 Wien` (address)
- `Finanzamtes Österreich` (organisation)
- `18-845/4090` (tax_number)
- `Dietmar Gratz` (person)

**Example 46** (doc_id: `findok-manually-annotated_TRAIN/149768.1`) (sent_id: `findok-manually-annotated_TRAIN/149768.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johann Fischerlehner in der  Beschwerdesache Siegmund Cofalke, Schürzbergweg, Thierbach 27, 8570 Bärnbach, Österreich, vertreten durch Mag. Elizabeta Koleva,  Karolinengasse 33 Tür 9, 1040 Wien, über die Beschwerde vom 28. Juli 2025 gegen den  Bescheid des Finanzamtes Österreich vom 4. Juni 2025 betreffend Abweisung eines Antrages  betreffend die Einkommensteuer 2023 zu Steuernummer 26-606/9835  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Siegmund Cofalke` | `Siegmund Cofalke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Johann Fischerlehner` (person)
- `Schürzbergweg, Thierbach 27, 8570 Bärnbach, Österreich` (address)
- `Mag. Elizabeta Koleva` (person)
- `Karolinengasse 33 Tür 9, 1040 Wien` (address)
- `Finanzamtes Österreich` (organisation)
- `26-606/9835` (tax_number)

**Example 47** (doc_id: `findok-manually-annotated_TRAIN/149763.1`) (sent_id: `findok-manually-annotated_TRAIN/149763.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Corinna Engenhart in der  Beschwerdesache Ulrich Grossehagenbrock, Hohenlehen 6, 9570 Alt-Ossiach, Österreich  über die Beschwerde vom 24. Jänner 2025 gegen  den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2023, Steuernummer 12-838/8904, zu Recht:   I. Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ulrich Grossehagenbrock` | `Ulrich Grossehagenbrock` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Corinna Engenhart` (person)
- `Hohenlehen 6, 9570 Alt-Ossiach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `12-838/8904` (tax_number)

**Example 48** (doc_id: `findok-manually-annotated_TRAIN/149801.1`) (sent_id: `findok-manually-annotated_TRAIN/149801.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Simon Schüttmeyer  in der Beschwerdesache Pawel Brodbecker,  Untergrödl 10, 9911 Vergein, Österreich, über die Beschwerde vom 28. April 2022 gegen die Bescheide des Finanzamtes  Österreich vom 11. April 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020  und 2021, Steuernummer 31-281/4248, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Pawel Brodbecker` | `Pawel Brodbecker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Simon Schüttmeyer` (person)
- `Untergrödl 10, 9911 Vergein, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `31-281/4248` (tax_number)

**Example 49** (doc_id: `findok-manually-annotated_TRAIN/149810.1`) (sent_id: `findok-manually-annotated_TRAIN/149810.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Adam Nietschl  in der Beschwerdesache Vincent Feidl,  Neumayrgasse 12, 9640 Würmlach, Österreich, vertreten durch Janina Ernicke, Bahnhof Liesing 3, 9065 Zell, Österreich, GF2***, Grabenholz 68, 4720 Würzberg, Österreich, und Saxinger  Chalupsky & Partner Rechtsanwälte GmbH, Böhmerwaldstraße 14, 4020 Linz, über die  Beschwerde vom 18. Oktober 2021 gegen den Bescheid des Finanzamtes Österreich vom 20.  September 2021 betreffend Zwangsstrafen 20.09.2021, Steuernummer 59-917/0690, nach  Durchführung einer mündlichen Verhandlung am 29. September 2025 zu Recht erkannt:    I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Vincent Feidl` | `Vincent Feidl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Adam Nietschl` (person)
- `Neumayrgasse 12, 9640 Würmlach, Österreich` (address)
- `Janina Ernicke` (person)
- `Bahnhof Liesing 3, 9065 Zell, Österreich` (address)
- `Grabenholz 68, 4720 Würzberg, Österreich` (address)
- `Saxinger  Chalupsky & Partner Rechtsanwälte GmbH` (organisation)
- `Böhmerwaldstraße 14, 4020 Linz` (address)
- `Finanzamtes Österreich` (organisation)
- `59-917/0690` (tax_number)

**Example 50** (doc_id: `findok-manually-annotated_TRAIN/149835.1`) (sent_id: `findok-manually-annotated_TRAIN/149835.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Raul Okyay  in der Beschwerdesache Volkmar Nemcova,  Tauplitz 86, 9346 Bach, Österreich, gegen den von der belangten Behörde Finanzamt Österreich am 9. Oktober  2024 zu Steuernummer 53-985/9991  ausgefertigten Bescheid betreffend  Einkommensteuer für das Jahr 2023 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Volkmar Nemcova` | `Volkmar Nemcova` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Raul Okyay` (person)
- `Tauplitz 86, 9346 Bach, Österreich` (address)
- `Finanzamt Österreich` (organisation)
- `53-985/9991` (tax_number)

**Example 51** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Gisbert Lindwedel, Penken 55, 4903 Hofmanning, Österreich, vertreten durch die Mag. Ghesla Steuerberater GmbH, Kirchstraße  32, 6923 Lauterach, über die Beschwerden gegen die Bescheide des Finanzamtes Bregenz  (nunmehr: Finanzamt Österreich) betreffend Einkommensteuer 2015 und 2016 sowie  Festsetzung von Vorauszahlungen an Einkommensteuer für 2017 sowie 2018 und Folgejahre,  85-106/2625, zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Gisbert Lindwedel` | `Gisbert Lindwedel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Penken 55, 4903 Hofmanning, Österreich` (address)
- `Mag. Ghesla Steuerberater GmbH` (organisation)
- `Kirchstraße  32, 6923 Lauterach` (address)
- `Finanzamtes Bregenz` (organisation)
- `Finanzamt Österreich` (organisation)
- `85-106/2625` (tax_number)

**Example 52** (doc_id: `findok-manually-annotated_TRAIN/149848.1`) (sent_id: `findok-manually-annotated_TRAIN/149848.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag.a Olivia Immes  in der Beschwerdesache  DDr. Willibald Hoffacker, Nockspitzweg 43, 6150 Stafflach, Österreich, über die Beschwerde vom 27. März 2024 gegen den Bescheid des  Finanzamtes Österreich vom 21. März 2024 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2021, Steuernummer 30-967/2512 :   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `DDr. Willibald Hoffacker` | `DDr. Willibald Hoffacker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Olivia Immes` (person)
- `Nockspitzweg 43, 6150 Stafflach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `30-967/2512` (tax_number)

**Example 53** (doc_id: `findok-manually-annotated_TRAIN/149863.1`) (sent_id: `findok-manually-annotated_TRAIN/149863.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Patrick Brandstetter in der  Beschwerdesache Wilma Kewer, Dr.-Adolf-Schärf-Straße 26, 2651 Mayerhöfen, Österreich, über die Beschwerde vom 17. August 2025  gegen den Bescheid des Finanzamtes Österreich vom 04. August 2025 betreffend die  Verzinsung der Rückerstattung gem. § 16 COFAG-NoAG (Steuernummer 45-588/1819 ) zu  Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Wilma Kewer` | `Wilma Kewer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Patrick Brandstetter` (person)
- `Dr.-Adolf-Schärf-Straße 26, 2651 Mayerhöfen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `45-588/1819` (tax_number)

**Example 54** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) (sent_id: `findok-manually-annotated_TRAIN/149861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Albert Sondersorg` | `Albert Sondersorg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Rut Frühoff` (person)
- `Eggenburger Gasse 7, 9121 Rakollach, Österreich` (address)
- `Deloitte Tax Wirtschaftsprüfungs GmbH` (organisation)
- `Renngasse  1/Freyung, 1010 Wien` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `Finanzamt Österreich` (organisation)
- `Finanzamtes Wien 1/23` (organisation)
- `Finanzamt Österreich` (organisation)
- `20-968/1669` (tax_number)

**Example 55** (doc_id: `findok-manually-annotated_TRAIN/149892.1`) (sent_id: `findok-manually-annotated_TRAIN/149892.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Louisa Kastan  in der Beschwerdesache des  Annette Lieschka, Würzberg 6, 3073 Mayerhöfen, Österreich, über die Beschwerde 25. September 2025 gegen die Bescheide  gemäß §§ 15 und 16 COFAG-NoAG des Finanzamt Klosterneuburg  6. August 2025 betreffend Rückerstattung  zum Fördervertrag Vorschuss auf den Fixkostenzuschuss 800.000 iRd Ausfallsbonus 01/2021,  Rückerstattung zum Fördervertrag Vorschuss auf den Fixkostenzuschuss 800.000 iRd  Ausfallsbonus 12/2020, Rückerstattung zum Fördervertrag Ausfallsbonus III 12/2021,  Rückerstattung zum Fördervertrag Ausfallsbonus III 11/2021, Rückerstattung zum  Fördervertrag Ausfallsbonus II 09/2021, Rückerstattung zum Fördervertrag Ausfallsbonus II  08/2021, Rückerstattung zum Fördervertrag Ausfallsbonus II 07/2021, Rückerstattung zum  Fördervertrag Ausfallsbonus 06/2021, Rückerstattung zum Fördervertrag Ausfallsbonus  05/2021, Rückerstattung zum Fördervertrag Ausfallsbonus 04/2021, Rückerstattung zum  Fördervertrag Ausfallsbonus 01/2021, Rückerstattung zum Fördervertrag Ausfallsbonus  12/2020, Rückerstattung zum Fördervertrag Ausfallsbonus 11/2020 und Verzinsung der  Rückerstattung, allesamt zu Steuernummer 65-634/0503, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Annette Lieschka` | `Annette Lieschka` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Louisa Kastan` (person)
- `Würzberg 6, 3073 Mayerhöfen, Österreich` (address)
- `Finanzamt Klosterneuburg` (organisation)
- `65-634/0503` (tax_number)

**Example 56** (doc_id: `findok-manually-annotated_TRAIN/149868.1`) (sent_id: `findok-manually-annotated_TRAIN/149868.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Günter Narat in der  Beschwerdesache Li Mazijewski, Bf-Adr, Ungarn, Steuernummer: 56-062/1596, über die  Beschwerde vom 25. Juni 2024 gegen den Bescheid des Finanzamtes Österreich vom 21. Juni  2024 betreffend Einkommensteuer 2023 zu Recht:  I)  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Li Mazijewski` | `Li Mazijewski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Günter Narat` (person)
- `Ungarn` (country)
- `56-062/1596` (tax_number)
- `Finanzamtes Österreich` (organisation)

**Example 57** (doc_id: `findok-manually-annotated_TRAIN/149874.1`) (sent_id: `findok-manually-annotated_TRAIN/149874.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Univ.-Prof. Emil Kilincarslan  in der Beschwerdesache Ida Broekhuis,  Ebnerwirtweg 22, 8282 Loipersdorf bei Fürstenfeld, Österreich, über die Beschwerde vom 25. April 2023 gegen die Bescheide des Finanzamtes  Österreich vom 5. April 2023 betreffend Familienbeihilfe 01.2018 und betreffend  Erhöhungsbetrag wegen erheblicher Behinderung ab Jänner 2018, Steuernummer  58-421/1804, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ida Broekhuis` | `Ida Broekhuis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Univ.-Prof. Emil Kilincarslan` (person)
- `Ebnerwirtweg 22, 8282 Loipersdorf bei Fürstenfeld, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `58-421/1804` (tax_number)

**Example 58** (doc_id: `findok-manually-annotated_TRAIN/149834.1`) (sent_id: `findok-manually-annotated_TRAIN/149834.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hedwig Kaszemeikat  in der Beschwerdesache  Erna Kaireit, Haibach im Mühlkreis, vertreten durch Peter Weinmar, Neudeggergasse 5 Tür 22, 1080  Wien, über die Beschwerde vom 11. Dezember 2019 gegen die Bescheide des Finanzamtes  Österreich vom 15. März 2019 betreffend Feststellung der Einkünfte § 188 BAO 2011 bis 2017  und betreffend Umsatzsteuer 2013 bis 2017 zu Steuernummer 91-046/2147  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Erna Kaireit` | `Erna Kaireit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Hedwig Kaszemeikat` (person)
- `Haibach im Mühlkreis` (city)
- `Peter Weinmar` (person)
- `Neudeggergasse 5 Tür 22, 1080  Wien` (address)
- `Finanzamtes  Österreich` (organisation)
- `91-046/2147` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/138410.1`) (sent_id: `findok-manually-annotated_TRAIN/138410.1_2`)


Gerald Erwin Ehgartner in der  Beschwerdesache Prof.in Klara Dolejsch, vertreten durch die Prof.in Tamara Simanek, über die Beschwerde vom 2.  November 2020 gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg (nunmehr  zuständig: Finanzamt Österreich) vom 9. September 2020 betreffend Abweisung des Antrags  auf Wiedereinsetzung in den vorigen Stand gemäß § 308 BAO zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Prof.in Klara Dolejsch,` — partial — gold is substring of pred: `Prof.in Klara Dolejsch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof.in Klara Dolejsch`(person)
- `Prof.in Tamara Simanek`(person)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_2`)


Gerald Erwin Ehgartner in der  Beschwerdesache Ronald Leinberger, vertreten durch Ernst & Young Steuerberatungsgesellschaft m.b.H.,  Wagramer Straße 19, 1220 Wien, über die Beschwerde vom 6. Dezember 2019 gegen die  Bescheide des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr  zuständig: Finanzamt Österreich) vom 31. Oktober 2019 betreffend Gebühren 2010 bis 2012 zu  Recht:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ronald Leinberger,` — partial — gold is substring of pred: `Ronald Leinberger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ronald Leinberger`(person)
- `Ernst & Young Steuerberatungsgesellschaft m.b.H.`(organisation)
- `Wagramer Straße 19, 1220 Wien`(address)
- `Finanzamt Österreich`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/140526.1`) (sent_id: `findok-manually-annotated_TRAIN/140526.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Alois Ahl  in der Beschwerdesache Romana van Straaten, MBA,  Seeanlage Straße V 4p, 9335 St. Johann am Pressen, Österreich, vertreten durch Dr. Anna Schlosser-Péter, Kurrentgasse 6/3, 1010  Wien, über die Beschwerden vom 23. März 2015 gegen die Bescheide des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf (heute zuständig: Finanzamt Österreich) vom 17. März 2015  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2011 und 2012, Steuernummer  38-795/8528, zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Romana van Straaten` — partial — pred is substring of gold: `Romana van Straaten, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Alois Ahl`(person)
- `Romana van Straaten, MBA`(person)
- `Seeanlage Straße V 4p, 9335 St. Johann am Pressen, Österreich`(address)
- `Dr. Anna Schlosser-Péter`(person)
- `Kurrentgasse 6/3, 1010  Wien`(address)
- `Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `Finanzamt Österreich`(organisation)
- `38-795/8528`(tax_number)

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/144052.1`) (sent_id: `findok-manually-annotated_TRAIN/144052.1_2`)


Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Mag. Janosch Moehrle, Bakk. rer. nat., Neue Frauengasse 2, 3180 Hintereben, Österreich  vertreten durch Tschurtschenthaler, Walder,  Fister Rechtsanwälte GmbH, Dr. Arthur Lemisch Platz 7, 9020 Klagenfurt, über die Beschwerde  vom 3. Juni 2022 gegen den Bescheid des Finanzamtes Österreich vom 4. Mai 2022 betreffend  Einkommensteuer 2020 (Steuernummer 71-848/5765) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Janosch Moehrle` — partial — pred is substring of gold: `Mag. Janosch Moehrle, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Janosch Moehrle, Bakk. rer. nat.`(person)
- `Neue Frauengasse 2, 3180 Hintereben, Österreich`(address)
- `Tschurtschenthaler, Walder,  Fister Rechtsanwälte GmbH`(organisation)
- `Dr. Arthur Lemisch Platz 7, 9020 Klagenfurt`(address)
- `Finanzamtes Österreich`(organisation)
- `71-848/5765`(tax_number)

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149456.1`) (sent_id: `findok-manually-annotated_TRAIN/149456.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Eva Rauber  in der Beschwerdesache der  Henken, Dr.Walter-Hochsteiner-Straße 39, 4730 Röckendorferholz, Österreich, über die Beschwerde vom 2. September 2025 gegen den Bescheid  des Finanzamt Schwechat Gerasdorf  vom 28. August 2025 betreffend Abweisung eines Antrages auf Änderung des  Einkommensteuerbescheides 2024 gemäß § 295a BAO zu Steuernummer 69-427/7795  zu  Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Henken` — type mismatch — same span as gold: `Henken`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Eva Rauber`(person)
- `Henken`(organisation)
- `Dr.Walter-Hochsteiner-Straße 39, 4730 Röckendorferholz, Österreich`(address)
- `Finanzamt Schwechat Gerasdorf`(organisation)
- `69-427/7795`(tax_number)

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149421.1`) (sent_id: `findok-manually-annotated_TRAIN/149421.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Linda Abdulla  in der Beschwerdesache Merlin Jespersen, LLB,  Graf-Hoyos-Weg 5, 9313 Fiming, Österreich, über die Beschwerde vom 17. Dezember 2019 gegen die Bescheide des  Finanzamtes Österreich vom 16. Dezember 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 bis 2018 zu Steuernummer 37-035/4368  zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Merlin Jespersen` — partial — pred is substring of gold: `Merlin Jespersen, LLB`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Linda Abdulla`(person)
- `Merlin Jespersen, LLB`(person)
- `Graf-Hoyos-Weg 5, 9313 Fiming, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `37-035/4368`(tax_number)

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149457.1`) (sent_id: `findok-manually-annotated_TRAIN/149457.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Annika Streicher in der Beschwerdesache  Erhard Hinterschnaiter, BEd, Jellgutweg 32, 9832 Stall, Österreich, über die Beschwerde vom 9. Juni 2023 gegen die Bescheide des  Finanzamtes Österreich vom 25. Mai 2023 betreffend Kraftfahrzeugsteuer 09-12/2020, 01- 12/2021 und 01-12/2022 zu Steuernummer 89-902/5732  zu Recht erkannt:   I. Die Beschwerde gegen die Kraftfahrzeugsteuerbescheide 09-12/2020, 01-12/2021 und 01- 12/2022 wird gem. § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Erhard Hinterschnaiter` — partial — pred is substring of gold: `Erhard Hinterschnaiter, BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Annika Streicher`(person)
- `Erhard Hinterschnaiter, BEd`(person)
- `Jellgutweg 32, 9832 Stall, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `89-902/5732`(tax_number)

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149558.1`) (sent_id: `findok-manually-annotated_TRAIN/149558.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Eckard Reemts, BEd, Äußere Wiesen 7, 2813 Kaltenberg, Österreich, über die Beschwerde vom 17. Oktober 2024 gegen die Bescheide  des Finanzamtes Österreich vom 15. Oktober 2024 betreffend Wiederaufnahme der Verfahren  zur Einkommensteuer 2021 und 2022, Steuernummer 81-010/6697  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Eckard Reemts` — partial — pred is substring of gold: `Eckard Reemts, BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Eckard Reemts, BEd`(person)
- `Äußere Wiesen 7, 2813 Kaltenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `81-010/6697`(tax_number)

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/149570.1`) (sent_id: `findok-manually-annotated_TRAIN/149570.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  der Oleg Peltzmann, Bakk. techn., Ludwig Halauska-Straße 7, 9544 Wiesen, Österreich, vertreten durch TAXCOACH Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG, Muthgasse 109, 1190 Wien, über deren Beschwerde vom  3. Dezember 2024 gegen den Bescheid des Finanzamtes Österreich vom 13. November 2024  betreffend Anspruchszinsen (§ 205 BAO) 2022, Steuernummer  94-582/7899, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Oleg Peltzmann` — partial — pred is substring of gold: `Oleg Peltzmann, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andreas Stanek`(person)
- `Oleg Peltzmann, Bakk. techn.`(person)
- `Ludwig Halauska-Straße 7, 9544 Wiesen, Österreich`(address)
- `TAXCOACH Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG`(organisation)
- `Muthgasse 109, 1190 Wien`(address)
- `Finanzamtes Österreich`(organisation)
- `94-582/7899`(tax_number)

</details>

---

## `Judge_Richter`

**F1:** 0.117 | **Precision:** 0.575 | **Recall:** 0.065  

**Format:** `regex`  
**Rule ID:** `b11b6b1a`  
**Description:**
Captures the name of a judge (Richter/Richterin/Vorsitzende) including complex titles and suffixes.

**Content:**
```
(?:durch\s+(?:den\s+)?(?:Richter|Richterin|Vorsitzende)\s+)([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|\u00d6kR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|Dr\.\s+Univ\.-Prof\.in?|Univ\.-Prof\.in?|Priv\.-Doz\.in?|Hon\.-Prof\.in?)?)?)(?:\s+(?:in der|\u00fcber die|in der Verwaltungsstrafsache)|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.575 | 0.065 | 0.117 | 40 | 23 | 17 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 23 | 17 | 331 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/132828.1`) (sent_id: `findok-manually-annotated_TRAIN/132828.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Michaela Okyay, Franz-Wagner-Weg 6, 4973 Forsthub, Österreich, betreffend Beschwerde vom 30. September 2020 gegen den  Bescheid des Finanzamtes Hollabrunn Korneuburg Tulln (nunmehr Finanzamt Österreich) vom  1. September 2020 betreffend Abweisung des Antrages auf Gewährung von Familienbeihilfe  01.01.2019 in Höhe des in § 33 Abs. 3 erster Satz des Einkommensteuergesetzes 1988  festgelegten Betrages beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Michaela Okyay` (person)
- `Franz-Wagner-Weg 6, 4973 Forsthub, Österreich` (address)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) (sent_id: `findok-manually-annotated_TRAIN/134689.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)

| Predicted | Gold |
|---|---|
| `Mag.Dr. Wolfgang Pagitsch` | `Mag.Dr. Wolfgang Pagitsch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Brunhild Katschmareck` (person)
- `Oberwinden 3, 4553 Hausmanning, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Wien` (city)
- `Wien` (city)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/135661.1`) (sent_id: `findok-manually-annotated_TRAIN/135661.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht über die Beschwerden der  Reinhold Moellenkamp, Höllererweg 4, 2852 Maltern, Österreich, vertreten durch die Achammer & Mennel Rechtsanwälte OG,  Schloßgraben 10, 6800 Feldkirch, gegen die Bescheide des Finanzamtes Feldkirch vom  7. Jänner 2020 betreffend Festsetzung der Kraftfahrzeugsteuer für den Zeitraum 8-10/2019  und Festsetzung der Normverbrauchsabgabe für den Zeitraum 07/2019, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Reinhold Moellenkamp` (person)
- `Höllererweg 4, 2852 Maltern, Österreich` (address)
- `Achammer & Mennel Rechtsanwälte OG` (organisation)
- `Schloßgraben 10, 6800 Feldkirch` (address)
- `Finanzamtes Feldkirch` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/135536.1`) (sent_id: `findok-manually-annotated_TRAIN/135536.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Florentine Beumers, Krischgasse 309, 4113 Windischberg, Österreich, über die Beschwerde vom 20. Februar 2020 gegen den Bescheid  des Finanzamtes Österreich vom 16. Jänner 2020 betreffend Familienbeihilfe 01.2020  Steuernummer 58-742/0765, SVNR 8800 110262, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Florentine Beumers` (person)
- `Krischgasse 309, 4113 Windischberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `58-742/0765` (tax_number)
- `8800 110262` (social_security_number)

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/139698.1`) (sent_id: `findok-manually-annotated_TRAIN/139698.1_1`)


IM NAMEN DER REPUBLI K  Gekürzte Ausfertigung des Erkenntnisses gemäß § 29 Abs. 5 VwGVG  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Verwaltungsstrafsache gegen Herrn Valentina Riehmers, Julius-Wagner-Jauregg-Gasse 1, 6232 Münster, Österreich, vertreten durch Huber  Swoboda Oswald Aixberger Rechtsanwälte GmbH, Tuchlauben 11/18, 1010 Wien, wegen der  Verwaltungsübertretungen gemäß § 1 Abs. 1 in Verbindung mit § 16 Abs. 1 und Tarifen D Post  1 und D Post 4 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBl. für Wien Nr. 20, in  der derzeit geltenden Fassung über die Beschwerde des Beschuldigten vom 4. März 2022  gegen   I. das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen  vom 3. Februar 2022, GZ. MA6/206000003074/2020,   II. das Straferkenntnis des Magistrates der Stadt Wien vom 21. Februar 2022, GZ.  MA6/206000003065/2020,   nach Durchführung einer mündlichen Verhandlung am 15. Dezember 2022 in Abwesenheit des  Beschuldigten, jedoch in Anwesenheit der Verteidigerin, auch als Vertreterin der haftenden  GmbH, der Behördenvertreterin und der Schriftführerin zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als bei  unverändert bleibenden Schuldsprüchen die Höhe der Strafen und der Kosten wie folgt  geändert werden:  II. Wegen der Verwaltungsübertretungen laut Erkenntnis vom 3. Februar 2022, GZ.  MA6/206000003074/2020, werden über den Beschuldigten folgende Strafen jeweils gemäß  § 16 Abs. 1 GAG LGBl. für Wien Nr. 20, in der derzeit geltenden Fassung verhängt:   1. – 5. Geldstrafen in Höhe von je € 330,00, falls diese uneinbringlich sind,   5 Ersatzfreiheitsstrafen von je 11 Stunden,   1 von 11 Seite 2 von 11

| Predicted | Gold |
|---|---|
| `Mag. Gerhard Groschedl` | `Mag. Gerhard Groschedl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Valentina Riehmers` (person)
- `Julius-Wagner-Jauregg-Gasse 1, 6232 Münster, Österreich` (address)
- `Huber  Swoboda Oswald Aixberger Rechtsanwälte GmbH` (organisation)
- `Tuchlauben 11/18, 1010 Wien` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) (sent_id: `findok-manually-annotated_TRAIN/143567.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde des  Desiree Häfke, Weinrebengasse 209, 4282 Hinterhütten, Österreich, vom 11. September 2023 gegen den Bescheid des Finanzamtes  Österreich vom 7. September 2023 betreffend   - Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für Kind T. für den Zeitraum  Jänner 2021 bis Dezember 2022   - Rückforderung von Familienbeihilfe für Kind A. für den Zeitraum Jänner 2021 bis Oktober  2022 (Geschwisterstaffel anteilig)  - Rückforderung von Familienbeihilfe für Kind B. für den Zeitraum Jänner 2021 bis Oktober  2021 (Geschwisterstaffel anteilig)  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Pavlik` | `Dr. Wolfgang Pavlik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Desiree Häfke` (person)
- `Weinrebengasse 209, 4282 Hinterhütten, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) (sent_id: `findok-manually-annotated_TRAIN/144562.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  August Ronzheimer, Daimlerweg 3, 5221 Babenham, Österreich, vom 26. Mai 2023 gegen den Bescheid des Finanzamtes Österreich  vom 28. April 2023 betreffend Abweisung des Antrages auf Familienbeihilfe ab Oktober 2022,  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Pavlik` | `Dr. Wolfgang Pavlik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `August Ronzheimer` (person)
- `Daimlerweg 3, 5221 Babenham, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149301.1`) (sent_id: `findok-manually-annotated_TRAIN/149301.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Annalena Spatzier, Bahnhof Krottenbachstraße 4, 3130 Unterwinden, Österreich, über die Beschwerde vom 21. März 2024 gegen  den Bescheid des Finanzamtes Österreich vom 22. Februar 2024 betreffend Einkommensteuer  2018, Steuernummer 78-848/2763, zu Recht erkannt:   I. Der angefochtene Bescheid wird ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Annalena Spatzier` (person)
- `Bahnhof Krottenbachstraße 4, 3130 Unterwinden, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `78-848/2763` (tax_number)

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) (sent_id: `findok-manually-annotated_TRAIN/149280.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Zwilling in der Beschwerdesache  Ferdinand Mielnickel, Viertelweg 16, 3720 Gaindorf, Österreich, vertreten durch Hallas & Partner Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG, Praterstraße 38, 1020 Wien, über die Beschwerde vom  30. November 2017 gegen die Bescheide des Finanzamtes Baden Mödling (nunmehr Finanzamt  Österreich) vom 31. Oktober 2017 betreffend Festsetzung eines Verspätungszuschlages  betreffend Einkommensteuer 2015 und 2016 und Umsatzsteuer 2015 und 2016,  Steuernummer 86-167/7419  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Josef Zwilling` | `Mag. Josef Zwilling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ferdinand Mielnickel` (person)
- `Viertelweg 16, 3720 Gaindorf, Österreich` (address)
- `Hallas & Partner Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG` (organisation)
- `Praterstraße 38, 1020 Wien` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `Finanzamt  Österreich` (organisation)
- `86-167/7419` (tax_number)

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149322.1`) (sent_id: `findok-manually-annotated_TRAIN/149322.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache HR KzlR Stephanie Ganssloser, Schwemmgasse 16, 8992 Fischerndorf, Österreich, betreffend Beschwerde vom 8. April 2025 gegen  den Bescheid des Finanzamtes Österreich vom 10. März 2025 betreffend Säumniszuschlag  10.03.2025 zur Steuernummer 16-527/7844  beschlossen:   Die Beschwerde vom 8. April 2025 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Mag. Markus Knechtl LL.M.` | `Mag. Markus Knechtl LL.M.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `HR KzlR Stephanie Ganssloser` (person)
- `Schwemmgasse 16, 8992 Fischerndorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `16-527/7844` (tax_number)

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/149309.1`) (sent_id: `findok-manually-annotated_TRAIN/149309.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Julia Terbofen, Treidlerstraße 2, 3820 Reith, Österreich, Steuernummer 31-441/2585, über die Beschwerde vom  9. Dezember 2024 gegen den Bescheid des Finanzamtes Österreich vom 22. November 2024  betreffend Festsetzung von Anspruchszinsen 2023 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Peter Bilger` | `Mag. Peter Bilger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Julia Terbofen` (person)
- `Treidlerstraße 2, 3820 Reith, Österreich` (address)
- `31-441/2585` (tax_number)
- `Finanzamtes Österreich` (organisation)

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) (sent_id: `findok-manually-annotated_TRAIN/149404.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johann Fischerlehner in der  Beschwerdesache Veronika Ogrissek, Weißeneggerberg 160, 3631 Kienings, Österreich, über die Beschwerde vom 23. September 2024  gegen die Bescheide des Finanzamtes Österreich vom 16. September 2024 betreffend  Pfändung einer Geldforderung und Verfügungsverbot zu Steuernummer 48-541/5488  zu  Recht erkannt:   I. Die Beschwerde gegen den Bescheid betreffend Pfändung einer Geldforderung wird  als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Johann Fischerlehner` | `Mag. Johann Fischerlehner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Veronika Ogrissek` (person)
- `Weißeneggerberg 160, 3631 Kienings, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `48-541/5488` (tax_number)

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/149424.1`) (sent_id: `findok-manually-annotated_TRAIN/149424.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Franka Bartolomey, Feisterweg 11, 8321 St. Margarethen an der Raab, Österreich, über die Beschwerde vom 13. Mai 2024 gegen den Bescheid des  Finanzamtes Österreich vom 29. April 2024 betreffend Einkommensteuer 2023, 82-102/0439,  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Franka Bartolomey` (person)
- `Feisterweg 11, 8321 St. Margarethen an der Raab, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `82-102/0439` (tax_number)

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/149497.1`) (sent_id: `findok-manually-annotated_TRAIN/149497.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  James Grentz, Katharine-Drexel-Straße 5, 3661 Lohsdorf, Österreich, vertreten durch T & M TRAUNSTEINER U. MITTERER KG,  Schubertviertel 38, 4300 St.Valentin, betreffend Beschwerde vom 16. Mai 2024 gegen den  Bescheid des Finanzamtes Österreich vom 7. Mai 2024 betreffend Anspruchszinsen (§ 205  BAO) 2022 (Einkommensteuer) Steuernummer 90-523/9682  beschlossen:  Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO für gegenstandlos erklärt.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `James Grentz` (person)
- `Katharine-Drexel-Straße 5, 3661 Lohsdorf, Österreich` (address)
- `T & M TRAUNSTEINER U. MITTERER KG` (organisation)
- `Schubertviertel 38, 4300 St.Valentin` (address)
- `Finanzamtes Österreich` (organisation)
- `90-523/9682` (tax_number)

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/149558.1`) (sent_id: `findok-manually-annotated_TRAIN/149558.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Eckard Reemts, BEd, Äußere Wiesen 7, 2813 Kaltenberg, Österreich, über die Beschwerde vom 17. Oktober 2024 gegen die Bescheide  des Finanzamtes Österreich vom 15. Oktober 2024 betreffend Wiederaufnahme der Verfahren  zur Einkommensteuer 2021 und 2022, Steuernummer 81-010/6697  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Eckard Reemts, BEd` (person)
- `Äußere Wiesen 7, 2813 Kaltenberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `81-010/6697` (tax_number)

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/149570.1`) (sent_id: `findok-manually-annotated_TRAIN/149570.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  der Oleg Peltzmann, Bakk. techn., Ludwig Halauska-Straße 7, 9544 Wiesen, Österreich, vertreten durch TAXCOACH Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG, Muthgasse 109, 1190 Wien, über deren Beschwerde vom  3. Dezember 2024 gegen den Bescheid des Finanzamtes Österreich vom 13. November 2024  betreffend Anspruchszinsen (§ 205 BAO) 2022, Steuernummer  94-582/7899, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Andreas Stanek` | `Mag. Andreas Stanek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Oleg Peltzmann, Bakk. techn.` (person)
- `Ludwig Halauska-Straße 7, 9544 Wiesen, Österreich` (address)
- `TAXCOACH Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG` (organisation)
- `Muthgasse 109, 1190 Wien` (address)
- `Finanzamtes Österreich` (organisation)
- `94-582/7899` (tax_number)

**Example 16** (doc_id: `findok-manually-annotated_TRAIN/149682.1`) (sent_id: `findok-manually-annotated_TRAIN/149682.1_1`)


BESCHLUSS  Das Bundesfinanzgericht beschließt durch den Richter Mag. David Hell LL.B. LL.M. in der  Beschwerdesache Ingolf Johannisbauer, Hochtregister Straße 44, 9560 Weit, Österreich, vertreten durch Dr. Michael Kotschnigg,  Stadlauer Straße 39/I/12, 1220 Wien, betreffend Beschwerde vom 16. Mai 2023 (eingebracht  am 1. September 2025) gegen den Bescheid des Finanzamtes Österreich vom 21. April 2023  betreffend Zurückweisung eines Antrages auf Festsetzung von Umsatzsteuerzinsen gemäß  § 205c BAO, Steuernummer 08-788/8579:  I. Die Beschwerde wird als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. David Hell LL.B. LL.M.` | `Mag. David Hell LL.B. LL.M.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ingolf Johannisbauer` (person)
- `Hochtregister Straße 44, 9560 Weit, Österreich` (address)
- `Dr. Michael Kotschnigg` (person)
- `Stadlauer Straße 39/I/12, 1220 Wien` (address)
- `Finanzamtes Österreich` (organisation)
- `08-788/8579` (tax_number)

**Example 17** (doc_id: `findok-manually-annotated_TRAIN/149691.1`) (sent_id: `findok-manually-annotated_TRAIN/149691.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Kay Wrulich in der Beschwerdesache   OStR Richarda Schödensack, Ornetsedt 12, 4274 Kollnedt, Österreich, vertreten durch Steuerberater Metzler & Adelsberger OG,  Stadtgraben 25, 6060 Hall in Tirol, über die Beschwerde vom 22. August 2019 gegen die gem. §  293b BAO berichtigten Einkommensteuerbescheide der Jahre 2014 – 2017 des Finanzamtes  Innsbruck (nunmehr Finanzamt Österreich) allesamt vom 22. Juli 2019, Steuernummer  31-785/0303, nach öffentlicher mündlicher Verhandlung zu Recht erkannt:   I. Die angefochtenen Bescheide werden aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Kay Wrulich` | `Mag. Kay Wrulich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OStR Richarda Schödensack` (person)
- `Ornetsedt 12, 4274 Kollnedt, Österreich` (address)
- `Steuerberater Metzler & Adelsberger OG` (organisation)
- `Stadtgraben 25, 6060 Hall in Tirol` (address)
- `Finanzamtes  Innsbruck` (organisation)
- `Finanzamt Österreich` (organisation)
- `31-785/0303` (tax_number)

**Example 18** (doc_id: `findok-manually-annotated_TRAIN/149711.1`) (sent_id: `findok-manually-annotated_TRAIN/149711.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  Joseph Kramors, Planseestraße 8, 9833 Lamnitz, Österreich, über dessen Beschwerde vom 7. Februar 2025 gegen den Bescheid  des Finanzamtes Österreich vom 15. Jänner 2025 betreffend Anspruchszinsen (§ 205 BAO)  2022, Steuernummer 27-377/4888, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Andreas Stanek` | `Mag. Andreas Stanek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Joseph Kramors` (person)
- `Planseestraße 8, 9833 Lamnitz, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `27-377/4888` (tax_number)

**Example 19** (doc_id: `findok-manually-annotated_TRAIN/149749.1`) (sent_id: `findok-manually-annotated_TRAIN/149749.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Heidemarie Zangel, Furtmüllerstraße 66, 5142 Hehenberg, Österreich  vertreten durch die Mag. Ghesla Steuerberater GmbH, Kirchstraße 32,  6923 Lauterach, über die Beschwerden gegen die Bescheide des Finanzamtes Österreich  betreffend Einkommensteuer 2019 und 2020, 08-156/6554, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Heidemarie Zangel` (person)
- `Furtmüllerstraße 66, 5142 Hehenberg, Österreich` (address)
- `Mag. Ghesla Steuerberater GmbH` (organisation)
- `Kirchstraße 32,  6923 Lauterach` (address)
- `Finanzamtes Österreich` (organisation)
- `08-156/6554` (tax_number)

**Example 20** (doc_id: `findok-manually-annotated_TRAIN/149768.1`) (sent_id: `findok-manually-annotated_TRAIN/149768.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johann Fischerlehner in der  Beschwerdesache Siegmund Cofalke, Schürzbergweg, Thierbach 27, 8570 Bärnbach, Österreich, vertreten durch Mag. Elizabeta Koleva,  Karolinengasse 33 Tür 9, 1040 Wien, über die Beschwerde vom 28. Juli 2025 gegen den  Bescheid des Finanzamtes Österreich vom 4. Juni 2025 betreffend Abweisung eines Antrages  betreffend die Einkommensteuer 2023 zu Steuernummer 26-606/9835  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Johann Fischerlehner` | `Mag. Johann Fischerlehner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Siegmund Cofalke` (person)
- `Schürzbergweg, Thierbach 27, 8570 Bärnbach, Österreich` (address)
- `Mag. Elizabeta Koleva` (person)
- `Karolinengasse 33 Tür 9, 1040 Wien` (address)
- `Finanzamtes Österreich` (organisation)
- `26-606/9835` (tax_number)

**Example 21** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) (sent_id: `findok-manually-annotated_TRAIN/149828.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Gisbert Lindwedel, Penken 55, 4903 Hofmanning, Österreich, vertreten durch die Mag. Ghesla Steuerberater GmbH, Kirchstraße  32, 6923 Lauterach, über die Beschwerden gegen die Bescheide des Finanzamtes Bregenz  (nunmehr: Finanzamt Österreich) betreffend Einkommensteuer 2015 und 2016 sowie  Festsetzung von Vorauszahlungen an Einkommensteuer für 2017 sowie 2018 und Folgejahre,  85-106/2625, zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gisbert Lindwedel` (person)
- `Penken 55, 4903 Hofmanning, Österreich` (address)
- `Mag. Ghesla Steuerberater GmbH` (organisation)
- `Kirchstraße  32, 6923 Lauterach` (address)
- `Finanzamtes Bregenz` (organisation)
- `Finanzamt Österreich` (organisation)
- `85-106/2625` (tax_number)

**Example 22** (doc_id: `findok-manually-annotated_TRAIN/149863.1`) (sent_id: `findok-manually-annotated_TRAIN/149863.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Patrick Brandstetter in der  Beschwerdesache Wilma Kewer, Dr.-Adolf-Schärf-Straße 26, 2651 Mayerhöfen, Österreich, über die Beschwerde vom 17. August 2025  gegen den Bescheid des Finanzamtes Österreich vom 04. August 2025 betreffend die  Verzinsung der Rückerstattung gem. § 16 COFAG-NoAG (Steuernummer 45-588/1819 ) zu  Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Patrick Brandstetter` | `Mag. Patrick Brandstetter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wilma Kewer` (person)
- `Dr.-Adolf-Schärf-Straße 26, 2651 Mayerhöfen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `45-588/1819` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/138410.1`) (sent_id: `findok-manually-annotated_TRAIN/138410.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter MMag.

**False Positives:**

- `MMag.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/140056.1`) (sent_id: `findok-manually-annotated_TRAIN/140056.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache   Emanuela Wilgen, Kölnhofsiedlung 12, 5622 Mitterstein, Österreich, über die Beschwerde vom 1. Juni 2022 gegen den Bescheid des  Finanzamtes Österreich vom 5. Mai 2022 betreffend Rückforderung von für Hademar Peschek  für  den Zeitraum Oktober 2021 bis Februar 2022 bezogener Beträge an Familienbeihilfe und  Kinderabsetzbetrag, Steuernummer 06-892/6489 (7083181213) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Emanuela Wilgen`(person)
- `Kölnhofsiedlung 12, 5622 Mitterstein, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Hademar Peschek`(person)
- `06-892/6489`(tax_number)
- `7083181213`(social_security_number)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) (sent_id: `findok-manually-annotated_TRAIN/137355.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter MMag.

**False Positives:**

- `MMag.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/140853.1`) (sent_id: `findok-manually-annotated_TRAIN/140853.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Juri Jonkhans  in der Beschwerdesache KommR Ulrich Maader,  Prangergasse 2, 5323 Hinterebenau, Österreich, vertreten durch Dr. Anton Herbert Pochieser, Schottenfeldgasse 2-4 Tür 23,  Wien 1070, betreffend die Beschwerde vom 29.09.2021 gegen den Bescheid des  Finanzamtes  Österreich vom 27. August 2021, mit welchem die Aussetzung der Entscheidung gem. § 271  BAO betreffend die Beschwerde vom 18.01.2021 gegen den Abweisungsbescheid vom  10.12.2020 (Ausgleichszahlung) verfügt wurde, zu SVNr.

**False Positives:**

- `Mag. Juri Jonkhans ` — partial — gold is substring of pred: `Mag. Juri Jonkhans`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Juri Jonkhans`(person)
- `KommR Ulrich Maader`(person)
- `Prangergasse 2, 5323 Hinterebenau, Österreich`(address)
- `Dr. Anton Herbert Pochieser`(person)
- `Schottenfeldgasse 2-4 Tür 23,  Wien 1070`(address)
- `Finanzamtes  Österreich`(organisation)

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/143368.1`) (sent_id: `findok-manually-annotated_TRAIN/143368.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Karlheinz Parlak  in der Beschwerdesache  Melinda Krebsz, Zauchmühle 136, 2463 Gallbrunn, Österreich, über die Beschwerde vom 8. Mai 2023 gegen den Bescheid des  Finanzamtes Österreich vom 27. April 2023 betreffend Einkommensteuer 2022 zur  Steuernummer 60-281/5380  zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Karlheinz Parlak ` — partial — gold is substring of pred: `Mag. Karlheinz Parlak`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Karlheinz Parlak`(person)
- `Melinda Krebsz`(person)
- `Zauchmühle 136, 2463 Gallbrunn, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `60-281/5380`(tax_number)

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/144072.1`) (sent_id: `findok-manually-annotated_TRAIN/144072.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Yelec Träubel, Pelargonienweg 13, 4063 Rudelsdorf, Österreich, vertreten durch Mag. Wolfgang Andreas Kleinhappel, Rabensteig 8/3a, 1010 Wien,  über die Beschwerde vom 23. Mai 2023 gegen den Bescheid des Finanzamtes Österreich vom  10. Mai 2023 betreffend Zurückweisung des Antrages auf Familienbeihilfe vom 14. Juni 2021  für Karin Steilen  für den Zeitraum März 2020 bis April 2021, Steuernummer  41-392/0377 (SVNR 4756010962), zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Yelec Träubel`(person)
- `Pelargonienweg 13, 4063 Rudelsdorf, Österreich`(address)
- `Mag. Wolfgang Andreas Kleinhappel`(person)
- `Rabensteig 8/3a, 1010 Wien`(address)
- `Finanzamtes Österreich`(organisation)
- `Karin Steilen`(person)
- `41-392/0377`(tax_number)
- `4756010962`(social_security_number)

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/144169.1`) (sent_id: `findok-manually-annotated_TRAIN/144169.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache   Felizia Ponsong, Georg-von-Trapp-Straße 66, 8243 Sparberegg, Österreich, über die Beschwerde vom 29. Juli 2023 gegen den Bescheid des  Finanzamtes Österreich vom 6. Juli 2023 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbetrag für den Zeitraum Oktober 2022 bis Juni 2023, Steuernummer  68-038/3701 (SVNR 8332180970), zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Felizia Ponsong`(person)
- `Georg-von-Trapp-Straße 66, 8243 Sparberegg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `68-038/3701`(tax_number)
- `8332180970`(social_security_number)

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/146849.1`) (sent_id: `findok-manually-annotated_TRAIN/146849.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Evelyn Sedlmayr, Ebener Straße 25, 5201 Seewalchen, Österreich, über die Beschwerde vom 2. April 2024 gegen den Bescheid des Finanzamtes  Österreich vom 20. März 2024 betreffend Rückforderung von für die Kinder Evelyn Boediker  und  Merlin Leutholdt  für den Zeitraum Juni 2022 bis Juli 2023 bezogenen Beträgen an Familienbeihilfe  (Differenz-/Ausgleichszahlungen), Steuernummer 50-831/8746 (SVNR 2154030383) zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Evelyn Sedlmayr`(person)
- `Ebener Straße 25, 5201 Seewalchen, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `Evelyn Boediker`(person)
- `Merlin Leutholdt`(person)
- `50-831/8746`(tax_number)
- `2154030383`(social_security_number)

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/148615.1`) (sent_id: `findok-manually-annotated_TRAIN/148615.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache   Nicola Happl, Unterfarracher Straße 34, 9542 Berg ob Afritz, Österreich, über die Beschwerde vom 18. November 2024 gegen den Bescheid  des Finanzamtes Österreich vom 21. Oktober 2024 betreffend Abweisung des Antrages auf  Familienbeihilfe vom 10. September 2024 für Delila Hofsäß  ab September 2024,  Steuernummer 20-702/2840 (SVNR 8634 041244), zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Nicola Happl`(person)
- `Unterfarracher Straße 34, 9542 Berg ob Afritz, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Delila Hofsäß`(person)
- `20-702/2840`(tax_number)
- `8634 041244`(social_security_number)

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/148648.1`) (sent_id: `findok-manually-annotated_TRAIN/148648.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter MMag.

**False Positives:**

- `MMag.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/148650.1`) (sent_id: `findok-manually-annotated_TRAIN/148650.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache   Agatha Vesper, Albersdorfweg 21, 4973 Rabenfurt, Österreich, betreffend Beschwerde vom 9. Juli 2024 gegen den Bescheid des  Finanzamtes Österreich vom 17. Juni 2024 betreffend Abweisung des Antrages vom  31. Jänner 2024 auf den Erhöhungsbetrag zur Familienbeihilfe ab Jänner 2024, Steuernummer  58-042/7990 (SVNR 6155 130467), beschlossen:   Der Vorlageantrag vom 20. November 2024 wird gemäß § 260 Abs. 1 lit. b  Bundesabgabenordnung (BAO) iVm § 264 Abs. 4 lit. e BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `R.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Agatha Vesper`(person)
- `Albersdorfweg 21, 4973 Rabenfurt, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `58-042/7990`(tax_number)
- `6155 130467`(social_security_number)

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/149333.1`) (sent_id: `findok-manually-annotated_TRAIN/149333.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Corvin Schlegl  in der Beschwerdesache Ada Fürpeil,  Gaminger Berg 97, 8600 Mötschlach, Österreich, gegen den Bescheid des Finanzamtes Österreich vom 28. Oktober 2024  betreffend Körperschaftsteuer 2022, Steuernummer 68-789/8168, beschlossen:  I. Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO als gegenstandslos erklärt.

**False Positives:**

- `Mag. Corvin Schlegl ` — partial — gold is substring of pred: `Mag. Corvin Schlegl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Corvin Schlegl`(person)
- `Ada Fürpeil`(person)
- `Gaminger Berg 97, 8600 Mötschlach, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `68-789/8168`(tax_number)

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) (sent_id: `findok-manually-annotated_TRAIN/149418.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hartwig Daxlberger  in der Beschwerdesache Arnd Ehrlein,  Schloßwiesen 332, 5651 Heuberg, Österreich  vertreten durch Ernst & Young Steuerberatungs-GmbH, Wagramer Straße 19,  1220 Wien über die Beschwerde vom 1. Oktober 2025 gegen den Bescheid des Finanzamtes für  Großbetriebe vom 2. September 2025 betreffend Stabilitätsabgabe 2024 Steuernummer  44-182/2731  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Hartwig Daxlberger ` — partial — gold is substring of pred: `Dr. Hartwig Daxlberger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hartwig Daxlberger`(person)
- `Arnd Ehrlein`(person)
- `Schloßwiesen 332, 5651 Heuberg, Österreich`(address)
- `Ernst & Young Steuerberatungs-GmbH`(organisation)
- `Wagramer Straße 19,  1220 Wien`(address)
- `44-182/2731`(tax_number)

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) (sent_id: `findok-manually-annotated_TRAIN/149473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Pawel Heldt  in der Beschwerdesache  Samir Krahnepuhl, Webersberg 40, 7331 Kalkgruben, Österreich, über die Beschwerde vom 18. September 2023 gegen den  Bescheid des Finanzamtes Österreich vom 7. September 2023 betreffend Abweisung des  Antrags auf Wiedereinsetzung in den vorigen Stand vom 5. August 2023, Steuernummer  88-903/5443, zu Recht:   I. Der angefochtene Bescheid wird abgeändert.

**False Positives:**

- `Dr. Pawel Heldt ` — partial — gold is substring of pred: `Dr. Pawel Heldt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Pawel Heldt`(person)
- `Samir Krahnepuhl`(person)
- `Webersberg 40, 7331 Kalkgruben, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `88-903/5443`(tax_number)

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/149499.1`) (sent_id: `findok-manually-annotated_TRAIN/149499.1_1`)


IM NAMEN DER REPUBLI K  Bundesfinanzgericht hat durch den Richter RI in der Verwaltungsstrafsache gegen Gernot Rabensteiner,  Öblarn 15, 4621 Rappersdorf, Österreich, über die Beschwerde vom 14. Februar 2025 gegen den  Zurückweisungsbescheid des Magistrates der Stadt Wien vom 6. Februar 2025, Zahl: MA67- XYZ, mit dem der Einspruch vom 13. Dezember 2024 gegen die Strafverfügung vom 18.  Oktober 2024 mit derselben Geschäftszahl gemäß § 49 Abs. 1 VStG als verspätet  zurückgewiesen wurde, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  der angefochtene Zurückweisungsbescheid bestätigt.

**False Positives:**

- `RI` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Gernot Rabensteiner`(person)
- `Öblarn 15, 4621 Rappersdorf, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/149810.1`) (sent_id: `findok-manually-annotated_TRAIN/149810.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Adam Nietschl  in der Beschwerdesache Vincent Feidl,  Neumayrgasse 12, 9640 Würmlach, Österreich, vertreten durch Janina Ernicke, Bahnhof Liesing 3, 9065 Zell, Österreich, GF2***, Grabenholz 68, 4720 Würzberg, Österreich, und Saxinger  Chalupsky & Partner Rechtsanwälte GmbH, Böhmerwaldstraße 14, 4020 Linz, über die  Beschwerde vom 18. Oktober 2021 gegen den Bescheid des Finanzamtes Österreich vom 20.  September 2021 betreffend Zwangsstrafen 20.09.2021, Steuernummer 59-917/0690, nach  Durchführung einer mündlichen Verhandlung am 29. September 2025 zu Recht erkannt:    I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Adam Nietschl ` — partial — gold is substring of pred: `Mag. Adam Nietschl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Adam Nietschl`(person)
- `Vincent Feidl`(person)
- `Neumayrgasse 12, 9640 Würmlach, Österreich`(address)
- `Janina Ernicke`(person)
- `Bahnhof Liesing 3, 9065 Zell, Österreich`(address)
- `Grabenholz 68, 4720 Würzberg, Österreich`(address)
- `Saxinger  Chalupsky & Partner Rechtsanwälte GmbH`(organisation)
- `Böhmerwaldstraße 14, 4020 Linz`(address)
- `Finanzamtes Österreich`(organisation)
- `59-917/0690`(tax_number)

**Example 16** (doc_id: `findok-manually-annotated_TRAIN/149835.1`) (sent_id: `findok-manually-annotated_TRAIN/149835.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Raul Okyay  in der Beschwerdesache Volkmar Nemcova,  Tauplitz 86, 9346 Bach, Österreich, gegen den von der belangten Behörde Finanzamt Österreich am 9. Oktober  2024 zu Steuernummer 53-985/9991  ausgefertigten Bescheid betreffend  Einkommensteuer für das Jahr 2023 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Raul Okyay ` — partial — gold is substring of pred: `Dr. Raul Okyay`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Raul Okyay`(person)
- `Volkmar Nemcova`(person)
- `Tauplitz 86, 9346 Bach, Österreich`(address)
- `Finanzamt Österreich`(organisation)
- `53-985/9991`(tax_number)

</details>

---

## `Herr_Name`

**F1:** 0.090 | **Precision:** 0.680 | **Recall:** 0.048  

**Format:** `regex`  
**Rule ID:** `4bee6298`  
**Description:**
Captures full names following 'Herr' or 'Herrn', ensuring the full name is extracted.

**Content:**
```
(?:Herr|Herrn)\s+([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.680 | 0.048 | 0.090 | 25 | 17 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 17 | 8 | 253 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/139698.1`) (sent_id: `findok-manually-annotated_TRAIN/139698.1_1`)


IM NAMEN DER REPUBLI K  Gekürzte Ausfertigung des Erkenntnisses gemäß § 29 Abs. 5 VwGVG  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Verwaltungsstrafsache gegen Herrn Valentina Riehmers, Julius-Wagner-Jauregg-Gasse 1, 6232 Münster, Österreich, vertreten durch Huber  Swoboda Oswald Aixberger Rechtsanwälte GmbH, Tuchlauben 11/18, 1010 Wien, wegen der  Verwaltungsübertretungen gemäß § 1 Abs. 1 in Verbindung mit § 16 Abs. 1 und Tarifen D Post  1 und D Post 4 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBl. für Wien Nr. 20, in  der derzeit geltenden Fassung über die Beschwerde des Beschuldigten vom 4. März 2022  gegen   I. das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen  vom 3. Februar 2022, GZ. MA6/206000003074/2020,   II. das Straferkenntnis des Magistrates der Stadt Wien vom 21. Februar 2022, GZ.  MA6/206000003065/2020,   nach Durchführung einer mündlichen Verhandlung am 15. Dezember 2022 in Abwesenheit des  Beschuldigten, jedoch in Anwesenheit der Verteidigerin, auch als Vertreterin der haftenden  GmbH, der Behördenvertreterin und der Schriftführerin zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als bei  unverändert bleibenden Schuldsprüchen die Höhe der Strafen und der Kosten wie folgt  geändert werden:  II. Wegen der Verwaltungsübertretungen laut Erkenntnis vom 3. Februar 2022, GZ.  MA6/206000003074/2020, werden über den Beschuldigten folgende Strafen jeweils gemäß  § 16 Abs. 1 GAG LGBl. für Wien Nr. 20, in der derzeit geltenden Fassung verhängt:   1. – 5. Geldstrafen in Höhe von je € 330,00, falls diese uneinbringlich sind,   5 Ersatzfreiheitsstrafen von je 11 Stunden,   1 von 11 Seite 2 von 11

| Predicted | Gold |
|---|---|
| `Valentina Riehmers` | `Valentina Riehmers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gerhard Groschedl` (person)
- `Julius-Wagner-Jauregg-Gasse 1, 6232 Münster, Österreich` (address)
- `Huber  Swoboda Oswald Aixberger Rechtsanwälte GmbH` (organisation)
- `Tuchlauben 11/18, 1010 Wien` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/139698.1`) (sent_id: `findok-manually-annotated_TRAIN/139698.1_36`)


Die UnterRecycling Services GMBH  hafte für die mit diesem Bescheid über den zur Vertretung nach außen  Berufenen, Herrn Valentina Riehmers, verhängten Geldstrafen von 5 x je € 510,00 und 2 x je € 520,00  und die Verfahrenskosten in der Höhe von € 359,00 sowie für sonstige in Geld bemessene  Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.

| Predicted | Gold |
|---|---|
| `Valentina Riehmers` | `Valentina Riehmers` |

**Missed by this rule (FN):**

- `UnterRecycling Services GMBH` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/139698.1`) (sent_id: `findok-manually-annotated_TRAIN/139698.1_37`)


II. Mit Straferkenntnis des Magistrates der Stadt Wien vom 21. Februar 2022, GZ.  MA6/206000003065/2020, wurde Herr Valentina Riehmers, (in weiterer Folge: Beschuldigter) als  handelsrechtlicher Geschäftsführer der Firma UnterRecycling Services GMBH  mit Sitz in Mosletzberg 2, 4084 Dörfledt, Österreich,  schuldig erkannt,   1. er habe als handelsrechtlicher Geschäftsführer der Firma UnterRecycling Services GMBH  im Juni 2020 vor  der Liegenschaft in Rodelsbach 3, 4800 Lehen, Österreich, den öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, durch eine Baustofflagerung im Ausmaß von 57,50 m² genutzt, wobei er hiefür  bis zum 13.08.2020 weder eine Gebrauchserlaubnis erwirkt noch die Gebrauchsabgabe  entrichtet habe.

| Predicted | Gold |
|---|---|
| `Valentina Riehmers` | `Valentina Riehmers` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)
- `UnterRecycling Services GMBH` (organisation)
- `Mosletzberg 2, 4084 Dörfledt, Österreich` (address)
- `UnterRecycling Services GMBH` (organisation)
- `Rodelsbach 3, 4800 Lehen, Österreich` (address)

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/139698.1`) (sent_id: `findok-manually-annotated_TRAIN/139698.1_62`)


Die UnterRecycling Services GMBH  hafte für die mit diesem Bescheid über den zur Vertretung nach außen  Berufenen, Herrn Valentina Riehmers, verhängten Geldstrafen von 3 x je € 520,00, 3 x je € 320,00 und 2  x je € 700,00 und die Verfahrenskosten in der Höhe von € 392,00 sowie für sonstige in Geld  bemessene Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.“

| Predicted | Gold |
|---|---|
| `Valentina Riehmers` | `Valentina Riehmers` |

**Missed by this rule (FN):**

- `UnterRecycling Services GMBH` (organisation)

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/148648.1`) (sent_id: `findok-manually-annotated_TRAIN/148648.1_6`)


Entscheidungsgründe  I. Verfahrensgang  Mit Einkommensteuerbescheid (Arbeitnehmerveranlagung) vom 1. März 2024 wurde die  Einkommensteuer von Herrn Bernhard Siegmundt (im Folgenden auch Beschwerdeführer oder Bf.) für das  Jahr 2023 mit einer Gutschrift in Höhe von EUR 29,- festgesetzt.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/148648.1`) (sent_id: `findok-manually-annotated_TRAIN/148648.1_25`)


 In der zweiten Monatshälfte des Juli 2023 hat Herr Bernhard Siegmundt  eine Beschäftigung bei der  Arbeitgeber Wien in Adr Arbeitgeber Wien, begonnen.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

**Missed by this rule (FN):**

- `Wien` (city)
- `Wien` (city)

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/148648.1`) (sent_id: `findok-manually-annotated_TRAIN/148648.1_29`)


Herr Bernhard Siegmundt  verfügte im Jahr 2023 über zwei Wohnsitze:   Herr Bernhard Siegmundt  hat seit 1. Juli 2020 einen Wohnsitz in einer Mietwohnung in Grabental 83, 9300 Goggerwenig, Österreich.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

**Missed by this rule (FN):**

- `Grabental 83, 9300 Goggerwenig, Österreich` (address)

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/148648.1`) (sent_id: `findok-manually-annotated_TRAIN/148648.1_32`)


 Weiters verfügt Herr Bernhard Siegmundt  über einen Wohnsitz in einem Haus in Ungarn in der Adr  Wohnsitz Ungarn.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

**Missed by this rule (FN):**

- `Ungarn` (country)
- `Ungarn` (country)

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/148648.1`) (sent_id: `findok-manually-annotated_TRAIN/148648.1_38`)


Der Lebensmittelpunkt von Herrn Bernhard Siegmundt  liegt in Österreich.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

**Missed by this rule (FN):**

- `Österreich` (country)

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/148648.1`) (sent_id: `findok-manually-annotated_TRAIN/148648.1_39`)


2. Beweiswürdigung  Der Sachverhalt zu den beiden Dienstverhältnissen von Herrn Bernhard Siegmundt  im Jahr 2023 ergibt  sich aus den Angaben zu Lohnzettel und Meldungen im Einkommensteuerbescheid 2023 sowie  aus den Antworten von Herrn Bernhard Siegmundt  auf die Vorhalte der belangten Behörde und des  Bundesfinanzgerichtes.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/148648.1`) (sent_id: `findok-manually-annotated_TRAIN/148648.1_41`)


Die Feststellungen zu den beiden Wohnsitzen basieren auf den von Herrn Bernhard Siegmundt  zur  Verfügung gestellten Unterlagen (Mietvertrag der Wohnung in Österreich, Grundbuchsauszug  aus Ungarn, ungarische Adresskarte) und seinen Erläuterungen im Rahmen der Beantwortung  der Vorhalte der belangten Behörde und des Bundesfinanzgerichtes.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

**Missed by this rule (FN):**

- `Österreich` (country)
- `Ungarn` (country)
- `Bundesfinanzgerichtes` (organisation)

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/148648.1`) (sent_id: `findok-manually-annotated_TRAIN/148648.1_44`)


 Mit Österreich verbindet Herrn Bernhard Siegmundt  seine Lebenspartnerin, sein Arbeitsplatz und  seine langfristigen Pläne, sodass seine Bindung zu Österreich stärker ist.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

**Missed by this rule (FN):**

- `Österreich` (country)
- `Österreich` (country)

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/148648.1`) (sent_id: `findok-manually-annotated_TRAIN/148648.1_45`)


Auch als Herr  Bernhard Siegmundt  nach Österreich gekommen ist, hatte er bereits geplant für längere Zeit in  Österreich zu bleiben.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

**Missed by this rule (FN):**

- `Österreich` (country)
- `Österreich` (country)

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/148648.1`) (sent_id: `findok-manually-annotated_TRAIN/148648.1_48`)


Die  Lebenspartnerin von Herrn Bernhard Siegmundt  lebt und arbeitet ebenfalls in Österreich.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

**Missed by this rule (FN):**

- `Österreich` (country)

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/149511.1`) (sent_id: `findok-manually-annotated_TRAIN/149511.1_5`)


Entscheidungsgründe  Der Magistrat der Stadt Wien, MA 67 lastete mit Strafverfügung vom 10. Juli 2025,  GZ. MA67/MA-GZ/2025, dem nunmehrigen Beschwerdeführer (Bf.), Herrn Bertha Goldhammer  an, er  habe als zur Vertretung nach außen Berufener der Zulassungsbesitzerin (ZLB) des Fahrzeugs  mit dem behördlichen Kennzeichen SW-Kennz. (A), dem ordnungsgemäß zugestellten  Verlangen der Behörde, innerhalb von zwei Wochen ab Zustellung bekanntzugeben, wem das  Fahrzeug überlassen worden war, sodass dieses am 08. April 2025 um 11:07 Uhr in 1220 Wien,  Saltenstraße gegenüber 11 gestanden ist, nicht entsprochen.

| Predicted | Gold |
|---|---|
| `Bertha Goldhammer` | `Bertha Goldhammer` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien, MA 67` (organisation)
- `1220 Wien,  Saltenstraße gegenüber 11` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_2`)


Herrn OSR Jan Passerschroer, MA, geb. am 1960, Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich  2. Reinemut + Smoch Handel, Zachariasweg 4K, 3250 Wieselburg, Österreich   beide vertreten durch HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH, Triesterstraße  14, 2351 Wiener Neudorf,   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und Abs. 2 lit. a und 49 Abs. 1 lit. a FinStrG des Finanzstrafgesetzes  (FinStrG) über die Beschwerden des Beschuldigten und des belangten Verbandes jeweils vom  7. August 2024 gegen das Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als  Finanzstrafbehörde vom 28. Mai 2024, Geschäftszahl SpS-1, in der Sitzung am 10. Dezember  2024 in Anwesenheit der Schriftführerin zu Recht erkannt:  1.

**False Positives:**

- `OSR Jan Passerschroer` — partial — pred is substring of gold: `OSR Jan Passerschroer, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OSR Jan Passerschroer, MA`(person)
- `1960`(date)
- `Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich`(address)
- `Reinemut + Smoch Handel`(organisation)
- `Zachariasweg 4K, 3250 Wieselburg, Österreich`(address)
- `HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH`(organisation)
- `Triesterstraße  14, 2351 Wiener Neudorf`(address)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_15`)


Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22

**False Positives:**

- `OSR Jan Passerschroer` — partial — pred is substring of gold: `OSR Jan Passerschroer, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Amtes für Betrugsbekämpfung als Finanzstrafbehörde`(organisation)
- `OSR Jan Passerschroer, MA`(person)
- `Finanzamts Österreich`(organisation)
- `Reinemut + Smoch Handel`(organisation)
- `72-531/2688`(tax_number)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_86`)


Dieser Bescheid wurde von  Herrn OSR Jan Passerschroer, MA  nicht bekämpft und die Zahllasten wurden am Finanzamtskonto verbucht.

**False Positives:**

- `OSR Jan Passerschroer` — partial — pred is substring of gold: `OSR Jan Passerschroer, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OSR Jan Passerschroer, MA`(person)

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_89`)


3. Feststellungen des Vorsatzes nach § 33 (1) sowie des Vorsatzes und der Wissentlichkeit nach  § 33 (2) a und b FinStrG  Aus den Ausführungen unserer Mandantschaft, insbesondere des Schreibens vom 17.05.2024  an das Amt für Betrugsbekämpfung, geht hervor, dass Herr OSR Jan Passerschroer, MA  zu den Tatzeitpunkten  in einem psychisch instabilen Zustand war.

**False Positives:**

- `OSR Jan Passerschroer` — partial — pred is substring of gold: `OSR Jan Passerschroer, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OSR Jan Passerschroer, MA`(person)

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_92`)


Herr OSR Jan Passerschroer, MA  hat aufgrund seiner  psychischen Instabilität seine Sorgfalt außer Acht gelassen und eine verspätete  Abgabenentrichtung herbeigeführt.

**False Positives:**

- `OSR Jan Passerschroer` — partial — pred is substring of gold: `OSR Jan Passerschroer, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OSR Jan Passerschroer, MA`(person)

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_108`)


Es wurden Finanzstrafverfahren eingeleitet und am 18.7.2023 Strafverfügungen gegen Herrn  OSR Jan Passerschroer, MA  als Erstbeschuldigten und gegen die Firma Reinemut + Smoch Handel  als belangten Verband  erlassen.

**False Positives:**

- `OSR Jan Passerschroer` — partial — pred is substring of gold: `OSR Jan Passerschroer, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OSR Jan Passerschroer, MA`(person)
- `Reinemut + Smoch Handel`(organisation)

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) (sent_id: `findok-manually-annotated_TRAIN/146475.1_152`)


Herr OSR Jan Passerschroer, MA  ist gewillt, alle ihm möglichen Schritte zu setzen um die abgabenrechtliche  Vergangenheit rechtskonform aufzuarbeiten.

**False Positives:**

- `OSR Jan Passerschroer` — partial — pred is substring of gold: `OSR Jan Passerschroer, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OSR Jan Passerschroer, MA`(person)

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/148648.1`) (sent_id: `findok-manually-annotated_TRAIN/148648.1_20`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Im verfahrensgegenständlichen Veranlagungszeitraum 2023 hatte Herr Bernhard Siegmundt  Einkünfte aus  nichtselbständiger Tätigkeit von zwei Dienstgebern:   Im Zeitraum zwischen Jänner und der zweiten Monatshälfte des Juli 2023 (mit einer  kurzen Unterbrechung und dem Bezug von Arbeitslosengeld im Jänner 2023) bezog der  Bf. Einkünfte von der Arbeitgeber NÖ in Adr Arbeitgeber NÖ.

**False Positives:**

- `Bernhard Siegmundt  Einkünfte` — partial — gold is substring of pred: `Bernhard Siegmundt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Bernhard Siegmundt`(person)

</details>

---

## `Frau_Name`

**F1:** 0.006 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `b07361b5`  
**Description:**
Captures full names following 'Frau'.

**Content:**
```
(?:Frau|Frauen)\s+([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+)+)(?=\s+(?:in|von|der|des|\(|$|\d{4}|\s+\d))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.006 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 0 | 313 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/135661.1`) (sent_id: `findok-manually-annotated_TRAIN/135661.1_85`)


Entweder schläft Frau  Reinhold Moellenkamp  bei Herrn A., oder Herr A. bei Frau Reinhold Moellenkamp  in der Schweiz.

| Predicted | Gold |
|---|---|
| `Reinhold Moellenkamp` | `Reinhold Moellenkamp` |

**Missed by this rule (FN):**

- `Schweiz` (country)

</details>

---

## `Herr_Name_Corrected`

**F1:** 0.006 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `98f92f79`  
**Description:**
Captures full names following 'Herr' or 'Herrn', ensuring it matches a name (not a title) and handles German characters.

**Content:**
```
(?:Herr|Herrn)\s+([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+)+)(?=\s+(?:in|von|der|des|\(|$|\d{4}|\s+\d))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.006 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 0 | 171 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/148648.1`) (sent_id: `findok-manually-annotated_TRAIN/148648.1_6`)


Entscheidungsgründe  I. Verfahrensgang  Mit Einkommensteuerbescheid (Arbeitnehmerveranlagung) vom 1. März 2024 wurde die  Einkommensteuer von Herrn Bernhard Siegmundt (im Folgenden auch Beschwerdeführer oder Bf.) für das  Jahr 2023 mit einer Gutschrift in Höhe von EUR 29,- festgesetzt.

| Predicted | Gold |
|---|---|
| `Bernhard Siegmundt` | `Bernhard Siegmundt` |

</details>

---

## `Representative_vertreten_durch`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4913d14d`  
**Description:**
Captures the name of a representative (lawyer/tax advisor) introduced by 'vertreten durch'.

**Content:**
```
(?:vertreten\s+durch\s+)([A-Z][a-zA-Z\.\s,]+?(?:\s+(?:LL\.M\.|M\.B\.L\.|B\.Ed\.|B\.Sc\.|MA|Bakk\.|Dipl\.-|Dipl\.\s+Kfm\.|Ing\.|MedR|VetR|Techn|\u00d6kR|OStR|Univ\.-|Priv\.-|Hon\.-|Dr\.in|Mag\.in|Mag\.a|PhD|LLB|BEd|BA|BSc|DDr\.|R\.in?|R\.)?)(?=,\s+[A-Z]|\s+GmbH|\s+Steuerberatung|\s+OG|\s+KG|\s+Rechtsanwalts|\s+PartG|\s+StbG|\s+\(|$))
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

